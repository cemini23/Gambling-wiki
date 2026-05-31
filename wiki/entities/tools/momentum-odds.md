---
title: MomentumOdds
type: entity
tags: [entity, tool, signal-feed, sportsbook, kalshi]
keywords: [momentum-odds, momentumods, sportsbook-signals, webhook]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/line-shopping-and-clv.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/prediction-markets-crossover.md — PM execution use case
- @osint-wiki/entities/tools/momentum-odds.md — Kalshi executor bot tutorial (K80)

## Raw Concept

Commercial sportsbook **signal feed** (60+ books) with webhook/API — used to trigger prediction-market executors. Detailed architecture in @osint-wiki.

## Narrative

Subscription terminal (**momentumods.com**) delivering correlated sportsbook signals. YouTube workflow (2026-05): API → local filter/risk → Kalshi orders.

**Retail angle:** understand signal latency, false positives, and that execution on PM still requires fee/CLV checks. **Bot angle:** `@osint-wiki/entities/tools/momentum-odds.md`.

Phase-0 before subscribe: pricing, TOS, track record.

## Snippets

*(see @osint-wiki for tutorial architecture)*
