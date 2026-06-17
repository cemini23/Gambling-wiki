---
title: PM LLM forecast coherence projection (JCD)
type: concept
tags: [concept, polymarket, llm-forecasting, calibration, no-arbitrage]
keywords: [JCD, coherence-projection, marginal-polytope, Brier, LLM-forecasting, arbitrage-free]
related:
  - concepts/pm-agent-cognitive-monoculture.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - concepts/polymarket-v1-research-database.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/polymarket.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md — Kotawala JCD paper
- @concepts/pm-agent-cognitive-monoculture.md — Nous prompt injection dead-end; JCD is structural post-hoc repair
- @concepts/gambling-bot-architecture.md — PM bot forecast hygiene requirement

## Raw Concept

**Joint-Coherent Decoding (JCD):** post-hoc L2 projection of independently elicited LLM marginals onto the **coherent marginal polytope** so aggregated forecasts respect logical relations before trading or publication.

## Narrative

### Failure mode

Parallel LLM calls can yield **incoherent** probabilities across related events (mutually exclusive outcomes both >50%). Any bot or dashboard that averages raw marginals creates **internal arbitrage** — arbers exploit the gap vs coherent prices.

### When JCD applies

| Workflow | Joint elicitation OK? | JCD role |
|----------|----------------------|----------|
| Single controlled prompt batch | Often yes | Optional polish |
| Agentic loops, RAG, third-party APIs | Often **no** | **Required** hygiene layer |

### Reported gains [TENTATIVE — abstract]

- Mean Brier **−16.7%** on Paleka + Polymarket model panels after per-stream calibration + JCD
- Historical Polymarket backtest: **USD 79** vs **USD 43** raw PnL (2% fee assumption)

### Bot requirements (gambling-wiki)

1. **Coherence pass** on all marginals before order construction
2. **Do not** assume multi-model ensemble is independent (`@concepts/pm-agent-cognitive-monoculture.md`)
3. **Phase-0** anonymous code — CONDITIONAL until license verified; implementation → `@osint-wiki` brief

### vs Nous

| Nous | JCD |
|------|-----|
| Wallet persona → prompt injection | Marginal probabilities → polytope projection |
| Null on diversity | Structural no-arbitrage repair |
| REFERENCE | CONDITIONAL-GO on code artifact |

## Snippets

> "Post-hoc coherence projection repairs independently elicited LLM forecasts." [Source: OpenReview Tqos7VqQhH, TL;DR]

## Dead Ends

- **Publishing raw multi-LLM marginals** to PM without coherence check
- **Nous-style prompt personas** as substitute for logical coherence
