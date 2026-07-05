#!/usr/bin/env python3
"""NFL slate prefetch — schedule-aware stubs for W8 hub research.

Runs hourly (LaunchAgent during NFL season). Fetches nflverse schedule + optional
Open-Meteo wind, writes briefs/slate-prefetch/{slate_id}-{pass}.md when the
configured hours-before-kickoff window matches.

Does NOT run LLM ingest or write wiki pages. Operator or Cursor automation
completes the hub brief from the prefetch stub.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)


@dataclass(frozen=True)
class Game:
    season: int
    week: int
    away: str
    home: str
    kickoff: datetime
    spread: str
    total: str
    game_type: str


@dataclass(frozen=True)
class Slate:
    slate_key: str
    label: str
    season: int
    week: int
    games: tuple[Game, ...]

    @property
    def slate_id(self) -> str:
        return f"{self.season}-w{self.week:02d}-{self.slate_key}"

    @property
    def first_kickoff(self) -> datetime:
        return min(g.kickoff for g in self.games)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_config() -> dict:
    path = Path(__file__).resolve().parent / "nfl_slate_prefetch_config.yaml"
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def infer_season(today: date, override: int | None) -> int:
    if override:
        return int(override)
    # NFL season label: Sep–Dec → that year; Jan–Feb → previous year's season
    if today.month >= 9:
        return today.year
    if today.month <= 2:
        return today.year - 1
    return today.year


def fetch_schedule(url: str) -> list[dict[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": "cemini-nfl-slate-prefetch/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    return list(csv.DictReader(io.StringIO(text)))


def parse_kickoff(row: dict[str, str], tz: ZoneInfo) -> datetime | None:
    gameday = (row.get("gameday") or "").strip()
    gametime = (row.get("gametime") or "").strip()
    if not gameday:
        return None
    try:
        d = date.fromisoformat(gameday[:10])
    except ValueError:
        return None
    if gametime:
        parts = gametime.split(":")
        try:
            h, m = int(parts[0]), int(parts[1])
            t = time(h, m)
        except (ValueError, IndexError):
            t = time(13, 0)
    else:
        t = time(13, 0)
    return datetime.combine(d, t, tzinfo=tz)


def classify_slate(kickoff: datetime) -> str | None:
    wd = kickoff.weekday()  # Mon=0 … Sun=6
    hour = kickoff.hour + kickoff.minute / 60
    if wd == 3:  # Thursday
        return "thu"
    if wd == 6:  # Sunday
        return "snf" if hour >= 20.0 else "sun"
    if wd == 0:  # Monday
        return "mnf"
    return None


def games_for_season(rows: list[dict[str, str]], season: int, tz: ZoneInfo) -> list[Game]:
    out: list[Game] = []
    for row in rows:
        if (row.get("game_type") or "").upper() != "REG":
            continue
        try:
            row_season = int(float(row.get("season") or 0))
        except ValueError:
            continue
        if row_season != season:
            continue
        kickoff = parse_kickoff(row, tz)
        if kickoff is None:
            continue
        try:
            week = int(float(row.get("week") or 0))
        except ValueError:
            continue
        away = (row.get("away_team") or "").strip()
        home = (row.get("home_team") or "").strip()
        if not away or not home:
            continue
        out.append(
            Game(
                season=season,
                week=week,
                away=away,
                home=home,
                kickoff=kickoff,
                spread=(row.get("spread_line") or "").strip(),
                total=(row.get("total_line") or "").strip(),
                game_type="REG",
            )
        )
    return out


def group_slates(games: list[Game], now: datetime) -> list[Slate]:
    upcoming = [g for g in games if g.kickoff > now - timedelta(hours=3)]
    buckets: dict[tuple[int, int, str], list[Game]] = {}
    for g in upcoming:
        sk = classify_slate(g.kickoff)
        if not sk:
            continue
        key = (g.season, g.week, sk)
        buckets.setdefault(key, []).append(g)
    slates: list[Slate] = []
    for (season, week, sk), gs in sorted(buckets.items()):
        gs = sorted(gs, key=lambda x: x.kickoff)
        slates.append(Slate(slate_key=sk, label=sk, season=season, week=week, games=tuple(gs)))
    return slates


def pass_due(
    slate: Slate,
    pass_id: str,
    hours_before: float,
    tolerance: float,
    now: datetime,
) -> bool:
    hours_until = (slate.first_kickoff - now).total_seconds() / 3600
    if hours_until < 0:
        return False
    return abs(hours_until - hours_before) <= tolerance


def fetch_wind(lat: float, lon: float, kickoff: datetime) -> str:
    """Open-Meteo hourly wind at kickoff (best effort)."""
    start = kickoff.strftime("%Y-%m-%d")
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&hourly=wind_speed_10m&"
        f"wind_speed_unit=mph&timezone=America%2FNew_York&start_date={start}&end_date={start}"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "cemini-nfl-slate-prefetch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        times = data.get("hourly", {}).get("time", [])
        speeds = data.get("hourly", {}).get("wind_speed_10m", [])
        target = kickoff.strftime("%Y-%m-%dT%H:00")
        for t, s in zip(times, speeds):
            if t == target:
                return f"{s:.0f} mph"
        if speeds:
            return f"{speeds[0]:.0f} mph (approx)"
    except (urllib.error.URLError, json.JSONDecodeError, KeyError, TypeError):
        pass
    return "n/a"


def weather_line(game: Game, stadiums: dict, enabled: bool) -> str:
    if not enabled:
        return "weather: disabled"
    meta = stadiums.get(game.home, {})
    roof = meta.get("roof", "unknown")
    if roof == "closed":
        return "dome — wind n/a"
    lat, lon = meta.get("lat"), meta.get("lon")
    if lat is None or lon is None:
        return "outdoor — coords n/a"
    wind = fetch_wind(float(lat), float(lon), game.kickoff)
    return f"outdoor — wind {wind}"


def prefetch_exists(path: Path, kickoff_iso: str) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    return f"first_kickoff: {kickoff_iso}" in text


def write_prefetch(
    repo: Path,
    cfg: dict,
    slate: Slate,
    pass_id: str,
    pass_label: str,
    now: datetime,
) -> tuple[Path, bool]:
    out_dir = repo / cfg["output"]["dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    slate_passes = cfg.get("slate_passes", {})
    slate_cfg = slate_passes.get(slate.slate_key, {})
    human_label = slate_cfg.get("label", slate.slate_key)

    kickoff_iso = slate.first_kickoff.isoformat()
    fname = f"{slate.slate_id}-{pass_id}.md"
    path = out_dir / fname

    if prefetch_exists(path, kickoff_iso):
        return path, False

    stadiums = cfg.get("stadiums", {})
    weather_on = cfg.get("weather", {}).get("enabled", False)

    lines = [
        "---",
        f"title: Slate prefetch — {human_label} ({pass_id})",
        "type: brief",
        f"tags: [brief, prefetch, nfl, w8, {slate.slate_key}]",
        f"slate_id: {slate.slate_id}",
        f"season: {slate.season}",
        f"week: {slate.week}",
        f"slate_key: {slate.slate_key}",
        f"pass: {pass_id}",
        f"first_kickoff: {kickoff_iso}",
        f"generated: {now.isoformat()}",
        "status: prefetch-stub",
        "---",
        "",
        f"# Slate prefetch — {human_label} · {pass_id.upper()}",
        "",
        f"**Season {slate.season} Week {slate.week}** · first kickoff `{kickoff_iso}`",
        "",
        "> Auto-generated by `scripts/nfl_slate_prefetch_run.py`. **Complete hub brief in Cursor** — see § Agent prompt.",
        "",
        "## Games (nflverse schedule)",
        "",
        "| Kickoff (ET) | Away | Home | Spread | Total | Weather |",
        "|--------------|------|------|--------|-------|---------|",
    ]
    for g in slate.games:
        wx = weather_line(g, stadiums, weather_on)
        lines.append(
            f"| {g.kickoff.strftime('%a %m/%d %H:%M')} | {g.away} | {g.home} | "
            f"{g.spread or '—'} | {g.total or '—'} | {wx} |"
        )

    hub_name = f"{slate.season}-w{slate.week:02d}-slate-hub-{slate.slate_key}.md"
    lines.extend(
        [
            "",
            "## Agent checklist (hub completion)",
            "",
            "- [ ] Injury / practice report (official + beat notes)",
            "- [ ] Line movement since open (Odds API or manual)",
            "- [ ] Game script / stack priorities",
            "- [ ] Cross-lane flags (weather, backup QB, etc.)",
            "- [ ] Lane pointers: FanDuel, Hard Rock, Underdog Pick'em",
            "",
            f"**Target hub file:** `briefs/{hub_name}`",
            "",
            "## Agent prompt (paste in gambling-wiki Cursor)",
            "",
            "```text",
            cfg.get("cursor_prompt", "").strip(),
            f"Prefetch: briefs/slate-prefetch/{fname}",
            f"Write: briefs/{hub_name}",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")

    prompt_sidecar = out_dir / f".cursor-prompt-{slate.slate_id}-{pass_id}.txt"
    prompt_sidecar.write_text(
        f"Complete NFL slate hub from prefetch {fname}\n"
        f"Target: briefs/{hub_name}\n",
        encoding="utf-8",
    )
    return path, True


def notify_macos(title: str, message: str) -> None:
    safe = message.replace('"', "'")[:200]
    script = f'display notification "{safe}" with title "{title}"'
    try:
        import subprocess

        subprocess.run(["osascript", "-e", script], check=False, timeout=5)
    except OSError:
        pass


def main() -> int:
    cfg = load_config()
    tz = ZoneInfo(cfg.get("timezone", "America/New_York"))
    now = datetime.now(tz)
    repo = repo_root()
    season = infer_season(now.date(), cfg.get("season_override"))

    # Off-season: quiet exit unless schedule has games in next 14 days
    try:
        rows = fetch_schedule(cfg["schedule_url"])
    except urllib.error.URLError as e:
        print(f"ERROR: schedule fetch failed: {e}", file=sys.stderr)
        return 1

    games = games_for_season(rows, season, tz)
    if not games:
        print(f"No REG games for season {season}; skipping.")
        return 0

    slates = group_slates(games, now)
    if not slates:
        print("No upcoming slates in window.")
        return 0

    written: list[Path] = []
    slate_passes = cfg.get("slate_passes", {})
    for slate in slates:
        scfg = slate_passes.get(slate.slate_key)
        if not scfg:
            continue
        for p in scfg.get("passes", []):
            pid = p["id"]
            hours = float(p["hours_before"])
            tol = float(p.get("tolerance_hours", 1.0))
            if not pass_due(slate, pid, hours, tol, now):
                continue
            path, created = write_prefetch(
                repo, cfg, slate, pid, scfg.get("label", slate.slate_key), now
            )
            if created:
                written.append(path)

    if written:
        for p in written:
            print(f"Wrote {p.relative_to(repo)}")
        notify_macos(
            "NFL slate prefetch",
            f"{len(written)} stub(s) ready — open gambling-wiki in Cursor",
        )
    else:
        print("No prefetch windows matched this hour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
