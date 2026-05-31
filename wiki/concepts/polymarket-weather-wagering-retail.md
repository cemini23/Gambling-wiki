---
title: Polymarket weather wagering (retail)
type: concept
tags: [concept, polymarket, weather, copy-trading, retail, k90]
keywords: [weather-markets, polymarket, copy-trading, wallet-following, retail, alterego]
related:
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: @osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md
---

# Polymarket weather wagering (retail)

## Relations

- @concepts/pm-copy-trading-retail-risks.md — shared copy-trading discipline checklist
- @entities/platforms/polymarket.md — platform fees, settlement, wallet setup
- @osint-wiki/concepts/polymarket-weather-trading-strategy.md — bot/forecast architecture (OSINT primary)
- @osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md — K90 Post 15 (@AlterEgo_eth)
- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — weather-bot graveyard context

## Raw Concept

Retail-facing angle on **Polymarket weather markets** — framed as copy-trading specific wallets rather than building forecast models. Sourced from K90 Posts.docx Post 15 (@AlterEgo_eth). **Not** a bot-adopt path; OSINT weather-bot repos are rejected/graveyard per K90 tool eval.

## Narrative

### The retail pitch [TENTATIVE]

Social posts (notably @AlterEgo_eth) promote weather PM markets as "easy money" if you **follow the right wallets** — implying execution edge via whale-copy rather than meteorology. This is a **behavioral wagering product** angle, not a quant stack.

### Why this page exists (scope split)

| Layer | Home wiki | Content |
|-------|-----------|---------|
| Bot architecture, forecast revision, station resolution | `@osint-wiki` | `@osint-wiki/concepts/polymarket-weather-trading-strategy.md` |
| Retail posture, wallet-copy skepticism, bankroll rules | **gambling-wiki** | this page |

K90 tool eval: **weather-bot GitHub graveyard** — 5 UNAVAILABLE + 4 Reject in one batch. Do not pursue open-source weather bots; retail should assume **manual or alert-based** copy only.

### Retail rules (extends `@concepts/pm-copy-trading-retail-risks.md`)

1. **Wallet-following ≠ edge** — on-chain flow is public; crowding destroys slippage advantage
2. **Weather ≠ sports** — station-specific resolution (whole °F, WU observations); read market rules before sizing
3. **Survivorship in "top weather traders"** — ranking posts are marketing funnels, not audited track records `[TENTATIVE]`
4. **Fee drag** — high trade count on thin weather books erodes edge faster than sports PM
5. **3-month log required** — ignore 30-day promo windows; weather variance is lumpy
6. **Never size from "easy money" copy** — treat as entertainment budget per `@concepts/bankroll-management.md`

### Verdict

**REFERENCE-ONLY** for retail discipline — document the pitch and countermeasures; **NO-GO** on weather-bot OSS adopt; cross-link OSINT for any automated execution path.

## Snippets

> "Weather markets on Polymarket are full of easy money - if you know whose trades to follow" [Source: Posts.docx K90 Post 15, @AlterEgo_eth via @osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md]

> Weather-bot GitHub URLs remain a high-noise cluster: seven UNAVAILABLE rows in a single batch. [Source: @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

## Dead Ends

- **Open-source weather bots** (PolyWeather AGPL, MoonsatProtocol, etc.) — K90 graveyard; see `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`
- **@AlterEgo_eth bot stack** — same author ecosystem routed to OSINT for deconstruction; retail copy-trading claims stay `[TENTATIVE]`
