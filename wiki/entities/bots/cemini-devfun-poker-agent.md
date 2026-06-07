---
title: Cemini dev.fun poker agent (cemini_decide)
type: entity
tags: [entity, bot, poker, devfun, arena-pokerkit]
keywords: [cemini, devfun, cemini_decide, arena-pokerkit, decide-function]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/pokerskill.md
  - entities/bots/poker-bot-tooling.md
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/people/tom-dwan.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - entities/games/poker.md
maturity: draft
created: 2026-06-01
updated: 2026-06-07
adoption_status: ACTIVE-DEV
claim_status: VERIFIED 2026-06-01 — @cemini23
---

## Relations

- @entities/platforms/devfun-poker-arena.md — venue + Phase-0
- @entities/tools/pokerskill.md — skill-binding pattern (full PokerSkill repo not wired yet)
- @entities/people/tom-dwan.md — Pro Table Finale villain profile (`durrrr` exploit overlay — **not** Playground defaults)
- @concepts/poker-hl-analyst-loop.md — **HL analyst loop** (analyze → patch → preflight → deploy)
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — K95 consistent opponent modeling anchor
- Implementation: **private** — `llm-wiki-by-cemini` repo, path `agents/devfun-poker-arena/` (not in public Gambling-wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Name** | Cemini Wiki Poker |
| **Handle** | `cemini_wiki_poker` (official arena) |
| **Owner** | **@cemini23** — X verified [CONFIRMED] |
| **Quote** | "structured skills over swagger" |
| **Venue** | dev.fun Poker Arena — Playground + tournament path |
| **Base kit** | arena-pokerkit + custom `decide()` (private repo path) |

## Narrative

### Architecture (public summary)

Arena API drives a local agent loop: pending actions in, action + reasoning YAML out. Strategy is **pure code at runtime** (no per-hand LLM). Iteration uses the HL analyst loop at @concepts/poker-hl-analyst-loop.md — analyze live leaks, patch offline, gate with tests, deploy to prod.

Layer stack (generic): preflop chart hints → labeled scenario reasoning → postflop equity vs pot odds → clock safety. **Specific thresholds, guards, and opponent overlays are competition-private.**

### Pro Table Finale prep (future)

When dev.fun publishes finale format: optional named-villain exploit overlays per @entities/people/tom-dwan.md — **not** merged into Playground survival defaults.

### Next iterations

- Wire **PokerSkill** expert library when license verified on GitHub
- Optional research lane: runtime LLM eval — not prod path
- Heartbeat / lobby resilience on prod host

### Entry fee

Paid tournaments may return **402** until MON entry fee is settled on Monad via dev.fun UI; prod lobby retries join on interval.

### Runbook

Operator commands and deploy paths: **private** `README-CEMINI.md` on operator machine / prod host — not duplicated here during active events.

**Qualification:** Playground windows feed a KO path; monitor cutoff with local status scripts. Playground rebuy rules vary by season — confirm on arena before assuming recovery.

### Wallet (MON) — beta vs official [CONFIRMED 2026-06-03]

Beta and official are separate agent IDs and custodial wallets; MON does not sync. Fund official via MoonPay or external send. Agent IDs and addresses: **private creds only**. See `LESSONS.md` L4.

## Snippets

> "structured skills over swagger" — agent quote at registration [CONFIRMED 2026-06-01]

> Claim card: **AGENT CLAIMED** · owner @cemini23 · verified · entered 2026-06-01 [Source: arena.dev.fun claim UI]

## Dead Ends

- Deploying same bot against `@entities/platforms/pokerstars.md` or Bovada — arena-only scope
- Publishing live ranks, frequencies, or leak clusters in public wiki during active qualification — gives competitors a free HUD
