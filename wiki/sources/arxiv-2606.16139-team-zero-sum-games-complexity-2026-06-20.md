---
title: The Computational Complexity of Team Zero-Sum Games (arXiv 2606.16139)
type: source
tags: [source, arxiv, game-theory, poker, imperfect-info, k123]
keywords: [team zero-sum, PPAD, Nash equilibrium, Sandholm, polymatrix, min-max]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/gambling-bot-architecture.md
  - concepts/heads-up-arena-strategy.md
  - entities/bots/poker-bot-tooling.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/daily-digest-reject-cluster-k123-2026-06-20.md
  - sweeps/2026-06-20-daily.md
  - sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md
maturity: draft
read_status: skimmed
created: 2026-06-20
updated: 2026-08-12
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.16139-2606.16139v1-the-computational-complexity-of-tea.pdf
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — why Nash solvers don't trivially scale to multi-agent poker
- @concepts/heads-up-arena-strategy.md — HU researcher track is **2-player zero-sum** (tractable class)
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — exploit lane vs equilibrium computation
- @sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md — team-FP supervisor shelf (K166; ZSPTG lineage)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.16139](https://arxiv.org/abs/2606.16139) |
| **Authors** | Anagnostides, Panageas, **Sandholm**, Yan |
| **Date** | 2026-06-15 |
| **Phase-0** | Theory paper; no code dependency |
| **Verdict** | **REFERENCE** — game-theory literacy for bot program |

## Narrative

Settles complexity of **team zero-sum games**: multiple agents per side share a team objective but cannot perfectly coordinate. Computing Nash equilibria is **PPAD-complete** — as hard as general-sum games, despite global zero-sum structure. Hardness holds for 2-player teams, polymatrix games, inverse-polynomial precision.

### Relevance to gambling-wiki

| Setting | Implication |
|---------|-------------|
| **HU dev.fun researcher track** | Classic **2-player zero-sum** — minimax tractable; TrueSkill ranks pairwise outcomes |
| **6-max Playground** | Multi-agent **not** team zero-sum in formal sense — each seat independent; explains why CFR/NE tools don't drop in cleanly |
| **Exploit bots (cemini_decide)** | Practical path is **heuristic + HUD**, not team-Nash computation |
| **DeepCFR eval panel** | Reference opponents trained in simpler game classes |

Do **not** attempt team-Nash solvers for arena `decide()` — REFERENCE only for why Level 6 CFR stays research/offline.

## Snippets

> "Computing Nash equilibria is PPAD-complete... despite the global adversarial structure, team zero-sum games are as hard as general-sum games." [Source: arxiv:2606.16139 abstract]

## Dead Ends

- Using this paper to justify runtime Nash computation in Arena clock-limited `decide()`
- Mapping 6-max independent agents to team zero-sum without coordination model — wrong game class
