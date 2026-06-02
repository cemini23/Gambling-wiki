"""Seat archetype layouts for mixed training tables (2–6 seats).

Templates are 6-tuple: index 0 = hero seat (unused for bot/HUD tags),
indices 1..5 = villain seats in table order (selfplay seatNumber 2..6).
"""
from __future__ import annotations

from typing import Optional

# Hero slot (index 0) is a placeholder — only villain seats drive bots + HUD.
SEAT_LAYOUT_TEMPLATES: dict[str, tuple[str, ...]] = {
    "uniform": ("rock", "rock", "rock", "rock", "rock", "rock"),
    "one_maniac_mp": ("rock", "rock", "maniac", "rock", "rock", "rock"),
    "btn_maniac": ("rock", "rock", "rock", "rock", "rock", "maniac"),
    "two_maniac": ("rock", "maniac", "rock", "maniac", "rock", "rock"),
    "rock_blinds": ("rock", "rock", "rock", "rock", "tight", "tight"),
}

SEAT_LAYOUT_GRID: tuple[str, ...] = ("uniform", "one_maniac_mp", "btn_maniac")


def is_uniform_layout(layout: Optional[str]) -> bool:
    return not layout or layout.strip().lower() in ("", "uniform")


def fit_seat_archetypes(
    layout: Optional[str],
    n_players: int,
    *,
    fallback: str = "rock",
) -> Optional[str]:
    """Return TRAINING_SEAT_ARCHETYPES comma string for n_players, or None if uniform."""
    key = (layout or "uniform").strip().lower()
    if is_uniform_layout(key):
        return None
    if key not in SEAT_LAYOUT_TEMPLATES:
        raise KeyError(f"unknown seat layout: {key}")
    if n_players < 2:
        return None

    tmpl = SEAT_LAYOUT_TEMPLATES[key]
    if len(tmpl) != 6:
        raise ValueError(f"layout {key} must have 6 template seats")

    if n_players >= 6:
        chosen = tmpl[:n_players]
    else:
        # Hero + last (n-1) villain seats — keeps BTN/late-seat layouts at HU/4-max.
        chosen = (tmpl[0],) + tmpl[-(n_players - 1):]

    return ",".join(chosen)


def layout_label(layout: Optional[str]) -> str:
    return (layout or "uniform").strip().lower()
