---
title: Ensemble QSP — hierarchical memory for long-horizon multi-agent workflows (arXiv 2607.07666)
type: source
tags: [source, arxiv, agents, memory, gambling-bot, k154]
keywords: [ensemble-qsp, hierarchical-memory, bounded-context, multi-agent, pi-agent]
related:
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/gambling-bot-architecture.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/brief-k154-metagame-memory-search-steals-2026-07-13.md
  - sources/daily-digest-batch-k154-2026-07-13.md
  - sweeps/2026-07-13-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-13
updated: 2026-07-13
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.07666-2607-07666v1-a-hierarchical-memory-architecture.pdf
phase_0_verdict: REFERENCE 2026-07-13 — paper-only; three-layer bounded memory for multi-agent long workflows
---

## Relations

- @concepts/custom-agent-methodology.md — P3→P5 agent loop memory pattern

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.07666](https://arxiv.org/abs/2607.07666) |
| **Verdict** | **REFERENCE** — **Ensemble QSP** caps injected context via hierarchical memory eviction |

## Narrative

**Problem:** stateless LLMs degrade on multi-session research workflows.

**Ensemble QSP:** three-layer hierarchical memory + PI agent over five worker specialists. Mid-term project state **median 301 tokens, max 4,050** across 104 runs — evict completed work, cap per category.

Domain demo: PK/PD model selection (pharma). Architecture claimed **domain-agnostic** — new domain = new PI config.

| Lane | Fit |
|------|-----|
| **Poker HL loop** | **MEDIUM** — bounded epoch state across analyze/preflight/regression cycles |
| **Gambling-bot fleet** | LOW–MEDIUM — long-horizon ops logging |
| **Wagering math** | N/A |

**Adoption for David:** HL analyst epochs should use **structured bounded memory** (evict closed spots, cap open regressions) instead of unbounded chat context.

## Snippets

> "Keeps injected context bounded and constant in project duration … by capping each state category and evicting completed work." [Source: arxiv:2607.07666 Abstract]

## Dead Ends

- Pharma PK/PD PI config as sportsbook bot
- Unbounded session logs as HL loop memory
