---
title: "Game Arena — strategic LLM evaluation in competitive games (arXiv 2609.31473)"
type: source
tags: [source, arxiv, llm-eval, poker-arena, k177]
keywords: [kaggle-game-arena, head-to-head, benchmark-saturation, devfun]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/custom-agent-methodology.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/arxiv-2604.27865-kellybench-2026-08-31.md
  - sources/daily-digest-batch-k177-2026-09-28.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-09-28-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-28
updated: 2026-09-28
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2609.31473-game-arena-strategic-llm-evaluation-in-competiti.pdf
phase_0_verdict: REFERENCE 2026-09-28 — eval platform awareness; no weight download; no prod wire
wire_status: wont_wire
---

## Relations

- @concepts/gambling-bot-architecture.md — **eval harness** lane, not sportsbook execution
- @entities/platforms/devfun-poker-arena.md — federation poker bot uses **arena** eval, not KellyBench betting
- @sources/arxiv-2604.27865-kellybench-2026-08-31.md — betting agents lose; Game Arena is **game-theoretic** matchup eval

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2609.31473](https://arxiv.org/abs/2609.31473) |
| **Title** | Game Arena: Strategic LLM Evaluation in Competitive Environments |
| **Claim** | Kaggle **Game Arena** — head-to-head LLM matchups in structured games; difficulty scales as models improve vs static benchmarks |
| **Phase-0** | **REFERENCE** — read abstract; no install from paper PDF |
| **Wire** | `wont_wire` — cross-link dev.fun / OSINT arena only |

## Narrative

Useful for **W6 poker-arena** and planned gambling-bot **eval gates**: prefer dynamic adversarial or league-style eval over one-shot trivia when comparing agent policies. Does **not** justify NFL pick'em bots (see KellyBench). No CeminiSuite deploy from this ingest.

## Snippets

> "Different from static benchmarks, game arena enables models to play head-to-head matchups in structured environments where the gameplay strength naturally increases as models evolve." [Source: https://arxiv.org/abs/2609.31473 (retrieved 2026-09-28)]
