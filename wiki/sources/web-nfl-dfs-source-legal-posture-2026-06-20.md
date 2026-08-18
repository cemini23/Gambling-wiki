---
title: Web research — NFL DFS source legal / ToS posture (June 2026)
type: source
tags: [source, dfs, nfl, legal, tos, scraping, rate-limits, w-legal]
keywords: [nflverse, the-odds-api, fanduel, draftkings, espn, open-meteo, ownership archives, rotogrinders, action network, etr]
related:
  - concepts/nfl-dfs-data-sources.md
  - entities/tools/the-odds-api.md
maturity: validated
read_status: deep-read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/nfl-dfs-data-sources.md — W-LEGAL decision matrix distilled from this scan
- @entities/tools/the-odds-api.md — vendor entity (quota, free tier, local scripts)

## Raw Concept

June 2026 web pass to answer one practical question: **which NFL DFS inputs are license-clear enough to automate, and which should stay manual or be avoided entirely?**

| Source | URL(s) checked | Retrieved | Why it matters |
|-------|-----------------|-----------|----------------|
| nflverse / nflreadr | `https://nflreadr.nflverse.com/`, `https://nflreadr.nflverse.com/reference/csv_from_url.html`, `https://github.com/nflverse/nflverse-data` | 2026-06-20 | Published bulk/data-package posture, caching behavior, GitHub-backed delivery |
| The Odds API | `https://the-odds-api.com/liveapi/guides/v4/`, `https://the-odds-api.com/guide/rate-limit.html`, `https://the-odds-api.com/historical-odds-data/` | 2026-06-20 | Official usage quota and rate-limit language |
| FanDuel | `https://fanduel.com/terms` | 2026-06-20 | Direct anti-scraping language |
| DraftKings | `https://sportsbook.draftkings.com/legal/us-terms-of-use` | 2026-06-20 | Direct anti-automation / anti-harvesting language |
| ESPN | `https://espn.playerfirsttech.com/site/legal/terms`, plus contextual repo docs for undocumented endpoints | 2026-06-20 | Official non-commercial-only posture; endpoint support ambiguity |
| Open-Meteo | `https://open-meteo.com/en/terms` | 2026-06-20 | Explicit free-tier limits and non-commercial allowance |
| Ownership vendors | `https://rotogrinders.com/terms-of-service`, `https://www.actionnetwork.com/terms`, `https://establishtherun.com/terms/` | 2026-06-20 | Representative ownership/projection vendor anti-scraping clauses |

## Narrative

### High-confidence reads

1. **The clean automation lane is official/public data services**: nflverse, The Odds API, Open-Meteo.
2. **Books and DFS operators are manual-only unless they explicitly grant another path**: FanDuel and DraftKings both ban scraping/automation.
3. **Undocumented public JSON is still weak legal / operational ground**: ESPN endpoints may be reachable, but they are not a stable or clearly permitted contract surface.
4. **Ownership archives are usually the product itself**: subscription sites explicitly ban scraping because projections/ownership are their monetized IP.

### Source notes

#### nflverse

The package/docs are friendly to programmatic access, but they stop short of granting blanket rights over all underlying NFL data. Practical reading: **fine for research use**, especially through the documented packages and GitHub release artifacts, but keep attribution / provenance and avoid assuming that every upstream data origin is fully relicensed.

#### The Odds API

This is the cleanest sportsbook-odds lane in the set. The provider documents **quota math**, **historical pricing**, and **rate-limit handling**, and explicitly recommends caching and combining markets/regions.

#### FanDuel / DraftKings

Both operators use classic anti-bot language and are the highest-risk automation targets because enforcement can touch a regulated gambling account, not just an anonymous IP. Operational read: **never make them the machine-ingest backbone**.

#### ESPN

Official terms clearly allow personal/non-commercial display/download and clearly prohibit broader exploitation without written permission, but do **not** publish a clean public developer contract for the commonly used site JSON endpoints. Community documentation is explicit that these endpoints are unofficial and unstable. That combination makes ESPN a poor foundation for a repeatable production workflow.

#### Ownership archives

Representative vendors are explicit: RotoGrinders bans scraping/data mining, Action/FantasyLabs bans page-scrape/robots, and ETR bans scraping plus robotic access beyond human browsing rates. Unless a vendor gives an explicit export right, treat ownership/projection pages as **manual-consumption subscription content**, not a scrape target.

## Snippets

> "The R code for this package is released as open source under the MIT License. NFL data accessed by this package belong to their respective owners, and are governed by their terms of use." [Source: https://nflreadr.nflverse.com/ (retrieved 2026-06-20)]

> "This is a thin wrapper on data.table::fread, but memoised & cached for twenty four hours." [Source: https://nflreadr.nflverse.com/reference/csv_from_url.html (retrieved 2026-06-20)]

> "The current rate limit is 30 requests per second on paid usage plans." [Source: https://the-odds-api.com/guide/rate-limit.html (retrieved 2026-06-20)]

> "The usage quota cost is 1 per region per market." [Source: https://the-odds-api.com/liveapi/guides/v4/ (retrieved 2026-06-20)]

> "The usage quota cost for historical odds is 10 per region per market." [Source: https://the-odds-api.com/liveapi/guides/v4/ (retrieved 2026-06-20)]

> "By using the Free API for non-commercial use you agree to following terms: - Less than 10'000 API calls per day, 5'000 per hour and 600 per minute. - You may only use the free API services for non-commercial purposes." [Source: https://open-meteo.com/en/terms (retrieved 2026-06-20)]

> "use any robot, spider, scraper, sniping software or other automated means to access the Service for any purpose ... without our express written permission." [Source: https://fanduel.com/terms (retrieved 2026-06-20)]

> "Using automated means ... to interact with the Website in any way ..." and "Using automated means ... to obtain, collect or access any information on the Website or of any User for any purpose." [Source: https://sportsbook.draftkings.com/legal/us-terms-of-use (retrieved 2026-06-20)]

> "You may display and ... download or print portions of the material ... solely for your own non-commercial use ... [but] you may not ... otherwise exploit this site or any portion of it unless expressly permitted by ESPN in writing." [Source: https://espn.playerfirsttech.com/site/legal/terms (retrieved 2026-06-20)]

> "Unofficial: These APIs are not officially supported and may change without notice ... Rate Limiting: Be respectful - no official limits published, but excessive requests may be blocked." [Source: https://github.com/pseudo-r/Public-ESPN-API (retrieved 2026-06-20)]

> "Users of the Service may not engage in unauthorized spidering, 'scraping,' data mining or harvesting of Content, or use any other unauthorized automated means to gather data from or about the Service." [Source: https://rotogrinders.com/terms-of-service (retrieved 2026-06-20)]

> "You may not use any 'deep-link', 'page-scrape', 'robot', 'spider' or other automatic device ..." [Source: https://www.actionnetwork.com/terms (retrieved 2026-06-20)]

> "You agree not to engage in ... 'scraping'; (ii) using any automated system, including without limitation 'robots,' 'spiders,' 'offline readers,' etc., to access the Service in a manner that sends more request messages ... than a human can reasonably produce ..." [Source: https://establishtherun.com/terms/ (retrieved 2026-06-20)]

## Dead Ends

- **ESPN as primary stats backbone** — rejected for unsupported endpoint contract + unclear permission path
- **Scraped ownership mirror** — rejected; too much contract/IP risk for too little edge durability
