---
title: DFS backtesting framework
type: concept
tags: [concept, dfs, nfl, backtest, accuracy, w-backtest]
keywords: [mae, rmse, spearman, walk-forward, leakage, benchmark]
related:
  - concepts/pickem-backtesting-framework.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/dfs-ownership-projection.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/line-shopping-and-clv.md
  - sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
  - sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md
maturity: draft
created: 2026-06-20
updated: 2026-06-25
---

## Relations

- @concepts/pickem-backtesting-framework.md — sibling harness for K147 props grading
- @entities/tools/stokastic-dfs.md — paid benchmark CSV column
- @entities/tools/fantasylabs-dfs.md — paid benchmark CSV column

## Raw Concept

Walk-forward, **leakage-safe** evaluation of DIY projections vs actuals and contest equity.

## Narrative

### Metric suite

| Metric | Purpose |
|--------|---------|
| MAE / RMSE by position | Point accuracy |
| Spearman rank corr | Ordering quality (often more important for DFS) |
| Mean error (bias) | Systematic over/under |
| Top-decile hit rate | GPP-relevant tails |

### Benchmark MAE targets (good models, weekly)

| Pos | Good | Very good |
|-----|------|-----------|
| QB | ≤6.3 | ≤6.1 |
| RB | ≤5.3 | ≤5.0 |
| WR | ≤5.0 | ≤4.85 |
| TE | ≤3.9 | ≤3.75 |

Source: Fantasy Football Analytics 2015–2025 vendor review [TENTATIVE — verify against current season].

### Harness design

- **Unit:** main slate × week
- **Cutoff:** fixed (e.g. Sunday T-90) — immutable snapshots
- **Train:** all slates before week t; **predict:** week t only
- **Benchmark table:** separate `benchmark_player_snapshot` — preserve raw Stokastic/Labs columns, not normalized FPPG only

### Leakage checklist

- No post-lock injuries in features
- No actual ownership in same-slate training features
- No future Vegas unless timestamp-valid at cutoff
- Version every export snapshot (vendor CSV can update intraday)

### Contest equity layer

Sim correlated outcomes + field → EV/ROI/cash%/top-1%. Compare DIY vs Stokastic vs Labs vs naive baseline.

## Snippets

> "Rank correlation tells you if you put the right players ahead of the wrong ones." [Source: K125 W-BACKTEST synthesis, 2026-06-20]
