"""Build Arena-shaped table dicts for cemini decide() regression tests.

The starter kit's `examples/testing.py` uses HU tables with seat 1 = hero
and no button — fine for smoke tests, but it hides position/HUD/multi-way
bugs that burned chips in Playground (74o MP, cold-start steals, etc.).
"""
from __future__ import annotations

from typing import Any, Optional


def _seat(
    num: int,
    *,
    agent_id: str = "villain",
    hole: list[str] | None = None,
    stack: int = 1000,
    bet: int = 0,
    committed: int = 0,
    position: str | None = None,
    training_archetype: str | None = None,
) -> dict:
    s: dict[str, Any] = {
        "seatId": f"s{num}",
        "seatNumber": num,
        "agentId": agent_id,
        "agentName": agent_id,
        "agentHandle": agent_id,
        "status": "Active",
        "stackChips": stack,
        "currentBetChips": bet,
        "totalCommittedChips": committed,
        "payoutChips": None,
        "holeCards": hole,
    }
    if position:
        s["position"] = position
    if training_archetype:
        s["trainingArchetype"] = training_archetype
    return s


def _allowed(
    *,
    can_fold: bool = True,
    can_check: bool = False,
    can_call: bool = False,
    can_bet: bool = False,
    can_raise: bool = False,
    can_all_in: bool = True,
    call_chips: int = 0,
    call_to: int = 0,
    bet_range: dict | None = None,
    raise_range: dict | None = None,
    all_in_to: int = 1000,
    max_commit: int = 1000,
) -> dict:
    available: list[str] = []
    if can_fold:
        available.append("fold")
    if can_check:
        available.append("check")
    if can_call:
        available.append("call")
    if can_bet:
        available.append("bet")
    if can_raise:
        available.append("raise")
    if can_all_in:
        available.append("all-in")
    return {
        "canFold": can_fold,
        "canCheck": can_check,
        "canCall": can_call,
        "canBet": can_bet,
        "canRaise": can_raise,
        "canAllIn": can_all_in,
        "callAmount": call_chips,
        "callChips": call_chips,
        "callToAmount": call_to,
        "maxCommit": max_commit,
        "allInToAmount": all_in_to,
        "betRange": bet_range,
        "raiseRange": raise_range,
        "availableActions": available,
        "amountSemantics": "toAmount",
    }


def six_max_table(
    *,
    name: str,
    hero_seat: int,
    button_seat: int,
    street: str,
    board: list[str],
    pot: int,
    hero_hole: list[str],
    hero_stack: int,
    allowed: dict,
    hero_bet: int = 0,
    villain_bets: dict[int, int] | None = None,
    stacks: dict[int, int] | None = None,
    competition_id: str = "regression-local",
    recent_events: list[dict] | None = None,
) -> dict:
    """6-max table with explicit button + hero seat (Playground-shaped)."""
    villain_bets = villain_bets or {}
    stacks = stacks or {}
    seats = []
    for num in range(1, 7):
        is_hero = num == hero_seat
        seats.append(
            _seat(
                num,
                agent_id="hero" if is_hero else f"bot_{num}",
                hole=hero_hole if is_hero else None,
                stack=stacks.get(num, hero_stack if is_hero else 1000),
                bet=villain_bets.get(num, hero_bet if is_hero else 0),
                training_archetype="rock" if num != hero_seat and num in (2, 5) else "maniac",
            )
        )
    return {
        "id": f"tbl_{name}",
        "tableId": f"tbl_{name}",
        "competitionId": competition_id,
        "status": "Active",
        "street": street,
        "potChips": pot,
        "boardCards": board,
        "smallBlindChips": 10,
        "bigBlindChips": 20,
        "buttonSeatNumber": button_seat,
        "selfSeatNumber": hero_seat,
        "actingSeatNumber": hero_seat,
        "seats": seats,
        "allowedActions": allowed,
        "recentEvents": recent_events or [],
    }


def mp_unopened(hero_hole: list[str], *, equity_boost: bool = False) -> dict:
    """Hero MP, 6-max, unopened pot — classic 74o leak spot."""
    # seat layout: BTN=1, SB=2, BB=3, UTG=4, MP=5, CO=6
    return six_max_table(
        name="mp_unopened",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
        hero_stack=980,
        hero_bet=0,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_check=False,
            can_call=True,
            can_raise=True,
            call_chips=20,
            call_to=20,
            raise_range={"min": 60, "max": 980},
        ),
    )


def utg_unopened(hero_hole: list[str]) -> dict:
    """Hero UTG first to act (after blinds)."""
    return six_max_table(
        name="utg_unopened",
        hero_seat=4,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_check=False,
            can_call=True,
            can_bet=True,
            call_chips=20,
            call_to=20,
            bet_range={"min": 40, "max": 980},
        ),
    )


def utg_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """Hero UTG facing a standard open from CO."""
    return six_max_table(
        name="utg_facing_raise",
        hero_seat=4,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={6: raise_to},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 980},
        ),
    )


def mp_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """Hero MP facing an UTG/early open."""
    return six_max_table(
        name="mp_facing_raise",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={4: raise_to},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 980},
        ),
    )


def co_unopened_steal_vs_rock(hero_hole: list[str]) -> dict:
    """CO unopened — J2o HUD steal leak."""
    return six_max_table(
        name="co_steal_rock",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_check=False,
            can_call=True,
            can_bet=True,
            call_chips=20,
            call_to=20,
            bet_range={"min": 40, "max": 980},
        ),
    )


def ep_oop_postflop_weak(
    hero_hole: list[str],
    board: list[str],
    *,
    hero_seat: int = 5,
    villain_bet: int = 120,
    pot: int = 240,
) -> dict:
    """MP/UTG OOP facing ~50% pot with a weak hand."""
    return six_max_table(
        name="ep_oop_weak",
        hero_seat=hero_seat,
        button_seat=1,
        street="Flop",
        board=board,
        pot=pot,
        hero_hole=hero_hole,
        hero_stack=500,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={hero_seat: 500},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 500},
        ),
    )


def overcommit_spot(hero_hole: list[str], *, call_chips: int = 200) -> dict:
    """Short stack, large call vs weak hand (board misses hero)."""
    return six_max_table(
        name="overcommit",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["As", "9d", "2c", "Kh"],
        pot=400,
        hero_hole=hero_hole,
        hero_stack=500,
        villain_bets={3: call_chips},
        stacks={5: 500},
        allowed=_allowed(
            can_call=True,
            call_chips=call_chips,
            call_to=call_chips,
        ),
    )
