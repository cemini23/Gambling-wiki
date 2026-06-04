"""Regression spots distilled from Playground S1 analyze (2026-06-03).

Each spot encodes a *decision we should never repeat*. When analyze finds
new leaks, add a spot here (or run `examples/export_regression_spots.py`).
"""
from __future__ import annotations

from dataclasses import dataclass

from tests.helpers.cemini_tables import (
    bb_a6o_paired_river,
    bb_facing_raise,
    bb_t2s_facing_open,
    btn_qto_flush_river,
    co_72o_paired_river,
    co_t5o_river,
    co_unopened_steal_vs_rock,
    ep_oop_postflop_weak,
    mp_t6o_paired_river,
    mp_unopened,
    mp_facing_raise,
    overcommit_spot,
    sb_a8o_tptk_flop,
    sb_22_overcard_turn,
    sb_43s_facing_open,
    sb_facing_open,
    sb_jj_paired_river,
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
        RegressionSpot(
            id="prod_83o_sb_vs_open",
            source="Playground 2026-06-03 analyze #02 — 83o SB −100 preflop",
            table=sb_facing_open(["8s", "3h"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="SB trash vs open — fold, never complete/call.",
        ),
        RegressionSpot(
            id="prod_jj_sb_paired_river",
            source="Playground 2026-06-03 analyze #01 — JJ SB −101 on K662T2",
            table=sb_jj_paired_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="SB underpair on paired runout vs river bet — fold.",
        ),
        RegressionSpot(
            id="prod_kqo_mp_oop_turn",
            source="Playground analyze #07 — KQo MP −100 OOP",
            table=ep_oop_postflop_weak(
                ["Kc", "Qh"],
                ["9c", "Ks", "6d", "8s"],
                hero_seat=5,
                villain_bet=160,
                pot=320,
            ),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="Weak top pair OOP vs big turn bet — fold.",
        ),
        RegressionSpot(
            id="prod_a8o_sb_tptk_flop",
            source="Playground 2026-06-03 analyze #03 — A8o SB −100",
            table=sb_a8o_tptk_flop(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="SB weak ace top pair OOP vs ~33% pot — fold.",
        ),
        RegressionSpot(
            id="prod_22_sb_overcard_turn",
            source="Playground analyze #09 — 22 SB −100",
            table=sb_22_overcard_turn(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="SB small pair OOP under overcards — fold.",
        ),
        RegressionSpot(
            id="prod_qto_btn_flush_river",
            source="Playground analyze #01 — QTo BTN −100 flush board",
            table=btn_qto_flush_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="BTN second pair on three-diamond runout vs big bet — fold.",
        ),
        RegressionSpot(
            id="prod_a6o_bb_paired_river",
            source="Playground analyze #07 — A6o BB −100 paired board",
            table=bb_a6o_paired_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="OOP weak ace on paired runout — fold.",
        ),
        RegressionSpot(
            id="prod_t6o_mp_paired_river",
            source="Playground analyze round 3 #01 — T6o MP −290",
            table=mp_t6o_paired_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="EP weak top pair on paired runout — fold.",
        ),
        RegressionSpot(
            id="prod_43s_sb_vs_open",
            source="Playground analyze round 3 #08 — 43s SB −100 preflop",
            table=sb_43s_facing_open(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="SB low suited trash vs open — fold.",
        ),
        RegressionSpot(
            id="prod_q6o_bb_vs_open",
            source="Playground analyze round 4 #02 — Q6o BB −100 preflop",
            table=bb_facing_raise(["6d", "Qc"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="BB chart-trash vs open — fold (IP pricing leak).",
        ),
        RegressionSpot(
            id="prod_t5o_co_river",
            source="Playground analyze round 4 #12 — T5o CO −100 river",
            table=co_t5o_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            notes="CO weak top pair OOP vs river bet — fold.",
        ),
        RegressionSpot(
            id="prod_77_mp_vs_raise",
            source="Playground analyze round 5 #02 — 77 MP −100 preflop",
            table=mp_facing_raise(["7h", "7s"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="Protect mode: no medium-pair calls vs EP opens.",
        ),
        RegressionSpot(
            id="prod_kqo_bb_vs_open_protect",
            source="Playground analyze round 5 #10 — KQo BB −100 preflop",
            table=bb_facing_raise(["Qs", "Kh"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="BB broadway fold under qualification protect.",
        ),
        RegressionSpot(
            id="prod_72o_co_paired_river",
            source="HL R6 analyze #01 — 72o CO −100 paired runout",
            table=co_72o_paired_river(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="CO IP low trash on paired board — never pay.",
        ),
        RegressionSpot(
            id="prod_t2s_bb_vs_open",
            source="HL R6 analyze #05 — T2s BB −100 preflop",
            table=bb_t2s_facing_open(),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="BB low suited trash vs open — fold.",
        ),
    ]
