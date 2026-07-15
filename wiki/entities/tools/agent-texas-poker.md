---
title: AgentTexasPoker
type: entity
tags: [entity, tool, foss, poker, llm-agents, k156]
keywords: [agenttexaspoker, xuankunrong, vpip, pfr, nlhe-sim]
related:
  - sources/arxiv-2607.10251-risk-sensitive-llm-poker-2026-07-15.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/heads-up-arena-strategy.md
  - sources/brief-k156-risk-sensitive-llm-poker-steals-2026-07-15.md
  - sources/daily-digest-batch-k156-2026-07-15.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
phase_0_verdict: CONDITIONAL-GO
license_verified: NOASSERTION — no LICENSE file 2026-07-15
---

## Relations

- @sources/arxiv-2607.10251-risk-sensitive-llm-poker-2026-07-15.md — paper
- @concepts/poker-hl-analyst-loop.md — VPIP/PFR + pressure adaptation steals
- @concepts/opponent-modeling-imperfect-info.md — risk-spectrum opponent types

## Raw Concept

| Field | Value |
|-------|-------|
| **GitHub** | https://github.com/XuankunRong/AgentTexasPoker |
| **Paper** | arXiv 2607.10251 |
| **Local** | `raw-sources/foss-evals/AgentTexasPoker/` (~688KB; gitignored) |
| **Language** | Python 3.10+ |
| **Deps** | Multi-provider API keys (GPT/Claude/Gemini/DeepSeek/Qwen/Xiaomi) |

## Phase-0 Audit (2026-07-15)

| Check | Result |
|-------|--------|
| Pricing | Free code; API costs for sims |
| TOS | Provider API TOS; research sim only (prompt forbids gambling advice) |
| License | **NOASSERTION** — no LICENSE file |
| Size | ~688KB shallow clone — well under 500MB |
| Failure mode | API spend; JSON parse retries; not Arena-compatible engine |
| vs wiki | Complements RLCard / sandbox — **behavioural risk assay**, not GTO |

**Verdict: CONDITIONAL-GO** — steal VPIP/PFR risk-spectrum + plasticity methodology; do not redistribute until SPDX. HF dataset deferred (size unknown).

## Narrative

Simulator (`holdem/`, `run_simulation.py`) + configs for homogeneous, mixed, and short-stack regimes. Dashboard via `run_dashboard.py`. Outputs/plots not shipped in public repo.

## Dead Ends

- Drop-in replacement for `cemini_decide` / arena-pokerkit
- Nightly multi-frontier API burns without cost cap
