"""Qualification protection — rank + chip buffer gates for lobby decide()."""
from __future__ import annotations

from qualification_guard import DEFAULT_BUFFER_CHIPS, fetch_qualification_status


class _FakeClient:
    def __init__(self, me: dict, cutoff_score: int):
        self._me = me
        self._cutoff = cutoff_score

    def get(self, path: str) -> dict:
        if path == "/agent/me":
            return self._me
        if "leaderboard" in path and "offset=" in path:
            return {"data": [{"totalScore": self._cutoff}]}
        raise AssertionError(path)


def test_protect_when_rank_in_zone_and_buffer_ge_1000():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 10, "totalScore": 4538}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is True
    assert st["buffer_chips"] == 2528


def test_no_protect_when_buffer_below_threshold():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 15, "totalScore": 2800}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is False
    assert st["buffer_chips"] == 790


def test_no_protect_when_rank_outside_top_20():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 25, "totalScore": 5000}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is False


def test_default_buffer_is_1000():
    assert DEFAULT_BUFFER_CHIPS == 1000
