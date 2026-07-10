---
title: CAGE-1 — control, assurance, and governance evaluation for enterprise agents (arXiv 2607.03510)
type: source
tags: [source, arxiv, agents, governance, gambling-bot, k151]
keywords: [cage-1, enterprise-agents, governance-eval, replay, policy-authorization]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/custom-agent-methodology.md
  - sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md
  - sources/arxiv-2607.02389-steerability-constraints-coding-agents-2026-07-06.md
  - sources/arxiv-2607.02453-oss-agent-framework-ecosystem-health-2026-07-06.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - sources/daily-digest-batch-k151-2026-07-10.md
  - sweeps/2026-07-10-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-10
updated: 2026-07-10
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.03510-2607-03510v1-cage-1-control-assurance-and-govern.pdf
phase_0_verdict: REFERENCE 2026-07-10 — paper-only; enterprise agent governance eval framework
---

## Relations

- @sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md — trace-compliance layer

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.03510](https://arxiv.org/abs/2607.03510) |
| **Verdict** | **REFERENCE** — operational agent eval beyond answer accuracy |

## Narrative

**CAGE-1** reframes enterprise agent evaluation: who authorized an action, which policy applied, evidence currency, memory validity, permitted tool calls, **replay**, and **stop-before-impact**.

| Question | Gambling-bot mapping |
|----------|---------------------|
| Who authorized trade? | Human-in-loop + API key scope |
| Can decision replay? | Audit log for CLV / PM fills |
| Stop before impact? | Kill switch + daily loss cap |

Pairs K148 framework Phase-0 and K150 AReaL evolution control plane.

**Adoption for David:** add **CAGE-style checklist** to any new wagering automation lane spec (wiki requirements; prod on @osint-wiki).

## Snippets

> "They need to know who authorized an action, which policy applied … whether the decision can be replayed, and whether the agent can be stopped before it creates business impact." [Source: arxiv:2607.03510 Abstract]

## Dead Ends

- CAGE-1 enterprise RFP content as retail DFS workflow
- Governance framework without per-venue ToS mapping
