"""Playground leak regression — cemini decide() on prod-shaped 6-max spots."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from cemini_decide import decide  # noqa: E402
from tests.fixtures.regression_spots import regression_spots  # noqa: E402


def _run(spot_table: dict) -> dict:
    out = decide(spot_table, deadline_s=10.0)
    legal = set(spot_table["allowedActions"]["availableActions"])
    assert out["action"] in legal, (
        f"illegal {out['action']!r} legal={sorted(legal)}"
    )
    assert "reasoning" in out and len(out["reasoning"]) <= 150
    return out


def test_all_regression_spots():
    for spot in regression_spots():
        action = _run(spot.table)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, (
                f"{spot.id}: got {action!r}, forbidden={sorted(spot.forbidden)} "
                f"— {spot.notes}"
            )
        if spot.required:
            assert action in spot.required, (
                f"{spot.id}: expected one of {sorted(spot.required)}, got {action!r}"
            )


def test_regression_count_grows_with_analyze():
    """Guardrail: we should keep adding spots after each analyze cycle."""
    n = len(regression_spots())
    assert n >= 6, f"expected ≥6 regression spots, got {n}"
