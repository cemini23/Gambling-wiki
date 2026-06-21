---
title: NFL DFS data sources
type: concept
tags: [concept, dfs, nfl, data-sources, legal, tos, w-legal]
keywords: [nflverse, the-odds-api, fanduel, draftkings, espn, open-meteo, ownership archives, scraping, rate limits, caching]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-foss-tooling-landscape.md
  - concepts/implied-team-totals-dfs.md
  - concepts/dfs-weather-adjustments.md
  - concepts/dfs-injury-and-news-workflow.md
  - sources/web-nfl-dfs-source-legal-posture-2026-06-20.md
  - concepts/dfs-model-orchestration.md
  - concepts/dfs-backtesting-framework.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/diy-nfl-dfs-model-architecture.md — W-DATA/W-LEGAL layer page for the DIY stack
- @sources/web-nfl-dfs-source-legal-posture-2026-06-20.md — underlying June 2026 ToS / usage scan
- @sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md — OSINT weather API inventory + sibling wiki matrix

## Raw Concept

Operator matrix for the **NFL DFS source stack** with emphasis on **contract / ToS posture**, **practical rate norms**, and **default cache discipline**. Goal: use sources that are stable enough for a repeatable model build without stepping into obvious scraping or account-risk lanes.

## Narrative

### Operating rule

Prefer the stack in this order:

1. **Official/public API or published bulk data** with explicit usage guidance
2. **Manual exports or first-party files** where the product intentionally exposes them
3. **Undocumented endpoints** only for throwaway exploration, not for a production or repeatable pipeline
4. **No account-bound scraping** of books, DFS operators, or paid-content vendors without explicit permission

### Source matrix

| Source | Recommended access mode | Scrape allowed? | Rate / usage norm | Personal-use OK? | Risk | Verdict |
|--------|--------------------------|-----------------|-------------------|------------------|------|---------|
| **nflverse** | Use `nflreadr` / `nflreadpy` / GitHub release files; lean on built-in caching | **Not framed as scraping**; use published package/data endpoints, not bespoke hammering | No nflverse-specific limit published; practical norm is **cache aggressively**, use GitHub token for release/API calls, and prefer bulk download over repetitive pulls | **Yes**, with caveat that underlying NFL data remain subject to source-owner terms | **Low-Medium** | **GO** |
| **The Odds API** | Official REST API with key | **Yes via official API** | Paid plans document **30 req/sec** burst limit; usage quota is **1 credit per region per market** and **10x** for historical odds; cache `/sports` + `/events` | **Yes**, per plan | **Low** | **GO** |
| **Open-Meteo** | Official weather API | **Yes via official API** | Free tier: **10k/day, 5k/hour, 600/min** for non-commercial use; weighted by request complexity | **Yes for non-commercial / personal**; commercial use requires paid plan | **Low** if non-commercial, **Medium** if monetized without upgrade | **GO** for personal research, **CONDITIONAL-GO** for commercial/monetized apps |
| **FanDuel** | Manual site/app use only; only use files they intentionally expose | **No**; terms explicitly ban robots, spiders, scrapers, and other automated access without written permission | No public API or rate guidance for third parties; practical norm is **do not automate against the site** | Personal use of app/site is fine; automated data extraction is not | **High** | **CONDITIONAL-GO** for manual-only workflows; **NO-GO** for scraping |
| **DraftKings** | Manual site/app use only; only use first-party files or explicitly allowed partner paths | **No**; terms ban automated interaction and automated collection of site information | No public sportsbook/DFS API for general use; practical norm is **do not automate against the site** | Personal use of app/site is fine; automated extraction is not | **High** | **CONDITIONAL-GO** for manual-only workflows; **NO-GO** for scraping |
| **ESPN endpoints** | Avoid as a backbone source; if touched, treat as undocumented and disposable | **Not expressly approved**; official terms allow only personal/non-commercial use and forbid broader exploitation without permission | No official public rate limits published; community docs warn endpoints are unofficial and can change or block at any time | **Weak yes** for casual personal viewing; **not a clean green light** for systematic ingestion | **High** | **NO-GO** as a primary pipeline source; **CONDITIONAL** for one-off prototyping only |
| **Ownership archives** (`RotoGrinders`, `FantasyLabs`/`Action`, `ETR`, similar) | Use only explicit vendor exports or manual notes; do not scrape paywalled pages | **Usually no**; major vendors explicitly ban scraping / page-scraping / robots | No public machine-use norms; practical norm is **manual access or vendor-approved export only** | Subscriber viewing is generally fine; reuse/export rights are narrow and redistribution risk is real | **High** | **CONDITIONAL-GO** only where export rights are explicit; otherwise **NO-GO** for automation |

### Red-flag sources

- **FanDuel / DraftKings** — clear anti-bot / anti-scraper language; also highest account-enforcement risk because access is tied to regulated wagering accounts.
- **ESPN undocumented endpoints** — publicly reachable but unsupported; terms do not give a clean ingest permission path, and the endpoint contract can break without notice.
- **Ownership archive vendors** — subscription IP is the product; scraping or mirroring paywalled ownership/projection pages is the fastest way into breach-of-contract / account-termination territory.

### Recommended caching policy

| Source class | Cache policy | Notes |
|-------------|--------------|-------|
| **nflverse historical / structural data** | Snapshot to disk by season and release; refresh **daily** in-season, less often for historical tables | Prefer bulk release download over frequent row-level pulls |
| **The Odds API metadata** (`/sports`, `/events`) | Cache **10-60 minutes** depending on slate churn | Their own docs recommend less frequent calls for endpoints that do not change often |
| **The Odds API live odds** | Cache **30-120 seconds** near lock; longer outside active monitoring windows | Combine markets/regions in one request to reduce quota burn |
| **Open-Meteo** | Cache **30-60 minutes** for weekly prep, **10-15 minutes** only when weather-sensitive edges matter near lock | Free tier is generous enough if you batch locations and avoid spam |
| **FanDuel / DraftKings salaries or contest data** | Treat any manually downloaded file as an **immutable timestamped artifact** | No polling; one fetch per slate unless the operator materially changes the slate |
| **ESPN endpoints** | If used for ad hoc prototypes, cache **6-24 hours** and never build a high-frequency dependency | Better replaced by nflverse or paid/official feeds |
| **Ownership archives** | One manual export / capture per slate; store locally and do not re-hit the site automatically | Preserve provenance because content can update close to lock |

### Default policy for the DIY stack

- **Primary GO stack:** `nflverse` + `The Odds API` + `Open-Meteo`
- **Manual-only supplement:** FanDuel / DraftKings salary and contest files if intentionally exposed to users
- **Avoid as system dependencies:** ESPN internal endpoints and scraped ownership pages
- **If ownership matters:** buy a tool that offers an explicit export path, or build a weak in-house ownership prior from contest-size / salary / projections / leverage heuristics instead of scraping paid pages

### Technical data inventory (W-DATA, K125)

| Dataset | Source | Granularity | In-season lag | License |
|---------|--------|-------------|---------------|---------|
| Play-by-play | nflreadpy `load_pbp()` | Play | Nightly + ~15m raw | CC-BY 4.0 |
| Player stats | `load_player_stats()` | Weekly | Nightly | CC-BY 4.0 |
| Schedules + Vegas | `load_schedules()` | Game | spread/total every 5m | CC-BY 4.0 |
| Snap counts | `load_snap_counts()` | Weekly | ~1 day post-game | CC-BY 4.0 |
| Injuries | `load_injuries()` | Weekly | With reports | CC-BY 4.0 |
| Routes (in-season) | FTN participation | Play | **Post-season only** free | CC-BY-SA 4.0 |
| Live odds | The Odds API | Game | On-demand | API ToS |
| Historical odds | nflreadr schedules | Game | Closing lines 1999+ | CC-BY 4.0 |

**Python loader:** **nflreadpy** GO (replaces deprecated nfl_data_py). **ID join:** gsis_id via `load_players()` + `load_ff_playerids()`; RapidFuzz fallback for FD/DK salary names.

**Gaps:** salaries (manual FD/DK export), ownership (paid export or custom model), in-season route data (snap share proxy).

### Cross-wiki complements

| Topic | Page |
|-------|------|
| Weather API inventory | @sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md |
| Open-Meteo / NWS / Visual Crossing / Wethr | @osint-wiki/entities/data-sources/open-meteo.md and related |
| API credential registry | @osint-wiki/concepts/api-credential-registry.md |
| MomentumOdds (multi-book) | @entities/tools/momentum-odds.md ↔ @osint-wiki/entities/tools/momentum-odds.md |

## Snippets

> "Every modeling choice must be backtest-justified and every data source license-cleared." [Source: @sources/research-diy-dfs-model-master-plan-2026-06-20.md]
