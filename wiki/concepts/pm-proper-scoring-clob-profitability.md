---
title: PM proper scoring and CLOB profitability
type: concept
tags: [concept, polymarket, kalshi, forecasting, proper-scoring, retail]
keywords: [proper-scoring, CLOB, accuracy-profit, prophets, AMM-vs-CLOB, liquidity]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-live-belief-updating.md
  - concepts/kelly-criterion-betting.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/pm-agent-cognitive-monoculture.md
  - concepts/pm-llm-coherence-projection.md
  - concepts/kelly-criterion-betting.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md
  - sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md
  - sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - concepts/pm-structural-volatility.md
  - sweeps/2026-06-17-daily.md
  - sweeps/2026-07-09-daily.md
  - sweeps/2026-07-10-daily.md
maturity: validated
created: 2026-06-17
updated: 2026-07-10
---

## Relations

- @sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md — Gu et al. (Forecast @ ICML 2026 Spotlight)
- @concepts/pm-copy-trading-retail-risks.md — copying wallets ≠ proper scoring
- @entities/platforms/polymarket.md — CLOB microstructure

## Raw Concept

**Accuracy–profit link** on modern **CLOB** prediction markets: when forecast edge converts to expected PnL, and when naive heuristics win without being “right.”

## Narrative

### AMM vs CLOB mental model

| Design | Classical accuracy → profit |
|--------|----------------------------|
| **AMM** (legacy PM theory) | Clean equivalence under proper scoring |
| **CLOB** (Polymarket, Kalshi scale) | Informed traders can lose; uninformed heuristics can profit |

Retail mistake: treating PM like a **calibration contest** instead of a **liquidity + scoring-rule** game.

### Proper betting (Gu et al.) [TENTATIVE — skim]

For strictly proper scoring rule \(S\), a **proper betting strategy** \(\pi(\mathbf{p}, \mathbf{q})\) earns positive expected profit when:

1. Forecaster belief \(\mathbf{p}\) **beats** market price \(\mathbf{q}\) under \(S\), and  
2. Market has **sufficient liquidity** for the strategy’s footprint.

Authors claim this is the **only** strategy class in their AI forecast panel that reliably maps accuracy → profit; live deployment stats cited (+80% ROI, Sharpe 3.35) need independent verification before prod use.

**K151 addendum:** Raven-Agent / predict-raven formalizes a **belief-to-trade layer** — calibrated forecasts can still lose money without a separate trade policy (@sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md).

### Retail checklist

1. **Liquidity gate** — edge on paper ≠ fill at mid
2. **Scoring alignment** — know which market resolution rule / score applies
3. **Heuristic trap** — momentum / copy without \(\mathbf{p}\) vs \(\mathbf{q}\) decomposition
4. **Large-trade ambiguity** — heavy-tailed liquidity shocks can mimic informed flow; do not treat block prints as edge without depth/spread context [Source: @sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md]
5. **Illiquidity premium (Kyle λ)** — high price-impact regimes tax entry/exit via adverse selection; widen edge threshold or size down [Source: @sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md]
6. **Bot lane** — proper-scoring module before size (`@concepts/gambling-bot-architecture.md`); execution on `@osint-wiki`

### Cross-links

- Coherence of LLM marginals before aggregation → `@concepts/pm-llm-coherence-projection.md`
- Live underreaction → `@concepts/pm-live-belief-updating.md`

## Snippets

> "Informed forecasters routinely lose money while uninformed strategies can profit on simple heuristics." [Source: OpenReview LYSTj2Cnuu via @sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md]

## Dead Ends

- **“I’m calibrated so I must be profitable”** on CLOB without proper-scoring + liquidity analysis
- **Whale copy as proper betting** — unrelated mechanism
