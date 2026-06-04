#!/usr/bin/env python3
"""Print competition field intel from export_competition_hands.py output.

Usage:
    uv run examples/competition_field_report.py reports/exports/playground-s1-live/
    pokerkit field-report reports/exports/playground-s1-live/ --hero cemini_wiki_poker
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out: list[dict] = []
    for line in path.read_text().splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def _dedupe_agents(rows: list[dict]) -> list[dict]:
    by_id: dict[str, dict] = {}
    for a in rows:
        aid = a.get("agent_id")
        if not aid:
            continue
        prev = by_id.get(aid)
        if prev is None or (a.get("rank") or 9999) < (prev.get("rank") or 9999):
            by_id[aid] = a
    return sorted(by_id.values(), key=lambda x: x.get("rank") or 9999)


def _fmt_pct(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    return f"{float(value):.1%}"


def _avg_stat(group: list[dict], key: str) -> float | None:
    vals = [(a.get("stats") or {}).get(key) for a in group]
    nums = [v for v in vals if isinstance(v, (int, float))]
    return mean(nums) if nums else None


def _leader_agent(agents: list[dict]) -> dict | None:
    """Return rank-1 agent; fall back to best (lowest) rank when export is partial."""
    if not agents:
        return None
    rank_one = next((a for a in agents if a.get("rank") == 1), None)
    if rank_one is not None:
        return rank_one
    return min(agents, key=lambda x: x.get("rank") or 9999)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Competition field report from export dir")
    p.add_argument("export_dir", type=Path, help="Directory with agents.jsonl, tables.jsonl")
    p.add_argument("--hero", default="cemini_wiki_poker")
    p.add_argument("--top", type=int, default=15, help="Leaderboard rows to print")
    args = p.parse_args(argv)

    export_dir = args.export_dir
    agents = _dedupe_agents(_load_jsonl(export_dir / "agents.jsonl"))
    tables = _load_jsonl(export_dir / "tables.jsonl")
    if not agents:
        print(f"No agents.jsonl in {export_dir}", file=sys.stderr)
        return 1

    handle_rank = {a["handle"]: a.get("rank") for a in agents if a.get("handle")}
    handle_stats = {a["handle"]: a.get("stats") or {} for a in agents if a.get("handle")}

    print(f"=== Field report: {export_dir.name} ({len(agents)} agents, {len(tables)} tables) ===\n")
    print(f"{'Rank':>4}  {'Chips':>6}  {'Hands':>5}  {'VPIP':>6}  {'PFR':>6}  {'3b':>6}  {'Style':<16}  Handle")
    for a in agents[: args.top]:
        st = a.get("stats") or {}
        vp = st.get("vpip")
        pf = st.get("pfr")
        tb = st.get("three_bet_pct")
        print(
            f"{a.get('rank', '?'):>4}  {a.get('chips', 0):>6}  {(a.get('hands') or 0):>5}  "
            f"{_fmt_pct(vp):>6}  {_fmt_pct(pf):>6}  {_fmt_pct(tb):>6}  "
            f"{(st.get('playing_style') or '?'):<16}  {a.get('handle')}"
        )

    hero = next((a for a in agents if (a.get("handle") or "").lower() == args.hero.lower()), None)
    leader = _leader_agent(agents)
    if hero and leader:
        leader_label = leader.get("handle") or f"rank {leader.get('rank', '?')}"
        print(f"\n=== Hero vs #1 ({leader_label}) ===")
        for key in ("vpip", "pfr", "three_bet_pct"):
            hs = (hero.get("stats") or {}).get(key)
            ls = (leader.get("stats") or {}).get(key)
            print(f"  {key}: hero={_fmt_pct(hs)}  #1={_fmt_pct(ls)}")

    top50 = agents[:50]
    styles = Counter((a.get("stats") or {}).get("playing_style") or "unknown" for a in top50)
    print(f"\n=== Top-50 playing_style ===")
    for style, n in styles.most_common():
        print(f"  {style}: {n}")

    for label, grp in [("top5", agents[:5]), ("top20", agents[:20]), ("21-50", agents[20:50])]:
        vp = _avg_stat(grp, "vpip")
        pf = _avg_stat(grp, "pfr")
        if vp is not None:
            line = f"{label:8} avg VPIP={_fmt_pct(vp)}"
            if pf is not None:
                line += f"  PFR={_fmt_pct(pf)}"
            print(line)

    grok = [a for a in agents if "grok" in (a.get("handle") or "").lower()]
    grok_top = sorted(grok, key=lambda x: x.get("rank") or 9999)[:10]
    print(f"\n=== Grok cluster ({len(grok)} agents, top 10 by rank) ===")
    for a in grok_top:
        st = a.get("stats") or {}
        vp = st.get("vpip")
        print(f"  #{a.get('rank')} {a.get('handle')}  VPIP={_fmt_pct(vp)}")

    h2h: dict[str, dict[str, int]] = defaultdict(lambda: {"tables": 0, "villain_won_pot": 0})
    co_tables: Counter[str] = Counter()
    for t in tables:
        seats = t.get("seats") or []
        hero_seat = next(
            (s for s in seats if (s.get("handle") or "").lower() == args.hero.lower()),
            None,
        )
        if not hero_seat:
            continue
        winners = {w.get("handle") for w in (t.get("winners") or []) if w.get("handle")}
        for s in seats:
            vh = s.get("handle")
            if not vh or vh.lower() == args.hero.lower():
                continue
            co_tables[vh] += 1
            h2h[vh]["tables"] += 1
            if vh in winners:
                h2h[vh]["villain_won_pot"] += 1

    if co_tables:
        print(f"\n=== Frequent tablemates ({args.hero}) ===")
        for h, n in co_tables.most_common(8):
            r = handle_rank.get(h, "?")
            vp = handle_stats.get(h, {}).get("vpip")
            pots = h2h[h]["villain_won_pot"]
            print(f"  {n:>3}x  #{r}  {h}  VPIP={_fmt_pct(vp)}  pots_won={pots}")

        print("\n=== Most pots won vs hero (min 3) ===")
        for h, rec in sorted(h2h.items(), key=lambda x: -x[1]["villain_won_pot"]):
            if rec["villain_won_pot"] < 3:
                continue
            r = handle_rank.get(h, "?")
            print(f"  {rec['villain_won_pot']:>3} pots / {rec['tables']:>3} tables  #{r}  {h}")

    print("\nNote: export lacks street actions and negative hero payouts — use HL analyze for leak patches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
