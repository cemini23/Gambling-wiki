"""Blind-orbit cost estimates for Playground chip preservation."""
from __future__ import annotations

DEFAULT_SB = 10
DEFAULT_BB = 20
DEFAULT_PLAYERS = 6


def blind_orbit_chips(table: dict | None = None) -> int:
    """Chips posted per full table orbit (one SB + one BB)."""
    if table:
        sb = int(table.get("smallBlindChips") or DEFAULT_SB)
        bb = int(table.get("bigBlindChips") or DEFAULT_BB)
        return sb + bb
    return DEFAULT_SB + DEFAULT_BB


def avg_blind_tax_per_hand(table: dict | None = None, *, players: int = DEFAULT_PLAYERS) -> float:
    """Expected blind chips lost per hand if never entering pots (6-max heuristic)."""
    return blind_orbit_chips(table) / max(players, 2)


def hands_to_erosion(buffer_chips: int, table: dict | None = None) -> int:
    """Hands of pure blind fold before buffer chips erode to zero."""
    tax = avg_blind_tax_per_hand(table)
    if tax <= 0:
        return 0
    return int(buffer_chips / tax)


# BTN/CO min-steal sets while lead-protect is on — chart-approved pressure, not maniac widens.
_BTN_LEAD_STEAL = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT",
    "A2s", "A3s", "A4s", "A5s", "A6s", "A7s", "A8s", "A9s", "ATs", "AJs", "AQs", "AKs",
    "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "QJs", "QTs", "JTs", "T9s",
})

_CO_LEAD_STEAL = frozenset({
    "55", "66", "77", "88", "99", "TT",
    "A9s", "ATs", "AJs", "AQs", "AKs", "ATo", "AJo", "AQo", "AKo",
    "KJs", "KTs", "KQs", "QJs", "JTs",
})


def lead_blind_steal(hand_class: str, position: str) -> bool:
    """True when lead-protect should still open to recapture blind decay."""
    if position == "BTN":
        return hand_class in _BTN_LEAD_STEAL
    if position == "CO":
        return hand_class in _CO_LEAD_STEAL
    return False
