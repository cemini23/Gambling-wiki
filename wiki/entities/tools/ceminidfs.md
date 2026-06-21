---
title: CeminiDFS
type: entity
tags: [tool, dfs, nfl, open-source, cemini23, w9, k125]
keywords: [ceminidfs, nflverse, pydfs, fanduel, projection-pipeline, ownership, backtest]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-strategy-overview.md
  - concepts/dfs-backtesting-framework.md
  - concepts/dfs-ownership-projection.md
  - concepts/nfl-dfs-data-sources.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/platforms/fanduel.md
  - sources/research-diy-dfs-model-master-plan-2026-06-20.md
  - "@osint-wiki/concepts/active-project-research-routing.md"
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/diy-nfl-dfs-model-architecture.md — K125 architecture hub
- @entities/tools/pydfs-lineup-optimizer.md — downstream lineup generation
- @osint-wiki/concepts/active-project-research-routing.md — morning digest + brief routing

## Raw Concept

Implementation repo for K125 DIY NFL DFS projection pipeline. Phases 0–5 complete 2026-06-20.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [github.com/cemini23/CeminiDFS](https://github.com/cemini23/CeminiDFS) |
| **Local path** | `~/Desktop/projects/CeminiDFS` |
| **Brief home** | `../CeminiDFS/briefs/` |
| **License** | MIT |
| **Primary site** | FanDuel |
| **Benchmarks** | Stokastic / FantasyLabs (accuracy only, not lineup source) |

### Morning digest steal-from

- nflverse fetch/cache patterns, PBP-derived usage models
- Projection calibration, walk-forward backtest, Spearman vs realized
- Ownership sim + copula rerank for MME pools
- Late-swap pydfs integration after team lock
- FanDuel slate GPP strategy (stacking, correlation, leverage)

### Cross-wiki boundary

- **Primary wiki:** gambling-wiki (methodology + retail DFS)
- **OSINT:** brief routing + cross-wiki ingest when source touches PM/bot stacks
