---
title: When large trades are not news — liquidity tail risk and price discovery (arXiv 2607.01198)
type: source
tags: [source, arxiv, prediction-markets, microstructure, liquidity, k150]
keywords: [limit-order-book, heavy-tails, price-impact, adverse-selection, informed-trading]
related:
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md
  - sources/daily-digest-batch-k150-2026-07-09.md
  - sweeps/2026-07-09-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-09
updated: 2026-07-09
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.01198-2607-01198v1-when-large-trades-are-not-news-liqu.pdf
phase_0_verdict: REFERENCE 2026-07-09 — paper-only; LOB theory for PM CLOB liquidity-tail ambiguity
---

## Relations

- @sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md — Kyle λ empirical companion (K150 batch)
- @sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.01198](https://arxiv.org/abs/2607.01198) |
| **Verdict** | **REFERENCE** — large trades may reflect **liquidity shocks**, not private information |

## Narrative

Sequential competitive LOB with asymmetric information. Liquidity suppliers see **aggregate flow**, not trader motives. **Heavy-tailed** uninformed liquidity demand creates **liquidity-tail ambiguity**: same large imbalance can be news or shock.

| Finding | PM retail implication |
|---------|---------------------|
| Heavy tails flatten/concavify price impact | Large Kalshi/Polymarket prints ≠ informed edge |
| Slower learning from flow | Prices adjust gradually — patience on "obvious" moves |
| Liquidity tail as state variable | Size down when tail-risk / thin book regimes |

Pairs K135 settlement hazards + K116 proper-betting liquidity gate.

**Adoption for David:** do not infer **information edge** from block flow alone on PM CLOB; cross-check spread, depth, and oracle timing.

## Snippets

> "When is a large trade news, and when is it a liquidity shock?" [Source: arxiv:2607.01198 Abstract]

> "Liquidity tail risk as a state variable for market impact, spread resilience, and the informativeness of large trades." [Source: arxiv:2607.01198 Abstract]

## Dead Ends

- LOB heavy-tail model as live bot fill predictor without venue data
- "Large buy = bullish" heuristic on thin PM books
