# Gambling & Betting Wiki

> A public knowledge hub for **sports betting, casino games, poker, DFS, best ball, and prediction-market wagering** (consumer/strategy angle). LLM-managed, human-read — built to stay useful whether you're researching a slate or wiring an agent.

Welcome. This repo is part of the Cemini wiki federation. Browse freely, fork what helps, and tip or follow our projects if you want to keep the lights on for more open research.

## What this is

This workspace is a **librarian** for betting and gambling research. It:

- **Manages** raw sources (books, PDFs, course notes, repo snapshots, transcripts) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — platforms, tools, games, sports, bots (requirements), and strategy concepts
- **Applies** them via briefs in `briefs/` for slate prep, study plans, and bankroll frameworks

## Quick start

1. Read `CLAUDE.md` — schema the LLM follows each session
2. Read `ROADMAP.md` — active workstreams
3. Copy `.env.example` → `.env` (optional Exa/Brave keys for external research)
4. Drop a source into `research to be indexed/` and ask Claude/Cursor to ingest it
5. Lint: `python3 scripts/wiki_lint.py`

**CI (GitHub):** wiki lint only on push/PR — no agent pytest in this public repo.

## Where code lives

| Content | Repo / path |
|---------|-------------|
| **This wiki** (public) | `wiki/`, `LESSONS.md`, `ROADMAP.md` |
| **dev.fun arena bot** (`cemini_decide`, deploy, briefs) | Private [llm-wiki-by-cemini](https://github.com/cemini23/llm-wiki-by-cemini) → `agents/devfun-poker-arena/` (open **OSINT WORKSPACE** locally) |
| **PM / CeminiSuite bots** | Same private osint repo — see `@osint-wiki` |

Public clone gets `agents/README.md` only (pointer stub). Do not commit competition strategy here.

## Folder layout

```
Gambling-wiki/
  CLAUDE.md
  README.md
  LESSONS.md
  ROADMAP.md
  agents/README.md          # stub → private bot repo (implementation gitignored)
  wiki/
    index.md                # catalog
    log.md                  # operations log
    entities/
      platforms/            # sportsbooks, DFS sites, PM venues, poker rooms
      tools/                # odds services, optimizers, trackers
      bots/                 # platform-bot requirements (code stays private)
      games/                # poker, blackjack, craps, …
      sports/               # NFL, NBA, …
      tournaments/          # e.g. Best Ball Mania
      people/
    concepts/               # bankroll, Kelly, DFS, house edge, …
    sources/
    meta/                   # cadence pages, ingest rubrics
    sweeps/                 # daily research digests
  scripts/                  # wiki_lint.py, preingest_check.py, digest runners
```

## Cemini wiki federation

**Eight** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis).

| Alias | Repository | Focus |
|-------|------------|--------|
| **`gambling-wiki`** | **This repo** | Sports betting, casino, poker, DFS, best ball |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | Castle/RTS hobby dev, Godot evals, agent harness |
| `osint-wiki` | *private* ([llm-wiki-by-cemini](https://github.com/cemini23/llm-wiki-by-cemini)) | PM bots, dev.fun arena bot code, CeminiSuite, quant OSINT |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | Agent workflow, MCP, skills |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Pentest, SOC |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Local SEO, creator ops |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | FDM/print farms |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | ComfyUI, LoRA |

Cross-links: `@gambling-wiki/concepts/bankroll-management.md` ↔ `@osint-wiki/concepts/kelly-sizing-quarter.md`

```bash
git clone https://github.com/cemini23/Gambling-wiki.git
```

## Privacy

- `.env`, `raw-sources/`, `briefs/`, `hot.md`, and `agents/devfun-poker-arena/` are gitignored
- Never commit API keys, arena credentials (`.arena-credentials`), account PII, or live competition intel (ranks, leak clusters, patch toggles)

## Responsible gambling

This wiki documents **+EV discipline and risk management**. Wager only where legal, within bankroll limits, and with awareness of addiction resources. We do not optimize for compulsive play.

## Related

- Methodology newsletter: [Outlier Weekly](https://outlierweekly.substack.com) · [Issue 3 — World Cup Bot](https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- **World Cup LP bot (automation):** [world-cup-bot](https://github.com/cemini23/world-cup-bot) — shadow-first Polymarket LP + Kalshi gap alerts; pairs with `@gambling-wiki/entities/sports/world-cup-2026-betting.md`
- Tooling: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet)


## Support

Thank you for reading, starring, forking, or otherwise supporting Cemini open research — it genuinely helps keep these public wikis and tools maintained.

**Projects & sites**

| Project | Link | What it is |
|---------|------|------------|
| **Outlier Weekly** | [outlierweekly.substack.com](https://outlierweekly.substack.com) | Methodology newsletter (trading, bots, research notes) |
| **Atto** | [youratto.com](https://youratto.com) | Desktop organizer for Italian family / citizenship documents |
| **GuruWatcher** | [guruwatcher.com](https://guruwatcher.com) | Local Discord alerts for newsletter price levels (alert-only) |
| **YouTube** | [@Cemini23](https://www.youtube.com/@Cemini23) | Build logs and walkthroughs |

Voluntary tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets. Canonical copy: [CCC SUPPORT.md](https://github.com/cemini23/cemini-claude-code-CCC/blob/main/SUPPORT.md).

| Chain family | Address |
|--------------|---------|
| **X Money** (fiat, US) | Request [@Cemini23](https://x.com/Cemini23) in the X app — scan the Request QR |
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |
| **Hyperliquid** (referral) | [app.hyperliquid.xyz/join/CEMINI23](https://app.hyperliquid.xyz/join/CEMINI23) |


## License

MIT — see `LICENSE`.
