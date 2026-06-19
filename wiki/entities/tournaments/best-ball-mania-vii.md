---
title: Best Ball Mania VII (2026)
type: entity
tags: [entity, tournament, best-ball, underdog, bbm7, nfl]
keywords: [best-ball-mania-vii, bbm7, underdog-fantasy, playoff-bracket, half-ppr, snake-draft]
related:
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-playoff-week-construction.md
  - concepts/bbm7-portfolio-construction.md
  - concepts/best-ball-strategy.md
  - concepts/best-ball-mania-winners.md
  - concepts/best-ball-draft-timing.md
  - concepts/bankroll-management.md
  - entities/platforms/underdog-fantasy.md
  - entities/sports/nfl-betting.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/fantasysixpack-bbm-new-meta-2026-06-08.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
  - sources/fantasy-guru-bbm-tactics-2026-06-08.md
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @entities/platforms/underdog-fantasy.md — parent platform
- @concepts/best-ball-strategy.md — roster construction and portfolio approach
- @concepts/best-ball-mania-winners.md — BBM1–BBM6 winner patterns to inform BBM7 builds
- @concepts/bankroll-management.md — treat max-enter fees as GPP bankroll

## Raw Concept

Underdog Fantasy's **2026 NFL season** flagship best-ball tournament. Live since **2026-04-28**. Primary source: [Best Ball Mania VII | Underdog Help](https://help.underdogfantasy.com/en/articles/14785343-best-ball-mania-vii) [CONFIRMED].

## Narrative

### Entry & prize pool [CONFIRMED]

| Item | Value |
|------|-------|
| Entry fee | **$25** |
| Total prize pool | **$15,000,000** |
| Max entries per user | **150** (standard BBM cap; verify in-app before max-entering) |
| 1st place | **$2,000,000** |
| 2nd place | **$1,000,000** |
| 3rd place | $500,000 |
| Min cash (Final, ranks 301–667) | **$3,750** |
| Regular Season Champion | **$100,000** |

**Bankroll note:** Max-enter = $25 × 150 = **$3,750** — exactly equals the Final min-cash band. One Final seat roughly recoups a full max-enter portfolio before upside.

Estimated field size ~672K entries [TENTATIVE — secondary sources]. Rake ~10.8% [TENTATIVE — carried from BBM6 analysis].

### Draft format [CONFIRMED]

| Item | Value |
|------|-------|
| Teams per draft | 12 |
| Format | **Snake** |
| Rounds | **18** (full roster) |
| Pick timer | Fast: 20–30 sec · Slow: 8 hours [TENTATIVE — BBM standard] |
| Draft window | Opened 2026-04-28; closes at NFL Week 1 kickoff or when contest fills [TENTATIVE] |

**Roster requirements** — auto-optimized best-ball lineup each week:

| Slot | Count |
|------|-------|
| QB | 1 |
| RB | 2 |
| WR | 3 |
| TE | 1 |
| Flex (RB/WR/TE) | 1 |
| Bench | 10 |
| **Total** | **18** |

No in-season management — no waivers, trades, or lineup setting. Platform selects highest-scoring eligible lineup from your 18-man roster.

### Scoring — half-PPR [CONFIRMED]

| Stat | Points |
|------|--------|
| Reception | **0.5** |
| Rushing/receiving yard | 0.1 |
| Passing yard | 0.04 |
| Passing TD | 4.0 |
| Rushing/receiving TD | 6.0 |
| 2-PT conversion | 2.0 |
| Interception | −1.0 |
| Fumble lost | −2.0 |

No yardage bonuses, no kickers, no team defense. Source: [Daily vs Best Ball Scoring](https://help.underdogfantasy.com/en/articles/11159786-daily-vs-best-ball-scoring).

### Tournament bracket [CONFIRMED structure; pod sizes TENTATIVE]

Four-round gauntlet mirroring the NFL season:

| Round | NFL weeks | Pod size | Advance | Partial prize |
|-------|-----------|----------|---------|---------------|
| **Regular season** | 1–14 | 12 | **Top 2** | ~$25 |
| **Quarterfinals** | 15 | 13 | **Top 1** | ~$75 |
| **Semifinals** | 16 | 16 | **Top 1** | ~$1,000 |
| **Final** | 17 | ~667 | — | $3,750+ |

**Advancement math:** One entry's odds of reaching the Final ≈ (2/12 × 1/13 × 1/16) ≈ **0.08%**.

**Why Week 17 matters:** Final pod is single-week scoring. Roster construction must optimize for **playoff-week correlation and bye avoidance**, not just regular-season point totals.

### Changes from BBM6 → BBM7

Format, scoring, and advancement **unchanged**. Notable payout shifts:

- **Larger Final field:** ~667 paid seats (301–667 @ $3,750) vs ~539 in BBM6
- Minor reshuffle of mid-tier prizes (10th place $100,240 vs $125,000 in BBM6)
- Entry, pool, top-2 prizes identical ($25 / $15M / $2M / $1M)

### Draft prep implications

1. **Draft timing** — core volume **mid-July to mid-August**; see @concepts/best-ball-draft-timing.md. Bye weeks are known from May schedule — August is for injury/role clarity, not bye discovery.
2. **Early drafts (May–June)** — widest ADP gaps; allocate ~20–30% of portfolio for CLV on rookies and mispricings [Source: Fantasy Life, AdVSOvT79tA]
3. **Portfolio approach** — 150 entries standard; diversify **archetypes** and **draft windows**
4. **Half-PPR** — reception value favors high-target WRs and pass-catching RBs vs full-PPR DFS
5. **Playoff construction** — Week 15–17 bye cliffs and game-environment stacks drive tournament equity

## Snippets

> "Best Ball Mania VII went live April 28, 2026 with a $15 million prize pool and $2 million first place." [Source: https://help.underdogfantasy.com/en/articles/14785343-best-ball-mania-vii (retrieved 2026-06-18)]

## Dead Ends

- **In-app rules page** (`app.underdogfantasy.com/rules`) — JS-gated; help center article is sufficient for format ingest
- **Exact pod sizes for BBM7** — not on official BBM7 page; 13/16 structure carried from BBM6 [TENTATIVE]
