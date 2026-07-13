---
title: DeepSearch-World — self-distillation for verifiable search agents (arXiv 2607.07820)
type: source
tags: [source, arxiv, agents, prediction-markets, search, k154]
keywords: [deepsearch-world, self-distillation, verifiable-environment, evidence-gathering, web-agent]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/pm-agent-cognitive-monoculture.md
  - entities/bots/predict-raven.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/arxiv-2607.07760-adversarial-social-epistemology-llm-2026-07-12.md
  - sources/brief-k154-metagame-memory-search-steals-2026-07-13.md
  - sources/daily-digest-batch-k154-2026-07-13.md
  - sweeps/2026-07-13-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-13
updated: 2026-07-13
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.07820-2607-07820v1-deepsearch-world-self-distillation.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-13 — code/env promised release; verifiable search self-evolution (PM evidence lane)
---

## Relations

- @entities/bots/predict-raven.md — Market Pulse evidence gather comparator

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.07820](https://arxiv.org/abs/2607.07820) |
| **Verdict** | **CONDITIONAL-GO** — **DeepSearch-World** deterministic verifiable search env + **DeepSearch-Evolve** self-distillation |

## Narrative

420K multi-hop QA from entity random walks; reproducible search/page-read tools. Supports progress verification, grounded reflection, failure recovery.

**DeepSearch-Evolve:** trajectory gen → filter → mix → fine-tune loop without stronger teacher model. DeepSearch-World-9B: 31.2% BrowseComp, 61.5% GAIA, 93.4% HotpotQA.

| Lane | Fit |
|------|-----|
| **PM evidence bots** | **MEDIUM** — verifiable research env for self-improving forecast gather (pairs K151/K153 ASE) |
| **Poker arena** | LOW |
| **Sportsbook** | LOW |

**Adoption for David:** PM agent research lane should prefer **verifiable, reproducible** evidence environments over ad-hoc web scrape loops; watch for public code release before Phase-0 adopt.

## Snippets

> "Deterministic and verifiable environment with reproducible search and page-reading tools." [Source: arxiv:2607.07820 Abstract]

## Dead Ends

- BrowseComp score as PM trading edge proof
- Self-distilled web agent on live wagering without ToS audit
