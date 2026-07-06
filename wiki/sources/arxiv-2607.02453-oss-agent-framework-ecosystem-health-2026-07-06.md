---
title: Adoption and ecosystem health — open-source agent frameworks (arXiv 2607.02453)
type: source
tags: [source, arxiv, agents, foss-eval, k148, langchain, pydantic-ai]
keywords: [contributor-density, github-stars, retention, framework-selection, phase-0]
related:
  - concepts/gambling-bot-architecture.md
  - meta/gambling-bot-ingest-rubric.md
  - concepts/custom-agent-methodology.md
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.02453-2607-02453v1-adoption-and-ecosystem-health-a-lon.pdf
phase_0_verdict: REFERENCE 2026-07-06 — empirical Phase-0 metrics; no single Adopt repo
---

## Relations

- @meta/gambling-bot-ingest-rubric.md — Phase-0 checklist extension

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.02453](https://arxiv.org/abs/2607.02453) |
| **Verdict** | **REFERENCE** — **GitHub stars mislead**; use contributor density, cross-ecosystem engagement, 30/90-day retention |

## Narrative

Longitudinal study of 15 OSS agent frameworks (808k stars, 2022–2026):

| Finding | Phase-0 implication |
|---------|---------------------|
| AutoGPT star spike, **<9 contributors per 1k stars** | Hype ≠ depth |
| **Pydantic-AI** higher contributor density | Prefer for typed bot scaffolding eval |
| **LangChain** 82.5% cross-ecosystem contributors | Shared infra, not always best standalone |
| Retention cliff **first 30 days** | Pilot forks before fleet commit |

**Adoption for David:** gambling-bot Phase-0 — log **contributor density + 90d retention**, not star count alone (extends K90–K103 eval discipline).

## Dead Ends

- Star count as FOSS eval sole metric
- AutoGPT-style autonomous loops for prod wagering
