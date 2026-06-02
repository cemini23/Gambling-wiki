"""Tests for seat layout fitting."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from train_seat_layouts import fit_seat_archetypes  # noqa: E402
from train_profiles import _grid_profiles, resolve_profile_list  # noqa: E402


def test_btn_maniac_hu():
    s = fit_seat_archetypes("btn_maniac", 2)
    assert s == "rock,maniac"


def test_one_maniac_6max():
    s = fit_seat_archetypes("one_maniac_mp", 6)
    assert s is not None
    assert s.split(",")[2] == "maniac"


def test_uniform_returns_none():
    assert fit_seat_archetypes("uniform", 6) is None


def test_grid_includes_seat_layouts():
    with_seats = _grid_profiles(include_seat_layouts=True)
    without = _grid_profiles(include_seat_layouts=False)
    assert len(with_seats) == len(without) * 3
    assert any(p.seat_layout == "btn_maniac" for p in with_seats)


def test_named_grid_seats_profile_count():
    profiles = resolve_profile_list("named+grid+seats")
    assert len(profiles) >= 100
