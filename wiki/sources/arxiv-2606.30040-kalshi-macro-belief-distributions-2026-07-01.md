---
title: Kalshi macro belief distributions from threshold contracts (arXiv 2606.30040)
type: source
tags: [source, arxiv, prediction-markets, kalshi, macro, k135]
keywords: [cpi, inflation, belief-distribution, threshold-contracts, tail-risk, kalshi-implied]
related:
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-live-belief-updating.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md
  - sources/daily-digest-batch-k135-2026-07-01.md
  - sweeps/2026-07-01-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-01
updated: 2026-07-01
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.30040-the-shape-of-macroeconomic-beliefs.pdf
phase_0_verdict: REFERENCE 2026-07-01 — Kalshi CPI panel methodology; no FOSS repo; retail macro-event literacy
---

## Relations

- @entities/platforms/kalshi.md — Kalshi CPI / core CPI threshold contracts
- @sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md — live belief updating on Kalshi
- @sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md — K135 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.30040](https://arxiv.org/abs/2606.30040) |
| **Title** | The Shape of Macroeconomic Beliefs |
| **Author** | Giovanni Angelini (University of Bologna) |
| **Phase-0** | N/A — empirical panel from Kalshi macro contracts |
| **Verdict** | **REFERENCE** — recover **full belief distributions** from adjacent threshold PM prices |

## Narrative

Uses **Kalshi CPI / core CPI release contracts** (adjacent inflation thresholds) to build high-frequency **market-implied distributions** from 30 days to 1 hour pre-release.

| Signal | Finding [TENTATIVE] |
|--------|---------------------|
| Market-implied **mean** | Forecast information, especially headline CPI |
| **Distributional** tail | Main incremental signal vs Reuters point consensus |
| Lagged positive surprise (+0.1pp) | Raises P(inflation > 0.3% monthly) by ~**4.7pp** |
| Upper-tail probabilities | Predict high-inflation realizations even when mean ≈ consensus |

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Kalshi macro retail** | **HIGH** — trade/threshold literacy; tail vs mean |
| **Sports / DFS** | NO-GO |
| **PM bot program** | Medium — distributional signals for macro-event lanes only |

Complements @sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md (live NBA updating; same author) with **full distribution** recovery from stacked binaries.

Phase-0 **REFERENCE** — methodology for reading Kalshi macro ladders; not a wagering bot dependency.

## Snippets

> "Observing prices across these thresholds before the release makes it possible to recover a discrete distribution over the upcoming macroeconomic outcome." [Source: arxiv:2606.30040 Abstract]

> "The main signal is distributional" — lagged surprises raise implied uncertainty and upper-tail inflation probabilities. [Source: arxiv:2606.30040 Abstract]

## Dead Ends

- Kalshi CPI tail trade as NFL DFS weather proxy
- Point-consensus-only sizing on macro Kalshi ladders
