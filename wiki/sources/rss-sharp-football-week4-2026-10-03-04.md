---
title: "Sharp Football Week 4 — PROE rankings, free stats tools, best bets, props (2026-10-03/04)"
type: source
tags: [source, rss, nfl, week-4, dfs, props, tooling, k181]
keywords: [proe, pass-rate-over-expected, stats-tools, shepardson, bo-nix, kittle, rashee-rice, paywall]
related:
  - entities/sports/nfl-betting.md
  - entities/tools/sharp-football-analysis.md
  - concepts/team-volume-pace-model.md
  - concepts/daily-edge-card.md
  - sources/daily-digest-batch-k181-2026-10-06.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/
phase_0_verdict: MIXED — 2 pages free (GO for tooling), 7 paywalled (stub + method only)
wire_status: policy_wired
---

## Relations

- @entities/tools/sharp-football-analysis.md — the free-tools directory, seeded here
- @entities/sports/nfl-betting.md — W8 season lane
- @concepts/team-volume-pace-model.md — PROE as a volume input
- @concepts/daily-edge-card.md — free de-vig tooling this complements
- @sources/daily-digest-batch-k181-2026-10-06.md — K181 batch hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Feed** | Sharp Football Analysis (`sharp-football`) |
| **Published** | 2026-10-03 → 2026-10-04 |
| **Articles** | 9 — **2 free, 7 paywalled** |
| **Site posture** | "does not endorse, recommend or support illegal betting"; "for entertainment purposes only" |

**Location** (`cemini-egress-fi:/opt/cemini-bulk/research/gambling/`): the 9 archived `rss-sharp-football-2026-10-0{3,4}-*.md` files.

**Article URLs** (required for batch pages — `preingest_check.py` matches on these):
https://www.sharpfootballanalysis.com/stats-nfl/nfl-pass-rate-over-expected/
https://www.sharpfootballanalysis.com/stats-nfl/nfl-stats-tools/
https://www.sharpfootballanalysis.com/fantasy/dfs-stacks-week-4-2026/
https://www.sharpfootballanalysis.com/fantasy/core-dfs-picks-week-4-2026/
https://www.sharpfootballanalysis.com/fantasy/tournament-dfs-picks-week-4-2026/
https://www.sharpfootballanalysis.com/fantasy/the-worksheet/
https://www.sharpfootballanalysis.com/betting/nfl-odds-picks-predictions/
https://www.sharpfootballanalysis.com/betting/nfl-player-props-odds-picks-predictions/
https://www.sharpfootballanalysis.com/fantasy/fantasy-football-live-q-and-a-rich-hribar/

| # | Article | Access |
|---|---------|--------|
| 1 | NFL Pass Rate Over Expected rankings | **FREE** |
| 2 | NFL advanced stats / free stats tools | **FREE** |
| 3 | Week 4 DFS — best game and team stacks | paywalled |
| 4 | Week 4 DFS — core players | paywalled |
| 5 | Week 4 DFS — tournament plays | paywalled |
| 6 | The Worksheet — Week 4 game previews | paywalled |
| 7 | Week 4 NFL odds picks, lines, best bets | **FREE** |
| 8 | Week 4 NFL player prop odds picks | **FREE** |
| 9 | Live Week 4 Q&A with Rich Hribar | paywalled |

## Narrative

### PROE — pass rate over expected (free)

**Definition:** a team's dropback rate minus its expected dropback rate, computed from **down, distance, quarter, and score difference** for every play. Three tabs: Offense (how often a team passes vs expectation), Defense (how often opponents pass vs expectation), and **Matchups** (each offense vs each defense, per week). Filterable by season, quarter, and down.

2026 leaders:

| | Most pass-heavy | Most run-heavy |
|---|-----------------|----------------|
| 1 | Dallas Cowboys | Atlanta Falcons |
| 2 | Pittsburgh Steelers | Minnesota Vikings |
| 3 | Carolina Panthers | New York Giants |
| 4 | Cincinnati Bengals | Miami Dolphins |
| 5 | Kansas City Chiefs | Baltimore Ravens |

**Why it matters to this wiki:** PROE is a **volume input**, not an efficiency input. It answers "will this offense throw more than the situation implies" — which pairs with `@concepts/team-volume-pace-model.md` (plays, pace, pass/run split) and feeds the dart-opposing-look method. The Matchups tab is the actionable layer: it names the teams expected to throw most in a given week. Note the article's own caveat — it carries no salaries or lines.

The prop desk used it directly: Denver's PROE **fell from 4th (+5.5%) to 22nd (−1.3%)** under new OC Davis Webb, which anchors the Bo Nix Under below.

### Free stats tools — the directory (free)

A hub of free NFL advanced-stats tools, updated weekly. Worth recording as the wiki's free-context toolkit alongside `@concepts/free-slate-context.md` (weather/venue) and `@scripts/daily_edge_card.py` (de-vig).

| Group | Tools |
|-------|-------|
| **Matchup** | Matchups · Advanced Box Scores (EPA + success rate per game) · **Pass Rate Over Expected** |
| **Offense** | Team Pace · Offensive Personnel · Offensive Stats · Offensive Line · Offensive Tendencies |
| **Defense** | Defensive Stats · Defensive Line · Defensive Tendencies · Coverage Schemes · Coverage Stats by Position |
| **Fantasy** | The Worksheet · **Expected Fantasy Points Tool** · Expected Fantasy Points Allowed · **Implied Team Totals** |
| **Betting** | NFL Odds and Lines · Player Prop Odds · **Weather Forecast** · Referee Assignments · ATS Records · Head Coach ATS Records |
| **Injury/schedule** | Free Agents · Practice Reports · IR Tracker · Strength of Schedule · Schedule Rest Disparity · Schedule Grid |

**Stated method:** early week, advanced box scores + expected fantasy points; mid-week, implied team totals + weekly matchups for DFS and props; late week, injury and weather tools to finalize. That is a **cadence**, and it matches this wiki's own weekday rhythm.

### Best bets (free) — Shepardson, Week 4

| Pick | Reasoning |
|------|-----------|
| **GB @ TB Under 38.5** | Green Bay's offensive line "was already a question mark entering the season, but injuries have turned it into a roaring tire fire." Last in ESPN pass-block win rate, 19th in run-block win rate. Love: **103.6 rating on 81 unpressured dropbacks vs 45.8 on 51 pressured**. Bowles blitzes 5th-most (42.5%). Tampa Bay starts rookie UDFA QB (59.3% college completion) |
| **MIA @ MIN Under 39** | Pairs the MIA @ MIN card in @sources/rss-lsb-week4-game-cards-2026-10-02.md |

Also: **Joe Gibbs' referee analysis** for LAR @ PHI — Craig Wrolstad's crew calls above-average offensive holding and false starts (**50% of penalties**), with **75%** of first/second-down penalties falling on offenses. Home underdogs are **26-45-2 ATS (37%)** since 2016. And the key-number reminder: ~15% of games end on a 3-point margin; key numbers are **3, 7, 10, 6, 8**.

### Prop picks (free)

| Pick | Reasoning |
|------|-----------|
| **Bo Nix Under 225.5 passing (−112)** | Denver's PROE dropped 4th → 22nd under new OC Davis Webb. Nix averages only **195.2 passing yards in 19 career road starts**, clearing 225.5 in **4** of them. San Francisco allows 215 passing yards/game with an NFL-low **−8.2% PROE** |
| **George Kittle Over 64.5 receiving (−113)** | — |
| **Rashee Rice Over 55.5 receiving (−114)** | — |
| Curtis Hirsch leaders | Burrow +900 most passing yards · Chase +1100 most receiving · Aaron Jones +1900 most rushing |
| Touchdowns | Drake London +1100 first TD (Falcons-Saints) · Juwan Johnson +230 anytime TD (team-high red-zone targets; Atlanta struggles covering TEs) |

### Paywalled — method only

Four DFS/worksheet/Q&A pieces cut off at the first heading. What is public:

- **DFS stacks:** Hribar favours small-field tournaments (**single-to-five-max entry, 5K or smaller fields**), uses **full-game stacks**, accepts frequent losses because one win over 18 weeks can pay for the year, targets games with a **wider range of outcomes**, and is willing to use chalky stacks because fewer entries let him go **deeper into the game stack** than opponents.
- **Core plays:** the players he will "have the most exposure to at their respective positions" — usable in cash and tournaments.
- **Tournament plays:** labelled for risk, but "if a player here fits your team structure in cash games around your primary core, use them." Aimed at being ahead of projected roster percentages.
- **The Worksheet:** game previews are on per-matchup pages. Public framing only — Week 3 scoring rebounded to **23.0 ppg** (from 19.7), sack rate a season-low **5.6%**, third-down a season-high **41.7%**, passing a season-high **226.6 yards**; penalties elevated at **7.4/game** with **2.1 automatic first downs/game**.

## Snippets

> "Green Bay's offensive line was already a question mark entering the season, but injuries have turned it into a roaring tire fire." [Source: Sharp Football best bets, 2026-10-04]

> "Being labeled a tournament play doesn't mean avoiding them in cash games. If a player here fits your team structure in cash games around your primary core, use them." [Source: Sharp Football tournament plays, 2026-10-03]

## Dead Ends

- **Seven of nine pages are paywalled.** Only the PROE rankings, the stats-tools directory, the best bets, and the prop picks have usable bodies. Do not cite DFS selections that are behind the wall.
- **The DFS method is the transferable part, not the picks.** Small-field, full-game-stack, deeper-than-opponents is a coherent tournament posture; treat it as a hypothesis to test against the operator's own results.
- **"Entertainment purposes only"** is the site's own framing. Nothing here is a CLV record.
- Do not auto-enter.
