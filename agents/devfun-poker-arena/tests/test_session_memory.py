"""Tests for session villain memory (Agent Memory Test → poker adaptation)."""
from session_memory import (
    exploit_from_memory,
    update_session_memory,
    villain_memory_for_table,
)


def test_villain_memory_abstains_without_samples():
    state = {"session_villain_memory": {}}
    table = {
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
        "street": "Flop",
        "actionHistory": [],
    }
    mem = villain_memory_for_table(state, table)
    assert mem.get("note") or not mem.get("villains")


def test_villain_memory_aggro_after_samples():
    state = {
        "session_villain_memory": {
            "v1": {"aggressive_acts": 6, "passive_acts": 1, "samples": 7},
        }
    }
    table = {
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
    }
    mem = villain_memory_for_table(state, table)
    assert mem["villains"]["v1"]["label"] == "aggro"
    margins = exploit_from_memory(mem)
    assert margins.get("fold_slack_delta", 0) > 0


def test_update_session_memory_records_bets():
    state = {}
    table = {
        "selfSeatNumber": 1,
        "street": "Flop",
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
        "actionHistory": [
            {"street": "Flop", "action": "bet", "seatNumber": 2, "amount": 50},
        ],
    }
    update_session_memory(state, table)
    assert state["session_villain_memory"]["v1"]["aggressive_acts"] == 1
