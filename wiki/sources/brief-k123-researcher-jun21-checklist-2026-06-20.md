---
title: K123 — Researcher track Jun 21 closed-beta checklist
type: source
tags: [source, brief, poker, devfun, researcher-track, k123]
keywords: [jun-21, hu-sandbox, trueskill, selfplay-sdk, preflight]
related:
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - concepts/heads-up-arena-strategy.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/poker-axis-eval-literacy.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
maturity: validated
read_status: deep-read
created: 2026-06-20
updated: 2026-06-20
cross-wiki-source: "briefs/2026-06-20_k123-researcher-track-jun21-checklist.md"
---

## Relations

- @sources/devfun-poker-researcher-track-email-2026-06-19.md — K121 HU TrueSkill timeline
- @concepts/heads-up-arena-strategy.md — HU fork doctrine
- Private brief: `briefs/2026-06-20_k123-researcher-track-jun21-checklist.md`
- @osint-wiki/concepts/devfun-researcher-track-readiness-2026-06.md — ops hub + HU gates

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K123 Jun 21 closed-beta operator checklist |
| **Date** | 2026-06-20 |
| **Target** | Researcher HU sandbox (separate from Playground 6-max) |

## Narrative

Condensed from K122 six-lane research synthesis. **Do not** submit 6-max logic to researcher lane.

### P0 — before first sandbox hand

- [ ] Accept invite / confirm cohort access
- [ ] Clone `devfun-org/poker-arena-starter-kit` — `./pokerkit test`
- [ ] **Fix K118 PFR gate** on shared preflop path (blocks Jungleman emulation)
- [ ] Fork HU `decide()` + regression corpus (OSINT: `run_hu_sandbox_gate.sh`)
- [ ] Pin researcher `competitionId` when SDK/email drops — do not assume Playground ID

### P1 — beta day (Jun 21)

- [ ] Read `skillFile` — table size, axis rubric, submission types
- [ ] Skeleton HU agent: legal actions + clock safety first
- [ ] Watch email/Discord for **Kaggle URL**, sandbox API base, sponsored credits
- [ ] Export trajectory + `axis_summary.json` before submit (Raeth hygiene)

### Metrics discipline

| Use | Ignore for researcher submit |
|-----|------------------------------|
| TrueSkill / match W/L | Playground chip leaderboard |
| Live ANALYZE worst hands | Selfplay bb/100 alone |
| HU freq bands + style shape | 6-max VPIP/PFR gates |

### Secrecy

No public wiki updates with ranks, patches, env toggles, or `decide()` internals during live event.

## Snippets

> "HU fork REQUIRED before K121 submit — do not port 6-max charts blindly." [Source: K122 research plan 2026-06-19]

## Dead Ends

- Routing Playground S2 qual logic to researcher sandbox
- Optimizing for Google Kaggle Game Arena HU (different product from dev.fun TrueSkill)
