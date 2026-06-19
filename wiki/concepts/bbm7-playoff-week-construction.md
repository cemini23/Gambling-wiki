---
title: BBM7 playoff week construction (W15–17)
type: concept
tags: [concept, best-ball, bbm7, schedule, bye-weeks, week-17, game-stacks]
keywords: [week-15, week-16, week-17, bye-weeks, game-stacks, playoff-advance]
related:
  - concepts/best-ball-mania-winners.md
  - concepts/best-ball-strategy.md
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-portfolio-construction.md
  - concepts/best-ball-draft-timing.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/platforms/underdog-fantasy.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @entities/tournaments/best-ball-mania-vii.md — bracket: QF W15, SF W16, Final W17
- @sources/4for4-bbm7-guide-series-2026-06-18.md — schedule + game-stack thesis
- @concepts/best-ball-mania-winners.md — BBM6 Sherman W17 stacks

## Raw Concept

How **NFL schedule, bye weeks, and Week 17 matchups** affect BBM7 roster construction. Distinction: **regular-season byes (W5–14)** affect advance rate; **playoff weeks (W15–17)** have **no byes** — optimize for ceiling and live players.

## Narrative

### Playoff structure reminder [CONFIRMED]

| Round | NFL week | Pod | Advance | Prize leverage |
|-------|----------|-----|---------|----------------|
| Regular season | 1–14 | 12 | Top 2 | ~$25 |
| Quarterfinals | **15** | 13 | Top 1 | ~$75 |
| Semifinals | **16** | 16 | Top 1 | ~$1,000 |
| Final | **17** | ~667 | Top 1 | **~84% of pool** |

Week 17 is a **single-week shootout** — first place pays **533×** last place in the Final [@sources/4for4-bbm7-guide-series-2026-06-18.md].

---

### Bye weeks — what actually matters

**Byes are known from the May schedule release** — you do **not** need to wait until August to plan them [@concepts/best-ball-draft-timing.md].

**During W15–17:** no NFL teams on bye. Playoff construction ≠ avoiding W17 byes (there are none).

**During W1–14:** byes affect **regular-season pod scoring**. One empty QB/TE week ≈ **45-point swing** — often the difference between 2nd (advance) and 3rd (out) in a 12-team pod [@sources/4for4-bbm7-guide-series-2026-06-18.md].

#### 2026 bye week calendar [CONFIRMED — sharpfootballanalysis.com 2026-05-31]

| Week | Teams on bye |
|------|--------------|
| 5 | Chiefs, Panthers |
| 6 | Bengals, Dolphins, Lions, Vikings |
| 7 | Bills, Chargers, Commanders, Jaguars |
| 8 | 49ers, Giants, Saints, Texans |
| 9 | Steelers, Titans |
| 10 | Bears, Broncos, Buccaneers, Eagles |
| 11 | Browns, Falcons, Packers, Patriots, Rams, Seahawks |
| 13 | Colts, Jets, Raiders, Ravens |
| 14 | Cardinals, Cowboys |

#### High-impact bye weeks for best ball

**Week 6 — heaviest skill-player bye**

Chase, Gibbs, ARSB, Jefferson, Burrow, Higgins, Brown, LaPorta, Jameson Williams, Achane (MIA W6). Stacking Bengals + Lions + Vikings = **multiple zeros same week**.

**Week 7 — QB bye cluster**

Allen, Daniels, Herbert, Lawrence, McConkey, McLaurin, Moore. **Same-bye QB room → 14.5% advance** vs 16.7% avg.

**Week 11 — six-team mega-bye**

Bijan, Puka, JSN, Judkins, Kraft, Pitts, Fannin, A.J. Brown, Jacobs, Davante Adams, Stafford. **Three of top 7 TE ADPs idle.**

**Week 14 — late-season**

Lamb, Pickens, McBride, Jeremiyah Love (DAL/ARI). Hurts late bye if stacked with PHI.

#### Bye construction rules [CONFIRMED]

| Rule | Threshold | Impact |
|------|-----------|--------|
| **3 QB — distinct byes** | No shared bye across all 3 | Same-bye 3-QB → below-avg advance |
| **3 TE — distinct byes** | 2nd consecutive year edge | Per 4for4 BBMVI |
| **Shared bye cap** | ≤7 players same bye OK | 10+ same bye → 15.6% advance (−1.1%) |
| **Stack bye overlap** | Same-team stacks share bye automatically | Accept for ceiling; diversify across entries |

**3-QB bye pairing example (good):**

- QB1: Burrow (CIN **W6**)
- QB2: Daniels (WAS **W7**)
- QB3: Stroud (HOU **W8**) or Young (CAR **W5**)

**Bad:** Allen (W7) + Herbert (W7) + Daniels (W7) = guaranteed zero from highest-scoring position one week.

---

### Week 17 game stacking

**Purpose:** Maximize ceiling in the money round — not for regular-season advance.

| Principle | Detail |
|-----------|--------|
| **More game stacks → higher ceiling** | Lower floor if game duds |
| **BBMVI winner** | Sam Sherman — **4 different W17 game stacks** |
| **Early-round bets first** | Draft best players R1–6; use W17 as **tiebreaker** |
| **Example** | McConkey (LAC) R4 → lean Worthy (KC) later as W17 bring-back if LAC-KC scheduled |

**Do not** force W17 stacks in R1–4 based on projected totals — 6-month totals unreliable (Patriots/Jets projected low, scored 52) [@sources/4for4-bbm7-guide-series-2026-06-18.md].

**Late draft tiebreaker logic:**

1. You have Burrow + Chase + Higgins (CIN)
2. Check CIN's Week 17 opponent
3. If facing CLE, lean **CLE pass-catcher or bring-back** over equivalent ADP player

---

### Soft playoff schedules (W15–17) [TENTATIVE]

From Yahoo 2026 schedule analysis — teams with **easier W15–17 matchups on paper**:

| Team | W15 | W16 | W17 | Note |
|------|-----|-----|-----|------|
| **ARI** | vs NYJ | vs NO | vs LV | Soft path after W14 bye |
| **IND** | TBD | TBD | TBD | Daniel Jones / Taylor stacks |

Treat as **tiebreaker only** — schedule strength shifts with roster changes.

---

### Live players at playoff entry [CONFIRMED — ETR]

More important than bye math for W15+: **13+ live players** entering playoffs.

- August drafts → overrepresented among 18/18 live rosters
- May–June drafts → more dead players by W15
- See @concepts/best-ball-draft-timing.md for portfolio timing split

BBM3 winner Kerrane: **15/18 live** in Week 17.

---

### Checklist per roster (draft room)

- [ ] **3 QBs** with **≥2 distinct bye weeks** (ideally 3)
- [ ] **2–3 TEs** with distinct byes if running 3-TE build
- [ ] **≤7 players** sharing any single regular-season bye
- [ ] **≥1 skinny stack** (2–3 players) per offense targeted
- [ ] **Week 17 correlation** considered for late picks (rounds 10+)
- [ ] **No 10+ player** same-bye cluster

## Snippets

> "There is a very reasonable chance that one additional week of QB or TE scoring is the difference between you advancing to the playoffs or just missing out." [Source: 4for4 schedule article]

> "About 84% of the total prize pool is doled out in Week 17." [Source: 4for4 schedule article]

## Dead Ends

- **Waiting until August to learn byes** — schedule public in May
- **Projecting W17 shootouts in May** — use as late tiebreaker only
- **Single-QB rosters** — <10% advance; never in BBM7 builds
