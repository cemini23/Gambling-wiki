---
title: Vig, juice, and hold
type: concept
tags: [concept, vig, juice, overround, sports-betting]
keywords: [vig, juice, hold, overround, breakeven, -110]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/sharp-vs-soft-books.md
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - concepts/line-shopping-and-clv.md
  - concepts/favorite-longshot-bias.md
  - concepts/parlay-and-correlated-bets.md
  - entities/platforms/pinnacle.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/sports-betting-fundamentals.md — how vig appears on tickets
- @concepts/sharp-vs-soft-books.md — sharp books run lower hold
- @concepts/line-shopping-and-clv.md — shopping reduces effective vig
- @entities/platforms/pinnacle.md — low-hold reference book

## Raw Concept

How sportsbooks embed margin (vig/juice) in prices, and what breakeven win rate bettors need.

## Narrative

### Standard -110/-110

On a two-sided market at **-110** each side:

- Implied probability per side: 110/(110+100) ≈ **52.38%**
- Sum: **104.76%** → **4.76% overround** (book hold ≈ 4.5%)

Breakeven win rate at -110: **52.38%** — you need >52.38% to be +EV before accounting for model error.

### Hold vs overround

- **Overround**: sum of implied probabilities − 100%
- **Hold**: book's expected margin given balanced action (often quoted as ~4.5% on -110/-110)

### Prediction market analog

Kalshi and Polymarket charge **fees** instead of traditional vig — effective hold depends on fee schedule + spread. Compare in `@concepts/prediction-markets-crossover.md`. Weather/sports PM fee caps differ by venue [NEEDS VERIFICATION 2026-05-31 — verify current fee pages before sizing].

### Reducing effective vig

1. **Line shopping** — best available price across books
2. **Reduced juice promos** (-105/-105) — temporary lower hold
3. **Sharp books** (Pinnacle) — lower hold, limits winners faster
4. **Exchange models** (Betfair) — commission on net winnings instead of embedded spread

## Snippets

*(populate from ingested sources)*
