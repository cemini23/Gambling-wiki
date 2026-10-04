---
title: NFL weekly research input pipeline
type: concept
tags: [meta, nfl, research, pipeline, operator, ceminidfs, ceminiparlays]
keywords: [research-inputs, environment-csv, status-csv, coverage-report, soft-fade, dart-rule, premium-mode, gemini-retired]
related:
  - concepts/nfl-weekly-slate-hub-workflow.md
  - concepts/dfs-dart-opposing-looks.md
  - concepts/dfs-weather-adjustments.md
  - concepts/parlay-and-correlated-bets.md
  - entities/tools/ceminidfs.md
  - meta/nfl-gemini-weekday-prompt-addendum.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
---

## Relations

- @concepts/nfl-weekly-slate-hub-workflow.md — consumes the two generated files
- @concepts/dfs-weather-adjustments.md — roof enum and the market-by-market weather note
- @concepts/dfs-dart-opposing-looks.md — dart ceiling method
- @concepts/parlay-and-correlated-bets.md — parlay gates; the legs come from CeminiParlays
- @entities/tools/ceminidfs.md — home of the generator
- @meta/nfl-gemini-weekday-prompt-addendum.md — **RETIRED** 2026-10-04; kept for history only

## Raw Concept

Decision 2026-10-04: **remove Gemini from the weekly research process.** The tools consume fields, not prose.

Evidence and plan: `briefs/2026-10-04_w05-research-plan.md`. Defect list: `@osint-wiki`-side repo `CeminiDFS/briefs/2026-10-04_w04-build-postmortem.md`. Over-fade measurement: `CeminiDFS/briefs/handoffs/2026-10-04_k283-team-coverage-darts.md`. Market ordering: `CeminiDFS/briefs/handoffs/2026-10-03_k282-market-premium.md`.

## Narrative

### The contract — what the two tools read

Nothing else is consumed. No prose enters either tool.

**`environment.csv`** (CeminiParlays `--environment`) — 24 rows, one per team, 12 games:

```
slate_id, game_id, team, opp, implied_total, spread, roof, weather_exposed, wind_mph, precip_pop
```

**Status list** — two formats, one source:

- hard exclude (CeminiDFS `--research-csv`): `out, ir, inactive, doubtful, nfi, pup, suspended`
- warn: `q, questionable, gtd, game-time, limited, dnp`
- soft fade (K283): a team weight discount. **Never a removal.**

**ITT** — `spread` and `total` per game, from the Odds API `h2h,spreads,totals` fetch.

**Handoff** (CeminiDFS → CeminiParlays): `player, team, projection, lineup_exposure_pct, game, implied_total`. The `projection` column must be the model, never the market.

### Why Gemini was removed

1. **Prose does not compile into fields.** Each week a human re-derived `wind_mph`, `roof`, and `status` from a docx. Every re-derivation added a rule to the addendum. The file became a pile of "do not copy X" instructions — bloat, not learning.
2. **Field errors crossed sources.** A Grok packet tagged Lumen Field `Indoor` (it is open). The Friday hub had Nico Collins OUT on a DraftEdge-only cite; the Saturday club check cleared him.
3. **Assumption dressed as a finding.** The Week 4 postmortem claimed a team-code fault because Kenneth Walker III read as a Seahawk. nflverse play-by-play puts him on **KC** for weeks 1–3. The claim was closed as a false positive. K283's first measurement made the same error and counted non-slate teams (11/7/11 instead of 7/3/6).
4. **K283 measured the cost.** The prose layer hard-fades whole teams. In Week 3, **13 of 26** slate teams had zero book exposure, and **6** of those still produced an 18+ scorer.

### The pipeline

| Layer | Work | Owner |
|-------|------|-------|
| 0 | nflverse schedule/injuries/Vegas, NWS hourly, Odds API game markets, club pages | data sources |
| 1 | emit `environment.csv` and the status CSV | `ceminidfs research-export env` / `research-export status` |
| 2 | validation gate — every team code resolves; every game on the slate; every weather value carries URL + timestamp; no blank passes silently | `ceminidfs research-export validate` |
| 3 | optional read-only reviewer | **cannot write an input file** |

### Standing rules (carried from the retired addendum)

- **Hard exclude is OUT / IR / D only.** A Questionable player stays in the pool.
- **A team opinion is a soft fade, never a removal** (K283).
- FanDuel Sunday afternoon only (1 p.m. and 4 p.m.). SNF and MNF stay off the afternoon ticket.
- Cap a ticket at two legs of one market. `first_td` legs must be in different games. Same-game `first_td` is illegal.
- Wind of 10 mph or more on a `first_td` or `pass_yds` leg is a review note. The leg stays. Do not invent a new cutoff.
- A retractable roof stays weather-exposed until the official call. NRG stays exposed. SoFi is `semi_open`, not a dome.
- Tool order: CeminiDFS first, then CeminiParlays. The CLIs read nothing unless the operator passes the hub, the status CSV, the salary CSV, and the environment CSV.
- Grade uses the displayed American. A profit-boost percent is a note only.
- An anytime touchdown needs a cited goal-line rate. A tight-end line that opens in the 40s is a bar.
- Order the premium band by the market (`--premium-mode market`); the model covers the cheap roles (K282).

### Feedback loop

Run the K283 coverage report after the slate. Turn on `--keep-team-dart` and log how often it fires. A team that is faded and produces in three of four weeks is a research defect, not a bad break.

## Snippets

> "The book hard-faded whole teams. Week 3: 13 of 26 slate teams had zero exposure, and 6 still produced an 18+ scorer." [Source: CeminiDFS/briefs/handoffs/2026-10-04_k283-team-coverage-darts.md (retrieved 2026-10-04)] [CONFIRMED]

> "Salary wins all three weeks, and in week 2 the model is worse than random." [Source: CeminiDFS/briefs/handoffs/2026-10-03_k282-market-premium.md (retrieved 2026-10-04)] [CONFIRMED]

> "normalized FPPG == FanDuel raw FPPG: 531 / 531" [Source: CeminiDFS/briefs/2026-10-04_w04-build-postmortem.md (retrieved 2026-10-04)] [CONFIRMED]

> "nflverse pbp weeks 1–3: Kenneth Walker III rusher team = KC." [Source: CeminiDFS artifacts/cache/2026/week_4/pbp.parquet (retrieved 2026-10-04)] [CONFIRMED]

## Dead Ends

- **Gemini Deep Research weekday prompts** (Tue/Wed, Thu, Fri, Sat). Retired 2026-10-04. The output was prose that a human re-derived into fields, and each pass added a rule. Do not restart this cadence.
- **Team-code fault claim (Week 4 postmortem P2).** False positive. Verified against nflverse play-by-play.
