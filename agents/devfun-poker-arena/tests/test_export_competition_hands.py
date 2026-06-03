"""Tests for competition hand export normalizers."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_competition_hands import (  # noqa: E402
    build_summary,
    normalize_submission,
    normalize_table,
)


def test_normalize_table_all_seats() -> None:
    raw = {
        "id": "tbl1",
        "boardCards": ["Ah", "Kd", "2c"],
        "seats": [
            {"agentId": "a1", "agentHandle": "hero", "seatNumber": 1,
             "holeCards": ["As", "Ks"], "payoutChips": 100, "stackChips": 1100},
            {"agentId": "a2", "agentHandle": "villain", "seatNumber": 2,
             "holeCards": ["Qh", "Qd"], "payoutChips": -100, "stackChips": 900},
        ],
        "winners": [{"agentId": "a1", "agentName": "hero", "amount": 100, "handName": "Pair"}],
    }
    rec = normalize_table(raw, competition_id="comp1")
    assert rec["record_type"] == "table"
    assert rec["table_id"] == "tbl1"
    assert len(rec["seats"]) == 2
    assert rec["seats"][1]["hole_cards"] == ["Qh", "Qd"]


def test_normalize_submission() -> None:
    raw = {
        "id": "sub1",
        "data": {"seatNumber": 3, "holeCards": ["5d", "9c"], "payoutChips": 0,
                 "stackChips": 9108, "agentHandle": "cemini_wiki_poker"},
        "challenge": {
            "id": "tbl2",
            "result": {
                "boardCards": ["Tc", "2s", "6h"],
                "winners": [{"agentName": "kestrel.py", "amount": 5, "handName": "High Card"}],
            },
            "data": {"tableNumber": 2323, "smallBlindChips": 1, "bigBlindChips": 2},
        },
        "submittedAt": 1780522525822,
    }
    rec = normalize_submission(raw, competition_id="comp1")
    assert rec["record_type"] == "submission"
    assert rec["table_id"] == "tbl2"
    assert rec["hole_cards"] == ["5d", "9c"]


def test_build_summary_win_rate() -> None:
    tables = [
        {
            "seats": [
                {"handle": "hero", "payout_chips": 50},
                {"handle": "villain", "payout_chips": -50},
            ],
            "winners": [{"handle": "hero", "amount": 50}],
        },
        {
            "seats": [
                {"handle": "hero", "payout_chips": -30},
                {"handle": "villain", "payout_chips": 30},
            ],
            "winners": [{"handle": "villain", "amount": 30}],
        },
        {
            "seats": [
                {"handle": "hero", "payout_chips": 10},
                {"handle": "villain", "payout_chips": -10},
            ],
            "winners": [{"handle": "hero", "amount": 10}],
        },
    ]
    summary = build_summary(tables, [], [])
    hero = next(r for r in summary["top_showdown_performers"] if r["handle"] == "hero")
    assert hero["showdowns"] == 3
    assert hero["wins"] == 2
