---
title: Poker bot tooling (rlcard, poker_ai, pokerstove cluster)
type: entity
tags: [entity, bot, poker, research, steal-from, k92]
keywords: [rlcard, poker_ai, pokerstove, dickreuter-poker, pypokerengine, k92]
related:
  - concepts/poker-strategy-overview.md
  - entities/games/poker.md
  - entities/bots/README.md
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - entities/tools/pokerskill.md
  - entities/tools/rlcard.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-02
---

## Relations

- @concepts/poker-strategy-overview.md — human strategy context
- @entities/games/poker.md — game entity
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 eval cluster

## Raw Concept

K92 eval **poker engine / RL** cluster — **research and evaluation** lane for future poker bots, not live online poker botting (collusion/ToS dead end on real-money sites).

## Narrative

### Repos (K92 tiers)

| Repo | Tier | Notes |
|------|------|-------|
| datamllab/rlcard | **Adopt** (research) | RL environments for poker variants |
| dickreuter/Poker | Steal-from | Bot framework |
| andrewprock/pokerstove | Steal-from | Equity calculator |
| fedden/poker_ai | Steal-from | Deep CFR / research |
| ishikota/PyPokerEngine | Defer | Engine |

### Daily digest note (2026-06-01)

**Big 2** self-play RL (arxiv:2605.28863): PPO beats value methods in 4-player imperfect-info card game — **research sim only**, not online poker. Complements **rlcard** (poker variants) and **PokerSkill** (LLM + skills, `@entities/tools/pokerskill.md`).

**GIMARL** (arxiv:2605.31318, 2026-06-02 digest): **Generalized Intention Modeling** — mixture of task-specific opponent intent embeddings; one head maximizes MI with ego **returns**. [TENTATIVE] Useful design pattern for **sim bots** and Arena-style opponent modeling; benchmarks are general MARL, not NLHE. See `@sources/daily-digest-arxiv-batch-2026-06-02.md`.

### Gambling-bot program fit

- **Study / sim bots** — equity, ICM drills, bot-vs-bot sim
- **Not** for deploying against real-money online poker (`@sources/youtube-operator-batch-casino-2026-05-31.md` collusion awareness)

### Verdict

**REFERENCE / RESEARCH** — strip-mine math; **NO-GO** for live account automation without explicit operator scope + legal review.

## Snippets

> K92: rlcard Adopt for poker RL environments; poker_ai / pokerstove Steal-from. [Source: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
