---
title: MPPO (AMysteriousBeing)
type: entity
tags: [entity, tool, rl, opponent-modeling, blackjack, k153]
keywords: [mppo, mixed-ppo, style-preserving, learning-from-demonstration]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/games/blackjack.md
  - sources/arxiv-2506.16995-mppo-style-preserving-game-agents-2026-07-12.md
  - sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md
maturity: draft
created: 2026-07-12
updated: 2026-07-12
phase_0_verdict: CONDITIONAL-GO 2026-07-12 — no LICENSE; methods reference
---

## Relations

- @sources/arxiv-2506.16995-mppo-style-preserving-game-agents-2026-07-12.md — paper

## Raw Concept

- **Repo**: [github.com/AMysteriousBeing/MPPO](https://github.com/AMysteriousBeing/MPPO)
- **Paper**: arXiv [2506.16995](https://arxiv.org/abs/2506.16995)

## Narrative

**Mixed Proximal Policy Optimization** — blend online PPO with style-specific offline demonstrations (β≈0.05). Envs: Blackjack, Maze, MCR Mahjong. **D_policy** style-distance metric.

### Phase-0 audit (2026-07-12)

| Check | Result |
|-------|--------|
| License | **Missing** |
| Maturity | 1★; pushed 2025-07 |
| Fit | Arena stylized-opponent upgrade; blackjack RL reference |

**Verdict: CONDITIONAL-GO (steal-from)** — requirements for league opponent improvement without style collapse. No fork until LICENSE.

## Dead Ends

- pip-install as prod dependency without license
