---
title: Beyond Forecasting — belief-to-trade layer in prediction-market agents (arXiv 2607.03015)
type: source
tags: [source, arxiv, prediction-markets, agents, gambling-bot, k151, predict-raven]
keywords: [belief-to-trade, raven-agent, predict-raven, polymarket, calibration-gap, market-pulse]
related:
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - concepts/gambling-bot-architecture.md
  - entities/bots/predict-raven.md
  - entities/platforms/polymarket.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - sources/daily-digest-batch-k151-2026-07-10.md
  - sweeps/2026-07-10-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-10
updated: 2026-07-10
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.03015-beyond-forecasting-the-belief-to-trade-layer-in.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-10 — MIT github.com/Alchemist-X/predict-raven (~65★); PM agent reference, ToS + live-risk gates
---

## Relations

- @entities/bots/predict-raven.md — Phase-0 entity
- @sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.03015](https://arxiv.org/abs/2607.03015) |
| **Repo** | [github.com/Alchemist-X/predict-raven](https://github.com/Alchemist-X/predict-raven) |
| **Phase-0** | **MIT** (gh api 2026-07-10); ~65★ |
| **Verdict** | **CONDITIONAL-GO** — separates **forecast calibration** from **belief-to-trade** execution |

## Narrative

**Raven-Agent** / **predict-raven**: autonomous Polymarket trading agent. Paper argues benchmarks show a **gap between calibrated probability scores and trading PnL** — trading needs a distinct layer beyond forecasting.

| Component | Role |
|-----------|------|
| **Market Pulse** | Independent \(\mathbf{p}\) estimate + evidence gather vs market \(\mathbf{q}\) |
| **Belief-to-trade** | Size/timing policy combining edge + capital efficiency under risk controls |
| **Market-blind mode** | WC forecasting without reading prices (research / calibration lane) |

Pairs K116 proper betting (accuracy ≠ profit on CLOB) and K150 liquidity gates.

**Adoption for David:** architect PM bots as **forecast module + trade module**; do not equate Brier/calibration leaderboard with wallet PnL. Study predict-raven **risk controls** before any live deploy; ToS + inventory risk remain blockers.

## Snippets

> "Trading, however, requires more than forecasting. Moreover, recent benchmarks report a substantial gap between calibrated probability scores and the trading results." [Source: arxiv:2607.03015 Abstract]

## Dead Ends

- Copying public Raven equity curve as +EV proof without independent replay
- Autonomous Polymarket bot without geoblock/ToS audit
