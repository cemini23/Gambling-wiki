"""PokerSkill adapter stub for cemini_decide (HU-first, 6-max degrades gracefully).

Maps Arena `table` dicts toward the PokerSkill HUNL schema
(`pokerskill_agent.schema.validate_game_state`) and returns rule-only skill
hints when the full library is unavailable (macOS / no pip install).

Full library (CC BY-NC 4.0 — non-commercial only):
  pip install git+https://github.com/lbn187/PokerSkill.git   # Linux x86_64 + Py3.9

Wire: `retrieve_pokerskill_hints(table)` from `cemini_decide.retrieve_solver_context`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import _hand_class  # noqa: E402

from position_utils import _active_seat_numbers, hero_position_label  # noqa: E402

# PokerSkill legal action codes
_PS_FOLD, _PS_CHECK, _PS_CALL, _PS_BET = "f", "k", "c", "b"

# Minimal HU preflop defend/open hints (stub P2 layer — not GTO exact).
_HU_BTN_OPEN = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A7s",
    "A6s", "A5s", "A4s", "A3s", "A2s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "K9s", "QJs", "QTs", "Q9s",
    "JTs", "J9s", "T9s", "98s", "87s", "76s",
})
_HU_BB_DEFEND = _HU_BTN_OPEN | frozenset({
    "A9o", "K8s", "K7s", "Q8s", "J8s", "T8s", "97s", "86s", "65s", "54s",
})


def _cards_compact(cards: list[str]) -> str:
    """['As', 'Kd'] -> 'AsKd'."""
    out = []
    for c in cards or []:
        c = (c or "").strip()
        if len(c) >= 2:
            out.append(c[0].upper() + c[-1].lower())
    return "".join(out)


def _street_ps(table: dict) -> str:
    s = (table.get("street") or "Preflop").lower()
    return s if s in {"preflop", "flop", "turn", "river"} else "preflop"


def _legal_actions_ps(allowed: dict) -> list[str]:
    avail = allowed.get("availableActions") or []
    out: list[str] = []
    if "fold" in avail:
        out.append(_PS_FOLD)
    if "check" in avail:
        out.append(_PS_CHECK)
    if "call" in avail:
        out.append(_PS_CALL)
    if any(a in avail for a in ("bet", "raise", "all-in")):
        out.append(_PS_BET)
    return out or [_PS_FOLD]


def _hunl_position(table: dict) -> Optional[str]:
    """Map hero to PokerSkill BTN/BB when exactly two active seats."""
    if len(_active_seat_numbers(table)) != 2:
        return None
    pos = hero_position_label(table)
    if pos == "BTN":
        return "BTN"
    if pos in {"BB", "SB"}:
        # HU: SB acts as BTN in PokerSkill schema.
        return "BB" if pos == "BB" else "BTN"
    return None


def arena_table_to_pokerskill_state(table: dict, *, hand_id: int = 1) -> Optional[dict]:
    """Build a PokerSkill-shaped dict, or None if not HU or cards missing."""
    ps_pos = _hunl_position(table)
    if ps_pos is None:
        return None

    self_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_num), {})
    hole = list(self_seat.get("holeCards") or [])
    hole_ps = _cards_compact(hole)
    if len(hole_ps) != 4:
        return None

    street = _street_ps(table)
    board_ps = _cards_compact(list(table.get("boardCards") or []))
    allowed = table.get("allowedActions") or {}
    bb = float(table.get("bigBlindChips") or 2)
    pot = float(table.get("potChips") or 0) / max(bb, 1)
    hero_stack = float(self_seat.get("stackChips") or 200) / max(bb, 1)
    villain_stack = hero_stack
    for s in seats:
        if s.get("seatNumber") != self_num:
            villain_stack = float(s.get("stackChips") or 200) / max(bb, 1)
            break

    rr = allowed.get("raiseRange") or allowed.get("betRange") or {}
    raise_min = float(rr.get("min") or 0) / max(bb, 1) if rr else None
    raise_max = float(rr.get("max") or 0) / max(bb, 1) if rr else None

    return {
        "hand_id": hand_id,
        "street": street,
        "hero_hole_cards": hole_ps,
        "board_cards": board_ps,
        "pot": max(pot, 1.5),
        "total_pot": max(pot, 1.5),
        "hero_stack": hero_stack,
        "villain_stack": villain_stack,
        "hero_position": ps_pos,
        "legal_actions": _legal_actions_ps(allowed),
        "raise_min": raise_min,
        "raise_max": raise_max,
        "action_history": list(table.get("actionHistory") or []),
        "use_skills": True,
    }


def _board_texture(board: list[str]) -> str:
    if len(board) < 3:
        return "preflop"
    suits = [c[-1].lower() for c in board if c]
    ranks = [c[0].upper() for c in board if c]
    if suits and max(suits.count(s) for s in set(suits)) >= 2:
        return "wet"
    if len(set(ranks)) < len(ranks):
        return "paired"
    high = max(ranks, key=lambda r: "23456789TJQKA".index(r) if r in "23456789TJQKA" else 0)
    if high in {"A", "K", "Q"}:
        return "high"
    return "dry"


def _stub_hu_preflop_hint(state: dict, hc: str) -> dict[str, Any]:
    pos = state["hero_position"]
    call_chips = 0  # caller passes via table — infer from legal actions
    legal = state["legal_actions"]
    facing_bet = _PS_CALL in legal and _PS_CHECK not in legal

    if not facing_bet:
        opens = _HU_BTN_OPEN if pos == "BTN" else set()
        if pos == "BTN" and hc in opens:
            return {"scenario": "hu_btn_open", "bias": "raise", "layer": "P2-stub"}
        if pos == "BB":
            return {"scenario": "hu_bb_check", "bias": "check", "layer": "P2-stub"}
        return {"scenario": "hu_preflop", "bias": "check", "layer": "P2-stub"}

    defend = hc in _HU_BB_DEFEND if pos == "BB" else hc in _HU_BTN_OPEN
    if defend:
        return {"scenario": "hu_defend", "bias": "call", "layer": "P2-stub"}
    return {"scenario": "hu_fold", "bias": "fold", "layer": "P2-stub"}


def _stub_postflop_hint(street: str, texture: str, in_position: bool) -> dict[str, Any]:
    if street == "river":
        return {
            "scenario": "river_showdown",
            "pot_control": False,
            "bias": "value_or_bluffcatch",
            "layer": "P5-stub",
        }
    if texture == "wet":
        return {
            "scenario": "wet_pot_control",
            "pot_control": True,
            "bias": "check_call" if not in_position else "probe_small",
            "layer": "P4-stub",
        }
    return {
        "scenario": "dry_value",
        "pot_control": False,
        "bias": "bet_ip" if in_position else "check_raise",
        "layer": "P3-stub",
    }


def _try_library_prompt(state: dict) -> Optional[dict[str, str]]:
    """Return {system_prompt, user_prompt} if pokerskill_agent is installed."""
    try:
        from pokerskill_agent.schema import validate_game_state  # type: ignore
        from pokerskill_agent._core import generate_prompt  # type: ignore
    except ImportError:
        return None
    try:
        validated = validate_game_state(state)
        return generate_prompt(validated)
    except Exception:
        return None


def retrieve_pokerskill_hints(table: dict) -> dict[str, Any]:
    """Skill hints for decide() — stub rules on all tables; library on HU + Linux."""
    allowed = table.get("allowedActions") or {}
    call_chips = int(allowed.get("callChips") or 0)
    board = list(table.get("boardCards") or [])
    street = _street_ps(table)
    self_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_num), {})
    hole = list(self_seat.get("holeCards") or [])
    hc = _hand_class(hole)
    n_active = len(_active_seat_numbers(table))
    in_position = hero_position_label(table) in {"BTN", "CO"}

    out: dict[str, Any] = {
        "mode": "stub",
        "players_active": n_active,
        "hand_class": hc,
        "board_texture": _board_texture(board),
    }

    ps_state = arena_table_to_pokerskill_state(table)
    if ps_state is not None:
        out["pokerskill_state_ok"] = True
        prompts = _try_library_prompt(ps_state)
        if prompts:
            out["mode"] = "library"
            out["prompt_chars"] = len(prompts.get("user_prompt") or "")
        if street == "preflop":
            hint = _stub_hu_preflop_hint(ps_state, hc)
            if call_chips > 0 and hint.get("bias") == "raise":
                hint = {"scenario": "hu_facing_raise", "bias": "call", "layer": "P2-stub"}
            out.update(hint)
        else:
            out.update(_stub_postflop_hint(street, out["board_texture"], in_position))
    else:
        out["pokerskill_state_ok"] = False
        if street == "preflop" and call_chips == 0:
            out.update({"scenario": "multiway_open", "bias": "chart", "layer": "P2-stub"})
        elif street == "preflop":
            out.update({"scenario": "multiway_defend", "bias": "equity", "layer": "P2-stub"})
        else:
            out.update(_stub_postflop_hint(street, out["board_texture"], in_position))

    return out


def _demo() -> int:
    hu_btn = {
        "street": "Preflop",
        "selfSeatNumber": 1,
        "smallBlindChips": 1,
        "bigBlindChips": 2,
        "buttonSeatNumber": 1,
        "potChips": 3,
        "boardCards": [],
        "seats": [
            {"seatNumber": 1, "holeCards": ["As", "Kd"], "stackChips": 200,
             "currentBetChips": 1, "status": "Active"},
            {"seatNumber": 2, "holeCards": [], "stackChips": 198,
             "currentBetChips": 2, "status": "Active"},
        ],
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": 1,
            "canRaise": True,
            "raiseRange": {"min": 4, "max": 200},
        },
    }
    print("HU hints:", retrieve_pokerskill_hints(hu_btn))
    return 0


if __name__ == "__main__":
    sys.exit(_demo())
