---
title: Sports betting fundamentals
type: concept
tags: [concept, sports-betting, spreads, moneylines, totals]
keywords: [spread, moneyline, total, props, american-odds, decimal-odds]
related:
  - concepts/vig-and-hold.md
  - concepts/bankroll-management.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/kelly-criterion-betting.md
  - concepts/favorite-longshot-bias.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-knockout-phase-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/line-shopping-and-clv.md — edge measurement
- @concepts/sharp-vs-soft-books.md — where to bet
- @entities/platforms/draftkings.md — major US book
- @entities/platforms/fanduel.md — major US book

## Raw Concept

Orientation page for mainstream US sports betting market types and odds formats.

## Narrative

### Market types

| Type | Question answered | Example |
|------|-------------------|---------|
| **Spread (handicap)** | Margin of victory | Chiefs -3.5 vs Bills |
| **Moneyline** | Straight win | Chiefs -150 / Bills +130 |
| **Total (over/under)** | Combined score | O/U 47.5 |
| **Props** | Player/team stat | Mahomes over 275.5 passing yards |
| **Futures** | Season/tournament | Super Bowl winner |
| **Live (in-play)** | Lines during game | Next score, live spread |

### Odds formats

- **American**: -110 favorite, +150 underdog
- **Decimal**: 1.91 = -110 equivalent
- **Implied probability**: from American negative `|odds|/(|odds|+100)`; positive `100/(odds+100)`

### Key disciplines

1. Bet **+EV lines**, not teams
2. Track **CLV** (closing line value) as skill proxy
3. Understand **push** rules (PK, half-points)
4. Know **void** rules (pitcher changes, postponements)

### Overlap with prediction markets

Some sporting outcomes trade on Kalshi/Polymarket as event contracts — see `@concepts/prediction-markets-crossover.md` for when to use books vs PM venues.

## Snippets

*(populate from ingested sports-betting primers)*
