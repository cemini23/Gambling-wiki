---
title: Brief K169 — NFL Week 1 ready (roster + RSS wire)
type: source
tags: [brief, k169, nfl, dfs, injury, rss]
keywords: [week-1, jacobs, parsons, charbonnet, tyson, donald, nacua, rotowire]
related:
  - meta/daily-research-digest-cadence.md
  - sources/brief-k168-nfl-season-paper-rss-2026-08-31.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
  - entities/sports/nfl-betting.md
  - concepts/dfs-injury-and-news-workflow.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - entities/platforms/fanduel.md
  - entities/platforms/hard-rock-bet.md
  - entities/platforms/underdog-fantasy.md
  - entities/tools/stokastic-dfs.md
  - sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md
maturity: validated
read_status: deep-read
created: 2026-08-31
updated: 2026-08-31
wire_status: policy_wired
cross-wiki-source: "briefs/2026-08-31_k169-nfl-week1-ready.md"
---

## Relations

- Gitignored brief: `briefs/2026-08-31_k169-nfl-week1-ready.md`
- Phase-1: `policy_wired` — RSS filters in `scripts/daily_research_config.yaml`. No scrape. No auto-bet.

## Raw Concept

K169 wires injury/roster RSS for in-season discovery and files the Week-0 53-man snapshot for Week 1 (kickoff **2026-09-09**).

**Dual-ID:** gambling digest K169 ≠ OSINT K169 (Jul 15 SLM harness steal). Resolve by file + date.

## Narrative

### RSS wire [CONFIRMED 2026-08-31 probe]

Added to the local digest (`rss.enabled: true`):

| Feed | Role |
|------|------|
| RotoWire NFL news | Practice / PUP / IR / 53-man |
| ProFootballRumors | Trades, waivers, exempt list |
| CBS NFL headlines | Roster/waiver trackers (filler rankings excluded) |
| PFF | NFL/Fantasy/DFS/Betting; CFB dropped |
| The Read Optional | Low-volume process (Baldwin) |
| DraftKings Playbook | NFL-only; tennis/MLB/soccer dropped |

PFT include-list now covers PUP, 53-man, waiver, exempt, practice. RotoBaller sleeper titles and Sharp ranking/projection trackers stay in the config as **discovery-only** (same K168 skip). RotoViz remains HTTP 403.

### Week-0 roster facts (cutdown 2026-08-30)

| Claim | Confidence | Source |
|-------|------------|--------|
| Jacobs on Commissioner’s Exempt; not on GB 53; cannot practice/attend games | [CONFIRMED] | [Source: https://www.espn.com/nfl/story/_/id/49774523/packers-rb-josh-jacobs-placed-commission-exempt-list (retrieved 2026-08-31)] |
| Packers traded for Kaleb Johnson; Lloyd + Brooks remain | [CONFIRMED] | same ESPN |
| Parsons Reserve/PUP; miss first 4; Week 6 vs DAL “realistic” | [CONFIRMED] | ESPN Jacobs piece + Schefter 2026-08-30 |
| Charbonnet reserve/PUP; miss first 4; Price likely lead vs NE 9/9 | [CONFIRMED] | [Source: https://www.nbcsports.com/fantasy/football/player-news/2026-08-30/charbonnet-placed-on-pup-to-start-season (retrieved 2026-08-31)] |
| Tyson IR-R hamstring; ≥4 games; ~2 months | [CONFIRMED] | [Source: https://www.rotowire.com/football/player/jordyn-tyson-19233 (retrieved 2026-08-31)] |
| Nacua groin; back at practice 8/30; Rams vs SF Melbourne 9/10 | [CONFIRMED] | [Source: https://www.rotowire.com/football/player/puka-nacua-16790 (retrieved 2026-08-31)] |
| Donald unretires; 1yr $20M (up to $30M); Week-1 snaps TBD | [CONFIRMED] | [Source: https://www.nfl.com/news/aaron-donald-unretires-rams-2026-season (retrieved 2026-08-31)] |
| Dexter CHI→ATL for Phillips + 5th | [CONFIRMED] | [Source: https://www.espn.com/nfl/story/_/id/49771892/sources-falcons-add-gervon-dexter-sr-trade-bears (retrieved 2026-08-31)] |
| Titans waive Will Levis | [CONFIRMED] | [Source: https://www.espn.com/nfl/story/_/id/49774800/titans-waive-former-starting-qb-levis (retrieved 2026-08-31)] |
| Kickoff Wed 2026-09-09 SEA vs NE | [CONFIRMED] | [Source: https://www.nfl.com/schedules/2026/by-week/week-1 (retrieved 2026-08-31)] |

### Operator steals

1. Do not price **Jacobs / Charbonnet / Tyson / Parsons** as Week-1 starters.
2. Nacua and Donald are **Melbourne TNF** questions — wait T-90 inactives.
3. GB rush and GB pass-rush scripts are **committee / depleted** through at least Week 4.
4. YouTube weekly pick shows: **skip**. GPP process stays `@sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md`. Stokastic = CSV export only.

## Dead Ends

- RotoViz / FTN / ETR / OddsJam / FanDuel research RSS — 403/404; no scrape
- DFS Army / Club Fantasy week tapes — pick shows, not methodology
- Stokastic HTML strategy guides — JS shells; use member CSV + existing wiki GPP playbook
