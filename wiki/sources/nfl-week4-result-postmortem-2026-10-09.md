---
title: "NFL Week 4 result — FanDuel and Hard Rock (2026-10-09)"
type: source
tags: [source, nfl, week-4, postmortem, dfs, parlay, fanduel, hard-rock]
keywords: [keenum, kincaid, collins, flowers, open-qb-cell, receiving-bar, te-dst-pair, first-td-none, cash-result]
related:
  - entities/sports/nfl-betting.md
  - concepts/parlay-and-correlated-bets.md
  - sources/nfl-week4-tnf-result-postmortem-2026-10-02.md
  - sources/nfl-week4-saturday-lock-2026-10-03.md
maturity: draft
read_status: deep-read
created: 2026-10-09
updated: 2026-10-09
location: operator desktop zips dfsrecapweek4.zip and week4parlaysrecap.zip (graded 2026-10-09; not archived to egress)
phase_0_verdict: REFERENCE — realized result; four standing rules
wire_status: policy_wired
---

## Relations

- @entities/sports/nfl-betting.md — the four rules live with the TNF bars
- @concepts/parlay-and-correlated-bets.md — on-card ticket construction
- @sources/nfl-week4-tnf-result-postmortem-2026-10-02.md — the two Thursday tickets this packet could not read
- @sources/nfl-week4-saturday-lock-2026-10-03.md — the open Chicago quarterback cell, and the Collins clear

## Raw Concept

| Field | Value |
|-------|-------|
| **Slate** | FanDuel NFL 2026 Week 4 Main, 2026-10-04. Thursday 2026-10-01 and Monday 2026-10-05 are in the parlay packet |
| **DFS packet** | `dfsrecapweek4.zip` — `recap.md`, `scores.csv`, `lineup_totals.csv`, `tool-gaps.md`. Retrieval `2026-10-09T23:14:44Z` |
| **Parlay packet** | `week4parlaysrecap.zip` — `recap.md`, `ledger.csv`, `tool-gaps.md`. Graded 2026-10-09 from Hard Rock screenshots plus PFR / FootballDB / club boxes |
| **Score check** | Every FanDuel lineup delta is **0.00**. Every graded parlay leg agrees with the book mark |
| **Build context** | The Week 4 FanDuel book was built by hand. The optimizer defect list is `CeminiDFS/briefs/2026-10-04_w04-build-postmortem.md` |

## Narrative

### Cash

| Book | Risked | Returned | Cash |
|------|-------:|---------:|-----:|
| FanDuel, 4 lineups / 6 entries | $12.05 | $5.10 | **−$6.95** |
| Hard Rock, Sunday + Monday cash tickets T2–T6 | $30.09 | $0 | **−$30.09** |
| Hard Rock, Thursday, two tickets already graded | $10.00 | $0 | **−$10.00** |
| **Week** | **$52.14** | **$5.10** | **−$47.04** |

The Monday 3-leg was a $10 bonus stake, so its cash result is $0. No Sweat on the Allen / Andrews ticket returned a $10 bonus. The bonus book is flat. One of four FanDuel lineups cashed. Every graded Sunday and Monday parlay lost.

The new parlay packet could read only one Thursday stake ($5, ticket `392036118507421970`, chips Over 70.5 / 34.5 / 14.5, +230). That ticket is T1 on the 2026-10-02 page. The cut-off +929 header is T2 on that page ($5). Add the second $5. Do not add $5 on top of the $10 already recorded.

### FanDuel — two families, one cash

| Lineup | Score | Fee | Won | Core |
|--------|------:|----:|----:|------|
| L04 | 126.22 | $3.05 (2 entries) | $5.10 | Allen, Walker III 33.40, Collins 30.30, Flowers 24.80 |
| L01 | 116.00 | $3.00 | $0 | Keenum **0.00**, Lamb 35.80, Flowers 24.80 |
| L02 | 101.12 | $3.00 | $0 | Same Henry / Lamb / Gesicki / Bengals core as L01 |
| L03 | 82.62 | $3.00 (2 entries) | $0 | Same Allen / Walker / Kincaid / Raiders core as L04 |

L01 and L02 share Henry, Lamb, Gesicki, and the Bengals. That core scored 66.20. L02's other four seats (Love, Adams, Raymond, Kelce) scored 15.30.

L03 and L04 share Allen, Walker, Kincaid, and the Raiders. The gap between 82.62 and 126.22 is 43.60, and it is entirely the other five seats. Collins and Flowers scored 55.10 of L04's unique points. Kincaid (1.20) and the Raiders (1.00) sat on both lineups.

L01 scored 116.00 with a quarterback at 0.00. Case Keenum took one ceremonial snap. Tyson Bagent played quarterback. The Saturday lock had left that cell open: the starter was unassigned and would be named 90 minutes before kickoff. L01 sits 10.22 under the only score that cashed. A starter-level quarterback is about 19 points. The two cards use different entry counts, so this page does not invent a payout for L01.

Allen scored 19.52. Six of those points were a rushing touchdown. He threw for 253 yards and one touchdown. Palmer scored 0.80, Kincaid 1.20, and Moore 2.20. Buffalo's passing stack did not travel with the quarterback's rushing points.

The projections column in the packet is empty. Moore and Tre' Harris were pinned by the lineup total, because the History cards show last names.

### What paid

Nico Collins is the process win. Friday had him out on a DraftEdge cite. Saturday cleared him from the club report. He scored 30.30 and sat on the only lineup that cashed.

Zay Flowers carried a hamstring warn, played, and paid both books: 24.80 on FanDuel and 118 receiving yards against a 71.5 line. The parlay around him still lost.

Kenneth Walker III (33.40) and CeeDee Lamb (35.80) were the other repeated scores. Lamb's pair still missed the cash line.

### Hard Rock — the compose card went 0-4

Fourteen graded legs. Three hit: Flowers 118, Burden 63, Allen 253.

| Ticket | Source | Price | Stake | Cash | Result |
|--------|--------|------:|------:|-----:|--------|
| T6 | compose-main #3 | +250 | $10 | −$10 | Allen 253 cleared 242.5. Andrews 27 missed 37.5 by 10.5 yards. No Sweat paid a $10 bonus |
| T5 | compose-3leg #5 | +528 | $10 | −$10 | Burden 63 hit. Lamar rushed for 20 on 2 attempts against 31.5. Moore had 11 yards against 50.5 |
| T2 | compose-main #5 | +250 | $5 | −$5 | Flowers 118 hit. Kincaid had 7 yards against 50.5 |
| T4 | compose-ftd #2 | +2925 | $3 | −$3 | Both first-touchdown legs missed. The Jets–Bears scheme card had said first touchdown: none |
| T3 | off the card | +1740 | $2.09 | −$2.09 | Chase left in the second quarter with a concussion and scored 0. Henry scored 1 |
| T1 | off the card, Monday | +258 | $10 bonus | $0 | Bijan 1 catch. Shough 1 pass TD. Kamara 23 rush yards. The slate packet had excluded Monday |

On-card cash is −$28. The new off-card cash is $2.09. Andrews is the only close miss. Kincaid, Moore, and Lamar were wide misses. Swift had two touchdowns reversed by replay, and Chase Brown also missed, so T4 loses either way.

Kincaid and Moore lost both products. Each was bet over 50.5 receiving yards, and each was on two FanDuel lineups.

### Four rules [CONFIRMED]

1. **An open quarterback cell cannot be rostered.** If the Saturday file says the starter is unassigned, that quarterback stays off the lineup.
2. **A receiving total at 50 or higher is a bar.** Kincaid 50.5 finished at 7. Moore 50.5 finished at 11. This extends the Thursday rule that a total opening in the 40s is the market's position.
3. **The same tight end and the same defense go on one lineup.** Kincaid and the Raiders scored 2.20 points on both L03 and L04.
4. **A first-touchdown leg stays off a game the scheme card marked "none."**

### Build defects that this result does not grade

The optimizer did not submit the Week 4 book. The defect list in `CeminiDFS/briefs/2026-10-04_w04-build-postmortem.md` still stands: normalize fell back to FanDuel's own FPPG, the role filter is missing, optimizer flags disagree across runs, merge-lineups skips the upload file, and review reports missed a shared core. The operator also reported that research excludes removed so many players that the lineups had too little variance. Those are code defects. This page records the played result only.

## Snippets

> "Starter unassigned between Bagent and Keenum; revealed 90 minutes before kickoff. Cell stays open." [Source: @sources/nfl-week4-saturday-lock-2026-10-03.md]

> "L01 rostered Case Keenum (CHI) at QB → 0.00: Bagent started; Keenum took only a ceremonial first snap." [Source: dfsrecapweek4.zip tool-gaps.md TG01]

## Dead Ends

- **Do not add the unread Thursday $5 a second time.** The 2026-10-02 page already has both Thursday tickets at −$10.
- **Do not treat the No Sweat bonus as cash.** Cash on T6 is −$10.
- **$47.04 is not a sample.** This page records method failures. No bankroll change follows from one week.
- **Do not post-hoc the Buffalo miss onto weather.** Allen threw for 253 yards. The miss was target share and a rushing touchdown, not pass volume.
