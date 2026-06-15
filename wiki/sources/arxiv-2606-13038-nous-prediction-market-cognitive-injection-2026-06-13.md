---
title: Nous — cognitive extraction/injection for prediction-market agents (arXiv 2606.13038)
type: source
tags: [source, arxiv, polymarket, llm-agents, cognitive-diversity, k114]
keywords: [2606.13038, nous, cognitive-monoculture, behavioral-extraction, prompt-injection, ensemble-forecasting]
related:
  - concepts/pm-agent-cognitive-monoculture.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-perspective-mismatch-trading.md
  - concepts/polymarket-v1-research-database.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/polymarket.md
  - sweeps/2026-06-13-daily.md
  - osint-wiki/concepts/market-informedness-market-making.md
  - osint-wiki/concepts/polymarket-retail-trading-discipline.md
maturity: validated
read_status: skimmed
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/pm-agent-cognitive-monoculture.md — synthesized concept (K114)
- @sweeps/2026-06-13-daily.md — overnight fetch provenance
- @concepts/prediction-markets-crossover.md — retail + agent PM lens
- @entities/platforms/polymarket.md — wallet-behavior extraction source
- @osint-wiki/concepts/market-informedness-market-making.md — ensemble / informedness stack (cross-wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Nous: An Attempt to Extract and Inject the Cognition Behind Prediction-Market Behavior |
| **Author** | Haowei Qian (Independent Researcher) |
| **arXiv** | [2606.13038](https://arxiv.org/abs/2606.13038) |
| **Repo** | [WillChienT/nous-paper](https://github.com/WillChienT/nous-paper) |
| **PDF** | `raw-sources/arxiv-2606.13038-nous-an-attempt-to-extract-and-inject-the-cognit.pdf` |
| **sha256** | `4bec5de21223a9ee…` |
| **Read status** | skimmed — abstract + intro + contribution claims (REFERENCE posture) |

## Narrative

### Thesis

As LLM agents proliferate on Polymarket, **epistemic monoculture** is the structural risk: frontier models' forecasting errors correlate at **r ≈ 0.77–0.78** across independently developed families. Nous asks whether **human cognitive diversity** can be recovered from on-chain behavior and transferred to LLM agents via an eight-dimension behavioral profile + prompt injection.

**Central finding — dissociation:** extraction partially works; **prompt-level injection does not** measurably improve ensemble diversity or Brier score.

### Extraction (partial success) [TENTATIVE — abstract only]

| Claim | Result |
|-------|--------|
| Temporal stability | 8 of 14 parameters stable (split-half ICC ≥ 0.5); contrarian score ICC ≈ 0.9 |
| Wallet identifiability | Top-1 retrieval 17–22% vs 1% random baseline (N=100 Polymarket wallets) |
| Profit linkage | 2 of 4 pre-specified dimensions correlate with future PnL OOS; **not robust** to behavioral-confound controls |

### Injection + usefulness (null) [TENTATIVE — abstract only]

- Structured prompt injection shows **no significant advantage** over length-matched filler on semantic embedding metrics
- Slight Jensen–Shannon diversity lift (+0.0035, p=0.010) but **no reduction in ensemble error correlation** and **no Brier improvement** (p ≈ 0.95)
- Bottleneck: structure-to-narrative translator emits **semantically near-uniform prompts** — spreading input profiles does not spread output diversity

### gambling-wiki posture: REFERENCE

| Owns here | Does not own |
|-----------|--------------|
| Retail framing — correlated AI forecasts ≠ diverse crowd | Prod bot injection / fine-tuning implementation |
| Warning against treating multi-agent PM stacks as independent | On-chain profile extraction pipeline |
| Link to copy-trading / monoculture risks | @osint-wiki agent harness or CeminiSuite deploy |

**Not a deployable edge.** Paper motivates **below-the-prompt** methods (PEFT, activation steering), not prompt personas for retail or bot operators.

### Routing

- PM retail discipline → `@osint-wiki/concepts/polymarket-retail-trading-discipline.md`
- Copy-trading risks → `@concepts/pm-copy-trading-retail-risks.md`
- Polymarket microstructure / dataset context → `@concepts/polymarket-v1-research-database.md`

## Snippets

> "When one agent misforecasts an event, agents trained on the same weights tend to reach the same wrong conclusion through the same structural failure." [Source: arxiv-2606.13038, §1.2 — paraphrase from abstract]

> "Prompt-level injection does not measurably transmit it … structured injection shows no significant advantage over a length-matched control on any model." [Source: arxiv-2606.13038, Abstract]

> "We therefore position Nous as measuring the cognitive-monoculture problem and the limits of a prompt-level remedy." [Source: arxiv-2606.13038, Abstract]

## Dead Ends

- **Hand-designed LLM personas as PM edge** — paper's null result on structured injection; near-uniform narrative prompts
- **Assuming multi-model ensemble = independent errors** — r ≈ 0.77 across frontier families
- **Deep-read / prod brief from skim** — full methodology needs PDF deep-read before any bot or research adoption
