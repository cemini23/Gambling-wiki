"""Preflop guardrails — block trash open-steals (J2o CO leak)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import _blocks_open_steal, _preflop_open  # noqa: E402


def test_blocks_j2o_co_steal():
    assert _blocks_open_steal("J2o", "CO") is True
    assert _blocks_open_steal("72o", "BTN") is True
    assert _blocks_open_steal("A5s", "CO") is False


def test_j2o_chart_fold_not_open_stolen_vs_rock():
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, amount = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.55,
        hand_class="J2o", position="CO", hud_mode="rock", margins=margins,
    )
    assert action in ("fold", "check")
    assert action != "bet"


def test_ep_no_steal_74o_mp():
    from cemini_decide import _preflop_open

    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.60,
        hand_class="74o", position="MP", hud_mode="rock", margins=margins,
    )
    assert action == "fold"


def test_overcommit_fold_weak_hand():
    from cemini_decide import _overcommit_should_fold

    table = {"selfSeatNumber": 1, "seats": [{"seatNumber": 1, "stackChips": 500}]}
    assert _overcommit_should_fold(table, "74o", 0.35, 200) is True
    assert _overcommit_should_fold(table, "AKs", 0.60, 200) is False
