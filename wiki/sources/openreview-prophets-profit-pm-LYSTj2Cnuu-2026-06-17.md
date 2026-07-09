---
title: When do prophets profit in prediction markets? (OpenReview LYSTj2Cnuu)
type: source
tags: [source, openreview, polymarket, proper-scoring, forecasting, k116]
keywords: [LYSTj2Cnuu, proper-scoring, CLOB, accuracy-profit, Forecast-ICML26, prophets]
related:
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/pm-agent-cognitive-monoculture.md
  - concepts/prediction-markets-crossover.md
  - meta/daily-research-digest-cadence.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-live-belief-updating.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - sweeps/2026-06-17-daily.md
  - sweeps/2026-07-09-daily.md
  - sources/daily-digest-batch-k150-2026-07-09.md
  - sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md
  - sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md
  - sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md
  - osint-wiki/concepts/market-informedness-market-making.md
maturity: validated
read_status: skimmed
created: 2026-06-17
updated: 2026-07-09
---

## Relations

- @concepts/pm-proper-scoring-clob-profitability.md — synthesized concept
- @sweeps/2026-06-17-daily.md — digest fetch provenance
- @entities/platforms/polymarket.md — CLOB retail context
- @sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md — complementary LLM forecast hygiene (JCD)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When do prophets profit in prediction markets? |
| **Authors** | Anri Gu, Nicole Kagan, Alec Sun, Jibang Wu, Haifeng Xu |
| **Venue** | Forecast @ ICML 2026 (Spotlight) |
| **OpenReview** | [LYSTj2Cnuu](https://openreview.net/forum?id=LYSTj2Cnuu) |
| **arXiv** | [2607.06166](https://arxiv.org/abs/2607.06166) — canonical supplement (K150; no duplicate page) |
| **PDF (local)** | `raw-sources/openreview-LYSTj2Cnuu-when-do-prophets-profit-in-prediction-markets-op.pdf` |
| **PDF (egress)** | `cemini-egress-fi:/opt/cemini-bulk/research/gambling/openreview-LYSTj2Cnuu-when-do-prophets-profit-in-prediction-markets-op.pdf` |
| **PDF (arXiv egress)** | `cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.06166-when-do-prophets-profit-in-prediction-markets-au.pdf` |
| **Keywords** | Prediction markets; forecasting; proper scoring rules; computational social science |
| **Read status** | skimmed — abstract + OpenReview metadata (REFERENCE for retail; live ROI claims unverified) |

## Narrative

### Problem

Classical theory links **forecast accuracy → trading profit** for **AMM** designs. Modern large PMs use **CLOBs** where informed traders can lose while naive heuristics profit — breaking the retail mental model that “being right = making money.”

### Contribution [TENTATIVE — abstract]

For any **strictly proper scoring rule** \(S\), authors construct a **proper betting strategy** (function of forecaster belief \(\mathbf{p}\) and market price \(\mathbf{q}\)) with positive expected profit when \(\mathbf{p}\) beats \(\mathbf{q}\) under \(S\) **and** liquidity is sufficient. Decomposition generalizes the AMM guarantee and explains profit **without** an accuracy edge.

### Empirical claims [NEEDS VERIFICATION — skim only]

| Claim | Detail |
|-------|--------|
| AI forecast panel | “Proper betting” only strategy reliably converting accuracy → profit across thousands of model forecasts |
| Personas | Systematic forecasting personas; optimal proper strategy varies |
| Live deployment | **+80.33% ROI**, Sharpe **3.35** over ~1 month |

**gambling-wiki posture:** requirements + retail framing. Do **not** treat live stats as deployable edge without deep-read + independent replication. Bot sizing / execution → `@osint-wiki`.

### Retail vs bot

| Here | OSINT |
|------|-------|
| When accuracy maps to CLOB PnL; heuristic-trap warning | Executor, liquidity gates, prod backtests |
| Proper-scoring checklist for PM research | CeminiSuite PM bot harness |

### Phase-0

| Target | Verdict |
|--------|---------|
| Paper / strategy definition | **REFERENCE** — academic; no FOSS repo linked on OpenReview |
| Live +80% ROI | **NEEDS VERIFICATION** — do not brief prod until replicated |
| Retail copy-heuristics on PM | **Dead End** — paper contrasts with proper scoring |

## Snippets

> "Classical theory establishes a clean equivalence between forecasting accuracy and trading profit, but only for the specific automated market maker (AMM) design." [Source: OpenReview LYSTj2Cnuu, Abstract]

> "Proper betting is the only strategy that reliably converts accuracy into profit." [Source: OpenReview LYSTj2Cnuu, Abstract — paraphrase]

## Dead Ends

- **Assuming CLOB PM edge = being calibrated** — uninformed heuristics can win without accuracy
- **Prod bot from abstract ROI** — live deployment stats not validated in this ingest
