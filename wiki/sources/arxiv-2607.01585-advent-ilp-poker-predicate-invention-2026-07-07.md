---
title: ADVENT — LLM predicate invention for poker-hand ILP (arXiv 2607.01585)
type: source
tags: [source, arxiv, poker, ilp, llm, interpretability, k149, advent]
keywords: [predicate-invention, prolog, poker-hand-ranking, relational-learning, knowledge-pool]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md
  - sources/daily-digest-batch-k149-2026-07-07.md
  - sweeps/2026-07-07-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-07
updated: 2026-07-07
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.01585-advent-llm-driven-automatic-predicate-invention.pdf
phase_0_verdict: REFERENCE 2026-07-07 — paper-only; poker-hand tasks disguised as Michalski Train ILP benchmark
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — interpretable feature / concept learning lane

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.01585](https://arxiv.org/abs/2607.01585) |
| **Verdict** | **REFERENCE** — LLM abduction + **Prolog verification** for predicate invention |

## Narrative

**ADVENT** automates **predicate invention** in ILP: LLM proposes named auxiliary predicates; Prolog execution verifies; knowledge pool enables cross-task reuse.

Benchmark: **nine poker-hand concepts** (pair, flush, straight, etc.) mapped to **Michalski Train** relational encoding to block LLM memorization of poker rules.

| Result | Value |
|--------|-------|
| LLM-only PI | **58%** success (ILP alone: 0%) |
| + formal verification | **80%** |
| Knowledge pool gain | up to **+31pp** |

| Lane | Fit |
|------|-----|
| **Offline analyst / rubric design** | **MEDIUM** — human-interpretable invented predicates for spot taxonomy |
| **NLHE strategy** | LOW — hand-ranking ILP ≠ betting policy |
| **Prod `decide()`** | NO-GO |

**Adoption for David:** steal **LLM→Prolog verify loop** pattern for offline **regression spot taxonomy** invention (name + testable predicate), not runtime policy.

## Snippets

> "Experiments on nine poker-hand concepts across seven LLMs show that LLM-driven PI achieves 58% success rate where ILP alone fails entirely, formal verification raises this to 80%." [Source: arxiv:2607.01585 Abstract]

## Dead Ends

- ADVENT hand-ranking rules as `cemini_decide()` features
- Predicate pool as Playground opponent classifier without NLHE validation
