"""Spot-aware opponent targeting for multi-way tables (2–6 seats).

Public helpers — no exploit constants. Used by opponent HUD to pick which
villain profile drives margins on this decision.
"""
from __future__ import annotations

from typing import Any, Optional


def _active_seats(table: dict, *, hero: bool = True) -> list[dict]:
    self_num = table.get("selfSeatNumber")
    out: list[dict] = []
    for seat in table.get("seats") or []:
        if not isinstance(seat, dict):
            continue
        status = (seat.get("status") or "Active").lower()
        if status in ("folded", "out", "empty", "sitting_out"):
            continue
        if not hero and seat.get("seatNumber") == self_num:
            continue
        out.append(seat)
    return out


def active_villain_count(table: dict) -> int:
    return len(_active_seats(table, hero=False))


def is_multiway(table: dict) -> bool:
    return active_villain_count(table) >= 2


def seat_agent_id(table: dict, seat_number: int) -> Optional[str]:
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == seat_number:
            aid = seat.get("agentId")
            return str(aid) if aid else None
    return None


def seat_training_archetype(seat: dict) -> Optional[str]:
    """Local self-play may tag seats with trainingArchetype."""
    arch = seat.get("trainingArchetype") or seat.get("archetype")
    if isinstance(arch, str) and arch.strip():
        return arch.strip().lower()
    return None


def call_chips(table: dict) -> int:
    allowed = table.get("allowedActions") or {}
    return int(allowed.get("callChips") or 0)


def spot_kind(table: dict) -> str:
    """unopened | facing_bet | facing_raise (heuristic)."""
    cc = call_chips(table)
    if cc <= 0:
        return "unopened"
    bb = int(table.get("bigBlindChips") or 0)
    allowed = table.get("allowedActions") or {}
    if allowed.get("canRaise") and cc > max(bb, 1):
        return "facing_raise"
    return "facing_bet"


def _aggressor_from_action_history(table: dict) -> Optional[int]:
    """Arena may supply actionHistory — use last bet/raise on current street."""
    street = (table.get("street") or "Preflop").lower()
    history = table.get("actionHistory") or table.get("actions") or []
    last_seat: Optional[int] = None
    for entry in history:
        if not isinstance(entry, dict):
            continue
        est = (entry.get("street") or entry.get("phase") or "").lower()
        if est and est != street:
            continue
        act = (entry.get("action") or entry.get("type") or "").lower()
        if act not in ("bet", "raise", "all-in", "allin", "all_in"):
            continue
        seat = entry.get("seatNumber") or entry.get("seat")
        if seat is not None:
            last_seat = int(seat)
    return last_seat


def last_aggressor_seat(table: dict) -> Optional[int]:
    """Seat number of villain we're most directly responding to."""
    explicit = table.get("lastAggressorSeatNumber") or table.get("lastAggressorSeat")
    if explicit is not None:
        try:
            return int(explicit)
        except (TypeError, ValueError):
            pass

    from_history = _aggressor_from_action_history(table)
    if from_history is not None:
        self_num = table.get("selfSeatNumber")
        if from_history != self_num:
            return from_history

    # Fallback: highest current street wager among active villains.
    self_num = table.get("selfSeatNumber")
    villains = _active_seats(table, hero=False)
    if not villains:
        return None
    max_bet = max(int(s.get("currentBetChips") or 0) for s in villains)
    if max_bet <= 0:
        return None
    candidates = [
        int(s["seatNumber"])
        for s in villains
        if int(s.get("currentBetChips") or 0) == max_bet and s.get("seatNumber") is not None
    ]
    if len(candidates) == 1:
        return candidates[0]
    # Tie-break: latest seat clockwise from button (approx — prefer higher seat #).
    return max(candidates) if candidates else None


def select_target_agent_id(table: dict) -> tuple[Optional[str], str, dict[str, Any]]:
    """Return (agent_id, reason, meta) for HUD profile lookup."""
    meta: dict[str, Any] = {
        "activeVillains": active_villain_count(table),
        "multiway": is_multiway(table),
        "spot": spot_kind(table),
        "playersAtTable": len(_active_seats(table, hero=True)),
    }
    spot = meta["spot"]

    if spot in ("facing_bet", "facing_raise"):
        ag = last_aggressor_seat(table)
        if ag is not None:
            aid = seat_agent_id(table, ag)
            meta["aggressorSeat"] = ag
            if aid:
                return aid, "last_aggressor", meta
            # Training seats may only have archetype tags.
            for seat in table.get("seats") or []:
                if seat.get("seatNumber") == ag:
                    arch = seat_training_archetype(seat)
                    if arch:
                        meta["aggressorArchetype"] = arch
                        return None, "last_aggressor_archetype", meta

    # Unopened pot — steal / iso: prefer softest villain still in (rock).
    villains = _active_seats(table, hero=False)
    rocks = [s for s in villains if seat_training_archetype(s) == "rock"]
    if rocks and spot == "unopened":
        seat = rocks[0]
        aid = seat.get("agentId")
        meta["stealTargetSeat"] = seat.get("seatNumber")
        if aid:
            return str(aid), "steal_vs_rock", meta

    # Table aggregate fallback — caller picks maniac > rock > first profile.
    return None, "table_aggregate", meta
