---
title: Daniel Cates (Jungleman)
type: entity
tags: [entity, people, poker, high-stakes, heads-up, devfun]
keywords: [daniel-cates, jungleman, jungleman12, hu-specialist, durrrr-challenge, trueskill, devfun]
related:
  - entities/people/tom-dwan.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @entities/people/tom-dwan.md — Durrrr Challenge rival; contrasting LAG archetype
- @entities/platforms/devfun-poker-arena.md — Pro Table Finale + researcher track pro anchor
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — style rep selection mechanic
- @sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md — web synthesis + HU strategy interviews
- @entities/bots/cemini-devfun-poker-agent.md — **`jungleman` villain overlay** (finale / HU sandbox)

## Raw Concept

| Field | Value |
|-------|-------|
| **Name** | Daniel Cates |
| **Handles** | Jungleman, Jungleman12, w00ki3z (online) |
| **Origin** | US; rose as **online HU NLHE specialist** (late 2000s Full Tilt) |
| **Live** | Macau / Manila "Big Game"; WSOP bracelets; GTO Wizard pro (2025) |
| **Known for** | Durrrr Challenge domination; extreme **HU aggression** with **analytical balance** |
| **Wiki relevance** | dev.fun — picks bots that **play most like him**; finale vs Dwan marketing pair |

## Narrative

### Archetype summary

**Heads-up specialist LAG** — not the same as Dwan's **image-driven merge machine**. Jungleman's edge combines:

1. **Maximum pot-winning frequency** — "I just try to win all the pots I possibly can" [CONFIRMED — Paul Phua interview]
2. **Structural high 3-bet** — peak online HU often **20–25%+** 3-bet at nosebleed stakes [TENTATIVE — Pokerology era stats]
3. **Decision-tree literacy** — self-described memory for **each node** and how opponents play them, or superior **adjustment** [Source: Paul Phua "How Jungleman made his name"]
4. **Range balance / merge** — mixes value and bluffs; punished Dwan by **calling light** and **double/triple merging** [TENTATIVE — 2+2 challenge analysis]

**Label:** **Balanced-aggressive HU reg** with solver-era refinement — aggression is **disciplined**, not degen.

### Preflop tendencies (especially HU)

| Pattern | Detail | Source |
|---------|--------|--------|
| **Win every pot possible** | Probe where villains surrender; attack weakness | Paul Phua HU interview |
| **High 3-bet frequency** | Sustained 3-bet well above population HU norms | Pokerology feature |
| **56s > QTs for 3-bet** | Prefer suited connectors as 3-bet bluff candidates over broadway-dominated | Paul Phua — Cates direct quote |
| **AQo mix call/3-bet** | Avoid readable "always call AQo" line | Paul Phua |
| **Wide HU opening** | Many more combos HU vs ring → thin value preflop OK | Paul Phua ring-vs-HU section |

**Ring adaptation:** Transfers HU steal/probe tactics to full-ring — picks **small pots** ring players over-fold (A10o UTG fold mentality) [Paul Phua].

**Bot read:** **Defend blinds wide**; **3-bet/4-bet back** light with suited wheel/connectors; don't assume linear 3-bet value range.

### Postflop tendencies

| Pattern | Detail | Bot knob |
|---------|--------|----------|
| **Small-ball probes** | Takes pots opponents concede | **Raise more** vs auto-check-fold |
| **Thin HU value** | Value-bets thinner than ring (weaker showdown winners) | Call lighter on rivers |
| **Semi-bluff check-raise** | Turn CR with equity vs Dwan when line caps villain (PokerVIP hand) | Don't over-fold to CR |
| **Story-aware bluffs** | Galfond analysis: CR flush draw when villain sizing caps at trips, not full house | Respect **credible stories** — bluff less merged |
| **Stop-and-go** | Check flop, CR turn — classic vs players with SDV-heavy ranges | Continue vs turn aggression with pairs+ |
| **Adjustment** | "Either I understand the tree better or I adjust better" | Expect **mid-session exploit shifts** |

### Psychological / mental game

| Trait | Detail |
|-------|--------|
| **Variance tolerance** | Tweeted **~$5M USD** Manila loss (2015 HKD); recovered — plays massive swings |
| **Study network** | Learned from specialists per game; second opinions on hands (Paul Phua) |
| **Durrrr Challenge feud** | Public frustration at stalled match; reconciled with Dwan Jun 2025 on GTO Wizard |
| **Persona** | "Going God mode" / playful arrogance in WSOP-era interviews [Jason Hennessey podcast — TENTATIVE for poker strategy] |

### Heads-up vs Tom Dwan — Durrrr Challenge [CONFIRMED]

| Field | Value |
|-------|-------|
| **Format** | 50,000 hands HU NLHE $200/$400+ (2010–2013, incomplete) |
| **Result** | Cates **+~$1.2M–1.5M** over ~20k hands; +$197k in Oct 2013 session alone |
| **Mechanism** | Called light vs Dwan bluffs; range merges; Dwan escalated LAG (spew loop) |
| **Notable pot** | J2hh flush > Dwan lower flush for **~$216k** pot (Rakeback report) |
| **2025** | Hatchet buried; GTO Wizard video; possible new challenge teased |

**Strategic contrast:**

| | **Dwan** | **Jungleman** |
|---|----------|---------------|
| **Core weapon** | Image + oversized pressure | HU frequency + balance |
| **Vs aggression** | Hero calls, wide continues | **Light call-down**, merge back |
| **Preflop** | Trash 4-bets, wide opens | High 3-bet, trap strong hands |
| **Exploit if you mirror Dwan** | Jungleman prints | — |
| **Exploit if you mirror TAG** | Jungleman steals relentlessly | — |

### dev.fun roles

| Role | Detail |
|------|--------|
| **Researcher track** | Plays HU sandbox field; selects bots whose **style matches his** |
| **Pro Table Finale** | Named alongside Dwan (Jun 2025 PR); human showcase |
| **Rep criterion** | **Style fidelity** — wide HU aggression, balanced lines, probe frequency |

### Bot counter-strategy (`jungleman` profile)

For `@entities/bots/cemini-devfun-poker-agent.md` — **finale / HU sandbox only**:

| Knob | vs generic pool | vs Jungleman archetype |
|------|-----------------|------------------------|
| **Blind defense** | Chart | **Much wider** — fight for every pot |
| **Fold to 3-bet** | Standard | **Tighter fold** — he 3-bets wide; 4-bet or call more |
| **Fold to small bet** | Often correct | **Raise more** — don't concede probes |
| **Bluff frequency** | Moderate | **Selective** — he calls light vs obvious bluffs |
| **Bluff catch** | Equity-based | **Wider** on textures he merges |
| **Value thinness** | Standard | **Thinner HU** — he calls down |
| **Trap respect** | Low | **Higher** — strong hands in mixed lines |
| **Session prior** | HUD | **`villain_id: jungleman`** — high aggression + call-down |

**Style emulation (researcher rep pick):** Target **high 3-bet**, **wide steal**, **probe small pots**, **mixed AQo lines**, **56s-type 3-bets** — not Dwan's pure overbet theatrics.

### vs chart / passive bots

Jungleman **punishes passivity** — bleeds blinds and small pots. A **low-PFR rock** (K118 leak signature) is **anti-Jungleman** and anti-HU. Fixing PFR gap helps both Playground and researcher lanes.

### Ring-game note

In 6-max Big Game, Jungleman applies HU tactics selectively — not every pot. dev.fun **researcher track is HU-native**; weight this profile **heavily** there.

## Snippets

> "I just try to win all the pots that I possibly can. I'd see where people let me take pots from them and where they don't." [Source: Paul Phua — @sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md]

> "I prefer to 3-bet a hand like 5-6 suited more so than, like, Queen-10 suited." [Source: Paul Phua — same]

> "I understand the game better than most opponents… all the decision tree points… It's either that, or that I adjust better than they do." [Source: Paul Phua Jungleman profile — same]

> Cates built a lead of around **$1.2 million across 19,000 hands** [Durrrr Challenge]. [Source: PokerNews 2025-06-10 — same]

## Dead Ends

- **Jungleman = Dwan** — different exploit profiles; merging them loses edge
- **Pure maniac model** — he balances and merges; Galfond hand shows **story discipline**
- **Ring Big Game = HU sandbox** — adjust frequencies down for multiway
- **2010 Full Tilt HUD stats as 2026 exact frequencies** — evolved with solvers (GTO Wizard pro)
