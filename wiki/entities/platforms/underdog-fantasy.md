---
title: Underdog Fantasy
type: entity
tags: [entity, platform, dfs, best-ball, season-long, nfl]
keywords: [underdog, best-ball-mania, bbm7, draft-and-hold, snake-draft]
related:
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-portfolio-construction.md
  - concepts/bbm7-playoff-week-construction.md
  - concepts/best-ball-strategy.md
  - concepts/best-ball-mania-winners.md
  - concepts/best-ball-draft-timing.md
  - concepts/dfs-strategy-overview.md
  - concepts/bankroll-management.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - entities/platforms/underdog-pickem.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/platforms/draftkings.md
  - entities/sports/nfl-betting.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md
  - sources/fantasysixpack-bbm-new-meta-2026-06-08.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
  - sources/fantasy-guru-bbm-tactics-2026-06-08.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md
maturity: validated
created: 2026-05-31
updated: 2026-07-20
---

## Relations

- @concepts/best-ball-strategy.md — primary strategy home
- @concepts/best-ball-mania-winners.md — BBM1–BBM6 winner dossier
- @entities/tournaments/best-ball-mania-vii.md — BBM7 official format and bracket
- @entities/platforms/draftkings.md — competitor best ball product
- @sources/youtube-operator-batch-wc-bbm-2026-05-31.md — BBM7 operator YouTube batch

## Raw Concept

US **daily fantasy + best ball** platform. Flagship large-field tournament: **Best Ball Mania** (BBM).

## Narrative

### K177 Context — prediction-market exchange (2026-07)

Jul 2026 Underdog launched its own CFTC-licensed prediction-market exchange (DCM+DCO+FCM stack) after previously routing via Kalshi/Crypto.com partners. See OSINT `@osint-wiki/sources/substack-rss-event-horizon-2026-07-20-underdog-exchange.md` + gambling brief `briefs/2026-07-20_k177-underdog-prediction-exchange.md`. DFS/best-ball product lines unchanged by this Context note.

### Best Ball Mania 7 (2026 season) [CONFIRMED — Underdog help center 2026-04-27]

See @entities/tournaments/best-ball-mania-vii.md for full rules. Summary:

| Field | Value |
|-------|-------|
| Entry fee | $25 |
| Max entries | 150 per user |
| Prize pool | $15,000,000 |
| First place | $2,000,000 |
| Draft format | 12-team snake, 18 rounds |
| Scoring | Half-PPR |
| Lineup | Auto-optimized weekly from roster |
| Live since | 2026-04-28 |

### Product mechanics & Draft Room UI (For Tool Builders)

#### 1. Draft Room UI Structure & Timers [CONFIRMED]
- **Fast Drafts**: Feature a strict **30-second pick clock** [Source: help.underdogfantasy.com (retrieved 2026-06-24)]. Fast drafts run continuously until completion (typically 20–30 minutes total for 18 rounds).
- **Slow Drafts**: Begin with an **8-hour pick clock** [Source: help.underdogfantasy.com (retrieved 2026-06-24)]. 
  - *Timer Compression*: As the contest's tournament cut-off or NFL season kickoff approaches, slow draft clocks compress dynamically. Two weeks before kickoff, it drops to 4 hours; one week before, it drops to 1 hour; the night before, to 10 minutes; and within two hours of kickoff, down to 60 seconds [Source: oddsassist.com/dfs/how-underdog-works/ (retrieved 2026-06-24)].
- **Auto-Pick Hierarchy**: If a draft clock hits zero, Underdog automatically executes a selection on behalf of the user following a strict fallback pipeline:
  1. **Player Queue**: Chooses the first player currently in the user's active draft-room queue.
  2. **Custom Rankings**: Selects the highest-ranked undrafted player in the user's uploaded/saved custom rankings.
  3. **Default ADP**: Defaults to the highest-ranked undrafted player according to Underdog's default ADP ranking.
  4. *Position Limits Exception*: The auto-picker will bypass players in the above priority if the user's roster has already met position-specific limits (e.g., maximum positional caps for QB/RB/WR/TE).

#### 2. Mobile App vs. Web Browser Experiences [CONFIRMED]
- **Feature Parity**: Underdog has excellent feature parity across the native iOS/Android apps, desktop web, and mobile web.
- **Layout Advantages**: 
  - *Web (Desktop)*: Highly preferred for serious/MME (multi-entry) drafters. The larger canvas displays the player pool, queue, and full draft board side-by-side. 
  - *Mobile App*: Native code offers faster loading speeds (<1s vs ~5s on desktop web), persistent login states, biometric authentication, and push notifications for completed drafts and scoring [Source: lines.com/dfs/underdog-fantasy (retrieved 2026-06-24)]. However, navigating multiple active drafts on a small screen is highly cramped.
- **CSV Portability [CRITICAL]**: The "Email exposure CSV" button is **only accessible via desktop web browser** (Drafts > Completed > NFL Season) and is entirely missing from mobile app clients [Source: fantasylife.com/articles/best-ball/ (retrieved 2026-06-24)].

#### 3. CSV/Roster Export Formats & Fields [CONFIRMED]
- **Ad-Hoc Exposure Export**: Underdog allows users to request their portfolio data via the desktop web. 
  - *Path*: Navigate to `Drafts` > `Completed` > `NFL Season 202X` > Click `"Email exposure CSV"` [Source: fantasylife.com/articles/best-ball/ (retrieved 2026-06-24)].
  - *Cadence*: Restricted to **one export email per calendar day** (sent from `support@underdog.com` with a temporary, secure download link) [Source: fantasylife.com/articles/best-ball/ (retrieved 2026-06-24)].
  - *Timeline*: Only available **post-draft** for fully completed entries.
  - *Exposure Fields*: This CSV contains player-level columns (e.g., `Player`, `Position`, `Team`, `Times Drafted`, `Exposure %`, `Total Entry Fees`) rather than raw draft-by-draft rosters [Source: fantasyondraft.com/underdog-exposure-analysis (retrieved 2026-06-24)].
- **Historical Pick-by-Pick Dumps**: Underdog periodically releases massive historical public datasets (e.g., BBM3, BBM4) containing granular, pick-by-pick rows with the following schema:
  - `draft_id`, `draft_time`, `clock` (fast vs. slow), `tournament_entry_id`, `tournament_round_number`, `player_name`, `position_name`, `bye_week`, `projection_adp`, `pick_order`, `overall_pick_number`, `team_pick_number`, `pick_points`, `roster_points`, `playoff_team` [Source: underdognetwork.com (retrieved 2026-06-24)].

#### 4. In-App ADP Display vs. External ADP Lag [CONFIRMED]
- **In-App ADP**: Pulled from real-money, completed paid drafts on a **48-hour rolling window** and updated **daily** (every 24 hours) during active draft season [Source: bestballteambuilder.com (retrieved 2026-06-24)]. 
- **External Lag**: External draft assistants (e.g., BestBallTeamBuilder, Draft Sharks, rosterOS) scrape or cache Underdog's public ADP listings. This introduces a **lag of 12 to 36 hours** relative to the live draft room. This latency becomes highly acute when player injuries, team signings, or training camp steam cause rapid, intraday ADP "drift" (such as a 1-2 round jump), presenting a high-value delta for real-time tool engines to exploit.

#### 5. Multi-Entry Management & Lobby UX [CONFIRMED]
- **Bulk Entry**: Users enter major tournaments (like the 150-entry max Best Ball Mania) via the primary draft lobby.
- **Active Tab Organization**: Entered drafts that are currently drafting are housed in the `"Active"` tab of the UI.
- **Cramped Multi-Draft List**: On web, active drafts are displayed in a scrolling sidebar on the left side of the window, displaying basic metadata (your draft slot, round/pick, active timer, whose clock is running).
- **The UI Bottleneck**: The native UI does not display who you have drafted on any given team in the active list view. To check your roster on a specific team, you must click into the specific draft box and click your username or scroll through the giant grid board [Source: github.com/Scottw1105/Underdog-Live-Team-Overlay (retrieved 2026-06-24)]. This is the core operational friction point for MME players.

#### 6. Extension Integration Points & DOM Mechanics [CONFIRMED]
- **Standard Architecture**: Existing third-party overlays (e.g., *Draft Brain*, *rosterOS*, *Underdog-Live-Team-Overlay*) deploy as standard Chrome Extensions (Manifest V3, using background service workers and `content.js` scripts injected into `app.underdogfantasy.com`) [Source: draftbrains.com, rosteros.com (retrieved 2026-06-24)].
- **Local-First Privacy**: Best-practice overlays run entirely in the browser using `chrome.storage.local`. They avoid sending user draft states or cookie sessions to external servers, protecting user privacy and reducing lag.
- **DOM Targets & Fragility**: 
  - Overlays target the sidebar's list of active draft boxes to extract basic state, and scrape player grid tables to read live pick histories.
  - *Selector Fragility*: Because Underdog runs a modern SPA framework (React/Next.js) with utility class engines (Tailwind), class selectors are highly unstable and change with site releases. Best-practice extensions target stable attributes like `aria-label` or role boundaries rather than layout classes [Source: HACKING.md in grok-powertools (pattern translation)].
  - *Main World Injection*: To trigger complex room state transitions or interface with the client's underlying data, tools inject lightweight bridge scripts (`bridge.js`) into the page's main world context [Source: HACKING.md in grok-powertools (pattern translation)].

#### 7. Terms of Service & Compliance Barriers [CONFIRMED]
Underdog's Terms of Use (specifically sections **ix** and **x** at `legal.underdogfantasy.com`) strictly define boundaries:
- **Scraping Prohibition**: Explicitly forbids scraping, crawling, indexing, framing, or copying any content via automated methods (using robots, spiders, crawlers, scrapers) [Source: legal.underdogfantasy.com (retrieved 2026-06-24)]. Access is only permitted manually through standard web browsers or approved APIs.
- **Robot Exclusion**: Explicitly prohibits bypassing robot exclusion headers or site access limitation protocols.
- **Compliance Matrix for Tool Builders**:
  - *Manual Entry + Local Recommender (CLI)*: **Zero Risk [LOW]**. Runs outside browser, zero interaction with the site.
  - *Read-Only DOM Overlay (Extension)*: **Low-to-Medium Risk**. Displays helpful exposure numbers without altering site state or network data. Tolerated by the platform (highly popular commercial overlays operate publicly).
  - *Automated DOM Polling / API Intercept*: **High Risk**. Automated scanning of room states or network sniffing.
  - *Auto-Pickers / Scripted Clicks*: **Critical Risk [VIOLATION]**. Auto-clicking draft actions triggers instant anti-bot geoblocks, IP bans, account locks, and potential legal prosecution.

#### 8. Autodraft & Queue Failure Modes [CONFIRMED]
- **Autopilot Sticky Latching**: In slow drafts, if a user misses **two consecutive picks**, the draft room latches into a permanent "Autopilot" mode [Source: oddsassist.com/dfs/how-underdog-works/ (retrieved 2026-06-24)]. The user remains on auto-pick until they manually log back in and toggle it off.
- **Position Cap Bypassing**: If the user's custom queue or custom rankings specify players at a position that has reached its maximum cap (e.g., 3 QBs in an 18-round roster), the auto-pick engine will silently **bypass** those players and pick the highest available player at a position still lacking representation. This often leads to "starvation" of intended stacks or uncoordinated final picks.
- **Queue Starvation / Stale Rankings**: If a custom queue is empty and custom rankings do not cover the remaining players (or contain players who have already been drafted), the system defaults to general ADP. For early-season lists run in late-season drafts, this frequently results in drafting retired, injured, or deeply mispriced players.

### Strategy implications

- Large-field = **extreme variance**; portfolio approach (many entries) standard among serious drafters
- Early-season drafts (May–June) show widest **ADP vs projection** gaps — see `@concepts/best-ball-strategy.md`
- Correlation stacks (QB+WR, game stacks) central to winner roster analysis in `@sources/youtube-operator-batch-wc-bbm-2026-05-31.md`

### Phase-0 checklist

1. ~~Confirm BBM7 structure and payout table~~ — done; see @entities/tournaments/best-ball-mania-vii.md [CONFIRMED]
2. Verify max entries and pick timers in-app before max-entering [TENTATIVE]
3. Compare vs DraftKings best ball for rake, liquidity, and draft speed
4. Treat entry fees as **GPP bankroll** — max-enter $3,750 = Final min-cash (@concepts/bankroll-management.md)

### Verdict

**REFERENCE** for best ball lane — primary platform in operator YouTube batch; not a sports **betting** sharp book.

For Underdog **pick'em** (higher/lower stats, not BBM drafts), see @entities/platforms/underdog-pickem.md and @concepts/diy-nfl-pickem-props-tool-architecture.md.

## Snippets

> "Best Ball Mania … costs $25 to enter … as many as 150 times … winner is awarded $2 million." [Source: Hpo51KrYKPI via @sources/youtube-operator-batch-wc-bbm-2026-05-31.md]

> "On underdog, there are 12 people in a draft and it's a snake format with 18 rounds." [Source: GSClshI0Ngc via @sources/youtube-operator-batch-wc-bbm-2026-05-31.md]
