#!/usr/bin/env python3
"""NFL offseason weekly research stub — Jul–Aug camp / ADP / K147 planning.

Runs weekly (LaunchAgent). Pulls unchecked digest rows for camp/BBM/pick'em clusters,
writes briefs/offseason/{season}-offseason-w{WW}-prefetch.md for a Cursor session
with the operator.

Does NOT ingest wiki or place wagers.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_config() -> dict:
    path = Path(__file__).resolve().parent / "nfl_offseason_weekly_config.yaml"
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def latest_sweep(repo: Path) -> Path | None:
    sweeps = sorted((repo / "wiki" / "sweeps").glob("*-daily.md"), reverse=True)
    return sweeps[0] if sweeps else None


def extract_cluster_rows(sweep_text: str, cluster: str, limit: int = 8) -> list[str]:
    """Parse markdown table rows under ### Q*: {cluster} section."""
    pattern = rf"### Q\d+:\s*{re.escape(cluster)}\s*\([^)]*\)(.*?)(?=### Q\d+:|## |\Z)"
    m = re.search(pattern, sweep_text, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    block = m.group(1)
    rows: list[str] = []
    for line in block.splitlines():
        if not line.startswith("| [ ]"):
            continue
        rows.append(line.strip())
        if len(rows) >= limit:
            break
    return rows


def notify_macos(title: str, message: str) -> None:
    safe = message.replace('"', "'")[:200]
    try:
        import subprocess

        subprocess.run(
            ["osascript", "-e", f'display notification "{safe}" with title "{title}"'],
            check=False,
            timeout=5,
        )
    except OSError:
        pass


def main() -> int:
    cfg = load_config()
    tz = ZoneInfo(cfg.get("timezone", "America/New_York"))
    now = datetime.now(tz)
    repo = repo_root()
    season = cfg.get("season_label", now.year)
    iso_week = now.isocalendar().week

    out_dir = repo / cfg["output"]["dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    hub_name = f"{season}-offseason-w{iso_week:02d}-hub.md"
    prefetch_path = out_dir / f"{season}-offseason-w{iso_week:02d}-prefetch.md"

    if prefetch_path.is_file():
        print(f"Already exists: {prefetch_path.relative_to(repo)}")
        return 0

    sweep_path = latest_sweep(repo)
    sweep_rows: dict[str, list[str]] = {}
    if sweep_path:
        sweep_text = sweep_path.read_text(encoding="utf-8")
        for cluster in cfg.get("sweep_clusters", []):
            sweep_rows[cluster] = extract_cluster_rows(sweep_text, cluster)

    lines = [
        "---",
        f"title: Offseason weekly prefetch — {season} week {iso_week}",
        "type: brief",
        "tags: [brief, offseason, nfl, w8, camp]",
        f"season: {season}",
        f"iso_week: {iso_week}",
        f"generated: {now.isoformat()}",
        "status: prefetch-stub",
        "---",
        "",
        f"# Offseason research — {season} · ISO week {iso_week}",
        "",
        "> **Jul–Aug mode:** weekly pulse only — no slate entries, pick'em tool not built yet.",
        "> Camp standouts and depth moves feed **BBM7**, **K147** planning, and Sep tool sessions.",
        "",
        f"**Target hub:** `briefs/offseason/{hub_name}`",
        "",
    ]

    if sweep_path:
        lines.append(f"**Digest source:** `{sweep_path.relative_to(repo)}`")
        lines.append("")

    for block in cfg.get("research_blocks", []):
        bid = block["id"]
        title = block["title"]
        prompt = block.get("prompt", "")
        lines.extend([f"## {title}", "", f"_{prompt}_", "", "- [ ] ", ""])

    lines.append("## Digest picks (unchecked — from morning sweep)")
    lines.append("")
    if not sweep_path:
        lines.append("_No sweep file found — run daily digest first._")
    else:
        any_rows = False
        for cluster, rows in sweep_rows.items():
            if not rows:
                continue
            any_rows = True
            lines.append(f"### {cluster}")
            lines.append("")
            for row in rows:
                lines.append(row)
            lines.append("")
        if not any_rows:
            lines.append("_No unchecked rows in configured clusters — review full sweep manually._")

    lines.extend(
        [
            "## Agent prompt (gambling-wiki Cursor)",
            "",
            "```text",
            cfg.get("cursor_prompt", "").strip(),
            f"Prefetch: briefs/offseason/{prefetch_path.name}",
            f"Write: briefs/offseason/{hub_name}",
            "```",
            "",
            "## Camp standout watchlist (fill in hub)",
            "",
            "| Player | Team | Role / buzz | BBM | Pick'em/prop later | Source |",
            "|--------|------|-------------|-----|-------------------|--------|",
            "| | | | | | |",
            "",
        ]
    )

    prefetch_path.write_text("\n".join(lines), encoding="utf-8")
    sidecar = out_dir / f".cursor-prompt-offseason-w{iso_week:02d}.txt"
    sidecar.write_text(
        f"Offseason weekly hub from {prefetch_path.name}\nTarget: briefs/offseason/{hub_name}\n",
        encoding="utf-8",
    )

    print(f"Wrote {prefetch_path.relative_to(repo)}")
    notify_macos(
        "NFL offseason weekly",
        f"Week {iso_week} prefetch ready — camp & K147 research in Cursor",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
