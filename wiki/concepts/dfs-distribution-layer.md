---
title: DFS distribution layer (Monte Carlo)
type: concept
tags: [concept, dfs, nfl, monte-carlo, ceiling, floor, w-dist]
keywords: [boom-bust, gaussian-copula, sim-roi, pydfs-rerank]
related:
  - concepts/dfs-stat-projection-engine.md
  - concepts/dfs-correlation-stacking.md
  - concepts/dfs-ownership-projection.md
  - entities/tools/pydfs-lineup-optimizer.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/dfs-correlation-stacking.md — correlation matrix for sampling
- @entities/tools/pydfs-lineup-optimizer.md — candidate lineup generator

## Raw Concept

Turn median projections into **distributions** for GPP ceiling/floor, contest ROI, and post-optimize reranking. **Post-optimize layer** — pydfs generates candidates; sim selects.

## Narrative

### Distribution families by position

| Position | Core family | TD modeling |
|----------|-------------|-------------|
| QB | Skew-normal + Poisson/NB pass TDs | Separate pass TD count |
| RB | Gamma core + hurdle TDs | GL/RZ xTD |
| WR/TE | Hurdle-lognormal + hurdle/NB TDs | Zero-mass + 2+ tail |

**Floor/ceiling:** P20 / P90 (not min/max). Parameterize from median via historical quantile ratios by archetype.

### Simulator architecture

1. Player outcome matrix (`N_players × N_iterations`) with copula correlation
2. Score candidate lineups (matrix multiply)
3. Generate opponent field from ownership + stack templates
4. Rank vs payout structure → **sim ROI**, **top-1%**, **win%**

### Iteration guidance

| Metric | Min iterations |
|--------|----------------|
| Median / P90 | 5k–10k |
| Top-1% / sim ROI | 20k–50k |
| Win% (large GPP) | 50k–100k+ |

### Integration

```text
pydfs optimize(n=500-2000 candidates) → Monte Carlo rerank → select final 150 by sim_roi
```

chanzer0/NFL-DFS-Tools = methodology reference only (no LICENSE — no code reuse).

## Snippets

> "They project players, we simulate games." [Source: SaberSim how-it-works — retrieved 2026-06-20]
