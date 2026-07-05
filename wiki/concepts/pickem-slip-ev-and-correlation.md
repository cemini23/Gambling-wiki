---
title: Pick'em slip EV and correlation
type: concept
tags: [concept, pickem, correlation, ev, parlay, kelly, k147, w-slip-ev, w-kelly]
keywords: [joint-probability, copula, same-game, slip-ranker, fractional-kelly, qb-wr]
related:
  - concepts/parlay-and-correlated-bets.md
  - concepts/kelly-criterion-betting.md
  - concepts/dfs-correlation-stacking.md
  - concepts/pickem-fair-probability.md
  - concepts/pickem-payout-and-breakeven.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/parlay-and-correlated-bets.md — sportsbook parlay math; pick'em lounges are the DFS analogue
- @concepts/kelly-criterion-betting.md — fractional Kelly on **whole slip**, not per leg
- @concepts/dfs-correlation-stacking.md — Gaussian copula + role priors for same-game stacks
- @concepts/pickem-fair-probability.md — per-leg `P(over)` inputs
- @concepts/pickem-payout-and-breakeven.md — payout multiplier `M` for EV denominator

## Raw Concept

Rank 2–6 leg pick'em slips by **expected value** using **joint hit probability** (not independent product) and size entries with **fractional Kelly on the entire slip**.

## Narrative

### Slip EV definition

For Power Play with multiplier `M` and stake normalized to $1:

```
EV = P_joint(win) × M − 1
```

`P_joint(win)` = probability **all legs hit** under the true joint model (correlation-aware).

For Flex Play:

```
EV = Σ_outcome P(outcome) × M_outcome − 1
```

where outcomes include partial-hit payouts from @concepts/pickem-payout-and-breakeven.md.

**Edge ranker** sorts candidate slips by `EV`, then filters by minimum edge and Kelly cap.

### Independent product (naive — wrong for stacks)

If legs were independent:

```
P_naive = ∏_i p_i
```

Same-game **QB pass yards over + WR receiving yards over** — legs are **positively correlated**. Independent product **underestimates** joint probability when both are overs in shootout scripts → **overstates edge** if used naively.

Use independent product only for **cross-game** legs with weak correlation, and only after explicit ρ ≈ 0 check.

### Correlation adjustment methods

| Method | When to use | Mechanism |
|--------|-------------|-----------|
| **Monte Carlo copula** | Same-game 2–4 legs, full tool | Draw correlated stat vectors; count sims where all legs hit [preferred] |
| **Gaussian copula on binary** | Fast ranker | Map each leg to latent `Z_i`; correlate via role matrix from @concepts/dfs-correlation-stacking.md |
| **Empirical conditional** | Backtest calibration | `P(WR over \| QB over)` from historical slates |
| **ρ bump heuristic** | Quick filter | `P_joint ≈ P_naive × (1 + κρ)` — [TENTATIVE] not for production sizing |

**Same-game QB + WR yards example:**

1. Build marginals for QB pass yds and WR rec yds from @concepts/pickem-fair-probability.md.
2. Assign correlation ρ from role table (QB–WR1 prior **+0.40 to +0.50** per @concepts/dfs-correlation-stacking.md).
3. Simulate `(Y_QB, Y_WR)` jointly — count fraction with `Y_QB > L_QB` AND `Y_WR > L_WR`.
4. Compare to `P_naive` — typical uplift **10–30%** on joint hit rate vs product when both overs [TENTATIVE — requires NFL walk-forward].

**Negative correlation** (e.g. QB over + opposing DST under): joint probability **below** product — independent model **understates** lounge edge requirement.

### Slip EV ranker logic

```text
FOR each candidate slip (2–6 legs):
  1. Load fair p_i per leg (fair-probability layer)
  2. Tag same-game clusters
  3. Compute P_joint via copula MC (N=10k default)
  4. Lookup M from payout table (power/flex, n legs)
  5. EV = P_joint * M - 1
  6. Kelly f* on slip (see below)
  7. Emit edges.csv: legs, P_joint, P_naive, EV, f_quarter_kelly
SORT BY EV DESC; apply min_EV and max_daily_exposure
```

**Filters:**

- Drop slips where `EV ≤ 0` after correlation (many retail stacks are -EV vs hold)
- Flag high `P_naive / P_joint` ratio — correlation sensitivity
- Separate pools for Goblin/Demon legs (effective vig from payout page)

### Fractional Kelly on whole slip

Treat the slip as **one binary bet**: win pays `b = M − 1`, lose pays `−1`.

```
f* = (p_joint × (b + 1) − 1) / b  =  (p_joint × M − 1) / (M − 1)
```

where `p_joint = P_joint(win)` for Power Play.

**Do not** apply Kelly per leg and sum — that double-counts edge and ignores correlation (@concepts/kelly-criterion-betting.md, @concepts/parlay-and-correlated-bets.md).

**Fractional Kelly defaults for pick'em:**

| Fraction | Rationale |
|----------|-----------|
| **¼ Kelly** | Default — model error on marginals + ρ + lounge void rules |
| **½ Kelly** | Only after 1+ season calibrated Brier/reliability |
| **Full Kelly** | Never — fat tails (injury, line voids, correlated blowouts) |

Cap with @concepts/bankroll-management.md unit rules and separate pick'em pool from DFS GPP / BBM.

**Flex Play Kelly:** use full `EV` and treat effective `b` as `EV / f_stake` at your modeled `p` — or Monte Carlo draw on all payout tiers; do not use Power `M` alone.

### Lounge vs sportsbook SGP

Sportsbooks embed correlation margin in SGP prices (@concepts/parlay-and-correlated-bets.md). Pick'em lounges use **fixed multipliers** — they do **not** reprice correlated stacks explicitly [TENTATIVE]. Potential +EV when `P_joint × M > 1` on mispriced same-game overs; -EV when stacking positive correlation without enough edge to clear hold.

### Open calibration tasks

- [ ] NFL walk-forward: joint vs naive hit rate by stack type
- [ ] Underdog Pick'em insurance features — adjust EV formula if product differs
- [ ] Live injury: joint `p` drift when leg voided mid-slate

## Snippets

> "Multiply **correlated** joint probability — not independent product." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md]

> "Treat parlay as **single bet** with combined `p` and `b`. Do not full-Kelly each leg separately." [Source: @concepts/parlay-and-correlated-bets.md]

> "QB + WR1 | Core positive prior; start around +0.40 to +0.50" [Source: @concepts/dfs-correlation-stacking.md]
