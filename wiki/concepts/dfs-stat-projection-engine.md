---
title: DFS stat projection engine
type: concept
tags: [concept, dfs, nfl, projections, regression, w-statproj]
keywords: [efficiency, xtd, defense-adjustment, hybrid-model, v1-v2]
related:
  - concepts/player-usage-models.md
  - concepts/fd-dk-scoring-conversion.md
  - concepts/dfs-distribution-layer.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-foss-tooling-landscape.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/player-usage-models.md — volume × usage inputs
- @concepts/fd-dk-scoring-conversion.md — counting stats → site points

## Raw Concept

Convert volume + usage into counting stats, then site fantasy points. **V1: stat-first regression; V2: hybrid + Monte Carlo.**

## Narrative

### Paradigm decision (W-STATPROJ)

| Paradigm | V1 fit | Notes |
|----------|--------|-------|
| **Regression on efficiency** | **Recommended v1** | Fast, debuggable, feeds pydfs median |
| Monte Carlo play sim | v2 | SaberSim-style; needs v1 parameters anyway |
| Hybrid | **Recommended v2** | v1 medians + distribution layer |

Build order: team plays → usage shares → per-attempt efficiency → counting stats → FD/DK scoring.

### Efficiency stability ranking

1. **aDOT** — direct role stat; light shrinkage (`k ~ 40–70 targets`)
2. **Catch rate** — depth-adjusted only; `k ~ 80–140 targets`
3. **YPA** — derived; heavy shrinkage (`k ~ 250–400 attempts`)
4. **YPC** — mostly team environment; `k ~ 250–400 carries`
5. **TD rate** — replace with **xTD / RZ opportunity**; do not project raw TD rate

### Defense adjustment (stat-defense-adj)

Use **split pass/rush EPA allowed** from nflfastR, shrunk toward prior:

- Weeks 1–4: no opponent schedule adj (or α=0.15); cap efficiency multiplier at ±3.5% pass / ±2.5% rush
- Weeks 9+: α up to 0.50; cap ±7% pass / ±5% rush
- Do **not** use aggressive full DVOA-style opponent adjustment on defense — can reduce predictive power [TENTATIVE — OSF rolling EPA study]

### Core pseudocode

```text
counting_stat = volume × usage_share × regressed_efficiency × defense_multiplier
fantasy_pts = scoring_function(counting_stat, site=FD|DK)
```

## Snippets

> "Trust volume to drive the projection; let efficiency only bend it." [Source: K125 W-STATPROJ synthesis, 2026-06-20]
