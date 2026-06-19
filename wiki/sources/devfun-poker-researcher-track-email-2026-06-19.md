---
title: dev.fun Poker Arena — researcher track invite email (2026-06-19)
type: source
tags: [source, email, devfun, poker-arena, researcher-track, heads-up, trueskill]
keywords: [researcher-track, heads-up, trueskill, self-play-sdk, kaggle, tom-dwan, jungleman, devlord]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/people/tom-dwan.md
  - entities/people/daniel-cates-jungleman.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - entities/bots/poker-bot-tooling.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - osint-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md
maturity: validated
read_status: read
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @entities/platforms/devfun-poker-arena.md — platform entity; researcher track ladder detail
- @entities/people/tom-dwan.md — pro rep-selection anchor
- @entities/people/daniel-cates-jungleman.md — second pro rep-selection anchor
- @entities/bots/cemini-devfun-poker-agent.md — operator agent (private implementation)
- @sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md — pro style research (Dwan + Jungleman)
- @osint-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md — OSINT cross-wiki stub + Cemini posture

## Raw Concept

| Field | Value |
|-------|-------|
| **Provenance** | Direct email to operator handle **cemini23** from **devlord** (co-founder, dev.fun) |
| **Received** | 2026-06-19 (operator report) |
| **CTA** | Join researcher track (signup link in email body) |
| **Read status** | Full text ingested |

## Narrative

### Summary [CONFIRMED — operator email]

dev.fun opens the **Poker Arena researcher track** — a **deeper** lane than the public 6-max arena. Builders submit **heads-up (HU)** agents; sandbox ranks by **TrueSkill**; the **top agent becomes the benchmark bot** the field must beat. **Tom Dwan** and **Daniel "Jungleman" Cates** will play the field and **select bots that play most like them** for representation.

### How it works

1. **Submit** any agent meeting the interface: Python bot, fine-tuned model, raw weights, or LLM agent with operator's own API key
2. **Sandbox** runs agents **heads-up**, ranked by **TrueSkill**
3. **Champion** — top-ranked agent becomes the bot everyone else must beat

### Builder tooling (sponsored)

| Resource | Role |
|----------|------|
| **Self-play SDK** | Local / sandbox iteration |
| **Kaggle competition page** | Public benchmark + submission surface |
| **Sponsored credits** | Sandbox compute cost covered by dev.fun |

### Timeline [CONFIRMED]

| Date | Milestone |
|------|-----------|
| **2026-06-21** | Closed beta for researchers |
| **2026-06-25** | Public sandbox opens |

### vs public arena (gambling-wiki framing)

| Dimension | Public arena (Playground / Tournament) | Researcher track |
|-----------|----------------------------------------|------------------|
| **Format** | 6-max NLHE, season bankroll | **Heads-up** sandbox |
| **Ranking** | Chip leaderboard / KO bracket | **TrueSkill** (pairwise skill estimate) |
| **Access** | Open registration + qual | Researcher signup / invite cohort |
| **Pro hook** | Finale seat vs Dwan (marketing) | Dwan + Jungleman **pick style-matched bots** |
| **Goal** | Qualify, survive, climb $50K ladder | Best HU agent; **champion = field benchmark** |

Cross-ref: Jun 18 PRNewswire release states researcher track **fixes engine and underlying LLM** so builders compete on **poker strategy** — aligns with pure-code `decide()` agents (no runtime LLM). [TENTATIVE — verify on Kaggle rules at access]

### Operator posture

- **Separate lane** from Playground S2 / Tournament — do not assume same charts, blind structure, or API entrypoint until SDK docs confirm
- **HU strategy fork** required — 6-max `cemini_decide` logic is not portable without regression rewrite
- **Style emulation** now explicit selection criterion — ties to `@entities/people/tom-dwan.md` villain profile and future Jungleman overlay
- **Competition secrecy** unchanged — no public wiki for live ranks, patches, or `decide()` internals during active events

## Snippets

> "the Poker Arena researcher track is open, and this one is built for people who want to go deeper than the public arena." [Source: dev.fun email to cemini23, 2026-06-19]

> "build a heads-up poker agent. the best ones get to represent Tom Dwan and Jungleman, who play the field and pick the bots that play most like them." [Source: dev.fun email to cemini23, 2026-06-19]

> "submit any agent that meets the interface: a python bot, a fine-tuned model, raw weights, or an LLM agent with your own key" [Source: dev.fun email to cemini23, 2026-06-19]

> "we run it heads-up in a sandbox, ranked by TrueSkill" [Source: dev.fun email to cemini23, 2026-06-19]

> "the top agent becomes the bot everyone else has to beat" [Source: dev.fun email to cemini23, 2026-06-19]

> "June 21: closed beta for researchers / June 25: public sandbox opens" [Source: dev.fun email to cemini23, 2026-06-19]

> "if you work on agents, eval, or reasoning under uncertainty, this is the cleanest heads-up benchmark to put your work up against." [Source: dev.fun email to cemini23, 2026-06-19]

## Dead Ends

- **Treating researcher track as Playground qual path** — separate format, ranking, and timeline
- **Assuming 6-max selfplay gates transfer to HU TrueSkill** — need HU-specific regression corpus
- **Publishing operator submission details or sandbox ranks** — competition secrecy; private repo only
