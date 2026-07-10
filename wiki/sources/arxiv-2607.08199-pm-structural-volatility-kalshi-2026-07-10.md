---
title: Volatility in prediction markets — structural approach (arXiv 2607.08199)
type: source
tags: [source, arxiv, prediction-markets, kalshi, volatility, k151]
keywords: [wright-fisher, glosten-milgrom, binary-volatility, deadline-resolution, kalshi-panel]
related:
  - concepts/pm-structural-volatility.md
  - concepts/pm-live-belief-updating.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - sources/daily-digest-batch-k151-2026-07-10.md
  - sweeps/2026-07-10-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-10
updated: 2026-07-10
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.08199-volatility-in-prediction-markets-a-structural-ap.pdf
phase_0_verdict: REFERENCE 2026-07-10 — paper-only; Kalshi-panel structural vol model
---

## Relations

- @concepts/pm-structural-volatility.md — synthesized concept

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08199](https://arxiv.org/abs/2607.08199) |
| **Authors** | Xi, Moallemi, Pai, Wang |
| **Verdict** | **REFERENCE** — binary PM volatility ≠ ARCH/GARCH on equities |

## Narrative

Structural volatility model for **binary prediction markets** (Kalshi panel):

1. **Wright–Fisher deadline-resolution** — forced resolution of remaining uncertainty as expiry nears
2. **Glosten–Milgrom order-flow** — informed-trading vol via spreads/volume

| Finding | Retail / bot implication |
|---------|--------------------------|
| ARCH/GARCH dominated by structural specs | Don't port equity vol heuristics to PM |
| Vol highest near 50¢, rises near resolution | Widen size discipline near coin-flip + expiry |
| Sports = jumpier than economics | Category-specific timing risk (NFL in-play vs macro) |
| Category-specific fit doesn't beat pooled | One structural template transfers across Kalshi categories |

**Adoption for David:** use **deadline + price-level** as vol state variables for PM sizing/timing (pairs K150 liquidity gates).

## Snippets

> "Volatility is highest near fifty-fifty prices, rises near resolution, and varies across categories with the timing and discreteness of information arrival." [Source: arxiv:2607.08199 Abstract]

## Dead Ends

- Equity GARCH σ as Kalshi contract sizing without structural overlay
- Vol forecast alone as auto-bet trigger without edge + liquidity gate
