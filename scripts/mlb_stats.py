"""MLB Stats API — schedule, probable pitchers, venue roof + coords. No key."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urlencode

from http_json import get_json


@dataclass(frozen=True)
class MlbGame:
    away: str
    home: str
    commence: str
    venue: str
    lat: float | None
    lon: float | None
    roof: str
    away_pitcher: str
    home_pitcher: str


def horizon_dates(hours: float, *, now: datetime | None = None) -> list[str]:
    now = now or datetime.now(timezone.utc)
    end = now + timedelta(hours=hours)
    d = now.date()
    out: list[str] = []
    last = end.date()
    while d <= last:
        out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def fetch_schedule(day: str) -> list[MlbGame]:
    qs = urlencode(
        {
            "sportId": "1",
            "date": day,
            "hydrate": "probablePitcher,venue(location,fieldInfo)",
        }
    )
    payload = get_json(f"https://statsapi.mlb.com/api/v1/schedule?{qs}")
    if not isinstance(payload, dict):
        return []
    games: list[MlbGame] = []
    for block in payload.get("dates") or []:
        for g in block.get("games") or []:
            teams = g.get("teams") or {}
            away = ((teams.get("away") or {}).get("team") or {}).get("name") or ""
            home = ((teams.get("home") or {}).get("team") or {}).get("name") or ""
            ap = ((teams.get("away") or {}).get("probablePitcher") or {}).get("fullName") or "TBD"
            hp = ((teams.get("home") or {}).get("probablePitcher") or {}).get("fullName") or "TBD"
            venue = g.get("venue") or {}
            loc = (venue.get("location") or {}).get("defaultCoordinates") or {}
            field = venue.get("fieldInfo") or {}
            roof = str(field.get("roofType") or "Open")
            lat = loc.get("latitude")
            lon = loc.get("longitude")
            games.append(
                MlbGame(
                    away=str(away),
                    home=str(home),
                    commence=str(g.get("gameDate") or ""),
                    venue=str(venue.get("name") or ""),
                    lat=float(lat) if lat is not None else None,
                    lon=float(lon) if lon is not None else None,
                    roof=roof,
                    away_pitcher=str(ap),
                    home_pitcher=str(hp),
                )
            )
    return games


def fetch_horizon(hours: float) -> list[MlbGame]:
    seen: set[tuple[str, str, str]] = set()
    out: list[MlbGame] = []
    for day in horizon_dates(hours):
        for g in fetch_schedule(day):
            key = (g.away, g.home, g.commence)
            if key in seen:
                continue
            seen.add(key)
            out.append(g)
    return out


def today_iso() -> str:
    return date.today().isoformat()
