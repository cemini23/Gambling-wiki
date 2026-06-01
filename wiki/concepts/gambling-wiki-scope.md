---
title: Gambling wiki scope and osint-wiki boundary
type: concept
tags: [concept, meta, federation, scope, bots]
keywords: [scope, boundary, osint-wiki, prediction-markets, routing, gambling-bot]
related:
  - concepts/bankroll-management.md
  - concepts/gambling-bot-architecture.md
  - concepts/prediction-markets-crossover.md
  - entities/bots/README.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - meta/cross-wiki-routing.md
  - meta/gambling-bot-ingest-rubric.md
  - meta/daily-research-digest-cadence.md
  - sources/brief-k93-federated-digest-2026-06-01.md
maturity: core
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/bots/README.md — bot entity namespace
- @concepts/prediction-markets-crossover.md — detailed split for Kalshi/Polymarket
- @concepts/bankroll-management.md — universal discipline layer
- @concepts/gambling-bot-architecture.md — planned bot fleet (this wiki)
- @meta/cross-wiki-routing.md — ingest routing checklist
- @meta/gambling-bot-ingest-rubric.md — bot-specific ingest

## Raw Concept

Meta page defining what belongs in **gambling-wiki** vs **@osint-wiki** (private Cemini quant/OSINT workspace).

## Narrative

### Primary home here

- Sportsbook strategy (NFL spreads, NBA props, soccer totals, live betting)
- Casino and poker (house edge, basic strategy, bankroll by stake, tournament ICM)
- DFS, daily fantasy, best ball, season-long fantasy
- Prediction markets **as wagering products**: contract rules, retail fees, behavioral biases, line shopping across PM venues
- Cross-cutting math: Kelly (general), vig, FLB (general), CLV, record-keeping
- **Gambling bot program (planned)** — architecture, per-platform requirements, FOSS evals, signal→action design, ToS/latency/failure modes (`@concepts/gambling-bot-architecture.md`)

### Primary home in @osint-wiki

- **CeminiSuite production deployment** — secrets, conductor, prod MCP, live orchestration
- Existing **World Cup bot** and quant backtests already wired to prod
- Deep **LP/maker** and market-making code paths when Cemini-specific
- Regulatory/compliance research for **institutional trading stack** (DCM preemption, CFTC) at operator depth
- Macro, equity, and OSINT research unrelated to wagering

### Split: gambling bots (both wikis, different angles)

| Angle | gambling-wiki | @osint-wiki |
|-------|---------------|-------------|
| *What* to automate on DK vs Kalshi | **Primary** | Cross-link |
| *How* to run on cemini-prod | Stub | **Primary** |
| FOSS repo Phase-0 for wagering | **Primary** eval narrative | Code mirror if adopted |
| polybot / Harrier strip-mine | Requirements + retail guardrails | Implementation |

### Routing heuristic at ingest

| Signal | Route |
|--------|--------|
| "How should I size this parlay?" | **gambling-wiki** |
| "What should the Kalshi bot do when books diverge 3¢?" | **gambling-wiki** (`@concepts/gambling-bot-architecture.md`) |
| "Deploy polybot module on cemini-prod" | **@osint-wiki** + stub here |
| "Kalshi fee schedule vs DraftKings vig" | **gambling-wiki** |
| "Cross-venue PM×Kalshi arb **bot code**" | wagering logic **here**; repo/prod **@osint-wiki** |

### Federation

Cross-links use `@gambling-wiki/...` and `@osint-wiki/...`. Bidirectional stubs when both wikis mention the same topic from different angles.

## Snippets

> Operator direction: eventual **master gambling bot or platform-specific bot fleet** — design and ingest live on gambling-wiki; Cemini prod stack stays on @osint-wiki. [Source: operator 2026-05-31]
