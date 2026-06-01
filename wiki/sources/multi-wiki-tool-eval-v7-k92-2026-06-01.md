---
title: "Multi-wiki tool eval v7 K92 — wagering & casino-bot strip (90 URLs)"
type: source
tags: [source, tool-eval, gambling-bot, poker, bovada, stake, k92]
keywords: [wagerbrain, bovadaapi, poker, rlcard, casino dead-end, stake-engine]
related:
  - concepts/gambling-bot-architecture.md
  - entities/bots/wagerbrain.md
  - entities/bots/bovada-api-reference.md
  - entities/platforms/README.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md"
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — canonical OSINT eval page
- @entities/bots/wagerbrain.md — top steal-from (quoter)
- @concepts/gambling-bot-architecture.md — fleet + iGaming dead-end

## Raw Concept

Gambling-wiki slice of K92 Gemini eval (`GitHub Repo Evaluation for Cemini.docx`, 90 URLs). Operator updated gambling-wiki routing 2026-06-01 — **wagering automation** content saved here first.

## Narrative

### Keep on gambling-wiki

| Repo | Tier | Lane |
|------|------|------|
| sedemmler/WagerBrain | Steal-from | Quoter / bankroll automation — requirements for PM/sportsbook bot |
| ctrlaltdylan/bovadaAPI, jkol36/bovadaAPI | Reference-only | Sportsbook API scanner patterns (ToS risk) |
| matt57225/bovada-hand-history-converter | Steal-from | Hand-history ingest for CLV tracking |
| furic/stake-engine-client | Steal-from | Stake.com engine client — **ToS / jurisdiction** review before any use |
| dickreuter/Poker, andrewprock/pokerstove, fedden/poker_ai | Steal-from | Poker bot math / evaluators |
| datamllab/rlcard | Adopt | Poker RL environments (research) |
| ishikota/PyPokerEngine | Defer | Poker engine |

### iGaming casino UI — dead end

Reject cluster: slot clients (PixiJS), crypto-casino monoliths, Stake predictor scams, crash simulators. **Not** gambling-bot program targets — no API edge, ToS-toxic, no Cemini headless fit. See @concepts/gambling-bot-architecture.md § iGaming dead-end.

### Prod vs requirements split

Implementation of WagerBrain-like quoting on **cemini-prod** / world-cup-bot stays @osint-wiki. This wiki holds **what to automate** and Phase-0 verdicts.

## Snippets

> Gemini: WagerBrain — "Extends module 3 (quoter)." [Source: @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
