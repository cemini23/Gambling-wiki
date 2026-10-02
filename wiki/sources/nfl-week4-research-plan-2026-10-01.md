---
title: "NFL Week 4 research plan — injury ledger + 13-game scheme card (2026-10-01)"
type: source
tags: [source, nfl, week-4, injury, dfs, k180]
keywords: [dart-ir, mcmillan-ir, mayfield-out, jefferson-ankle, daniels-elbow, warren-bellcow, scheme-card]
related:
  - entities/sports/nfl-betting.md
  - sources/nfl-week4-practice-reports-2026-10-01.md
  - sources/nfl-week4-slate-env-2026-10-02.md
  - sources/steelers-browns-tnf-metaplan-2026-10-01.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - concepts/dfs-injury-and-news-workflow.md
  - concepts/dfs-dart-opposing-looks.md
  - meta/nfl-gemini-weekday-prompt-addendum.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Week 4 Research Plan.docx
phase_0_verdict: REFERENCE — Gemini Deep Research; Thu baseline, verify Fri designations
wire_status: policy_wired
---

## Relations

- @entities/sports/nfl-betting.md — W8 season lane
- @concepts/dfs-injury-and-news-workflow.md — Q/D/O + late swap
- @concepts/dfs-dart-opposing-looks.md — dart / opposing-look method
- @meta/nfl-gemini-weekday-prompt-addendum.md — standing weekday blocks; no one-week retunes
- Gitignored hub: `briefs/2026-w04-slate-hub-sun.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Week 4 Research Plan.docx` |
| **sha256** | `d2d0cfa3bb96b71c…` |
| **Type** | Gemini Deep Research — Part A injury ledger + Part B 13-game scheme card |
| **Captured** | 2026-10-01 baseline |

## Narrative — Part A: injury ledger

### Scratch list (OUT / IR — never on a ticket)

| Player | Team | Status |
|--------|------|--------|
| Jaxson Dart | NYG | IR — season-ending knee (meniscus/MCL/PCL; surgery 2026-09-25) |
| Jalen McMillan | TB | IR — PCL sprain; 6–8 week window |
| Baker Mayfield | TB | OUT — dislocated right thumb |
| Michael Onwenu | NE | IR |
| A.J. Brown | NE | IR |
| Alec Pierce | IND | IR |
| Jack Bech | LV | IR |
| Jonathon Brooks | CAR | IR |
| Travis Etienne | NO | OUT |
| Rico Dowdle | PIT | OUT — toe (2nd straight) |
| Joey Porter Jr. | PIT | OUT — since traded to Dallas |
| Teven Jenkins | CLE | OUT — back |
| Elgton Jenkins | CLE | OUT — concussion |
| Tylan Wallace | CLE | OUT — knee |
| Kendrick Green / Joe Royer / Elijah Chatman / Edefuan Ulofoshio / Tyson Campbell / Damarri Mathis | CLE | OUT |
| Cole Burgess / Jack Driscoll | PIT | OUT |

### Warning list (Q / GTD / LP / DNP — stays in pool until Sunday inactives)

| Player | Team | Note |
|--------|------|------|
| **Justin Jefferson** | MIN | Low left ankle sprain; DNP Wed; GTD. 7 snaps in W3 before exit |
| **Caleb Williams** | CHI | Grade 2 hamstring; 3–4 week curve; DNP Wed |
| **Jayden Daniels** | WAS | Left elbow dislocation; LP; GTD |
| **Nico Collins** | HOU | Hamstring; LP Wed |
| Chris Godwin | TB | Ankle; DNP Wed |
| Bucky Irving | TB | Glute; LP |
| Zay Flowers | BAL | Questionable |
| Brock Bowers | LV | Knee monitored; active in pool |
| Dallas Goedert | PHI | Questionable / GTD |
| Jalen Ramsey | PIT | Doubtful — broken wrist |
| Ed Ingram | HOU | Groin; LP |
| Ashton Dulin / Mo Alie-Cox | IND | DNP Wed |

### DFS usage priors — what a job change moves

| Team | Change | Volume effect |
|------|--------|---------------|
| **NYG** | Winston replaces Dart | Passing volume **up**; more air yards per attempt |
| **TB** | Backup replaces Mayfield | Passing volume **down**; compressed depths, quick screens, early-down run |
| **TB** | Ted Hurst (WR3) | Route participation **up** — McMillan on IR forces 3-WR sets |
| **NE** | Van Roten replaces Onwenu at RG | Pass-block efficiency **down**; shorter pocket time |
| **PIT** | Warren replaces Dowdle | Rushing **and** route volume **up** substantially |
| **CHI** | Keenum replaces Williams | Dropback volume **down**; quick-rhythm, intermediate crossers, checkdowns |

## Narrative — Part B: 13-game scheme card

Slate = 09:30 ET London, 13:00 ET early, 16:05/16:25 ET afternoon. **TNF (PIT@CLE), SNF (DET@CAR), MNF (ATL@NO) are excluded.**

| # | Game | Lean |
|---|------|------|
| 1 | IND @ WAS (London) | rec_yds on Washington primary slot; **full WAS stacks restricted until Daniels confirmed** [TENTATIVE] |
| 2 | TEN @ BAL | rush_yds on Baltimore backfield; positive script to bleed clock |
| 3 | NE @ BUF | **pass_yds on Buffalo** — NE interior after Onwenu → IR |
| 4 | NYJ @ CHI | rush_yds on Chicago RBs to protect Keenum from obvious passing downs |
| 5 | JAC @ CIN | **slate-high 51.5 total** — rec_yds on perimeter; primary game stack |
| 6 | DAL @ HOU | anytime_td on Houston secondary red-zone options; **roof uncalled** |
| 7 | ARI @ NYG | **pass_yds on Winston** — high YPA in spot starts; contrarian |
| 8 | LAR @ PHI | rush_yds on early-down volume vs light boxes |
| 9 | GB @ TB | rush_yds on Green Bay — clock-killing vs disrupted TB offense |
| 10 | MIA @ MIN | rush_yds on Minnesota RB (Aaron Jones) |
| 11 | KC @ LV | **rec_yds on Brock Bowers** — 13 targets in W3; dome |
| 12 | LAC @ SEA | rush_yds on Seattle — home favorite second-half script |
| 13 | DEN @ SF | anytime_td on SF primary red-zone rushers |

### Three stack priorities

1. **JAC @ CIN** — 51.5 total. Burrow + Ja'Marr Chase, brought back with a Jacksonville boundary option.
2. **KC @ LV** — dome. Mahomes + primary boundary, brought back with Bowers.
3. **NE @ BUF** — Allen + alpha pass-catcher; NE line vulnerable after Onwenu → IR.

### Three fades

1. **MIN passing** — Jefferson GTD on an ankle, decoy risk; MIN −10.5 at 39.5 favors ground control.
2. **CHI passing** — Keenum operating a conservative offense.
3. **TB passing** — rookie QB debut behind a banged-up line.

### Parlay constructs named in the doc

- Same-game yardage: CIN QB pass_yds + WR1 rec_yds. KC QB pass_yds + Bowers rec_yds. BAL RB rush_yds + TEN QB pass_yds.
- Cross-game anytime TD: CIN primary RB + BUF goal-line rusher. Bowers + SF lead rusher.

### Environmental uncertainties

- **NRG Stadium roof officially uncalled** — treat DAL @ HOU as exposed until the league posts a directive.
- Domes: U.S. Bank Stadium (MIA @ MIN), Allegiant (KC @ LV).
- London: 68°F, 79% humidity, 10% precip, 7 mph SW — favorable passing.

## Snippets

> "Rico Dowdle is ruled OUT with a severe lower-body injury for Pittsburgh." [Source: NFL Week 4 Research Plan.docx, Part A exec summary]

> "This contest serves as the primary game stack environment on the board." — on JAC @ CIN [Source: same, Part B]

## Dead Ends

- **The document names a Tampa Bay starting quarterback. The operator briefed against naming him.** Tampa Bay's gameday starter is **unannounced**; backup depth-chart names in this docx are source assertions, not club filings. Do not ticket that cell.
- **"Nico Collins OUT" is DraftEdge-sourced, not a club page.** Treat it as strong but secondary. See @sources/nfl-week4-slate-env-2026-10-02.md.
- **Three-game sample caveat is stated in the document itself.** Every CPOE/AGG/TTT figure covers fewer than 115 dropbacks. Do not treat as stabilized.
- **All designations are Thursday-baseline.** Friday filings supersede this page; see @sources/nfl-week4-slate-env-2026-10-02.md.
- The scheme card recipes are **structuring guidance, not selections**. No auto-enter.
