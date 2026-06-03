"""Playground qualification status — tighten decide() when safely in top 20."""
from __future__ import annotations

import os
from typing import Any

DEFAULT_CUTOFF_RANK = 20
DEFAULT_BUFFER_CHIPS = 1000  # chips above rank-20 floor before protect mode


def _buffer_threshold() -> int:
    raw = os.environ.get("CEMINI_QUAL_BUFFER_CHIPS")
    if raw is None or raw == "":
        return DEFAULT_BUFFER_CHIPS
    return int(raw)


def fetch_qualification_status(
    client: Any,
    competition_id: str,
    *,
    cutoff_rank: int = DEFAULT_CUTOFF_RANK,
    buffer_chips: int | None = None,
) -> dict[str, Any]:
    """Return rank/chips and whether to enable qualification_protect in decide().

    Protect when: rank <= cutoff_rank AND chips >= cutoff_chips + buffer_chips.
    Default buffer is 1000 chips above the #20 floor.
    """
    if buffer_chips is None:
        buffer_chips = _buffer_threshold()
    out: dict[str, Any] = {
        "qualification_protect": False,
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
    if int(rank) <= cutoff_rank and buffer >= buffer_chips:
        out["qualification_protect"] = True
    return out
