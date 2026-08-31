---
title: PM whale conviction bias (size-weighted forecasts)
type: concept
tags: [concept, prediction-markets, kalshi, polymarket, microstructure, retail]
keywords: [whales, conviction, microstructure, kalshi, polymarket, forecasting]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/favorite-longshot-bias.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md
  - osint-wiki/sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md
  - sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md
maturity: draft
created: 2026-07-05
updated: 2026-08-31
---

## Relations

- @concepts/pm-copy-trading-retail-risks.md — whale-copy discipline
- @sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md — Klement summary of Daleep et al.
- @osint-wiki/sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md — OSINT provenance
- @sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md — sports large-trade compression is null; politics is not

## Raw Concept

Klement on Investing (2026-07-02) summarizes **Daleep et al. (2026)** microstructure study across **5,456** Kalshi + Polymarket markets: traders who bet **larger size (“whales”)** have **lower average edge** than smaller participants — undermining the premise that dollar-weighted PM prices aggregate “best” forecasts.

## Narrative

### Claim [TENTATIVE — single academic preprint via Klement]

PM prices overweight high-conviction / high-notional bettors. If whales are **worse** than the crowd, displayed probabilities are **biased** vs an unweighted opinion pool.

### Market buckets studied

- 15-minute crypto up/down
- “Mention” markets (earnings call wording)
- NBA game forecasts

Bias direction varies by market type (sometimes optimistic, sometimes pessimistic) — not a single FLB story.

### Retail implications

1. **Do not treat PM mid as “sharp consensus”** — size weighting may inject noise
2. **Whale-copy strategies** (`@concepts/pm-copy-trading-retail-risks.md`) — invert: large visible flow may be **negative** signal
3. **Cross-venue** — if Kalshi/Polymarket disagree, check **who holds OI** not just price
4. **Academic follow-up** — read primary paper before upgrading to `[CONFIRMED]`

## Snippets

> “People who bet more money in prediction markets (often called ‘whales’) aren’t more accurate than the average or smaller participants. They are, in truth, worse.” [TENTATIVE — Klement citing Daleep et al. 2026, @sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md]
