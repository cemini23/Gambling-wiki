---
title: DFS strategy overview
type: concept
tags: [concept, dfs, daily-fantasy, roster-construction]
keywords: [dfs, gpp, cash, ownership, stacking, correlation]
related:
  - concepts/best-ball-strategy.md
  - concepts/bankroll-management.md
  - concepts/parlay-and-correlated-bets.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/platforms/underdog-fantasy.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/best-ball-strategy.md — season-long variant
- @entities/platforms/draftkings.md — DraftKings DFS
- @entities/platforms/fanduel.md — FanDuel DFS

## Raw Concept

Daily fantasy sports (DFS) — GPP vs cash, stacking, ownership leverage, bankroll.

## Narrative

### Formats

| Format | Goal | Variance |
|--------|------|----------|
| **Cash (50/50, H2H)** | Top ~50% cash | Lower |
| **GPP / tournament** | Top-heavy payout | High |
| **Single-game (Showdown)** | One-game slate | High correlation |

### Core levers

1. **Projection edge** — model vs field
2. **Ownership leverage** — low-owned players in GPPs when projection edge exists
3. **Stacking** — QB + WR(s), game stack for correlation
4. **Bankroll** — see `@concepts/bankroll-management.md`; GPP is high-variance

### Tools

- **pydfs-lineup-optimizer** — open-source lineup generation (`@entities/tools/pydfs-lineup-optimizer.md`); Phase-0 license check before install
- Paid optimizers — ownership leverage, late swap, contest sims
- Projection sites — model quality dominates optimizer output

Gemini landscape flags classical ML DFS repos as **reference for DFS modeling**, not spread-betting edge [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md].

### Not prediction markets

DFS is **contest vs field**, not against the house line (though rake exists). Different math from sports spread betting.

## Snippets

> `pydfs-lineup-optimizer` — CONDITIONAL-GO Phase-0 for DFS lane. [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md]
