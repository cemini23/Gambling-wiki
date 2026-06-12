---
title: World Cup 2026 PM retail hygiene
type: concept
tags: [concept, world-cup-2026, polymarket, kalshi, retail, risk]
keywords: [wc2026, retail-checklist, uma, fees, third-place, drawdown-brakes]
related:
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-2026-format.md
  - concepts/world-cup-prediction-market-types.md
  - concepts/world-cup-third-place-advancement-betting.md
  - concepts/world-cup-knockout-phase-betting.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/prediction-markets-crossover.md
  - concepts/favorite-longshot-bias.md
  - concepts/vig-and-hold.md
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - concepts/pm-copy-trading-retail-risks.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - concepts/world-cup-2026-fan-narrative-preview.md
  - sources/brief-k112-gambling-wc-2026-narrative-2026-06-12.md
  - osint-wiki/concepts/polymarket-retail-trading-discipline.md
maturity: validated
created: 2026-06-09
updated: 2026-06-12
---

## Relations

- @sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md — K108 ingest provenance
- @entities/sports/world-cup-2026-betting.md — WC entity hub
- @osint-wiki/concepts/polymarket-retail-trading-discipline.md — general PM retail tactics (K57 + K108 overlay)

## Raw Concept

Pre-tournament and in-tournament **human operator checklist** for wagering FIFA 2026 on **Polymarket / Kalshi** — mechanical gates before sizing, not a model or bot spec.

## Narrative

### Pre-tournament mechanical gates

| Gate | Action |
|------|--------|
| **Rules** | Read resolution block — ET vs 90-min, penalties, abandonment, oracle/data source |
| **Costs** | Model taker fee + spread; round-trip often **1–2%** on liquid sports books `[TENTATIVE]` |
| **Sizing** | **1–2%** bankroll per trade; fractional Kelly — `@concepts/kelly-criterion-betting.md` |
| **Drawdown brakes** | Pre-commit stops at **20 / 40 / 50%** session or tournament drawdown |
| **Venue** | De-vig PM vs **Kalshi + sportsbook consensus** before PM-only entry — `@concepts/world-cup-books-vs-pm-divergence.md` |
| **Tenor** | Match market duration to thesis — group/R16 vs **outright winner** capital lockup |
| **Oracle** | UMA: **2h** challenge window; disputes may extend **48–96h** — size for settlement lag |

### Format-specific (2026)

1. **48-team / 12 groups** — `@concepts/world-cup-2026-format.md`
2. **Eight third-place advancers** — qualification math is error-prone; bubble on GD — `@concepts/world-cup-third-place-advancement-betting.md`
3. **Extra R32 round** — more variance for favorites; chalk advance contracts often **90¢+** with poor upside
4. **US/Mexico/Canada hosts** — patriotic flow vs model; heat venues → tempo/injury narrative risk

### Behavioral gates (group stage density)

- **Daily trade cap** during 104-match schedule — avoid tilt/revenge sizing
- **Longshot discipline** — FLB on nation futures; need articulated edge, not tail lottery — `@concepts/favorite-longshot-bias.md`
- **Thin books** — slippage check before market orders; niche props may not match book liquidity

### Contract-type reminders

| Market | Pitfall |
|--------|---------|
| **Advance / group winner** | Not same as outright; reprices quickly after results |
| **Match ML** | 90-min vs to-advance after ET — `@concepts/world-cup-knockout-phase-betting.md` |
| **Outright winner** | Capital tied weeks; favorites ~30% historical win rate since 1978 `[TENTATIVE]` |

### Not betting advice

Educational framing for **+EV discipline** where legal. Jurisdiction, affordability, and responsible-gambling guardrails apply — `@concepts/bankroll-management.md`.

## Snippets

> "Try to bet using logic over odds. Do not bet with your heart … There are 104 games … You do not need to bet on match day one." [Source: Action Network WC preview via @entities/sports/world-cup-2026-betting.md]

> "Always price the trade after costs, and consider posting limit orders instead of crossing the spread." [Source: K108 @GodEyeDotFun via @sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md]

## Dead Ends

- **Patriotism-only sizing** on USA/Mexico/Canada without cross-venue price check
- **Outright winner** as default WC play — poor capital velocity vs stage markets
- **Copy-trading** WC whales without aggressor-side data — `@concepts/pm-copy-trading-retail-risks.md`
