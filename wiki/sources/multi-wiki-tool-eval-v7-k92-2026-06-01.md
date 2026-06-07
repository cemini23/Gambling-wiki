---
title: "Multi-wiki tool eval v7 K92 — wagering & casino-bot strip (90 URLs)"
type: source
tags: [source, tool-eval, gambling-bot, poker, bovada, stake, k92]
keywords: [wagerbrain, bovadaapi, poker, rlcard, casino dead-end, stake-engine, igaming]
related:
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - entities/bots/README.md
  - entities/bots/wagerbrain.md
  - entities/bots/bovada-api-reference.md
  - entities/bots/bovada-hand-history-converter.md
  - entities/bots/poker-bot-tooling.md
  - entities/bots/stake-engine-client.md
  - entities/tools/rlcard.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — canonical OSINT eval page
- @entities/bots/wagerbrain.md — top Steal-from (quoter)
- @concepts/gambling-bot-architecture.md — fleet + iGaming dead-end

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GitHub Repo Evaluation for Cemini (v5 prompt, casino/poker/stake cluster) |
| **Author** | Gemini Deep Research |
| **Type** | docx |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/GitHub Repo Evaluation for Cemini.docx` |
| **Retrieved** | 2026-06-01 |
| **URLs** | 90 |
| **Read status** | deep-read |

Gambling-wiki slice of K92. Heavy **iGaming UI / Stake clones / poker engines / Bovada API** — not a general PM bot sweep. **Wagering automation** requirements saved here; Cemini prod deploy on @osint-wiki.

## Narrative

### Tier summary (Gemini as reported) [TENTATIVE until `gh api`]

| Tier | Count | Gambling-wiki action |
|------|-------|---------------------|
| Adopt | 6 | **rlcard** → `@entities/bots/poker-bot-tooling.md` (research env) |
| Steal-from | 12 | WagerBrain, poker evaluators, bovada hand-history, stake-engine-client |
| Reference-only | 12 | bovadaAPI pair (scanner duplicate) |
| Defer | 1 | PyPokerEngine |
| Reject | ~59 | Slot/casino frontends, Stake predictors, crash simulators |

### Keep on gambling-wiki (entity pages)

| Repo | Tier | Lane | Page |
|------|------|------|------|
| sedemmler/WagerBrain | Steal-from | Quoter / bankroll | `@entities/bots/wagerbrain.md` |
| ctrlaltdylan/bovadaAPI, jkol36/bovadaAPI | Reference-only | Sportsbook API | `@entities/bots/bovada-api-reference.md` |
| matt57225/bovada-hand-history-converter | Steal-from | CLV / journal ingest | `@entities/bots/bovada-hand-history-converter.md` |
| furic/stake-engine-client | Steal-from | Stake.com engine | `@entities/bots/stake-engine-client.md` |
| dickreuter/Poker, andrewprock/pokerstove, fedden/poker_ai | Steal-from | Poker math | `@entities/bots/poker-bot-tooling.md` |
| datamllab/rlcard | Adopt | Poker RL research | `@entities/bots/poker-bot-tooling.md` |
| ishikota/PyPokerEngine | Defer | Poker engine | noted on poker-bot-tooling |

### iGaming casino UI — dead end

Reject cluster: PixiJS slot clients, crypto-casino monoliths, Stake "predictor" forks, crash simulators. **Not** gambling-bot program targets. See `@concepts/gambling-bot-architecture.md`.

**Exception:** `egorfedorov/Slot-Casino-Game-Developer-Skills-for-Stake` → **@ccc-wiki** (skills craft), not prod trading.

**OSINT-only steal:** `floatinghotpot/casino-server` WS→Redis — world-cup-bot fill handler; implementation on @osint-wiki.

### Prod vs requirements split

WagerBrain-like quoting on **cemini-prod** stays @osint-wiki. This wiki holds **what to automate** and Phase-0 verdicts.

### License posture

Many URLs reported **NO LICENSE FOUND** in Gemini eval — verify with `gh api` before any install `[NEEDS VERIFICATION 2026-06-01]`.

## Snippets

> "WagerBrain" — Steal-from; extends module 3 (quoter). [Source: GitHub Repo Evaluation for Cemini.docx via @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]

> "Duplicates module 1 (scanner)" — bovadaAPI pair. [Source: same]

## Dead Ends

- **~59 Reject URLs** — iGaming slot UI, Stake predictor scams, AGPL/GPL casino monoliths
- **Stake predictor / crash bots** — `[RETRACTED]` for +EV program
