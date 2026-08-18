---
title: The Odds API
type: entity
tags: [entity, tool, odds, api, sportsbook, hard-rock]
keywords: [the-odds-api, odds-api, live-odds, quota, hardrockbet, pinnacle]
related:
  - concepts/nfl-dfs-data-sources.md
  - concepts/pickem-data-sources.md
  - concepts/daily-edge-card.md
  - concepts/free-slate-context.md
  - concepts/line-shopping-and-clv.md
  - entities/platforms/hard-rock-bet.md
  - entities/tools/momentum-odds.md
  - sources/web-nfl-dfs-source-legal-posture-2026-06-20.md
  - "@osint-wiki/concepts/api-credential-registry.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @concepts/nfl-dfs-data-sources.md — GO live-odds lane in the DIY stack
- @concepts/daily-edge-card.md — optional `--fetch-odds-api` dump; CSV remains the card
- @concepts/free-slate-context.md — weather/pitchers are free; this vendor is the **price** feed
- @entities/platforms/hard-rock-bet.md — `hardrockbet_fl` / `hardrockbet` bookmaker keys
- @entities/tools/momentum-odds.md — commercial multi-book **signals**; not a substitute for this REST feed
- @sources/web-nfl-dfs-source-legal-posture-2026-06-20.md — June 2026 ToS / quota scan
- @osint-wiki/concepts/api-credential-registry.md — inventory row; secret stays in OSINT `.env`

## Raw Concept

Official sports-odds REST API at [https://the-odds-api.com](https://the-odds-api.com) (Melbourne, operating since 2017). JSON v4 feed of bookmaker prices — moneylines, spreads, totals, selected player props — **not** a projection model and **not** a book scraper.

## Narrative

### Operator role (this wiki)

| Script | Use |
|--------|-----|
| `scripts/ticket_builder.py` | Live Hard Rock (FL) ML / unders tickets; prefers `hardrockbet_fl` → `hardrockbet` → DK → FD |
| `scripts/daily_edge_card.py --fetch-odds-api` | Raw dump to paste into the CSV; does **not** replace the typed card |
| Pick'em / DFS research | Optional sportsbook prop **benchmark** vs lounge posted lines |

**Key location:** `THE_ODDS_API_KEY` on the **OSINT laptop** `.env` (`~/Projects/OSINT WORKSPACE/.env`, gitignored). Gambling-wiki scripts load that file via `scripts/env_load.py` — do **not** copy the value into this repo. Never commit it. Stay on the **free tier** unless the operator explicitly upgrades.

### Phase-0 (2026-08-15 homepage + June 2026 docs)

| Plan | Credits / month | Price (USD) |
|------|-----------------|-------------|
| Starter (free) | 500 | $0 |
| 20K | 20,000 | $30 |
| 100K | 100,000 | $59 |
| 5M | 5,000,000 | $119 |
| 15M | 15,000,000 | $249 |

- **Quota:** 1 credit per **region** per **market** on a live `/odds` call. Combine markets/regions in one request. `/sports` does not count; `/events` is cheap/no-odds. Historical odds are **10×**.
- **Burst:** paid plans document **30 req/sec**; still expect occasional HTTP 429 — retry after a couple of seconds. [Source: https://the-odds-api.com/guide/rate-limit.html (retrieved 2026-06-20; page still current 2026-08-15)]
- **Coverage (vendor claim):** 70+ sports, 40+ books including US (DK, FD, BetMGM, Caesars, Hard Rock keys), EU (incl. Pinnacle), UK, AU. [Source: https://the-odds-api.com (retrieved 2026-08-15)]
- **Not this vendor:** scraping Hard Rock / DK / FD sites — those ToS remain **NO-GO** (@concepts/nfl-dfs-data-sources.md).

### Free-tier burn (local scripts)

`ticket_builder.py` requests `regions=us,us2` plus one or more markets. Two regions × two markets = **4 credits** per call. 500/month is enough for a few daily tickets, not a polling daemon.

Cache `/sports` (~1h) and `/events` (~10 min). Live odds: 30–120s near lock only. Print `x-requests-remaining` after each call.

### Verdict

**GO** as the licensed live-odds path. **Stay free-tier** for ticket builder / edge-card dumps. **CONDITIONAL-GO** paid only if historical props or polling volume exhausts 500 credits. Do not treat API prices as Hard Rock SGP (in-app parlay juice differs).

## Snippets

> "The current rate limit is 30 requests per second on paid usage plans." [Source: https://the-odds-api.com/guide/rate-limit.html (retrieved 2026-06-20)]

> "The usage quota cost is 1 per region per market." [Source: https://the-odds-api.com/liveapi/guides/v4/ (retrieved 2026-06-20)]

> "The usage quota cost for historical odds is 10 per region per market." [Source: https://the-odds-api.com/liveapi/guides/v4/ (retrieved 2026-06-20)]

> "This will count as 1 request from your plan's usage quota." [Source: https://the-odds-api.com (retrieved 2026-08-15) — FAQ: one sport + one market + one region]

## Dead Ends

- **Paid odds aggregators** (OddsJam scanner, Unabated feed) as a replacement for this key — different product; keep Phase-0 separate
- **Polling loop** on free 500 credits — will empty the month in a few hours
- **Auto-bet / HR scrape** — out of scope; API is read-only prices
