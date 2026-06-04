#!/usr/bin/env python3
"""Deep pre-deploy audit for anti-profiling (sanitize + postflop mix).

Validates prod defense does not regress Playground leak guards or KPI gates.

Usage:
    uv run python examples/cemini_anti_profiling_audit.py
    uv run python examples/cemini_anti_profiling_audit.py --gate
"""
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import decide  # noqa: E402
from output_sanitize import FALLBACK_REASONING, maybe_sanitize_action  # noqa: E402
from selfplay import run_selfplay, _load_decide_from_path  # noqa: E402

ROOT = _EXAMPLES.parent
sys.path.insert(0, str(ROOT))
from tests.fixtures.regression_spots import regression_spots  # noqa: E402


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str = ""


def _set_env(key: str, value: Optional[str]) -> None:
    if value is None:
        os.environ.pop(key, None)
    else:
        os.environ[key] = value


def _run_spot(
    spot_table: dict,
    *,
    mix: bool,
    deadline: float = 10.0,
    sanitize: bool = False,
) -> dict:
    _set_env("CEMINI_MIX_POSTFLOP", "1" if mix else "0")
    _set_env("CEMINI_SANITIZE_OUTPUT", "1" if sanitize else "0")
    return decide(spot_table, deadline_s=deadline)


def _check_spot_constraints(spot, out: dict) -> Optional[str]:
    legal = set(spot.table["allowedActions"]["availableActions"])
    act = out["action"]
    if act not in legal:
        return f"illegal action {act!r} legal={sorted(legal)}"
    if spot.forbidden and act in spot.forbidden:
        return f"forbidden {act!r} — {spot.notes}"
    if spot.required and act not in spot.required:
        return f"expected one of {sorted(spot.required)}, got {act!r}"
    if len(out.get("reasoning", "")) > 150:
        return f"reasoning too long ({len(out['reasoning'])})"
    return None


def check_regression_baseline_vs_mix_off() -> CheckResult:
    """Mix OFF must match frozen baseline actions (no behavior drift)."""
    baseline: dict[str, str] = {}
    for spot in regression_spots():
        out = _run_spot(spot.table, mix=False)
        err = _check_spot_constraints(spot, out)
        if err:
            return CheckResult("regression_mix_off", False, f"{spot.id}: {err}")
        baseline[spot.id] = out["action"]

    for spot in regression_spots():
        out = _run_spot(spot.table, mix=False)
        if out["action"] != baseline[spot.id]:
            return CheckResult(
                "regression_mix_off_stable",
                False,
                f"{spot.id}: {baseline[spot.id]!r} -> {out['action']!r}",
            )
    return CheckResult("regression_mix_off", True, f"{len(baseline)} spots OK")


def check_regression_mix_on_forbidden(*, repeats: int = 8) -> CheckResult:
    """Mix ON must never violate forbidden/required on prod leak spots (MC-stable)."""
    failures: list[str] = []
    for spot in regression_spots():
        for rep in range(repeats):
            out = _run_spot(spot.table, mix=True)
            err = _check_spot_constraints(spot, out)
            if err:
                failures.append(f"{spot.id}[{rep}]: {err}")
                break
    if failures:
        return CheckResult("regression_mix_on", False, "; ".join(failures[:5]))
    n = len(regression_spots()) * repeats
    return CheckResult("regression_mix_on", True, f"{n} spot-runs OK")


def check_scan_behaviors_mix_on() -> CheckResult:
    """Personality/survival behaviors under prod mix flag."""
    from tests.helpers.cemini_tables import ep_oop_postflop_weak, six_max_table, _allowed
    from cemini_decide import retrieve_solver_context

    _set_env("CEMINI_MIX_POSTFLOP", "1")

    # Clear -EV: 72o on AKQ — MC variance cannot justify a call.
    table = ep_oop_postflop_weak(
        ["7c", "2d"], ["Ah", "Kc", "Qs"], hero_seat=2, villain_bet=60, pot=120,
    )
    for i in range(30):
        out = decide(table, deadline_s=3.0)
        if out["action"] not in ("fold", "check"):
            return CheckResult(
                "composure_mix_on",
                False,
                f"72o AKQ deadline 3s got {out['action']!r} (run {i})",
            )

    table2 = ep_oop_postflop_weak(
        ["Qc", "Jd"], ["Ah", "8s", "3c"], hero_seat=5, villain_bet=80, pot=160,
    )
    ctx = retrieve_solver_context(table2)
    ctx["survival_mode"] = True
    ctx["qualification_protect"] = True
    out2 = decide(table2, deadline_s=10.0, research_context=ctx)
    if out2["action"] not in ("fold", "check"):
        return CheckResult(
            "survival_mix_on",
            False,
            f"survival got {out2['action']!r}",
        )

    candor = six_max_table(
        name="candor_beat",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["Ah", "Kd", "9s", "4c"],
        pot=200,
        hero_hole=["7c", "2d"],
        hero_stack=900,
        villain_bets={3: 120},
        stacks={5: 900},
        allowed=_allowed(
            can_call=True, can_raise=True, call_chips=120, call_to=120,
            raise_range={"min": 240, "max": 900},
        ),
    )
    out3 = decide(candor, deadline_s=10.0)
    if out3["action"] != "fold":
        return CheckResult("candor_mix_on", False, f"expected fold got {out3['action']!r}")

    return CheckResult("scan_behaviors_mix_on", True, "composure/survival/candor OK")


def check_sanitize_preserves_action() -> CheckResult:
    _set_env("CEMINI_SANITIZE_OUTPUT", "1")
    for spot in regression_spots():
        raw = _run_spot(spot.table, mix=False, sanitize=False)
        _set_env("CEMINI_SANITIZE_OUTPUT", "1")
        sanitized = maybe_sanitize_action(raw)
        if sanitized["action"] != raw["action"]:
            return CheckResult(
                "sanitize_action",
                False,
                f"{spot.id}: {raw['action']!r} -> {sanitized['action']!r}",
            )
        if sanitized.get("amount") != raw.get("amount"):
            return CheckResult(
                "sanitize_amount",
                False,
                f"{spot.id}: amount changed",
            )
        if sanitized["reasoning"] != FALLBACK_REASONING:
            return CheckResult("sanitize_reasoning", False, spot.id)
        if "survival" in sanitized["message"].lower() or "@" in sanitized["message"]:
            return CheckResult("sanitize_message", False, spot.id)
    return CheckResult("sanitize", True, f"{len(regression_spots())} spots OK")


def check_selfplay_ab(*, hands: int, seed: int, max_bb_delta: float) -> CheckResult:
    """Prod mix ON must stay within bb/100 of mix OFF on rock + maniac."""
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw = _load_decide_from_path(str(decide_path))

    def _bb(mix: bool, opp: str, run_seed: int) -> float:
        _set_env("CEMINI_MIX_POSTFLOP", "1" if mix else "0")
        _set_env("CEMINI_SANITIZE_OUTPUT", "0")
        os.environ["TRAINING_OPPONENT_MODE"] = opp
        r = run_selfplay(
            decide_fn=raw,
            n_hands=hands,
            opponent_label=opp,
            n_players=6,
            starting_stack=500,
            small_blind=10,
            big_blind=20,
            seed=run_seed,
            training_hud=True,
        )
        return float(r["bb_per_100"])

    off_rock = _bb(False, "rock", seed)
    on_rock = _bb(True, "rock", seed)
    off_maniac = _bb(False, "maniac", seed + 1)
    on_maniac = _bb(True, "maniac", seed + 1)

    d_rock = abs(on_rock - off_rock)
    d_maniac = abs(on_maniac - off_maniac)
    detail = (
        f"rock off={off_rock:+.1f} on={on_rock:+.1f} Δ={d_rock:.1f}; "
        f"maniac off={off_maniac:+.1f} on={on_maniac:+.1f} Δ={d_maniac:.1f}"
    )
    if d_rock > max_bb_delta or d_maniac > max_bb_delta * 2:
        return CheckResult("selfplay_ab", False, detail)
    return CheckResult("selfplay_ab", True, detail)


def check_prod_env_selfplay_gate(*, hands: int, seed: int) -> CheckResult:
    """Run KPI gates with prod-like env; use preflight hand count (250) for stability."""
    from cemini_selfplay_audit import GateThresholds, run_audit

    _set_env("CEMINI_MIX_POSTFLOP", "1")
    _set_env("CEMINI_SANITIZE_OUTPUT", "1")
    gate_hands = min(hands, 250)
    rc = run_audit(
        hands=gate_hands,
        players=6,
        seed=seed,
        gate=True,
        thresholds=GateThresholds(),
    )
    if rc != 0:
        return CheckResult(
            "prod_env_kpi_gate",
            False,
            f"cemini_selfplay_audit --gate failed ({gate_hands} hands)",
        )
    return CheckResult("prod_env_kpi_gate", True, f"{gate_hands} hands rock+maniac gated")


def run_all(*, gate: bool, hands: int, seed: int) -> int:
    checks: list[CheckResult] = [
        check_regression_baseline_vs_mix_off(),
        check_regression_mix_on_forbidden(),
        check_scan_behaviors_mix_on(),
        check_sanitize_preserves_action(),
        check_selfplay_ab(hands=hands, seed=seed, max_bb_delta=12.0),
        check_prod_env_selfplay_gate(hands=hands, seed=seed),
    ]

    print("═" * 60)
    print("  cemini anti-profiling deep audit")
    print("═" * 60)
    failed = 0
    for c in checks:
        mark = "PASS" if c.ok else "FAIL"
        print(f"  [{mark}] {c.name}: {c.detail}")
        if not c.ok:
            failed += 1
    print("═" * 60)
    if failed:
        print(f"  {failed} check(s) FAILED — do not deploy")
        return 1 if gate else 0
    print("  ALL CHECKS PASSED — safe to deploy anti-profiling layer")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Deep audit for anti-profiling deploy")
    p.add_argument("--gate", action="store_true", help="Exit 1 on any failure")
    p.add_argument("--hands", type=int, default=400, help="Self-play hands per profile")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args(argv)
    try:
        return run_all(gate=args.gate, hands=args.hands, seed=args.seed)
    finally:
        _set_env("CEMINI_MIX_POSTFLOP", None)
        _set_env("CEMINI_SANITIZE_OUTPUT", None)


if __name__ == "__main__":
    sys.exit(main())
