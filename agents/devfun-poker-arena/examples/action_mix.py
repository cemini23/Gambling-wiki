"""Hand-stable marginal mixing for postflop call/fold (anti pure-exploit)."""
from __future__ import annotations

import hashlib
import os
from typing import Optional


def mix_postflop_enabled() -> bool:
    raw = os.environ.get("CEMINI_MIX_POSTFLOP", "")
    return raw.lower() in ("1", "true", "yes")


def hand_stable_uniform(table: dict, *, salt: str = "") -> float:
    """Deterministic U(0,1) for this decision point — stable across retries."""
    allowed = table.get("allowedActions") or {}
    parts = [
        str(table.get("tableId") or table.get("id") or ""),
        str(table.get("street") or ""),
        str(table.get("potChips") or ""),
        str(allowed.get("callChips") or ""),
        ",".join(table.get("boardCards") or []),
        salt,
    ]
    sn = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == sn:
            parts.append(",".join(seat.get("holeCards") or []))
            break
    digest = hashlib.sha256("|".join(parts).encode()).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def fold_probability_marginal(
    equity: float,
    pot_odds: float,
    fold_slack: float,
    call_margin: float,
) -> float:
    """1.0 = always fold, 0.0 = always call, (0,1) = mixed band."""
    fold_line = pot_odds - fold_slack
    call_line = pot_odds + call_margin
    if equity < fold_line:
        return 1.0
    if equity >= call_line:
        return 0.0
    span = call_line - fold_line
    if span <= 1e-9:
        return 0.5
    return max(0.0, min(1.0, (call_line - equity) / span))


def resolve_postflop_call_fold(
    table: dict,
    equity: float,
    pot_odds: float,
    fold_slack: float,
    call_margin: float,
    available: list[str],
    *,
    allow_mix: bool = True,
) -> tuple[str, Optional[int]]:
    """Resolve call/fold/check in the marginal equity band with optional mixing."""
    p_fold = fold_probability_marginal(equity, pot_odds, fold_slack, call_margin)

    if p_fold >= 1.0:
        if "fold" in available:
            return "fold", None
    elif p_fold <= 0.0:
        if "call" in available:
            return "call", None
    elif mix_postflop_enabled() and allow_mix:
        roll = hand_stable_uniform(table, salt="postflop_cf")
        choice = "fold" if roll < p_fold else "call"
        if choice in available:
            return choice, None

    # Mix off: preserve legacy tie-break in the marginal band (fold unless clear call).
    if equity >= pot_odds + call_margin and "call" in available:
        return "call", None
    if "check" in available:
        return "check", None
    if "fold" in available:
        return "fold", None
    return ("call" if "call" in available else "fold"), None
