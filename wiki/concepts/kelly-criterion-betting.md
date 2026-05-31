---
title: Kelly criterion for betting
type: concept
tags: [concept, kelly-criterion, position-sizing, math]
keywords: [kelly, fractional-kelly, edge, growth-rate, binary-bets]
related:
  - concepts/bankroll-management.md
  - concepts/favorite-longshot-bias.md
  - concepts/vig-and-hold.md
  - concepts/sports-betting-fundamentals.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/prediction-markets-crossover.md
  - sources/kelly-1956-information-rate.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/bankroll-management.md — Kelly informs unit size; bankroll rules cap Kelly
- @concepts/favorite-longshot-bias.md — mis-estimated `p` breaks full-Kelly
- @concepts/vig-and-hold.md — edge must exceed vig before Kelly applies
- @concepts/prediction-markets-crossover.md — PM bot implementations in @osint-wiki

## Raw Concept

General Kelly criterion for wagering — binary and decimal-odds forms. Polymarket-specific quarter-Kelly bot defaults live in `@osint-wiki/concepts/kelly-sizing-quarter.md`.

## Narrative

### Binary contract form

For win probability `p` and net odds `b` (profit per $1 staked on a win):

```
f* = (p · (b + 1) − 1) / b
```

Example: 55% true win probability at even money (`b = 1`):

```
f* = (0.55 × 2 − 1) / 1 = 0.10  → 10% of bankroll
```

### Decimal odds form

If decimal odds are `d`, then `b = d − 1`:

```
f* = (p · d − 1) / (d − 1)
```

### Fractional Kelly in practice

Full-Kelly assumes **exact** `p`. Real bettors use **fractional Kelly** (½, ¼, ⅛) because:

1. Model error on `p`
2. Correlated simultaneous bets (portfolio overshoot)
3. Fat tails (injury news, void rules, palpable error)

**Rule of thumb:** half-Kelly ≈ 75% of growth at ~50% volatility; quarter-Kelly ≈ 50% growth at ~25% volatility [TENTATIVE — standard fractional-Kelly literature].

For Cemini **prediction-market bots**, the house default is quarter-Kelly — see `@osint-wiki/concepts/kelly-sizing-quarter.md` and `@osint-wiki/sources/kelly-1956-information-rate.md`.

### When Kelly does not apply

- Parlays with unknown correlation structure — size as single combined bet with conservative `p`
- Promotional play-through with hidden vig — model effective edge first
- Casino -EV games — Kelly says **don't bet** (f* ≤ 0)

## Snippets

> Kelly, J. L. (1956). A New Interpretation of Information Rate — @sources/kelly-1956-information-rate.md

> "the gambler ignores the posted odds in placing his bets!" when odds are fair — Kelly 1956 p.922 [Source: @sources/kelly-1956-information-rate.md]
