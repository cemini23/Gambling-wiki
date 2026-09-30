---
title: "Daily digest batch K179 — CFTC mention advisory, NCPG, PM share, SBC, NHL opening night (2026-09-30)"
type: source
tags: [source, batch, k179, pm-retail, regulatory, nhl, industry]
keywords: [cftc-letter-26-27, ncpg, app-downloads, sbc-summit, nhl-opening-night]
related:
  - sources/rss-lsr-cftc-mention-market-advisory-2026-09-23.md
  - sources/rss-lsr-ncpg-functionally-gambling-2026-09-23.md
  - sources/rss-lsr-nfl-app-downloads-pm-share-2026-09-24.md
  - sources/rss-sbc-summit-lisbon-2026-09-29.md
  - sources/rss-lsb-nhl-opening-night-props-2026-09-29.md
  - sources/rss-eh-kalshi-curry-geofence-2026-09-25.md
  - entities/sports/nhl-betting.md
  - sweeps/2026-09-30-daily.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: REFERENCE — 2 regulatory, 2 industry, 1 new sport vertical
wire_status: policy_wired
---

## Batch summary

Eight inbox stubs from the 2026-09-23 → 2026-09-29 RSS window. The K178 close stubbed five of these as **titles only**; this batch fetches the bodies and replaces the stubs with deep reads.

| # | Source | Phase-0 | Wire |
|---|--------|---------|------|
| 1 | CFTC Letter 26-27 — mention markets (LSR 09-23) | REFERENCE | policy_wired kalshi / crossover |
| 2 | NCPG "functionally gambling" (LSR 09-23) | REFERENCE | policy_wired kalshi / crossover |
| 3 | NFL app downloads + PM share (LSR 09-24) | REFERENCE | policy_wired divergence / vig |
| 4 | SBC Summit Lisbon — Jordan keynote (SBC 09-29) | OOD | wont_wire |
| 5–8 | NHL opening night — 4 game cards (LSB 09-29) | GO (research) | new `nhl-betting` entity |
| 9 | Event Horizon S4 — Curry self-cert, NY v Polymarket, CA geofence (09-25) | REFERENCE | policy_wired kalshi / crossover |

**New pages:** 7 (6 sources + 1 sport entity).
**Papers:** no arXiv in this window; the 14-day lane stayed empty.

## Recommended actions

1. **CFTC mention advisory** — awareness only. No geofence change, no pm scp. If the operator holds a sports mention position, close it; the advisory presumes unlistable. Cross-link `@osint-wiki`.
2. **NCPG statement** — responsible-gambling context. No operator action. Do not treat as a legal trigger.
3. **Kalshi pricing** — the implied-vig edge is **pre-fee** and **reverses on parlays** (26.4% vs 23.9%). Any combo shop must net fees first. See @concepts/vig-and-hold.md.
4. **NHL** — research-only vertical. No auto-enter. Re-check starters at puck drop.
5. **Operator follow-ups from prior batches still open:** K177 scratch CSV / seat actuals; MNF tickets manual only.

## Briefs dispatched

- None new this batch. NHL material stays in-wiki until a lane is chosen.

## Notes

- **Archive blocked.** The egress host (`cemini-egress-fi`) is unreachable from this session (SSH denied by sandbox). The 8 inbox files remain in `research to be indexed/` and must be archived manually.
- **LSR and SBC block direct fetch** (HTTP 403). Bodies came through Brave LLM Context plus corroborating outlets. Every number sourced that way is marked `[TENTATIVE]` on the child page.
