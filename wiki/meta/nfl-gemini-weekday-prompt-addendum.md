---
title: NFL Gemini weekday prompt addendum
type: concept
tags: [meta, nfl, gemini, prompt, weekly-prep, operator]
keywords: [gemini-prompt, tuesday, wednesday, thursday, friday, saturday, slate-hub, fanDuel, hard-rock]
related:
  - meta/research-input-pipeline.md
maturity: draft
created: 2026-09-22
updated: 2026-10-04
---

> **[RETIRED] 2026-10-04 — superseded by @meta/research-input-pipeline.md.**
> Gemini is removed from the weekly research process. The standing rules moved to
> the pipeline page. Keep this page for history only. Do not start a new Gemini
> weekday prompt.

## Relations

- @concepts/dfs-dart-opposing-looks.md — dart opposing-look method referenced in Wednesday block
- @concepts/nfl-weekly-slate-hub-workflow.md — hub workflow consumes these weekday blocks
- @concepts/dfs-weather-adjustments.md — Friday environment block references market-specific weather review
- @concepts/parlay-and-correlated-bets.md — Saturday parlay caps reference two legs of one market and no same-game first_td
- @entities/platforms/hard-rock-bet.md — Hard Rock lane uses the same compose gates

## Raw Concept

Standing blocks to paste into the next week's Gemini prompts. Do not rewrite the Week 2 docx prompts. Source: CeminiDFS and CeminiParlays Week 2 recap audits (2026-09-22). Commits already shipped: CeminiDFS d084f40 (lock-lineup join cannot break exposure cap), ec0d45f (scratch excludes already out of pool do not stop Sunday optimize), CeminiParlays e3abb49 (auto compose caps ticket at two legs of one market; wind ≥10 mph on first_td or pass_yds prints WEATHER_MARKET_REVIEW; leg stays; boost note does not change graded payout).

## Narrative

### Tuesday — injury and depth only

Injury and depth only. No box-score chase. Do not import last week's points into means or ceilings.

### Wednesday scheme — dart opposing-look block

Add a dart opposing-look block. For each Sunday-main game, name the cheap role and the opposing coverage or front. Cite the source. Write NO_EVIDENCE if you cannot cite. Do not invent PFF grades, snap rates, salaries, ownership, or a displayed American. Point at the dart concept page @concepts/dfs-dart-opposing-looks.md.

### Thursday — confirm role from practice report

Confirm the role (routes, targets, carries) if a practice report states it. Do not import last week's points.

### Friday environment — weather by market

One weather rule per flagged game, by market. A windy game can support a rush over and still bar a first_td. Do not invent a new mph cutoff. Do not scratch every player in that game. Retractable roofs stay exposed until the official call. SoFi stays semi_open and is not a wind fade.

Shipped behavior (commit e3abb49): wind of 10 mph or more on a first_td or pass_yds leg prints WEATHER_MARKET_REVIEW. The leg stays. It is not a new cutoff. Do not copy the Week 2 20 mph card into the rule.

### Saturday lock — FanDuel Sunday afternoon only

FanDuel Sunday afternoon only (1 p.m. and 4 p.m.). SNF and MNF stay off the afternoon parlay ticket.

Cap any recommended ticket at two legs of one market. First_td legs must be different games. Same-game first_td is illegal.

Questionable players stay. Do not retune means, stack badges, defense weights, or ownership from one Sunday.

Do not state a FanDuel net. Grade uses the displayed American. A profit-boost percent is a note only.

Tool order: CeminiDFS first, then CeminiParlays. The CLIs do not read Gemini unless the operator passes the hub, the scratch CSV, the salary CSV, and the environment CSV.

### Anytime touchdown and a moved receiving line (2026-10-02)

An anytime touchdown needs a cited goal-line rate. Another back being out is not that rate. PIT @ CLE: Warren rushed for 93 yards and scored 0. The goal-line carries went to Wilson and a second back. The second name was not recorded. The research had called the goal-line work uncontested because Dowdle was out.

A tight-end receiving line that opens in the 40s is a bar. Buying the number down does not fix it. Fannin opened in the 40s, the ticket used 34.5, and he finished at 27. One good week is not the sample. Do not ticket the over when the quarterback and the tight end are not enough for that number.

## Snippets

> "Do not retune means, stack badges, defense weights, or ownership from one Sunday." [Source: /Users/claudiobarone/Projects/CeminiDFS/reports/audit/free-w02-recap/SYNTHESIS.md p.159–161 (retrieved 2026-09-22)] [CONFIRMED]

> "Cap a ticket at two legs of one market. Evidence: five rush overs, 2 of 5." [Source: /Users/claudiobarone/Projects/CeminiParlays/reports/audit/free-w02-recap/SYNTHESIS.md p.128 (retrieved 2026-09-22)] [CONFIRMED]

> "Wind of 10 mph or more on a first_td or pass_yds leg prints WEATHER_MARKET_REVIEW. The leg stays." [Source: same file p.127, p.58 (retrieved 2026-09-22)] [CONFIRMED]

> "SoFi stays semi_open and is not a wind fade." [Source: same file p.58; @concepts/dfs-weather-adjustments.md p.64] [CONFIRMED]

> "Keep SNF legs off afternoon tickets. Evidence: the $27 Mahomes + Lamar slip." [Source: same file p.126 (retrieved 2026-09-22)] [CONFIRMED]

> "Questionable players stay. Zero a ceiling only when the player is inactive." [Source: CeminiDFS synthesis p.49; CeminiParlays synthesis p.64 (retrieved 2026-09-22)] [CONFIRMED]

> "Tool order: CeminiDFS first, then CeminiParlays. The CLIs do not read Gemini unless the operator passes the hub, the scratch CSV, the salary CSV, and the environment CSV." [Source: operator workflow; CeminiParlays synthesis p.63 (retrieved 2026-09-22)] [CONFIRMED]