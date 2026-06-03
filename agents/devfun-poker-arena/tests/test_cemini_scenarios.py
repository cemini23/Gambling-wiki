"""Run cemini decide() through the starter-kit 20 scenarios (not skeleton agent)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from cemini_decide import decide  # noqa: E402
from testing import get_scenario, scenarios  # noqa: E402


def test_cemini_all_scenarios_legal():
    for sc in scenarios():
        action = decide(sc.table, deadline_s=10.0)
        legal = set(sc.table["allowedActions"]["availableActions"])
        assert action["action"] in legal, (
            f"{sc.name}: {action['action']!r} not in {sorted(legal)}"
        )
        assert 1 <= len(action.get("reasoning", "")) <= 150
        assert 1 <= len(action.get("message", "")) <= 500


def test_cemini_aa_utg_raises():
    sc = get_scenario("preflop_premium_AA_utg")
    assert decide(sc.table, deadline_s=10.0)["action"] in ("raise", "call", "all-in")


def test_cemini_72o_vs_3bet_no_raise():
    sc = get_scenario("preflop_trash_72o_bb_facing_3bet")
    assert decide(sc.table, deadline_s=10.0)["action"] not in ("raise", "all-in")
