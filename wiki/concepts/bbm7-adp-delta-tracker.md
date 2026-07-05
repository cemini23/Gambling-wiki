---
title: BBM7 ADP delta tracker
type: concept
tags: [concept, best-ball, bbm7, adp, underdog, value]
keywords: [adp-delta, closing-line-value, te-cluster, rookie-value, buy-fade]
related:
  - concepts/best-ball-strategy.md
  - concepts/best-ball-draft-timing.md
  - concepts/bbm7-playoff-week-construction.md
  - concepts/bbm7-portfolio-construction.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/platforms/underdog-fantasy.md
  - sources/fantasysixpack-bbm-new-meta-2026-06-08.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/web-offseason-hub-w27-synthesis-2026-07-05.md
  - concepts/nfl-offseason-research-cadence.md
maturity: validated
created: 2026-06-18
updated: 2026-07-05
---

## Relations

- @concepts/best-ball-strategy.md — positional playbook and CLV priority
- @concepts/bbm7-portfolio-construction.md — how to deploy buys across 150 entries
- @sources/4for4-bbm7-guide-series-2026-06-18.md — TE window + QB cluster thesis
- @sources/fantasysixpack-bbm-new-meta-2026-06-08.md — WR selectivity + QB-cost framing

## Raw Concept

Living tracker of **Underdog ADP vs strategy rank** for BBM7 draft decisions. Update when ADP moves materially (camp news, injuries).

**Primary ADP source:** [bestballteambuilder.com Underdog ADP](https://www.bestballteambuilder.com/underdog-best-ball-average-draft-position) — retrieved **2026-06-18**. Cross-check: [FantasyPros best-ball consensus](https://www.fantasypros.com/nfl/adp/best-ball-overall.php).

**Delta notation:** `Δ = strategy slot − ADP` (positive = **BUY**, player should rise; negative = **FADE**, overpriced).

## Narrative

### Methodology

1. **Closing-line goal** — top CLV bucket ≈ **3× finals rate** vs worst [@sources/4for4-bbm7-guide-series-2026-06-18.md]
2. **Real-time goal** — draft player below their ADP at pick time; top 20% CLV → **+~25%** advance rate [ETR]
3. **Position windows** — 4for4 BBMVI meta: QB **R8–10** (ADP ~85–119), TE **R11–13** (ADP ~121–156), elite WR tier OK R1, else RB early
4. **Confidence** — `[CONFIRMED]` = multi-source + BBMVI data; `[TENTATIVE]` = early-season ADP only

---

### TE cluster — R11–13 (ADP 121–156) [PRIORITY]

~**33% of picks** in this band are TEs on Underdog [@sources/4for4-bbm7-guide-series-2026-06-18.md]. Target **3 TE builds** with QB stacks where possible.

| Player | ADP | Rnd | Proj pts* | Signal | Notes |
|--------|-----|-----|-----------|--------|-------|
| Travis Kelce | 120.4 | 11 | 131.5 | **BUY** | Anchor of cluster; KC W5 bye |
| Jake Ferguson | 126.2 | 11 | 126.8 | **BUY** | 4for4 explicit target; DAL W14 bye |
| Mark Andrews | 126.5 | 11 | 127.8 | **BUY** | BAL W13 bye |
| Dalton Kincaid | 129.5 | 11 | 125.6 | NEUTRAL | BUF W7 — pair QBs away from W7 |
| Isaiah Likely | 131.7 | 11 | 121.7 | NEUTRAL | BAL stack with Andrews = same bye |
| Dallas Goedert | 136.0 | 12 | 115.5 | **BUY** | 4for4 target; PHI W10 |
| Oronde Gadsden | 144.7 | 12 | 122.1 | **BUY** | **Fell ~24 spots** post-Njoku; LAC W7 |
| Chig Okonkwo | 147.0 | 13 | 95.9 | **BUY** | Riser (+3.4 Jun); WAS W7 |
| Brenton Strange | 153.0 | 13 | 124.8 | **BUY** | 4for4 target; JAX W7 |
| Hunter Henry | 150.2 | 13 | 119.9 | NEUTRAL | NE W11 |
| Juwan Johnson | 158.0 | 14 | — | **BUY** | BBM6 winner piece; NO W8; late value |
| Greg Dulcich | 194.4 | 17 | — | **BUY** | +17 ADP riser Jun; MIA W6 |
| Terrance Ferguson | — | — | — | **BUY** [TENTATIVE] | ADP riser w27 — Fantasy Life + ETR Market Monday; verify on bestballteambuilder |

*Proj pts from bestballteambuilder half-PPR season projection, 2026-06-18.

**TE fades (early):**

| Player | ADP | Signal | Why |
|--------|-----|--------|-----|
| Brock Bowers | 19.9 | **FADE** | Elite TE underperformed BBMVI; R2 opportunity cost |
| Trey McBride | 26.4 | **FADE** | Same; ARI W14 |
| George Kittle | 114.9 | NEUTRAL | SF W8; OK if stacked with Purdy |
| Sam LaPorta | 97.3 | NEUTRAL | DET W6 — bye overlap with Gibbs/ARSB stacks |

**Operator note:** YouTube batch flagged **40–50 spot TE ADP deltas** broadly [@sources/youtube-operator-batch-wc-bbm-2026-05-31.md] — cluster is the highest-conviction mispricing lane for BBM7.

---

### QB window — R8–10 (ADP ~85–119) [PRIORITY]

~**40% of ADP 85–116 are QBs** [@sources/4for4-bbm7-guide-series-2026-06-18.md]. **3-QB builds** mandatory; avoid **same bye** across QB room.

| Player | ADP | Rnd | Signal | Bye | Notes |
|--------|-----|-----|--------|-----|-------|
| Jalen Hurts | 71.9 | 6 | **BUY** | W10 | 4for4 R6 tier; stack with Brown/Smith |
| Jayden Daniels | 66.9 | 6 | **BUY** | W7 | Discount vs prior years |
| Joe Burrow | 65.2 | 6 | **BUY** | W6 | Stack with Chase/Higgins/Brown |
| Drake Maye | 70.4 | 6 | NEUTRAL | W11 | |
| Trevor Lawrence | 85.6 | 8 | **BUY** | W7 | QB2/3 value |
| Patrick Mahomes | 89.4 | 8 | NEUTRAL | W5 | Stack Kelce |
| Brock Purdy | 96.9 | 8 | **BUY** | W8 | Kittle stack |
| Baker Mayfield | 107.9 | 9 | NEUTRAL | W10 | TB W10 stack |
| C.J. Stroud | 142.4 | 12 | **BUY** | W8 | Last "confident starter" ~R12; BBM4 winner path |
| Tyler Shough | 119.2 | 10 | **BUY** | W8 | **Falling** (−4.3 Jun); NO stack w/ Olave |
| Bryce Young | 155+ | 13 | **BUY** | W5 | BBM6 winner QB path; late lottery |
| Josh Allen | 33.8 | 3 | **FADE** | W7 | 4for4: opportunity cost vs RB cliff |

**QB pairing rule:** When drafting QB2 + QB3, check byes — e.g. Burrow (W6) + Daniels (W7) + Stroud (W8) = **three distinct byes** ✓

---

### RB — early vs cliff (ADP ~1–55) [CONFIRMED BBMVI]

| Tier | ADP band | Signal | Targets |
|------|----------|--------|---------|
| **Elite early** | 1–18 | **BUY** (advance meta) | Gibbs, Bijan, Taylor, CMC, Henry, Jeanty, Achane |
| **RB2 tier** | 19–36 | **BUY** | Chase Brown, Omarion Hampton, Kyren, Breece |
| **Cliff** | 37+ | CAUTION | Upside thin; Henderson, Judkins, Skattebo only flagged young RBs |
| **Zero-RB salvage** | 74–93 | **BUY** (if zero-RB) | Stevenson, Swift, Pollard — high routes/game |

**Fades / caution:**

| Player | ADP | Signal | Why |
|--------|-----|--------|-----|
| Bucky Irving | 53.2 | **FADE** | Falling; TB RB room murky |
| Josh Jacobs | 39+ | NEUTRAL | Falling −12.5 Jun |

---

### WR — elite tier + late value

**F6P filter (2026):** hit WR **shell count** (4–5 by R7 per 4for4) but avoid **name-only WR3 depth** in heavy-personnel offenses [@sources/fantasysixpack-bbm-new-meta-2026-06-08.md]. Prefer alphas + ADP 25–60 earners over ambiguous camp-hype WR3.

| Player | ADP | Signal | Notes |
|--------|-----|--------|-------|
| Ja'Marr Chase | 3.1 | **BUY** (elite) | W6 bye — stack w/ Burrow; finals ownership insane when hits |
| Puka Nacua | 4.0 | **BUY** | W11 bye cliff if over-stacked |
| Amon-Ra St. Brown | 7.7 | **BUY** | W6 bye |
| Jaxon Smith-Njigba | 5.2 | **BUY** | W11 bye |
| Tetairoa McMillan | 38.2 | **BUY** | R4 rookie; CAR stack w/ Young |
| Emeka Egbuka | ~41 | **BUY** | TB stack |
| Chris Olave | 27.7 | NEUTRAL | BBM6 winner best pick |
| Tyreek Hill | 133+ | **FADE** | Free agent; −27 ADP Jun |
| Brandon Aiyuk | 188+ | **FADE** | Uncertainty |

**Rookie WR CLV (May–June window)** — draft before ADP catches NFL draft capital:

| Player | ADP | Signal | Notes |
|--------|-----|--------|-------|
| Omar Cooper Jr. | ~140 | **BUY** | Round 1 NFL draft projection; riser |
| Denzel Boston | ~159 | **BUY** | Cleveland; late riser |
| KC Concepcion | ~116 | **BUY** | ADP 116 vs rising mock capital |
| Zachariah Branch | ~187 | **BUY** | +16.5 ADP Jun; ATL WR2 path |
| Ted Hurst | ~183 | **BUY** | +28 ADP Jun; TB X receiver |
| Travis Hunter | ~69 | NEUTRAL | Two-way role risk |

---

### Quick reference — buy/fade summary

**Strong BUY lanes:** TE R11–13 cluster · QB R6 + R8–10 · Rookie WRs (May–June) · Early RB (4for4 advance meta) · Gadsden post-fade · CLV on any pick >2 slots below ADP

**Strong FADE lanes:** Josh Allen R3 · Elite TE R2 (Bowers/McBride) · Tyreek Hill · Same-bye QB rooms · 10+ players sharing one bye

---

### Update cadence

| When | Action |
|------|--------|
| Weekly (Jun–Aug) | Refresh ADP table; note risers/fallers from 4for4 column |
| Camp reports | Move injury fades to BUY; update FADE list |
| Aug 1+ | Shift focus from CLV to live-player clarity; reduce rookie speculation |
| Pre-Week 1 | Final closing-line snapshot for post-mortem |

## Snippets

> "Nearly 40% of the players with an ADP from 85 to 116 are QBs at the moment." [Source: 4for4 QB article]

> "One-third of the players taken in Rounds 11 through 13 right now are TEs." [Source: 4for4 TE article]

## Dead Ends

- **Chasing ADP risers after +20 spot move** — often missed CLV; prefer origin point (May–June) for rookies
- **Drafting Allen R3** — 4for4 + RB cliff data both say opportunity cost too high in 2026 market
