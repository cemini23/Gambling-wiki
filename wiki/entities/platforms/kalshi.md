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
  - concepts/sharp-vs-soft-books.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/world-cup-prediction-market-types.md
  - entities/platforms/polymarket.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/momentum-odds.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
maturity: draft
created: 2026-05-31
updated: 2026-06-01
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

### Regulation and sports volume (R3 WSJ, 2026-06-01) [TENTATIVE]

- **CFTC DCM** — US event contracts regulated as **swaps** (CFTC, same agency as commodity futures per WSJ explainer).
- **Sports dominance** — WSJ cites **>70%** of Kalshi volume in sports; legal fight with **states** after sports expansion.
- **State gaming conflict** — Nevada and others push PMs toward **state gambling licenses**; research firm: **~69%** of volume from **19 states** without legal online sports betting.
- **“Not the house”** marketing vs **Kalshi Trading LLC** internal market maker — retail should assume **liquidity comes from designated MMs**, not peer-only pool.
- **Sharp migration** — pro bettor segment (WSJ: Frank Santolo) cites **higher limits** vs books that limit winners — aligns with `@concepts/sharp-vs-soft-books.md` PM column.

Hub source: `@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`.

### Fees vs sportsbooks (R2, 2026-06-01) [TENTATIVE]

Tech-Insider comparison: flagship Kalshi sports contracts **~0.5–1.5%** implied vig vs **~4.5%** standard -110/-110 book hold. Example: Chiefs ML priced **1.1¢** better effective on Kalshi vs DraftKings in May 2026 test. High-volume bettors: fee gap compounds ($50k/yr ≈ $2.25k vig at books vs $500–1k fees on Kalshi per article math). **Tax:** Kalshi gains may qualify for **Section 1256** 60/40 treatment vs ordinary gambling income on books [NEEDS VERIFICATION 2026-06-01].

## Snippets

> "Kalshi priced KC YES at $0.585… DraftKings -135… Kalshi paid the better effective price by 1.1 cents." [Source: @sources/daily-digest-news-r1-r12-2026-06-01.md, R2]
