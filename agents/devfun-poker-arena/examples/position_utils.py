"""Derive 6-max (and shorter) position labels from Arena table state.

Prefers explicit API fields (`buttonSeatNumber`, `seat.position`). Falls back
to blind-post inference from `currentBetChips` + `smallBlindChips` /
`bigBlindChips` so rotated buttons work in selfplay and live Arena.
"""
from __future__ import annotations

from typing import Optional

_VALID_POSITIONS = frozenset({"UTG", "MP", "CO", "BTN", "SB", "BB"})

# Clockwise distance from button for N active players.
_POS_BY_PLAYER_COUNT: dict[int, list[str]] = {
    2: ["BTN", "BB"],
    3: ["BTN", "SB", "BB"],
    4: ["BTN", "SB", "BB", "CO"],
    5: ["BTN", "SB", "BB", "UTG", "CO"],
    6: ["BTN", "SB", "BB", "UTG", "MP", "CO"],
}

# Legacy canonical seating when blind inference fails (seat 1 = BTN).
_SEAT_TO_POS_6MAX = {1: "BTN", 2: "SB", 3: "BB", 4: "UTG", 5: "MP", 6: "CO"}


def _active_seat_numbers(table: dict) -> list[int]:
    seats = table.get("seats") or []
    nums: list[int] = []
    for s in seats:
        if not isinstance(s, dict):
            continue
        status = (s.get("status") or "Active").lower()
        if status in ("folded", "out", "empty"):
            continue
        num = s.get("seatNumber")
        if num is not None:
            nums.append(int(num))
    return sorted(set(nums))


def infer_button_seat(table: dict) -> Optional[int]:
    """Return dealer/button seat number, or None if unknown."""
    for key in ("buttonSeatNumber", "dealerSeatNumber", "buttonSeat", "dealerSeat"):
        val = table.get(key)
        if val is not None:
            try:
                return int(val)
            except (TypeError, ValueError):
                pass

    sb = int(table.get("smallBlindChips") or 0)
    bb = int(table.get("bigBlindChips") or 0)
    if sb <= 0 or bb <= 0:
        return None

    seat_nums = _active_seat_numbers(table)
    if len(seat_nums) < 2:
        return None

    seats = {int(s["seatNumber"]): s for s in (table.get("seats") or [])
             if isinstance(s, dict) and s.get("seatNumber") is not None}

    sb_seat: Optional[int] = None
    bb_seat: Optional[int] = None
    for num in seat_nums:
        bet = int(seats.get(num, {}).get("currentBetChips") or 0)
        if bet == sb:
            sb_seat = num
        elif bet == bb:
            bb_seat = num

    anchor = sb_seat
    if anchor is None and bb_seat is not None:
        bb_idx = seat_nums.index(bb_seat)
        anchor = seat_nums[(bb_idx - 1) % len(seat_nums)]
    if anchor is None:
        return None

    anchor_idx = seat_nums.index(anchor)
    return seat_nums[(anchor_idx - 1) % len(seat_nums)]


def hero_position_label(table: dict) -> str:
    """Map hero seat to UTG/MP/CO/BTN/SB/BB."""
    self_num = table.get("selfSeatNumber")
    if self_num is None:
        return "MP"

    seats = table.get("seats") or []
    for s in seats:
        if s.get("seatNumber") == self_num:
            pos = s.get("position")
            if isinstance(pos, str) and pos.upper() in _VALID_POSITIONS:
                return pos.upper()
            break

    seat_nums = _active_seat_numbers(table)
    if not seat_nums or int(self_num) not in seat_nums:
        return _SEAT_TO_POS_6MAX.get(int(self_num), "MP")

    btn = infer_button_seat(table)
    if btn is None or btn not in seat_nums:
        return _SEAT_TO_POS_6MAX.get(int(self_num), "MP")

    n = len(seat_nums)
    labels = _POS_BY_PLAYER_COUNT.get(n, _POS_BY_PLAYER_COUNT[6])
    dist = (seat_nums.index(int(self_num)) - seat_nums.index(btn)) % n
    if dist < len(labels):
        return labels[dist]
    return "MP"


def hero_is_in_position(table: dict) -> bool:
    """True when hero has a late-seat / button-adjacent label (IP heuristic)."""
    return hero_position_label(table) in {"BTN", "CO"}
