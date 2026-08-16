"""Stadium lat/lon + roof for sports where MLB Stats does not supply them.

MLB parks come live from statsapi (coords + roofType). NFL is static.
Indoor leagues skip weather.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Venue:
    name: str
    lat: float
    lon: float
    roof: str  # open | retractable | enclosed | semi


# Aliases are Odds API / common nicknames, lowercase.
NFL_VENUES: dict[str, Venue] = {
    "arizona cardinals": Venue("State Farm Stadium", 33.5276, -112.2626, "retractable"),
    "atlanta falcons": Venue("Mercedes-Benz Stadium", 33.7555, -84.4008, "retractable"),
    "baltimore ravens": Venue("M&T Bank Stadium", 39.2780, -76.6227, "open"),
    "buffalo bills": Venue("Highmark Stadium", 42.7738, -78.7870, "open"),
    "carolina panthers": Venue("Bank of America Stadium", 35.2251, -80.8526, "open"),
    "chicago bears": Venue("Soldier Field", 41.8623, -87.6167, "open"),
    "cincinnati bengals": Venue("Paycor Stadium", 39.0954, -84.5160, "open"),
    "cleveland browns": Venue("Huntington Bank Field", 41.5061, -81.6995, "open"),
    "dallas cowboys": Venue("AT&T Stadium", 32.7473, -97.0945, "retractable"),
    "denver broncos": Venue("Empower Field at Mile High", 39.7439, -105.0201, "open"),
    "detroit lions": Venue("Ford Field", 42.3400, -83.0456, "enclosed"),
    "green bay packers": Venue("Lambeau Field", 44.5013, -88.0622, "open"),
    "houston texans": Venue("NRG Stadium", 29.6847, -95.4107, "retractable"),
    "indianapolis colts": Venue("Lucas Oil Stadium", 39.7601, -86.1639, "retractable"),
    "jacksonville jaguars": Venue("EverBank Stadium", 30.3239, -81.6373, "open"),
    "kansas city chiefs": Venue("Arrowhead Stadium", 39.0489, -94.4839, "open"),
    "las vegas raiders": Venue("Allegiant Stadium", 36.0908, -115.1830, "enclosed"),
    "los angeles chargers": Venue("SoFi Stadium", 33.9535, -118.3392, "semi"),
    "los angeles rams": Venue("SoFi Stadium", 33.9535, -118.3392, "semi"),
    "miami dolphins": Venue("Hard Rock Stadium", 25.9580, -80.2389, "open"),
    "minnesota vikings": Venue("U.S. Bank Stadium", 44.9736, -93.2575, "enclosed"),
    "new england patriots": Venue("Gillette Stadium", 42.0909, -71.2643, "open"),
    "new orleans saints": Venue("Caesars Superdome", 29.9509, -90.0814, "enclosed"),
    "new york giants": Venue("MetLife Stadium", 40.8128, -74.0742, "open"),
    "new york jets": Venue("MetLife Stadium", 40.8128, -74.0742, "open"),
    "philadelphia eagles": Venue("Lincoln Financial Field", 39.9008, -75.1675, "open"),
    "pittsburgh steelers": Venue("Acrisure Stadium", 40.4468, -80.0158, "open"),
    "san francisco 49ers": Venue("Levi's Stadium", 37.4033, -121.9694, "open"),
    "seattle seahawks": Venue("Lumen Field", 47.5952, -122.3316, "open"),
    "tampa bay buccaneers": Venue("Raymond James Stadium", 27.9759, -82.5033, "open"),
    "tennessee titans": Venue("Nissan Stadium", 36.1665, -86.7713, "open"),
    "washington commanders": Venue("Northwest Stadium", 38.9077, -76.8645, "open"),
}

INDOOR_SPORTS = frozenset({"nba", "nhl", "wnba", "ufc", "mma"})


def lookup_nfl_home(home_team: str) -> Venue | None:
    key = (home_team or "").strip().lower()
    return NFL_VENUES.get(key)


def weather_applies(sport: str, roof: str | None) -> bool:
    if sport.lower() in INDOOR_SPORTS:
        return False
    r = (roof or "open").lower()
    return r not in {"enclosed", "dome", "indoor", "fixed"}
