---
title: K108 — WC 2026 Polymarket retail hygiene (cross-wiki brief)
type: source
tags: [source, brief, world-cup-2026, polymarket, retail, k108]
keywords: [k108, godeyedotfun, wc2026, retail-hygiene, uma, fees]
related:
  - concepts/world-cup-pm-retail-hygiene.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-third-place-advancement-betting.md
  - concepts/world-cup-knockout-phase-betting.md
  - concepts/world-cup-2026-format.md
  - concepts/world-cup-prediction-market-types.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/prediction-markets-crossover.md
  - concepts/favorite-longshot-bias.md
  - concepts/vig-and-hold.md
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - osint-wiki/concepts/polymarket-retail-trading-discipline.md
  - osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md
maturity: validated
read_status: deep-read
created: 2026-06-09
updated: 2026-06-09
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md"
---

## Relations

- @concepts/world-cup-pm-retail-hygiene.md — gambling-wiki operator checklist
- @entities/sports/world-cup-2026-betting.md — WC entity hub
- @osint-wiki/concepts/polymarket-retail-trading-discipline.md — full tactic framework + K108 overlay

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | `briefs/2026-06-09_k108-gambling-wc-retail-hygiene-from-osint.md` |
| **Origin** | K108 @GodEyeDotFun — ten mistakes for FIFA 2026 on Polymarket |
| **OSINT compile** | `@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md` (Post 0) |
| **Routed** | 2026-06-09 |

## Narrative

Cross-wiki brief routed from OSINT K108. **gambling-wiki owns** the human WC trader checklist (rules, fees, format, cross-venue). **@osint-wiki owns** CLOB tooling, bot gates, and full seven-tactic framework.

### Ten mistakes → retail gates [CONFIRMED — K108 Post 0]

| # | Mistake | Gate |
|---|---------|------|
| 1 | Title not rules | Read resolution: ET, penalties, abandonment, data source |
| 2 | Ignore fees + spread | Model taker fee curve + spread; prefer maker limits where rebates apply |
| 3 | Longshot festival | FLB — need concrete mispricing thesis, not tail lottery |
| 4 | Outright winner lockup | Match tenor to thesis — group/R16 vs season-long outright |
| 5 | Thin niche books | Depth/slippage check before market orders |
| 6 | Gut sizing | 1–2% bankroll/trade; pre-commit drawdown brakes (20/40/50%) |
| 7 | Revenge trading | Daily trade cap during dense group-stage schedule |
| 8 | UMA dispute latency | 2h challenge window; possible 48–96h DVM — favor templated sports rules |
| 9 | Single-venue anchor | De-vig vs Kalshi/books before PM-only sizing |
| 10 | 48-team format drift | Third-place math, extra R32, US heat venues |

### 2026 format reminders

- **12×4 groups** → Round of 32; **8 of 12 third-place teams** advance
- Extra knockout round increases variance for favorites
- Host-nation / heat narratives — see `@concepts/world-cup-third-place-advancement-betting.md`

## Snippets

> "Always price the trade after costs, and consider posting limit orders instead of crossing the spread." [Source: K108 Post 0, @GodEyeDotFun]

## Dead Ends

- Treating K108 as bot deployment spec — informational hygiene only
- Blind copy-trading WC markets without wallet filters (`@concepts/pm-copy-trading-retail-risks.md`)
