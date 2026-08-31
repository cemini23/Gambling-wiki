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
  - concepts/daily-edge-card.md
  - concepts/favorite-longshot-bias.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/pickem-payout-and-breakeven.md
  - entities/platforms/pinnacle.md
  - sources/kelly-1956-information-rate.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - concepts/pm-live-belief-updating.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - sources/arxiv-2604.17194-odds-conversion-emh-2026-08-31.md
maturity: validated
created: 2026-05-31
updated: 2026-08-31
---

## Relations

- @concepts/pickem-payout-and-breakeven.md — pick'em lounges embed hold via payout tables
- @concepts/sports-betting-fundamentals.md — how vig appears on tickets
- @concepts/sharp-vs-soft-books.md — sharp books run lower hold
- @concepts/line-shopping-and-clv.md — shopping reduces effective vig
- @concepts/daily-edge-card.md — de-vig reference before ranking Hard Rock
- @entities/platforms/pinnacle.md — low-hold reference book
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160 vig-removed 1X2 market baseline (~1.05 overround)
- @sources/arxiv-2604.17194-odds-conversion-emh-2026-08-31.md — OO-EPC vs multiplicative de-vig (soccer panel; do not swap NFL card yet)

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

### Devig sharp lines (model input)

To estimate fair probability from a two-way market, **remove juice** from sharp books (Pinnacle, Circa) before comparing soft-book offers. OddsJam tutorial walks devig on a Pinnacle spread (~16¢ juice example) [Source: 6HN-d9mC0DI]. Pair with `@entities/tools/odds-jam.md` and `@concepts/line-shopping-and-clv.md`.

### Reducing effective vig

1. **Line shopping** — best available price across books
2. **Reduced juice promos** (-105/-105) — temporary lower hold
3. **Sharp books** (Pinnacle) — lower hold, limits winners faster
4. **Exchange models** (Betfair) — commission on net winnings instead of embedded spread

## Snippets

> "You can devig the market … remove the juice from Pinnacle." [Source: 6HN-d9mC0DI via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

> "Lack of pricing knowledge … keep cranking the vig up where a 50/50 coin flip isn't plus 100." [Source: XZvXWVztJoY via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]
