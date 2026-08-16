"""Free slate context: Open-Meteo + MLB Stats + NFL venues → under lean.

Heuristics, not a projection model. Confirm lines in-app.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from mlb_stats import MlbGame, fetch_horizon  # noqa: E402
from open_meteo import WeatherSnap, snap_at  # noqa: E402
from venues import lookup_nfl_home, weather_applies  # noqa: E402

LEAN_UNDER = "LEAN_UNDER"
LEAN_OVER = "LEAN_OVER"
NEUTRAL = "NEUTRAL"
INDOOR = "INDOOR"
UNKNOWN = "UNKNOWN"


@dataclass
class GameContext:
    event: str
    venue: str
    roof: str
    lean: str
    score: int
    reasons: list[str]
    weather: WeatherSnap | None
    extra: str  # pitchers or blank


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def classify_roof(roof: str | None) -> str:
    r = (roof or "open").lower()
    if r in {"dome", "enclosed", "indoor", "fixed", "retractable dome"}:
        return "enclosed"
    if "retractable" in r:
        return "retractable"
    if "semi" in r:
        return "semi"
    return "open"


def under_lean(
    *,
    sport: str,
    roof: str | None,
    weather: WeatherSnap | None,
    park_name: str = "",
) -> tuple[str, int, list[str]]:
    if sport.lower() in {"nba", "nhl", "wnba", "ufc", "mma"}:
        return INDOOR, 0, ["indoor sport — weather off"]
    kind = classify_roof(roof)
    reasons: list[str] = []
    score = 0
    if kind == "enclosed":
        return INDOOR, 0, ["enclosed roof — weather off"]
    if kind == "retractable":
        reasons.append("retractable roof — confirm closed; weather still shown")
    if kind == "semi":
        reasons.append("semi-open (SoFi-style) — weather on")
    if weather is None:
        return UNKNOWN, 0, reasons + ["no forecast"]

    if weather.precip_prob is not None and weather.precip_prob >= 40:
        score += 2
        reasons.append(f"rain chance {weather.precip_prob:.0f}%")
    if weather.precip_in is not None and weather.precip_in >= 0.05:
        score += 1
        reasons.append(f"{weather.precip_in:.2f} in precip")
    if weather.wind_mph is not None and weather.wind_mph >= 15:
        score += 2
        reasons.append(f"wind {weather.wind_mph:.0f} mph")
    elif weather.wind_mph is not None and weather.wind_mph >= 10:
        score += 1
        reasons.append(f"wind {weather.wind_mph:.0f} mph")
    if weather.temp_f is not None and weather.temp_f <= 45:
        score += 2
        reasons.append(f"cold {weather.temp_f:.0f}F")
    elif weather.temp_f is not None and weather.temp_f <= 55:
        score += 1
        reasons.append(f"cool {weather.temp_f:.0f}F")

    park = park_name.lower()
    if "coors" in park or "mile high" in park:
        score -= 2
        reasons.append("altitude park — weather unders often fade")

    if score >= 2:
        return LEAN_UNDER, score, reasons
    if score <= -2:
        return LEAN_OVER, score, reasons
    return NEUTRAL, score, reasons or ["no strong weather signal"]


def _when(raw: str) -> datetime | None:
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _wx(lat: float | None, lon: float | None, commence: str) -> WeatherSnap | None:
    if lat is None or lon is None:
        return None
    when = _when(commence)
    if when is None:
        return None
    try:
        return snap_at(lat, lon, when)
    except RuntimeError:
        return None


def match_mlb(event: str, games: list[MlbGame]) -> MlbGame | None:
    blob = _norm(event)
    for g in games:
        if _norm(g.away) in blob and _norm(g.home) in blob:
            return g
    return None


def context_for_mlb(event: str, commence: str, games: list[MlbGame]) -> GameContext:
    g = match_mlb(event, games)
    if not g:
        return GameContext(event, "?", "open", UNKNOWN, 0, ["no MLB Stats match"], None, "")
    wx = _wx(g.lat, g.lon, commence or g.commence) if weather_applies("mlb", g.roof) else None
    lean, score, reasons = under_lean(sport="mlb", roof=g.roof, weather=wx, park_name=g.venue)
    extra = f"{g.away_pitcher} vs {g.home_pitcher}"
    return GameContext(event, g.venue, g.roof, lean, score, reasons, wx, extra)


def context_for_nfl(event: str, commence: str, home_team: str) -> GameContext:
    venue = lookup_nfl_home(home_team)
    if venue is None:
        # event like "Away at Home"
        home_guess = event.split(" at ")[-1].strip() if " at " in event else home_team
        venue = lookup_nfl_home(home_guess)
    if venue is None:
        return GameContext(event, "?", "open", UNKNOWN, 0, ["no NFL venue match"], None, "")
    wx = _wx(venue.lat, venue.lon, commence) if weather_applies("nfl", venue.roof) else None
    lean, score, reasons = under_lean(sport="nfl", roof=venue.roof, weather=wx, park_name=venue.name)
    return GameContext(event, venue.name, venue.roof, lean, score, reasons, wx, "")


def indoor_context(event: str) -> GameContext:
    return GameContext(event, "arena", "enclosed", INDOOR, 0, ["indoor — weather off"], None, "")


def wx_brief(ctx: GameContext) -> str:
    w = ctx.weather
    bits = [ctx.lean]
    if w:
        if w.temp_f is not None:
            bits.append(f"{w.temp_f:.0f}F")
        if w.wind_mph is not None:
            bits.append(f"wind {w.wind_mph:.0f}")
        if w.precip_prob is not None:
            bits.append(f"rain {w.precip_prob:.0f}%")
    elif ctx.reasons:
        bits.append(ctx.reasons[0])
    return ", ".join(bits)


def render_table(rows: list[GameContext]) -> str:
    lines = [
        "| Event | Venue / roof | Lean | Weather | Notes |",
        "|-------|--------------|------|---------|-------|",
    ]
    for r in rows:
        notes = "; ".join(r.reasons[:3])
        if r.extra:
            notes = f"{r.extra}. {notes}".strip()
        wx = wx_brief(r)
        lines.append(f"| {r.event} | {r.venue} ({r.roof}) | **{r.lean}** ({r.score:+d}) | {wx} | {notes} |")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("sport", choices=("mlb", "nfl", "nba", "nhl", "wnba"))
    p.add_argument("--hours", type=float, default=36)
    args = p.parse_args()
    if args.sport in {"nba", "nhl", "wnba"}:
        print("Indoor slate — Open-Meteo off. No free lineup API wired (ESPN JSON is NO-GO).")
        return 0
    rows: list[GameContext] = []
    if args.sport == "mlb":
        games = fetch_horizon(args.hours)
        now = datetime.now(timezone.utc)
        for g in games:
            when = _when(g.commence)
            if when is None:
                continue
            delta_h = (when - now).total_seconds() / 3600.0
            if not (0 <= delta_h <= args.hours):
                continue
            event = f"{g.away} at {g.home}"
            rows.append(context_for_mlb(event, g.commence, games))
    else:
        print("NFL context needs Odds API team names; run ticket_builder --mode unders instead.")
        print("Stadium table is loaded for weather once a ticket fetch runs.")
        return 0
    if not rows:
        print("No MLB games in that window.")
        return 2
    print(f"# MLB slate context ({len(rows)} games, next {args.hours:.0f}h)")
    print()
    print("Open-Meteo + MLB Stats API -- heuristics, not a model. Confirm roof / pitchers in-app.")
    print()
    print(render_table(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
