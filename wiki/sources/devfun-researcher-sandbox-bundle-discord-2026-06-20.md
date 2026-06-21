---
title: dev.fun Researcher sandbox — bundle submission Discord (2026-06-20)
type: source
tags: [source, discord, devfun, poker-arena, researcher-track, sandbox, bundle]
keywords: [bundle-submit, submission-interface, heuristic-bot, llm-byok, trueskill, heads-up]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - concepts/heads-up-arena-strategy.md
  - concepts/poker-axis-eval-literacy.md
  - osint-wiki/sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
maturity: validated
read_status: read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/platforms/devfun-poker-arena.md — sandbox ladder + submission types
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — TrueSkill HU timeline
- @sources/brief-k123-researcher-jun21-checklist-2026-06-20.md — Jun 21 operator checklist
- @concepts/heads-up-arena-strategy.md — HU fork doctrine
- @osint-wiki/sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md — OSINT cross-wiki stub + Cemini posture

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Researcher sandbox submission mechanics (Discord, dev team) |
| **Author** | dev.fun builders / dev team (operator relay) |
| **Type** | Discord message |
| **Retrieved** | 2026-06-20 |
| **Read status** | read |

## Narrative

### Submission model [CONFIRMED Discord 2026-06-20]

Builders submit **agent bundle files** to the sandbox. Supported approaches: **heuristic bot**, **LLM agent**, **fine-tuned model**, **small solver** — anything that conforms to the **submission interface**. dev.fun runs eval and publishes the **leaderboard**.

**Goal:** fair **heads-up** agent benchmark; identify the bot that faces **pros heads-up in the finale**.

### Closed beta [CONFIRMED]

Sandbox opening **soon** for researcher cohort to test first; devs will adjust quickly based on builder feedback. **Full submission details** promised in a follow-up message.

### LLM agents [CONFIRMED — dev recommendation]

| Aspect | Detail |
|--------|--------|
| BYOK | Builder API keys **encrypted**; injected only into **that submission's isolated sandbox** at runtime |
| Security | Per-submission isolation — keys not shared across builders |
| **Recommendation** | **Do not use LLM agents at this stage** for Poker Arena sandbox — dev testing shows **poor performance** and **very high cost** |

### Cemini posture (gambling-wiki framing)

| Lane | Posture |
|------|---------|
| **Researcher submit** | Pure-code `decide()` (`cemini_decide.py`) — aligns with dev recommendation |
| **LLM runtime** | Out of scope for sandbox until cost/quality improves |
| **Bundle packaging** | **WAIT** — interface spec pending; diff starter-kit bundle layout when published |
| **Eval target** | TrueSkill HU + trajectory/axis hygiene — not Playground chips |

## Snippets

> "Builders build their agents as bundle files submitted to sandbox, anything works, a heuristic bot, an llm agent, a fine tuned model, a small solver, etc. As long as it conforms to our submission interface, we'll run the eval and put up the leaderboard." [Source: dev.fun Discord 2026-06-20 (retrieved 2026-06-20)]

> "However based on our current testing, llm agents don't perform particularly well and the cost is very high. So for poker arena sandbox format, i don't really recommend using llm agents at this stage" [Source: dev.fun Discord 2026-06-20 (retrieved 2026-06-20)]

## Dead Ends

- Assuming `pokerkit run` on prod lobby is the only submit path — **bundle upload to sandbox eval** is the stated model; lobby remains intel / smoke only until interface docs land.
