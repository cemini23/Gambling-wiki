---
title: SWE-INTERACT — user-driven long-horizon coding agent benchmark (arXiv 2606.30573)
type: source
tags: [source, arxiv, agents, coding-agents, benchmark, k137, swe-interact]
keywords: [multi-turn, user-simulator, vague-requirements, long-horizon, scale-ai, interactive-swe]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md
  - sources/daily-digest-batch-k137-2026-07-03.md
  - sweeps/2026-07-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-03
updated: 2026-07-03
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.30573-2606-30573v1-swe-interact-reimagining-swe-benchm.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-03 — Apache-2.0 github.com/scaleapi/SWE-Interact (~14★); benchmark reference for multi-turn sandbox harness, not prod dependency
---

## Relations

- @sources/devfun-sandbox-researcher-guide-2026-06-26.md — Researcher Round multi-step MCP workflow
- @sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md — K137 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.30573](https://arxiv.org/abs/2606.30573) |
| **Title** | SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions |
| **Authors** | Raghavendra et al. (Scale AI) |
| **Repo** | [github.com/scaleapi/SWE-Interact](https://github.com/scaleapi/SWE-Interact) |
| **Phase-0** | **Apache-2.0** (gh api 2026-07-03); ~14★ |
| **Verdict** | **CONDITIONAL-GO** — strip-mine **interactive goal discovery** eval pattern for sandbox harness design |

## Narrative

Existing SWE benchmarks give **complete specs upfront** and score **autonomous** implementation. SWE-INTERACT instead uses a **user simulator** that starts with vague instructions, progressively reveals requirements, inspects workspace, and gives targeted feedback — mirroring real developer sessions.

| Finding | Implication |
|---------|-------------|
| **~50% → ~25% solve rate** | Strong single-turn SWE models halve on interactive tasks |
| **Ambiguity tolerance** | Best models (Opus 4.8, GPT 5.5) persevere; weak models give up early |
| **Failure modes** | Over-agentic coding, forgotten requirements, technical mistakes, rework loops |
| **Orthogonal axis** | Interactive refinement ≠ long-horizon autonomy alone |

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Researcher sandbox / HL loop** | **HIGH** — offline patch briefs are user-driven, evolving requirements; eval should test partial-spec recovery |
| **MCP bundle agents** | **MEDIUM** — pairs K136 training stability + K131 runtime hazards |
| **Pure-code `decide()`** | NO-GO — benchmark is for LLM coding agents |
| **Sportsbook / PM retail** | NO-GO |

Phase-0 **CONDITIONAL-GO**: read Apache-2.0 repo for user-sim task schema; **NO-GO** as Playground qualification metric substitute.

## Snippets

> "Strong performance on single-turn SWE tasks does not reliably transfer to multi-turn, user-driven workflows: the best-performing models solve roughly 50% of single-turn baseline tasks but only 25% of the corresponding SWE-INTERACT tasks." [Source: arxiv:2606.30573 Abstract]

> SWE-INTERACT "measures an orthogonal, real-world capability axis for frontier model development: interactive goal discovery and iterative refinement with a user in the loop." [Source: arxiv:2606.30573 Abstract]

## Dead Ends

- SWE-bench pass rate as HU sandbox leaderboard proxy
- Installing Scale SWE-INTERACT stack inside prod `decide()` path
- Treating vague user sim as substitute for deterministic regression spots (P5 still needs fixed gates)
