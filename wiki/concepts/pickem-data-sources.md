---
title: Pick'em data sources
type: concept
tags: [concept, pickem, props, nfl, data-sources, w-data, k147]
keywords: [nflreadpy, the-odds-api, open-meteo, manual-lines, historical-props, scraper-reject]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/pickem-operator-workflow.md
  - concepts/pickem-pipeline-integration-spec.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/pickem-stat-type-mapping.md
  - concepts/pickem-legal-and-tos-posture.md
  - concepts/pickem-backtesting-framework.md
  - concepts/pickem-operator-workflow.md
  - sources/research-nfl-historical-odds-2026-06-20.md
  - sources/web-nfl-dfs-source-legal-posture-2026-06-20.md
  - entities/tools/ceminidfs.md
  - entities/sports/nfl-betting.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/nfl-dfs-data-sources.md — parent stack; pick'em inherits GO/NO-GO posture
- @sources/research-nfl-historical-odds-2026-06-20.md — game-level Vegas history; props extension below
- @concepts/pickem-legal-and-tos-posture.md — scraper reject list (W-LEGAL)

## Raw Concept

**Data inventory** for the standalone pick'em / props fair-value tool (K147). Reuses CeminiDFS nflverse path for features; adds posted-line capture, optional sportsbook prop benchmarks, and historical grading sources — **no platform scrapers**.

## Narrative

### Operating rule (inherit from nfl-dfs-data-sources)

1. **Official/public APIs** with license (nflverse, The Odds API, Open-Meteo)
2. **Manual operator capture** for PrizePicks / UD posted lines
3. **Paid SaaS** for benchmark reads only (PickLabs, Unabated) — manual export
4. **REJECT** unlicensed platform scrapers — same bar as CeminiDFS K129

### Source matrix

| Source | Role in pick'em stack | Access mode | Scrape? | Verdict |
|--------|----------------------|-------------|---------|---------|
| **nflreadpy / nflverse** | PBP, usage, player stats, schedules, injuries | Package + disk cache | Not scraping — published bulk | **GO** |
| **The Odds API** | Sportsbook player prop lines (benchmark / CLV) | REST + API key | Via official API only | **GO** (if subscribed) |
| **Open-Meteo + stadiums** | Wind/temp → passing environment | Official API | Via official API | **GO** |
| **nflreadr schedules** | Closing spread/total for game env | `load_schedules()` | N/A | **GO** — @sources/research-nfl-historical-odds-2026-06-20.md |
| **PrizePicks / UD posted lines** | Target O/U lines for edge calc | **Manual entry** or timestamped screenshot log | **NO** | **MANUAL ONLY** |
| **PickLabs / BettingPros / Unabated** | Accuracy benchmark | Manual UI / export | **NO** automation | **CONDITIONAL** |
| **Platform scrapers (no LICENSE)** | — | — | **REJECT** | **NO-GO** |

### nflreadpy reuse (from CeminiDFS)

Same loaders as @concepts/nfl-dfs-data-sources.md — no fork required Phase-1:

| Dataset | Loader | Pick'em use |
|---------|--------|-------------|
| Play-by-play | `load_pbp()` | Usage, efficiency, red zone |
| Player stats | `load_player_stats()` | Backtest actuals vs line |
| Schedules + Vegas | `load_schedules()` | ITT, pace, game script |
| Snap counts | `load_snap_counts()` | Volume priors |
| Injuries | `load_injuries()` | Pre-slate status (lag-aware) |
| Players / IDs | `load_players()`, `load_ff_playerids()` | Name join to posted lines |

**Cache policy:** snapshot by season; daily refresh in-season; immutable weekly backtest slices at cutoff (see @concepts/pickem-backtesting-framework.md).

### The Odds API — player props lane

| Use | Endpoint pattern | Quota note |
|-----|------------------|------------|
| Live prop benchmark | `/v4/sports/americanfootball_nfl/events/{id}/odds` + prop markets | 1 credit/region/market; batch regions |
| Historical props | Historical odds endpoint | **10×** credit multiplier — budget carefully |
| Metadata | `/sports`, `/events` | Cache 10–60 min |

**Role:** compare DIY `fair_p` vs sharp/soft book implied prob — **not** a substitute for lounge posted lines. Lounge take differs from -110/-110 books.

**Gap:** market coverage varies by book region; prop menu ≠ pick'em stat menu — map via @concepts/pickem-stat-type-mapping.md.

### Open-Meteo

Reuse @concepts/dfs-weather-adjustments.md patterns: stadium lat/lon → hourly wind/gust/precip at kickoff window. Cache 30–60 min weekly prep; 10–15 min near lock only when wind props matter.

### Manual posted lines schema

Operator-maintained CSV (or SQLite) — **immutable snapshot per capture**:

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `line_id` | UUID | yes | Unique row |
| `captured_at` | ISO8601 | yes | When line was read from app |
| `platform` | enum | yes | `prizepicks`, `underdog_pickem`, `sleeper`, … |
| `player_name` | string | yes | As shown on app |
| `player_id` | string | no | Internal join if resolved |
| `stat_id` | string | yes | Canonical from stat-type mapping |
| `line` | float | yes | Posted O/U number |
| `line_type` | enum | no | `standard`, `demon`, `goblin`, `alt` |
| `direction_offered` | enum | no | `more_only`, `less_only`, `both` |
| `slate_date` | date | yes | Game date (ET) |
| `game_id` | string | no | nflverse join |
| `notes` | string | no | Injury context, screenshot ref |

**Provenance:** never overwrite rows — append-only log. Screenshot optional backup in local `briefs/` (gitignored).

### Historical prop lines (backtest)

| Source | Coverage | Join | Verdict |
|--------|----------|------|---------|
| **Operator manual log** | Your captures only | `player_id` + `stat_id` + `slate_date` | **GO** — primary for lounge-specific lines |
| **The Odds API historical** | Sportsbook props (if plan) | Event + player name fuzzy | **CONDITIONAL** — CLV studies vs books |
| **nflreadr schedules** | Spread/total only | `game_id` | **GO** — game env, not prop lines |
| **Kaggle / scraped archives** | Variable | Heavy clean | **NO-GO** default |

**Minimum bar:** 1 full NFL season of walk-forward grading before edge claims — see @concepts/pickem-backtesting-framework.md.

**Opening lines:** nflverse has closing game lines only; opening-line CLV for props requires paid Odds API historical or manual log — @sources/research-nfl-historical-odds-2026-06-20.md.

### Scraper reject list (do not ingest)

Mirror architecture + CeminiDFS K129 eval:

| Repo / tool | Reason |
|-------------|--------|
| `aidanhall21/underdog-fantasy-pickem-scraper` | **NO LICENSE** |
| `fantasydatapros/underdog` | **NO LICENSE** |
| Any PrizePicks GPL scraper | No official API; ToS risk |
| Mobile app intercept / credential automation | **NO-GO** — legal posture |

Full posture: @concepts/pickem-legal-and-tos-posture.md.

### Default stack (Phase-1 MVP)

```text
nflreadpy (features + actuals)
  + Open-Meteo (weather)
  + manual posted_lines.csv (target)
  + The Odds API optional (benchmark)
  → prop-fair → edges.csv
```

## Snippets

> "PrizePicks / UD posted lines — Manual entry or operator screenshot — no scraper." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md data posture]

> "No free granular opening line history in nflverse — closing lines only." [Source: @sources/research-nfl-historical-odds-2026-06-20.md]
