"""Regression spots distilled from Playground S1 analyze (2026-06-03).

Each spot encodes a *decision we should never repeat*. When analyze finds
new leaks, add a spot here (or run `examples/export_regression_spots.py`).
"""
from __future__ import annotations

from dataclasses import dataclass

from tests.helpers.cemini_tables import (
    co_unopened_steal_vs_rock,
    ep_oop_postflop_weak,
    mp_unopened,
    mp_facing_raise,
    overcommit_spot,
    utg_facing_raise,
    utg_unopened,
)


@dataclass(frozen=True)
class RegressionSpot:
    id: str
    source: str
    table: dict
    forbidden: frozenset[str] = frozenset()
    required: frozenset[str] = frozenset()
    notes: str = ""


def regression_spots() -> list[RegressionSpot]:
    return [
        RegressionSpot(
            id="prod_74o_mp_open",
            source="Playground S1 analyze — avg −916 with 74o MP",
            table=mp_unopened(["7c", "4d"]),
            forbidden=frozenset({"bet", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="EP chart-only; no HUD steal from MP.",
        ),
        RegressionSpot(
            id="prod_kts_utg_open",
            source="Playground S1 — KTs UTG −393",
            table=utg_unopened(["Kh", "Ts"]),
            forbidden=frozenset({"bet", "raise", "all-in"}),
            notes="UTG: chart fold — no open.",
        ),
        RegressionSpot(
            id="prod_j2o_co_steal_rock",
            source="HUD open-steal vs rock — J2o CO",
            table=co_unopened_steal_vs_rock(["Jc", "2d"]),
            forbidden=frozenset({"bet", "raise", "all-in"}),
            notes="Blocked offsuit junk steals even with high equity estimate.",
        ),
        RegressionSpot(
            id="prod_74o_mp_vs_raise",
            source="Playground — defend too wide MP",
            table=mp_facing_raise(["7c", "4d"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="Trash vs open — fold.",
        ),
        RegressionSpot(
            id="prod_74o_overcommit_turn",
            source="Stack commitment — 74o facing big turn bet",
            table=overcommit_spot(["7c", "4d"], call_chips=200),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="~40% stack call with trash — fold.",
        ),
        RegressionSpot(
            id="prod_mp_oop_weak_flop",
            source="EP OOP float/call leak",
            table=ep_oop_postflop_weak(["7c", "4d"], ["As", "9d", "2c"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="Weak hand OOP vs half-pot — prefer fold.",
        ),
        RegressionSpot(
            id="prod_aa_mp_value",
            source="Sanity — must not fold premiums",
            table=mp_unopened(["Ah", "Ad"]),
            forbidden=frozenset({"fold", "check"}),
            notes="AA MP must raise or call, never pass.",
        ),
    ]
