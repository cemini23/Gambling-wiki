---
title: DraftKings
type: entity
tags: [entity, platform, sportsbook, dfs, us-legal]
keywords: [draftkings, dk, sportsbook, dfs, best-ball]
related:
  - concepts/best-ball-strategy.md
  - concepts/dfs-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/sharp-vs-soft-books.md
  - concepts/sports-betting-fundamentals.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - entities/people/rufus-peabody.md
  - entities/platforms/fanduel.md
  - entities/platforms/underdog-fantasy.md
  - entities/sports/nba-betting.md
  - entities/sports/nfl-betting.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/pydfs-lineup-optimizer.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/tools/wc2026-agents.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - concepts/parlay-and-correlated-bets.md
maturity: draft
created: 2026-05-31
updated: 2026-08-14
---

## Relations

- @entities/platforms/fanduel.md — primary US competitor
- @concepts/dfs-strategy-overview.md — DFS product
- @concepts/sharp-vs-soft-books.md — retail/soft book classification
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160 used mostly DK opening 1X2 previews as market baseline
- @entities/tools/wc2026-agents.md — released odds + LLM agent P&L vs DK-priced market
- @sources/daily-digest-rss-industry-2026-08-14.md — DKeX football 40.2 + COMBOS

## Raw Concept

Major US legal operator — sportsbook + DFS + casino (+ best ball). Stub pending deep ingest.

## Narrative

DraftKings operates **sports betting**, **DFS**, **iCasino**, and **best ball** in licensed US states. Classified as **soft/rec retail** for sharp betting purposes — strong promos, account limits for winners possible.

### DKeX / Railbird (Aug 2026) [CONFIRMED]

DraftKings-owned DCM **Railbird Exchange (DKeX)** self-certified nine football event contracts (win/spread/total/player-or-team stat/outright/award/head-to-head) plus a **COMBOS** product that settles as the **product of component binary YES values**. $1 notional, NCAA included, Reg **40.2** (no CFTC product approval). This is DK’s **in-house PM** path vs routing Predictions volume through partners. Retail: shop DKeX vs Kalshi vs book SGP on the same football questions; COMBOS is still a **joint-implied** price, not a vig-free parlay. Hub: `@sources/daily-digest-rss-industry-2026-08-14.md`, `@concepts/parlay-and-correlated-bets.md`.

## Snippets

> "The COMBOS does not introduce a new underlying… [it] governs only the aggregation of those independently determined results." [Source: DKeX 40.2 filing via @sources/daily-digest-rss-industry-2026-08-14.md]
