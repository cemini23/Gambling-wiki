---
title: Agentic Time Machine — future-event forecasting eval (arXiv 2606.21013)
type: source
tags: [source, arxiv, prediction-markets, forecasting, k126, time-machine]
keywords: [futurex, polymarket, retrospective replay, planner-solver-aggregator, live leaderboard]
related:
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
  - sweeps/2026-06-23-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-23
updated: 2026-06-23
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.21013-2606.21013v1-agentic-time-machine-as-an-infrastr.pdf
phase_0_verdict: REFERENCE 2026-06-23 — PM/FutureX offline eval sandbox; not sportsbook execution
---

## Relations

- @entities/platforms/polymarket.md — evaluated under TM on FutureX-Past
- @sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md — operator steal (PM eval hygiene)
- @concepts/prediction-markets-crossover.md — retail PM agent evaluation angle

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.21013](https://arxiv.org/abs/2606.21013) |
| **Title** | Agentic Time Machine as an Infrastructure for Future-Event Forecasting |
| **Phase-0** | FutureX live leaderboard cited; no wagering prod repo |
| **Verdict** | **REFERENCE** — PM forecasting agent eval methodology |

## Narrative

Live forecasting evaluation (elections, monetary policy, **financial markets**, PM contracts) suffers a **speed vs fidelity** tradeoff: live benchmarks have slow feedback; retrospective replays often use frozen static databases.

**Agentic Time Machine (TM)** reconstructs approximate web state at a past cutoff by filtering post-cutoff content — a fast sandbox that correlates with live **FutureX** scores. Framework: planner → parallel solver agents → aggregator for multi-angle evidence fusion.

### Retail PM relevance

| Finding | Wagering takeaway |
|---------|-------------------|
| TM offline ↔ live FutureX correlation | Template for **backtesting PM bots** without waiting for settlement |
| Polymarket under TM | Evaluated on FutureX-Past; beats closed-book + tool baselines |
| Live leaderboard #1 (May 2026) | Research system — not retail copy-trading signal |

### Scope boundary

- **Primary home here:** consumer PM **evaluation hygiene** (fast replay vs live drift)
- **Execution / CeminiSuite bots:** @osint-wiki — do not route prod config from this page

## Snippets

> "Offline scores under TM correlate strongly with live FutureX scores, validating that TM offers a fast and reliable sandbox for forecasting-agent evaluation." [Source: arxiv:2606.21013 abstract]

> "On FutureX-Past and Polymarket evaluated under TM, our framework achieves the highest score among strong baselines." [Source: arxiv:2606.21013 abstract]

## Dead Ends

- **TM as Kalshi/Polymarket arb engine** — eval infrastructure, not order routing
- **Sportsbook CLV proxy** — different settlement and line mechanics than PM event contracts
