---
title: Web research — NFL DFS scoring correlations and stacking (June 2026)
type: source
tags: [source, dfs, nfl, correlation, stacking, gpp, w-corr]
keywords: [qb-wr1, bring-back, rb-dst, opposing-passing-game, pydfs, teamstack]
related:
  - concepts/dfs-correlation-stacking.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - entities/tools/pydfs-lineup-optimizer.md
maturity: validated
read_status: deep-read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/dfs-correlation-stacking.md — W-CORR synthesis page for the DIY model
- @concepts/diy-nfl-dfs-model-architecture.md — correlation layer in the larger projection/sim stack
- @entities/tools/pydfs-lineup-optimizer.md — implementation target for stack rules

## Raw Concept

June 2026 web pass to answer one operator question: **what DFS scoring correlations are strong enough to treat as empirical priors, and how should those priors map into pydfs lineup rules?**

| Source | URL | Retrieved | Why it matters |
|-------|-----|-----------|----------------|
| 4for4 correlation tool intro | `https://www.4for4.com/2021/preseason/using-4for4-nfl-dfs-player-correlation-tool` | 2026-06-20 | Gives an explicit example coefficient: QB to WR1 = `0.46` |
| 4for4 DraftKings stacking study | `https://www.4for4.com/2018/preseason/definitive-guide-stacking-draftkings` | 2026-06-20 | Empirical DK stack hit rates, opposing-game lift, negative pairs |
| 4for4 FanDuel stacking study | `https://www.4for4.com/2018/preseason/definitive-guide-stacking-fanduel` | 2026-06-20 | Same framework on half-PPR / no-bonus scoring |
| 4for4 RB-DEF game-script study | `https://www.4for4.com/2019/preseason/rb-def-stack-analyzing-game-script-nfl-dfs` | 2026-06-20 | Clarifies RB + own D/ST is mild positive, not a core stack |
| PFF position-correlation piece | `https://www.pff.com/news/fantasy-football-utilizing-position-correlations-for-dfs-lineup-construction` | 2026-06-20 | Confirms stacking prevalence and opposing-game correlation framing |
| pydfs rules docs | `https://pydfs-lineup-optimizer.readthedocs.io/en/latest/rules.html` | 2026-06-20 | Confirms `TeamStack`, `PositionsStack`, `GameStack`, and opposing-team rules |

## Narrative

### High-confidence reads

1. **QB-WR1 is the anchor correlation** across both sites. It is the strongest same-team positive pair in every public study reviewed.
2. **Bring-backs are justified by measured opposing passing-game lift**, especially on DraftKings where yardage bonuses amplify shootouts.
3. **RB + own D/ST is not a negative pairing**. It is a **mild positive / game-script** stack, but much weaker than QB-pass-catcher pairings.
4. **QB vs opposing D/ST is the cleanest avoid pair**. That is the strongest negative relationship surfaced in the public DFS studies.
5. **FanDuel supports thinner stacks than DraftKings**. Half-PPR and no yardage bonuses reduce the payoff from deeper 3-man and 4-man passing onslaughts.

### Evidence table

| Finding | Evidence |
|---------|----------|
| **QB-WR1 strongest positive** | 4for4's tool article gives a concrete example of `QB-WR1 = 0.46`; both 2018 stacking studies say QB-WR1 is "by far" the strongest positive stack. |
| **QB-TE1 / QB-WR2 next tier** | 4for4 DK says QB-WR2 and QB-TE1 are tied for second; FD says QB-TE1 narrowly edges QB-WR2. |
| **Bring-back logic is real, not just heuristic** | On DK, when a QB scores 25+, the opposing QB also hits 25+ **61.1%** of the time and the opposing WR1 **26.2%**. On FD, those numbers are **25.7%** and **16.3%**. |
| **QB-RB1 is viable but not elite** | DK two-man `QB+RB1` hits 50+ combined **7.5%** of the time; FD `QB+RB1` hits 50+ **4.2%**. |
| **RB1 + own D/ST is mild positive only** | Both 4for4 stacking studies say RB1-D/ST has some correlation, but far less than QB-WR1. The dedicated RB-DEF article says RB1s get a production bump when their defense scores at least 15 fantasy points. |
| **QB vs opposing D/ST is strongest negative** | Both 4for4 stacking studies explicitly call QB vs opposing D/ST the strongest negative stack. |
| **pydfs can encode the core rules** | The docs expose `TeamStack`, `PositionsStack`, `GameStack`, `force_positions_for_opposing_team`, `restrict_positions_for_opposing_team`, and `restrict_positions_for_same_team`. |

### Modeling read for W-CORR

The best public evidence is strongest at the **role level** (`WR1`, `WR2`, `TE1`, `RB1`, opposing `WR1`) rather than at raw player IDs. That suggests using a **role-prior matrix** first, then adjusting pairwise correlations for:

- team total
- spread / game competitiveness
- target concentration
- pass rate over expectation
- site scoring (FanDuel vs DraftKings)

This is a better default than pretending every `QB-WR` or every `RB-DST` pair shares the same coefficient.

## Snippets

> "As further evidence of overall correlation, we see that a quarterback has a `0.46` with his number one wide receiver." [Source: https://www.4for4.com/2021/preseason/using-4for4-nfl-dfs-player-correlation-tool (retrieved 2026-06-20)]

> "QB-WR1 is by far the strongest positively correlated stack." [Source: https://www.4for4.com/2018/preseason/definitive-guide-stacking-draftkings (retrieved 2026-06-20)]

> "QB-Opp DST is by far the strongest negatively correlated stack." [Source: https://www.4for4.com/2018/preseason/definitive-guide-stacking-fanduel (retrieved 2026-06-20)]

> "When a QB posts a 25-point game, there's a 61-percent chance the opposing QB will too. And there's a 25-percent chance the opposing WR1 will do so as well." [Source: https://www.4for4.com/2018/preseason/definitive-guide-stacking-draftkings (retrieved 2026-06-20)]

> "The correlation between RB1 scoring and D/ST scoring isn't the strongest - it's certainly no QB/WR1 correlation - but it has enough relation for us to construct a lineup or two each week using a running back and his team's defense." [Source: https://www.4for4.com/2019/preseason/rb-def-stack-analyzing-game-script-nfl-dfs (retrieved 2026-06-20)]

> "`optimizer.force_positions_for_opposing_team(('QB', 'WR'))`" and "`optimizer.add_stack(TeamStack(3))`" [Source: https://pydfs-lineup-optimizer.readthedocs.io/en/latest/rules.html (retrieved 2026-06-20)]

## Dead Ends

- **Treating RB + own D/ST as a negative pair** — not supported by the evidence reviewed; the public studies describe it as mild positive / script-dependent.
- **Using a single global correlation coefficient per position pair** — too coarse for a usable sim layer; role and game-environment conditioning matter.
