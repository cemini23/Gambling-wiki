"""Public opponent HUD facade — no exploit constants in the public repo.

Production loads `private/opponent_hud_exploit.py` (gitignored, rsync on deploy).
See private/README.example.md.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_AGENT_ROOT = Path(__file__).resolve().parent.parent
if str(_AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(_AGENT_ROOT))

_NEUTRAL_MARGINS: dict[str, float] = {
    "bet_bar_delta": 0.0,
    "call_margin_delta": 0.0,
    "fold_slack_delta": 0.0,
    "preflop_fold_margin_delta": 0.0,
    "open_steal_equity": 0.99,
}


def _exploit_impl() -> Any:
    try:
        from private import opponent_hud_exploit as mod  # type: ignore
        return mod
    except ImportError:
        return None


def exploit_margins(mode: str) -> dict[str, float]:
    mod = _exploit_impl()
    if mod is not None:
        return mod.exploit_margins(mode)
    return dict(_NEUTRAL_MARGINS)


def build_opponent_hud(table: dict) -> dict:
    mod = _exploit_impl()
    if mod is not None:
        return mod.build_opponent_hud(table)
    return {}


def invalidate_opponent_cache(
    competition_id: str | None = None,
    agent_id: str | None = None,
) -> None:
    mod = _exploit_impl()
    if mod is not None:
        mod.invalidate_opponent_cache(competition_id, agent_id)


def classify_archetype(stats: dict) -> str:
    mod = _exploit_impl()
    if mod is not None:
        return mod.classify_archetype(stats)
    return "unknown"
