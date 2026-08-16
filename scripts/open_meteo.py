"""Open-Meteo forecast at a stadium (free, no key, personal/non-commercial)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import urlencode

from http_json import get_json

_CACHE: dict[tuple[float, float], dict] = {}


@dataclass(frozen=True)
class WeatherSnap:
    temp_f: float | None
    wind_mph: float | None
    precip_in: float | None
    precip_prob: float | None
    hour_utc: str


def _forecast_payload(lat: float, lon: float) -> dict:
    key = (round(lat, 3), round(lon, 3))
    if key in _CACHE:
        return _CACHE[key]
    qs = urlencode(
        {
            "latitude": f"{lat:.4f}",
            "longitude": f"{lon:.4f}",
            "hourly": "temperature_2m,precipitation_probability,precipitation,wind_speed_10m",
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "UTC",
            "forecast_days": 8,
        }
    )
    payload = get_json(f"https://api.open-meteo.com/v1/forecast?{qs}")
    if not isinstance(payload, dict) or "hourly" not in payload:
        raise RuntimeError("Open-Meteo unexpected payload")
    _CACHE[key] = payload
    return payload


def _parse_iso(raw: str) -> datetime:
    dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def snap_at(lat: float, lon: float, when: datetime) -> WeatherSnap | None:
    hourly = _forecast_payload(lat, lon).get("hourly") or {}
    times = hourly.get("time") or []
    if not times:
        return None
    target = when.astimezone(timezone.utc)
    best_i = 0
    best_dt = abs((_parse_iso(times[0] + "Z") - target).total_seconds())
    for i, t in enumerate(times):
        stamp = t if t.endswith("Z") else t + "Z"
        delta = abs((_parse_iso(stamp) - target).total_seconds())
        if delta < best_dt:
            best_dt = delta
            best_i = i

    def _num(key: str) -> float | None:
        series = hourly.get(key) or []
        if best_i >= len(series) or series[best_i] is None:
            return None
        try:
            return float(series[best_i])
        except (TypeError, ValueError):
            return None

    hour = times[best_i]
    if not hour.endswith("Z"):
        hour = hour + "Z"
    return WeatherSnap(
        temp_f=_num("temperature_2m"),
        wind_mph=_num("wind_speed_10m"),
        precip_in=_num("precipitation"),
        precip_prob=_num("precipitation_probability"),
        hour_utc=hour,
    )
