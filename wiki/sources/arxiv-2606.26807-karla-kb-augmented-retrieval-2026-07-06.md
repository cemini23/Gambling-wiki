---
title: KARLA — knowledge-base augmented retrieval for language models (arXiv 2606.26807)
type: source
tags: [source, arxiv, rag, agents, k148, karla]
keywords: [kb-trigger-tokens, factual-grounding, updatable-knowledge, tool-use]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.26807-2606-26807v1-karla-knowledge-base-augmented-retr.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-06 — code promised in supplementary; verify license on public release before Adopt
---

## Relations

- @concepts/custom-agent-methodology.md — RAG vs parametric facts pattern

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.26807](https://arxiv.org/abs/2606.26807) |
| **Verdict** | **CONDITIONAL-GO** — KB **trigger tokens** during generation; facts updatable via KB edits not retrain |

## Narrative

Trains LLM to emit special tokens that **query a structured KB** mid-generation — improves factual grounding, traceability, and allows **KB edits** to override stale parametric knowledge.

| Lane | Fit |
|------|-----|
| **Wiki librarian / analyst** | **MEDIUM** — platform TOS/fees/payout tables as KB not prompts |
| **K147 pick'em** | **MEDIUM** — Underdog payout profile as KB artifact |
| **Prod wagering bots** | NO-GO until license + latency validated |

**Adoption for David:** when CeminiPick or arena analyst needs **versioned platform rules**, prefer KB-trigger RAG over bloated system prompts — wait for public code + license check.

## Dead Ends

- KARLA as live odds fetch replacement
- Full wiki ingest into model weights
