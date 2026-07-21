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
  - concepts/polymarket-v1-research-database.md
  - sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/tools/wc2026-agents.md
maturity: validated
created: 2026-05-31
updated: 2026-07-21
---

## Relations

- @concepts/prediction-markets-crossover.md — FLB on Kalshi vs Polymarket
- @entities/platforms/kalshi.md — event contracts
- @entities/platforms/polymarket.md — CLOB event markets
- @osint-wiki/concepts/favorite-longshot-bias.md — Cemini PM trading monetization (Avellaneda-Stoikov, cross-venue)
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160: favorites over-performed WC2026; fade-market lost for LLMs

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

**Polymarket-v1 panel (K100, arXiv 2606.04217) [CONFIRMED]:** resolved v1 trades show **favorite-longshot reversal** — opposite sign from classic racetrack FLB:

| Price decile | Mean return (payout − price) |
|--------------|------------------------------|
| 0.00–0.30 | **Negative** (longshots overpriced) |
| 0.40–1.00 | **Positive** (favorites underpriced) |

Retail systematically **overestimates tail outcomes** on Polymarket. Paper: `@sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md`. Dataset: `@concepts/polymarket-v1-research-database.md`.

### Exploitation (retail)

- Prefer **favorite-side** value and disciplined small longshot exposure only with independent +EV model
- Avoid lottery parlays unless correlated edge is modeled
- For bots: see `@osint-wiki` — favorite-side MM, longshot-fade modules

### WC2026 LLM agents (K160) [CONFIRMED]

@sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md: across 104 WC2026 matches, favorites **over-performed** their opening price; a flat-favorite baseline beat four frontier LLM agents in absolute P&L, and **fading the market** was unprofitable for all four. Reinforces favorite-side discipline when LLM “value” narratives point at underdogs without a price-respecting model.

## Snippets

> Polymarket v1: "Low-probability tokens exhibit negative realized returns (systematic overpricing), while high-probability tokens exhibit positive returns (underpricing). This is the reverse of the classic longshot bias in betting markets." [Source: arxiv-2606.04217 via @sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md]

*(populate from academic sources on FLB — e.g. @osint-wiki/sources/nber-w10504-wolfers-zitzewitz-prediction-markets-2004.md for market-efficiency baseline)*
