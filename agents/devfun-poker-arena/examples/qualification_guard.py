"""Playground qualification + lead protection — tighten decide() when safely ahead."""
from __future__ import annotations

import os
from typing import Any

DEFAULT_CUTOFF_RANK = 20
DEFAULT_BUFFER_CHIPS = 1000  # chips above rank-20 floor before protect mode
DEFAULT_LEAD_RANK = 5
DEFAULT_LEAD_BUFFER_CHIPS = 3000  # extra cushion before lead-protect tier


def _buffer_threshold() -> int:
    raw = os.environ.get("CEMINI_QUAL_BUFFER_CHIPS")
    if raw is None or raw == "":
        return DEFAULT_BUFFER_CHIPS
    return int(raw)


def _lead_buffer_threshold() -> int:
    raw = os.environ.get("CEMINI_LEAD_BUFFER_CHIPS")
    if raw is None or raw == "":
        return DEFAULT_LEAD_BUFFER_CHIPS
    return int(raw)


def _lead_rank_threshold() -> int:
    raw = os.environ.get("CEMINI_LEAD_RANK")
    if raw is None or raw == "":
        return DEFAULT_LEAD_RANK
    return int(raw)


def fetch_qualification_status(
    client: Any,
    competition_id: str,
    *,
    cutoff_rank: int = DEFAULT_CUTOFF_RANK,
    buffer_chips: int | None = None,
    lead_rank: int | None = None,
    lead_buffer_chips: int | None = None,
) -> dict[str, Any]:
    """Return rank/chips and protection flags for decide().

    qualification_protect: rank <= cutoff_rank AND chips >= floor + buffer_chips
    lead_protect: rank <= lead_rank AND chips >= floor + lead_buffer_chips
    """
    if buffer_chips is None:
        buffer_chips = _buffer_threshold()
    if lead_rank is None:
        lead_rank = _lead_rank_threshold()
    if lead_buffer_chips is None:
        lead_buffer_chips = _lead_buffer_threshold()

    out: dict[str, Any] = {
        "qualification_protect": False,
        "lead_protect": False,
        "rank": None,
        "chips": None,
        "cutoff_chips": None,
        "buffer_chips": 0,
    }
    try:
        me = client.get("/agent/me")
    except Exception:
        return out

    row = next(
        (r for r in (me.get("leaderboard") or []) if r.get("arenaId") == competition_id),
        None,
    )
    if not row:
        return out

    rank = row.get("rank")
    chips = row.get("totalScore")
    out["rank"] = rank
    out["chips"] = chips

    try:
        lb = client.get(
            f"/competition/leaderboard?competitionId={competition_id}"
            f"&limit=1&offset={max(cutoff_rank - 1, 0)}"
        )
        cutoff_rows = lb.get("data") or []
        cutoff_chips = cutoff_rows[0].get("totalScore") if cutoff_rows else None
    except Exception:
        cutoff_chips = None

    out["cutoff_chips"] = cutoff_chips
    if rank is None or chips is None or cutoff_chips is None:
        return out

    buffer = int(chips) - int(cutoff_chips)
    out["buffer_chips"] = buffer
    if buffer >= buffer_chips and int(rank) <= cutoff_rank:
        out["qualification_protect"] = True
    if buffer >= lead_buffer_chips and int(rank) <= lead_rank:
        out["lead_protect"] = True
    return out
