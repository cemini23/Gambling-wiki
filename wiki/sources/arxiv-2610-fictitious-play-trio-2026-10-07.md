---
title: "arXiv trio — fictitious play: mean-field controls, BluffJAX, slow convergence (2026-10-07)"
type: source
tags: [source, arxiv, poker, game-theory, equilibrium, k182]
keywords: [fictitious-play, mean-field-games, bluffjax, karlin-conjecture, convergence-rate, jax, gpu-simulator, texas-holdem]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/heads-up-arena-strategy.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/tools/rlcard.md
  - entities/tools/adversarial-coevolution.md
  - entities/platforms/devfun-poker-arena.md
  - sources/daily-digest-batch-k182-2026-10-07.md
maturity: draft
read_status: skimmed
created: 2026-10-07
updated: 2026-10-07
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/
phase_0_verdict: REFERENCE — two theory bounds + one adoptable simulator; no bot wire this batch
wire_status: wont_wire
---

## Relations

- @concepts/poker-hl-analyst-loop.md — W6 analyst loop; FP is the equilibrium method behind it
- @concepts/heads-up-arena-strategy.md — HU NLHE primer
- @concepts/opponent-modeling-imperfect-info.md — imperfect-information lane
- @entities/tools/rlcard.md — the CPU baseline this suite outperforms
- @sources/daily-digest-batch-k182-2026-10-07.md — K182 hub

## Raw Concept

A tight cluster of three October 2026 arXiv papers, all on **fictitious play and equilibrium convergence in imperfect-information games**. Fetched by the morning digest; read here as one batch.

| # | arXiv | Title | Type |
|---|-------|-------|------|
| 1 | **2610.06292** | Learning Controls in Mean Field Games: the Fictitious Play and Related Gradient Descent | theory |
| 2 | **2610.07686** | **BluffJAX: Adversarial Imperfect Information Games in JAX** | **artifact** |
| 3 | **2610.08768** | Arbitrarily Slow Polynomial Convergence of Fictitious Play | theory |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2610.06292-…pdf` · `…-2610.07686-bluffjax-…pdf` · `…-2610.08768-…pdf`

## Narrative

### 1 — Mean-field games: fictitious play over controls (2610.06292)

**Meynard Charles.** Two learning procedures in **potential mean-field games (MFGs)**, where a population of rational agents interacts only through the population distribution.

- **The first is a fictitious play variant** in which players observe **the actions (controls) of others directly** and update the distribution of the field through an update rule **on controls** — not on payoff estimates. The paper proves convergence for a **wide class of potential MFGs of controls**, including with **common noise**.
- **The second is a principal agent** solving a mean-field control problem with only **local gradient information**. The paper proves the gradient descent **converges to a solution of the associated potential MFG**.

**Why it is in this wiki:** it is a convergence guarantee for FP-style learning when the observable is **actions**, not payoffs. Poker agents in this wiki's W6 lane log **opponent actions**; this is the theoretical result that such an update converges in the potential-game case.

### 2 — BluffJAX: a GPU poker simulator (2610.07686) — **the actionable one**

**Reddi, Peters, D'Eramo** (TU Darmstadt, Hessian.ai, DFKI, Würzburg). An **open-source suite of adversarial imperfect-information games in JAX**, built for high simulation throughput on GPUs.

Games implemented — ten, spanning well-studied and **previously unstudied** mechanics:

Kuhn Poker · Leduc Poker · Texas Hold'Em Limit · **Texas Hold'Em No-Limit** · Five Card Draw · Seven Card Stud · Goofspiel · Werewolf · **Bluff** · **Kemps**

**Reported performance:** scaling to **hundreds of millions of samples per second** across single and multi-GPU settings, with throughput and memory benchmarks published. The paper benchmarks RL, tree search, and game-solving algorithms in JAX as baselines.

**The stated motivation is the bottleneck this wiki actually has.** Quoting the paper: high-speed simulators that leverage hardware accelerators are a bottleneck for scaling large-scale RL in these domains. The paper positions BluffJAX against existing **GPU and CPU-based libraries** — the CPU side of which is `@entities/tools/rlcard.md`.

**Assessment:** the most directly usable artifact of the three. It is a simulator, not a solver, so it does not hand over a strategy — but it supplies the self-play volume that a research lane needs. **Verify the licence on GitHub before any use**; the abstract calls it "open-source" but the licence is not stated in the paper. [NEEDS VERIFICATION 2026-10-07]

### 3 — Fictitious play can converge arbitrarily slowly (2610.08768)

**Abernethy, Lazarsfeld, Wibisono** (Georgia Tech, Google Research, Yale). The sharpest result of the three.

**Claim:** fictitious play can converge at **arbitrarily slow polynomial rates** in two-player zero-sum games. For every integer **k ≥ 2** the authors construct a payoff matrix with **(k+1)² − 5 actions per player** for which the **duality gap of the empirical strategies decays as Θ(t^(−1/k))** after t steps.

- The family starts from **rock-paper-scissors**; each higher-order game is built **recursively** from the preceding one.
- After a prescribed common initial action, **every subsequent best response under FP is unique**.
- For **k ≥ 3** these are **counterexamples to Karlin's conjectured O(t^(−1/2)) convergence rate**.
- They **extend Wang's (2025) Θ(t^(−1/3)) construction** to arbitrarily slow rates.

**Why it matters practically:** the standing assumption that FP converges "fast enough" is not generally true — it degrades without bound as a function of the game. Any lane relying on **fictitious-play self-play to reach equilibrium** (`@concepts/poker-hl-analyst-loop.md`, MAFP in the W6 stack) inherits that bound. The construction is **adversarial**, not typical: real poker games are not built to be slow. But it kills the claim that FP convergence rate is a fixed property of the method.

## Snippets

> "We show that fictitious play can converge at arbitrarily slow polynomial rates in two-player zero-sum games." [Source: arXiv 2610.08768 abstract]

> "The bottleneck for scaling large-scale RL systems in such domains is the availability of data. High-speed simulators that can leverage hardware accelerators and collect diverse…" [Source: arXiv 2610.07686, §1]

## Dead Ends

- **No bot wire from this batch.** `wont_wire` — none of the three changes `decide()` behaviour on its own. BluffJAX is a **candidate** simulator once its licence is verified.
- **Do not over-read the slow-convergence result.** The construction is purpose-built to be slow. It bounds the method, not the operator's games.
- **BluffJAX licence unverified.** The paper says "open-source"; no SPDX identifier appears. Check the repo before any code or weights move. [NEEDS VERIFICATION 2026-10-07]
- **Two of three are pure theory.** No implementation is offered for 2610.06292 or 2610.08768.
