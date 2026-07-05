---
title: NFL offseason research cadence (camp → tools)
type: concept
tags: [concept, nfl, w8, offseason, camp, research]
keywords: [training-camp, camp-standouts, depth-chart, weekly-hub, k147-planning]
related:
  - meta/nfl-offseason-weekly-cadence.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/dfs-injury-and-news-workflow.md
  - sources/web-bleacher-report-key-injuries-2026-07-01.md
  - sources/web-bleacher-report-key-injuries-2026-07-01.md
  - sources/web-offseason-hub-w27-synthesis-2026-07-05.md
  - entities/tools/ceminidfs.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @meta/nfl-offseason-weekly-cadence.md — Sunday LaunchAgent + prefetch files
- @sources/web-offseason-hub-w27-synthesis-2026-07-05.md — week 27 hub ingest (2026-07-05)
- @sources/web-bleacher-report-key-injuries-2026-07-01.md — injury watchlist source
- @concepts/nfl-weekly-slate-hub-workflow.md — replaces this cadence in Sep (per-slate entries)

## Raw Concept

**Once-a-week** gambling-wiki research during Jul–Aug while pick'em tool is unbuilt: stay current on camp, depth, and platform news; maintain a **camp standout watchlist** for future props/pick'em and BBM edges.

## Narrative

### Why weekly (not daily slates)

- No REG games — slate prefetch is idle until September
- Pick'em / `prop-fair` CLI **not shipped** — no line capture or entries
- Camp news is cumulative; **weekly synthesis** beats reactive daily noise
- Daily digest still runs @ 08:15 for **discovery**; Sunday session **curates**

### Operator invoke

> "Offseason week {N} hub" / "Camp research this week"

Or open Sunday's `briefs/offseason/{season}-offseason-w{WW}-prefetch.md` after automation fires.

### Weekly research blocks

| Block | Why it matters later |
|-------|---------------------|
| **Camp standouts** | Backup RB/WR earning reps → preseason prop volume; breakout → pick'em lines in Sep |
| **Depth chart deltas** | Starter job changes → usage priors for CeminiDFS / fair-P models |
| **Injury / PUP / holdouts** | Availability priors; BBM fade candidates |
| **BBM ADP movers** | @concepts/bbm7-adp-delta-tracker.md — camp buzz often leads ADP 24–48h |
| **Futures / win totals** | Team environment (ITT priors) when projections turn on |
| **K147 signals** | Underdog/PP rule tweaks, PickLabs — inform repo spawn, not betting |

### Camp standout watchlist (carry forward)

Maintain in each hub brief — **rolling table** copied week to week:

| Player | Team | Buzz | BBM lane | Pick'em/prop lane (Sep+) | First noted |
|--------|------|------|----------|--------------------------|-------------|
| Example: RB2 | TEAM | 1st-team reps | FADE starter / stack | Rush att O/U if role sticks | 2026-w27 |

**Discipline:** name only if repeated reports or depth-chart proof — avoid one-day Twitter hype.

### What we do NOT do in Jul–Aug

- Pick'em slips or prop entries (no tool + often no meaningful lines)
- Per-slate hub files (`slate-hub-thu` etc.) — wait for REG season
- Re-research the same beat note in every tool repo — **gambling-wiki hub only**

### Transition to in-season (Sep)

| Milestone | Action |
|-----------|--------|
| Preseason exhibition slates | Optional manual hub; test FanDuel salaries if posted |
| REG Week 1 | `bash scripts/install_nfl_slate_prefetch.sh`; offload `install_nfl_offseason_weekly` |
| K147 CLI live | Add Underdog tool session after hub; still manual line entry |

### Relationship to daily digest

| Job | Role |
|-----|------|
| Digest @ 08:15 | Find URLs (camp, BBM, pick'em news) |
| **Sunday offseason weekly** | Curate → hub brief + camp watchlist |

## Snippets

> "Research once a week on offseason activity… camp stars can produce down the road." [Source: operator spec, 2026-07-05]
