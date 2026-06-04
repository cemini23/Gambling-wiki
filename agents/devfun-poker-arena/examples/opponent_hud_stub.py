"""Public HUD stub for CI and local dev when private/ is absent.

Copy to private/opponent_hud_exploit.py for offline tests without prod exploits:
  cp examples/opponent_hud_stub.py private/opponent_hud_exploit.py
"""
from __future__ import annotations

import os
from typing import Optional

_MIN_SAMPLE = 12
_COLD_START_MIN_VILLAIN_SAMPLE = int(os.environ.get("OPPONENT_HUD_COLD_START_SAMPLE", "12"))
_COLD_START_HERO_HANDS = int(os.environ.get("OPPONENT_HUD_COLD_START_HERO_HANDS", "20"))
_COLD_START_MIN_CONF = float(os.environ.get("OPPONENT_HUD_COLD_START_CONF", "0.35"))
_COLD_START_BANKROLL_PCT = float(os.environ.get("OPPONENT_HUD_COLD_START_BANKROLL", "0.85"))
_PLAYGROUND_START_CHIPS = int(os.environ.get("ARENA_PLAYGROUND_START_CHIPS", "1000"))


def classify_archetype(stats: dict) -> str:
    sample = int(stats.get("sampleSize") or 0)
    if sample < _MIN_SAMPLE:
        return "unknown"

    style = stats.get("playingStyle") or {}
    archetype = (style.get("archetype") or "").lower()
    if archetype in ("rock", "nit"):
        return "rock"
    if archetype in ("maniac", "lag", "loose-aggressive", "loose_aggressive"):
        return "maniac"

    vpip = stats.get("vpip")
    pfr = stats.get("pfr") or 0.0
    if vpip is None:
        return "unknown"
    if vpip < 0.15:
        return "rock"
    if vpip > 0.40 or (vpip > 0.30 and pfr > 0.25):
        return "maniac"
    if vpip < 0.22:
        return "tight"
    return "unknown"


def exploit_margins(mode: str) -> dict[str, float]:
    if mode == "rock":
        return {
            "bet_bar_delta": -0.10,
            "call_margin_delta": 0.02,
            "fold_slack_delta": 0.05,
            "preflop_fold_margin_delta": 0.04,
            "open_steal_equity": 0.34,
        }
    if mode == "maniac":
        return {
            "bet_bar_delta": 0.06,
            "call_margin_delta": -0.06,
            "fold_slack_delta": -0.04,
            "preflop_fold_margin_delta": -0.04,
            "open_steal_equity": 0.99,
        }
    return {
        "bet_bar_delta": 0.0,
        "call_margin_delta": 0.0,
        "fold_slack_delta": 0.0,
        "preflop_fold_margin_delta": 0.0,
        "open_steal_equity": 0.99,
    }


def _cold_start_margins() -> dict[str, float]:
    return {
        "bet_bar_delta": 0.10,
        "call_margin_delta": 0.05,
        "fold_slack_delta": 0.07,
        "preflop_fold_margin_delta": 0.06,
        "open_steal_equity": 0.99,
    }


def _hero_stack_ratio(table: dict) -> Optional[float]:
    self_num = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") != self_num:
            continue
        stack = seat.get("stackChips")
        if stack is None:
            return None
        start = _PLAYGROUND_START_CHIPS
        if start <= 0:
            return None
        return max(0.0, float(stack) / float(start))
    return None


def _cold_start_reason(
    table: dict,
    competition_id: str,
    conf: float,
    profiles: list[dict],
) -> str:
    del competition_id  # stub has no arena client
    max_sample = max((int(p.get("sampleSize") or 0) for p in profiles), default=0)
    if max_sample < _COLD_START_MIN_VILLAIN_SAMPLE:
        return "villain_sample"
    if conf < _COLD_START_MIN_CONF:
        return "low_conf"
    ratio = _hero_stack_ratio(table)
    if ratio is not None and ratio < _COLD_START_BANKROLL_PCT:
        return "bankroll"
    return "hero_sample"


def _apply_cold_start_guard(
    *,
    table: dict,
    competition_id: str,
    conf: float,
    profiles: list[dict],
    mode: str,
    margins: dict[str, float],
) -> tuple[str, dict[str, float], bool, str]:
    reason = _cold_start_reason(table, competition_id, conf, profiles)
    if not reason:
        return mode, margins, False, ""
    return "unknown", _cold_start_margins(), True, reason


def build_opponent_hud(table: dict) -> dict:
    del table
    return {}


def invalidate_opponent_cache(
    competition_id: str | None = None,
    agent_id: str | None = None,
) -> None:
    del competition_id, agent_id
