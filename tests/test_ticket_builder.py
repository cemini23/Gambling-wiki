"""Parlay combine + ticket picker (no live API)."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from odds import combine_parlay  # noqa: E402
from ticket_builder import Side, pick_legs  # noqa: E402


def test_five_minus_110_is_about_plus_2436():
    combined = combine_parlay([-110, -110, -110, -110, -110])
    assert 2400 < combined < 2500


def test_lotto_picks_dogs_strong_picks_favorites():
    sides = [
        Side("A vs B", "2026-08-16T00:00:00Z", "A", "B", -200, "hardrockbet_fl"),
        Side("A vs B", "2026-08-16T00:00:00Z", "B", "A", +170, "hardrockbet_fl"),
        Side("C vs D", "2026-08-16T00:00:00Z", "C", "D", -150, "hardrockbet_fl"),
        Side("C vs D", "2026-08-16T00:00:00Z", "D", "C", +130, "hardrockbet_fl"),
    ]
    strong = pick_legs(sides, legs=2, mode="strong", min_odds=None)
    assert {s.team for s in strong} == {"A", "C"}
    lotto = pick_legs(sides, legs=2, mode="lotto", min_odds=None)
    assert {s.team for s in lotto} == {"B", "D"}


def test_min_odds_swaps_in_a_dog():
    sides = []
    # 3 chalk games at -300 (combined still minus) plus one dog game
    for i, fav in enumerate(["F1", "F2", "F3"], start=1):
        sides.append(Side(f"G{i}", "t", fav, "x", -400, "hr"))
        sides.append(Side(f"G{i}", "t", f"D{i}", fav, +300, "hr"))
    sides.append(Side("G4", "t", "F4", "x", -400, "hr"))
    sides.append(Side("G4", "t", "Long", "F4", +800, "hr"))
    picked = pick_legs(sides, legs=3, mode="strong", min_odds=300)
    combined = combine_parlay([p.american for p in picked])
    assert combined >= 300
