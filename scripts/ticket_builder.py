#!/usr/bin/env python3
"""Chat ticket builder — live Hard Rock (FL) odds via The Odds API.

Examples:
  python scripts/ticket_builder.py mlb --legs 5 --min-odds +300 --mode strong
  python scripts/ticket_builder.py mlb --legs 4 --mode unders --min-odds +300
  python scripts/ticket_builder.py ufc --legs 10 --mode lotto
  python scripts/slate_context.py mlb --hours 36

Does not place bets. HR SGP pricing may differ from this independent parlay math.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from env_load import load_dotenv  # noqa: E402
from mlb_stats import fetch_horizon  # noqa: E402
from odds import american_to_implied, combine_parlay  # noqa: E402
from slate_context import (  # noqa: E402
    GameContext,
    context_for_mlb,
    context_for_nfl,
    indoor_context,
    wx_brief,
)

SPORTS = {
    "mlb": "baseball_mlb",
    "ufc": "mma_mixed_martial_arts",
    "mma": "mma_mixed_martial_arts",
    "nfl": "americanfootball_nfl",
    "nba": "basketball_nba",
    "nhl": "icehockey_nhl",
    "wnba": "basketball_wnba",
}

BOOK_PREFERENCE = ("hardrockbet_fl", "hardrockbet", "draftkings", "fanduel")


@dataclass(frozen=True)
class Side:
    event: str
    commence: str
    team: str
    opponent: str
    american: float
    book: str
    market: str = "h2h"
    point: float | None = None
    home_team: str = ""
    notes: str = ""

    @property
    def implied(self) -> float:
        return american_to_implied(self.american)


def _fmt_american(a: float) -> str:
    if a > 0:
        return f"+{a:.0f}"
    return f"{a:.0f}"


def fetch_odds(api_key: str, sport_key: str, markets: str) -> list[dict]:
    qs = urlencode(
        {
            "apiKey": api_key,
            "regions": "us,us2",
            "markets": markets,
            "oddsFormat": "american",
            "bookmakers": ",".join(BOOK_PREFERENCE),
        }
    )
    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds/?{qs}"
    req = Request(url, headers={"User-Agent": "gambling-wiki-tickets/1.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            remaining = resp.headers.get("x-requests-remaining", "?")
            used = resp.headers.get("x-requests-used", "?")
            payload = json.loads(resp.read().decode())
    except HTTPError as exc:
        body = exc.read().decode(errors="replace")[:400]
        raise SystemExit(f"Odds API HTTP {exc.code}: {body}") from exc
    except URLError as exc:
        raise SystemExit(f"Odds API unreachable: {exc}") from exc
    if not isinstance(payload, list):
        raise SystemExit("Odds API returned unexpected payload")
    payload.append({"_meta": {"remaining": remaining, "used": used}})  # type: ignore[arg-type]
    return payload


def _pick_book(event: dict) -> dict | None:
    books = {b.get("key"): b for b in event.get("bookmakers") or []}
    for key in BOOK_PREFERENCE:
        if key in books:
            return books[key]
    return None


def flatten_ml_sides(events: list[dict]) -> list[Side]:
    sides: list[Side] = []
    for event in events:
        if not isinstance(event, dict) or "_meta" in event:
            continue
        home = event.get("home_team") or ""
        away = event.get("away_team") or ""
        title = f"{away} at {home}".strip(" at ")
        commence = event.get("commence_time") or ""
        book = _pick_book(event)
        if not book:
            continue
        markets = [m for m in book.get("markets") or [] if m.get("key") == "h2h"]
        if not markets:
            continue
        outcomes = markets[0].get("outcomes") or []
        if len(outcomes) < 2:
            continue
        for o in outcomes:
            name = str(o.get("name") or "")
            price = o.get("price")
            if name.lower() in {"draw", "tie"} or price is None:
                continue
            try:
                american = float(price)
            except (TypeError, ValueError):
                continue
            opp = home if name == away else away if name == home else "field"
            sides.append(
                Side(
                    event=title,
                    commence=commence,
                    team=name,
                    opponent=opp,
                    american=american,
                    book=str(book.get("key") or ""),
                    market="h2h",
                    home_team=str(home),
                )
            )
    return sides


def flatten_under_sides(events: list[dict]) -> list[Side]:
    sides: list[Side] = []
    for event in events:
        if not isinstance(event, dict) or "_meta" in event:
            continue
        home = event.get("home_team") or ""
        away = event.get("away_team") or ""
        title = f"{away} at {home}".strip(" at ")
        commence = event.get("commence_time") or ""
        book = _pick_book(event)
        if not book:
            continue
        markets = [m for m in book.get("markets") or [] if m.get("key") == "totals"]
        if not markets:
            continue
        for o in markets[0].get("outcomes") or []:
            if str(o.get("name") or "").lower() != "under":
                continue
            price = o.get("price")
            if price is None:
                continue
            try:
                american = float(price)
                point = float(o["point"]) if o.get("point") is not None else None
            except (TypeError, ValueError):
                continue
            label = f"Under {point:g}" if point is not None else "Under"
            sides.append(
                Side(
                    event=title,
                    commence=commence,
                    team=label,
                    opponent=str(away),
                    american=american,
                    book=str(book.get("key") or ""),
                    market="totals",
                    point=point,
                    home_team=str(home),
                )
            )
    return sides


def filter_horizon(sides: list[Side], hours: float) -> list[Side]:
    now = datetime.now(timezone.utc)
    kept: list[Side] = []
    for s in sides:
        raw = (s.commence or "").replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(raw)
        except ValueError:
            continue
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        delta_h = (dt - now).total_seconds() / 3600.0
        if 0 <= delta_h <= hours:
            kept.append(s)
    return kept


def unique_events(sides: list[Side]) -> dict[str, list[Side]]:
    grouped: dict[str, list[Side]] = {}
    for s in sides:
        grouped.setdefault(s.event, []).append(s)
    return grouped


@dataclass
class EventMl:
    event: str
    fav: Side
    dog: Side


def _events(sides: list[Side]) -> list[EventMl]:
    out: list[EventMl] = []
    for event, ev_sides in unique_events(sides).items():
        ranked = sorted(ev_sides, key=lambda s: s.implied, reverse=True)
        if len(ranked) < 2:
            continue
        out.append(EventMl(event=event, fav=ranked[0], dog=ranked[-1]))
    return out


def pick_legs(
    sides: list[Side],
    *,
    legs: int,
    mode: str,
    min_odds: float | None,
) -> list[Side]:
    events = _events(sides)
    if len(events) < legs:
        raise SystemExit(f"Only {len(events)} events live; need {legs}.")
    if mode == "lotto":
        events = sorted(events, key=lambda e: e.dog.implied)  # longest dogs first
        chosen_sides = [e.dog for e in events[:legs]]
        unused = events[legs:]
    else:
        events = sorted(events, key=lambda e: e.fav.implied, reverse=True)
        chosen_ev = events[:legs]
        unused = events[legs:]
        chosen_sides = [e.fav for e in chosen_ev]
        if min_odds is not None:
            combined = combine_parlay([c.american for c in chosen_sides])
            # Flip chalkiest remaining favorite to its dog until min odds hit.
            while combined < min_odds:
                idx = max(range(len(chosen_ev)), key=lambda j: chosen_sides[j].implied)
                if chosen_sides[idx].team != chosen_ev[idx].fav.team:
                    if not unused:
                        break
                    # replace a chalk game with a leftover game's dog
                    nxt = unused.pop(0)
                    chosen_ev[idx] = nxt
                    chosen_sides[idx] = nxt.dog
                else:
                    chosen_sides[idx] = chosen_ev[idx].dog
                combined = combine_parlay([c.american for c in chosen_sides])
        return chosen_sides

    if len(chosen_sides) < legs:
        raise SystemExit(f"Only {len(chosen_sides)} events live; need {legs}.")
    if min_odds is None:
        return chosen_sides
    combined = combine_parlay([c.american for c in chosen_sides])
    i = 0
    while combined < min_odds and i < len(unused):
        chalk_idx = max(range(len(chosen_sides)), key=lambda j: chosen_sides[j].implied)
        chosen_sides[chalk_idx] = unused[i].dog
        i += 1
        combined = combine_parlay([c.american for c in chosen_sides])
    return chosen_sides


def pick_unders(
    sides: list[Side],
    *,
    legs: int,
    min_odds: float | None,
    scores: dict[str, int] | None = None,
) -> list[Side]:
    scores = scores or {}
    grouped = unique_events(sides)
    if len(grouped) < legs:
        raise SystemExit(f"Only {len(grouped)} totals games live; need {legs}.")

    def sort_key(event: str) -> tuple[int, float, float]:
        s = grouped[event][0]
        point = s.point if s.point is not None else 99.0
        return (-scores.get(event, 0), point, s.implied)

    ordered = sorted(grouped.keys(), key=sort_key)
    chosen = [grouped[e][0] for e in ordered[:legs]]
    unused = [grouped[e][0] for e in ordered[legs:]]
    if min_odds is None:
        return chosen
    combined = combine_parlay([c.american for c in chosen])
    while combined < min_odds and unused:
        idx = max(range(len(chosen)), key=lambda j: chosen[j].implied)
        chosen[idx] = unused.pop(0)
        combined = combine_parlay([c.american for c in chosen])
    return chosen


def annotate_sides(sport: str, sides: list[Side]) -> tuple[list[Side], dict[str, GameContext]]:
    ctx: dict[str, GameContext] = {}
    mlb_games = fetch_horizon(48) if sport == "mlb" else []
    out: list[Side] = []
    for s in sides:
        if s.event in ctx:
            c = ctx[s.event]
        elif sport == "mlb":
            c = context_for_mlb(s.event, s.commence, mlb_games)
            ctx[s.event] = c
        elif sport == "nfl":
            c = context_for_nfl(s.event, s.commence, s.home_team)
            ctx[s.event] = c
        else:
            c = indoor_context(s.event)
            ctx[s.event] = c
        note = wx_brief(c)
        if c.extra:
            note = f"{c.extra} · {note}"
        out.append(
            Side(
                event=s.event,
                commence=s.commence,
                team=s.team,
                opponent=s.opponent,
                american=s.american,
                book=s.book,
                market=s.market,
                point=s.point,
                home_team=s.home_team,
                notes=note,
            )
        )
    return out, ctx


def render_ticket(legs: list[Side], *, sport: str, mode: str, min_odds: float | None, remaining: str) -> str:
    combined = combine_parlay([c.american for c in legs])
    lines = [
        f"# {sport.upper()} {len(legs)}-leg {mode} ticket",
        "",
        f"Book: `{legs[0].book}` (Hard Rock FL preferred; fallback DK/FD).",
        "Independent parlay math — **confirm combined price in the Hard Rock app**.",
        f"Odds API requests remaining: `{remaining}`",
        "",
        "| # | Event | Pick | Odds | Context |",
        "|---|-------|------|------|---------|",
    ]
    for i, leg in enumerate(legs, start=1):
        when = leg.commence.replace("T", " ")[:16] + "Z"
        ctx = (leg.notes or "").replace("|", "/")
        lines.append(
            f"| {i} | {leg.event} ({when}) | **{leg.team}** | {_fmt_american(leg.american)} | {ctx} |"
        )
    hit = True if min_odds is None else combined + 1e-9 >= min_odds
    lines += [
        "",
        f"**Combined (est.): {_fmt_american(combined)}**"
        + (f"  · target {_fmt_american(min_odds)} {'HIT' if hit else 'SHORT'}" if min_odds is not None else ""),
        "",
        "Punch these as a **straight parlay** (not SGP unless they are the same game).",
        "Weather/pitcher notes are **heuristics from free APIs**, not a model. Confirm the number in-app.",
        "",
    ]
    if not hit:
        lines.append("Could not reach the min odds with the live board — add a dog in-app or drop a chalk leg.")
    return "\n".join(lines)


def parse_american_flag(raw: str) -> float:
    s = raw.strip().replace("+", "")
    return float(s)


def main() -> int:
    load_dotenv()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("sport", choices=sorted(SPORTS), help="mlb / ufc / nfl / nba / nhl / wnba")
    p.add_argument("--legs", type=int, required=True)
    p.add_argument("--mode", choices=("strong", "lotto", "unders"), default="strong")
    p.add_argument("--min-odds", default=None, help="e.g. +300 — solver swaps dogs until hit")
    p.add_argument("--hours", type=float, default=36, help="only events starting within this many hours")
    p.add_argument("--no-context", action="store_true", help="skip Open-Meteo / MLB Stats (odds only)")
    args = p.parse_args()
    if args.legs < 2:
        raise SystemExit("--legs must be >= 2")

    key = os.environ.get("THE_ODDS_API_KEY", "").strip()
    if not key:
        print("Missing THE_ODDS_API_KEY in .env", file=sys.stderr)
        return 1

    markets = "totals" if args.mode == "unders" else "h2h"
    payload = fetch_odds(key, SPORTS[args.sport], markets)
    meta = next((x.get("_meta") for x in payload if isinstance(x, dict) and "_meta" in x), {})
    remaining = str(meta.get("remaining", "?"))
    sides = flatten_under_sides(payload) if args.mode == "unders" else flatten_ml_sides(payload)
    sides = filter_horizon(sides, args.hours)
    if not sides:
        print("No live prices for that sport/market (or Hard Rock/DK not listing).", file=sys.stderr)
        return 2

    scores: dict[str, int] = {}
    if not args.no_context and args.sport in {"mlb", "nfl", "nba", "nhl", "wnba"}:
        try:
            sides, ctx_map = annotate_sides(args.sport, sides)
            scores = {k: v.score for k, v in ctx_map.items()}
        except Exception as exc:  # noqa: BLE001 — context is optional
            print(f"Free context skipped ({exc})", file=sys.stderr)

    min_odds = parse_american_flag(args.min_odds) if args.min_odds else None
    if args.mode == "unders":
        legs = pick_unders(sides, legs=args.legs, min_odds=min_odds, scores=scores)
    else:
        legs = pick_legs(sides, legs=args.legs, mode=args.mode, min_odds=min_odds)
    print(render_ticket(legs, sport=args.sport, mode=args.mode, min_odds=min_odds, remaining=remaining))
    out = ROOT / "briefs" / f"{datetime.now(timezone.utc).date().isoformat()}_{args.sport}-{args.mode}-{args.legs}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        render_ticket(legs, sport=args.sport, mode=args.mode, min_odds=min_odds, remaining=remaining),
        encoding="utf-8",
    )
    print(f"\nSaved {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
