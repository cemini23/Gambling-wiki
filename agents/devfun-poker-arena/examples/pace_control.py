"""Lobby join pacing — slow table intake when qualification/lead protect is on."""
from __future__ import annotations

import os

DEFAULT_JOIN_RETRY_S = 60.0
DEFAULT_IN_QUEUE_RETRY_S = 180.0
DEFAULT_QUAL_JOIN_RETRY_S = 300.0  # 5 min — still seated, fewer new tables
DEFAULT_LEAD_JOIN_RETRY_S = 900.0  # 15 min — time game > chip game when safely ahead


def _env_float(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    return float(raw)


def join_retry_seconds(
    *,
    lead_protect: bool,
    qual_protect: bool,
    in_queue_only: bool,
) -> float:
    """Seconds between join attempts when idle (no pending actions).

    Lead protect uses the longest backoff; qualification protect is moderate;
    otherwise use the default lobby cadence (or in-queue wait).
    """
    if in_queue_only:
        return _env_float("CEMINI_IN_QUEUE_RETRY_S", DEFAULT_IN_QUEUE_RETRY_S)
    if lead_protect:
        return _env_float("CEMINI_LEAD_JOIN_RETRY_S", DEFAULT_LEAD_JOIN_RETRY_S)
    if qual_protect:
        return _env_float("CEMINI_QUAL_JOIN_RETRY_S", DEFAULT_QUAL_JOIN_RETRY_S)
    return _env_float("CEMINI_JOIN_RETRY_S", DEFAULT_JOIN_RETRY_S)
