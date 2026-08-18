---
title: Daily research digest cadence (gambling-wiki)
type: concept
tags: [meta, automation, discovery, k93, federation]
keywords: [daily-research-digest, exa, sweep, inbox, federated-digest, rss]
related:
  - meta/cross-wiki-routing.md
  - concepts/gambling-wiki-scope.md
  - concepts/gambling-bot-architecture.md
  - sources/brief-k93-federated-digest-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - sweeps/2026-06-04-daily.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - sweeps/2026-06-09-daily.md
  - sweeps/2026-06-13-daily.md
  - sweeps/2026-06-14-daily.md
  - sweeps/2026-06-15-daily.md
  - sweeps/2026-06-17-daily.md
  - sweeps/2026-06-18-daily.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/daily-digest-reject-cluster-k119-2026-06-18.md
  - sources/daily-digest-reject-cluster-k116-2026-06-17.md
  - sweeps/2026-06-19-daily.md
  - sweeps/2026-06-20-daily.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
  - sweeps/2026-06-21-daily.md
  - sources/daily-digest-reject-cluster-k124-2026-06-21.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sweeps/2026-06-22-daily.md
  - sources/daily-digest-reject-cluster-k125-2026-06-22.md
  - sweeps/2026-06-23-daily.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
  - sweeps/2026-06-24-daily.md
  - sources/daily-digest-reject-cluster-k127-2026-06-24.md
  - sweeps/2026-06-25-daily.md
  - sources/daily-digest-reject-cluster-k129-2026-06-25.md
  - sources/daily-digest-batch-k161-2026-07-26.md
  - sources/daily-digest-reject-cluster-k161-2026-07-26.md
  - sources/brief-k161-ev-charging-false-positive-shelf-2026-07-26.md
  - sources/daily-digest-batch-k162-2026-07-28.md
  - sources/daily-digest-reject-cluster-k162-2026-07-28.md
  - sources/brief-k162-harnessllm-false-positive-shelf-2026-07-28.md
  - sources/daily-digest-batch-k163-2026-07-29.md
  - sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md
  - sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md
  - sources/daily-digest-batch-k164-2026-07-30.md
  - sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
  - sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md
  - sources/daily-digest-batch-k165-2026-08-04.md
  - sources/daily-digest-reject-cluster-k165-2026-08-04.md
  - sources/brief-k165-bits-per-spike-false-positive-shelf-2026-08-04.md
  - sweeps/2026-07-27-daily.md
  - sweeps/2026-07-28-daily.md
  - sweeps/2026-07-29-daily.md
  - sweeps/2026-07-30-daily.md
  - sweeps/2026-07-31-daily.md
  - sweeps/2026-08-01-daily.md
  - sweeps/2026-08-02-daily.md
  - sweeps/2026-08-03-daily.md
  - sweeps/2026-08-04-daily.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sweeps/2026-08-16-daily.md
  - sweeps/2026-08-17-daily.md
  - sweeps/2026-08-18-daily.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
  - sources/daily-digest-batch-k167-2026-08-18.md
  - sources/brief-k167-sfp-mfg-shelf-2026-08-18.md
maturity: validated
created: 2026-06-01
updated: 2026-08-18
---

## Relations

- @osint-wiki/concepts/federated-daily-research-digest.md — federation install kit (K93)
- @meta/cross-wiki-routing.md — ingest routing vs @osint-wiki
- @sources/brief-k93-federated-digest-2026-06-01.md — brief provenance
- @sources/daily-digest-rss-industry-2026-08-14.md — first RSS-lane ingest (industry/legal)
- @sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md — K167 SFP-MFG shelf (REFERENCE)
- @sources/daily-digest-batch-k167-2026-08-18.md — K167 batch (1 REFERENCE)
- @sources/brief-k167-sfp-mfg-shelf-2026-08-18.md — K167 shelf brief (wont_wire)

## Raw Concept

K93 federated install: morning **discovery-only** loop for sports betting, PM retail, poker/DFS, and gambling-bot eval lanes. Does **not** auto-write entity pages — Cursor **full ingest** does.

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily @ 08:15 local (`com.cemini.daily-research-digest.gambling`) |
| **Installed** | 2026-06-01 (K93 brief) |
| **Last run** | 2026-08-18 |
| **Fetch sources** | arXiv PDFs → inbox (sparse). **RSS/Atom** practitioner + industry + GitHub releases → sweep rows `S1`… (2026-08-14). OpenReview unused while `paper_mode: arxiv-only`. |
| **Script** | `~/bin/cemini-daily-research-digest-gambling` → `scripts/daily_research_digest_run.py` |
| **Deps** | `wiki_source_index.py` + `rss_digest.py` (required alongside digest runner) |
| **Config** | `scripts/daily_research_config.yaml` (`paper_queries`, `rss.feeds`; Exa news off) |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |
| **Inbox** | `research to be indexed/` (gitignored; PDFs only — RSS is discovery-only) |

### Operator loop

1. Review `wiki/sweeps/YYYY-MM-DD-daily.md` (or run digest manually)
2. Check RSS rows `S1`… first (seasonal signal); papers `P1`… when non-empty; optional social pass
3. Say **full ingest** in Cursor for this wiki folder on approved items
4. Weekly: optional Monokern pipeline on top `active_topics` row

### Topic lanes (config)

**Co-primary (2026-06-20):** W6 **Poker Arena / Researcher Round** and W9 **CeminiDFS** — equal digest priority; W8 NFL season prep follows. All in `active_topics`, news queries, and social pass.

Also: Kalshi/PM retail, sports betting +EV/CLV, World Cup 2026 cross-venue (cross-ref @osint-wiki WC bot + `@osint-wiki/entities/tools/wc-ticket-monitor.md` for physical-ticket resale), gambling-bot FOSS evals (W4), bankroll/Kelly, DFS/best ball.

**Brief routing:** `scripts/active_project_brief_targets.yaml` (co-primary: poker-arena · ceminidfs; secondary: nfl-w8).

**Auto-fetch (2026-06-17):** poker + DFS paper lanes first; `fetch.sources: [arxiv, openreview]`; `fetch_likely: true`; 10-day window; cap **12** PDFs/night. News rows still manual.

**RSS lane (2026-08-14):** papers are the wrong daily diet for W8 NFL / W9 DFS. arXiv sports-betting and DFS queries routinely return **0 hits**; Exa news stays **off** (credits). Free RSS/Atom is the seasonal primary: check `S1`… in the sweep, then **full ingest** selected URLs. Does **not** dump HTML into the inbox.

| Cluster | Feeds (live 2026-08-14 probe) | Why |
|---------|-------------------------------|-----|
| PM / sportsbook industry | Event Horizon, The Closing Line, Outlier Weekly, Legal Sports Report, Legal Sports Betting, SBC News | Product/legal/methodology. First three also polled by OSINT (`cross_wiki: gambling-wiki`) |
| NFL / DFS / best ball | RotoViz, Sharp Football Analysis, RotoBaller, 4for4 (marketing titles dropped), Over The Cap, PFT injury/camp filter | Usage, props, ADP, contracts, camp news |
| CeminiDFS data | `nflverse-data` + `nflreadpy` GitHub releases.atom | Package/data drops, not papers |

**Rejected as daily RSS** (picks mills, empty, 404, or paywall placeholders): Action Network, BettingPros, Covers, VSiN, Gaming Today, ESPN NFL, ETR feed (locked podcast stub), RotoGrinders, Unabated, OddsJam, PokerNews, Underdog blog.

**Keep elsewhere (not this digest):**
- **OSINT Substack poller** — full EH / Closing Line / Outlier / Klement bodies → OSINT inbox, then cross-wiki stubs
- **Offseason Sunday hub** — `@meta/nfl-offseason-weekly-cadence.md` (Jul–Aug camp/ADP)
- **In-season slate prefetch** — `@meta/nfl-slate-prefetch-cadence.md` (Sep+ operational, not research)
- **Monokern / yt-dlp** — weekly NotebookLM on co-primary topic
- **Manual paywall** — ETR, FantasyLabs, Stokastic, Underdog ADP exports (ToS: no scrape)
- **Poker strategy** — still arXiv/OpenReview; poker.org RSS is tournament PR, not HU exploit research

### Gates [CONFIRMED]

- Tier 3 autonomous ingest remains **NO-GO** — digest lands candidates only
- Prod bot deploy stays @osint-wiki; wagering requirements saved here

### LaunchAgent

```bash
launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.gambling.plist
```

Manual run from repo root:

```bash
python3 scripts/daily_research_digest_run.py
```

### RSS LaunchAgent gap (2026-08-18)

The installed LaunchAgent payload does **not** run the RSS lane: `~/Library/LaunchAgents/com.cemini.daily-research-digest.gambling.plist` → `~/bin/cemini-daily-research-digest-gambling` → `~/.cemini/launchagent/osint/daily_research_digest_run.py`, which has **zero** `rss` matches. The repo-local `scripts/daily_research_digest_run.py` **does** (config `rss.enabled: true`). Sweeps 2026-08-15…18 carry no RSS section; 08-14 RSS worked because that morning ran the local script. **Action:** morning jobs stay paper-only until OSINT merges RSS into the **canonical OSINT** runner + `PY_BUNDLE` and reinstalls — do **not** run `sync_federation_digest_bundle.sh` from this repo (it would overwrite gambling's local RSS runner).

## Snippets

> "No new Adopt tools in K93 eval for gambling surface." [Source: briefs/2026-06-01_k93-gambling-digest-from-osint.md]
