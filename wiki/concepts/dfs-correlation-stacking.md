---
title: DFS correlation and stacking
type: concept
tags: [concept, dfs, nfl, correlation, stacking, simulation, w-corr]
keywords: [qb-wr1, bring-back, rb-dst, cholesky, gaussian-copula, pydfs]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-strategy-overview.md
  - entities/tools/pydfs-lineup-optimizer.md
  - sources/web-nfl-dfs-correlation-stacking-2026-06-20.md
  - concepts/pickem-slip-ev-and-correlation.md
maturity: draft
created: 2026-06-20
updated: 2026-07-05
---

## Relations

- @concepts/pickem-slip-ev-and-correlation.md — copula priors for same-game pick'em stacks
- @concepts/diy-nfl-dfs-model-architecture.md — W-CORR layer inside the full DIY NFL model
- @concepts/dfs-strategy-overview.md — high-level DFS/GPP stack context
- @entities/tools/pydfs-lineup-optimizer.md — implementation target for lineup rules
- @sources/web-nfl-dfs-correlation-stacking-2026-06-20.md — underlying empirical research pass

## Raw Concept

W-CORR layer for the DIY NFL DFS stack: translate **empirically measured role-level scoring correlations** into both (a) a simulation-ready covariance structure and (b) sane default stack rules in `pydfs-lineup-optimizer`.

## Narrative

### Correlation cheat table

| Pair / pattern | Empirical read | Measured support | Modeling default | Optimizer implication |
|----------------|----------------|------------------|------------------|-----------------------|
| **QB + WR1** | Clear strongest same-team positive | 4for4 tool example: `0.46`; also the best two-man stack on both DK and FD [CONFIRMED] | **Core positive prior**; start around `+0.40` to `+0.50` before game-level adjustments | Make every tournament lineup start with a QB + primary pass-catcher stack |
| **QB + TE1 / WR2** | Next-best same-team pass-catching pairs | 4for4 DK: QB-WR2 and QB-TE1 tied for second; FD: QB-TE1 narrowly ahead [CONFIRMED] | **Secondary positive prior** around `+0.22` to `+0.35` | Use as the second pass-catcher tier when WR1 is unavailable or salary-sensitive |
| **QB + RB1** | Slight positive, viable because it captures total TD share | DK `QB+RB1` 50+ combined: `7.5%`; FD `QB+RB1` 50+: `4.2%` [CONFIRMED] | **Small positive prior** around `+0.05` to `+0.15` | Allowed as a secondary or 3-man addition; do not force it globally |
| **QB + opposing QB / opposing WR1** | Bring-back signal exists via opposing passing-game lift | When QB scores 25+, DK: Opp QB `61.1%`, Opp WR1 `26.2%`; FD: Opp QB `25.7%`, Opp WR1 `16.3%` [CONFIRMED] | **Contextual positive prior**; stronger in high-total close games | Use bring-backs for shootouts, especially DK and smaller/slimmer game pools |
| **RB1 + own D/ST** | Mild positive / game-script stack, not a core correlation | 4for4 says some correlation exists but far weaker than QB-WR1; RB1s get a bump when their defense scores 15+ [CONFIRMED] | **Small positive prior** around `+0.05` to `+0.10` | Allow as a contrarian script bet; do not center lineup construction on it |
| **QB + opposing D/ST** | Strongest negative pair in public studies | Both 4for4 studies flag this as the strongest negative stack [CONFIRMED] | **Hard negative prior** around `-0.30` to `-0.40` | Ban in optimizer rules |
| **Deep 4-man onslaughts on FanDuel** | Much weaker than on DraftKings | FD four-man 100+ hit rates top out at `0.8%`; FD 3-man stacks also degrade faster [CONFIRMED] | Reduce tail dependence for deeper FD stacks | Prefer `2-man` or light `3-man` FD stacks; reserve `4-man` for short slates |

### Cholesky / copula method

Use a **Gaussian copula with role-conditioned correlations**, not a raw multivariate normal on fantasy points.

1. **Build player marginals first.**  
   For each player `i`, simulate counting stats or fantasy points from your projection layer and define a marginal CDF `F_i`.

2. **Start from a role-prior matrix.**  
   Map each player into a role bucket such as `QB`, `WR1`, `WR2`, `TE1`, `RB1`, `DST`, `Opp WR1`, then assign base correlations from the cheat table above.

3. **Apply game-level adjustments.**  
   Adjust each pairwise base correlation by environment:
   - `+0.03` to `+0.08` for close, high-total games on bring-back pairs
   - `-0.03` to `-0.08` for large-favorite opposing bring-backs
   - `+0.03` to `+0.06` for concentrated target trees
   - slightly lower pass-catching correlations on FanDuel than DraftKings

4. **Project to a valid correlation matrix.**  
   Symmetrize `Sigma`, clip off-diagonals into `[-0.95, 0.95]`, floor tiny negative eigenvalues, then renormalize the diagonal to `1.0`.

5. **Draw correlated uniforms.**  
   Sample `z ~ N(0, Sigma)`, convert to uniforms `u_i = Phi(z_i)`, then transform back into player outcomes with `x_i = F_i^-1(u_i)`.

6. **If you only need a simple normal sim, use Cholesky directly.**  
   With `L = chol(Sigma)` and `eps ~ N(0, I)`, sample `z = L eps`.  
   But for real DFS distributions, the **copula path is better** because fantasy outcomes are skewed and heavy-tailed.

### Default stack rules for `pydfs`

#### Baseline main-slate rule

```python
from pydfs_lineup_optimizer import TeamStack, PositionsStack

optimizer.add_stack(PositionsStack(['QB', ('WR', 'TE')]))
optimizer.add_stack(
    TeamStack(3, for_positions=['QB', 'WR', 'TE', 'RB'], max_exposure=0.35)
)
```

Interpretation:

- `PositionsStack(['QB', ('WR', 'TE')])` is the default because QB-pass-catcher is the strongest empirical relationship.
- `TeamStack(3, ...)` is the optional extension for a **3x0 / 3x1-style core**; cap exposure because broad `TeamStack` can generate too many mediocre same-team 3-mans if left unchecked.

#### Bring-back logic

```python
optimizer.force_positions_for_opposing_team(('QB', 'WR'))
```

Use this as the default **single bring-back** rule on:

- high-total games
- spreads roughly within one score
- condensed opposing target trees

For heavier shootout assumptions, use a game stack instead of a generic team stack:

```python
from pydfs_lineup_optimizer import GameStack

optimizer.add_stack(GameStack(5, min_from_team=2))
```

That is the closest built-in expression of a **3x2** game stack. For exact `3x1` vs `3x2` archetypes by role, you may still want post-filtering or custom groups.

#### Negative-correlation rules

```python
optimizer.restrict_positions_for_opposing_team(['QB'], ['DST'])
```

Default read:

- **Ban** QB vs opposing D/ST
- **Do not ban** RB with his own D/ST; that pair is mild positive, not negative
- **Do not force** RB + D/ST either; treat it as a game-script lever, not a core stack

### Practical defaults by site

| Site | Default build |
|------|---------------|
| **DraftKings** | QB + WR/TE core; single bring-back by default in strong environments; 3-man passing stacks more viable |
| **FanDuel** | QB + WR/TE core still mandatory, but keep stacks thinner; prefer 2-man and selective 3-man constructions because half-PPR/no bonuses reduce deep-stack payoff |

## Snippets

> "QB-WR1 is by far the strongest positively correlated stack." [Source: @sources/web-nfl-dfs-correlation-stacking-2026-06-20.md]

> "When a QB posts a 25-point game, there's a 61-percent chance the opposing QB will too. And there's a 25-percent chance the opposing WR1 will do so as well." [Source: @sources/web-nfl-dfs-correlation-stacking-2026-06-20.md]

> "The correlation between RB1 scoring and D/ST scoring isn't the strongest - it's certainly no QB/WR1 correlation." [Source: @sources/web-nfl-dfs-correlation-stacking-2026-06-20.md]

## Dead Ends

- **Global anti-correlation rule for RB + own D/ST** — rejected; public evidence does not support calling this pair negative.
- **One-size-fits-all same-team correlation matrix** — rejected; role and environment conditioning matter too much.
