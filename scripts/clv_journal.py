#!/usr/bin/env python3
"""Grade a manual CLV ledger against the de-vigged close.

  python scripts/clv_journal.py --csv config/clv_journal.example.csv
  python scripts/clv_journal.py --csv briefs/clv-journal.csv --out briefs/2026-10-10_clv-grade.md

The CSV is the operator log. This script reads it and writes a grade.
It does not place a bet and it does not call an odds API.
A boost, SGP, or parlay row is refused. Keep those tickets in a separate file.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from odds import expected_value, multiplicative_devig  # noqa: E402

REQUIRED = (
    "ticket_id",
    "placed_at",
    "event",
    "sport",
    "market",
    "outcome",
    "book",
    "price_taken",
    "close_book",
    "close_yes",
    "close_no",
)
STRAIGHT = {"", "straight"}


@dataclass(frozen=True)
class JournalRow:
    ticket_id: str
    placed_at: str
    event: str
    sport: str
    market: str
    outcome: str
    book: str
    price_taken: float
    stake: float | None
    close_book: str
    close_yes: float | None
    close_no: float | None
    status: str
    close_fair_p: float | None
    close_hold: float | None
    clv: float | None


def _parse_american(raw: str) -> float:
    text = str(raw).strip().replace("+", "")
    if not text:
        raise ValueError("missing American price")
    price = float(text)
    if price == 0:
        raise ValueError("American odds cannot be 0")
    return price


def _blank(raw: str | None) -> bool:
    return not (raw or "").strip()


def _require_text(row: dict[str, str], key: str) -> str:
    value = (row.get(key) or "").strip()
    if not value:
        raise ValueError(f"missing {key}")
    return value


def _parse_placed_at(raw: str) -> str:
    try:
        datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"placed_at is not a timestamp: {raw}") from exc
    return raw


def _parse_stake(raw: str | None) -> float | None:
    if _blank(raw):
        return None
    stake = float(str(raw).strip())
    if stake <= 0:
        raise ValueError("stake must be > 0 when it is set")
    return stake


def grade_close(price_taken: float, close_yes: float, close_no: float) -> tuple[float, float, float]:
    """CLV is EV of the taken price against the de-vigged close.

    close_yes is the side that was bet. close_no is the other side.
    """
    fair = multiplicative_devig(close_yes, close_no)
    return fair.fair_a, fair.hold, expected_value(fair.fair_a, price_taken)


def load_ledger(path: Path) -> list[JournalRow]:
    rows: list[JournalRow] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or not set(REQUIRED).issubset(set(reader.fieldnames)):
            raise SystemExit(f"CSV missing columns {list(REQUIRED)}; got {reader.fieldnames}")
        for line_no, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue
            try:
                ticket_id = _require_text(row, "ticket_id")
                if ticket_id in seen:
                    raise ValueError(f"duplicate ticket_id {ticket_id}")
                seen.add(ticket_id)
                kind = (row.get("ticket_kind") or "").strip().lower()
                if kind not in STRAIGHT:
                    raise ValueError(
                        f"{ticket_id}: ticket_kind {kind!r} stays out of the CLV journal"
                    )
                price_taken = _parse_american(_require_text(row, "price_taken"))
                stake = _parse_stake(row.get("stake"))
                close_yes_raw = row.get("close_yes")
                close_no_raw = row.get("close_no")
                yes_blank = _blank(close_yes_raw)
                no_blank = _blank(close_no_raw)
                if yes_blank != no_blank:
                    raise ValueError(f"{ticket_id}: close needs both sides")
                if yes_blank:
                    rows.append(
                        JournalRow(
                            ticket_id=ticket_id,
                            placed_at=_parse_placed_at(_require_text(row, "placed_at")),
                            event=_require_text(row, "event"),
                            sport=_require_text(row, "sport"),
                            market=_require_text(row, "market"),
                            outcome=_require_text(row, "outcome"),
                            book=_require_text(row, "book"),
                            price_taken=price_taken,
                            stake=stake,
                            close_book=(row.get("close_book") or "").strip(),
                            close_yes=None,
                            close_no=None,
                            status="open",
                            close_fair_p=None,
                            close_hold=None,
                            clv=None,
                        )
                    )
                    continue
                close_yes = _parse_american(close_yes_raw or "")
                close_no = _parse_american(close_no_raw or "")
                fair_p, hold, clv = grade_close(price_taken, close_yes, close_no)
                rows.append(
                    JournalRow(
                        ticket_id=ticket_id,
                        placed_at=_parse_placed_at(_require_text(row, "placed_at")),
                        event=_require_text(row, "event"),
                        sport=_require_text(row, "sport"),
                        market=_require_text(row, "market"),
                        outcome=_require_text(row, "outcome"),
                        book=_require_text(row, "book"),
                        price_taken=price_taken,
                        stake=stake,
                        close_book=_require_text(row, "close_book"),
                        close_yes=close_yes,
                        close_no=close_no,
                        status="closed",
                        close_fair_p=fair_p,
                        close_hold=hold,
                        clv=clv,
                    )
                )
            except (ValueError, KeyError) as exc:
                raise SystemExit(f"{path}:{line_no}: {exc}") from exc
    return rows


def summarize(rows: list[JournalRow]) -> dict[str, float | int | None]:
    closed = [row for row in rows if row.status == "closed" and row.clv is not None]
    mean: float | None = None
    weighted: float | None = None
    if closed:
        mean = sum(row.clv or 0.0 for row in closed) / len(closed)
        if all(row.stake is not None for row in closed):
            total_stake = sum(row.stake or 0.0 for row in closed)
            weighted = sum((row.clv or 0.0) * (row.stake or 0.0) for row in closed) / total_stake
    return {
        "n_open": sum(1 for row in rows if row.status == "open"),
        "n_closed": len(closed),
        "mean_clv": mean,
        "stake_weighted_clv": weighted,
    }


def _american(price: float) -> str:
    if price > 0:
        return f"+{price:.0f}"
    return f"{price:.0f}"


def render_markdown(rows: list[JournalRow], *, source: str) -> str:
    stats = summarize(rows)
    lines = [
        "# CLV journal grade",
        "",
        "Each closed row is the EV of the price taken against the multiplicative de-vig of the close.",
        "`close_yes` is the side you bet. The script does not place a bet.",
        "",
        f"- Source: `{source}`",
        f"- Closed / open: **{stats['n_closed']}** / **{stats['n_open']}**",
        "",
        "| Ticket | Event | Pick | Taken | Close fair | CLV | Status |",
        "|--------|-------|------|-------|------------|-----|--------|",
    ]
    if not rows:
        lines.append("| — | — | — | — | — | — | no rows |")
    for row in rows:
        fair = "—" if row.close_fair_p is None else f"{row.close_fair_p:.1%}"
        clv = "—" if row.clv is None else f"{row.clv:.2%}"
        lines.append(
            f"| {row.ticket_id} | {row.event} | {row.outcome} | {_american(row.price_taken)} | {fair} | {clv} | {row.status} |"
        )
    lines.append("")
    mean = stats["mean_clv"]
    weighted = stats["stake_weighted_clv"]
    if mean is None:
        lines.append("Mean CLV: no closed row.")
    else:
        lines.append(f"Mean CLV (unweighted): **{mean:.2%}**.")
    if weighted is None:
        lines.append("Stake-weighted mean: skipped until every closed row has a stake.")
    else:
        lines.append(f"Stake-weighted mean: **{weighted:.2%}**.")
    lines += [
        "",
        "This grade is not a bankroll. A boost, SGP, or parlay row stays out of this file.",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, required=True, help="Manual CLV ledger CSV")
    parser.add_argument("--out", type=Path, help="Write the grade markdown to this path")
    args = parser.parse_args(argv)
    rows = load_ledger(args.csv)
    text = render_markdown(rows, source=str(args.csv))
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text, end="" if text.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
