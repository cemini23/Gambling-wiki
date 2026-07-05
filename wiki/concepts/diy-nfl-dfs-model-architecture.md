---
title: DIY NFL DFS model architecture
type: concept
tags: [concept, dfs, nfl, diy-model, architecture, w8, k125]
keywords: [diy-projections, fanduel, nflverse, monte-carlo, ownership, pipeline]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/dfs-paid-tool-methodologies.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/implied-team-totals-dfs.md
  - concepts/team-volume-pace-model.md
  - concepts/player-usage-models.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/fd-dk-scoring-conversion.md
  - concepts/dfs-distribution-layer.md
  - concepts/dfs-correlation-stacking.md
  - concepts/dfs-ownership-projection.md
  - concepts/dfs-backtesting-framework.md
  - concepts/dfs-pipeline-integration-spec.md
  - concepts/dfs-foss-tooling-landscape.md
  - concepts/dfs-weather-adjustments.md
  - concepts/dfs-injury-and-news-workflow.md
  - concepts/dfs-model-orchestration.md
  - concepts/line-shopping-and-clv.md
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - entities/tools/momentum-odds.md
  - entities/sports/nfl-betting.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/ceminidfs.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - sources/research-diy-pickem-props-master-plan-2026-07-05.md
  - entities/platforms/fanduel.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
  - sources/research-diy-dfs-model-master-plan-2026-06-20.md
  - sources/research-nfl-dfs-id-mapping-2026-06-20.md
  - sources/research-nfl-historical-odds-2026-06-20.md
  - "@osint-wiki/concepts/nfl-coherence-risk-features.md"
maturity: draft
created: 2026-06-20
updated: 2026-06-26
---

## Relations

- @sources/research-diy-dfs-model-master-plan-2026-06-20.md — K125 master plan (18 workstreams · 38 subagents)
- @sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md — sibling-wiki weather/orchestration inventory
- @osint-wiki/concepts/nfl-coherence-risk-features.md — K126 ClarusC64 coherence-risk feature suite (stage-2 extensions)
- @concepts/dfs-paid-tool-methodologies.md — paid benchmark reference
- @entities/tools/ceminidfs.md — implementation repo (K125/W9)
- @entities/tools/pydfs-lineup-optimizer.md — lineup generation downstream
- @concepts/diy-nfl-pickem-props-tool-architecture.md — sibling K147 pick'em tool (shares projection layers only)
- @sources/research-diy-pickem-props-master-plan-2026-07-05.md — K147 master plan (14 workstreams)

## Raw Concept

From-scratch **NFL DFS projection pipeline** (FanDuel-primary) feeding pydfs optimizer. **Implementation repo:** [github.com/cemini23/CeminiDFS](https://github.com/cemini23/CeminiDFS). Stokastic/FantasyLabs = **accuracy benchmark only**. Research completed K125 (2026-06-20).

## Narrative

### Goal

Emit normalized per-player CSV (median + optional ceiling/floor/ownership) → existing pydfs FanDuel optimizer. Every modeling choice backtest-justified; every data source license-cleared.

### Layer diagram

```mermaid
flowchart TD
    subgraph SRC["Data Sources"]
        PBP["nflreadpy / nflverse"]
        VEG["Vegas: schedules + Odds API"]
        WX["Open-Meteo + stadium table"]
        INJ["load_injuries + inactives"]
        SAL["FD/DK salary CSV manual"]
    end
    subgraph ENV["Game Environment"]
        ITT["Implied team totals"]
        PACE["Pace / PROE"]
    end
    subgraph VOL["Volume"]
        PLAYS["Team plays"]
        SPLIT["Pass / run split"]
    end
    subgraph USE["Usage"]
        SNAP["Snap / route gate"]
        TGT["Target / carry / RZ share"]
    end
    subgraph STAT["Stat Projection"]
        EFF["Efficiency + defense adj"]
        CNT["Counting stats"]
    end
    subgraph SCORE["Scoring"]
        FD["FanDuel half-PPR"]
        DK["DraftKings full-PPR"]
    end
    subgraph DIST["Distribution + Field"]
        MC["Monte Carlo + copula"]
        OWN["Ownership + field sim"]
    end
    OPT["pydfs optimizer"]
    BT["Backtest loop"]

    PBP --> ENV & VOL & USE & STAT
    VEG --> ITT
    ITT --> PLAYS
    PLAYS --> USE
    USE --> CNT
    EFF --> CNT
    CNT --> FD & DK
    FD --> MC
    MC --> OPT
    OWN --> OPT
    SAL --> OPT
    MC --> BT
    BT -.calibration.-> STAT
```

### Layer pages (K125)

| Layer | Page | Status |
|-------|------|--------|
| Data + legal | @concepts/nfl-dfs-data-sources.md | draft |
| FOSS stack | @concepts/dfs-foss-tooling-landscape.md | draft |
| Implied totals | @concepts/implied-team-totals-dfs.md | draft |
| Volume / pace | @concepts/team-volume-pace-model.md | draft |
| Usage | @concepts/player-usage-models.md | draft |
| Stat engine | @concepts/dfs-stat-projection-engine.md | draft |
| Scoring | @concepts/fd-dk-scoring-conversion.md | draft |
| Distribution | @concepts/dfs-distribution-layer.md | draft |
| Correlation | @concepts/dfs-correlation-stacking.md | draft |
| Ownership | @concepts/dfs-ownership-projection.md | draft |
| Weather | @concepts/dfs-weather-adjustments.md | draft |
| Injury / news | @concepts/dfs-injury-and-news-workflow.md | draft |
| Backtest | @concepts/dfs-backtesting-framework.md | draft |
| Integration | @concepts/dfs-pipeline-integration-spec.md | draft |
| Orchestration | @concepts/dfs-model-orchestration.md | draft |
| Paid methods | @concepts/dfs-paid-tool-methodologies.md | draft |

### Build vs borrow (summary)

| Component | Verdict |
|-----------|---------|
| Data backbone | **Borrow** nflreadpy |
| Vegas history | **Borrow** load_schedules |
| Vegas live | **Borrow** The Odds API (CONDITIONAL quota) |
| Optimizer | **Borrow** pydfs (MIT) |
| Projections v1 | **Build** stat-first regression |
| Ownership | **Build** (FantasyLabs labels for train) |
| Contest sim | **Build** v2; chanzer0 = ideas only |
| Salaries | **Manual** FD/DK export |

### Implementation backlog (ROADMAP K125)

1. `normalize_dfs_projection_csv.py` — `--site`, DK path, extra columns
2. `dfs_slate_optimize.py` — generalize from FD-only
3. `nfl_dfs_weekly_run.py` — orchestrator + manifest
4. `fanduel_late_swap_optimize.py` — W-NEWS path
5. `scripts/dfs_backtest.py` — walk-forward harness [future]

### Cross-wiki resources (K125 sweep 2026-06-20)

Full matrix: @sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md

| Need | Primary wiki | Key pages |
|------|--------------|-----------|
| Weather APIs | **@osint-wiki** | open-meteo, nws-weather-gov, visualcrossing, wethr-net, ensemble-weather-forecasting |
| API keys / limits | **@osint-wiki** | api-credential-registry |
| Pipeline DAG | **@ccc-wiki** | plan-then-execute-topological-orchestration, scatter-gather |
| CLV / sharp benchmark | **@gambling-wiki** | line-shopping-and-clv |
| Bankroll / Kelly | **@gambling-wiki** | bankroll-management, kelly-criterion-betting |
| Multi-book signals | both | momentum-odds (gambling stub ↔ osint deep page) |
| Raw archive | both | cemini-egress-fi (osint) = gambling CLAUDE.md archive path |

## Snippets

> "18 workstreams · 38 subagents · 6 execution waves." [Source: @sources/research-diy-dfs-model-master-plan-2026-06-20.md]
