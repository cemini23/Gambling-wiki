---
title: dev.fun Poker Arena — Phase-0 audit (2026-06-01)
type: source
tags: [source, web, devfun, poker, agent-arena, phase-0]
keywords: [devfun, monad, poker-arena, arena-pokerkit, phase-0, tom-dwan]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/tools/pokerskill.md
  - entities/tools/pokerskill.md
  - entities/bots/poker-bot-tooling.md
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - entities/people/tom-dwan.md
  - sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md
  - concepts/opponent-modeling-imperfect-info.md
maturity: validated
read_status: read
created: 2026-06-01
updated: 2026-06-04
---

## Relations

- @entities/platforms/devfun-poker-arena.md — entity verdict
- @concepts/opponent-modeling-imperfect-info.md — arena exploit / HUD lane
- @entities/bots/cemini-devfun-poker-agent.md — implementation stub
- @entities/people/tom-dwan.md — finale pro opponent (post Phase-0 ingest)

## Raw Concept

| Field | Value |
|-------|-------|
| **Method** | Web fetch docs.dev.fun, dev.fun landing, b-arena API probe, arena-pokerkit clone |
| **Retrieved** | 2026-06-01 |

## Narrative

### Operator question

Can the gambling-wiki / Cemini operator stack enter dev.fun’s **$50K Poker Arena** (opens **2026-06-03**)?

### Findings [CONFIRMED unless noted]

- **Format**: NLHE agent arena; API-driven `decide()`; 6-max; action clock.
- **Entry**: Register agent → `arena_sk_` key; optional **402 entry fee** per competition [TENTATIVE amount for main event].
- **Prizes**: X verification + external payout wallet required.
- **Starter path**: MIT `arena-pokerkit`; custom decide logic in private operator repo.
- **Prep competitions live on b-arena** (2026-06-01): Playground S1, Tournament S28, Poker Eval benchmark IDs in `.env.example`.

### Phase-0 verdict

**CONDITIONAL-GO** for arena participation. **NO-GO** for cross-deploy to consumer poker rooms.

## Snippets

> "An agent is an AI model running inside a coding tool that can read URLs, run commands, and follow written instructions." [Source: docs.dev.fun quickstart]

> "opens june 3, 2026" [Source: https://dev.fun/ FAQ]

## Dead Ends

- agentcasino.dev (memovai) — different product; not dev.fun arena
