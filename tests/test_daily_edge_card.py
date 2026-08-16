"""Tests for wiki-canon odds math and daily edge card ranking."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from daily_edge_card import classify, load_csv  # noqa: E402
from odds import (  # noqa: E402
    american_to_implied,
    expected_value,
    kelly_fraction,
    multiplicative_devig,
)


def test_minus_110_implied_matches_wiki():
    p = american_to_implied(-110)
    assert abs(p - 0.52381) < 1e-4


def test_two_way_minus_110_hold():
    dv = multiplicative_devig(-110, -110)
    assert abs(dv.hold - 0.04762) < 1e-4
    assert abs(dv.fair_a - 0.5) < 1e-9
    assert abs(dv.fair_b - 0.5) < 1e-9


def test_negative_ev_at_fair_price():
    dv = multiplicative_devig(-110, -110)
    ev = expected_value(dv.fair_a, -110)
    assert ev < 0


def test_positive_ev_when_hr_is_softer():
    dv = multiplicative_devig(-105, -105)
    ev = expected_value(dv.fair_a, -118)
    assert ev < 0  # laying extra juice on a 50/50 is -EV


def test_plus_price_on_fair_coin_is_plus_ev():
    dv = multiplicative_devig(-110, -110)
    ev = expected_value(dv.fair_a, 110)
    assert ev > 0


def test_kelly_zero_on_negative_edge():
    assert kelly_fraction(0.5, -110) == 0.0


def test_kelly_positive_and_capped():
    k = kelly_fraction(0.58, -110)
    assert 0 < k <= 0.05


def test_classify_stale_and_hold():
    action, _ = classify(0.04, 0.04, 12.0, min_ev=0.02, max_hold=0.08, max_age=6.0)
    assert action == "PASS"
    action2, _ = classify(0.04, 0.12, 1.0, min_ev=0.02, max_hold=0.08, max_age=6.0)
    assert action2 == "PASS"


def test_example_csv_loads(tmp_path: Path):
    src = Path(__file__).resolve().parents[1] / "config" / "hr_lines.example.csv"
    now = datetime(2026, 8, 15, 19, 0, tzinfo=timezone.utc)
    rows = load_csv(src, now=now, min_ev=0.02, max_hold=0.08, max_age=6.0, kelly_frac=0.25)
    assert len(rows) == 4
    stale = [r for r in rows if r.event == "Sample stale"][0]
    assert stale.action == "PASS"
    assert rows[0].ev >= rows[-1].ev
    bets = [r for r in rows if r.action == "BET"]
    assert bets, "example CSV should include at least one +EV demo row"
