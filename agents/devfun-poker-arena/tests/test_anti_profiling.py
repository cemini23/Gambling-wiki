"""Tests for prod anti-profiling helpers."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from action_mix import (  # noqa: E402
    fold_probability_marginal,
    hand_stable_uniform,
    mix_postflop_enabled,
    resolve_postflop_call_fold,
)
from output_sanitize import maybe_sanitize_action, sanitize_output_enabled  # noqa: E402


def _table(**overrides):
    base = {
        "tableId": "tbl_mix_test",
        "street": "Flop",
        "potChips": 100,
        "boardCards": ["Kh", "7d", "2c"],
        "selfSeatNumber": 1,
        "seats": [{"seatNumber": 1, "holeCards": ["As", "Qd"]}],
        "allowedActions": {"callChips": 50},
    }
    base.update(overrides)
    return base


def test_hand_stable_uniform_is_deterministic():
    t = _table()
    assert hand_stable_uniform(t, salt="x") == hand_stable_uniform(t, salt="x")
    assert hand_stable_uniform(t, salt="x") != hand_stable_uniform(t, salt="y")


def test_fold_probability_marginal_band():
    assert fold_probability_marginal(0.20, 0.30, 0.06, 0.04) == 1.0
    assert fold_probability_marginal(0.40, 0.30, 0.06, 0.04) == 0.0
    mid = fold_probability_marginal(0.30, 0.30, 0.06, 0.04)
    assert 0.0 < mid < 1.0


def test_mix_disabled_uses_deterministic_marginal():
    os.environ.pop("CEMINI_MIX_POSTFLOP", None)
    assert not mix_postflop_enabled()
    action, _ = resolve_postflop_call_fold(
        _table(), equity=0.28, pot_odds=0.30, fold_slack=0.06, call_margin=0.04,
        available=["fold", "call"],
    )
    assert action == "fold"
    action2, _ = resolve_postflop_call_fold(
        _table(), equity=0.32, pot_odds=0.30, fold_slack=0.06, call_margin=0.04,
        available=["fold", "call"],
    )
    assert action2 == "fold"
    action3, _ = resolve_postflop_call_fold(
        _table(), equity=0.40, pot_odds=0.30, fold_slack=0.06, call_margin=0.04,
        available=["fold", "call"],
    )
    assert action3 == "call"


def test_mix_enabled_stable_in_marginal_band():
    os.environ["CEMINI_MIX_POSTFLOP"] = "1"
    try:
        t = _table()
        a1, _ = resolve_postflop_call_fold(
            t, equity=0.30, pot_odds=0.30, fold_slack=0.06, call_margin=0.04,
            available=["fold", "call"],
        )
        a2, _ = resolve_postflop_call_fold(
            t, equity=0.30, pot_odds=0.30, fold_slack=0.06, call_margin=0.04,
            available=["fold", "call"],
        )
        assert a1 == a2
        assert a1 in ("fold", "call")
    finally:
        os.environ.pop("CEMINI_MIX_POSTFLOP", None)


def test_sanitize_strips_telegraphy():
    os.environ["CEMINI_SANITIZE_OUTPUT"] = "1"
    try:
        assert sanitize_output_enabled()
        raw = {
            "action": "fold",
            "message": "open_defend@BTN: survival (survival)",
            "reasoning": '{sk: "wet_board@SB|stub|rock", ke: "32% eq"}',
        }
        out = maybe_sanitize_action(raw)
        assert out["message"] == "fold"
        assert "sk:" not in out["reasoning"]
        assert "32%" not in out["reasoning"]
    finally:
        os.environ.pop("CEMINI_SANITIZE_OUTPUT", None)
