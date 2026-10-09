---
title: Sharp Football Analysis
type: entity
tags: [entity, tool, nfl, stats, dfs, betting, free-tier]
keywords: [sharp-football, proe, pass-rate-over-expected, stats-tools, epa, success-rate, expected-fantasy-points]
related:
  - entities/sports/nfl-betting.md
  - concepts/free-slate-context.md
  - concepts/daily-edge-card.md
  - concepts/team-volume-pace-model.md
  - concepts/implied-team-totals-dfs.md
  - entities/tools/ceminidfs.md
  - sources/rss-sharp-football-week4-2026-10-03-04.md
  - sources/daily-digest-batch-k181-2026-10-06.md
  - sources/rss-sharp-football-week5-worksheets-2026-10-07.md
  - sources/daily-digest-batch-k183-2026-10-09.md
maturity: draft
created: 2026-10-06
updated: 2026-10-09
---

## Relations

- @concepts/free-slate-context.md — free weather/venue context this complements
- @concepts/daily-edge-card.md — the operator's own free de-vig tool
- @concepts/team-volume-pace-model.md — PROE as a volume input
- @concepts/implied-team-totals-dfs.md — the ITT tool is in this directory
- @entities/sports/nfl-betting.md — W8 season lane
- @sources/rss-sharp-football-week4-2026-10-03-04.md — the seed batch

## Raw Concept

Free NFL advanced-stats and tooling hub (Warren Sharp / Rich Hribar). The **stats pages are free**; the weekly DFS, Worksheet, and Q&A columns are **paywalled**.

## Narrative

### Phase-0 verdict — GO (free tools only)

| Check | Result |
|-------|--------|
| **Cost** | The stats/tools directory is **free** and updated weekly. No account required to view the tool index |
| **Paywalled** | Weekly DFS stacks, core plays, tournament plays, The Worksheet, and the live Q&A sit behind an All-Access/Fantasy package. **Seven of nine pages** in the 2026-10-06 batch returned method only |
| **Method transparency** | PROE is published with its **definition and inputs** (down, distance, quarter, score difference). That is a reproducible spec, not a black box |
| **Posture** | Site states it "does not endorse, recommend or support illegal betting or gambling" and that content is "for entertainment purposes only" |
| **Overlap** | Complements `@concepts/free-slate-context.md` (Open-Meteo + MLB Stats + stadiums) and `@scripts/daily_edge_card.py`. No paid API needed for the free tier |
| **Verdict** | **CONDITIONAL-GO** — free tools usable in the research loop; **do not buy the DFS package** without a measured plan, since the operator already has CeminiDFS for projections |

### The free tool map

| Group | Tools | Use in this wiki |
|-------|-------|------------------|
| **Matchup** | Matchups · **Advanced Box Scores** (EPA + success rate) · **PROE** | Volume and efficiency context per game |
| **Offense** | Team Pace · Offensive Personnel · Offensive Line · Tendencies | Feeds `@concepts/team-volume-pace-model.md` and `@concepts/player-usage-models.md` |
| **Defense** | Defensive Stats · Defensive Line · **Coverage Schemes** · Coverage by Position | Dart opposing-look inputs (`@concepts/dfs-dart-opposing-looks.md`) |
| **Fantasy** | The Worksheet · **Expected Fantasy Points Tool** · Expected FP Allowed · **Implied Team Totals** | ITT cross-check against `@concepts/implied-team-totals-dfs.md` |
| **Betting** | Odds and Lines · Player Prop Odds · **Weather** · **Referee Assignments** · ATS Records | Weather + referee keys; referee data is rare elsewhere in this wiki |
| **Injury/schedule** | Practice Reports · IR Tracker · Strength of Schedule · Rest Disparity | Injury cadence (`@concepts/dfs-injury-and-news-workflow.md`) |

### Paywall rate is rising (K183, 2026-10-09)

Through three batches the pattern is stable and getting worse: **12 of 14 pages paywalled**. The weekly Worksheet columns consistently free only the **matchup data, team notes, and quarterback previews** before cutting off at the running-back section.

**What that still gives us:** the matchup table (spread, implied totals, per-team scoring, EPA, plays/game, rush/pass splits) and the **pressure-split QB profiles** — e.g. Darnold at **16.8 rating under pressure vs 138.0 clean**, Brissett at **38.2 pressured**. That split is a reusable check: a quarterback's value flips on the opponent's pressure rate.

**Decision point:** the free tier is the **stats directory** (PROE, ITT, coverage, referees). The columns deliver framing, not picks — weigh whether they are worth the ingest effort.

### PROE — the one to use

**Pass Rate Over Expected** = a team's dropback rate minus its expected dropback rate, derived from **down, distance, quarter, and score difference** on every play. Three tabs: Offense, Defense, and **Matchups** (offense vs defense, per week).

Read it as a **volume prior**, not an efficiency signal. It answers "will this offense throw more than the situation implies." The Matchups tab names the teams expected to throw most in a given week.

Worked example from the seed batch: Denver's PROE **fell from 4th (+5.5%) to 22nd (−1.3%)** under a new offensive coordinator — a coordinator change moved the volume profile.

### Referee data

The betting section carries **referee assignments** with penalty tendencies. The seed batch used one: a crew calling above-average offensive holding and false starts, **50%** of penalties, with **75%** of first/second-down penalties on offenses. Also recorded there: home underdogs **26-45-2 ATS (37%)** since 2016, and the key-number reminder that **~15%** of games end on a 3-point margin (keys: **3, 7, 10, 6, 8**).

### Stated research cadence

The site's own method matches this wiki's weekday rhythm:

1. **Early week** — advanced box scores + expected fantasy points.
2. **Mid-week** — implied team totals + weekly matchups, for DFS and props.
3. **Late week** — injury and weather tools to finalize.

## Snippets

> "PROE measures a team's dropback rate minus its expected dropback rate." [Source: @sources/rss-sharp-football-week4-2026-10-03-04.md]

## Dead Ends

- **Do not cite paywalled picks.** Seven of nine pages in the seed batch were behind the wall; only the method was public.
- **No CLV record on the free tier.** The best-bets and props pages are opinion columns, not a tracked ledger.
- **Do not buy the DFS package as a reflex.** The operator already generates projections via CeminiDFS (`@entities/tools/ceminidfs.md`). Compare the free tools against that output first.
