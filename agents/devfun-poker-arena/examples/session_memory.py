"""Lightweight per-session villain memory for lobby play.

Tracks recent aggression per opponent agent id within a competition session.
Fed into cemini_decide via research_context — mirrors Agent Memory Test themes:
extract stable patterns, update on new evidence, abstain when sample is thin.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any

_MIN_SAMPLES = 3
_AGGR_THRESHOLD = 0.55  # fold-to-bet rate below this → "aggro"


def _seat_agent_map(table: dict) -> dict[int, str]:
    out: dict[int, str] = {}
    for s in table.get("seats") or []:
        sn = s.get("seatNumber")
        aid = s.get("agentId") or s.get("playerId")
        if sn is not None and aid:
            out[int(sn)] = str(aid)
    return out


def _hero_seat(table: dict) -> int | None:
    sn = table.get("selfSeatNumber")
    return int(sn) if sn is not None else None


def _street_bets(table: dict) -> list[tuple[str, int, int]]:
    """(agent_id, chips, seat) for current-street aggressive actions if present."""
    events = table.get("actionHistory") or table.get("actions") or []
    street = (table.get("street") or "").lower()
    rows: list[tuple[str, int, int]] = []
    agents = _seat_agent_map(table)
    for ev in events:
        if not isinstance(ev, dict):
            continue
        if street and (ev.get("street") or "").lower() not in ("", street):
            continue
        act = (ev.get("action") or ev.get("type") or "").lower()
        if act not in ("bet", "raise", "all-in", "allin"):
            continue
        seat = ev.get("seatNumber")
        if seat is None:
            continue
        aid = agents.get(int(seat)) or ev.get("agentId")
        if not aid:
            continue
        amt = int(ev.get("amount") or ev.get("chips") or 0)
        rows.append((str(aid), amt, int(seat)))
    return rows


def update_session_memory(state: dict, table: dict) -> None:
    """Call after each hero action submission with latest table snapshot."""
    mem = state.setdefault("session_villain_memory", {})
    hero = _hero_seat(table)
    if hero is None:
        return
    for aid, _amt, seat in _street_bets(table):
        if seat == hero:
            continue
        rec = mem.setdefault(aid, {"aggressive_acts": 0, "passive_acts": 0, "samples": 0})
        rec["aggressive_acts"] = int(rec.get("aggressive_acts", 0)) + 1
        rec["samples"] = int(rec.get("samples", 0)) + 1
    # Passive signal from checked/called line on current street (lightweight)
    agents = _seat_agent_map(table)
    events = table.get("actionHistory") or table.get("actions") or []
    street = (table.get("street") or "").lower()
    for ev in events:
        if not isinstance(ev, dict):
            continue
        if street and (ev.get("street") or "").lower() not in ("", street):
            continue
        act = (ev.get("action") or ev.get("type") or "").lower()
        if act not in ("check", "call"):
            continue
        seat = ev.get("seatNumber")
        if seat is None or int(seat) == hero:
            continue
        aid = agents.get(int(seat)) or ev.get("agentId")
        if not aid:
            continue
        rec = mem.setdefault(str(aid), {"aggressive_acts": 0, "passive_acts": 0, "samples": 0})
        rec["passive_acts"] = int(rec.get("passive_acts", 0)) + 1
        rec["samples"] = int(rec.get("samples", 0)) + 1


def villain_memory_for_table(state: dict, table: dict) -> dict[str, Any]:
    """Return memory slice for active villains at this table."""
    mem = state.get("session_villain_memory") or {}
    hero = _hero_seat(table)
    agents = _seat_agent_map(table)
    villains: dict[str, dict] = {}
    for seat, aid in agents.items():
        if hero is not None and seat == hero:
            continue
        rec = mem.get(aid)
        if not rec:
            continue
        samples = int(rec.get("samples", 0))
        if samples < _MIN_SAMPLES:
            villains[aid] = {"label": "unknown", "samples": samples, "confidence": "low"}
            continue
        ag = int(rec.get("aggressive_acts", 0))
        total = max(1, ag + int(rec.get("passive_acts", 0)))
        aggr_rate = ag / total
        label = "aggro" if aggr_rate >= _AGGR_THRESHOLD else "passive"
        villains[aid] = {
            "label": label,
            "aggr_rate": round(aggr_rate, 2),
            "samples": samples,
            "confidence": "high" if samples >= 8 else "medium",
        }
    if not villains:
        return {"villains": {}, "note": "abstain — insufficient session samples"}
    return {"villains": villains}


def exploit_from_memory(villain_mem: dict[str, Any]) -> dict[str, float]:
    """Map session memory to margin deltas (neutral if abstaining)."""
    villains = villain_mem.get("villains") or {}
    if not villains:
        return {}
    labels = [v.get("label") for v in villains.values() if v.get("confidence") != "low"]
    if not labels:
        return {}
    if labels.count("aggro") >= labels.count("passive"):
        return {"call_margin_delta": -0.02, "fold_slack_delta": 0.03}
    return {"bet_bar_delta": -0.02, "call_margin_delta": 0.02}
