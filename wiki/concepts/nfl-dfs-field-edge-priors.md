---
title: NFL DFS field edge and rookie priors
type: concept
tags: [concept, dfs, nfl, projections, rookies, parlays]
keywords: [cpoe, csoe, air-yards, goal-line, dominator, yprr, wind, closing-line]
related:
  - concepts/dfs-stat-projection-engine.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-weather-adjustments.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/player-usage-models.md
  - concepts/team-volume-pace-model.md
  - concepts/implied-team-totals-dfs.md
maturity: draft
created: 2026-09-27
updated: 2026-09-27
---

## Relations

- @concepts/dfs-stat-projection-engine.md — volume times efficiency is the mean; CPOE only bends it
- @concepts/diy-nfl-dfs-model-architecture.md — pipeline hub
- @concepts/dfs-weather-adjustments.md — outdoor wind; indoor roofs stay flat
- @concepts/parlay-and-correlated-bets.md — closing spread and total, not a CPOE rank
- @concepts/player-usage-models.md — target share, air yards, WOPR
- @concepts/team-volume-pace-model.md — pace and pass rate
- @concepts/implied-team-totals-dfs.md — schedule total
- @osint-wiki/concepts/k274-gambling-pm-wave.md — K274 FILE hub; no clone

## Raw Concept

Synthesis from the 2026-09-27 K274 sports pass, three model scans, DeepSeek, Hunyuan (`tencent/hy3`), an OpenRouter free pass, and an OpenCLI read of Reddit, X, and YouTube. DFS here is a contest against other entries. A sportsbook hold is a different problem.

## Narrative

### What moves fantasy points

Completion percentage over expected is a style flag. It does not set the fantasy-point mean. A public 4for4 study of quarterback stats from 2018–2023, correlated with next-season fantasy points, ranks the inputs this way. These are community correlations. They are not coefficients.

| Input | Correlation with next-season fantasy points |
|-------|-----------------------------------------------|
| Fantasy points per dropback | 0.59 |
| Fantasy points per game | 0.54 |
| Rush attempts per game | 0.47 |
| Rush yards per game | 0.47 |
| Rush touchdowns per game | 0.40 |
| Pass touchdown rate | 0.35 |
| EPA per dropback | 0.33 |
| Yards per attempt | 0.28 |
| Time to throw | 0.24 |
| Average depth of target | 0.19 |
| CPOE | 0.13 |
| Completion percentage | 0.11 |
| Pass yards per game | 0.10 |

nfelo’s year-over-year figure for CPOE (RSQ 0.226) predicts future CPOE. It does not predict fantasy points. Closing speed has no public fantasy-points test. Separation and cushion repeat year to year and still show weak or negative same-season fantasy correlations in the 4for4 Next Gen Stats write-up. [TENTATIVE]

The stats that move a lineup against the field, and that already sit in nflverse schedules, play-by-play, and player stats:

1. Volume: targets, carries, routes, and snap share.
2. Air yards, air-yards share, and WOPR.
3. Red-zone share (yardline_100 at or under 20) and goal-line share (yardline_100 at or under 5).
4. Implied team total from the schedule total.
5. Neutral-script pace.
6. Outdoor wind on passing and kicking. Indoor and closed roofs stay flat.

Public Next Gen Stats columns worth a small residual, after volume is in the model, are average intended air yards, average time to throw, and yards after catch over expectation. Route-participation rate and pass-block win rate are not a free true source.

### What CeminiDFS already computes

`usage.py` already has target share, air yards share, and WOPR. `volume.py` already has pace, implied team total, quarterback rush attempts, and a pass-rate cut when wind is at least 10 mph. `coherence_risk.py` already adjusts team red-zone play-call inside the 20. `stadiums.py` already has roof type. A single `player_projection_base.parquet` already exists. `pipeline/sdv_benchmark.py` can already read one nflverse release parquet.

Still missing, and left at a live coefficient of zero until a fixture proves the column:

- Season and week partitions for our own projection rows.
- A stored CPOE or average-separation column. Do not paste the 4for4 table as a weight.
- Player goal-line carry share and target share.
- A passing-yards mean haircut outdoors, on top of the pass-rate cut that already exists. Do not add a second pass-rate penalty.
- A rookie prior module.

### Rookie prior for next year

Fit this on our own history, with draft capital in the model. Do not import a published correlation as a multiplier.

Use dominator rating, breakout age (age at the first season with dominator at or above 20 percent), and career yards per route run. Fantasy Points reported college YPRR to NFL rookie YPRR at about r = 0.26 for 84 wide receivers since 2014. Final-season YPRR was about r = 0.08, so the career number is the prior. [TENTATIVE] Targets per route run and career adjusted yards per team pass attempt are the same family. College target share mostly repeats dominator.

Leave wide-receiver forty times out. Public samples put that correlation near zero. Tight-end forty time is the Combine drill with more signal. Leave CFL production out. No pass in this run found a published CFL-to-NFL fantasy-points study.

College rows come from `cfbfastR` or `cfbd` loaders, plus nflverse combine and rosters. The multi-GB college dumps stay on GitHub. The useful shape is a thin client that reads one season parquet from a release tag. `nflverse/nflreadpy` and `nflverse/nflverse-data` are that shape. Copy the loader. Leave the data repos uncloned.

### Socials on 2026-09-27

OpenCLI reads of Reddit, X, and YouTube did not produce a new formula.

X posts about CPOE are MVP ranks. That is the public narrative. Do not copy that rank into the mean. An X search for “closing speed” returned athletic highlight clips, not the projection stat. Do not add that name to a game total.

X yards-per-route-run posts are same-season leaderboards. Those are weekly ranks. The rookie prior uses career college yards per route run.

Reddit r/DynastyFF “Follow the Volume” matches target share, air yards, and pace. Those already live in the model. Peter Howard’s video defines college dominator and breakout age as linked market-share stats: https://www.youtube.com/watch?v=jqGiYZl0w18. The auto-captions are messy. Do not transcribe a formula from them.

YouTube DFS results were weekly pick shows, a FantasyLabs air-yards explainer, and a SaberSim “Adjusting Projections” video. Air yards are already in the model. Do not copy a paid sim.

The only CFL Reddit hit was a low-score “CFL Fantasy?” post. A low-score DynastyFF metrics promo listed RAS and target vacancies, and the comments called the post generated. Neither becomes a feature.

### Parlays

The calibration table is historical closing spread and closing total, keyed by season, week, and game. Live prices stay typed. Wind on an outdoor total already belongs in `weather.py`. Indoor and closed retractable roofs get no discount. Do not add CPOE, EPA, or closing speed to the total.

### Paste prompts

These prompts are the build slice. They were not run from the OSINT session.

- CeminiDFS, route hard: `/Users/claudiobarone/Projects/CeminiDFS/prompts/2026-09-27_k274-parquet-csoe-wind.md`
- CeminiParlays, route mid: `/Users/claudiobarone/Projects/CeminiParlays/prompts/2026-09-27_k274-closing-lines-wind.md`

A human still types the FanDuel or Hard Rock ticket. No book scrape. No recruit scrape. No auto-submit.

## Snippets

> Trust volume to drive the projection; let efficiency only bend it.

That line is already the stat-engine rule. This page applies it to CPOE. [Source: concepts/dfs-stat-projection-engine.md]

## Dead Ends

- Closing speed as a fantasy-point lever. No public test. X uses the same words for highlight clips.
- CFL production as an NFL fantasy feature. No published translation in this pass.
- Wide-receiver forty time and RAS as rookie features.
- Cloning nflverse data dumps, cfbfastR data dumps, or the closing-speed notebook.
