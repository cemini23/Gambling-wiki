#!/usr/bin/env python3
"""Assemble HL analyst brief from Arena analyze report (OSINT brief shape).

Used by `examples/cemini_hl_loop.sh` step 2. Output is paste-ready for Cursor.

Usage:
    uv run python examples/cemini_hl_brief.py --report reports/analyze/latest.txt
    uv run python examples/cemini_hl_brief.py --report /tmp/analyze.txt --round 3
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_DIR = _EXAMPLES.parent
_PROMPT = _AGENT_DIR / "prompts" / "cemini_hl_analyst_prompt.md"
_FIXTURES = _AGENT_DIR / "tests" / "fixtures" / "regression_spots.py"
_DEFAULT_OUT = _AGENT_DIR / "reports" / "hl-loop" / "latest_brief.md"


def _git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(_AGENT_DIR),
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except Exception:
        return "unknown"


def _regression_inventory() -> str:
    if not _FIXTURES.is_file():
        return "(regression_spots.py not found)\n"
    text = _FIXTURES.read_text(encoding="utf-8")
    lines: list[str] = []
    spot_id = ""
    notes = ""
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith('id="'):
            spot_id = s.split('"')[1]
        elif s.startswith("notes="):
            val = s.split("=", 1)[1].strip()
            if val.startswith('"'):
                end = val.rfind('"')
                notes = val[1:end] if end > 0 else val.strip('"')
        elif s.startswith("RegressionSpot(") and spot_id:
            lines.append(f"- `{spot_id}` — {notes}")
            spot_id = ""
            notes = ""
    if not lines:
        return "(parse regression_spots manually)\n"
    return "\n".join(lines) + "\n"


def build_brief(
    *,
    report_text: str,
    round_n: int,
    match_id: str,
    top_leak_hint: str,
) -> str:
    today = date.today().isoformat()
    sha = _git_short_sha()
    prompt_body = ""
    if _PROMPT.is_file():
        prompt_body = _PROMPT.read_text(encoding="utf-8")
    else:
        prompt_body = "(prompt template missing — see prompts/cemini_hl_analyst_prompt.md)\n"

    reg = _regression_inventory()
    summary_leak = top_leak_hint or "See analyze worst-hands section — pick #1 leak."

    return f"""---
title: "Cemini HL analyst round {round_n} — cemini_decide patch"
type: brief
tags: [brief, poker, hl-loop, cemini-decide, devfun-arena]
created: {today}
target: examples/cemini_decide.py
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — prod decide() on cemini-prod.
**Not** `examples/agent.py`.

## Summary

HL analyst round **{round_n}**: patch **one** leak from Arena analyze (competition
`{match_id}`), gate with pytest + regression spots + EP VPIP self-play audit, then
deploy. Self-play thousands of hands is **verification only**, not the trainer.

Primary leak candidate: {summary_leak}

## Body

### Workflow (this round)

```
analyze → LLM patch (this brief) → cemini_preflight.sh → deploy (optional)
```

### Gate requirements (mandatory before deploy)

| Gate | Command | Pass criteria |
|------|---------|---------------|
| Unit + regression | `pytest tests/` | All green |
| EP VPIP + trash | `cemini_selfplay_audit.py --gate` | EP VPIP ≤ 22%, 0 trash opens |
| Lobby smoke | `agent.py --dry-run` | 15 hands, no crash |

Self-play bb/100 is **informational** — do not optimize decide() for self-play scores.

### Patch scope (ONE leak)

- Edit `cemini_decide.py` only; smallest diff.
- If leak repeats after a prior fix, add/update `tests/fixtures/regression_spots.py`.
- Do not widen EP opens to "fix" maniac tables — tighten trash, fix HUD cold-start.

### Frozen regression spots (must stay green)

{reg}

### Arena analyze report

```
{report_text.strip()}
```

### Analyst prompt (paste block below into Cursor if not auto-loaded)

{prompt_body}

## Sources

- @wiki/concepts/poker-hl-analyst-loop.md
- @wiki/entities/bots/cemini-devfun-poker-agent.md
- `docs/TESTING-CEMINI.md`
- @osint-wiki/concepts/cemini-knowledge-application-architecture.md — brief→verify→deploy pattern

## Implementation status

| Field | Value |
|-------|-------|
| Status | NOT_STARTED |
| Implemented by | (HL analyst / operator) |
| Git SHA (pre-patch) | `{sha}` |
| Verified | — |
| Proof | `./scripts/cemini_preflight.sh` exit 0 |
| Follow-up | Re-analyze after ~50 live hands; freeze top new leak |
"""


def _top_leak_from_report(report: str) -> str:
    for line in report.splitlines():
        s = line.strip()
        if s.startswith("#") and "delta=" in s:
            return s.lstrip("#").strip()
    return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build HL analyst brief from analyze report")
    p.add_argument("--report", required=True, help="Path to failure analyze .txt")
    p.add_argument("--out", default=str(_DEFAULT_OUT), help="Output brief path")
    p.add_argument("--round", type=int, default=1, help="HL iteration number")
    p.add_argument("--match", default="", help="Arena competitionId")
    args = p.parse_args(argv)

    report_path = Path(args.report)
    if not report_path.is_file():
        print(f"ERROR: report not found: {report_path}", file=sys.stderr)
        return 2

    report_text = report_path.read_text(encoding="utf-8")
    hint = _top_leak_from_report(report_text)
    brief = build_brief(
        report_text=report_text,
        round_n=args.round,
        match_id=args.match or "(from env ARENA_LOBBY_COMPETITION_ID)",
        top_leak_hint=hint,
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(brief, encoding="utf-8")
    print(f"wrote → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
