---
title: World Cup prediction market contract types
type: concept
tags: [concept, world-cup-2026, prediction-markets, kalshi, polymarket]
keywords: [advance-market, group-winner, outright, moneyline, to-advance, resolution]
related:
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-2026-format.md
  - concepts/world-cup-knockout-phase-betting.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/world-cup-third-place-advancement-betting.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
maturity: validated
created: 2026-05-31
updated: 2026-06-09
---

## Relations

- @entities/sports/world-cup-2026-betting.md — WC hub
- @concepts/world-cup-knockout-phase-betting.md — 90-min vs to-advance detail
- @osint-wiki/sources/gemini-world-cup-market-structure-research-2026-05-29.md — full contract map

## Raw Concept

Retail guide to **which Polymarket / Kalshi contract** answers which betting question for World Cup 2026.

## Narrative

### Group stage (primary retail menu)

| Your question | Polymarket (typical series) | Kalshi (typical series) | Notes |
|---------------|----------------------------|-------------------------|-------|
| Will Team X reach knockout stage? | `FIFA World Cup: Team to advance to Knockout Stages` | `World Cup Group [X] Qualifiers` | Resolves ~end of group play; **reprices** during group |
| Will Team X **win** the group? | `FIFA World Cup Group [X] Winner` | `Group [X] Winner` | **Not** the same as advance in 48-team format |
| Will Team X win the **tournament**? | `2026 FIFA World Cup Winner` | `Men's World Cup Winner` | Long capital lockup; immediate No on KO elimination |
| Who wins **this match** (regulation)? | Match moneyline (3-way) | `Games` / fixture markets | See knockout resolution rules |
| Who **advances** from this KO tie? | To Advance / To Qualify | To Advance variants | Includes ET + penalties |

### Naming map

"Advance to knockout" = **Reach Round of 32** in the 48-team format [CONFIRMED @osint-wiki knockout map source].

### Fee / settlement differences (retail)

| Platform | Retail notes |
|----------|--------------|
| **Polymarket** | Hybrid CLOB; sports **taker fees** scale with price (~0.75–1.8% peak near 50¢) [TENTATIVE]; maker often free; resolves via FIFA + credible reporting |
| **Kalshi** | CFTC DCM; taker ~$0.01–0.02/contract; resolves via **ESPN/Fox/WSJ/Reuters** consensus — can differ from FIFA-only PM path on edge cases [TENTATIVE] |

Always read the **contract rules text** before betting — oracle source matters for voids and delays.

### What to avoid as a casual bettor

- **97–98¢ advance YES** on elites pre-tournament — tiny upside, full downside if upset
- **Outright winner** unless you accept weeks of capital lock and immediate elimination on any KO loss
- **In-play match ML** without understanding 90′ draw settlement vs live score

### Cross-venue shopping

Same team may trade at different implied % on Kalshi vs Polymarket vs FanDuel — see `@concepts/world-cup-books-vs-pm-divergence.md`. Resolution text must match before treating as the same bet.

## Snippets

> A 3-way moneyline tied at 90′ resolves Draw even if a team wins in extra time; To Advance markets include ET and penalties. [Source: @osint-wiki/sources/gemini-wc-knockout-market-map-2026-05-30.md]
