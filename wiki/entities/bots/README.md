---
title: Gambling bots (entity namespace)
type: entity
tags: [meta, bots, namespace]
keywords: [bots, automation, stubs]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - meta/gambling-bot-ingest-rubric.md
  - entities/bots/wagerbrain.md
  - entities/bots/bovada-api-reference.md
  - entities/bots/bovada-hand-history-converter.md
  - entities/bots/poker-bot-tooling.md
  - entities/bots/stake-engine-client.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: core
created: 2026-05-31
updated: 2026-06-01
---

## Relations

- @concepts/gambling-wiki-scope.md — wiki vs @osint-wiki boundary
- @concepts/gambling-bot-architecture.md — fleet design hub

## Raw Concept

Placeholder namespace for **platform-specific gambling bot** entity pages (`entities/bots/<slug>.md`). Create stubs as design notes or FOSS evals land — not for production code (see `@osint-wiki`).

## Narrative

### Stubs (K92)

| Page | Lane | Notes |
|------|------|-------|
| @entities/bots/wagerbrain.md | Quoter / bankroll | Steal-from K92 eval |
| @entities/bots/bovada-api-reference.md | Sportsbook API | **NO-GO** Phase-0 (no license) |
| @entities/tools/rlcard.md | Poker RL sim | CONDITIONAL-GO research |
| @entities/bots/stake-engine-client.md | Stake client | **NO-GO** Phase-0 |
| @entities/bots/bovada-hand-history-converter.md | Analytics / CLV | Steal-from K92 |
| @entities/bots/poker-bot-tooling.md | Poker RL / equity | rlcard Adopt + engines |
| @entities/bots/stake-engine-client.md | Stake engine API | Steal-from; high ToS risk |

### Planned stubs (create on first ingest)

| Slug (draft) | Lane | Notes |
|--------------|------|-------|
| `sportsbook-ev-bot` | Sportsbooks | +EV scanner, line shop, CLV log |
| `pm-kalshi-divergence-bot` | PM | Sportsbook vs PM/Kalshi gaps |
| `dfs-slate-bot` | DFS | Import/optimize hooks, exposure caps |
| `master-orchestrator` | Cross-venue | Only if D4 resolves to unified control |

### Existing cross-wiki references (code on @osint-wiki)

Document **gambling angle** here; link implementation:

- `@osint-wiki/entities/tools/polybot.md`
- `@osint-wiki/entities/tools/harrier-pm-toolkits.md`
- `@osint-wiki/concepts/world-cup-advance-market-bot-v1.md`

## Snippets

*(none)*
