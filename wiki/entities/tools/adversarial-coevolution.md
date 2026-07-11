---
title: adversarial-coevolution (Nikelroid)
type: entity
tags: [entity, tool, poker, rl, opponent-modeling, k152]
keywords: [adversarial-coevolution, expert-yardstick, gin-rummy, leduc, pettingzoo, trpo, curriculum]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/tools/rlcard.md
  - entities/bots/README.md
  - sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
  - sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md
maturity: draft
created: 2026-07-11
updated: 2026-07-11
phase_0_verdict: CONDITIONAL-GO 2026-07-11 — no LICENSE; methods + eval harness reference
---

## Relations

- @sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md — paper + ablation results
- @entities/tools/rlcard.md — Leduc env cross-check

## Raw Concept

- **Repo**: [github.com/Nikelroid/adversarial-coevolution](https://github.com/Nikelroid/adversarial-coevolution)
- **Paper**: arXiv [2607.06854](https://arxiv.org/abs/2607.06854)

## Narrative

Game-agnostic RL training pipeline (`coev/`) for PettingZoo AEC games. Ships **GoldStandardAgent** (Gin Rummy perfect meld solver) as **eval-only yardstick**, curriculum manager, NFSP/ISMCTS baselines, sweep harness, optional LLM serving stack.

### Phase-0 audit (2026-07-11)

| Check | Result |
|-------|--------|
| License | **Missing** — no `LICENSE` file (`gh api` SPDX null) |
| Maturity | 2★; pushed 2026-07-07 |
| Overlap | Arena HU eval methodology; Leduc tabular optimum check |
| Risk | Gin-specific reward code; LLM path too heavy for prod training |

**Verdict: CONDITIONAL-GO (steal-from)** — copy **expert-yardstick eval + curriculum/keep-best** requirements into arena regression spec; read ablation negatives (no DAgger/LLM-at-scale). **No pip/fork until LICENSE.**

## Snippets

> "The gold standard is used for scoring only — it never trains the agent." [Source: adversarial-coevolution README via @sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md]

## Dead Ends

- Gin Rummy gold agent as NLHE opponent
- Repo install without license clearance
