---
title: Sharp Football — 2026 NFL RB season-long prop unders
type: source
tags: [source, web, nfl, props, pickem, w8]
keywords: [jonathan-taylor, chuba-hubbard, rushing-yards, season-long-props, volume-regression]
related:
  - sweeps/2026-08-14-daily.md
  - entities/sports/nfl-betting.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/player-usage-models.md
  - concepts/pickem-fair-probability.md
maturity: validated
read_status: read
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- @sweeps/2026-08-14-daily.md — RSS S23
- @entities/sports/nfl-betting.md — season-long player props
- @concepts/player-usage-models.md — carry-share / committee priors
- @concepts/diy-nfl-pickem-props-tool-architecture.md — K147 fair-value vs posted line

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | 2026 NFL Running Back Prop Bets: Best Unders to Target |
| **URL** | https://www.sharpfootballanalysis.com/betting/nfl-running-back-player-prop-unders/ |
| **Author** | Curtis Hirsch |
| **Published** | 2026-08-13 |
| **Read status** | read (free web; futures-package CTA on page) |

## Narrative

Hirsch uses in-house (Warren Sharp / Rich Hribar-style) projections vs posted **season-long rushing-yard** numbers. Two unders only in this article — not a full board. **Affiliate/package marketing** on the page; treat the **mechanism** (volume × game script × committee) as the ingest, not the 98-55 package record.

### Jonathan Taylor Under 1224.5 rushing yards (-105) [TENTATIVE]

Thesis is **volume regression**, not talent fade:

- 2025: league-high **323** carries, **1,585** yards; **86.7%** of Colts RB carries.
- Win/loss split (last two seasons): **22.4** carries / **126** rush yards in wins vs **18.6** / **76.4** in losses (~50-yard game-state gap).
- Four straight seasons **under 5.0 YPC** → needs ~**260–280** carries to clear 1,225.
- Steichen wants a lighter workload; contract extension = protect the asset; age **27**; only two 17-game seasons in five years.
- Colts win-total drifted down; Daniel Jones Achilles return; Pierce (surgery) / Downs (groin) receiver depth; 2025 early-season efficiency hard to repeat → more trailing scripts → fewer carries.

Retail: this is a **carry-share + team-win** bet. Map to K147 as season-long O/U, not weekly pick'em. Do **not** auto-fade Taylor weekly without the same volume gate.

### Chuba Hubbard Under 700 rushing yards (-114) [TENTATIVE]

Thesis is **committee + OL + negative script**:

- 2025 calf year was weak; no **15+** yard explosive rushes.
- From Week 9 2025: **6.1** carries/game, **29.7%** of Panthers RB carries; never >50% in that stretch.
- 2026: Rico Dowdle already cut into role; **Jonathon Brooks** (2024 2nd-round) is the younger capital; Hubbard camp **hamstring**; Panthers can cut Hubbard next year with little dead money → org incentive to feature Brooks.
- Career **4.1 YPC** (≤3.8 in three of five seasons) → ~**170** attempts (~10/game) to hit 700.
- Panthers favorites in **only three** games; tough defensive SOS; both starting tackles out to open (Ekwonu patellar, Moton blood clots).

Retail: same mechanism as `@concepts/player-usage-models.md` committee HHI — do not project a 700-yard season from early-career peak without a carry monopoly.

## Snippets

> "This is not a bet questioning Taylor’s talent or ability. It is a bet on volume reduction from 2025, which is a difficult season to replicate." [Source: https://www.sharpfootballanalysis.com/betting/nfl-running-back-player-prop-unders/ (retrieved 2026-08-14)]

> "The case for betting Hubbard's 2026 rushing-yard total under isn't that he is going to struggle or incapable of producing. It is a bet against him reaching the required number of carries in a committee on a team with a low win total and offensive line injuries." [Source: same]

## Dead Ends

- Page cites a **98-55 (64%)** Sharp futures package record — marketing, not a reproducible CLV sample. Do not import into bankroll process.
- WR prop unders “coming soon” — no ingest.
