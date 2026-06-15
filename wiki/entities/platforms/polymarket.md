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
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - concepts/polymarket-v1-research-database.md
  - concepts/pm-live-belief-updating.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - concepts/pm-agent-cognitive-monoculture.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
maturity: draft
created: 2026-05-31
updated: 2026-06-15
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

### Fee reform timeline (K100, on-chain) [CONFIRMED]

Staggered **2026** taker-fee activation on CTF Exchange v1 (arXiv 2606.04217, on-chain fee-revenue panel):

| Category | Activation |
|----------|------------|
| Crypto | 2026-01 |
| Sports (selected leagues) | 2026-02 |
| Politics, News, Entertainment, others | 2026-03 |

Fee revenue was **zero before Jan 2026**. Post-activation descriptive pattern: lower wash-trading share, wider effective spreads, remaining taker flow more informed (noise-trader flight) `[TENTATIVE — DiD pre-trend caveats on some liquidity metrics]`. Source: `@sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md`.

### Research dataset (K100)

**Polymarket-v1** public archive — 1.2B trades, Nov 2022 – Apr 2026, ground-truth aggressor side. Use for offline FLB/calibration backtests; live wagering still uses Gamma/CLOB. See `@concepts/polymarket-v1-research-database.md` and [HuggingFace dataset](https://huggingface.co/datasets/TimeSeventeen/Polymarket-v1).

**Empirical FLB on v1 panel:** longshots (≤30¢) **overpriced**, favorites (≥40¢) **underpriced** — paper terms this **favorite-longshot reversal** (opposite sign from classic racetrack FLB). `@concepts/favorite-longshot-bias.md`.

### Research signals

- **StakeBench** — comment commitment vs sentiment (`@concepts/pm-commitment-grounded-language.md`)
- **PolyGnosis 2.0** — PM vs GDELT **perspective mismatch** (`@concepts/pm-perspective-mismatch-trading.md`)

### World Cup 2026

Sports menu includes **advance to knockout**, **group winner**, **match fixtures**, and **outright winner** — see `@concepts/world-cup-prediction-market-types.md` and `@entities/sports/world-cup-2026-betting.md`. Taker fees on sports scale with price; read settlement sources (FIFA + credible reporting) before sizing.

For copy-trading, LP farming, agent frameworks: `@osint-wiki/entities/platforms/polymarket.md`.

### Regulation and positioning (R3 WSJ, 2026-06-01) [TENTATIVE]

- **Offshore main platform** vs **CFTC-compliant US** rollout (2026, per WSJ).
- **Insider trading** — platform rule updates (stolen info, illegal tips, outcome influence); high-profile enforcement examples cited in video.
- **“Information market”** — company-reported **>90%** of audience engages without trading; median loss **<$10** for traders [TENTATIVE — company via WSJ].
- **Political/regulatory** — Don Jr. adviser role to Kalshi and Polymarket noted; CFTC asserts DCM authority vs state gambling framing.

Hub source: `@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`. Prod harness: `@osint-wiki/entities/tools/polygnosis.md`.

### US volume vs Kalshi (R2, 2026-06-02) [TENTATIVE]

Week ending **2026-05-24**: **~29%** of combined US PM notional on Polymarket (**$1.65B** vs Kalshi **$3.99B**); sports **$675.5M** vs Kalshi sports **$1.599B**. Politics category still PM-heavy; US sports onboarding (fiat, parlay parity) cited as gap vs Kalshi. `@sources/daily-digest-news-r1-r12-2026-06-02.md`.

## Snippets

> Fee activation: Crypto Jan 2026, Sports Feb 2026, Politics/News/Entertainment Mar 2026 — confirmed from on-chain fee revenue (zero pre-2026). [Source: arxiv-2606.04217 Table 7 via @sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md]

> Sports category median Gibbs spread 0.016 vs Crypto 0.007 on Standard Binary v1 panel — sports wider. [Source: same, Table 4]
