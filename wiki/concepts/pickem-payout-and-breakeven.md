---
title: Pick'em payout and breakeven math
type: concept
tags: [concept, pickem, payout, breakeven, vig, power-play, flex-play, k147, w-payout]
keywords: [prizepicks, power-play, flex-play, demon, goblin, implied-probability, breakeven, hold]
related:
  - concepts/vig-and-hold.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/pickem-fair-probability.md
  - concepts/pickem-slip-ev-and-correlation.md
  - entities/platforms/prizepicks.md
  - entities/platforms/underdog-pickem.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/vig-and-hold.md — pick'em lounges embed margin via fixed payout tables instead of -110 sides
- @concepts/diy-nfl-pickem-props-tool-architecture.md — tool must reverse posted payouts before edge ranking
- @concepts/pickem-fair-probability.md — model `P(over)` numerator for edge vs implied breakeven
- @entities/platforms/prizepicks.md — canonical Power/Flex tables (verify in-app before entry)
- @entities/platforms/underdog-pickem.md — competitor payout structure [NEEDS VERIFICATION]

## Raw Concept

How DFS pick'em lounges (PrizePicks-style) convert **fixed slip multipliers** into **implied win probabilities** and **per-leg breakeven hit rates**. Demon/Goblin lines shift the effective vig without changing the payout table.

## Narrative

### Power Play vs Flex Play

| Mode | Win condition | Variance | Typical use |
|------|---------------|----------|-------------|
| **Power Play** | All legs correct | High — one miss = $0 | Max payout when model edge is strong |
| **Flex Play** | Partial credit for 1–2 misses (3+ legs) | Lower — insurance on a miss | When per-leg accuracy is good but not elite |

Payout multipliers are **posted before submit** — treat them as the lounge's "odds." Always confirm in-app; promos and special projections can differ [NEEDS VERIFICATION per slate].

### Implied probability formulas

**Power Play (all-or-nothing).** For `n` legs and posted multiplier `M` (profit multiple on stake; $1 → `$M` return):

```
P_implied(slip wins) = 1 / M
```

If legs are modeled as **independent with equal per-leg hit rate** `q`:

```
q_implied = M^(-1/n)
```

Breakeven per-leg hit rate (uncorrelated, equal legs): **`p* = M^(-1/n)`** — solve `p*^n × M = 1`.

**Flex Play (partial payouts).** Let `M_k` = multiplier when exactly `k` of `n` legs hit (only outcomes with `M_k > 0` matter). With independent equal leg probability `p`:

```
EV(p) = Σ_{k} C(n,k) · p^k · (1-p)^(n-k) · M_k  −  1
```

Breakeven `p*` solves `EV(p*) = 0` numerically. Closed form exists when only top two outcomes pay (e.g. 3-pick Flex: `3p² = 1` → `p* = 1/√3`).

**Edge vs lounge (single leg, binary).** When comparing model fair probability `p_fair` to a one-leg reference:

```
edge = p_fair − q_implied
```

For multi-leg slips, compare **joint** model probability to `1/M` (Power) or full `EV` under Flex schedule — see @concepts/pickem-slip-ev-and-correlation.md.

### PrizePicks standard tables [CONFIRMED — help center 2026-07-05]

**Power Play** — all correct required:

| Legs `n` | Multiplier `M` | Implied slip win `1/M` | Breakeven per leg `M^(-1/n)` |
|----------|----------------|------------------------|------------------------------|
| 2 | 3× | 33.33% | **57.74%** |
| 3 | 6× | 16.67% | **55.03%** |
| 4 | 10× | 10.00% | **56.23%** |
| 5 | 20× | 5.00% | **54.93%** |
| 6 | 37.5× | 2.67% | **51.62%** |

**Flex Play** — partial payouts (PrizePicks standard):

| `n` | All correct | 1 miss | 2 misses | Breakeven `p*` (i.i.d. legs) |
|-----|-------------|--------|----------|------------------------------|
| 3 | 3× | 1× (2/3) | — | **57.74%** |
| 4 | 6× | 1.5× (3/4) | — | **55.03%** |
| 5 | 10× | 2× (4/5) | 0.4× (3/5) | **~54.0%** [TENTATIVE — solve numerically] |
| 6 | 25× | 2× (5/6) | 0.4× (4/6) | **~53.6%** [TENTATIVE — solve numerically] |

Per-leg breakeven **decreases** on higher-leg Flex entries because partial payouts subsidize misses — but **slip-level** hit rate (all legs correct) remains low. Do not confuse `p*` with P(full sweep).

**Power vs Flex crossover.** Flex dominates Power when your true per-leg `p` is near breakeven but below the Power threshold; Power dominates when `p` is well above `p*` because full-sweep multipliers are higher. Crossover depends on `n` and payout row — simulate `EV(p)` for both modes at your calibrated `p`.

### Demon / Goblin effective vig

**Standard** lines are the lounge's baseline O/U. **Goblin** (easier) and **Demon** (harder) posts move the stat threshold while the **slip multiplier table stays fixed**.

Effective vig on altered lines:

1. Estimate fair `P(stat > goblin_line)` vs `P(stat > standard_line)` from @concepts/pickem-fair-probability.md.
2. Lounge still prices the leg as if it were a ~50/50 standard leg inside the same `M` table.
3. **Effective vig** ≈ `q_implied − p_fair_goblin` (Goblin: you accept worse true odds for the same payout tier) or `p_fair_demon − q_implied` (Demon: harder line, same multiplier).

Goblin-heavy slips look attractive on breakeven tables but **compress edge** unless the easier line still clears `p*` after distribution shift. Demon lines can be +EV when the tail probability is mispriced — but variance rises.

Multi-leg slips mixing Goblin + standard legs use **hidden per-leg pricing** on some platforms [TENTATIVE — PrizePicks does not display per-leg decimal odds on mixed slips]. Tool approach: assign each leg its own `q_implied` from the line type, then combine via correlation layer — not the equal-`q` shortcut.

### Hold analogy to sportsbooks

Sportsbook -110/-110 ≈ 4.76% overround per two-way market (@concepts/vig-and-hold.md). Pick'em hold is **embedded in the gap** between `p*` and 50%:

| 2-leg Power 3× | `p*` 57.74% | ≈ **15.5%** excess vs coin-flip per leg |
|----------------|-------------|------------------------------------------|

Higher hold than sharp spreads — DIY edge must exceed **model error + correlation error + hold**. This is why Phase-0 quantifies breakeven before repo work (@concepts/diy-nfl-pickem-props-tool-architecture.md).

### Tool implementation (K147)

```text
payout_implied(n, mode, M_or_flex_row) → q_implied, p_breakeven
edge_slip = EV_joint(fair_probs, correlation) − EV_implied(payout_table)
```

CLI should accept `--mode power|flex`, `--legs n`, and optional `--payout-json` override when app shows non-standard multipliers.

## Snippets

> "6-Pick Win = 37.5x the entry fee … 2-Pick Win = 3x" [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]

> "Flex Play: Lineups can still win even if one or two picks are incorrect" [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]

> Breakeven per leg for 2-pick Power at 3×: `p* = 3^(-1/2) ≈ 0.5774` — derived from `p*^2 × 3 = 1`.
