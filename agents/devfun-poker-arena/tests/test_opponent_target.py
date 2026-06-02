"""Tests for multi-way opponent targeting helpers."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from opponent_target import (  # noqa: E402
    active_villain_count,
    is_multiway,
    last_aggressor_seat,
    select_target_agent_id,
    spot_kind,
)


def _table(**kwargs):
    base = {
        "selfSeatNumber": 1,
        "bigBlindChips": 2,
        "street": "Flop",
        "seats": [
            {"seatNumber": 1, "agentId": "hero", "status": "Active", "currentBetChips": 0},
            {"seatNumber": 2, "agentId": "v2", "status": "Active", "currentBetChips": 20,
             "trainingArchetype": "maniac"},
            {"seatNumber": 3, "agentId": "v3", "status": "Active", "currentBetChips": 0,
             "trainingArchetype": "rock"},
            {"seatNumber": 4, "agentId": "v4", "status": "Folded", "currentBetChips": 0},
        ],
        "allowedActions": {"callChips": 20, "canRaise": True},
    }
    base.update(kwargs)
    return base


def test_multiway_count():
    assert active_villain_count(_table()) == 2
    assert is_multiway(_table()) is True


def test_spot_facing_raise():
    assert spot_kind(_table()) == "facing_raise"


def test_last_aggressor_by_wager():
    assert last_aggressor_seat(_table()) == 2


def test_select_target_aggressor():
    aid, reason, meta = select_target_agent_id(_table())
    assert aid == "v2"
    assert reason == "last_aggressor"
    assert meta["aggressorSeat"] == 2
    assert meta["multiway"] is True


def test_unopened_steal_targets_rock():
    t = _table(allowedActions={"callChips": 0, "canRaise": False})
    aid, reason, meta = select_target_agent_id(t)
    assert reason == "steal_vs_rock"
    assert aid == "v3"
    assert meta["spot"] == "unopened"
