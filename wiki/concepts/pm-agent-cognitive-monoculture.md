---
title: PM agent cognitive monoculture
type: concept
tags: [concept, polymarket, llm-agents, ensemble, behavioral]
keywords: [cognitive-monoculture, prompt-injection, ensemble-correlation, nous, llm-forecasting]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-perspective-mismatch-trading.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/gambling-bot-architecture.md
  - concepts/polymarket-v1-research-database.md
  - entities/platforms/polymarket.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
  - concepts/pm-llm-coherence-projection.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - sweeps/2026-06-13-daily.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
  - sources/arxiv-2607.07760-adversarial-social-epistemology-llm-2026-07-12.md
  - sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md
  - osint-wiki/concepts/market-informedness-market-making.md
maturity: validated
created: 2026-06-13
updated: 2026-07-12
---

## Relations

- @sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md — Nous paper (arXiv 2606.13038)
- @concepts/pm-copy-trading-retail-risks.md — crowding + non-independent flow
- @concepts/gambling-bot-architecture.md — multi-agent PM bot design warnings

## Raw Concept

Structural risk as **LLM agents** proliferate on Polymarket: **correlated forecasting errors** across models and the **failure of prompt-level "persona injection"** to restore diversity.

## Narrative

### The monoculture problem [TENTATIVE — Nous abstract]

Independent frontier model families show forecast error correlation **r ≈ 0.77–0.78**. When one agent misforecasts, same-weight stacks tend to fail **the same way** — multi-agent ensembles are not independent draws.

**Retail implication:** products marketing "diverse AI agents" on PM may still be **one epistemic cluster** unless architectures differ below the prompt layer.

### Nous experiment (REFERENCE, not deployable edge)

| Stage | Finding |
|-------|---------|
| **Extraction** | 8/14 behavioral parameters stable on Polymarket wallets; top-1 wallet retrieval 17–22% vs 1% random; weak PnL linkage after confound controls |
| **Injection** | Structured prompt injection **≈ null** vs length-matched filler — no Brier gain (p ≈ 0.95); minimal Jensen–Shannon diversity lift without lower error correlation |
| **Bottleneck** | Structure-to-narrative translator emits **semantically uniform prompts** |

**Verdict:** hand-designed LLM personas and wallet-profile prompt stuffing are **Dead Ends** for PM edge. Paper points to **below-prompt** methods (PEFT, activation steering) — `@osint-wiki` implementation lane.

### Evidence-chain audit (K153 ASE) [TENTATIVE]

@sources/arxiv-2607.07760-adversarial-social-epistemology-llm-2026-07-12.md: beyond correlated errors — agents may **omit, under-specify, or distort** scaffolded testimony chains. PM forecast bots need **auditable source→inference→trade** logs, not headline trust. Pairs K151 predict-raven evidence gather.

### Bot design checklist

1. Do not assume **multi-model ensemble = uncorrelated errors**
2. Treat **prompt personas** as narrative, not diversity engineering
3. Prefer **heterogeneous signal sources** (books, exogenous media, on-chain with ground-truth side) over cloned LLM stacks — `@concepts/pm-perspective-mismatch-trading.md`
4. Wallet behavioral extraction may inform **research** but not retail copy products without validated OOS PnL

### gambling-wiki vs @osint-wiki

| Here | OSINT |
|------|-------|
| Retail + bot **requirements** (monoculture warning) | Agent harness, fine-tuning, prod ensemble |
| REFERENCE posture on Nous | Deep implementation if pursued |

## Snippets

> "We therefore position Nous as measuring the cognitive-monoculture problem and the limits of a prompt-level remedy." [Source: arxiv-2606.13038, Abstract]

> "Prompt-level injection does not measurably transmit it." [Source: arxiv-2606.13038 via @sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md]

## Dead Ends

- **Prompt-only wallet persona bots** — Nous null on structured injection
- **Assuming GPT + Claude + Gemini ensemble is independent** — r ≈ 0.77 cited in paper
- **Prod brief from skim-only** — full methodology needs deep-read before adoption
