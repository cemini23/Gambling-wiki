---
title: PrizePicks
type: entity
tags: [entity, platform, pickem, props, dfs-lounge, nfl]
keywords: [prizepicks, pickem, player-props, demon, goblin, power-play, flex, reboot, dnp]
related:
  - concepts/pickem-stat-type-mapping.md
  - concepts/pickem-operator-workflow.md
  - concepts/pickem-legal-and-tos-posture.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/pickem-payout-and-breakeven.md
  - concepts/pickem-legal-and-tos-posture.md
  - concepts/pickem-stat-type-mapping.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/bankroll-management.md
  - entities/sports/nfl-betting.md
  - entities/platforms/underdog-pickem.md
  - sources/fantasylabs-picklabs-launch-2026-07-05.md
  - sources/research-diy-pickem-props-master-plan-2026-07-05.md
maturity: validated
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/diy-nfl-pickem-props-tool-architecture.md — primary research hub
- @concepts/pickem-payout-and-breakeven.md — Power/Flex multipliers and breakeven math (K147)
- @concepts/pickem-legal-and-tos-posture.md — cross-platform ToS synthesis
- @concepts/pickem-stat-type-mapping.md — CeminiDFS → PrizePicks stat mapping
- @sources/research-diy-pickem-props-master-plan-2026-07-05.md — W-PLATFORM-PP workstream (SA-01)
- @entities/platforms/underdog-pickem.md — competitor pick'em lounge
- @entities/sports/nfl-betting.md — sportsbook props lane (benchmark)

## Raw Concept

US **DFS pick'em** operator — binary over/under on player stat lines in 2–6 leg slips (Power Play, Flex Play). NBA-heavy brand; NFL season is a **secondary but fully supported** research target for K147. No public API; lines are operator-posted and multiplier-adjusted per slip.

## Narrative

### Product summary

PrizePicks Player Picks are **not** salary-cap DFS. The user selects 2–6 athletes, calls **More** or **Less** on a posted stat projection per athlete, then chooses **Power Play** (all legs must hit) or **Flex Play** (partial credit on misses). Payout multipliers are **pre-disclosed on the submission screen** before entry; they can vary by demon/goblin mix, same-game correlation, promos, and combined Player + Team pick lineups. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]

Operator also offers **Team Picks** and **Culture Picks** (event contracts via PrizePicks Predict) and **Free2Play** nationwide — out of scope for K147 v1 except as geo context.

### Phase-0 checklist

- [x] **State availability / geo** — Player Picks in **36 states + Washington D.C.**; age 18+ (most), 19+ (AL, CO), 21+ (AZ, IL, MA, VA). Free2Play in all 50 + D.C. State-specific rules: CO min 3 picks; MO/AR/NH full-game only; college-sport restrictions in several states (NFL unaffected). Geolocation enforced; VPN/spoofing = account termination. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/eligibility (retrieved 2026-07-05)] [Source: https://www.prizepicks.com/resources/states-where-you-can-play-prizepicks (retrieved 2026-07-05)]
- [x] **Payout tables (standard Player Pick lineups)** — see table below. Official rates updated **2026-07-02**. Demon/goblin and same-game combos can alter displayed multiplier. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]
- [x] **Demon / Goblin / standard** — Standard: More or Less. Demon (red): harder line, **More only**, boosts multiplier (up to **2000x** on 6-leg builds). Goblin (green): easier line, **More only**, reduces multiplier. Mix allowed; multiplier shown live before lock. Promos generally exclude demon/goblin lineups. [CONFIRMED] [Source: https://www.prizepicks.com/demons-and-goblins (retrieved 2026-07-05)] [Source: https://www.prizepicks.com/resources/how-to-play-prizepicks (retrieved 2026-07-05)]
- [x] **Push / void / DNP rules** — **Tie** (exact match to decimal): payout reverts one tier; leg stays in slip. **DNP** (no snap/play, board error, postponed game per league rules): leg removed, slip reverts one tier; 2-pick Power → refund. **Reboot** (NFL: More on full-game leg, player exits 1H injured, no 2H return): treated like DNP for payout tier; **Less still grades normally**. Same-team-only or single-leg remainder → auto refund. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/dnps-reboots-and-ties (retrieved 2026-07-05)] [Source: https://www.prizepicks.com/reboots (retrieved 2026-07-05)]
- [x] **NFL stat menu** — see § NFL stat types below. Includes fantasy score (full PPR), combo props, partial-game boards (1H/1Q/2H), live boards, K/P/DST categories. [CONFIRMED] [Source: https://www.prizepicks.com/playbook-article/how-to-play-nfl-dfs-on-prizepicks (retrieved 2026-07-05)]
- [x] **Line refresh cadence** — No published pre-game refresh SLA. Board lines change at operator discretion (injury news, board errors). **Live Squares** adjust in real time during games; user can enable auto-accept or manually confirm changes before submit. PrizePicks may pause/unpause live projections mid-game. [TENTATIVE — no fixed cadence doc] [Source: https://www.prizepicks.com/livesquares (retrieved 2026-07-05)] [Source: https://www.prizepicks.com/help-center/dnps-reboots-and-ties (retrieved 2026-07-05)]
- [x] **ToS: scraping, bots, third-party tools** — Prohibits robots/spiders/automated access; improper conduct includes accumulating wins via **unauthorized scripts or automated means**. No public developer API. Account suspension/void prizes on violation. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/terms-of-service (retrieved 2026-07-05)]
- [x] **Responsible gaming limits** — Mandatory monthly deposit caps for 18–20 y/o ($1,500 / $3,000 / $5,000 by age). Self-limit tools available. [CONFIRMED] [Source: https://www.prizepicks.com/help-center/eligibility (retrieved 2026-07-05)]

### Payout summary (standard Player Picks)

Rates below are **base** multipliers before demon/goblin or correlation adjustments. Implied per-leg breakeven assumes independent 50/50 legs and ignores vig embedded in line setting — use as **floor math** only; real edges require fair-P vs posted line.

#### Power Play (all legs must hit)

| Picks | Multiplier | Implied leg hit rate |
|------:|-----------:|---------------------:|
| 2 | 3x | 57.7% |
| 3 | 6x | 55.0% |
| 4 | 10x | 56.2% |
| 5 | 20x | 54.9% |
| 6 | 37.5x | 54.0% |

#### Flex Play

| Picks | Result | Multiplier |
|------:|--------|----------:|
| 3 | 3/3 | 3x |
| 3 | 2/3 | 1x (push) |
| 4 | 4/4 | 6x |
| 4 | 3/4 | 1.5x |
| 5 | 5/5 | 10x |
| 5 | 4/5 | 2x |
| 5 | 3/5 | 0.4x |
| 6 | 6/6 | 25x |
| 6 | 5/6 | 2x |
| 6 | 4/6 | 0.4x |

**Revert rules:** each DNP, Reboot, or tie drops slip one tier (e.g. 4-pick Flex → 3-pick Flex; 3-pick Flex → 2-pick Power). [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]

**Note:** Marketing pages sometimes cite 6-pick Power at 25x vs help-center 37.5x — **trust in-app disclosure at submit time**. [NEEDS VERIFICATION 2026-07-05]

### Demon / Goblin impact on breakeven

| Line type | Direction | Multiplier effect | Sharp-default |
|-----------|-----------|-------------------|---------------|
| Standard | More or Less | Baseline | Default research leg |
| Demon | More only | Increases (variable; up to 2000x stack) | Only if fair-P still clears adjusted breakeven |
| Goblin | More only | Decreases (variable) | Only if easier line still +EV at reduced payout |

Dynamic multiplier is shown on the lineup review screen — **never assume static power/flex table when demons or goblins present**. [CONFIRMED] [Source: https://www.prizepicks.com/demons-and-goblins (retrieved 2026-07-05)]

### NFL stat types (Player Picks board)

Weekly availability varies; categories from official NFL playbook. Partial-game boards: **1H, 1Q, 2H**; **live** full-game boards on major stats.

| Position | Stat categories |
|----------|-----------------|
| **QB** | Pass attempts, completions, passing yards, passing TDs, rushing yards, longest completion, fantasy score |
| **RB** | Rush attempts, rush yards, rush yards in first 5 attempts, longest rush, receptions, receiving yards, Rush+Rec TD, fantasy score |
| **WR/TE** | Receptions, targets, receiving yards, longest reception, receiving yards in first 2 receptions, Rush+Rec TD, fantasy score |
| **K/P** | FG made/attempts/yards, kicker fantasy score, kicking points, longest/shortest FG combos, PAT attempts, punts inside 20, gross punt yards, 50+ yard punts |
| **DEF** | Total tackles, sacks, tackle for loss, interceptions |
| **Combos** | Multi-QB yard combos, either-player TD combos (board-dependent) |

**Fantasy score scoring (NFL):** full **PPR** — pass yds 0.04, pass TD 4, INT −1, rush/rec yds 0.1, rush/rec TD 6, reception 1, fumble lost −1, 2-pt conv 2, return TDs 6. Offensive players need ≥1 offensive snap (or return TD) to grade. [CONFIRMED] [Source: https://www.prizepicks.com/playbook-article/how-to-play-prizepicks-nfl-fantasy-scoring-system (retrieved 2026-07-05)]

**CeminiDFS mapping (K147):** yards/rec/TD/fantasy-score projections align with core CeminiDFS stat outputs; combo and partial-game props need separate distribution logic; K/DST props are **platform-native** (not in CeminiDFS v1).

### Geo: Player Picks availability (36 + D.C.)

**18+:** AK, AR, CA, DE, FL, GA, IN, KS, KY, ME, MN, MO, NC, ND, NE, NH, NM, NY, OK, OR, RI, SC, SD, TN, TX, UT, VT, WI, WV, WY, D.C.

**19+:** AL, CO

**21+:** AZ, IL, MA, VA

**Not Player Picks** (other product modes only): CT, HI, IA, ID, LA, MD, MI, MS, MT, NJ, NV (F2P only), OH, PA, WA — plus Free2Play everywhere. [Source: https://www.prizepicks.com/resources/states-where-you-can-play-prizepicks (retrieved 2026-07-05)]

### Legal / tool-builder posture

| Approach | Risk | Verdict |
|----------|------|---------|
| Local fair-value CLI + **manual line entry** | Low | **GO** — mirror CeminiDFS posture |
| Read-only browser overlay (no auto-submit) | Medium | **CONDITIONAL-GO** — confirm no ToS automation; deferred in K147 |
| Scrape `api.prizepicks.com` or app DOM | High | **NO-GO** — ToS §15(l) bans automated access |
| Auto-submit slips / credential bots | High | **NO-GO** |
| Paid third-party line feeds (SharpAPI, sportsdata.io, etc.) | Medium | **CONDITIONAL** — SaaS cost + ToS chain; benchmark only |

**Scraper repo audit (reject):**

| Repo / pattern | License | Verdict |
|----------------|---------|---------|
| Community `api.prizepicks.com/projections` scripts (Stack Overflow, Medium tutorials) | N/A | **REJECT** — ToS violation regardless of license |
| Selenium board scrapers (e.g. lazarobeas2 tutorials) | Unaudited / none | **REJECT** |
| `aidanhall21/underdog-fantasy-pickem-scraper` | NO LICENSE | **REJECT** (UD analog; cited in architecture) |

No **MIT/GPL pick'em scraper with valid license** identified for PrizePicks — consistent with architecture matrix. [CONFIRMED]

### Verdict

**VALIDATED** for K147 Phase-0 — primary platform candidate. **GO** for CLI fair-value + manual line workflow. **NO-GO** on line scrapers. Next: compare payout/breakeven vs @entities/platforms/underdog-pickem.md and pick primary lounge.

## Snippets

> Power Play standard rates (2026-07-02): 2-pick 3x · 3-pick 6x · 4-pick 10x · 5-pick 20x · 6-pick 37.5x. Flex 6/6 = 25x; 5/6 = 2x; 4/6 = 0.4x. [Source: https://www.prizepicks.com/help-center/payouts (retrieved 2026-07-05)]

> ToS: "use any robot, spider, or other automatic device, process, or means to access the Site or App for any purpose, including monitoring or copying any of the material on the Site or App." Improper conduct includes "accumulating points, Contest wins or Prizes through unauthorized methods such as unauthorized scripts or other automated means." [Source: https://www.prizepicks.com/help-center/terms-of-service (retrieved 2026-07-05)]

> NFL Reboot: More on full-game projection; player leaves in 1st half with injury and does not return in 2nd half → payout reverts one tier. [Source: https://www.prizepicks.com/reboots (retrieved 2026-07-05)]

> PrizePicks named official partner of Atlanta Hawks (2026-07) — pick'em lounges mainstream in regulated states. [Source: @sources/substack-rss-event-horizon-2026-07-01-world-launches-solana-based-prediction-market.md]
