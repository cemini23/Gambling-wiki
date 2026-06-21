---
title: DFS pipeline integration spec
type: concept
tags: [concept, dfs, nfl, pipeline, pydfs, w-integ]
keywords: [csv-schema, normalize, fanduel, draftkings, ceiling-floor-ownership]
related:
  - entities/tools/pydfs-lineup-optimizer.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-model-orchestration.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/tools/pydfs-lineup-optimizer.md — downstream optimizer
- @scripts/normalize_dfs_projection_csv.py — current adapter (FanDuel-only)

## Raw Concept

Contract between **DIY model output** and existing wiki scripts.

## Narrative

### Two-layer schema

1. **Canonical model CSV** — one row/player with `fd_*` and `dk_*` columns
2. **Site-normalized pydfs CSV** — exact importer headers

### Canonical required fields

`slate_id`, `player_key`, `fd_id`, `fd_position`, `fd_salary`, `fd_projection`, `dk_id`, `dk_position`, `dk_salary`, `dk_projection`, `team`, `opp`, `game`, `injury_status`

### Optional pydfs extras (pass-through)

`Projected Ownership`, `Projection Floor`, `Projection Ceil`, `Max Exposure`, `Min Exposure`, `Min Deviation`, `Max Deviation`

### Script backlog

| Script | Change |
|--------|--------|
| `normalize_dfs_projection_csv.py` | Add `--site fanduel\|draftkings`; DK schema; extra column pass-through |
| `fanduel_slate_optimize.py` | Generalize to `dfs_slate_optimize.py` with `--site`; ownership rules; built-in exporter |
| New | `fanduel_late_swap_optimize.py` — `load_lineups_from_csv` + `optimize_lineups` |

### End-to-end flow

```text
DIY canonical CSV → normalize (--site fd) → dfs_slate_optimize → lineups.csv
Optional: Monte Carlo rerank on candidate pool
```

## Snippets

> Current OUT_FIELDS match FanDuel pydfs importer exactly — no breakage for FD path. [CONFIRMED — K125 W-SALARY, 2026-06-20]
