---
title: DFS dart opposing looks
type: concept
tags: [concept, dfs, nfl, dart, opposing-look, fanDuel, weekly-prep]
keywords: [dart, ceiling, cheap-player, salary-cut, opposing-coverage, box-count, pre-lock-usage, exposure-cap]
related:
  - concepts/nfl-weekly-slate-hub-workflow.md
  - meta/nfl-gemini-weekday-prompt-addendum.md
maturity: draft
created: 2026-09-22
updated: 2026-09-22
---

## Relations

- @concepts/nfl-weekly-slate-hub-workflow.md — weekly hub references this method for Wednesday scheme and Thursday practice
- @meta/nfl-gemini-weekday-prompt-addendum.md — Wednesday block asks for dart opposing look by role; Friday block is weather by market; Saturday block caps parlay legs and forbids retunes

## Raw Concept

DFS Week 2 recap audit (2026-09-22). Two synthesis files: CeminiDFS `reports/audit/free-w02-recap/SYNTHESIS.md` and CeminiParlays `reports/audit/free-w02-recap/SYNTHESIS.md`. Both retrieved 2026-09-22. The audit found that the shrunk mean inside the p85 ranker cannot see a cheap boom, the 3-of-15 exposure cap broke when a later lock file joined, and no player-level actuals exist. This page records the research method for dart selection going forward. It is not a stack badge. It is not a one-week Purdy, Patriots, or Titans prior.

## Narrative

### Dart definition

A dart is a FanDuel player at salary at or below $5,500. A $5,900 player is outside that cut. [CONFIRMED] [Source: /Users/claudiobarone/Projects/CeminiDFS/reports/audit/free-w02-recap/SYNTHESIS.md p.46 (retrieved 2026-09-22)]

Do not name any other salary threshold for the dart rule. Coker at $5,900 is excluded from the dart ceiling channel. [CONFIRMED] [Source: same file p.46]

### Pre-lock role screen

Screen the dart on the role known before lock: routes, targets (target share), carries, and red-zone use. [CONFIRMED] [Source: same file p.204 (step 1), p.193 (step 5)]

Do not copy last week's box score into the mean or the ceiling. [CONFIRMED] [Source: same file p.45, p.197, p.200]

### Opposing look screen

Then screen the opposing look for that role: coverage (man, zone, two-high, single-high), box count, and pressure. Match the look to the role. A receiver look is not a running-back look. This is the 2026-09-22 operator method. The FanDuel synthesis does not state this step explicitly.

Rank a ceiling from that pre-lock usage. Keep the shrunk mean for the cash number. Do not rank the dart on the shrunk mean alone. [CONFIRMED] [Source: same file p.156 (fix 1), p.193–200]

### Mixture constant

Do not pick a mixture constant. `k/3` (OpenCode) and mass `0.15` (Grok) stay unshipped until a past-slate test. [TENTATIVE — one auditor each] [Source: same file p.71 (Grok mass 0.15), p.97 (OpenCode k/3), p.200 (do not pick), p.123 (conflict table)]

### Lineup total vs seat score

A lineup total is not a seat score. Do not name a boom or a bust from a History total. [CONFIRMED] [Source: same file p.37, p.51, p.141, p.214, p.218; CeminiParlays synthesis p.48–51, p.69–80]

Price, Helm, Warren, and Williams stay unresolved on a last name only. Do not assign the L02–L04 gap to a Williams. [CONFIRMED] [Source: same file p.135–146 (name map table); CeminiParlays synthesis p.66–68]

### Questionable and inactive

Questionable players stay in the pool. Zero a ceiling only when the player is inactive. [CONFIRMED] [Source: CeminiDFS synthesis p.49 (TG05), p.237; CeminiParlays synthesis p.64 (capture rule)]

### Seat actuals before KPI

Seat actuals must exist before a dart KPI. The audit names the fields: player id, salary, lineup id, projected, actual, delta. Do not fill those fields. [CONFIRMED] [Source: CeminiParlays synthesis p.66 (capture fields), p.89 (seat_actuals_complete), p.131 (fix 3)]

### Exposure cap includes later lock file

The exposure cap includes a later lock file. Do not freeze "3 of 15" as the rule for every future slate. [CONFIRMED] [Source: CeminiDFS synthesis p.57–61 (exposure check), p.157 (fix 2), p.179, p.240]

### No one-week retunes

No one-week stack badge. No one-week defense boost. No Purdy prior. [CONFIRMED] [Source: CeminiDFS synthesis p.51 (TG01, TG02, TG03), p.159–161 (fix 4, fix 5), p.233–236]

## Snippets

> "Keep the shrunk mean for the cash / median number. Do not copy Week 1 points into that mean." [Source: /Users/claudiobarone/Projects/CeminiDFS/reports/audit/free-w02-recap/SYNTHESIS.md p.45 (retrieved 2026-09-22)] [CONFIRMED]

> "Screen darts on a ceiling built from pre-lock usage (routes, targets, carries). Do not screen on last week's box score." [Source: same file p.204 (retrieved 2026-09-22)] [CONFIRMED]

> "Do not pick a mixture constant. k/3 and mass 0.15 stay unshipped until a past-slate test." [Source: same file p.200 (retrieved 2026-09-22)] [TENTATIVE]

> "A lineup total is not a seat score. Do not name a boom or a bust from a History total." [Source: same file p.37 (retrieved 2026-09-22)] [CONFIRMED]

> "Questionable players stay in the pool. Zero a ceiling only when the player is inactive." [Source: same file p.49 (retrieved 2026-09-22)] [CONFIRMED]

> "The exposure cap includes a later lock file. Do not freeze 3 of 15 as the rule for every future slate." [Source: same file p.157 (retrieved 2026-09-22)] [CONFIRMED]

> "Keep grade input as the displayed American. Store the 25% and 50% notes as notes only. Keep SNF legs off afternoon tickets. Cap same-market legs." [Source: /Users/claudiobarone/Projects/CeminiParlays/reports/audit/free-w02-recap/SYNTHESIS.md p.55–58 (retrieved 2026-09-22)] [CONFIRMED]

## Dead Ends

- Copying Week 1 points into the dart mean (lifts Vele and Antonio Williams, cuts Concepcion — one-week chase) [RETRACTED]
- Naming a boom from a lineup total without seat actuals [RETRACTED]
- Locking a stack rule from one Sunday (TG01) [RETRACTED]
- Boosting Patriots or Titans defense from one Sunday (TG03) [RETRACTED]
- Fading from the softmax ownership heuristic (TG04) [RETRACTED]