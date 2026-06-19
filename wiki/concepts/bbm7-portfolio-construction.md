---
title: BBM7 portfolio construction (150 entries)
type: concept
tags: [concept, best-ball, bbm7, portfolio, bankroll, archetypes]
keywords: [150-entries, portfolio-drafting, hero-rb, zero-rb, stack-heavy, timing-windows]
related:
  - concepts/best-ball-strategy.md
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-playoff-week-construction.md
  - concepts/best-ball-draft-timing.md
  - concepts/best-ball-mania-winners.md
  - concepts/bankroll-management.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/platforms/underdog-fantasy.md
  - sources/fantasysixpack-bbm-new-meta-2026-06-08.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @concepts/bankroll-management.md — $3,750 max-enter = GPP bankroll cap
- @concepts/bbm7-adp-delta-tracker.md — buy/fade targets per window
- @concepts/bbm7-playoff-week-construction.md — bye + W17 rules per roster
- @concepts/best-ball-draft-timing.md — when to draft each tranche

## Raw Concept

Operator playbook for **150 BBM7 entries** ($3,750 total). Assumes max-enter; scale proportionally if entry count changes.

**Handoff copy:** `briefs/2026-06-18_bbm7-portfolio-brief.md` (gitignored deliverable)

## Narrative

### Bankroll frame [CONFIRMED]

| Item | Value |
|------|-------|
| Entry fee | $25 |
| Entries | 150 |
| Total exposure | **$3,750** |
| Final min-cash (301–667) | **$3,750** |
| Breakeven narrative | **1 Final seat ≈ recoups max-enter** before upside |

Treat as **single GPP portfolio** — not 150 independent lottery tickets. Goal: maximize **P(any Final)** + **P($2M)** via diversification.

---

### Three axes of diversification

1. **Draft timing** — CLV vs live players (ETR + 4for4)
2. **Archetype** — advance-optimal vs winner-path variance
3. **Player exposure** — cap single-player ownership across 150

---

### Timing split (150 entries)

| Window | Entries | % | Primary goal |
|--------|---------|---|--------------|
| **May–June** | 38 | 25% | CLV — rookie WRs, post-NFL-draft mispricings, structured 3QB/3TE shells |
| **Mid-July – mid-Aug** | 82 | 55% | **Core** — ETR optimal balance; bulk of 4for4 advance builds |
| **Late Aug – Sep** | 30 | 20% | Clarity — injury fades, role confirmation, W17 tiebreakers |

**Draft speed:** Fast drafts default; slow drafts only in May–June if seeking softer rooms (minor CLV edge, confounded) [ETR].

---

### Archetype split (150 entries)

Balance **4for4 BBMVI advance meta** with **historical winner paths** [@concepts/best-ball-mania-winners.md].

| Archetype | Entries | % | Description | Key exposures |
|-----------|---------|---|-------------|---------------|
| **A — RB-forward (4for4)** | 53 | 35% | R1–2 RB, 4–5 RB total, 4–5 WR by R7, late TE cluster | Gibbs/Taylor/Henry anchors; Ferguson/Goedert/Strange |
| **B — Hero RB + WR** | 38 | 25% | Single early RB (R2), WR-heavy; BBM6 path | Henry, ARSB, JSN builds |
| **C — Stack-heavy** | 30 | 20% | 3–4 man stacks; BBM5 path | CIN (Burrow/Chase/Higgins/Brown), PHI, LAC |
| **D — Zero / late RB** | 23 | 15% | WR-first R1–3, RB late; BBM4 path | Stevenson/Swift/Pollard if RB after R5 |
| **E — Contrarian / balanced** | 6 | 4% | Board-driven; no forced archetype | Highest CLV picks only |

#### Cross-matrix: timing × archetype

| Archetype | May–Jun | Jul–Aug | Late Aug |
|-----------|---------|---------|----------|
| A RB-forward | 8 | 30 | 15 |
| B Hero RB | 10 | 22 | 6 |
| C Stack-heavy | 6 | 18 | 6 |
| D Zero RB | 10 | 8 | 5 |
| E Contrarian | 4 | 4 | 2 |

---

### Positional shell (default 18-man)

Apply to archetypes A–C unless contrarian:

| Pos | Target count | Draft capital |
|-----|--------------|---------------|
| QB | **3** | R6 + R8–10 + R12–15 |
| RB | **4–5** | R1–2 (A/B) or R8+ (D) |
| WR | **6–7** | R1 elite or R3–7 cluster |
| TE | **2–3** | **R11–13 cluster** primary |

---

### Exposure caps (150 entries)

Prevent portfolio wipeout on one injury/event.

| Tier | Max exposure | Examples |
|------|--------------|----------|
| **Elite anchor** | 35% (53/150) | Chase, Gibbs, Bijan, ARSB |
| **Stack core** | 25% (38/150) | Burrow, Chase combo |
| **Mid-round target** | 20% (30/150) | Ferguson, Strange, Hurts |
| **Late-round lottery** | 15% (23/150) | Shough, Gadsden, rookies |
| **Single late dart** | 10% (15/150) | Any R17–18 one-off |

**Minimum unique rosters:** aim for **≥120 structurally distinct** teams (80% uniqueness) — vary QB3, TE3, and RB4–5 counts.

---

### Per-archetype draft script

#### A — RB-forward (53 entries)

```
R1–2: RB-RB or RB-WR (elite RB required)
R3–5: WR run (2–3 WRs)
R6: QB1 (Hurts/Daniels/Burrow tier)
R7–9: WR/RB fill
R8–10: QB2 + value
R11–13: TE TE TE (cluster)
R14–18: QB3, RB depth, lottery
```

**Avoid:** R1 WR unless elite tier (Chase/Nacua/ARSB/Lamb).

#### B — Hero RB (38 entries)

```
R1: WR (ARSB/JSN/Nacua)
R2: Hero RB (Henry/Jeanty/Taylor)
R3–6: WR WR WR
R6–8: QB
R11–13: TE cluster
Late: QB3, stack pieces
```

#### C — Stack-heavy (30 entries)

```
R1–3: Stack anchor (Chase/Brown or McConkey)
R4–8: Complete 3–4 man stack same team
R6–10: QB from stack + bring-backs
R11–13: TE (stack-aligned if possible)
Fill: opposing W17 game pieces
```

**Cap:** 4 players same team; avoid 5+ [@sources/4for4-bbm7-guide-series-2026-06-18.md].

#### D — Zero RB (23 entries)

```
R1–3: WR WR WR (elite if available)
R4–6: WR + QB
R7+: RB Stevenson/Swift/Pollard/Skattebo
R11–13: TE cluster
Late: RB lottery, QB3
```

---

### Weekly operator cadence (Jun–Sep)

| Cadence | Task |
|---------|------|
| **Daily** | Check player news before draft blocks (4for4 Player News) |
| **Weekly** | Refresh @concepts/bbm7-adp-delta-tracker.md; adjust BUY/FADE |
| **Monthly** | Rebalance remaining entries toward underrepresented archetypes |
| **Aug 1** | Shift 70%+ of remaining drafts to late window |
| **Sep 1** | Final 30 entries max; only clear CLV or injury fades |

---

### Success metrics (track in spreadsheet)

| Metric | Target |
|--------|--------|
| Avg CLV per roster | Top 40% of field |
| Archetype distribution | Within ±5% of matrix |
| Advance rate (in-season) | ~16.7% baseline → 18%+ = good process |
| Final appearances | 0.08% per entry baseline → 1+ Final = successful portfolio variance |
| Max single-player exposure | ≤35% |

---

### Open decisions [operator]

- [ ] Confirm final entry count (150 vs partial)
- [ ] Select projection source for CLV (ETR vs 4for4 vs RotoBaller)
- [ ] Fantasy Guru deep-read if subscribed — may adjust stack targets
- [ ] Post-camp refresh: Aug 15 re-run ADP tracker

## Snippets

> "One Final seat roughly recoups a full max-enter portfolio before upside." [Source: @entities/tournaments/best-ball-mania-vii.md]

> "Portfolio diversification across archetypes is rational." [Source: @concepts/best-ball-mania-winners.md]

## Dead Ends

- **150 identical RB-forward builds** — wins advance rate battles but caps winner-path variance
- **All May drafts** — live-player penalty at playoffs [ETR]
- **Ignoring exposure caps** — one ACL to Chase at 60% exposure destroys portfolio
