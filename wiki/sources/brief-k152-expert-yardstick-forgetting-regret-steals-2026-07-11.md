---
title: Brief K152 — expert yardstick eval + forgetting-factor regret steals
type: source
tags: [brief, k152, poker, opponent-modeling, game-theory]
keywords: [k152, expert-yardstick, leduc, curriculum, forgetting-factor-regret, david-adoption]
related:
  - sources/daily-digest-batch-k152-2026-07-11.md
  - sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
  - sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md
  - entities/tools/adversarial-coevolution.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/tools/rlcard.md
  - sweeps/2026-07-11-daily.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
maturity: validated
read_status: deep-read
created: 2026-07-11
updated: 2026-08-12
cross-wiki-source: "briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steals.md"
---

## Relations

- Wiki mirror: `briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steals.md`
- OSINT arena: `agents/devfun-poker-arena/briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steal.md`

## Raw Concept

K152 operator steals for **David** — arena eval hygiene + online self-play metrics.

## Narrative

### Expert yardstick (06854 / adversarial-coevolution)

1. **Grade vs fixed strong opponent** — not self-play Elo or random crush rate.
2. **Steal helps:** TRPO/PPO trust region, opponent curriculum, warm start, keep-best checkpoint.
3. **Skip:** reward shaping, heavy embeddings, DAgger, live LLM training opponent.
4. **Leduc path:** validate methodology on RLCard/Leduc before NLHE claims.
5. **Blocker:** repo has **no LICENSE** — requirements only until cleared.

### Forgetting-factor regret (07078)

6. **Recency-weighted regret** when opponent pool / meta is non-stationary — uniform lifetime regret misleads.

## Dead Ends

- Self-play champion as sole promotion gate
- Fork adversarial-coevolution without LICENSE
