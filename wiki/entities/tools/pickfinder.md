---
title: PickFinder
type: entity
tags: [entity, tool, sports-betting, research, saas]
keywords: [pickfinder, research, odds, spread, total, win-probability]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - entities/tools/odds-jam.md
  - entities/tools/unabated.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-09-30
---

## Relations

- @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md — tRZzx1Alw5A tutorial

## Raw Concept

**PickFinder** — sports betting **research SaaS** (filters, match odds, win probability) featured in operator YouTube tutorial.

## Narrative

### What it does (per tutorial)

- Aggregates match odds: moneyline, **spread**, **total**, implied win probability
- Filter/stat views to narrow bet candidates
- Positioned as workflow accelerator — **not** a substitute for EV math or CLV logging

### Phase-0 checklist — closed 2026-09-30

| Check | Result |
|-------|--------|
| **Canonical domain** | **`pickfinder.app`** — `pickfinder.com` is **not** the vendor. Correct any earlier reference. |
| **Premium** | **$19.99/mo** ($14.99/mo web-exclusive), **$39.99**/quarter, **$149.99**/year |
| **Pro** | **$299.99**/year. Adds the **Arbitrage finder**, **Middles board**, and **EV+ board** |
| **Refund** | Refund request accepted **within 3 days** of first purchase. **No free trial** for Premium; Premium members get a one-time 3-day Pro trial |
| **Coverage** | 14 sports + esports · 25+ books and DFS apps — includes **PrizePicks, Underdog, Sleeper**, DraftKings, FanDuel |
| **Odds latency** | Vendor claims "within seconds"; unverified against book feeds [NEEDS VERIFICATION 2026-09-30] |
| **+EV proof** | The **EV+ board** is priced against a **de-vigged fair line**. That is a method, not a track record. No independent CLV audit found [TENTATIVE] |
| **Boards overlap** | EV+/arb/middles boards overlap `@entities/tools/odds-jam.md`. PickFinder competes on **price**, not depth |

### Verdict

**CONDITIONAL-GO** — cheap props-research UI, and the only low-cost option found that covers **FS/pick'em books** (PrizePicks, Underdog, Sleeper) alongside traditional sportsbooks. Pair with `@concepts/line-shopping-and-clv.md` discipline. No edge claim is validated by the vendor's own marketing.

Phase-0 closed 2026-09-30. At ~$12.50–$20/mo it is the lowest-commitment paid tool in `entities/tools/`. The 3-day refund window is the only risk control — test it against a real slate inside that window.

**Note:** the earlier stub referenced a single creator tutorial. Pricing above is from the vendor site plus third-party reviews; treat exact tier prices as [TENTATIVE] until seen in-app.

## Snippets

> "How to Research Winning Sports Bets: PickFinder Tutorial" — product walkthrough for match odds and filters. [Source: tRZzx1Alw5A via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]
