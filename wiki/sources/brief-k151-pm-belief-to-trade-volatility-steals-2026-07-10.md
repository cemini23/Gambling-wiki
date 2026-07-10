---
title: Brief K151 — PM belief-to-trade + structural volatility steals
type: source
tags: [brief, k151, prediction-markets, agents, volatility, predict-raven]
keywords: [k151, belief-to-trade, predict-raven, structural-volatility, agentltl, cage-1, david-adoption]
related:
  - sources/daily-digest-batch-k151-2026-07-10.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md
  - sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md
  - sources/arxiv-2607.03510-cage-1-enterprise-agent-governance-2026-07-10.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/pm-structural-volatility.md
  - concepts/gambling-bot-architecture.md
  - entities/bots/predict-raven.md
  - sweeps/2026-07-10-daily.md
maturity: validated
read_status: deep-read
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- Operator copy: `briefs/2026-07-10_k151-pm-belief-to-trade-volatility-steal.md`

## Raw Concept

K151 operator steals for **David** — PM agent architecture + vol state variables + bot governance.

## Narrative

### PM retail / bots (adopt now)

1. **Belief-to-trade layer (03015 / predict-raven)** — separate **forecast module** (\(\mathbf{p}\)) from **trade policy** (size, timing, risk caps). Calibration leaderboard ≠ wallet PnL (reinforces K116).
2. **Structural volatility (08199)** — PM vol peaks near 50¢ and rises into resolution; sports jumpier than economics. Use deadline + price level as sizing/timing state (not equity GARCH).

### Fleet bot governance (research / spec)

3. **AgentLTL (02599)** — procedural trace specs gate tool calls; procedure is part of correctness for wager-submit bots.
4. **CAGE-1 (03510)** — authorization, replay, stop-before-impact checklist for any new automation lane.

### Skip

- **04178** DeFi reverse Kelly — not wagering Kelly sizing

## Dead Ends

- Autonomous Polymarket deploy without ToS audit
- Copying Raven equity curve as independent +EV proof
