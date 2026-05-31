---
title: Prediction markets crossover (Kalshi, Polymarket)
type: concept
tags: [concept, prediction-markets, kalshi, polymarket, crossover]
keywords: [prediction-markets, event-contracts, kalshi, polymarket, fees, crossover]
related:
  - concepts/gambling-wiki-scope.md
  - concepts/favorite-longshot-bias.md
  - concepts/kelly-criterion-betting.md
  - concepts/sharp-vs-soft-books.md
  - concepts/best-ball-strategy.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/tools/momentum-odds.md
  - entities/tools/odds-jam.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/pm-copy-trading-retail-risks.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-prediction-market-types.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - concepts/polymarket-weather-wagering-retail.md
  - entities/people/rufus-peabody.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/gambling-wiki-scope.md — scope split
- @entities/platforms/kalshi.md — regulated event contracts
- @entities/platforms/polymarket.md — crypto CLOB PM
- @osint-wiki/entities/platforms/kalshi.md — Cemini execution context
- @osint-wiki/entities/platforms/polymarket.md — bot/LP context
- @osint-wiki/concepts/cross-venue-arbitrage-pattern.md — automated arb
- @osint-wiki/concepts/sports-prediction-consensus-agent.md — sports PM entry signals

## Raw Concept

How Kalshi and Polymarket fit the **wagering** knowledge base vs the **trading stack** in osint-wiki.

## Narrative

### Same activity, two lenses

| Lens | gambling-wiki | osint-wiki |
|------|---------------|------------|
| Question | "Is this contract +EV for my bankroll?" | "How does the bot quote/farm/arbitrage it?" |
| Fees | Retail fee math, withdrawal costs | Fee APIs in orchestrator |
| Sports | Consensus agents, MomentumOdds signals | Executor bots, WC LP |
| Regulation | Consumer rules, state gaming vs DCM | CFTC, compliance briefs |

### Retail checklist before betting PM sports

1. Read **settlement rules** (void conditions, data sources)
2. Model **fees** + spread — effective hold in `@concepts/vig-and-hold.md`
3. Compare price vs **sportsbook line** (CLV analog)
4. Size with **fractional Kelly** — `@concepts/kelly-criterion-betting.md` + `@osint-wiki/concepts/kelly-sizing-quarter.md`
5. Know **jurisdiction** — geoblocks, KYC

### Tools spanning both wikis

- **MomentumOdds** — sportsbook signal feed; tutorials target Kalshi execution (`@entities/tools/momentum-odds.md`, `@osint-wiki/entities/tools/momentum-odds.md`)
- **Odds Jam / Prediction Insiders** — Polymarket copy alerts (`@entities/tools/odds-jam.md`)

### Sports prediction markets (Novig and peers)

Wharton interview with `@entities/people/rufus-peabody.md` frames **sports-focused prediction markets** (Novig cited) as an alternative when **DK/FD limit sharp winners**. Tradeoffs vs books:

| Factor | Traditional book | Sports PM venue |
|--------|------------------|-----------------|
| Limits | Low for winners at soft US books | Liquidity caps `[TENTATIVE]` |
| Pricing | Embedded vig (-110) | Bid-ask + fees |
| Reference | Pinnacle close | Often still benchmark vs Pinnacle |

Retail: same checklist as Kalshi/PM — fees, settlement, bankroll. Bot arb → `@osint-wiki`.

### When to stay in traditional books

Better liquidity on mainstream spreads; PM shines on **niche events**, **political/macroeconomic** contracts, and **cross-venue** mispricings (advanced).

### World Cup 2026

Expanded tournament + host nations (USA/Mexico/Canada) create **books vs PM/Kalshi divergence** on advance and futures — `@entities/sports/world-cup-2026-betting.md`, `@concepts/world-cup-books-vs-pm-divergence.md`. Contract-type cheat sheet: `@concepts/world-cup-prediction-market-types.md`.

### Signal products

- **MomentumOdds** — `@entities/tools/momentum-odds.md` + `@concepts/sportsbook-pm-line-divergence.md`
- **Odds Jam / Prediction Insiders** — `@entities/tools/odds-jam.md` + `@concepts/pm-copy-trading-retail-risks.md`

## Snippets

> Rufus Peabody on prediction markets vs books: sharp limits at major US sportsbooks push flow to Pinnacle or PM venues with different liquidity/fee profiles. [Source: M1T0OlG3XEU via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

*(cross-wiki — deep bot snippets live in @osint-wiki)*
