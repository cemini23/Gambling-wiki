---
title: Pick'em fair probability P(stat > line)
type: concept
tags: [concept, pickem, fair-value, distribution, nfl, props, k147, w-fair-prob]
keywords: [p-over, marginal, lognormal, poisson, median-trap, stat-line]
related:
  - concepts/dfs-distribution-layer.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/pickem-stat-type-mapping.md
  - concepts/pickem-payout-and-breakeven.md
  - concepts/pickem-slip-ev-and-correlation.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/dfs-distribution-layer.md — Monte Carlo / marginal families reused for per-stat CDFs
- @concepts/dfs-stat-projection-engine.md — median counting-stat projections feed marginals
- @concepts/pickem-stat-type-mapping.md — which lounge stat types map to which projection outputs
- @concepts/pickem-payout-and-breakeven.md — fair `p` vs implied breakeven for edge
- @concepts/diy-nfl-pickem-props-tool-architecture.md — core math layer #1 in pick'em tool

## Raw Concept

Estimate **fair probability** that a player's realized stat exceeds the posted pick'em line: `P(stat > line)` from a **full projected distribution**, not from median vs line alone.

## Narrative

### Median trap (do not use for edge)

Pick'em lounges post lines near the market median. Comparing `median > line` → "over" is **wrong** for binary pricing:

- Skewed stats (yards, TD counts): median ≠ mean; tail mass matters for O/U.
- Integer stats with pushes: `P(over)` depends on continuity correction at `.5` lines.
- Combo props (rush + rec yards): need **sum distribution**, not sum of medians.

**Rule:** always integrate or simulate from the marginal CDF `F(x) = P(stat ≤ x)`:

```
P(over) = 1 − F(line)     # strict > line at half-point lines (e.g. 74.5)
P(over) = 1 − F(line − ε)   # platform-specific tie/push rules — verify per lounge
```

### Adapt dfs-distribution-layer for per-stat marginals

DFS GPP layer simulates **fantasy points** with copula correlation (@concepts/dfs-distribution-layer.md). Pick'em layer needs **raw stat marginals** per prop type:

| Step | DFS layer | Pick'em adaptation |
|------|-----------|-------------------|
| 1 | Position-based FP family | **Stat-specific** family per `stat_type` |
| 2 | Copula across players | Marginals first; correlation deferred to slip layer |
| 3 | P20/P90 for ceiling | `P(over line)` at posted `line` |
| 4 | 20k+ iters for sim ROI | 5k–10k sufficient per marginal [TENTATIVE] |

Pipeline:

```text
stat_projection_engine → median + dispersion params
  → fit marginal F_i per player/stat
  → P(over line_i) = 1 − F_i(line_i)
```

Export from CeminiDFS-style `project` as `(player, stat, median, sigma_or_shape, family)` rows — not FD fantasy points.

### Distribution family guidance by stat type

| Stat category | Examples | Recommended family | Notes |
|---------------|----------|-------------------|-------|
| Continuous positive skew | Pass yards, rush yards, rec yards | **Lognormal** or skew-normal | Match mean to projection; calibrate σ from historical CV by role |
| Receptions, attempts | Rec, pass att, rush att | **Normal** (μ ≥ 3) or **Negative binomial** | Discrete; use `P(X > line)` with integer support |
| Count / rare events | TDs, INTs, sacks | **Poisson** or **zero-inflated Poisson** | Hurdle for "anytime TD" vs yard props |
| Yards + TD combos | Rush+rec TD, fantasy score | **Sum of marginals** or **joint sim** | Prefer correlated draw if TD included |
| K/DST points | Kicking, D/ST | Platform-specific scoring | Map via @concepts/pickem-stat-type-mapping.md |

**Parameterization from median** (lognormal example):

```
Given median m, assume CV from historical bucket (QB pass yds, WR rec yds, …)
σ_ln ≈ sqrt(ln(1 + CV²))
μ_ln = ln(m) − σ_ln²/2
P(over L) = 1 − Φ((ln L − μ_ln) / σ_ln)
```

Shrink σ toward league prior early season — same discipline as @concepts/dfs-stat-projection-engine.md efficiency shrinkage.

### Normal / lognormal / Poisson decision tree

```
Is stat non-negative integer with mean < 3?
  YES → Poisson (or ZIP if excess zeros)
  NO → Is stat strictly positive and right-skewed?
    YES → Lognormal (default) or Gamma
    NO → Normal truncated at 0 (large-volume counts)
```

**Pass TDs:** Poisson on expected TD rate × red-zone opportunities, not normal on 1.8 median.

**Reception yards:** lognormal core; receptions count as NB if line is low integer.

### Half-point lines and pushes

Most lounges use `.5` lines (no push). Verify:

- DNP / void rules → leg removed from slip vs graded loss
- Combo stat definitions (rushing only vs scramble included)

Document per platform on @entities/platforms/prizepicks.md and @entities/platforms/underdog-pickem.md.

### Calibration checklist

1. **Backtest hit rate** vs `P(over)` deciles — reliability diagram
2. **Brier score** on O/U vs closing line if sportsbook benchmark available
3. **Median trap audit:** flag props where `sign(median − line) ≠ sign(P(over) − 0.5)`

### CLI shape (target)

```text
prop-fair --player "Mahomes" --stat pass_yds --line 275.5
→ fair_p_over: 0.54, median: 268, family: lognormal, p_implied_breakeven: 0.577 (2-leg power ref)
```

## Snippets

> "Fair probability: P(stat > line) from projected distribution (not median vs line alone)." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md]

> "QB | Skew-normal + Poisson/NB pass TDs" [Source: @concepts/dfs-distribution-layer.md — adapt marginals per stat, not FP score]

> "Do not project raw TD rate" — use xTD / RZ opportunity [Source: @concepts/dfs-stat-projection-engine.md]
