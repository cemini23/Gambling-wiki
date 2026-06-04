"""Tests for competition_field_report.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from competition_field_report import (  # noqa: E402
    _dedupe_agents,
    _fmt_pct,
    main,
)


def test_fmt_pct_formats_fractions() -> None:
    assert _fmt_pct(0.151) == "15.1%"
    assert _fmt_pct(None) == "n/a"


def test_dedupe_agents_keeps_best_rank() -> None:
    rows = [
        {"agent_id": "a1", "rank": 5, "handle": "slow"},
        {"agent_id": "a1", "rank": 2, "handle": "slow"},
    ]
    out = _dedupe_agents(rows)
    assert len(out) == 1
    assert out[0]["rank"] == 2


def test_main_prints_percent_hero_vs_leader(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    export_dir = tmp_path / "sample"
    export_dir.mkdir()
    agents = [
        {
            "agent_id": "l1",
            "handle": "leader",
            "rank": 1,
            "chips": 20000,
            "hands": 100,
            "stats": {"vpip": 0.208, "pfr": 0.056, "three_bet_pct": 0.046, "playing_style": "balanced-passive"},
        },
        {
            "agent_id": "h1",
            "handle": "cemini_wiki_poker",
            "rank": 3,
            "chips": 13000,
            "hands": 200,
            "stats": {"vpip": 0.151, "pfr": 0.026, "three_bet_pct": 0.019, "playing_style": "tight-passive"},
        },
    ]
    (export_dir / "agents.jsonl").write_text("\n".join(json.dumps(a) for a in agents) + "\n")
    (export_dir / "tables.jsonl").write_text("")

    rc = main([str(export_dir), "--hero", "cemini_wiki_poker", "--top", "2"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "Hero vs #1" in out
    assert "hero=15.1%" in out
    assert " #1=20.8%" in out
    assert "0.151" not in out
