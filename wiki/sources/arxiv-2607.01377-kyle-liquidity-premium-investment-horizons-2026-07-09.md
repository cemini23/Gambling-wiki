---
title: Liquidity premium and investment horizons — Kyle λ from order flow (arXiv 2607.01377)
type: source
tags: [source, arxiv, microstructure, liquidity, k150]
keywords: [kyle-lambda, price-impact, order-flow, illiquidity-premium, adverse-selection]
related:
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md
  - sources/daily-digest-batch-k150-2026-07-09.md
  - sweeps/2026-07-09-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-09
updated: 2026-07-09
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.01377-2607-01377v1-liquidity-premium-and-investment-ho.pdf
phase_0_verdict: REFERENCE 2026-07-09 — paper-only; Kyle λ cross-sectional premium (equity CRSP; theory applies to CLOB PM)
---

## Relations

- @sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md — tail-risk theory layer

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.01377](https://arxiv.org/abs/2607.01377) |
| **Verdict** | **REFERENCE** — **Kyle λ** from signed order flow forecasts cross-sectional returns via adverse-selection illiquidity premium |

## Narrative

Estimates Kyle (1985) price-impact **λ** from daily equity order flow (CRSP 2020–2025). Signed flow predicts returns; high λ → illiquidity premium without classical risk compensation.

| Lane | Fit |
|------|-----|
| **PM CLOB** | **MEDIUM** — λ logic transfers: wide impact + low flow → entry/exit tax |
| **Equity** | Primary empirical domain — not sportsbook |
| **Sports betting** | LOW — different microstructure |

**Adoption for David:** on PM entries, treat **liquidity / impact** as separate gate from forecast accuracy (pairs K116 proper betting).

## Snippets

> "A stock with a high λ is one whose order flow is … more costly to trade against." [Source: arxiv:2607.01377 §1]

## Dead Ends

- CRSP λ estimates as Kalshi contract sizing inputs without venue calibration
- Illiquidity premium as auto +EV without proper-scoring edge
