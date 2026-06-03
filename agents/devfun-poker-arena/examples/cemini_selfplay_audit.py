#!/usr/bin/env python3
"""Self-play KPI audit for cemini decide() — catches VPIP / EP leaks pytest misses.

The starter kit tests `examples/agent.py` (skeleton), not your custom decide(),
and HU scenarios hide 6-max position + HUD paths. This script runs offline
6-max self-play with `--training-hud`, records hero decisions, and optionally
**gates** deploy when KPIs drift.

Usage:
    uv run python examples/cemini_selfplay_audit.py
    uv run python examples/cemini_selfplay_audit.py --gate
    uv run python examples/cemini_selfplay_audit.py --hands 800 --seed 42 --gate

Exit 0 = pass (or report-only). Exit 1 = gate failed.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from position_utils import hero_position_label  # noqa: E402
from selfplay import run_selfplay, _load_decide_from_path  # noqa: E402


@dataclass
class HeroAudit:
    preflop_seen: int = 0
    vpip: int = 0
    pfr: int = 0
    ep_opportunities: int = 0
    ep_trash_raises: int = 0
    by_position: Counter = field(default_factory=Counter)
    vpip_by_position: Counter = field(default_factory=Counter)
    trash_hands_opened: list[str] = field(default_factory=list)
    _vpip_hands: set[str] = field(default_factory=set)
    _pfr_hands: set[str] = field(default_factory=set)
    _counted_hands: set[str] = field(default_factory=set)
    _ep_opp_hands: set[str] = field(default_factory=set)

    _TRASH = frozenset({
        "72o", "73o", "74o", "75o", "76o", "82o", "83o", "84o", "85o",
        "92o", "93o", "94o", "95o", "96o", "J2o", "J3o", "J4o", "Q2o",
        "K2o", "K3o", "K4o", "T2o", "T3o", "32o", "42o", "52o", "62o",
    })

    def record(self, table: dict, action: dict) -> None:
        street = (table.get("street") or "").lower()
        if street != "preflop":
            return

        hand_key = str(table.get("tableId") or table.get("id") or "")
        if not hand_key:
            return

        act = (action.get("action") or "").lower()
        pos = hero_position_label(table)
        allowed = table.get("allowedActions") or {}
        call_chips = int(allowed.get("callChips") or 0)
        bb = int(table.get("bigBlindChips") or 20)
        sb = int(table.get("smallBlindChips") or 10)
        facing_raise = call_chips > bb

        # One VPIP/PFR sample per hand (first hero preflop decision).
        if hand_key in self._counted_hands:
            return

        self._counted_hands.add(hand_key)
        self.preflop_seen += 1
        self.by_position[pos] += 1

        seats = table.get("seats") or []
        sn = table.get("selfSeatNumber")
        hero = next((s for s in seats if s.get("seatNumber") == sn), {})
        hole = hero.get("holeCards") or []
        if len(hole) == 2:
            from agent import _hand_class  # noqa: WPS433

            hc = _hand_class(list(hole)) or ""
        else:
            hc = ""

        if act in ("bet", "raise", "all-in"):
            self._vpip_hands.add(hand_key)
            self.vpip += 1
            self.vpip_by_position[pos] += 1
            if not facing_raise:
                self._pfr_hands.add(hand_key)
                self.pfr += 1
                if pos in ("UTG", "MP") and hc in self._TRASH:
                    self.ep_trash_raises += 1
                    self.trash_hands_opened.append(f"{hc}@{pos}")
        elif act == "call":
            # BB check behind unopened pot is not VPIP; SB complete is.
            is_bb_free = pos == "BB" and call_chips == 0
            if not is_bb_free:
                self._vpip_hands.add(hand_key)
                self.vpip += 1
                self.vpip_by_position[pos] += 1

        if pos in ("UTG", "MP") and not facing_raise and hand_key not in self._ep_opp_hands:
            self._ep_opp_hands.add(hand_key)
            self.ep_opportunities += 1


def _wrap_decide(fn: Callable, audit: HeroAudit) -> Callable:
    def wrapped(table: dict, **kwargs: Any) -> dict:
        action = fn(table, **kwargs)
        if isinstance(action, dict):
            audit.record(table, action)
        return action

    return wrapped


@dataclass(frozen=True)
class GateThresholds:
    max_ep_vpip: float = 0.22
    max_ep_trash_raises: int = 0
    min_bb_per_100_rock: float = -25.0
    min_bb_per_100_maniac: float = -40.0


def _rate(num: int, den: int) -> float:
    return num / den if den else 0.0


def run_audit(
    *,
    hands: int,
    players: int,
    seed: Optional[int],
    gate: bool,
    thresholds: GateThresholds,
) -> int:
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw_decide = _load_decide_from_path(str(decide_path))
    audit = HeroAudit()
    decide_fn = _wrap_decide(raw_decide, audit)

    os.environ.setdefault("TRAINING_OPPONENT_MODE", "rock")
    rock = run_selfplay(
        decide_fn=decide_fn,
        n_hands=hands,
        opponent_label="rock",
        n_players=players,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed,
        training_hud=True,
    )

    audit2 = HeroAudit()
    decide_fn2 = _wrap_decide(raw_decide, audit2)
    os.environ["TRAINING_OPPONENT_MODE"] = "maniac"
    maniac = run_selfplay(
        decide_fn=decide_fn2,
        n_hands=hands,
        opponent_label="maniac",
        n_players=players,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=(seed + 1) if seed is not None else None,
        training_hud=True,
    )

    # Merge audits (both runs contribute to VPIP picture)
    merged = HeroAudit(
        preflop_seen=audit.preflop_seen + audit2.preflop_seen,
        vpip=audit.vpip + audit2.vpip,
        pfr=audit.pfr + audit2.pfr,
        ep_opportunities=audit.ep_opportunities + audit2.ep_opportunities,
        ep_trash_raises=audit.ep_trash_raises + audit2.ep_trash_raises,
        by_position=audit.by_position + audit2.by_position,
        vpip_by_position=audit.vpip_by_position + audit2.vpip_by_position,
        trash_hands_opened=audit.trash_hands_opened + audit2.trash_hands_opened,
    )

    vpip_rate = _rate(merged.vpip, merged.preflop_seen)
    pfr_rate = _rate(merged.pfr, merged.preflop_seen)
    ep_seen = merged.by_position.get("UTG", 0) + merged.by_position.get("MP", 0)
    ep_vpip = merged.vpip_by_position.get("UTG", 0) + merged.vpip_by_position.get("MP", 0)
    ep_vpip_rate = _rate(ep_vpip, ep_seen)

    sep = "─" * 58
    print(sep)
    print(f"  cemini self-play audit  ({hands} hands × rock + maniac, {players}-max)")
    print(f"  seed={seed}  training-hud=ON")
    print(sep)
    print(f"  VPIP (all)  : {vpip_rate:.1%}  ({merged.vpip}/{merged.preflop_seen})")
    print(f"  VPIP (EP)   : {ep_vpip_rate:.1%}  ({ep_vpip}/{ep_seen})  ← gate metric")
    print(f"  PFR         : {pfr_rate:.1%}  ({merged.pfr}/{merged.preflop_seen})")
    print(f"  EP trash opens: {merged.ep_trash_raises}  {merged.trash_hands_opened[:5]}")
    print(f"  bb/100 rock : {rock['bb_per_100']:+.1f}")
    print(f"  bb/100 maniac: {maniac['bb_per_100']:+.1f}")
    print("  VPIP by seat:")
    for pos in ("UTG", "MP", "CO", "BTN", "SB", "BB"):
        seen = merged.by_position.get(pos, 0)
        vp = merged.vpip_by_position.get(pos, 0)
        if seen:
            print(f"    {pos:3s}  {_rate(vp, seen):.1%}  ({vp}/{seen})")
    print(sep)

    failures: list[str] = []
    if ep_vpip_rate > thresholds.max_ep_vpip:
        failures.append(
            f"EP VPIP {ep_vpip_rate:.1%} > max {thresholds.max_ep_vpip:.1%}"
        )
    if merged.ep_trash_raises > thresholds.max_ep_trash_raises:
        failures.append(
            f"EP trash opens {merged.ep_trash_raises} > {thresholds.max_ep_trash_raises}"
        )
    if rock["bb_per_100"] < thresholds.min_bb_per_100_rock:
        failures.append(
            f"bb/100 vs rock {rock['bb_per_100']:+.1f} < {thresholds.min_bb_per_100_rock:+.1f}"
        )
    if maniac["bb_per_100"] < thresholds.min_bb_per_100_maniac:
        failures.append(
            f"bb/100 vs maniac {maniac['bb_per_100']:+.1f} < "
            f"{thresholds.min_bb_per_100_maniac:+.1f}"
        )

    if failures:
        print("  GATE FAIL:")
        for f in failures:
            print(f"    • {f}")
        if gate:
            return 1
    elif gate:
        print("  GATE PASS")
    else:
        print("  (report only — pass `--gate` to enforce thresholds on deploy)")

    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Cemini self-play KPI audit")
    p.add_argument("--hands", type=int, default=400, help="Hands per opponent profile")
    p.add_argument("--players", type=int, default=6)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gate", action="store_true", help="Exit 1 if KPI thresholds fail")
    p.add_argument("--max-ep-vpip", type=float, default=GateThresholds.max_ep_vpip)
    p.add_argument("--min-bb-rock", type=float, default=GateThresholds.min_bb_per_100_rock)
    p.add_argument("--min-bb-maniac", type=float, default=GateThresholds.min_bb_per_100_maniac)
    args = p.parse_args(argv)

    th = GateThresholds(
        max_ep_vpip=args.max_ep_vpip,
        min_bb_per_100_rock=args.min_bb_rock,
        min_bb_per_100_maniac=args.min_bb_maniac,
    )
    return run_audit(
        hands=args.hands,
        players=args.players,
        seed=args.seed,
        gate=args.gate,
        thresholds=th,
    )


if __name__ == "__main__":
    sys.exit(main())
