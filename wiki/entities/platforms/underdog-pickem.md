---
title: Underdog Pick'em
type: entity
tags: [entity, platform, pickem, props, underdog, nfl]
keywords: [underdog, pickem, higher-lower, player-props, not-bbm, flex, standard, scorchers, alt-lines]
related:
  - concepts/pickem-stat-type-mapping.md
  - concepts/pickem-legal-and-tos-posture.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/pickem-legal-and-tos-posture.md
  - concepts/pickem-payout-and-breakeven.md
  - concepts/pickem-stat-type-mapping.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/bankroll-management.md
  - entities/platforms/underdog-fantasy.md
  - entities/platforms/prizepicks.md
  - entities/sports/nfl-betting.md
  - sources/fantasylabs-picklabs-launch-2026-07-05.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @entities/platforms/underdog-fantasy.md — **same brand, different product** — BBM is snake-draft best ball, not pick'em
- @entities/platforms/prizepicks.md — primary competitor pick'em lounge (payout comparison below)
- @concepts/diy-nfl-pickem-props-tool-architecture.md — K147 research hub
- @concepts/pickem-payout-and-breakeven.md — breakeven math per slip tier
- @concepts/pickem-stat-type-mapping.md — CeminiDFS projection → UD stat menu
- @concepts/pickem-legal-and-tos-posture.md — scraping bar shared with BBM
- @concepts/parlay-and-correlated-bets.md — multi-leg slips are correlated portfolios; UD adjusts payouts
- @entities/sports/nfl-betting.md — W8 operator stack (sportsbook props = benchmark lines)
- @sources/fantasylabs-picklabs-launch-2026-07-05.md — PickLabs names Underdog as supported pick'em lounge

## Raw Concept

Underdog Fantasy's **pick'em** product — binary higher/lower on posted player stat lines in 2–8 leg slips (Standard or Flex). Distinct from **Best Ball Mania** slow drafts covered by CeminiDFS `bbm` copilot.

## Narrative

### Do not conflate with BBM

| Product | Mechanics | CeminiDFS coverage | Wiki home |
|---------|-----------|-------------------|-----------|
| Best Ball Mania VII | 12-team snake, 18 rounds, half-PPR auto-lineup | `ceminidfs bbm` + MV3 extension | @entities/platforms/underdog-fantasy.md |
| Pick'em (Higher/Lower) | 2–8 O/U stat legs, fixed/flex multipliers | **None** | This page |
| Rivals | Head-to-head player stat matchups | **None** | [TENTATIVE] — defer to in-app rules |
| Champions | Peer P2P pick'em tournament | **None** | [TENTATIVE] |
| Ladders / Streaks / Swipe | Alternate game types | **None** | Out of K147 scope |

Shared with BBM: brand, app shell (`app.underdogfantasy.com`), operator may already have account and payment profile. **Not shared:** draft-room DOM, exposure CSV, ADP, recommender logic, or extension injection points.

### Product mechanics [CONFIRMED — help.underdogfantasy.com 2026-07-05]

**Higher/Lower (core pick'em):**

1. Select **2–8** player stat projections.
2. Choose **Higher** or **Lower** on each.
3. Entry must include players from **at least two different teams** [Source: help.underdogfantasy.com, underdogsports.com (retrieved 2026-07-05)].
4. Submit as **Standard** (all legs must hit) or **Flex** (3+ legs; partial credit on misses).
5. Minimum entry **$1** [Source: underdogsports.com/games/pickem (retrieved 2026-07-05)].

**Entry modes:**

| Mode | Leg range | Miss tolerance | Analog on PrizePicks |
|------|-----------|----------------|----------------------|
| Standard | 2–8 | 0 — one miss = loss | Power Play |
| Flex | 3–8 | 1 miss (3–5 legs); up to **2 misses** on 6–8 leg Flex ("double-flex") | Flex Play |

Flex requires minimum three selections. User can set default entry style (Standard vs Flex) in account settings [Source: help.underdogfantasy.com/en/articles/11099830 (retrieved 2026-07-05)].

### Payout tables vs PrizePicks [CONFIRMED — UD help center; PP help center 2026-07-05]

Base multipliers assume **1.0× per-leg difficulty**. Underdog **shifts** total payout when picks use non-standard per-leg multipliers (alt lines, Scorchers, correlated combos) — see § Correlation & shifted payouts. PrizePicks shifts on Demon/Goblin legs and some correlated golf combos [TENTATIVE — @entities/platforms/prizepicks.md stub].

#### Standard / Power Play (all legs must hit)

| Legs | Underdog Standard | PrizePicks Power Play | UD edge |
|------|-------------------|----------------------|---------|
| 2 | **3.5×** | 3× | UD +0.5× |
| 3 | **6.5×** | 6× | UD +0.5× |
| 4 | 10× | 10× | Tie |
| 5 | 20× | 20× | Tie |
| 6 | 35× | **37.5×** | PP +2.5× |
| 7 | **65×** | — | UD only |
| 8 | **120×** | — | UD only |

Underdog supports up to **8** Standard legs; PrizePicks Power Play caps at **6**. Maximum displayed multiplier on either platform can reach promotional ceilings (UD documents up to **5,000×** with stacked modifiers [Source: help.underdogfantasy.com/en/articles/10847198]).

#### Flex / Flex Play (partial credit)

| Legs | Result | Underdog Flex | PrizePicks Flex |
|------|--------|---------------|-----------------|
| 3 | Perfect | 3.25× | 3× |
| 3 | 1 miss | 1.09× | 1× |
| 4 | Perfect | 6× | 6× |
| 4 | 1 miss | 1.5× | 1.5× |
| 5 | Perfect | 10× | 10× |
| 5 | 1 miss | 2.5× | 2× |
| 5 | 2 misses | — | 0.4× |
| 6 | Perfect | 25× | 25× |
| 6 | 1 miss | 2.6× | 2× |
| 6 | 2 misses | 0.25× | 0.4× |
| 8 | Perfect | 80× | — |
| 8 | 1 miss | 3× | — |
| 8 | 2 misses | 1× | — |

**Breakeven implication:** UD's slightly richer 2–3 pick Standard tiers lower per-leg break-even vs PrizePicks Power Play at the same leg count. Flex 5-pick 1-miss pays **2.5×** on UD vs **2×** on PP. Tool builders must use **platform-specific** payout tables in slip EV math (@concepts/diy-nfl-pickem-props-tool-architecture.md).

### NFL stat menu [CONFIRMED — help.underdogfantasy.com NFL scoring articles 2026-07-05]

Weekly game picks (representative menu — availability varies by slate):

| Category | Examples | Grading notes |
|----------|----------|---------------|
| Passing | Yards, TDs, completions, attempts, first downs | 2-pt conversions **excluded** from standard passing stats |
| Rushing | Yards, attempts, TDs, longest rush | |
| Receiving | Yards, receptions, TDs | |
| Combos | Rush + Rec yards, Rush + Rec TDs (e.g. 1.5 = need 2 total TDs) | Both legs of **player combo** props must play or void |
| TD scorers | Anytime, first, second TD | Loss if no TD scored in game (anytime/first) |
| Situational | First rush attempt yards, 3rd-down conversions | First rush attempt voids if player has **zero** rush attempts |
| Defensive | Tackles for loss, etc. | Rescue policy **excludes** defensive players |
| Season-long | Regular-season games started, playoff games started | Settled after regular season; player needs ≥1 snap |

**Special teams:** yards/TDs on special teams do **not** count toward standard offensive stat picks unless the projection is special-teams-specific [Source: help.underdogfantasy.com/en/articles/8974214].

**NFL combos** (two-player bundled projections): both players must play or the combo voids [Source: help.underdogfantasy.com/en/articles/11063264].

### Alt lines, Scorchers, and per-leg multipliers [CONFIRMED]

- **Alt system:** Operator can move a player's line (higher target → harder; lower → easier). Payout multiplier adjusts per leg — e.g. 0.7× (easier) to 1.5× (harder) [Source: help.underdogfantasy.com/en/articles/13780101, underdogsports.com/games/pickem (retrieved 2026-07-05)].
- **Scorchers:** Promotional lines shifted in the player's favor (often fire/chili icon). Scorcher leg must **hit** for the boost to apply; missing it can void the boost [Source: stokastic.com, oddsreference.com (retrieved 2026-07-05) — cross-check in-app].
- **Shifted payouts:** If a void drops leg count, the **percentage** payout shift from modified legs carries to the recalculated slip (e.g. 5-pick with −20% modifier → void → 4-pick still −20%) [Source: help.underdogfantasy.com/en/articles/8974208].

PrizePicks analog: **Demon** (harder, higher multiplier) / **Goblin** (easier, lower multiplier) — different UX, similar shifted-EV mechanics.

### Insurance, correlation, and void rules

| Feature | Underdog | Tool-builder note |
|---------|----------|-------------------|
| **Flex** | Built-in 1–2 miss insurance (see table) | Map to slip EV with miss branches |
| **Rescue** | Refund + next-day "Gimme Pick" if offensive NFL player exits after playing first half and **Higher** leg loses; Standard entries only if no other leg already lost [Source: help.underdogfantasy.com/en/articles/8970218] | Asymmetric — favors Higher legs; model separately |
| **Correlated projections** | Platform reduces (or increases) **total** payout when legs are positively (or negatively) correlated — shown before submit [Source: help.underdogfantasy.com/en/articles/11010091] | **Must** read displayed multiplier; independent-product math overstates EV |
| **Void / DNP** | Inactive or zero snaps (incl. no ST snap) → void; slip repriced down one tier; **<2 active legs → full refund** [Source: help.underdogfantasy.com/en/articles/8923389] | Same push-down behavior as PP void/DNP tier drop |
| **Tie** | Exact push on line → void (repriced) | See help article on tie/voided selections |

Rescue applies to NFL **offensive** players only (no kickers/punters/DST). NFL preseason excluded [Source: help.underdogfantasy.com/en/articles/8970218].

### Terms of Service — automation / scraping [CONFIRMED]

Same platform ToS as BBM (@entities/platforms/underdog-fantasy.md §7). Sections **ix** and **x** at `legal.underdogfantasy.com/terms-of-use`:

> "scrape, access, monitor, index, frame, link, or copy any content or information on the Services by accessing the Services in an automated way, using any robot, spider, scraper, web crawler…" [Source: legal.underdogfantasy.com (retrieved 2026-07-05)]

> "violate the restrictions in any robot exclusion headers of the Services… or bypass or circumvent other measures employed to prevent or limit access" [Source: legal.underdogfantasy.com (retrieved 2026-07-05)]

**Compliance matrix (pick'em-specific):**

| Approach | Risk | K147 posture |
|----------|------|--------------|
| Local fair-value CLI + manual app entry | **Low** | **Preferred** |
| Read-only line overlay (no auto-submit) | **Low–Medium** | Tolerated pattern on BBM; verify pick'em DOM separately |
| Automated line scrape / API intercept | **High** | **NO-GO** |
| Auto-submit slips / scripted clicks | **Critical** | **NO-GO** |

### Manual line workflow feasibility [CONFIRMED for Phase-0]

| Path | Verdict |
|------|---------|
| Operator reads lines in iOS/Android/web app | **Feasible** — primary Phase-0 path |
| Licensed API / bulk export | **None** — no public pick'em line feed |
| FOSS scrapers | **REJECT** — see below |
| Cross-book benchmark | Log Hard Rock / Odds API prop closes manually (@entities/sports/nfl-betting.md) |

**Natural operator fit:** existing Underdog BBM account, familiar app shell, same bankroll rail — but **zero code reuse** from BBM extension (different SPA routes, pick'em lobby DOM, no exposure CSV for pick'em legs).

Line refresh cadence vs injury news: **[TENTATIVE]** — treat as event-driven; no published SLA. Re-check multiplier in entry review after news breaks.

Geo availability: pick'em restricted in **14+ US states** per secondary review [Source: oddsreference.com (retrieved 2026-07-05) — **verify in-app before max-enter**].

### Scraper reject

| Repo | Verdict | Notes |
|------|---------|-------|
| `aidanhall21/underdog-fantasy-pickem-scraper` | **REJECT** | No LICENSE (CeminiDFS K129) |
| `fantasydatapros/underdog` | **REJECT** | No LICENSE |

### Phase-0 checklist

- [x] Slip sizes and payout multipliers vs PrizePicks — tables above [CONFIRMED help centers]
- [x] NFL stat types and alt lines — menu above; alt + Scorcher mechanics [CONFIRMED]
- [x] Correlation / insurance features — Flex, Rescue, correlated payout shifts [CONFIRMED]
- [x] ToS sections ix/x — same scraping bar as BBM [CONFIRMED]
- [x] Manual line workflow feasibility — feasible; no licensed export [CONFIRMED]
- [ ] Operator state geo verification in-app [TENTATIVE]
- [ ] In-season line refresh / liquidity spot-check (NFL Sunday slate) [NEEDS VERIFICATION 2026-09-01]

### Verdict

**PRIMARY (K147 MVP)** — operator-locked 2026-07-05. Start here: account warm via BBM7, competitive 2–3 pick Standard payouts, 2–8 legs, Flex double-miss on 6+, Rescue on NFL offensive Higher legs. PrizePicks added as **Phase-2** second payout profile. **No CeminiDFS integration** until pick'em CLI graded. Payout comparison reference: @entities/platforms/prizepicks.md.

## Snippets

> "Entries can either default to Standard payouts or Flex payouts… a minimum of three (3) selections is required for a Flex entry." [Source: help.underdogfantasy.com/en/articles/11099830 (retrieved 2026-07-05)]

> "2-pick standard entry: 3.5x … 8-pick standard entry: 120x" [Source: help.underdogfantasy.com/en/articles/13780101 (retrieved 2026-07-05)]

> "Your potential payout adjusts based on the difficulty of your picks. If you choose a pick with a 0.7x multiplier, your total payout decreases… if you choose a pick with a 1.5x multiplier, your total payout increases." [Source: help.underdogfantasy.com/en/articles/13780101 (retrieved 2026-07-05)]

> "In order to bring you the widest variety of projections, certain picks and pick combinations will impact your payout amount." [Source: help.underdogfantasy.com/en/articles/8974208 (retrieved 2026-07-05)]

> "scrape… using any robot, spider, scraper, web crawler…" [Source: legal.underdogfantasy.com/terms-of-use §ix (retrieved 2026-07-05)]
