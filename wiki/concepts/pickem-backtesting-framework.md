---
title: Pick'em backtesting framework
type: concept
tags: [concept, pickem, props, nfl, backtest, w-backtest, k147]
keywords: [walk-forward, hit-rate, clv, correlation-calibration, prop-lines, leakage]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/dfs-backtesting-framework.md
  - concepts/pickem-fair-probability.md
  - concepts/pickem-slip-ev-and-correlation.md
  - concepts/pickem-data-sources.md
  - concepts/pickem-stat-type-mapping.md
  - concepts/line-shopping-and-clv.md
  - sources/research-nfl-historical-odds-2026-06-20.md
  - entities/tools/ceminidfs.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/dfs-backtesting-framework.md — sibling harness; shared leakage discipline
- @concepts/line-shopping-and-clv.md — CLV definition for book-benchmark props
- @concepts/pickem-data-sources.md — manual line log + historical actuals join

## Raw Concept

**Walk-forward, leakage-safe** evaluation of pick'em fair probabilities vs realized stats and (optionally) closing sportsbook prop lines. Minimum **one full NFL season** before trusting edge claims; explicit **same-game correlation calibration** for multi-leg slips.

## Narrative

### What we grade

| Layer | Unit | Primary metrics |
|-------|------|-----------------|
| Single prop | player × stat × slate × posted line | Hit rate, Brier, calibration, edge vs outcome |
| Fair model | week t holdout | MAE on stat vs actual (diagnostic) |
| Slip (2-leg) | same-game pairs | Joint hit rate vs independent product |
| Lounge vs book | matched prop (if any) | CLV vs closing book line |

Pick'em **payout** EV requires platform-specific breakeven — @concepts/pickem-payout-and-breakeven.md (when exists). This page covers **probability accuracy** first.

### Walk-forward design (inherit from DFS backtest)

```text
For each week t in season:
  train_features = all games strictly before week t
  snapshot_at    = fixed cutoff (e.g. Sunday T-90 ET)
  predict        = fair_p for each logged line with capture_time <= snapshot_at
  grade          = actual stat vs line (over hit / under hit / push)
```

| Rule | Requirement |
|------|-------------|
| Cutoff | Immutable timestamp per slate; no post-lock injury in features |
| Line timing | Use `captured_at` from manual log; discard lines logged after cutoff from **decision** backtest (may keep for CLV study separately) |
| Train/predict split | No future weeks in training |
| Versioning | Pin nflverse release + projection config per run |

### Hit rate vs CLV

| Metric | When to use | Definition |
|--------|-------------|------------|
| **Hit rate** | Lounge lines (primary) | % picks where side taken beats posted line vs actual |
| **Brier / log loss** | Model quality | `(fair_p - outcome)²` on over hit = 1 |
| **Calibration** | Systematic bias | Decile reliability: predicted 60% → ~60% hits |
| **CLV** | Book benchmark available | Your fair line vs **closing** book line movement — @concepts/line-shopping-and-clv.md |

**Do not conflate:** beating a soft posted pick'em line is not the same as +CLV vs Pinnacle/Circa prop close. Track both if Odds API historical props subscribed.

**Opening vs closing:** nflverse schedules = closing game lines only — @sources/research-nfl-historical-odds-2026-06-20.md. Prop CLV needs historical Odds API (10× credits) or manual close capture.

### Minimum sample

| Gate | Threshold | Rationale |
|------|-----------|-----------|
| Season coverage | **≥ 1 full NFL regular season** walk-forward | Variance on 17-week prop menu |
| Per stat type | ≥ 30 graded decisions before stat-specific claims | Thin tails on TD props |
| Edge bins | Report confidence intervals on top decile edge | Avoid overfit to lucky weeks |

**Verdict:** no "GO" on live slip sizing until season gate passes.

### Same-game correlation calibration

Pick'em slips multiply leg probabilities — mispriced correlation destroys EV (@concepts/pickem-slip-ev-and-correlation.md).

**Mandatory calibration test (example pair):**

| Pair | Null (independent) | Target |
|------|---------------------|--------|
| QB `pass_yds` over + WR1 `rec_yds` over | `P(A) × P(B)` | Empirical joint rate from sim or historical copula |
| QB over + opposing WR over | Lower correlation | Do not use same-game stack matrix |

**Procedure:**

1. Historical week holdout: list all same-game QB+WR pairs with both lines logged.
2. Compute `joint_hit_independent = fair_p_qb × fair_p_wr`.
3. Compute `joint_hit_actual` = both cleared line.
4. Report ratio `actual / independent` by week; tune copula or correlation matrix until error band stable.

**Pass criterion [TENTATIVE]:** independent product within ±5 pp of empirical joint on ≥ 100 pairs, or documented adjustment factor applied in slip EV ranker.

### Leakage checklist

- [ ] No post-cutoff injury status in projection features
- [ ] No actual stat from same week in training
- [ ] Posted line `captured_at` ≤ decision cutoff for decision backtest
- [ ] Demon/goblin lines graded with correct payout table, not standard
- [ ] Push/DNP rules applied per platform doc before hit label

### Harness outputs

| Artifact | Contents |
|----------|----------|
| `backtest_props_weekly.csv` | week, player, stat_id, line, fair_p, side, actual, hit, edge |
| `calibration_report.md` | decile table, Brier, by stat_id |
| `correlation_pairs.csv` | joint vs independent for configured pairs |
| `clv_vs_books.csv` | optional — if Odds API match |

### Relation to CeminiDFS backtest

| DFS backtest | Pick'em backtest |
|--------------|------------------|
| MAE / Spearman on FPPG | Hit rate / Brier on `P(stat > line)` |
| Ownership leakage | N/A |
| Contest sim ROI | Slip EV vs payout table (downstream) |
| Stokastic/Labs benchmark | PickLabs / manual book lines optional |

Reuse walk-forward **code patterns** from CeminiDFS repo; **separate** grader module in future K147 repo.

## Snippets

> "Minimum sample: 1 full NFL season walk-forward before trusting edge claims." [Source: K147 Phase-0 checklist]

> "Correlation calibration: same-game QB yards + WR yards joint hit rate." [Source: same]

> "Rank correlation tells you if you put the right players ahead of the wrong ones." [Source: @concepts/dfs-backtesting-framework.md — analog for prop ranking via fair_p ordering]
