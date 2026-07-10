---
title: Daily digest batch K151 (2026-07-10)
type: source
tags: [source, arxiv, daily-digest, k151, prediction-markets, agents]
keywords: [digest, 2607.03015, 2607.08199, 2607.02599, 2607.03510, 2607.04178, predict-raven, volatility]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-07-10-daily.md
  - sources/daily-digest-batch-k150-2026-07-09.md
  - sources/daily-digest-reject-cluster-k151-2026-07-10.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md
  - sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md
  - sources/arxiv-2607.03510-cage-1-enterprise-agent-governance-2026-07-10.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - concepts/pm-structural-volatility.md
  - entities/bots/predict-raven.md
maturity: validated
read_status: skimmed
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- @sweeps/2026-07-10-daily.md — overnight fetch (5 PDFs)
- @sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-07-10 |
| **Origin** | `research to be indexed/` — 5 PDFs |
| **Verdict** | **3 REFERENCE + 1 CONDITIONAL-GO + 1 reject** |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2607.03015 | Belief-to-trade layer / Raven-Agent (PM) | MIT predict-raven ~65★ | **CONDITIONAL-GO** |
| 2607.08199 | PM structural volatility (Kalshi panel) | Paper-only | **REFERENCE** |
| 2607.02599 | AgentLTL trace verification | Paper-only | **REFERENCE** |
| 2607.03510 | CAGE-1 enterprise agent governance | Paper-only | **REFERENCE** |
| 2607.04178 | Reverse Kelly AMM (DeFi lending) | — | **Reject** |

**Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (5 PDFs; inbox cleared)

## Narrative

Strong PM agent batch: **calibration ≠ trading** (03015) + **structural vol** for sizing timing (08199). Agent governance pair (02599, 03510) for fleet bot specs. DeFi rkAMM reject (Kelly keyword false positive).

## Dead Ends

- DeFi reverse Kelly as sportsbook Kelly sizing
- Raven public PnL as verified +EV without replay
