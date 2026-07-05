---
name: nfl-fanduel-slate-prep
description: >-
  FanDuel NFL DFS slate prep for gambling-wiki W8 — read projection CSV exports
  (Stokastic/FantasyLabs), apply wiki GPP playbook, run pydfs lineup gen, write
  briefs/ slate card. Use when user says slate prep, FanDuel NFL, DFS lineups,
  Stokastic export, or Sunday NFL DFS.
---

# NFL FanDuel slate prep (W8)

Operator stack: **FanDuel GPP** (not Underdog BBM7, not Hard Rock book). Read wiki playbook before building.

## Wiki pages (read first)

- @wiki/concepts/nfl-weekly-slate-hub-workflow.md — **if hub brief exists**, read `briefs/{season}-w{NN}-slate-hub.md` first; do not re-research schedule/weather/injury
- @wiki/entities/platforms/fanduel.md — half-PPR, 4-player stack cap
- @wiki/sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md — game stacks, MME pools
- @wiki/entities/tools/stokastic-dfs.md — CSV export workflow (primary paid tool)
- @wiki/entities/tools/fantasylabs-dfs.md — alternate paid + CSV export
- @wiki/entities/tools/pydfs-lineup-optimizer.md — FOSS lineup engine

## Inputs

1. **Projection CSV** in `research to be indexed/` from Stokastic spreadsheet export or FantasyLabs model export
2. Optional: slate date, contest name, entry count (default 150 MME), core locks/excludes from user

## Workflow

### 1. Normalize CSV (if from paid export)

```bash
python3 scripts/normalize_dfs_projection_csv.py \
  --in "research to be indexed/<export>.csv" \
  --out "research to be indexed/fanduel-nfl-pydfs-YYYY-MM-DD.csv" \
  --source stokastic
```

If normalize fails, inspect headers — ensure **Team** column exists in paid export. Output must match FanDuel pydfs columns (see `@entities/tools/pydfs-lineup-optimizer.md`).

### 2. Generate lineups

```bash
pip install pydfs-lineup-optimizer   # once; MIT license — see tool page

python3 scripts/fanduel_slate_optimize.py \
  --csv "research to be indexed/fanduel-nfl-pydfs-YYYY-MM-DD.csv" \
  --count 150 \
  --max-exposure 0.35 \
  --stack qb:2 \
  --out "briefs/fanduel-lineups-YYYY-MM-DD.csv"
```

Tune `--count` and `--stack` per slate size. FanDuel upload expects player names matching site IDs — verify a sample lineup in FD upload UI before mass entry.

### 3. Write slate brief (`briefs/YYYY-MM-DD_fanduel-nfl-slate.md`)

Include:

| Section | Content |
|---------|---------|
| **Slate environment** | Top 3 game stacks (Vegas totals, both QBs) |
| **Chalk RBs** | High ownership backs to accept |
| **Leverage WR/TE** | Low-owned pass-catchers with stack fit |
| **Core locks** | User/core plays in all or most lineups |
| **Exposure notes** | Max exposure settings used |
| **Upload file** | Path to `briefs/fanduel-lineups-*.csv` |

Apply K124 rules: 3 game environments × 2 QBs for MME; RB in flex on half-PPR; avoid TE flex; leave ≤$500 salary unused.

### 4. Do not

- Scrape Stokastic/FantasyLabs (ToS)
- Commit paid projection CSVs to public git (briefs/ and research folders are gitignored)
- Conflate with BBM7 Underdog draft advice

## Paid tool without CSV

If user has Stokastic/Labs UI only: produce **slate brief + stack plan** from wiki + injury news; skip pydfs step until export available.

## Integration limits

**No MCP server** exists for any major DFS optimizer. Integration = CSV drop + scripts above.
