---
title: Polymarket
type: entity
tags: [entity, platform, prediction-markets, crypto, sports]
keywords: [polymarket, clob, usdc, sports-markets]
related:
  - concepts/favorite-longshot-bias.md
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - concepts/polymarket-weather-wagering-retail.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/pm-perspective-mismatch-trading.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/world-cup-prediction-market-types.md
  - entities/platforms/kalshi.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/momentum-odds.md
  - entities/tools/odds-jam.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
maturity: draft
created: 2026-05-31
updated: 2026-06-01
---

## Relations

- @concepts/pm-commitment-grounded-language.md — StakeBench commitment vs sentiment

- @entities/platforms/kalshi.md — cross-venue comparison
- @osint-wiki/entities/platforms/polymarket.md — bots, LP rewards, CeminiSuite

## Raw Concept

Crypto-based prediction market (CLOB). Consumer angle here; automation in @osint-wiki.

## Narrative

Polymarket uses **USDC on-chain** settlement with off-chain order book. Sports, politics, crypto, and macro markets. Retail: wallet setup, fees, withdrawal friction, FLB vs Kalshi.

### Sports fees (R1, Mar 2026) [TENTATIVE]

Probability-based **taker fee** on sports (per SI.com ingest): peak **~0.75%** effective at 50¢, tapering toward price extremes; **no taker fee on sells**; **maker fees** on filled limits. Category peaks differ (e.g. crypto up to ~1.8% per secondary summaries). US residents: **geo-blocked** post-CFTC settlement — legal US alternative often cited as Kalshi (`@entities/platforms/kalshi.md`).

### Research signals

- **StakeBench** — comment commitment vs sentiment (`@concepts/pm-commitment-grounded-language.md`)
- **PolyGnosis 2.0** — PM vs GDELT **perspective mismatch** (`@concepts/pm-perspective-mismatch-trading.md`)

### World Cup 2026

Sports menu includes **advance to knockout**, **group winner**, **match fixtures**, and **outright winner** — see `@concepts/world-cup-prediction-market-types.md` and `@entities/sports/world-cup-2026-betting.md`. Taker fees on sports scale with price; read settlement sources (FIFA + credible reporting) before sizing.

For copy-trading, LP farming, agent frameworks: `@osint-wiki/entities/platforms/polymarket.md`.

## Snippets

*(pending ingest)*
