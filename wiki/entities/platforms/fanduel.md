---
title: FanDuel
type: entity
tags: [entity, platform, sportsbook, dfs, us-legal, nfl]
keywords: [fanduel, fd, sportsbook, dfs, nfl-gpp, half-ppr, showdown]
related:
  - entities/platforms/draftkings.md
  - entities/platforms/hard-rock-bet.md
  - concepts/sports-betting-fundamentals.md
  - concepts/dfs-strategy-overview.md
  - concepts/sharp-vs-soft-books.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/people/rufus-peabody.md
  - sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: validated
created: 2026-05-31
updated: 2026-08-31
---

## Relations

- @entities/platforms/draftkings.md — primary US competitor (DFS + book)
- @entities/platforms/hard-rock-bet.md — cross-shop sportsbook peer (W8)
- @concepts/dfs-strategy-overview.md — NFL GPP framework
- @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md — K124 FanDuel-relevant GPP playbook
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — Predicts sports → Crypto.com (Q2 2026)
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — NFL official betting partner (with DK / Fanatics)

## Raw Concept

Major US legal operator (Flutter-owned). **W8 lanes:** NFL DFS GPP/tournaments + soft-book line shop vs Hard Rock handle.

## Narrative

### Sportsbook (CLV cross-shop)

Same **soft book** retail profile as DraftKings. Industry reviews often rank FanDuel among **sharper spread prices** on NFL — use for line shopping even when primary handle is Hard Rock.

### FanDuel Predicts (PM, Aug 2026) [CONFIRMED via EH]

Q2: sports/novelties on **Predicts** move to **Crypto.com**; CME retained for financials. Flutter flagged **~$50M** market-making revenue for 2026 ($6M in Q2). Predicts is **not** the FanDuel sportsbook line — shop it as a third venue (book vs Kalshi vs Predicts/Crypto.com). Hub: `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`.

### NFL DFS (operator primary DFS lane)

| Setting | FanDuel NFL |
|---------|-------------|
| Scoring | **Half-PPR** |
| Team stack cap | **4** players from one team (vs DK 5) |
| Main slates | Sun/Mon/Thu + alt slates |
| Showdown | Single-game; high correlation |

### GPP strategy summary [CONFIRMED — @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md]

**Goal:** top-1% finish, not min-cash.

1. **Game stacks** — default 3×1 (QB + 2 pass-catchers + opp WR); 3×2 in smaller fields; 4×1 on short slates
2. **Game selection** — high Vegas totals, low QB pressure rate, rising totals through week
3. **RB workload** — secure-touch backs for floor; chalk RB ownership acceptable
4. **WR/TE leverage** — lower-owned pass-catchers (UPWR thesis: targets + air yards)
5. **Flex** — RB often best on half-PPR; **avoid TE in flex** for GPP ceiling
6. **Salary** — leave ≤ $500 on table
7. **MME (150 max)** — 3 game environments × both QBs; 5–10 RBs; 15–30 WRs; 4–6 TEs; 4–8 DST; max 2 off-stack players per team

### Bankroll

GPP = high variance — size entries per @concepts/bankroll-management.md; separate from Hard Rock sportsbook roll and Underdog BBM7 draft budget.

### Tools

- `@entities/tools/pydfs-lineup-optimizer.md` — FOSS lineup gen (MIT; see `scripts/fanduel_slate_optimize.py`)
- `@entities/tools/stokastic-dfs.md` — recommended paid projections/sims (W8)
- `@entities/tools/fantasylabs-dfs.md` — alternate paid + CSV export (ETR bundle)

## Snippets

> "On half-point PPR sites like FanDuel … consider using a running back in your flex spot for stability." [Source: @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md]

> "When entering high-stakes or large-field GPP contests, the goal is to secure a top finish, not just to cash." [Source: same]
