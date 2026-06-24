---
title: Indian Rummy
type: entity
tags: [entity, game, casino, rummy, cards]
keywords: [indian-rummy, meld, sequence, set, deadwood, wildcard, gin-rummy-family]
related:
  - entities/games/poker.md
  - entities/bots/poker-bot-tooling.md
  - concepts/gambling-bot-architecture.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @entities/games/poker.md — sibling imperfect-info card game (different payoff structure)
- @sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md — first RL agent (IRumAI, CoG 2026)

## Raw Concept

Widely played meld-forming card game in South Asia. Wiki scope: **rules + bot-research lane** — not live online botting.

## Narrative

### Core mechanic

Players hold 13 cards and must partition them into **valid melds** (sequences and sets) before declaring. A per-deal **wildcard** rewrites card values. Unlike poker, a hand has **no graded strength** until fully melded — tactical play mixes meld construction, discard-pile blocking, and opponent inference.

### Bot / research posture

| Lane | Verdict |
|------|---------|
| **IRumAI (2606.21975)** | REFERENCE — PPO + meld-aware encoding; 53.9% vs search baseline |
| **Live bot automation** | **NO-GO** — real-money ToS / collusion (same as @entities/bots/poker-bot-tooling.md) |
| **NLHE arena transfer** | Analog only — fast policy inference, hidden-hand probing from public events |

## Snippets

> "Unlike poker, where any drawn hand has a well-defined rank on a continuous spectrum of strength, an Indian Rummy hand is functionally worthless until the player can partition all thirteen cards into valid sequences and sets." [Source: arxiv:2606.21975 §I]

## Dead Ends

- Martingale / pattern "systems" for rummy — not documented; house/player edge is skill + variance
- Porting IRumAI to dev.fun NLHE — different game tree
