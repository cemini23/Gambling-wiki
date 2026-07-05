---
title: NFL slate prefetch cadence (gambling-wiki)
type: concept
tags: [meta, automation, nfl, w8, slate-prefetch]
keywords: [launchagent, cron, prefetch, thu-sun-mnf, hub-brief]
related:
  - concepts/nfl-weekly-slate-hub-workflow.md
  - meta/daily-research-digest-cadence.md
  - concepts/dfs-injury-and-news-workflow.md
  - entities/sports/nfl-betting.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/nfl-weekly-slate-hub-workflow.md — hub brief completed after prefetch
- @meta/daily-research-digest-cadence.md — sibling automation (morning discovery)

## Raw Concept

**Hourly slate-aware prefetch** during NFL **regular season** (Sep–Feb): deterministic schedule + Vegas lines + optional wind → `briefs/slate-prefetch/` stubs.

**Jul–Aug:** use @meta/nfl-offseason-weekly-cadence.md instead — no slate entries, pick'em tool not built.

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Hourly @ :05 local (`com.cemini.nfl-slate-prefetch.gambling`) |
| **Season** | Sep–Feb (script no-ops when no upcoming REG games) |
| **Script** | `~/bin/cemini-nfl-slate-prefetch-gambling` → `scripts/nfl_slate_prefetch_run.py` |
| **Config** | `scripts/nfl_slate_prefetch_config.yaml` |
| **Output** | `briefs/slate-prefetch/{season}-w{NN}-{thu\|sun\|snf\|mnf}-{early\|final}.md` |
| **Hub target** | `briefs/{season}-w{NN}-slate-hub-{slate}.md` |

### Slate buckets (from nflverse kickoff ET)

| Key | Games |
|-----|-------|
| `thu` | Thursday |
| `sun` | Sunday before ~8:00pm ET (main DFS / early window) |
| `snf` | Sunday ~8:00pm+ ET |
| `mnf` | Monday |

Weeks with no Thursday or Monday game simply skip those passes.

### Prefetch passes (hours before first kickoff)

| Slate | Early | Final (T-90) |
|-------|-------|----------------|
| **TNF** | ~30h (Wed afternoon) | ~2h |
| **Sun main** | ~20h (Sat evening) | ~1.5h |
| **SNF** | ~6h | ~1.5h |
| **MNF** | ~26h (Sun evening) | ~1.5h |

Tune in `nfl_slate_prefetch_config.yaml` (`tolerance_hours` absorbs hourly agent drift).

### Two-tier automation

```text
Tier 1 (LaunchAgent, no LLM)
  nflverse schedule + spread/total + Open-Meteo wind
  → prefetch .md + macOS notification

Tier 2 (Cursor — manual or Automation)
  Read prefetch + wiki corpus
  → complete hub brief (injury, narrative, lane pointers)
  → operator launches tool sessions
```

**Tier 3 remains NO-GO:** auto-submit entries on any platform.

### Install

```bash
bash scripts/install_nfl_slate_prefetch.sh
```

Manual run from repo root:

```bash
python3 scripts/nfl_slate_prefetch_run.py
```

Logs: `~/Library/Logs/cemini/nfl-slate-prefetch-gambling.{out,err}.log`

Unload:

```bash
launchctl bootout gui/$(id -u)/com.cemini.nfl-slate-prefetch.gambling
```

### Cursor Automation (optional)

Trigger when a new file appears in `briefs/slate-prefetch/*-final.md`:

1. Open **Gambling wiki** folder
2. Prompt: read sidecar `briefs/slate-prefetch/.cursor-prompt-*.txt` + complete hub per @concepts/nfl-weekly-slate-hub-workflow.md

Early pass (`*-early.md`) is optional preview; **final** pass is the pre-entry research window.

### vs daily digest

| Job | Purpose |
|-----|---------|
| Daily digest @ 08:15 | arXiv/news **discovery** — not slate-specific |
| Slate prefetch hourly | **This week's games** — timing tied to kickoff |

## Snippets

> "Research before each slate… close enough to game for weather and injury." [Source: operator spec, 2026-07-05]
