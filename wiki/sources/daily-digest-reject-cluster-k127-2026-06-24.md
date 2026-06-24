---
title: Daily digest reject cluster K127 (2026-06-24)
type: source
tags: [source, arxiv, daily-digest, reject, k127]
keywords: [digest, reject, 2606.19264, 2606.20918, 2606.20995, 2606.24386]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-06-24-daily.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
  - sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/arxiv-2606.20960-equilibrium-internal-transfers-2026-06-24.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
maturity: validated
read_status: skimmed
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sweeps/2026-06-24-daily.md — overnight fetch (18 PDFs in inbox)
- @sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md — operator steals from ingested papers

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-24 |
| **Origin** | `research to be indexed/` — 18 PDFs |
| **Verdict** | **3 REFERENCE ingest / 15 reject** |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2606.21975 | IRumAI — Indian Rummy RL | No public repo | **REFERENCE** → dedicated source |
| 2606.23995 | EMAgnet — parameter EMA self-play | Riot proprietary | **REFERENCE** → dedicated source |
| 2606.20960 | Equilibrium with internal transfers (SETE) | Theoretical | **REFERENCE** → dedicated source |
| 2606.19264 | Large Language Gibbs | N/A | **Reject** — structured LLM MCMC; no wagering |
| 2606.20918 | Electricity demand forecasting (NE) | N/A | **Reject** — energy markets |
| 2606.20995 | ML reconfiguring science (1990–2025) | N/A | **Reject** — meta-science bibliometrics |
| 2606.21440 | Fusing backdoors + MILP | N/A | **Reject** — power systems / supply chain LTO |
| 2606.21631 | CuratorKIT LLM post-training | N/A | **Reject** — generic data curation |
| 2606.21931 | Three barriers to Kantian cooperation | N/A | **Reject** — public-goods economics |
| 2606.21967 | Moral geometry in Nash–Kantian games | N/A | **Reject** — Kantian scaling theory |
| 2606.22630 | MaxEnt RL for diffusion policies | N/A | **Reject** — robotics/control |
| 2606.23032 | IPO Finance Agent | N/A | **Reject** — SEC S-1 LLM eval |
| 2606.23070 | DeFi CL-AMM adverse selection | N/A | **Reject** — Uniswap v3 microstructure (→ @osint-wiki quant) |
| 2606.23414 | Similarities in multi-armed bandits | N/A | **Reject** — generic online learning |
| 2606.24019 | Square-root law market impact (AAPL) | N/A | **Reject** — equity microstructure |
| 2606.24037 | Morality Game platform | N/A | **Reject** — social-science cooperation lab |
| 2606.24160 | Introduction to causal RL | N/A | **Reject** — general ML survey |
| 2606.24386 | Line planning at scale | N/A | **Reject** — public transport planning |

**Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (18 PDFs; inbox cleared)

## Narrative

### Keyword false positives (digest lanes)

Several papers matched Exa queries via tangential terms:

- **2606.21440** — "knapsack" / optimization digest lane; actual topic is parametric MILP backdoors
- **2606.24386** — "line planning" matched sports-betting line-shopping noise; actual topic is railway line frequency
- **2606.23070** — digest `sports-betting-arxiv` cluster; DeFi AMM LVR, not sportsbook or Kalshi CLOB
- **2606.23414** — DFS roster lane MAB noise; tree-structured bandits without fantasy content

### Ingested siblings

- @sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md
- @sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
- @sources/arxiv-2606.20960-equilibrium-internal-transfers-2026-06-24.md

## Dead Ends

- CuratorKIT for poker hand-history curation — unrelated post-training tooling
- Morality Game as dev.fun replacement — different domain (cooperation experiments)
- Square-root impact law for sports bet sizing — equity order-flow study only
