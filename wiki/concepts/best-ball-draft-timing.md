---
title: Best ball draft timing
type: concept
tags: [concept, best-ball, underdog, bbm7, adp, draft-strategy]
keywords: [draft-timing, when-to-draft, closing-line-adp, camp-injuries, live-players, july-august]
related:
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-playoff-week-construction.md
  - concepts/bbm7-portfolio-construction.md
  - concepts/best-ball-strategy.md
  - concepts/best-ball-mania-winners.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/platforms/underdog-fantasy.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @entities/tournaments/best-ball-mania-vii.md — BBM7 draft window (opens late April, closes Week 1)
- @concepts/best-ball-strategy.md — roster construction and ADP value
- @concepts/best-ball-mania-winners.md — Kerrane (BBM3) drafted July 18
- @sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md — ETR Leone BBM3 timing analysis

## Raw Concept

When to draft in Underdog Best Ball Mania given a ~4.5-month window (late April → Week 1). Tradeoff between **closing-line ADP value (CLV)** and **roster health at playoff entry**.

## Narrative

### The core tradeoff

Two forces pull in opposite directions:

| Force | Favors | Mechanism |
|-------|--------|-----------|
| **ADP inefficiency** | Early (May–June) | Market uses stale rankings; rookies mispriced post-NFL Draft; "risers never rise fast enough" [Source: Fantasy Life] |
| **Live players at playoffs** | Late (July–August) | Fewer camp/preseason injuries on your roster entering Week 15; depth charts settled |

Mike Leone's BBM3 data analysis (ETR Manifesto Part 2) is the strongest quantitative source on timing. His conclusion: **mid-July through mid-August** balances both goals [CONFIRMED].

> "Drafting somewhere between mid-July and mid-August seems to provide contestants with the best combined odds of achieving strong closing line ADP Value and having 13-plus live players on a roster when entering the playoff stages." [Source: ETR Manifesto via @sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md]

BBM3 winner Pat Kerrane drafted **July 18** — anecdotal but aligned with the data [CONFIRMED].

### Month-by-month breakdown (BBM3 data) [CONFIRMED — ETR]

**May–June — high variance CLV, health penalty**
- Odds of top ADP Capital teams increase sharply vs later months
- May shows the widest variance: biggest gains in top *and* bottom ADP Capital buckets
- Teams drafted May–June fight uphill battle for **13+ live players** at playoff entry
- Slow drafts overrepresented in May–July (softer competition, but timing confound)

**July — transition sweet spot**
- Still achieves strong CLV without May-level dead-player risk
- "Natural cutoff" — acceptable on both metrics
- Recommended as start of core drafting window

**August — health boost, slight CLV cost**
- **47.2%** of teams with 18 live players at Week 15 were drafted in August vs **41.2%** baseline (overrepresented)
- Top single-month ADP Capital teams less likely, but **buckets 1–3 collectively** only diminish slightly
- Top 25% of teams by model: **~3.0%** QF advance rate (Aug/Sep) vs **~2.6%** (earlier months) [TENTATIVE — ETR model]

**September — diminishing returns**
- CLV opportunities mostly exhausted; ADP converges toward closing line
- Health advantage remains but less edge vs August
- Draft volume drops; less liquidity in draft rooms

### Bye weeks — your August hypothesis [PARTIALLY RETRACTED]

**Bye weeks are known from the NFL schedule release (~May)**, not from waiting until August. You can plan Week 15–17 bye cliffs from May onward.

Leone explicitly tested whether bye-week effects distorted playoff-upside analysis: *"The data did not change in any meaningful way after accounting for either bye weeks or early-season weeks."* [CONFIRMED — ETR Manifesto]

**Implication:** bye-week construction matters at draft time regardless of *when* you draft — it's a roster-building discipline, not a reason to wait until August. August helps for **injury/role clarity**, not bye discovery.

### Camp and preseason injuries [CONFIRMED]

Primary reason to avoid May–early July for your *entire* portfolio:

- Training camp (late July) and preseason (August) produce ACL tears, holdouts, depth-chart demotions
- Early-drafted teams accumulate "dead players" — injured, suspended, or benched by Week 15
- ETR defines "live player" as any player scoring >0 in a given week; **13+ live players** at playoff entry strongly correlates with estimated playoff win rates
- Kerrane's BBM3 winner: **15/18 live** in Week 17 [CONFIRMED]

**August-specific edge:** players slide on ADP due to negative camp reports or minor injuries — buyable discount if role is stable [Source: Draft Sharks best ball strategy, 2026].

### Closing-line ADP (CLV) [CONFIRMED]

- **Closing line** = player ADP at end of BBM draft window (late August / early September, pre-Week 1) [Source: 4for4 BBM WR analysis]
- Top 10% of BBM3 teams gained ADP value equivalent to **116 picks**; bottom 10% lost **212 picks** — 328-pick gap [Source: Fantasy Life citing Leone]
- Real-time ADP value (draft-time ADP vs your pick) is **almost as impactful** as closing-line value
- Top 20% in ADP value/capital: regular-season advance rates **+~25%**, playoff win rates **+~5–10%** [CONFIRMED — ETR]

### Fast vs slow drafts [CONFIRMED — ETR]

- Slow drafts skew earlier in offseason (May–July); confounds timing analysis
- After adjusting for month: slow drafts only **slightly worse** for top ADP Value buckets
- May slow drafts notably worse; August slow drafts roughly neutral
- For 150 entries: **prioritize fast drafts** for volume; slow drafts optional in early window for softer rooms

### Recommended timing for 150-entry portfolio [TENTATIVE — synthesis]

Reconciles ETR (live players + CLV balance) with 4for4 (preseason = sharpest volume) [@sources/4for4-bbm7-guide-series-2026-06-18.md]:

Split the portfolio across windows to capture both edges:

| Window | Share of entries | Goal |
|--------|------------------|------|
| **May–June** (post-NFL Draft) | 20–30% (~30–45) | CLV on rookie WRs, landing-spot mispricings, post-draft ADP gaps |
| **Mid-July – mid-August** | 50–60% (~75–90) | **Core window** — ETR optimal balance of CLV + live players |
| **Late August – September** | 15–25% (~25–35) | 4for4: highest ceiling teams; injury clarity; pad portfolio per preseason guidance |

**Do not** put all 150 in May–June (health cliff) or all in September (no CLV left).

**4for4 nuance:** Jul–early Aug drafts skew toward **low-score outliers**; late Aug/Sep toward **high-score outliers** — align core volume with ETR mid-July–mid-August, push final tranche into late Aug/Sep for clarity.

Within each window, diversify **archetypes** per @concepts/best-ball-mania-winners.md — timing and construction are independent axes.

### What to monitor by month

| Month | Watch for | Draft action |
|-------|-----------|--------------|
| May | NFL schedule (byes), rookie landing spots | Target mispriced rookies; build stacks with known assignments |
| June | OTAs, minicamp buzz | Fade players with bad reports still at old ADP |
| July | Training camp opens | Shift bulk of volume here; capitalize on pre-camp ADP |
| August | Preseason games, injuries | Injury fades; confirm roles; finalize portfolio |
| September | Roster cuts, final ADP | Last entries only for specific values; CLV mostly gone |

## Snippets

> "I think the best time to draft is likely July and August." [Source: Mike Leone, ETR Best Ball Mania Manifesto Part 2]

> "The goal is simple: build teams with players at prices that won't exist in two weeks. You're pulling the ladder up behind you." [Source: Fantasy Life, Approaching BBM 2026]

> "Good August values on guys who slide down the ADP board simply because of negative reports or perhaps a minor injury." [Source: Draft Sharks, Best Ball Draft Strategy 2026]

> "Closing-line ADP is the average drafted position at the very end of the tournament. For BBM, that is the end of August or early September." [Source: 4for4, How Winners Draft WRs in BBM]

## Dead Ends

- **Wait until September for bye weeks** — byes are on the May schedule; August is for injuries/roles, not bye discovery
- **Draft everything in May for max CLV** — BBM3 data shows May teams underperform on live-player count at playoffs
- **Single "perfect" draft day** — with 150 entries, timing diversification beats picking one date
