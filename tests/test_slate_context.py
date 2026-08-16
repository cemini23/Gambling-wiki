"""Under-lean heuristics + unders picker (no live APIs)."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from open_meteo import WeatherSnap  # noqa: E402
from slate_context import INDOOR, LEAN_UNDER, NEUTRAL, match_mlb, under_lean  # noqa: E402
from mlb_stats import MlbGame, horizon_dates  # noqa: E402
from ticket_builder import Side, pick_unders  # noqa: E402
from venues import lookup_nfl_home  # noqa: E402


def test_dome_is_indoor():
    lean, score, _ = under_lean(sport="mlb", roof="Dome", weather=None, park_name="Tropicana Field")
    assert lean == INDOOR
    assert score == 0


def test_rain_and_wind_lean_under():
    wx = WeatherSnap(temp_f=68, wind_mph=16, precip_in=0.1, precip_prob=55, hour_utc="2026-08-16T00:00Z")
    lean, score, reasons = under_lean(sport="mlb", roof="Open", weather=wx, park_name="Fenway Park")
    assert lean == LEAN_UNDER
    assert score >= 2
    assert any("rain" in r or "wind" in r for r in reasons)


def test_calm_warm_is_neutral():
    wx = WeatherSnap(temp_f=72, wind_mph=4, precip_in=0.0, precip_prob=5, hour_utc="t")
    lean, score, _ = under_lean(sport="mlb", roof="Open", weather=wx, park_name="Oracle Park")
    assert lean == NEUTRAL
    assert score == 0


def test_coors_fades_weather_unders():
    wx = WeatherSnap(temp_f=60, wind_mph=16, precip_in=0.0, precip_prob=10, hour_utc="t")
    _lean, score, reasons = under_lean(sport="mlb", roof="Open", weather=wx, park_name="Coors Field")
    assert score < 2
    assert any("altitude" in r for r in reasons)


def test_nba_indoor():
    lean, _, _ = under_lean(sport="nba", roof="open", weather=None)
    assert lean == INDOOR


def test_nfl_eagles_open_air():
    v = lookup_nfl_home("Philadelphia Eagles")
    assert v is not None
    assert v.roof == "open"
    assert v.lat > 39


def test_mlb_name_match():
    games = [
        MlbGame(
            away="Boston Red Sox",
            home="New York Yankees",
            commence="t",
            venue="Yankee Stadium",
            lat=40.8,
            lon=-73.9,
            roof="Open",
            away_pitcher="A",
            home_pitcher="B",
        )
    ]
    hit = match_mlb("Boston Red Sox at New York Yankees", games)
    assert hit is not None
    assert hit.home_pitcher == "B"


def test_horizon_dates_covers_window():
    from datetime import datetime, timezone

    days = horizon_dates(36, now=datetime(2026, 8, 16, 22, 0, tzinfo=timezone.utc))
    assert days[0] == "2026-08-16"
    assert "2026-08-18" in days


def test_unders_prefer_weather_score():
    sides = [
        Side("calm", "t", "Under 9", "x", -110, "hr", market="totals", point=9.0),
        Side("storm", "t", "Under 8.5", "x", -110, "hr", market="totals", point=8.5),
        Side("other", "t", "Under 7.5", "x", -110, "hr", market="totals", point=7.5),
    ]
    picked = pick_unders(sides, legs=2, min_odds=None, scores={"storm": 4, "calm": 0, "other": 1})
    assert picked[0].event == "storm"
    assert {p.event for p in picked} == {"storm", "other"}
