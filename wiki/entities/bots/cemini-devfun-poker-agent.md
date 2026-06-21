---
title: Cemini dev.fun poker agent (cemini_decide)
type: entity
tags: [entity, bot, poker, devfun, arena-pokerkit]
keywords: [cemini, devfun, cemini_decide, arena-pokerkit, decide-function]
related:
  - concepts/poker-axis-eval-literacy.md
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/pokerskill.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - entities/bots/poker-bot-tooling.md
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/people/tom-dwan.md
  - entities/people/daniel-cates-jungleman.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - entities/people/daniel-cates-jungleman.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k107-poker-open-spot-audit-2026-06-09.md
  - concepts/custom-agent-methodology.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - entities/games/poker.md
maturity: draft
created: 2026-06-01
updated: 2026-06-19
adoption_status: ACTIVE-DEV
claim_status: VERIFIED 2026-06-01 — @cemini23
---

## Relations

- @entities/platforms/devfun-poker-arena.md — venue + Phase-0
- @entities/tools/pokerskill.md — skill-binding pattern (full PokerSkill repo not wired yet)
- @entities/people/tom-dwan.md — Pro Table Finale villain profile (`durrrr` exploit overlay — **not** Playground defaults)
- @concepts/poker-hl-analyst-loop.md — **HL analyst loop** (analyze → patch → preflight → deploy)
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — K95 consistent opponent modeling anchor
- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — K118 research gap analysis + P0 fix backlog (private brief)
- @sources/brief-k107-poker-open-spot-audit-2026-06-09.md — K107 open-spot audit baseline
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — K121 researcher track invite
- Implementation: **private** — `llm-wiki-by-cemini` repo, path `agents/devfun-poker-arena/` (not in public Gambling-wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Name** | Cemini Wiki Poker |
| **Handle** | `cemini_wiki_poker` (official arena) |
| **Owner** | **@cemini23** — X verified [CONFIRMED] |
| **Quote** | "structured skills over swagger" |
| **Venue** | dev.fun Poker Arena — Playground + tournament path |
| **Base kit** | arena-pokerkit + custom `decide()` (private repo path) |

## Narrative

### Architecture (public summary)

Arena API drives a local agent loop: pending actions in, action + reasoning YAML out. Strategy is **pure code at runtime** (no per-hand LLM). Iteration uses the HL analyst loop at @concepts/poker-hl-analyst-loop.md — analyze live leaks, patch offline, gate with tests, deploy to prod.

Layer stack (generic): preflop chart hints → labeled scenario reasoning → postflop equity vs pot odds → clock safety. **Specific thresholds, guards, and opponent overlays are competition-private.**

### Pro villain prep (K121 research, 2026-06-19)

Named exploit overlays for finale / HU sandbox — **private implementation** only:

| `villain_id` | Profile page | Core adjustment |
|--------------|--------------|-----------------|
| `durrrr` | @entities/people/tom-dwan.md | Call-heavy vs bombs; thin value; cut bluffs |
| `jungleman` | @entities/people/daniel-cates-jungleman.md | Wide defend; punish probes; fix passive PFR |

Synthesis source: @sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md. **Researcher rep pick** may require **style emulation** (especially Jungleman HU frequencies), not pure exploit.

### Researcher track (K121, 2026-06-19) [CONFIRMED — public email]

Separate **heads-up** sandbox lane — not Playground qual. See @sources/devfun-poker-researcher-track-email-2026-06-19.md.

| Item | Detail |
|------|--------|
| **Format** | HU bot-vs-bot; **TrueSkill** ranking |
| **Timeline** | Closed beta **2026-06-21**; public sandbox **2026-06-25** |
| **Submit** | Python bot (current path), weights, fine-tune, or LLM + own key |
| **Tooling** | Self-play SDK, Kaggle page, sponsored credits |
| **Pro hook** | Dwan + Jungleman pick bots that **play most like them** |

**Public rule:** 6-max Playground logic requires **HU fork** + new regression corpus before researcher submission. Implementation details private.

### Pro Table Finale prep (future)

When dev.fun publishes finale format: optional named-villain exploit overlays per @entities/people/tom-dwan.md — **not** merged into Playground survival defaults.

### Next iterations (K118 priority)

1. **P0 — PFR gate + open path** — selfplay shows VPIP 11.5% / PFR 2.2% (2026-06-17); SB limp inflation; rock steal threshold too high. See @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md.
2. Wire **PokerSkill** expert library when license verified on GitHub
3. **AlphaExploitem-lite** — extend session memory beyond aggression counts
4. Optional research lane: runtime LLM eval — not prod path
5. Heartbeat / lobby resilience on prod host

### Entry fee

Paid tournaments may return **402** until MON entry fee is settled on Monad via dev.fun UI; prod lobby retries join on interval.

### Runbook

Operator commands and deploy paths: **private** `README-CEMINI.md` on operator machine / prod host — not duplicated here during active events.

**Qualification:** Playground windows feed a KO path; monitor cutoff with local status scripts. Playground rebuy rules vary by season — confirm on arena before assuming recovery.

### Wallet (MON) — beta vs official [CONFIRMED 2026-06-03]

Beta and official are separate agent IDs and custodial wallets; MON does not sync. Fund official via MoonPay or external send. Agent IDs and addresses: **private creds only**. See `LESSONS.md` L4.

### Playground S1 close (2026-06-08) [CONFIRMED]

Season **S1 LIVE** (`cmpy2qy65002ud9ej6b7jjq0l`, ~290 ranked) snapshot before rollover:

| Metric | Value |
|--------|-------|
| **Chip rank** | **#1** — 139,946 chips / 2,362 hands |
| **Adjusted bb/100** | **+2,820** — **#3 EV** among players with ≥400 hands (Jeff +3,670; Jagoan +2,828) |
| **Style** | Tight-passive (~10.4% VPIP / 3.5% PFR) |
| **Poker Eval S1 overnight** | −17.45 adj bb/100 vs panel (500h) — in starter-kit baseline band |

UI leaderboard screenshots archived; structured fixture in private repo `agents/devfun-poker-arena/tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json`. **De-luck:** chip lead ≠ EV lead at volume; Jeff passed hero on adjusted bb/100.

## Snippets

> "structured skills over swagger" — agent quote at registration [CONFIRMED 2026-06-01]

> Claim card: **AGENT CLAIMED** · owner @cemini23 · verified · entered 2026-06-01 [Source: arena.dev.fun claim UI]

## Dead Ends

- Deploying same bot against `@entities/platforms/pokerstars.md` or Bovada — arena-only scope
- Publishing live ranks, frequencies, or leak clusters in public wiki during active qualification — gives competitors a free HUD
