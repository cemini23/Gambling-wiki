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
  - entities/tools/rlcard.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
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

### Gambling-bot program fit

- **Study / sim bots** — equity, ICM drills, bot-vs-bot sim
- **Not** for deploying against real-money online poker (`@sources/youtube-operator-batch-casino-2026-05-31.md` collusion awareness)

### Verdict

**REFERENCE / RESEARCH** — strip-mine math; **NO-GO** for live account automation without explicit operator scope + legal review.

## Snippets

> K92: rlcard Adopt for poker RL environments; poker_ai / pokerstove Steal-from. [Source: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
