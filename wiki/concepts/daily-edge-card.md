---
title: Daily Hard Rock edge card
type: concept
tags: [concept, clv, hard-rock, edge, kelly, daily-card]
keywords: [daily-edge-card, de-vig, hard-rock, market-fair, clv]
related:
  - concepts/line-shopping-and-clv.md
  - concepts/vig-and-hold.md
  - concepts/kelly-criterion-betting.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/favorite-longshot-bias.md
  - entities/platforms/hard-rock-bet.md
  - entities/sports/nfl-betting.md
  - entities/platforms/pinnacle.md
  - concepts/free-slate-context.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @concepts/line-shopping-and-clv.md — skill metric is CLV vs sharp close, not W/L
- @concepts/vig-and-hold.md — de-vig before claiming edge
- @concepts/kelly-criterion-betting.md — quarter-Kelly on the single ticket
- @entities/platforms/hard-rock-bet.md — target book (soft); never treat as fair
- @concepts/free-slate-context.md — Open-Meteo + MLB pitchers for unders tickets (not EV)

## Raw Concept

Runnable **market-relative** daily card: de-vig a two-sided **reference** (Pinnacle / consensus), compare to **Hard Rock**, rank only spots that clear vig + a 2% EV gate. Not a projection model. Not auto-bet.

## Narrative

### Why this exists

Gambling-wiki had Kelly / vig / CLV as **prose**. Super-audit 2026-08-15 (5 auditors, all FAIL): no executable edge engine. P0 is this CLI, not CeminiDFS and not K147.

### Run

```bash
python scripts/daily_edge_card.py --csv config/hr_lines.example.csv --bankroll 1000
# copy the example → config/hr_lines.csv (gitignored if you keep it under briefs/)
python scripts/daily_edge_card.py --csv path/to/today.csv --out briefs/YYYY-MM-DD_edge-card.md
```

Optional live dump (does not replace the CSV):

```bash
# THE_ODDS_API_KEY in env only — never commit
python scripts/daily_edge_card.py --fetch-odds-api --odds-sport americanfootball_nfl
```

### Math (canon)

1. Both sides of the **reference** → implied probs → **multiplicative de-vig** → `fair_p`
2. `EV = fair_p × HR_decimal − 1`
3. Gate: `EV ≥ 2%`, reference hold ≤ 8%, capture age ≤ 6h
4. Stake = `min(quarter-Kelly, 5% bankroll)`
5. **BET / WATCH / PASS** — lottery SGPs stay off this card

`fair_p` is **market_fair_p**, not “true” win probability. Tiny edges are often timestamp noise.

### Operator loop

1. Type today’s Pinnacle (or best sharp) **and** Hard Rock two-sided prices into the CSV.
2. Run the card. Verify the HR number still live.
3. Place **manually**.
4. Next day: grade CLV vs close (ledger not shipped yet — P1).

### What this is not

- NFL projection / pick’em distributions (K147)
- FanDuel GPP optimizer (CeminiDFS)
- Hard Rock scraper / auto-submit
- Promo SGP builder (separate, entertainment)

## Snippets

> De-vig the sharp two-way, then ask whether Hard Rock is worse than that fair. If it is not, there is no sportsbook edge to size. [Source: super-audit 2026-08-15]
