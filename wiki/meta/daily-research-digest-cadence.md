---
title: Daily research digest cadence (gambling-wiki)
type: concept
tags: [meta, automation, discovery, k93, federation]
keywords: [daily-research-digest, exa, sweep, inbox, federated-digest]
related:
  - meta/cross-wiki-routing.md
  - concepts/gambling-wiki-scope.md
  - concepts/gambling-bot-architecture.md
  - sources/brief-k93-federated-digest-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - sweeps/2026-06-04-daily.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - sweeps/2026-06-09-daily.md
  - sweeps/2026-06-13-daily.md
  - sweeps/2026-06-14-daily.md
  - sweeps/2026-06-15-daily.md
  - sweeps/2026-06-17-daily.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
maturity: validated
created: 2026-06-01
updated: 2026-06-17
---

## Relations

- @osint-wiki/concepts/federated-daily-research-digest.md — federation install kit (K93)
- @meta/cross-wiki-routing.md — ingest routing vs @osint-wiki
- @sources/brief-k93-federated-digest-2026-06-01.md — brief provenance

## Raw Concept

K93 federated install: morning **discovery-only** loop for sports betting, PM retail, poker/DFS, and gambling-bot eval lanes. Does **not** auto-write entity pages — Cursor **full ingest** does.

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily @ 08:15 local (`com.cemini.daily-research-digest.gambling`) |
| **Installed** | 2026-06-01 (K93 brief) |
| **Last run** | 2026-06-17 |
| **Fetch sources** | arXiv + OpenReview PDFs → `research to be indexed/` (tuned 2026-06-17) |
| **Script** | `~/bin/cemini-daily-research-digest-gambling` → `scripts/daily_research_digest_run.py` |
| **Deps** | `wiki_source_index.py` (required alongside digest runner) |
| **Config** | `scripts/daily_research_config.yaml` |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |
| **Inbox** | `research to be indexed/` (gitignored drops) |

### Operator loop

1. Review `wiki/sweeps/YYYY-MM-DD-daily.md` (or run digest manually)
2. Check rows worth fetching; optional social pass (opencli, twitter-reader)
3. Say **full ingest** in Cursor for this wiki folder on approved items
4. Weekly: optional Monokern pipeline on top `active_topics` row

### Topic lanes (config)

Kalshi/PM retail, sports betting +EV/CLV, World Cup 2026 cross-venue (cross-ref @osint-wiki WC bot), gambling-bot FOSS evals (W4), bankroll/Kelly, DFS/best ball, poker/casino study.

**Auto-fetch (2026-06-17):** 6 paper Exa lanes + `fetch.sources: [arxiv, openreview]`; `fetch_likely: true`; 10-day window; cap 8 PDFs/night. News rows still manual.

### Gates [CONFIRMED]

- Tier 3 autonomous ingest remains **NO-GO** — digest lands candidates only
- Prod bot deploy stays @osint-wiki; wagering requirements saved here

### LaunchAgent

```bash
launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.gambling.plist
```

Manual run from repo root:

```bash
python3 scripts/daily_research_digest_run.py
```

## Snippets

> "No new Adopt tools in K93 eval for gambling surface." [Source: briefs/2026-06-01_k93-gambling-digest-from-osint.md]
