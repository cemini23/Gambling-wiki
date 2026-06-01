---
title: Kalshi
type: entity
tags: [entity, platform, prediction-markets, regulated, sports]
keywords: [kalshi, event-contracts, cftc, dcm, sports-markets]
related:
  - concepts/favorite-longshot-bias.md
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/world-cup-prediction-market-types.md
  - entities/platforms/polymarket.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/momentum-odds.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/platforms/polymarket.md — primary cross-venue peer
- @concepts/prediction-markets-crossover.md — retail vs bot lens
- @osint-wiki/entities/platforms/kalshi.md — Cemini trading stack, regulation, bots

## Raw Concept

CFTC-regulated prediction market (DCM). **Consumer/strategy** entity here; execution infrastructure in @osint-wiki.

## Narrative

Kalshi lists **event contracts** (sports, economics, weather, politics). Retail considerations: fee schedule, contract specs, FLB on sports lines, geoblocking.

### World Cup 2026

**Group qualifiers** (advance), **group winner**, **match games**, and **outright** series — cross-walk to Polymarket in `@concepts/world-cup-prediction-market-types.md`. Kalshi resolves many sports via **ESPN/Fox/WSJ/Reuters** consensus — may differ from FIFA-only PM paths on edge cases [TENTATIVE]. Hub: `@entities/sports/world-cup-2026-betting.md`.

For bot architecture, LP, logit pricing, regulatory preemption: `@osint-wiki/entities/platforms/kalshi.md`.

## Snippets

*(pending ingest — fee pages, sports contract specs)*
