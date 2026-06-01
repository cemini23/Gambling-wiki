---
title: Favorite-longshot bias (FLB)
type: concept
tags: [concept, behavioral, longshots, favorites, market-efficiency]
keywords: [flb, favorite-longshot-bias, longshot-tax, implied-probability]
related:
  - concepts/kelly-criterion-betting.md
  - concepts/vig-and-hold.md
  - concepts/sports-betting-fundamentals.md
  - concepts/prediction-markets-crossover.md
  - concepts/live-betting-match-integrity.md
  - concepts/parlay-and-correlated-bets.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-books-vs-pm-divergence.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/prediction-markets-crossover.md — FLB on Kalshi vs Polymarket
- @entities/platforms/kalshi.md — event contracts
- @entities/platforms/polymarket.md — CLOB event markets
- @osint-wiki/concepts/favorite-longshot-bias.md — Cemini PM trading monetization (Avellaneda-Stoikov, cross-venue)

## Raw Concept

Robust empirical finding: bettors overpay for longshots and underpay for favorites. General theory here; prediction-market bot strategies in `@osint-wiki`.

## Narrative

### Sportsbook manifestation

- Longshots (+500 and worse) often have **lower true win rate** than implied odds suggest
- Favorites (-200 and shorter) may offer slightly **better** realized value than implied (after vig)
- Prop markets and lottery-style parlays amplify FLB

### Behavioral drivers

Retail bettors overweight **payoff magnitude** vs expected value. Books shade lines toward popular longshots. Wider spreads on longshots make arbing capital-expensive.

### Prediction markets

On Kalshi/Polymarket, FLB appears as longshot contracts (5–15¢) trading above fair implied probability. Polymarket may show **weaker** FLB than Kalshi (different retail mix) — cross-venue gradient noted in `@osint-wiki/concepts/favorite-longshot-bias.md` [TENTATIVE].

### Exploitation (retail)

- Prefer **favorite-side** value and disciplined small longshot exposure only with independent +EV model
- Avoid lottery parlays unless correlated edge is modeled
- For bots: see `@osint-wiki` — favorite-side MM, longshot-fade modules

## Snippets

*(populate from academic sources on FLB — e.g. @osint-wiki/sources/nber-w10504-wolfers-zitzewitz-prediction-markets-2004.md for market-efficiency baseline)*
