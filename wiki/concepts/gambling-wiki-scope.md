---
title: Gambling wiki scope and osint-wiki boundary
type: concept
tags: [concept, meta, federation, scope]
keywords: [scope, boundary, osint-wiki, prediction-markets, routing]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/bankroll-management.md
  - meta/cross-wiki-routing.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
maturity: core
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/prediction-markets-crossover.md — detailed split for Kalshi/Polymarket
- @concepts/bankroll-management.md — universal discipline layer
- @meta/cross-wiki-routing.md — ingest routing checklist

## Raw Concept

Meta page defining what belongs in **gambling-wiki** vs **@osint-wiki** (private Cemini quant/OSINT workspace).

## Narrative

### Primary home here

- Sportsbook strategy (NFL spreads, NBA props, soccer totals, live betting)
- Casino and poker (house edge, basic strategy, bankroll by stake, tournament ICM)
- DFS, daily fantasy, best ball, season-long fantasy
- Prediction markets **as wagering products**: contract rules, retail fees, behavioral biases, line shopping across PM venues
- Cross-cutting math: Kelly (general), vig, FLB (general), CLV, record-keeping

### Primary home in @osint-wiki

- Polymarket/Kalshi **bot architecture**, LP farming, copy-trading pipelines
- CeminiSuite deployment, World Cup bot, quant backtests
- Regulatory/compliance research for **trading stack** (DCM preemption, CFTC)
- Macro, equity, and OSINT research unrelated to wagering strategy

### Routing heuristic at ingest

| Signal | Route |
|--------|--------|
| "How should I size this parlay?" | **gambling-wiki** |
| "How do I deploy the logit pricing engine?" | **@osint-wiki** |
| "Kalshi fee schedule vs DraftKings vig" | **gambling-wiki** (compare in `@concepts/vig-and-hold.md`) |
| "Cross-venue PM×Kalshi arb bot" | stub here → **@osint-wiki** primary |

### Federation

Cross-links use `@gambling-wiki/...` and `@osint-wiki/...`. Bidirectional stubs when both wikis mention the same topic from different angles.

## Snippets

*(none)*
