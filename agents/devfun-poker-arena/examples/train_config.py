"""Training-time tunables for self-play sweeps (read via env after apply_profile)."""
from __future__ import annotations

import os
from typing import Any, Optional

# HUD exploit margin env suffixes (CEMINI_{ROCK|MANIAC}_{SUFFIX})
_MARGIN_SUFFIX = {
    "bet_bar_delta": "BET_BAR_DELTA",
    "call_margin_delta": "CALL_MARGIN_DELTA",
    "fold_slack_delta": "FOLD_SLACK_DELTA",
    "preflop_fold_margin_delta": "PREFLOP_FOLD_DELTA",
    "open_steal_equity": "STEAL_EQ",
}

# Decision thresholds (CEMINI_{NAME})
_THRESHOLD_KEYS = {
    "trash_fold_eq": "TRASH_FOLD_EQ",
    "paired_ip_fold_eq": "PAIRED_IP_FOLD_EQ",
    "paired_vuln_fold_eq": "PAIRED_VULN_FOLD_EQ",
    "weak_preflop_margin": "WEAK_PREFLOP_MARGIN",
    "ip_trash_margin": "IP_TRASH_MARGIN",
    "rock_oop_fold_eq": "ROCK_OOP_FOLD_EQ",
    "garbage_postflop_margin": "GARBAGE_POSTFLOP_MARGIN",
}


def active_profile() -> str:
    return os.environ.get("CEMINI_PROFILE", "default")


def env_float(key: str, default: float) -> float:
    raw = os.environ.get(key)
    if raw is None or raw == "":
        return default
    return float(raw)


def threshold(name: str, default: float) -> float:
    suffix = _THRESHOLD_KEYS.get(name)
    if not suffix:
        raise KeyError(name)
    return env_float(f"CEMINI_{suffix}", default)


def apply_margin_overrides(mode: str, margins: dict[str, float]) -> dict[str, float]:
    out = dict(margins)
    prefix = f"CEMINI_{mode.upper()}_"
    for key, suffix in _MARGIN_SUFFIX.items():
        raw = os.environ.get(prefix + suffix)
        if raw is not None and raw != "":
            out[key] = float(raw)
    return out


def profile_snapshot() -> dict[str, Any]:
    """Serializable params for sweep reports."""
    snap: dict[str, Any] = {"profile": active_profile()}
    for _name, suffix in _THRESHOLD_KEYS.items():
        ek = f"CEMINI_{suffix}"
        if os.environ.get(ek) not in (None, ""):
            snap[ek] = os.environ[ek]
    for mode in ("rock", "maniac"):
        for _key, suffix in _MARGIN_SUFFIX.items():
            ek = f"CEMINI_{mode.upper()}_{suffix}"
            if os.environ.get(ek) not in (None, ""):
                snap[ek] = os.environ[ek]
    return snap


def clear_profile_env() -> None:
    keys = ["CEMINI_PROFILE", "TRAINING_SEAT_ARCHETYPES", *(
        f"CEMINI_{s}" for s in _THRESHOLD_KEYS.values()
    ), *(
        f"CEMINI_{m}_{s}"
        for m in ("ROCK", "MANIAC")
        for s in _MARGIN_SUFFIX.values()
    )]
    for k in keys:
        os.environ.pop(k, None)


def reset_hud_runtime() -> None:
    """Clear cached HUD state between sweep profiles."""
    try:
        import private.opponent_hud_exploit as hud  # type: ignore
    except ImportError:
        return
    hud._CACHE.clear()
    hud._DECISION_COUNT = 0
    hud._STEAL_OUTCOMES.clear()
