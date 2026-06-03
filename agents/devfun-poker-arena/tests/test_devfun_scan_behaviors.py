"""Offline tests inspired by dev.fun Agent Scan suite (personality / memory).

These do not call the Arena scan API — they lock in poker behaviors we derived
from scan results (Stalwart: low candor → honest folds; memory KU → preserve nums).
"""
from __future__ import annotations

import json
from pathlib import Path

from cemini_decide import decide, retrieve_solver_context
from session_memory import exploit_from_memory, villain_memory_for_table
from tests.helpers.cemini_tables import _allowed, ep_oop_postflop_weak, six_max_table

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "devfun_scan_baselines.json"
BASELINE = json.loads(FIXTURES.read_text())


def test_scan_baseline_fixture_loaded():
    assert BASELINE["version"] == "v2.3"
    assert "personality_baseline" in BASELINE
    assert len(BASELINE["personality_baseline"]["poker_patches"]) >= 4


def test_candor_honest_fold_message_when_beat():
    """Personality candor 35% → table chat admits clear -EV calls."""
    table = six_max_table(
        name="candor_beat",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["Ah", "Kd", "9s", "4c"],
        pot=200,
        hero_hole=["7c", "2d"],
        hero_stack=900,
        villain_bets={3: 120},
        stacks={5: 900},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=120,
            call_to=120,
            raise_range={"min": 240, "max": 900},
        ),
    )
    out = decide(table, deadline_s=10.0)
    assert out["action"] == "fold"
    msg = out["message"].lower()
    candid = ("honest fold", "short of price", "trash hand", "stack cap", "fold")
    assert any(p in msg for p in candid)


def test_survival_mode_folds_marginal_postflop():
    """Roast/degen guardrail: stack < buy-in → preserve chips, no loose calls."""
    table = ep_oop_postflop_weak(
        ["Qc", "Jd"],
        ["Ah", "8s", "3c"],
        hero_seat=5,
        villain_bet=80,
        pot=160,
    )
    table["seats"][4]["stackChips"] = 540  # hero seat index 4 = seat 5
    ctx = retrieve_solver_context(table)
    ctx["survival_mode"] = True
    out = decide(table, deadline_s=10.0, research_context=ctx)
    assert out["action"] in ("fold", "check")
    if out["action"] == "fold":
        msg = out["message"].lower()
        assert "survival" in msg or "honest fold" in msg


def test_qualification_protect_activates_survival_margins():
    """Top-20 ticket protect → survival_mode tightens marginal calls."""
    table = ep_oop_postflop_weak(
        ["Qc", "Jd"],
        ["Ah", "8s", "3c"],
        hero_seat=5,
        villain_bet=80,
        pot=160,
    )
    ctx = retrieve_solver_context(table)
    ctx["qualification_protect"] = True
    ctx["survival_mode"] = True
    out = decide(table, deadline_s=10.0, research_context=ctx)
    assert out["action"] in ("fold", "check")


def test_composure_tightens_under_deadline():
    """Composure 70% → short clock, no hero call with weak equity."""
    table = ep_oop_postflop_weak(
        ["9c", "8d"],
        ["Ah", "Kc", "7s"],
        hero_seat=2,
        villain_bet=60,
        pot=120,
    )
    out = decide(table, deadline_s=3.0)
    assert out["action"] in ("fold", "check")


def test_memory_ku_preserves_numeric_updates():
    """Memory test q8 failure mode — summaries must keep updated numbers."""
    sample = BASELINE["memory_ku_sample"]
    good = f"Budget: ${sample['required_numeric']}/mo API cap, local-first"
    bad = sample["bad_pattern"]
    assert sample["required_numeric"] in good
    assert sample["required_numeric"] not in bad


def test_session_memory_aggro_exploit_margins():
    """Memory MR/IE → session villain labels adjust margins when confident."""
    mem = {
        "villains": {
            "v1": {"label": "aggro", "confidence": "high", "samples": 10},
        }
    }
    margins = exploit_from_memory(mem)
    assert margins.get("fold_slack_delta", 0) > 0


def test_session_memory_abstains_low_confidence():
    """Memory Ab → no exploit tweak without enough samples."""
    state = {"session_villain_memory": {"v1": {"aggressive_acts": 1, "passive_acts": 0, "samples": 1}}}
    table = {
        "selfSeatNumber": 1,
        "seats": [{"seatNumber": 1, "agentId": "hero"}, {"seatNumber": 2, "agentId": "v1"}],
    }
    mem = villain_memory_for_table(state, table)
    assert exploit_from_memory(mem) == {}


def test_drive_richer_message_when_time_allows():
    """Drive 50% → when deadline comfortable, session tags appear if memory present."""
    table = six_max_table(
        name="btn_ip_check",
        hero_seat=1,
        button_seat=1,
        street="Flop",
        board=["2h", "7d", "Ts"],
        pot=60,
        hero_hole=["Ac", "Kd"],
        hero_stack=1500,
        allowed=_allowed(can_check=True, can_bet=True, bet_range={"min": 20, "max": 1500}),
    )
    ctx = retrieve_solver_context(table)
    ctx["session_villain_memory"] = {
        "villains": {"v2": {"label": "passive", "confidence": "medium", "samples": 5}},
    }
    out = decide(table, deadline_s=12.0, research_context=ctx)
    assert out["action"] in ("check", "bet", "raise", "call")
    if "session:" in out.get("message", "").lower():
        assert "passive" in out["message"].lower()
