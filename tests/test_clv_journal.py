"""CLV journal grades a manual CSV. No live odds and no bet placement."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from clv_journal import grade_close, load_ledger, summarize  # noqa: E402
from odds import expected_value, multiplicative_devig  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
HEADER = (
    "ticket_id,placed_at,event,sport,market,outcome,book,price_taken,"
    "stake,close_book,close_yes,close_no,ticket_kind"
)


def _write(tmp_path: Path, body: str) -> Path:
    path = tmp_path / "journal.csv"
    path.write_text(HEADER + "\n" + body, encoding="utf-8")
    return path


def test_positive_clv_matches_devigged_close(tmp_path: Path):
    path = _write(
        tmp_path,
        "T1,2026-01-01T18:00:00Z,A at B,nfl,ml,A,hard-rock,+100,10,pinnacle,-130,+110,straight\n",
    )
    rows = load_ledger(path)
    fair = multiplicative_devig(-130, 110)
    assert rows[0].status == "closed"
    assert rows[0].clv == pytest.approx(expected_value(fair.fair_a, 100))
    assert rows[0].clv is not None and rows[0].clv > 0
    assert grade_close(100, -130, 110)[2] == pytest.approx(rows[0].clv)


def test_worse_price_than_close_is_negative(tmp_path: Path):
    path = _write(
        tmp_path,
        "T1,2026-01-01T18:00:00Z,A at B,nfl,spread,A -3.5,hard-rock,-150,,pinnacle,-110,-110,straight\n",
    )
    row = load_ledger(path)[0]
    assert row.clv is not None and row.clv < 0
    stats = summarize(load_ledger(path))
    assert stats["stake_weighted_clv"] is None


def test_open_row_stays_out_of_the_mean(tmp_path: Path):
    path = _write(
        tmp_path,
        "T1,2026-01-01T18:00:00Z,A at B,nfl,total,Over 44.5,hard-rock,-110,,,,,straight\n",
    )
    stats = summarize(load_ledger(path))
    assert stats["n_open"] == 1
    assert stats["n_closed"] == 0
    assert stats["mean_clv"] is None


def test_boost_sgp_and_parlay_are_refused(tmp_path: Path):
    for kind in ("boost", "sgp", "parlay"):
        path = _write(
            tmp_path,
            f"T1,2026-01-01T18:00:00Z,A at B,nfl,ml,A,hard-rock,+100,10,pinnacle,-130,+110,{kind}\n",
        )
        with pytest.raises(SystemExit, match="stays out of the CLV journal"):
            load_ledger(path)


def test_one_close_side_is_refused(tmp_path: Path):
    path = _write(
        tmp_path,
        "T1,2026-01-01T18:00:00Z,A at B,nfl,ml,A,hard-rock,+100,10,pinnacle,-130,,straight\n",
    )
    with pytest.raises(SystemExit, match="close needs both sides"):
        load_ledger(path)


def test_stake_weighted_mean_uses_only_closed_rows(tmp_path: Path):
    path = _write(
        tmp_path,
        "\n".join(
            [
                "T1,2026-01-01T18:00:00Z,A at B,nfl,ml,A,hard-rock,+100,10,pinnacle,-130,+110,straight",
                "T2,2026-01-01T18:05:00Z,A at B,nfl,ml,B,hard-rock,-150,30,pinnacle,-110,-110,straight",
                "",
            ]
        ),
    )
    rows = load_ledger(path)
    stats = summarize(rows)
    weights = [(row.clv or 0.0) * (row.stake or 0.0) for row in rows]
    stakes = [row.stake or 0.0 for row in rows]
    assert stats["stake_weighted_clv"] == pytest.approx(sum(weights) / sum(stakes))


def test_example_csv_has_two_closed_and_one_open():
    rows = load_ledger(ROOT / "config" / "clv_journal.example.csv")
    stats = summarize(rows)
    assert stats["n_closed"] == 2
    assert stats["n_open"] == 1
    assert stats["stake_weighted_clv"] is None


def test_script_does_not_call_live_odds():
    text = (SCRIPTS / "clv_journal.py").read_text(encoding="utf-8")
    assert "urlopen" not in text
    assert "the-odds-api" not in text
    assert "closings" not in text
    assert "47.04" not in text
