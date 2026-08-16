#!/usr/bin/env python3
"""Daily Hard Rock edge card — market-relative, not a projection model.

Reads a two-sided CSV (sharp/reference vs Hard Rock) or optional The Odds API
snapshot, de-vigs the reference, ranks +EV vs the HR price.

  python scripts/daily_edge_card.py --csv config/hr_lines.example.csv
  python scripts/daily_edge_card.py --csv path.csv --bankroll 1000 --out briefs/2026-08-15_edge-card.md

Never auto-submits. Operator verifies the live HR number before betting.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from env_load import load_dotenv  # noqa: E402
from odds import expected_value, kelly_fraction, multiplicative_devig  # noqa: E402

DEFAULT_MIN_EV = 0.02
DEFAULT_MAX_HOLD = 0.08
DEFAULT_MAX_AGE_HOURS = 6.0
DEFAULT_KELLY_FRAC = 0.25


@dataclass(frozen=True)
class Candidate:
    event: str
    sport: str
    market: str
    outcome: str
    kickoff: str
    captured_at: str
    ref_book: str
    ref_yes: float
    ref_no: float
    hr_price: float
    fair_p: float
    hold: float
    ev: float
    kelly: float
    action: str
    notes: str


def _parse_american(raw: str) -> float:
    s = str(raw).strip().replace("+", "")
    return float(s)


def _parse_dt(raw: str) -> datetime | None:
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def age_hours(captured_at: str, now: datetime) -> float | None:
    dt = _parse_dt(captured_at)
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    return (now - dt).total_seconds() / 3600.0


def classify(ev: float, hold: float, age_h: float | None, *, min_ev: float, max_hold: float, max_age: float) -> tuple[str, str]:
    notes: list[str] = []
    if hold > max_hold:
        return "PASS", f"reference hold {hold:.1%} above {max_hold:.0%} cap"
    if age_h is not None and age_h > max_age:
        return "PASS", f"stale capture {age_h:.1f}h > {max_age:.0f}h"
    if ev >= min_ev:
        return "BET", "edge vs de-vigged reference"
    if ev > 0:
        return "WATCH", f"positive EV {ev:.2%} below {min_ev:.0%} gate"
    notes.append("no edge vs de-vigged reference")
    return "PASS", "; ".join(notes)


def load_csv(path: Path, *, now: datetime, min_ev: float, max_hold: float, max_age: float, kelly_frac: float) -> list[Candidate]:
    rows: list[Candidate] = []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {
            "event",
            "sport",
            "market",
            "outcome",
            "kickoff",
            "captured_at",
            "ref_book",
            "ref_yes",
            "ref_no",
            "hr_price",
        }
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise SystemExit(f"CSV missing columns {sorted(required)}; got {reader.fieldnames}")
        for i, row in enumerate(reader, start=2):
            if not any((v or "").strip() for v in row.values()):
                continue
            try:
                yes = _parse_american(row["ref_yes"])
                no = _parse_american(row["ref_no"])
                hr = _parse_american(row["hr_price"])
                dv = multiplicative_devig(yes, no)
                ev = expected_value(dv.fair_a, hr)
                k = kelly_fraction(dv.fair_a, hr, fraction=kelly_frac)
                age = age_hours(row["captured_at"], now)
                action, notes = classify(
                    ev, dv.hold, age, min_ev=min_ev, max_hold=max_hold, max_age=max_age
                )
                rows.append(
                    Candidate(
                        event=row["event"].strip(),
                        sport=row["sport"].strip(),
                        market=row["market"].strip(),
                        outcome=row["outcome"].strip(),
                        kickoff=row["kickoff"].strip(),
                        captured_at=row["captured_at"].strip(),
                        ref_book=row["ref_book"].strip(),
                        ref_yes=yes,
                        ref_no=no,
                        hr_price=hr,
                        fair_p=dv.fair_a,
                        hold=dv.hold,
                        ev=ev,
                        kelly=k,
                        action=action,
                        notes=notes,
                    )
                )
            except (ValueError, KeyError) as exc:
                raise SystemExit(f"{path}:{i}: {exc}") from exc
    rows.sort(key=lambda c: c.ev, reverse=True)
    return rows


def fetch_odds_api(api_key: str, sport: str) -> dict:
    url = (
        f"https://api.the-odds-api.com/v4/sports/{sport}/odds/"
        f"?regions=us&markets=h2h,spreads,totals&oddsFormat=american&apiKey={api_key}"
    )
    req = Request(url, headers={"User-Agent": "gambling-wiki-edge-card/1.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as exc:
        raise SystemExit(f"The Odds API HTTP {exc.code}") from exc
    except URLError as exc:
        raise SystemExit(f"The Odds API unreachable: {exc}") from exc


def render_markdown(cands: list[Candidate], *, bankroll: float, source: str, generated: str) -> str:
    bets = [c for c in cands if c.action == "BET"]
    watch = [c for c in cands if c.action == "WATCH"]
    lines = [
        f"# Daily edge card — {generated[:10]}",
        "",
        "Market-relative only: de-vigged **reference** vs **Hard Rock**. Not a projection model.",
        "Verify the live HR number in-app before betting. No auto-submit.",
        "",
        f"- Generated: `{generated}`",
        f"- Source: `{source}`",
        f"- Bankroll for Kelly $: `{bankroll:.0f}`",
        f"- BET / WATCH / PASS: **{len(bets)}** / **{len(watch)}** / **{len(cands) - len(bets) - len(watch)}**",
        "",
        "## BET",
        "",
        "| Event | Market | Pick | HR | Fair p | EV | 1/4 Kelly $ | Notes |",
        "|-------|--------|------|----|--------|----|-------------|-------|",
    ]
    if not bets:
        lines.append("| — | — | — | — | — | — | — | none cleared 2% EV gate |")
    for c in bets:
        stake = bankroll * c.kelly
        hr = f"{c.hr_price:+.0f}" if c.hr_price > 0 else f"{c.hr_price:.0f}"
        lines.append(
            f"| {c.event} | {c.market} | {c.outcome} | {hr} | {c.fair_p:.1%} | {c.ev:.2%} | ${stake:.0f} | {c.notes} |"
        )
    lines += [
        "",
        "## WATCH",
        "",
        "| Event | Market | Pick | HR | EV | Notes |",
        "|-------|--------|------|----|----|-------|",
    ]
    if not watch:
        lines.append("| — | — | — | — | — | — |")
    for c in watch:
        hr = f"{c.hr_price:+.0f}" if c.hr_price > 0 else f"{c.hr_price:.0f}"
        lines.append(f"| {c.event} | {c.market} | {c.outcome} | {hr} | {c.ev:.2%} | {c.notes} |")
    lines += [
        "",
        "## Promo / SGP (manual)",
        "",
        "Do **not** mix lottery SGPs into this table. Wiki: parlays are promo conversion, not core +EV.",
        "Log boost tickets separately; do not put them in the CLV journal.",
        "",
        "## Next",
        "",
        "1. Confirm each BET price still live on Hard Rock.",
        "2. Place manually.",
        "3. Tomorrow: record close vs your price (CLV ledger — P1).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    load_dotenv()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--csv", type=Path, help="Two-sided line CSV (see config/hr_lines.example.csv)")
    p.add_argument("--out", type=Path, help="Markdown output path")
    p.add_argument("--bankroll", type=float, default=1000.0)
    p.add_argument("--min-ev", type=float, default=DEFAULT_MIN_EV)
    p.add_argument("--max-hold", type=float, default=DEFAULT_MAX_HOLD)
    p.add_argument("--max-age-hours", type=float, default=DEFAULT_MAX_AGE_HOURS)
    p.add_argument("--kelly-frac", type=float, default=DEFAULT_KELLY_FRAC)
    p.add_argument(
        "--fetch-odds-api",
        action="store_true",
        help="Print raw The Odds API JSON (needs THE_ODDS_API_KEY). Does not replace --csv.",
    )
    p.add_argument("--odds-sport", default="americanfootball_nfl")
    args = p.parse_args()

    if args.fetch_odds_api:
        key = os.environ.get("THE_ODDS_API_KEY", "").strip()
        if not key:
            print("Set THE_ODDS_API_KEY (never commit it).", file=sys.stderr)
            return 1
        data = fetch_odds_api(key, args.odds_sport)
        print(json.dumps(data, indent=2)[:8000])
        print("\n# Paste sharp + HR two-sided prices into the CSV; then rerun without --fetch-odds-api.")
        return 0

    csv_path = args.csv or (ROOT / "config" / "hr_lines.example.csv")
    if not csv_path.is_file():
        print(f"Missing CSV: {csv_path}", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    cands = load_csv(
        csv_path,
        now=now,
        min_ev=args.min_ev,
        max_hold=args.max_hold,
        max_age=args.max_age_hours,
        kelly_frac=args.kelly_frac,
    )
    generated = now.isoformat(timespec="seconds")
    md = render_markdown(cands, bankroll=args.bankroll, source=str(csv_path), generated=generated)
    print(md)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(md, encoding="utf-8")
        print(f"\nWrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
