---
title: "Steelers @ Browns TNF metaplan — market support and bar list (2026-10-01)"
type: source
tags: [source, nfl, week-4, tnf, props, parlay, k180]
keywords: [warren-bellcow, fannin, judkins, rodgers, watson, market-support, anytime-td]
related:
  - entities/sports/nfl-betting.md
  - sources/nfl-week4-research-plan-2026-10-01.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/free-slate-context.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/Steelers Browns Research Metaplan.docx
phase_0_verdict: REFERENCE — single-game prop card; no auto-enter
wire_status: policy_wired
---

## Relations

- @entities/sports/nfl-betting.md — W8 season lane
- @concepts/parlay-and-correlated-bets.md — leg limits + correlation
- @entities/platforms/hard-rock-bet.md — operator ticket surface
- @sources/nfl-week4-tnf-result-postmortem-2026-10-02.md — **result: both tickets lost; the goal-line inference failed**
- Gitignored card: `briefs/deep-research/2026-w04-tnf-card.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `Steelers Browns Research Metaplan.docx` |
| **sha256** | `9e8be21e311eb726…` |
| **Game** | PIT @ CLE, 2026-10-01 20:15 ET, Huntington Bank Field |
| **Market** | PIT −2.5, total 38.5 |

## Narrative

### Personnel

| Player | Team | Status | Implication |
|--------|------|--------|-------------|
| **Rico Dowdle** | PIT | OUT (toe) | **Jaylen Warren bellcow** |
| Joey Porter Jr. | PIT | OUT | Traded to Dallas |
| Jalen Ramsey | PIT | Questionable (broken wrist) | Game-time cast test |
| Brandin Echols | PIT | Cleared (concussion) | Available |
| **Teven Jenkins** | CLE | OUT (back) | Interior guard void |
| **Elgton Jenkins** | CLE | OUT (concussion) | **Luke Wypler** starts at center |
| Tylan Wallace | CLE | OUT (knee) | Snaps to rookie WRs |
| Dylan Sampson | CLE | IR (knee) | Judkins owns volume |
| Kendrick Green | CLE | Released (injury settlement) | Not on tonight's roster |

Confirmed starters: **Aaron Rodgers** (PIT), **Deshaun Watson** (CLE).

### Advanced metrics — three-game sample

| QB | Att | Cmp% | Yds | TD | INT | Rating | CPOE | AGG% | TTT |
|----|-----|------|-----|----|-----|--------|------|------|-----|
| Rodgers | 113 | 58.4% | 700 | 4 | 2 | 81.0 | −2.0% | 14.2% | 2.89s |
| Watson | 82 | 68.3% | 587 | 5 | 1 | 104.1 | −3.8% / +0.3% | 12.2% | 2.91s |

Watson adds **24 carries for 105 yards** (14% designed QB run share, 12% scramble rate).

### Backfield

| Rusher | Team | Carries | Yards | YPC | TD |
|--------|------|---------|-------|-----|-----|
| **Jaylen Warren** | PIT | 38 | 216 | 5.68 | 0 |
| Quinshon Judkins | CLE | 42 | 124 | 2.95 | 0 |

Warren: 10/46 → 11/43 → 17/127, with a **91.5% snap share** in Week 3. Judkins: 12/33 → 12/21 → 18/70, **62% rush share**, **84.1% of yardage after first contact**.

### Scheme

**Pittsburgh** passes on **60.0% of first downs** (NFL high) and 64.7% overall, but uses pre-snap motion on only **52.1%** (NFL low). Target split is extreme: **5.9 yards per attempt to WRs** (NFL low) vs **8.8 to TEs** (4th). Metcalf runs a 100% route rate at a 22% target share but coverage forces checkdowns to Freiermuth and Washington. Warren ran routes on **68%** of dropbacks in Week 3.

**Cleveland** leans play-action (30.1%, 7th) with a shallow aDOT of **6.2 yards**. Target concentration: **53 of 82 targets (64.6%)** go to Fannin, Boston, and Concepcion. The run game is broken — **0.6 yards before contact per carry, NFL worst** — behind a line missing both Jenkins.

### Market support / bar list

| Market | Supported | Barred |
|--------|-----------|--------|
| **pass_yds** | — | **Rodgers, Watson** — CLE nickel 85.9% caps vertical; PIT 11.8% sack rate + CLE interior losses + 21 mph gusts |
| **rush_yds** | **Jaylen Warren** | Quinshon Judkins — 0.6 YBC; PIT penetrates on 52.1% of designed runs |
| **rec_yds** | **Harold Fannin Jr., Pat Freiermuth** | DK Metcalf (targets 10→9→5; 2.1 yd separation), Jerry Jeudy (target displaced) |
| **anytime_td** | **Jaylen Warren, Harold Fannin Jr.** | Judkins (0 TD, CLE converts 37.5% of red-zone visits), Rodgers, Watson |
| **first_td** | **Jaylen Warren** | All others — multiple first-TD picks in one game are prohibited |

Operator constraints echoed in the doc: **no more than two legs from any single market**; a three-leg ticket must combine distinct markets; same-game first-TD selections cannot be paired.

### Environment

Open air on Lake Erie. 75–78°F, mostly cloudy, **8–10 mph SSW with gusts 17–21 mph**, 0–10% precipitation. Above 8–11 mph at an open-air lakefront venue, passes beyond 15 air yards and kicks outside 45 yards take friction; sub-12 mph leaves interior rushing structurally insulated.

## Snippets

> "Anytime touchdown leans require an empirically cited goal-line carry rate, given that backfield vacancies alone do not confer goal-line usage." [Source: Steelers Browns Research Metaplan.docx]

> "Cleveland averages an NFL-worst 0.6 yards before contact per carry." [Source: same]

## Dead Ends

- **Three-game sample.** The document warns these figures cover fewer than 115 dropbacks and 50 carries per side. Not predictive.
- **NO_EVIDENCE rows are real.** Catch Score, CROE, Cushion, Closing Speed, and YACOE are unlisted publicly for 2026 for every pass catcher but Metcalf's separation.
- **This game is excluded from the FanDuel Sunday main slate.** Do not merge these legs into a main-slate build.
- No auto-enter. A human types the ticket.
