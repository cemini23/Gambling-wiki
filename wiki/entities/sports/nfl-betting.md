---
title: NFL betting
type: entity
tags: [entity, sport, nfl, football, sports-betting]
keywords: [nfl, football, spreads, props, totals, key-numbers, clv, injury-report]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/best-ball-strategy.md
  - entities/tournaments/best-ball-mania-vii.md
  - concepts/dfs-strategy-overview.md
  - concepts/line-shopping-and-clv.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - concepts/sharp-vs-soft-books.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/bankroll-management.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/platforms/hard-rock-bet.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/platforms/underdog-fantasy.md
  - entities/platforms/underdog-pickem.md
  - entities/platforms/prizepicks.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - meta/nfl-slate-prefetch-cadence.md
  - concepts/nfl-offseason-research-cadence.md
  - meta/nfl-offseason-weekly-cadence.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
  - sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md
  - sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md
  - sources/sharp-nfl-rb-prop-unders-2026-08-13.md
  - sources/rotoviz-preseason-paywall-2026-08-14.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - concepts/free-slate-context.md
maturity: validated
created: 2026-05-31
updated: 2026-08-15
---

## Relations

- @entities/platforms/hard-rock-bet.md — operator primary NFL book (W8)
- @concepts/line-shopping-and-clv.md — CLV workflow
- @concepts/best-ball-strategy.md — shared player research stack
- @concepts/dfs-strategy-overview.md — FanDuel/Underdog DFS overlap
- @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md — K124 process primer
- @sources/sharp-nfl-rb-prop-unders-2026-08-13.md — 2026 season-long RB rushing unders (volume thesis)
- @sources/rotoviz-preseason-paywall-2026-08-14.md — OL/target-share/ADP titles (paywalled)
- @sources/daily-digest-rss-industry-2026-08-14.md — DKeX football contracts + Colorado deposit cap
- @concepts/free-slate-context.md — Open-Meteo wind/precip for outdoor totals

## Raw Concept

NFL-specific betting and fantasy context — key numbers, season structure, market types, operator W8 workflow.

## Narrative

### W8 operator stack (2026 season)

| Lane | Platform | Wiki home |
|------|----------|-----------|
| Sportsbook + casino | Hard Rock Bet | @entities/platforms/hard-rock-bet.md |
| Daily fantasy GPP | FanDuel | @entities/platforms/fanduel.md |
| Best ball | Underdog BBM7 | @entities/tournaments/best-ball-mania-vii.md |
| DFS pick'em / props lounges | PrizePicks, Underdog Pick'em | @entities/platforms/prizepicks.md, @entities/platforms/underdog-pickem.md, @concepts/diy-nfl-pickem-props-tool-architecture.md (K147 — **no tool yet**) |

Same injury and game-environment research feeds all four; **betting** is vs the line, **DFS/best ball** vs the field, **pick'em** is binary O/U on posted stat lines.

**In-season weekly cadence:** research once in gambling-wiki → hub brief → launch each tool session separately. See @concepts/nfl-weekly-slate-hub-workflow.md.

**Offseason (Jul–Aug):** weekly camp/depth research only — no pick'em entries until tool ships. See @concepts/nfl-offseason-research-cadence.md.

### Key numbers (spread) [CONFIRMED]

3 and 7 dominate NFL margins (FG + TD). Order of frequency: **3 > 7 > 10 > 6 > 14**. Half-points around 3 and 7 are the highest-ROI shop targets; 1/4/5 are rare margins.

| Line move | EV note |
|-----------|---------|
| -3 → -2.5 (fav) | Often worth worse price |
| +3 → +3.5 (dog) | Often worth worse price |
| +6.5 → +7 | Valuable on dogs |

See @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md for situational angles (weather, rest, division, backup QB).

### Market menu

| Market | Notes | CLV tracking |
|--------|-------|--------------|
| Spread / ML / total | Highest liquidity | **Primary** — log open vs close |
| Player props | Higher hold (~30¢ vig on soft books) | Secondary; more FLB on longshots |
| Season-long player props | Volume × game-script bets (e.g. rush yards) | Log close vs projection, not W-L |
| SGP | Correlation priced — see @concepts/parlay-and-correlated-bets.md | Usually -EV unless correlated edge |
| Futures | Division, SB — capital locked months | Low frequency |
| Live | Fast moves on drives | Supplement pre-game; pre-set rules |

### Process (season-long) [CONFIRMED]

1. **Line shop** across Hard Rock + FanDuel + others for best number
2. **Flat 1–2% units** — @concepts/bankroll-management.md
3. **Track CLV** — positive close beat = edge signal stronger than W-L
4. **Avoid parlay-core strategy** — hold compounds per leg

### Season rhythm

| Phase | Betting notes |
|-------|---------------|
| **Jun–Aug** | BBM7 drafts; futures move on camp news |
| **Preseason** | Unreliable lines, low limits — mostly ignore for +EV |
| **Regular season** | Sun/Mon/Thu slates; injury report **Wed/Fri** moves |
| **Playoffs** | Tighter lines; public on favorites |

### Injury / news cadence

- **Wed** — initial practice report
- **Fri** — final injury designations (major line moves)
- **Inactive lists** — 90 min pre-kick (props, totals)

Cross-link DFS: same OUT tags move FanDuel ownership and Underdog ADP.

### 2026 season-long RB unders (preseason) [TENTATIVE]

Sharp (Hirsch, 2026-08-13): **Taylor Under 1224.5 rush yards (-105)** and **Hubbard Under 700 (-114)** — both **carry-share / committee / trailing-script** theses, not talent fades. Use as a template for K147 season-long O/U; do not import as weekly pick'em. Hub: `@sources/sharp-nfl-rb-prop-unders-2026-08-13.md`.

### Live betting hygiene

- Markets overreact to early TDs; slow starts can improve live unders
- Do not size live bets larger than pre-game unit — set rules before kickoff
- **In-game win probability models** (K137 — @sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md): public-state WP can match market **calibration** (ECE ~0.027–0.029) without implying +EV — residual market edge is **live information** beyond shared feeds. Benchmark vs closing in-game line; keep **CLV** separate from Brier/ECE checks

### Open-source ML note

Gemini landscape cites NBA ML repos as analog class — **NFL models need separate validation**; see @sources/gemini-github-sports-betting-landscape-2026-05-30.md.

## Snippets

> "If you consistently beat [the closing line] … you are very likely betting with a real edge." [Source: @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md]

> "Hard Rock's quality of NFL odds – 20-cent vig on standard markets and 30-cent vig on secondary opportunities." [Source: @sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md]
