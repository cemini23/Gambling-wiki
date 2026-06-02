"""Cemini / gambling-wiki dev.fun Poker Arena agent.

Layers on arena-pokerkit L1:
  1. Auto Research — preflop chart (research_static_chart)
  2. Skill binding stub — street/hand-class labels in reasoning (PokerSkill pattern)
  3. Equity + pot-odds postflop (treys MC from agent.py)
  4. Hard deadline fallbacks (check > fold)

Run:
  uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 20
  uv run examples/agent.py --agent examples/cemini_decide.py --competition-id <id>
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import (  # noqa: E402
    _build,
    _build_reasoning,
    _hand_class,
    estimate_equity,
)
from research_static_chart import research_static_chart  # noqa: E402


def retrieve_solver_context(table: dict) -> dict:
    """Preflop chart + PokerSkill-style binding labels for decide()."""
    ctx = research_static_chart(table)
    hole = ctx.get("hole") or []
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop").lower()
    hc = _hand_class(hole)
    ctx["skill_binding"] = {
        "street": street,
        "hand_class": hc or "unknown",
        "board_len": len(board),
        "scenario": _scenario_label(street, board, hc),
    }
    return ctx


def _scenario_label(street: str, board: list[str], hc: str) -> str:
    if street == "preflop":
        return "open_defend" if hc else "preflop_unknown"
    if len(board) >= 3:
        suits = [c[-1].lower() for c in board if c]
        if suits and max(suits.count(s) for s in set(suits)) >= 2:
            return "wet_board_pot_control"
    return "dry_board_value"


def decide(
    table: dict,
    deadline_s: float = 10.0,
    research_context: Optional[dict] = None,
) -> dict:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    ctx = research_context or {}

    if deadline_s < 2.0:
        if allowed.get("canCheck"):
            return _build("check", None, table, allowed, eq=0.5, po=0.0,
                          msg="clock pressure — free check")
        return _build("fold", None, table, allowed, eq=0.0, po=1.0,
                      msg="clock pressure — fold")

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop")

    pot = int(table.get("potChips") or 0)
    call_chips = int(allowed.get("callChips") or 0)
    pot_odds = call_chips / max(pot + call_chips, 1) if call_chips else 0.0
    equity = estimate_equity(hole, board, sims=300, deadline_s=deadline_s)

    chart = ctx.get("preflop_chart") or {}
    suggested = chart.get("suggested_action")
    binding = (ctx.get("skill_binding") or {}).get("scenario", "unknown")

    action_name: str
    amount: Optional[int] = None

    if street == "Preflop" and suggested and call_chips == 0:
        action_name, amount = _preflop_open(
            suggested, allowed, available, pot, equity)
    elif street == "Preflop" and suggested and call_chips > 0:
        action_name, amount = _preflop_vs_bet(
            suggested, chart, allowed, available, equity, pot_odds, call_chips, pot)
    elif call_chips == 0:
        action_name, amount = _postflop_free(
            equity, allowed, available, pot)
    else:
        action_name, amount = _postflop_facing_bet(
            equity, pot_odds, allowed, available, call_chips, pot)

    if action_name in ("fold", "check", "call"):
        amount = None

    msg = _message(action_name, equity, pot_odds, binding, suggested)
    out = _build(action_name, amount, table, allowed, eq=equity, po=pot_odds, msg=msg)
    out["reasoning"] = _skill_reasoning(
        out.get("reasoning", ""), binding, suggested, chart)
    return out


def _preflop_open(suggested: str, allowed: dict, available: list,
                  pot: int, equity: float) -> tuple[str, Optional[int]]:
    if suggested == "raise" and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.55), max_bet))
        return "bet", target
    if suggested == "fold" and "fold" in available:
        return "fold", None
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _preflop_vs_bet(suggested: str, chart: dict, allowed: dict, available: list,
                    equity: float, pot_odds: float, call_chips: int,
                    pot: int) -> tuple[str, Optional[int]]:
    hc = chart.get("hand_class") or ""
    premium = hc in {"AA", "KK", "QQ", "AKs", "AKo"}
    if suggested == "raise" and premium and allowed.get("canRaise"):
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2.5), max_r))
        return "raise", target
    if equity >= pot_odds + 0.03 and "call" in available:
        return "call", None
    if suggested == "fold" or equity < pot_odds - 0.08:
        return ("fold" if "fold" in available else "call"), None
    return ("call" if "call" in available else "fold"), None


def _postflop_free(equity: float, allowed: dict, available: list,
                   pot: int) -> tuple[str, Optional[int]]:
    if equity > 0.72 and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.33), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.66), max_bet))
        return "bet", target
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _postflop_facing_bet(equity: float, pot_odds: float, allowed: dict,
                         available: list, call_chips: int,
                         pot: int) -> tuple[str, Optional[int]]:
    if equity < pot_odds - 0.06 and "fold" in available:
        return "fold", None
    if equity > 0.82 and allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2), max_r))
        return "raise", target
    if equity >= pot_odds + 0.04 and "call" in available:
        return "call", None
    if "check" in available:
        return "check", None
    return ("fold" if "fold" in available else "call"), None


def _message(action: str, equity: float, pot_odds: float,
             binding: str, suggested: Optional[str]) -> str:
    eq = int(round(equity * 100))
    if action == "fold":
        return f"{binding}: equity {eq}% short of price, folding"
    if action == "check":
        return f"{binding}: free card, equity {eq}%"
    if action == "call":
        return f"{binding}: calling — equity covers pot odds"
    if suggested and action in ("bet", "raise"):
        return f"chart says {suggested}; executing {action} for value"
    return f"{binding}: {action} with {eq}% equity"


def _skill_reasoning(base: str, binding: str, suggested: Optional[str],
                     chart: dict) -> str:
    """Append skill tag within 150-char YAML cap."""
    pos = chart.get("position") or "?"
    tag = f'sk: "{binding}@{pos}"'
    if suggested:
        tag = f'sk: "{binding}|{suggested}@{pos}"'
    if len(base) + len(tag) + 2 <= 150:
        return base[:-1] + f", {tag}}}" if base.endswith("}") else f"{{{tag}}}"
    return base[:150]
