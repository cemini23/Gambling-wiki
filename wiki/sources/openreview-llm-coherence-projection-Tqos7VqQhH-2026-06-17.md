---
title: Arbitrage-free LLM forecasts via coherence projection (OpenReview Tqos7VqQhH)
type: source
tags: [source, openreview, polymarket, llm-forecasting, calibration, k116]
keywords: [Tqos7VqQhH, JCD, coherence-projection, Brier, Polymarket, no-arbitrage, Forecast-ICML26]
related:
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/pm-llm-coherence-projection.md
  - meta/daily-research-digest-cadence.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
  - concepts/polymarket-v1-research-database.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/polymarket.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sweeps/2026-06-17-daily.md
  - osint-wiki/concepts/market-informedness-market-making.md
maturity: validated
read_status: skimmed
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @concepts/pm-llm-coherence-projection.md — JCD concept
- @concepts/pm-agent-cognitive-monoculture.md — complements Nous (below-prompt structural fix vs prompt personas)
- @sweeps/2026-06-17-daily.md — digest provenance
- @entities/platforms/polymarket.md — historical mid-price backtest panel

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Arbitrage-Free Forecasts from Language Models via Coherence Projection |
| **Author** | Anany Kotawala |
| **Venue** | Forecast @ ICML 2026 (Poster) |
| **OpenReview** | [Tqos7VqQhH](https://openreview.net/forum?id=Tqos7VqQhH) |
| **Code (anon)** | [anonymous.4open.science/r/jcd-forecasting-2810](https://anonymous.4open.science/r/jcd-forecasting-2810) |
| **PDF (local)** | `raw-sources/openreview-Tqos7VqQhH-arbitrage-free-forecasts-from-language-models-vi.pdf` |
| **PDF (egress)** | `cemini-egress-fi:/opt/cemini-bulk/research/gambling/openreview-Tqos7VqQhH-arbitrage-free-forecasts-from-language-models-vi.pdf` |
| **Read status** | skimmed — abstract + OpenReview metadata |

## Narrative

### Problem

Independently queried LLMs return **incoherent marginals** (e.g. 60% “Fed cuts” and 60% “Fed does not cut”) — any aggregator reading raw marginals is **arbitrage-exposed**. Joint elicitation fixes this when the forecaster controls the prompt; **agentic / retrieval / third-party API** workflows often cannot batch.

### Method — Joint-Coherent Decoding (JCD)

Post-hoc **L2 projection** of \(K\) sample marginals onto the **coherent marginal polytope** (inference-time, marginal-only).

### Results [TENTATIVE — abstract]

| Benchmark | Finding |
|-----------|---------|
| Paleka OrChecker | Brier-improvement saturation slope sign-flip (+1/m → −0.45) as theory predicts |
| 4-model Paleka + 6-model Polymarket panels | Per-stream calibration + JCD → **−16.7%** mean Brier |
| Polymarket historical mid-price backtest | JCD-L2 **USD 79** cumulative PnL vs **USD 43** raw; positive under **2% fee** assumption |

### gambling-wiki vs @osint-wiki

| Here | OSINT |
|------|-------|
| Bot **requirement**: enforce coherence before PM order submission | JCD implementation in prod forecast pipeline |
| Retail warning: incoherent LLM panels = free money for arbers | Code deploy when repo de-anonymizes |

### Phase-0 — code stub

| Repo | Verdict | Notes |
|------|---------|-------|
| `anonymous.4open.science/r/jcd-forecasting-2810` | **CONDITIONAL-GO** | Anonymous ICML artifact; license unknown until public release `[NEEDS VERIFICATION 2026-06-17]` |
| Prod gambling bot | **NO-GO** until license + egress mirror | See brief `briefs/2026-06-17_k117-gambling-jcd-coherence-osint-from-gambling.md` |

## Snippets

> "LLMs queried independently produce marginal probabilities that violate basic logical relations." [Source: OpenReview Tqos7VqQhH, Abstract]

> "JCD-L2 realizes USD 79 cumulative PnL versus USD 43 raw and remains positive under a 2% fee assumption." [Source: OpenReview Tqos7VqQhH, Abstract]

## Dead Ends

- **Raw multi-LLM marginals without coherence pass** — structural arb surface
- **Prompt-only persona diversity (Nous)** — orthogonal; JCD is post-hoc structural repair
