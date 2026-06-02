"""Arena opponent HUD — fetch /texas/agent-stats and classify exploit targets.

Opponent styles drift as the tournament runs (more hands → updated VPIP/PFR).
Cache invalidates on: adaptive TTL, new tableId, sample-size growth, and every
N hero decisions vs the same villain (see OPPONENT_HUD_* env vars).
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Any, Optional

_MIN_SAMPLE = 12
# Hero decisions vs villain before forcing a stats refetch (even inside TTL).
_DECISIONS_BEFORE_REFRESH = int(os.environ.get("OPPONENT_HUD_DECISION_REFRESH", "4"))
# Refetch when API sampleSize grew by at least this since last cache write.
_SAMPLE_GROWTH_REFRESH = int(os.environ.get("OPPONENT_HUD_SAMPLE_DELTA", "8"))

_CLIENT: Any = None
_DECISION_COUNT: dict[tuple[str, str], int] = {}


@dataclass
class _CacheEntry:
    fetched_at: float
    stats: dict
    sample_size: int
    archetype: str
    table_id: Optional[str]


_CACHE: dict[tuple[str, str], _CacheEntry] = {}


def _arena_client() -> Optional[Any]:
    """Lazy Arena client (ARENA_API_KEY or .arena-credentials)."""
    global _CLIENT
    if _CLIENT is not None:
        return _CLIENT
    from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE

    api_key = os.environ.get("ARENA_API_KEY")
    if not api_key and CREDS_PATH.is_file():
        import json

        api_key = json.loads(CREDS_PATH.read_text()).get("apiKey")
    if not api_key:
        return None
    base = os.environ.get("ARENA_API_BASE", DEFAULT_BASE)
    _CLIENT = ArenaClient(base, api_key=api_key)
    return _CLIENT


def _villain_agent_ids(table: dict) -> list[str]:
    self_num = table.get("selfSeatNumber")
    out: list[str] = []
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == self_num:
            continue
        aid = seat.get("agentId")
        if aid and aid not in out:
            out.append(aid)
    return out


def _adaptive_ttl_s(sample_size: int) -> float:
    """High-volume villains update faster — poll their stats more often."""
    override = os.environ.get("OPPONENT_HUD_TTL_S")
    if override:
        try:
            return max(20.0, float(override))
        except ValueError:
            pass
    if sample_size >= 500:
        return 40.0
    if sample_size >= 200:
        return 60.0
    if sample_size >= 80:
        return 90.0
    return 120.0


def _should_refresh(
    entry: Optional[_CacheEntry],
    now: float,
    table_id: Optional[str],
    *,
    force: bool,
) -> bool:
    if force or entry is None:
        return True
    if table_id and entry.table_id and table_id != entry.table_id:
        return True
    age = now - entry.fetched_at
    if age >= _adaptive_ttl_s(entry.sample_size):
        return True
    return False


def invalidate_opponent_cache(
    competition_id: Optional[str] = None,
    agent_id: Optional[str] = None,
) -> None:
    """Drop cached HUD rows (all, one comp, or one villain). For tests / deploy."""
    global _CACHE, _DECISION_COUNT
    if competition_id is None and agent_id is None:
        _CACHE.clear()
        _DECISION_COUNT.clear()
        return
    drop = [
        k for k in _CACHE
        if (competition_id is None or k[0] == competition_id)
        and (agent_id is None or k[1] == agent_id)
    ]
    for k in drop:
        _CACHE.pop(k, None)
        _DECISION_COUNT.pop(k, None)


def _fetch_agent_stats(
    agent_id: str,
    competition_id: str,
    *,
    table_id: Optional[str] = None,
    force: bool = False,
) -> Optional[dict]:
    key = (competition_id, agent_id)
    now = time.time()
    hit = _CACHE.get(key)

    if not force:
        _DECISION_COUNT[key] = _DECISION_COUNT.get(key, 0) + 1
        if _DECISION_COUNT[key] >= _DECISIONS_BEFORE_REFRESH:
            force = True

    if not _should_refresh(hit, now, table_id, force=force):
        return hit.stats if hit else None

    client = _arena_client()
    if client is None:
        return hit.stats if hit else None
    try:
        body = client.get(
            f"/texas/agent-stats?agentId={agent_id}&competitionId={competition_id}"
        )
    except Exception:
        return hit.stats if hit else None
    if not isinstance(body, dict):
        return hit.stats if hit else None

    new_sample = int(body.get("sampleSize") or 0)
    new_arch = classify_archetype(body)

    _CACHE[key] = _CacheEntry(
        fetched_at=now,
        stats=body,
        sample_size=new_sample,
        archetype=new_arch,
        table_id=table_id,
    )
    _DECISION_COUNT[key] = 0
    return body


def classify_archetype(stats: dict) -> str:
    """rock | maniac | tight | unknown — aligned with Arena playingStyle."""
    style = stats.get("playingStyle") or {}
    archetype = (style.get("archetype") or "").lower()
    if archetype in ("rock", "nit"):
        return "rock"
    if archetype in ("maniac", "lag", "loose-aggressive", "loose_aggressive"):
        return "maniac"

    vpip = stats.get("vpip")
    pfr = stats.get("pfr") or 0.0
    sample = int(stats.get("sampleSize") or 0)
    if vpip is None or sample < _MIN_SAMPLE:
        return "unknown"
    if vpip < 0.15:
        return "rock"
    if vpip > 0.40 or (vpip > 0.30 and pfr > 0.25):
        return "maniac"
    if vpip < 0.22:
        return "tight"
    return "unknown"


def hud_confidence(sample_size: int, stats_age_s: float) -> float:
    """0–1 scale: trust exploit offsets more with sample + freshness."""
    if sample_size < _MIN_SAMPLE:
        return 0.0
    by_sample = min(1.0, sample_size / 80.0)
    if stats_age_s <= 60:
        freshness = 1.0
    elif stats_age_s <= 180:
        freshness = 0.85
    elif stats_age_s <= 300:
        freshness = 0.65
    else:
        freshness = 0.45
    return round(by_sample * freshness, 3)


def scale_margins(margins: dict[str, float], confidence: float) -> dict[str, float]:
    """Blend exploit deltas toward neutral when stats are thin or stale."""
    c = max(0.0, min(1.0, confidence))
    out: dict[str, float] = {}
    for k, v in margins.items():
        if k == "open_steal_equity" and v < 0.5:
            # Rock steal threshold only — blend toward passive when low confidence
            neutral = 0.99
            out[k] = neutral + (v - neutral) * c
        else:
            out[k] = v * c if k != "open_steal_equity" else v
    return out


def _profile_from_stats(
    stats: dict,
    agent_id: str,
    *,
    fetched_at: float,
    prev_archetype: Optional[str],
) -> dict:
    archetype = classify_archetype(stats)
    now = time.time()
    sample = int(stats.get("sampleSize") or 0)
    age = max(0.0, now - fetched_at)
    return {
        "agentId": agent_id,
        "archetype": archetype,
        "prevArchetype": prev_archetype,
        "archetypeShifted": bool(
            prev_archetype and prev_archetype != "unknown"
            and archetype != prev_archetype
        ),
        "vpip": stats.get("vpip"),
        "pfr": stats.get("pfr"),
        "af": stats.get("af"),
        "wsd": stats.get("wsd"),
        "sampleSize": sample,
        "statsAgeSec": round(age, 1),
        "confidence": hud_confidence(sample, age),
        "tagline": (stats.get("playingStyle") or {}).get("tagline"),
    }


def build_opponent_hud(table: dict) -> dict:
    """Return opponent_hud dict for research_context (empty if unavailable)."""
    competition_id = table.get("competitionId")
    if not competition_id or competition_id == "scenario":
        return {}

    villains = _villain_agent_ids(table)
    if not villains:
        return {}

    table_id = table.get("tableId") or table.get("id")
    profiles: list[dict] = []
    for vid in villains:
        key = (competition_id, vid)
        prev = _CACHE.get(key)
        prev_arch = prev.archetype if prev else None
        stats = _fetch_agent_stats(
            vid, competition_id, table_id=table_id, force=False,
        )
        if stats:
            fetched = (_CACHE.get(key).fetched_at if _CACHE.get(key) else time.time())
            profiles.append(_profile_from_stats(
                stats, vid, fetched_at=fetched, prev_archetype=prev_arch,
            ))

    if not profiles:
        return {"villains": [], "mode": "unknown", "primary": None}

    archetypes = [p["archetype"] for p in profiles]
    if "maniac" in archetypes:
        mode = "maniac"
        primary = next(p for p in profiles if p["archetype"] == "maniac")
    elif all(a == "rock" for a in archetypes):
        mode = "rock"
        primary = profiles[0]
    elif "rock" in archetypes:
        mode = "rock"
        primary = next(p for p in profiles if p["archetype"] == "rock")
    else:
        mode = archetypes[0] if archetypes else "unknown"
        primary = profiles[0]

    conf = float((primary or {}).get("confidence") or 0.0)
    margins = scale_margins(exploit_margins(mode), conf)

    return {
        "villains": profiles,
        "primary": primary,
        "mode": mode,
        "margins": margins,
        "confidence": conf,
    }


def exploit_margins(mode: str) -> dict[str, float]:
    """Threshold deltas applied in cemini_decide (negative = looser / more aggressive)."""
    if mode == "rock":
        return {
            "bet_bar_delta": -0.10,
            "call_margin_delta": 0.02,
            "fold_slack_delta": 0.05,
            "preflop_fold_margin_delta": 0.04,
            "open_steal_equity": 0.36,
        }
    if mode == "maniac":
        return {
            "bet_bar_delta": 0.06,
            "call_margin_delta": -0.05,
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
