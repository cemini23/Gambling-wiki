---
title: NFL offseason weekly research cadence
type: concept
tags: [meta, automation, nfl, w8, offseason, camp]
keywords: [weekly, training-camp, camp-standouts, k147-planning, bbm-adp]
related:
  - concepts/nfl-weekly-slate-hub-workflow.md
  - concepts/nfl-offseason-research-cadence.md
  - meta/daily-research-digest-cadence.md
  - meta/nfl-slate-prefetch-cadence.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/bbm7-adp-delta-tracker.md
  - sources/web-offseason-hub-w27-synthesis-2026-07-05.md
  - sources/web-offseason-hub-w28-synthesis-2026-07-19.md
  - sources/web-offseason-hub-w29-synthesis-2026-07-19.md
  - sources/web-bleacher-report-key-injuries-2026-07-01.md
maturity: draft
created: 2026-07-05
updated: 2026-07-19
---

## Relations

- @concepts/nfl-offseason-research-cadence.md — operator topics and watchlist discipline
- @meta/nfl-slate-prefetch-cadence.md — **Sep+** in-season; defer until REG slates

## Raw Concept

**Sunday weekly** automation (Jul–Aug): prefetch stub for camp, depth, ADP, and K147 planning — **no pick'em entries**, tool build still in progress.

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Sundays @ 09:15 local (`com.cemini.nfl-offseason-weekly.gambling`) |
| **Window** | Jul–Aug (camp / preseason); swap to slate prefetch in Sep |
| **Script** | `~/bin/cemini-nfl-offseason-weekly-gambling` |
| **Output** | `briefs/offseason/{season}-offseason-w{WW}-prefetch.md` |
| **Hub target** | `briefs/offseason/{season}-offseason-w{WW}-hub.md` |

### vs in-season slate prefetch

| Mode | When | Focus |
|------|------|-------|
| **Offseason weekly** | Jul–Aug | Camp stars, depth, ADP, K147 build, futures — **research only** |
| **Slate prefetch** | Sep–Feb | Per-slate Thu/Sun/SNF/MNF hub before entries |

### Install

```bash
bash scripts/install_nfl_offseason_weekly.sh
```

Manual:

```bash
python3 scripts/nfl_offseason_weekly_run.py
```

### Operator loop

1. Sunday notification → open gambling-wiki in Cursor
2. Read prefetch + complete hub brief with agent
3. Optional: deep-read 2–3 unchecked digest URLs from camp/BBM clusters
4. File camp standout rows in hub watchlist table

**No tool sessions required** until preseason slates or pick'em CLI exists.

## Snippets

> "Offseason camp stars can produce down the road." [Source: operator spec, 2026-07-05]
