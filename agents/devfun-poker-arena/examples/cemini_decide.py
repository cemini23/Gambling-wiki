"""Cemini / gambling-wiki dev.fun Poker Arena agent.

Layers on arena-pokerkit L1:
  1. Auto Research — preflop chart (research_static_chart)
  2. Skill binding stub — street/hand-class labels in reasoning (PokerSkill pattern)
  3. Equity + pot-odds postflop (treys MC from agent.py)
  4. Hard deadline fallbacks (check > fold)

Run:
  uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 20
  uv run examples/agent.py --agent examples/cemini_decide.py --competition-id <id>
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import (  # noqa: E402
    _build,
    _build_reasoning,
    _hand_class,
    estimate_equity,
)
from position_utils import hero_is_in_position  # noqa: E402
from opponent_hud import build_opponent_hud, exploit_margins  # noqa: E402
from pokerskill_adapter import retrieve_pokerskill_hints  # noqa: E402

try:
    from train_config import threshold as _train_threshold  # noqa: E402
except ImportError:
    def _train_threshold(_name: str, default: float) -> float:  # noqa: E402
        return default
from research_static_chart import research_static_chart  # noqa: E402

# Preflop trash facing a raise — fold unless equity clearly covers price.
_WEAK_FACING_RAISE = frozenset({
    "A2o", "A3o", "A4o", "A5o", "A6o", "A7o", "A8o", "A9o",
    "K9o", "K8o", "K7o", "K6o", "K5o", "K4o", "K3o", "K2o",
    "Q9o", "Q8o", "Q7o", "Q6o", "Q5o", "Q4o", "Q3o", "Q2o",
    "J9o", "J8o", "J7o", "J6o", "T9o", "T8o", "T7o", "98o", "97o", "87o",
    "KJo", "QJo", "JTo", "KTo", "QTo",
    "84o", "83o", "82o", "74o", "73o", "72o", "64o", "63o", "62o",
    "54o", "53o", "52o", "43o", "42o", "32o",
})

_RANKS = "23456789TJQKA"


def retrieve_solver_context(table: dict) -> dict:
    """Preflop chart + PokerSkill hints + skill-binding labels for decide()."""
    chart = research_static_chart(table)
    ps = retrieve_pokerskill_hints(table)
    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop").lower()
    hc = _hand_class(hole) or chart.get("hand_class") or ""
    scenario = ps.get("scenario") or _scenario_label(street, board, hc)

    ctx: dict[str, Any] = {
        "preflop_chart": {
            "suggested_action": chart.get("preflop_action"),
            "hand_class": hc or chart.get("hand_class"),
            "position": chart.get("position"),
        },
        "pokerskill": ps,
        "skill_binding": {
            "street": street,
            "hand_class": hc or "unknown",
            "board_len": len(board),
            "scenario": scenario,
        },
    }
    if chart:
        ctx.update(chart)
    oh = build_opponent_hud(table)
    if oh:
        ctx["opponent_hud"] = oh
    return ctx


def _scenario_label(street: str, board: list[str], hc: str) -> str:
    if street == "preflop":
        return "open_defend" if hc else "preflop_unknown"
    if len(board) >= 3:
        suits = [c[-1].lower() for c in board if c]
        if suits and max(suits.count(s) for s in set(suits)) >= 2:
            return "wet_board_pot_control"
    return "dry_board_value"


def decide(
    table: dict,
    deadline_s: float = 10.0,
    research_context: Optional[dict] = None,
) -> dict:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    if research_context is None:
        research_context = retrieve_solver_context(table)
    ctx = research_context

    if deadline_s < 2.0:
        if allowed.get("canCheck"):
            return _build("check", None, table, allowed, eq=0.5, po=0.0,
                          msg="clock pressure — free check")
        return _build("fold", None, table, allowed, eq=0.0, po=1.0,
                      msg="clock pressure — fold")

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop")

    pot = int(table.get("potChips") or 0)
    call_chips = int(allowed.get("callChips") or 0)
    pot_odds = call_chips / max(pot + call_chips, 1) if call_chips else 0.0
    sims = 500 if deadline_s > 5 else (350 if deadline_s > 3 else 200)
    equity = estimate_equity(hole, board, sims=sims, deadline_s=deadline_s)

    chart = ctx.get("preflop_chart") or {}
    suggested = chart.get("suggested_action") or ctx.get("preflop_action")
    ps = ctx.get("pokerskill") or {}
    binding = (ctx.get("skill_binding") or {}).get("scenario", "unknown")
    in_position = hero_is_in_position(table)
    pot_control = bool(ps.get("pot_control"))
    ps_bias = ps.get("bias")
    ps_library = ps.get("mode") == "library"
    ps_hand_eval = ps.get("hand_eval")
    position = chart.get("position") or ""
    hud = ctx.get("opponent_hud") or {}
    hud_mode = hud.get("mode") or "unknown"
    margins = hud.get("margins") or exploit_margins(hud_mode)
    cold_start = bool(hud.get("coldStart"))
    hc = chart.get("hand_class") or ""

    action_name: str
    amount: Optional[int] = None

    # Cold start: chart-first — no marginal postflop calls until HUD reads land.
    if (cold_start and street != "Preflop" and call_chips > 0 and "fold" in available
            and hc not in {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs"}
            and equity < pot_odds + 0.08):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: cold-start — fold marginal spot")

    # Live leak: never pay with bottom offsuit trash postflop (64o-type lines).
    trash_eq = _train_threshold("trash_fold_eq", 0.30)
    garbage_margin = _train_threshold("garbage_postflop_margin", 0.04)
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and _is_garbage_offsuit(hc)
            and equity < max(pot_odds + garbage_margin, trash_eq)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: trash hand vs bet — fold")

    # PokerSkill library / stub: explicit fold when facing a bet (weak hands only).
    if (ps_bias == "fold" and call_chips > 0 and "fold" in available
            and (_should_fold_weak_preflop(chart.get("hand_class") or "", equity, pot_odds)
                 or equity < pot_odds + 0.04)):
        action_name, amount = "fold", None
    # Chart drives opens — library bias can nudge HU opens/checks.
    elif street == "Preflop" and call_chips == 0:
        eff = _effective_preflop_open(suggested, ps_library, ps_bias, equity)
        action_name, amount = _preflop_open(
            eff, allowed, available, pot, equity,
            hand_class=hc,
            position=position, ps_bias=ps_bias, ps_library=ps_library,
            hud_mode=hud_mode, margins=margins, cold_start=cold_start)
    elif street == "Preflop" and call_chips > 0:
        action_name, amount = _preflop_vs_bet(
            chart, allowed, available, equity, pot_odds, call_chips, pot,
            in_position=in_position, ps_bias=ps_bias, ps_library=ps_library,
            hud_mode=hud_mode, margins=margins)
    elif call_chips == 0:
        action_name, amount = _postflop_free(
            equity, allowed, available, pot, pot_control=pot_control,
            ps_bias=ps_bias, ps_library=ps_library,
            hand_eval=ps_hand_eval,
            hand_class=hc, hud_mode=hud_mode, margins=margins)
    else:
        action_name, amount = _postflop_facing_bet(
            equity, pot_odds, allowed, available, call_chips, pot,
            in_position=in_position, pot_control=pot_control,
            hand_class=hc,
            hole=hole, board=board, ps_bias=ps_bias, ps_library=ps_library,
            hand_eval=ps_hand_eval, hud_mode=hud_mode, margins=margins)

    if action_name in ("fold", "check", "call"):
        amount = None

    msg = _message(action_name, equity, pot_odds, binding, suggested, hud_mode=hud_mode)
    out = _build(action_name, amount, table, allowed, eq=equity, po=pot_odds, msg=msg)
    out["reasoning"] = _skill_reasoning(
        out.get("reasoning", ""), binding, suggested, chart, ps, hud_mode=hud_mode)
    return out


def _effective_preflop_open(
    suggested: Optional[str],
    ps_library: bool,
    ps_bias: Optional[str],
    equity: float,
) -> str:
    """Merge chart open with PokerSkill library nudges (HU priority)."""
    base = suggested or "check"
    if not ps_library or not ps_bias:
        return base
    if ps_bias == "check":
        return "check"
    if ps_bias == "raise" and equity > 0.45:
        return "raise"
    if ps_bias == "fold":
        return "fold"
    return base


def _is_garbage_offsuit(hc: str) -> bool:
    """Bottom offsuit trash — no postflop calls without a strong price edge."""
    if not hc:
        return False
    return hc in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hc)


def _blocks_open_steal(hand_class: str, position: str) -> bool:
    """Chart-fold trash — never open-steal (J2o CO leak vs rock HUD)."""
    if not hand_class:
        return True
    if hand_class in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hand_class):
        return True
    if _is_sb_complete_trash(hand_class):
        return True
    # CO/BTN: block wheel + low broadway offsuit steals (J4o, T3o, …).
    if position in ("CO", "BTN") and len(hand_class) == 3 and hand_class[2] == "o":
        if hand_class[0] == hand_class[1]:
            return False
        hi, lo = _RANKS.index(hand_class[0]), _RANKS.index(hand_class[1])
        if hi <= 9 and lo <= 4:
            return True
    return False


def _preflop_open(suggested: str, allowed: dict, available: list,
                  pot: int, equity: float,
                  hand_class: str = "", position: str = "",
                  ps_bias: Optional[str] = None,
                  ps_library: bool = False,
                  hud_mode: str = "unknown",
                  margins: Optional[dict] = None,
                  cold_start: bool = False) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    if (position == "SB" and _weak_ace_offsuit(hand_class)
            and suggested == "raise" and "check" in available):
        return "check", None
    if (position == "SB" and _is_sb_complete_trash(hand_class)
            and "check" in available):
        return "check", None
    if ps_library and ps_bias == "check" and "check" in available:
        return "check", None
    # vs rock: steal when chart is passive but equity supports an open.
    steal_eq = float(margins.get("open_steal_equity", 0.99))
    if (not cold_start and hud_mode == "rock" and suggested in ("check", "fold")
            and equity >= steal_eq and allowed.get("canBet") and "bet" in available
            and not _is_sb_complete_trash(hand_class)
            and not _blocks_open_steal(hand_class, position)):
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.5), max_bet))
        return "bet", target
    if suggested == "raise" and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.55), max_bet))
        return "bet", target
    if suggested == "fold" and "fold" in available:
        return "fold", None
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _preflop_vs_bet(chart: dict, allowed: dict, available: list,
                    equity: float, pot_odds: float, call_chips: int,
                    pot: int, *, in_position: bool,
                    ps_bias: Optional[str] = None,
                    ps_library: bool = False,
                    hud_mode: str = "unknown",
                    margins: Optional[dict] = None) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    hc = chart.get("hand_class") or ""
    position = chart.get("position") or ""
    suggested = chart.get("suggested_action") or "fold"

    if ps_library and ps_bias == "fold" and "fold" in available:
        if _should_fold_weak_preflop(hc, equity, pot_odds) or equity < pot_odds + 0.04:
            return "fold", None
    if ps_library and ps_bias == "call" and equity >= pot_odds and "call" in available:
        return "call", None

    if _should_fold_weak_preflop(hc, equity, pot_odds) and "fold" in available:
        return "fold", None
    # SB OOP: don't defend chart-fold trash without a clear price edge.
    if (position == "SB" and suggested == "fold"
            and equity < pot_odds + 0.08 and "fold" in available):
        return "fold", None
    if (_is_low_trash_offsuit(hc) and not in_position
            and equity < pot_odds + 0.06 and "fold" in available):
        return "fold", None
    # BTN/IP: 64o–98o trash — fold vs opens without a clear edge (S28 64o leak).
    if (in_position and _is_low_trash_offsuit(hc)
            and equity < pot_odds + _train_threshold("ip_trash_margin", 0.06)
            and "fold" in available):
        return "fold", None
    # BTN/IP: weak offsuit aces fold vs raises without a solid edge.
    if (in_position and _weak_ace_offsuit(hc)
            and equity < pot_odds + 0.08 and "fold" in available):
        return "fold", None
    premium = hc in {"AA", "KK", "QQ", "JJ", "AKs", "AKo"}
    strong_3bet = premium or (in_position and hc in {"AQs", "AQo", "TT"})
    if strong_3bet and equity > 0.52 and allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2.5), max_r))
        return "raise", target
    call_margin = 0.03 if in_position else 0.06
    fold_margin = 0.08 if in_position else 0.05
    call_margin += float(margins.get("call_margin_delta", 0))
    fold_margin += float(margins.get("preflop_fold_margin_delta", 0))
    # vs rock: their raise is polarized — fold more marginal opens.
    if hud_mode == "rock" and not premium and not strong_3bet:
        fold_margin += 0.03
    if equity >= pot_odds + call_margin and "call" in available:
        return "call", None
    if equity < pot_odds - fold_margin and "fold" in available:
        return "fold", None
    return ("call" if "call" in available else "fold"), None


def _should_fold_weak_preflop(hc: str, equity: float, pot_odds: float) -> bool:
    """Fold dominated trash preflop unless MC equity clears price with margin."""
    if not hc:
        return False
    if hc not in _WEAK_FACING_RAISE:
        return False
    # Weak aces / broadways need a clear edge, not a marginal call.
    return equity < pot_odds + _train_threshold("weak_preflop_margin", 0.07)


def _weak_ace_offsuit(hc: str) -> bool:
    return len(hc) == 3 and hc[0] == "A" and hc[2] == "o"


def _is_low_trash_offsuit(hc: str) -> bool:
    """Both ranks below T, offsuit, unpaired — live SB leak hands."""
    if len(hc) != 3 or hc[2] != "o" or hc[0] == hc[1]:
        return False
    i1, i2 = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    return i1 < 8 and i2 < 8


def _is_sb_complete_trash(hc: str) -> bool:
    """Hands SB should never open — complete or fold only."""
    if not hc:
        return False
    if hc in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hc):
        return True
    if _weak_ace_offsuit(hc):
        return True
    return hc in {"K9o", "Q9o", "Q8o", "Q7o", "Q6o", "Q5o", "Q4o", "Q3o", "Q2o",
                  "J9o", "T8o", "97o", "86o", "75o", "J8o", "T7o", "96o", "85o", "74o"}


def _board_paired_hero_missed(hole: list[str], board: list[str]) -> bool:
    """True when board is paired/trips and hero did not connect."""
    if len(board) < 3 or len(hole) != 2:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    if not any(v >= 2 for v in bc.values()):
        return False
    hranks = {c[0].upper() for c in hole}
    return not any(bc.get(r, 0) >= 2 for r in hranks)


def _board_is_paired(board: list[str]) -> bool:
    if len(board) < 3:
        return False
    branks = [c[0].upper() for c in board]
    return max(Counter(branks).values()) >= 2


def _weak_broadway_offsuit(hc: str) -> bool:
    return hc in {"AJo", "ATo", "A9o", "KJo", "KTo", "QJo", "QTo", "JTo"}


def _hero_ace_high_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Ace-high only on paired runouts (AJo on 55x — S28 -46 leak)."""
    if not _board_is_paired(board) or len(hole) != 2:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return False
    if "A" not in hranks:
        return False
    branks = [c[0].upper() for c in board]
    return not any(r in branks for r in hranks)


def _hero_vulnerable_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Underpair / single non-boat pair on paired boards (fold vs big bets)."""
    if not _board_is_paired(board) or len(hole) != 2:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    pair_rank = next(r for r, c in bc.items() if c >= 2)
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return _RANKS.index(hranks[0]) < _RANKS.index(pair_rank)
    if any(r in branks and branks.count(r) >= 2 for r in hranks):
        return False
    return any(r in branks and branks.count(r) == 1 for r in hranks)


def _hero_overcards_only(hole: list[str], board: list[str]) -> bool:
    """Paired board, hero missed — only unpaired overcards (Kh4c on TTT)."""
    if not _board_paired_hero_missed(hole, board) or len(hole) != 2:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return False
    branks = [c[0].upper() for c in board]
    return not any(r in branks for r in hranks)


def _postflop_free(equity: float, allowed: dict, available: list,
                   pot: int, *, pot_control: bool = False,
                   ps_bias: Optional[str] = None,
                   ps_library: bool = False,
                   hand_eval: Optional[str] = None,
                   hand_class: str = "",
                   hud_mode: str = "unknown",
                   margins: Optional[dict] = None) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    # PokerSkill: nut-high + draw → pot control, don't lead.
    if hand_eval == "nut_high_draw" and "check" in available:
        return "check", None
    if ps_library and ps_bias == "check" and "check" in available:
        return "check", None
    bet_bar = 0.78 if pot_control else 0.72
    bet_bar += float(margins.get("bet_bar_delta", 0))
    if ps_bias == "probe_small" and allowed.get("canBet") and "bet" in available:
        bet_bar = 0.58 + float(margins.get("bet_bar_delta", 0))
    if ps_library and ps_bias == "raise" and equity > 0.62:
        bet_bar = 0.55 + float(margins.get("bet_bar_delta", 0))
    if equity > bet_bar and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.33), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.66), max_bet))
        return "bet", target
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _postflop_facing_bet(equity: float, pot_odds: float, allowed: dict,
                         available: list, call_chips: int,
                         pot: int, *, in_position: bool,
                         pot_control: bool = False,
                         hand_class: str = "",
                         hole: Optional[list[str]] = None,
                         board: Optional[list[str]] = None,
                         ps_bias: Optional[str] = None,
                         ps_library: bool = False,
                         hand_eval: Optional[str] = None,
                         hud_mode: str = "unknown",
                         margins: Optional[dict] = None) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    hole = hole or []
    board = board or []

    if ps_library and ps_bias == "fold" and "fold" in available:
        if (_should_fold_weak_preflop(hand_class, equity, pot_odds)
                or equity < pot_odds + 0.04):
            return "fold", None

    # J2o-type trash: fold vs bets on paired boards (662A2 runouts).
    if (hand_class in _WEAK_FACING_RAISE and _board_is_paired(board)
            and call_chips > 0 and equity < 0.48 and "fold" in available):
        return "fold", None

    # PokerSkill nut-high + draw: check-call line, avoid spewy raises.
    if hand_eval == "nut_high_draw":
        raise_bar = 0.88
        call_margin = -0.02 if in_position else 0.01
        if equity > raise_bar and allowed.get("canRaise") and "raise" in available:
            rr = allowed.get("raiseRange") or {}
            min_r = int(rr.get("min") or call_chips * 2)
            max_r = int(rr.get("max") or min_r)
            target = max(min_r, min(int(pot * 0.65 + call_chips * 2), max_r))
            return "raise", target
        if equity >= pot_odds + call_margin and "call" in available:
            return "call", None
        if equity < pot_odds - 0.03 and "fold" in available:
            return "fold", None
        if "check" in available:
            return "check", None

    # Live leak: air on paired boards (Kh4c on TTT-type runouts).
    if (_hero_overcards_only(hole, board) and not in_position
            and equity < 0.48 and "fold" in available):
        return "fold", None
    if (_board_paired_hero_missed(hole, board) and not in_position
            and equity < 0.44 and "fold" in available):
        return "fold", None
    if (_board_paired_hero_missed(hole, board) and pot_control
            and equity < 0.50 and "fold" in available):
        return "fold", None

    # S28 leak: AJo IP on paired boards — don't pay large bets with ace-high / weak pair.
    big_bet = call_chips >= max(int(pot * 0.42), 1)
    if (in_position and len(board) >= 3 and big_bet and "fold" in available):
        paired_ip = _train_threshold("paired_ip_fold_eq", 0.42)
        paired_vuln = _train_threshold("paired_vuln_fold_eq", 0.44)
        if (_hero_ace_high_on_paired_board(hole, board) and equity < paired_ip):
            return "fold", None
        if ((_hero_vulnerable_on_paired_board(hole, board)
             or _weak_broadway_offsuit(hand_class))
                and equity < paired_vuln):
            return "fold", None

    # Live leak: weak ace-high folds cheaply on later streets (Ad3c-type spots).
    if _weak_ace_offsuit(hand_class) and equity < 0.38 and "fold" in available:
        return "fold", None
    if _weak_ace_offsuit(hand_class) and not in_position and equity < 0.45:
        if equity < pot_odds and "fold" in available:
            return "fold", None
    fold_slack = 0.06 if in_position else 0.04
    call_margin = 0.04 if in_position else 0.07
    fold_slack += float(margins.get("fold_slack_delta", 0))
    call_margin += float(margins.get("call_margin_delta", 0))
    if pot_control:
        call_margin += 0.03
        fold_slack -= 0.01
    # vs rock OOP: respect aggression — don't over-fold IP medium hands.
    rock_oop_eq = _train_threshold("rock_oop_fold_eq", 0.40)
    if hud_mode == "rock" and not in_position and equity < rock_oop_eq and "fold" in available:
        fold_slack += 0.02
    if equity < pot_odds - fold_slack and "fold" in available:
        return "fold", None
    raise_bar = 0.82 if in_position else 0.86
    if equity > raise_bar and allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2), max_r))
        return "raise", target
    if equity >= pot_odds + call_margin and "call" in available:
        return "call", None
    if "check" in available:
        return "check", None
    return ("fold" if "fold" in available else "call"), None


def _message(action: str, equity: float, pot_odds: float,
             binding: str, suggested: Optional[str],
             hud_mode: str = "unknown") -> str:
    eq = int(round(equity * 100))
    hud = f" vs {hud_mode}" if hud_mode not in ("unknown", "") else ""
    if action == "fold":
        return f"{binding}{hud}: equity {eq}% short of price, folding"
    if action == "check":
        return f"{binding}: free card, equity {eq}%"
    if action == "call":
        return f"{binding}: calling — equity covers pot odds"
    if suggested and action in ("bet", "raise"):
        return f"chart says {suggested}; executing {action} for value"
    return f"{binding}: {action} with {eq}% equity"


def _skill_reasoning(base: str, binding: str, suggested: Optional[str],
                     chart: dict, ps: Optional[dict] = None,
                     hud_mode: str = "unknown") -> str:
    """Append skill tag within 150-char YAML cap."""
    pos = chart.get("position") or "?"
    layer = (ps or {}).get("layer", "stub")
    hud = hud_mode if hud_mode not in ("unknown", "") else "-"
    tag = f'sk: "{binding}@{pos}|{layer}|{hud}"'
    if suggested:
        tag = f'sk: "{binding}|{suggested}@{pos}|{hud}"'
    if len(base) + len(tag) + 2 <= 150:
        return base[:-1] + f", {tag}}}" if base.endswith("}") else f"{{{tag}}}"
    return base[:150]
