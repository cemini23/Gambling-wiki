---
title: NFL historical odds archive research (Vegas backtest)
type: source
tags: [source, brief, dfs, nfl, vegas, backtest, nflverse]
keywords: [load_schedules, spread_line, total_line, spreadspoke, implied-totals]
related:
  - concepts/pickem-data-sources.md
  - concepts/pickem-backtesting-framework.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/implied-team-totals-dfs.md
  - concepts/dfs-backtesting-framework.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - entities/tools/ceminidfs.md
maturity: validated
read_status: deep-read
created: 2026-06-20
updated: 2026-06-26
cross-wiki-source: "briefs/nfl-historical-odds-research.md"
---

## Relations

- @concepts/pickem-data-sources.md — game-level history; prop lines need extension
- @concepts/pickem-backtesting-framework.md — CLV / walk-forward consumer
- @concepts/implied-team-totals-dfs.md — Vegas → team total workflow
- @concepts/dfs-backtesting-framework.md — walk-forward eval discipline
- @entities/tools/ceminidfs.md — pipeline consumer

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | NFL historical odds research (vegas-history agent) |
| **Date** | 2026-06-20 |
| **Verdict** | **GO** nflreadr schedules · **NO-GO** Spreadspoke for 5+ season DFS |

## Narrative

### Source comparison

| Source | Coverage | Join | Verdict |
|--------|----------|------|---------|
| **`nflreadr::load_schedules()`** | Closing spread/total + juice (5+ seasons complete) | Native `game_id` | **GO** |
| **Kaggle Spreadspoke** | Lines since 1979 | Manual team/date join | **NO-GO** for modern DFS backtest |
| **Scraped archives** | Variable | Heavy cleaning | Avoid unless paid API |

### Caveats

- No free granular **opening** line history in nflverse — closing lines only
- Early-year juice columns may be sparse pre-2010; last 5 seasons pristine for DFS

### CeminiDFS use

Feed implied team totals layer in projection pipeline; join PBP via `game_id` without custom mapping overhead.

## Dead Ends

- Spreadspoke for CeminiDFS primary backtest (mapping overhead, no advantage vs nflreadr)
- Opening-line CLV studies without paid odds API
