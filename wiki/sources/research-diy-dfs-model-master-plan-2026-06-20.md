---
title: DIY NFL DFS model — master research plan (K125)
type: source
tags: [source, research-plan, dfs, nfl, diy-model, w8]
keywords: [diy-projections, nfl-dfs, research-plan, subagent-dispatch, fanduel]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-paid-tool-methodologies.md
  - concepts/dfs-strategy-overview.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/platforms/fanduel.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/diy-nfl-dfs-model-architecture.md — keystone synthesis target
- @concepts/dfs-paid-tool-methodologies.md — paid-tool reverse-engineering workstream
- @entities/tools/pydfs-lineup-optimizer.md — downstream optimizer integration

## Raw Concept

**Master research plan** for building a DIY NFL DFS projection model (FanDuel-primary). Authored by Opus 4.8 planning subagent, 2026-06-20. **18 workstreams · 38 subagents · 6 execution waves.** Research-only dispatch — implementation follows synthesis.

## Narrative

### Executive summary

Build a from-scratch NFL DFS projection pipeline whose output feeds `scripts/normalize_dfs_projection_csv.py` → `scripts/fanduel_slate_optimize.py`. Stokastic/FantasyLabs retained as **paid accuracy benchmark only**. Layers: game environment (Vegas) → volume (pace/pass-run) → usage (snap/target/carry) → stat projection → site scoring → distribution (Monte Carlo) → ownership/field. Every choice must be backtest-justified and data-source license-cleared.

### Workstreams (18)

| ID | Title | Priority | Subagents |
|----|-------|----------|-----------|
| W-DATA | Core data backbone (nflverse) | P0 | 3 |
| W-VEGAS | Vegas lines ingestion | P0 | 2 |
| W-WEATHER | Weather + dome metadata | P1 | 1 |
| W-INJ | Injuries, depth charts, news | P0 | 2 |
| W-SALARY | FD/DK salary files + slate | P0 | 1 |
| W-IMPLIED | Implied team totals | P0 | 1 |
| W-VOLUME | Pace + pass/run split | P0 | 2 |
| W-USAGE | Player usage shares | P0 | 3 |
| W-STATPROJ | Stat projection engine | P0 | 3 |
| W-SCORING | FD half-PPR vs DK full-PPR | P0 | 1 |
| W-DIST | Distributions + Monte Carlo | P1 | 2 |
| W-CORR | Correlation + stacking | P1 | 1 |
| W-OWN | Ownership + field modeling | P1 | 3 |
| W-NEWS | Human override + late swap | P1 | 1 |
| W-BACKTEST | Backtesting framework | P0 | 2 |
| W-FOSS | FOSS tooling landscape | P1 | 3 |
| W-PAID-RE | Paid tool reverse-engineering | P1 | 2 |
| W-LEGAL | ToS / scraping posture | P0 | 1 |
| W-INTEG | Pipeline integration spec | P0 | 1 |
| W-ORCH | Orchestration + config | P1 | 1 |

### Execution waves

```
Wave0: W-DATA, W-VEGAS, W-SALARY, W-PAID-RE
Wave1: W-WEATHER, W-INJ, W-IMPLIED, W-FOSS, W-SCORING
Wave2: W-VOLUME → W-USAGE
Wave3: W-STATPROJ
Wave4: W-DIST, W-CORR, W-OWN (parallel)
Wave5: W-NEWS, W-INTEG
Wave6: W-BACKTEST, W-ORCH
Cross: W-LEGAL (Wave0 start → Wave5 finalize)
```

### Synthesis targets (post-research)

1. `concepts/diy-nfl-dfs-model-architecture.md` (keystone)
2. `concepts/nfl-dfs-data-sources.md`
3. Layer concept pages (14+) per workstream deliverables
4. Updates: dfs-strategy-overview, tool pages, fanduel/draftkings, index, log, ROADMAP

## Snippets

> "Totals: 18 workstreams · 38 subagents · 6 execution waves." [Source: Opus 4.8 planning subagent, 2026-06-20]

Full subagent dispatch spec (agent_id, focus_question, search_targets, output_format) lives in conversation transcript and ROADMAP W8/K125 entry.
