---
title: "Daily digest batch K181 — W4 Saturday lock, LSB cards, Sharp Football, SBC Europe, W5 waivers (2026-10-06)"
type: source
tags: [source, batch, k181, nfl, week-4, pm-retail, fantasy]
keywords: [saturday-lock, nico-collins, sharp-football, proe, sbc-europe, czech-kalshi, waiver-wire]
related:
  - sources/nfl-week4-saturday-lock-2026-10-03.md
  - sources/rss-lsb-week4-game-cards-2026-10-02.md
  - sources/rss-sharp-football-week4-2026-10-03-04.md
  - sources/rss-sbc-pm-europe-2026-10-01-05.md
  - sources/rss-rotoballer-w5-rb-waiver-2026-10-05.md
  - entities/tools/sharp-football-analysis.md
  - concepts/season-long-fantasy-waiver-wire.md
  - sweeps/2026-10-05-daily.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: REFERENCE — 1 docx, 20 RSS; 5 true duplicates archived
wire_status: policy_wired
---

## Batch summary

25 inbox files. **5 are true duplicates** — already covered by `@sources/rss-lsr-pm-industry-2026-09-29-30.md` (the K180 batch page). preingest reported all 25 as NEW because that page carries a **batch title**, so its title-based matcher cannot see the individual articles inside it.

| # | Source | Phase-0 | Wire |
|---|--------|---------|------|
| 1 | NFL Saturday Lock-Day Deltas docx | REFERENCE | nfl-w8 |
| 2 | LSB Week 4 game cards (4) | REFERENCE | nfl-w8 |
| 3 | Sharp Football (9: 2 free, 7 paywalled) | MIXED | new `sharp-football-analysis` tool |
| 4 | SBC Europe (5) | REFERENCE | policy_wired kalshi / polymarket / crossover |
| 5 | RotoBaller W5 RB waivers (1) | REFERENCE | new `season-long-fantasy-waiver-wire` concept |
| — | 5 LSR stubs | **DUPLICATE** | archived, not re-ingested |

**New pages:** 7 (5 sources + 1 tool entity + 1 concept).

## Recommended actions

1. **Nico Collins was cleared on Saturday.** The Friday card had him OUT on a **DraftEdge-only** cite; the club report excluded him entirely. This is the exact failure the retired Gemini prose layer produced — see @meta/research-input-pipeline.md. **Prefer club filings over aggregators for status.**
2. **Tampa Bay and MetLife pass cautions were lifted** Saturday (25→6-8 mph; 11→9 mph). The **team fades stay** — they were personnel-driven.
3. **Sharp Football** — use the free tools (PROE, ITT, coverage schemes, referee assignments). Do **not** buy the DFS package; CeminiDFS already covers projections.
4. **Season-long waivers** inform DFS priors only. Not a wagering lane.
5. **Czech Kalshi block effective 2026-10-15**; Polymarket appealing the Dutch €420K penalty. Awareness only, no pm scp.

## Process note — preingest gap

Five LSR stubs re-entered the inbox after the K180 archive and matched as NEW. The cause: K180 **batched** those five articles into one source page whose title differs from any single stub title, so the title-based duplicate check cannot match them.

**Consequence:** re-fetching them wastes an ingest cycle. A future fix is either to index **article URLs** inside batch pages, or to keep batch pages unbatched for LSR. Recorded here rather than changed.

## Briefs dispatched

- None new. The Week 4 slate pipeline is closed (see the retired Gemini cadence).

## Notes

- **SBC and RotoBaller reject direct fetch.** SBC returns 403; RotoBaller truncates the body. Both bodies came via Brave LLM Context and are marked `[TENTATIVE]` on the child pages.
- **Paywall rate is now a standing filter.** Sharp Football returns 7-of-9 pages paywalled — record access status on the source page so the next poller sweep can skip them.
- **Archive pending.**
