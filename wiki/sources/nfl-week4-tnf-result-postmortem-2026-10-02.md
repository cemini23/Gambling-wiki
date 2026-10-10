---
title: "TNF PIT @ CLE result + postmortem — goal-line inference fails (2026-10-02)"
type: source
tags: [source, nfl, week-4, postmortem, props, parlay, k180]
keywords: [warren, fannin, freiermuth, goal-line-rate, anytime-td, line-shopping, realized-result]
related:
  - sources/steelers-browns-tnf-metaplan-2026-10-01.md
  - sources/nfl-week4-slate-env-2026-10-02.md
  - entities/sports/nfl-betting.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/line-shopping-and-clv.md
  - concepts/daily-edge-card.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - sources/nfl-week4-result-postmortem-2026-10-09.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-09
phase_0_verdict: REFERENCE — realized result; three transferable rules
wire_status: policy_wired
---

## Relations

- @sources/steelers-browns-tnf-metaplan-2026-10-01.md — the card this grades
- @sources/nfl-week4-slate-env-2026-10-02.md — the Friday env doc already encodes lesson 1
- @concepts/parlay-and-correlated-bets.md — leg construction
- @concepts/line-shopping-and-clv.md — buying a number down
- @entities/sports/nfl-betting.md — W8 season lane
- @sources/nfl-week4-result-postmortem-2026-10-09.md — the Sunday packet's unread +230 and +929 headers are these two tickets

## Raw Concept

| Field | Value |
|-------|-------|
| **Game** | PIT @ CLE, 2026-10-01, Huntington Bank Field |
| **Final** | **PIT 24 — CLE 27** |
| **Tickets** | 2 × $5, entered in Hard Rock 2026-10-01 |
| **Result** | **Both lost. Cash −$10** |
| **Source** | Operator slips + `briefs/deep-research/2026-w04-tnf-card.md` |

## Narrative

### The two tickets

**T1 — +230, $5 stake, 10% profit boost.** Jaylen Warren rush_yds · Harold Fannin Jr. rec_yds · Pat Freiermuth rec_yds. Three legs, two markets.

| Leg | Line | Result |
|-----|------|--------|
| Warren rush_yds | over 70.5 | **93 — HIT** |
| Freiermuth rec_yds | over 14.5 | **17 — HIT** |
| Fannin rec_yds | over 34.5 | **27 — MISS** |

**T2 — +929, $5 stake, 10% profit boost.** Jaylen Warren anytime_td · Harold Fannin Jr. anytime_td · Pat Freiermuth rec_yds.

| Leg | Line | Result |
|-----|------|--------|
| Fannin anytime_td | over 0.5 | **1 — HIT** |
| Freiermuth rec_yds | over 19.5 | **17 — MISS** |
| Warren anytime_td | over 0.5 | **0 — MISS** |

The 10% boost paid nothing on either ticket, because there was no profit. The boost changes profit, not the grade price.

### Lesson 1 — a backfield vacancy is not goal-line work

The research treated **Rico Dowdle being OUT** as evidence that Warren inherited the goal-line role. He did not.

> Warren rushed for 93 yards and scored 0. The operator saw no goal-line touches. Those carries went to Wilson and a second back. The second name was not recorded.

**The rule:** an anytime-TD leg requires a **cited goal-line carry rate**. Do not infer it from the other back being out. The Friday environment doc independently reached the same rule and cited this exact game as the example — "backfield vacancies alone do not confer goal-line usage."

**Why the metaplan missed it:** it listed Warren as supported in `anytime_td` and `first_td` on the reasoning "Warren holds uncontested goal-line leverage with Rico Dowdle ruled out." That is the inference the rule now forbids. The rule appears in the source corpus; it was not applied to the leg.

### Lesson 2 — a line that opens in the 40s is a bar

Fannin's receiving total **opened in the 40s**. The operator bought it down to **34.5**. He finished at **27**.

> One good week is not enough for that number, and Watson plus Fannin were not enough for a tight-end over that high. A line that opens in the 40s is a bar. Buying it down does not fix the market.

**The rule:** when a tight-end receiving total opens at 40+, treat the opening number as the market's position, not as an error to be exploited. Buying down moves the price without changing the underlying distribution. See @concepts/line-shopping-and-clv.md — shopping is for the same number across venues, not for relocating a number on one venue.

### Lesson 3 — same player, two lines, two bets

Freiermuth finished with **17**. He cleared **14.5** and missed **19.5**.

**The rule:** two different totals on the same player in the same game are two different wagers with two different break-even points. Both tickets can be graded honestly and land on opposite sides. Do not treat one as a duplicate of the other, and do not size them as if they were the same position.

### What worked

The **market bar list** held. `pass_yds` was barred for both quarterbacks, and neither passing leg was needed. `rush_yds` on Warren was the one clean read: 93 against a Cleveland front allowing a league-worst 16.7% explosive-run rate. The **Fannin receiving** bar and the **Warren TD** bar were the failures, not the market selection.

## Snippets

> "The research treated Dowdle being out as Warren goal-line work. That is not goal-line use." [Source: operator note, 2026-10-02]

> "A line that opens in the 40s is a bar. Buying it down does not fix the market." [Source: same]

## Dead Ends

- **Do not re-derive goal-line usage from a depth chart.** Two tickets failed on one unfounded inference. Require the carry rate.
- **The second rusher is unnamed.** The operator saw carries go to "Wilson and a second back"; only the surname was recorded. Do not lock a first name — the hub brief flags this explicitly.
- **$10 is not a sample.** This page records a method failure, not a variance result. No bankroll conclusion follows from two tickets.
- **Same-game first_td stays prohibited** in multi-leg sets. Neither ticket carried one; keep it that way.
