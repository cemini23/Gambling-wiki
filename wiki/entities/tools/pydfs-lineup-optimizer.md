---
title: pydfs-lineup-optimizer
type: entity
tags: [entity, tool, dfs, open-source, python, nfl, fanduel]
keywords: [pydfs, lineup-optimizer, draftkings, fanduel, nfl, mit]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/dfs-correlation-stacking.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/web-nfl-dfs-correlation-stacking-2026-06-20.md
maturity: validated
created: 2026-05-31
updated: 2026-06-20
---

## Relations

- @entities/tools/stokastic-dfs.md — projection CSV source (paid)
- @entities/tools/fantasylabs-dfs.md — alternate CSV source
- @concepts/dfs-correlation-stacking.md — W-CORR default stack priors + bring-back rules
- @sources/web-nfl-dfs-correlation-stacking-2026-06-20.md — empirical correlation scan + pydfs method map
- @entities/platforms/fanduel.md — W8 FanDuel NFL target site
- @.cursor/skills/nfl-fanduel-slate-prep/ — operator slate workflow

## Raw Concept

Open-source **DFS lineup optimizer** (Python) for DraftKings/FanDuel — stacks, exposure limits, multi-lineup generation. **Lineup math only** — projections come from Stokastic/Labs export or custom CSV.

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/DimaKudosh/pydfs-lineup-optimizer |
| **PyPI** | `pydfs-lineup-optimizer` (v3.6.1) |
| **License** | **MIT** [CONFIRMED — `gh api` + PyPI 2026-06-20] |
| **FanDuel NFL** | Supported [CONFIRMED — PyPI readme matrix] |
| **Last push** | 2024-03 [CONFIRMED — GitHub] — maintenance lag; pin version in prod |

## Narrative

### Phase-0 verdict [CONFIRMED 2026-06-20]

**GO** for FOSS lineup generation in W8 FanDuel pipeline. Pair with paid **ownership/projections** (Stokastic or FantasyLabs); pydfs does not simulate contests.

| Check | Result |
|-------|--------|
| License via `gh api` | MIT |
| FanDuel + NFL | Yes |
| Ownership / sims | **No** — use Stokastic sims or hand rules |
| CSV import | `load_players_from_csv()` |

### W8 command path (150 FanDuel lineups)

**Prereq:** `pip install pydfs-lineup-optimizer`

```bash
# 1. Normalize paid export (Stokastic / FantasyLabs)
python3 scripts/normalize_dfs_projection_csv.py \
  --in "research to be indexed/stokastic-nfl-export.csv" \
  --out "research to be indexed/fanduel-nfl-pydfs.csv"

# 2. Generate lineups
python3 scripts/fanduel_slate_optimize.py \
  --csv "research to be indexed/fanduel-nfl-pydfs.csv" \
  --count 150 \
  --max-exposure 0.35 \
  --stack qb:2 \
  --out "briefs/fanduel-lineups.csv"
```

Wrapper scripts live in repo `scripts/` — see @.cursor/skills/nfl-fanduel-slate-prep/.

### CSV format (FanDuel pydfs)

FanDuel site requires: `Id`, `First Name`, `Last Name`, `Position`, `Team`, `Salary`, `FPPG`, `Game`, `Injury Indicator`.

**Best path:** download FanDuel salary CSV at lock → run optimizer directly.

**Paid export path:** `scripts/normalize_dfs_projection_csv.py` maps Stokastic/Labs columns → pydfs format (ensure **Team** column present in export).

Docs: https://pydfs-lineup-optimizer.readthedocs.io/

### Stacking

Default NFL rule set should reflect measured correlations, not generic "more same-team players" logic:

```python
from pydfs_lineup_optimizer import GameStack, PositionsStack, TeamStack

optimizer.add_stack(PositionsStack(['QB', ('WR', 'TE')]))
optimizer.add_stack(TeamStack(3, for_positions=['QB', 'WR', 'TE', 'RB'], max_exposure=0.35))
optimizer.force_positions_for_opposing_team(('QB', 'WR'))
optimizer.restrict_positions_for_opposing_team(['QB'], ['DST'])

# Optional short-slate / shootout setting
optimizer.add_stack(GameStack(5, min_from_team=2))
```

Practical defaults:

- **Core** — `PositionsStack(['QB', ('WR', 'TE')])` because QB-pass-catcher is the strongest public correlation
- **Same-team extension** — `TeamStack(3, ...)` only for condensed/high-total offenses; exposure-cap it
- **Bring-back** — `force_positions_for_opposing_team(('QB', 'WR'))` is the clean built-in single bring-back rule
- **Anti-correlation** — ban QB vs opposing D/ST
- **Do not ban RB + own D/ST** — public DFS studies describe it as **mild positive**, not negative

See @concepts/dfs-correlation-stacking.md for the empirical cheat table and role-prior logic.

### Failure modes

- **Stale pydfs** — DK/FD format changes; test one lineup upload each season opener
- **Missing projections** — garbage-in from wrong CSV columns; always run normalize step
- **No GPP sim ROI** — pydfs optimizes points, not ownership; use Stokastic sims for MME validation

## Snippets

> MIT License — DimaKudosh/pydfs-lineup-optimizer [CONFIRMED: gh api 2026-06-20]

> Listed under "Classical ML / DFS" in Gemini landscape — reference for DFS modeling. [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md]

## Dead Ends

- pydfs alone as **full GPP solution** — no ownership/contest sim; insufficient vs field
- **chanzer0/NFL-DFS-Tools** — no LICENSE file on GitHub [2026-06-20]; sim stack **REFERENCE only** until license clarified
