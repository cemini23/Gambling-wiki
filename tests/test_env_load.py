"""env_load fills missing keys only; never overwrites process env."""

from __future__ import annotations

import os
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from env_load import candidate_env_paths, load_dotenv  # noqa: E402


def test_load_one_skips_existing_env(tmp_path, monkeypatch):
    monkeypatch.setenv("THE_ODDS_API_KEY", "already-set")
    env = tmp_path / ".env"
    env.write_text("THE_ODDS_API_KEY=from-file\nOTHER_TEST_KEY=xyz\n", encoding="utf-8")
    load_dotenv(env)
    assert os.environ["THE_ODDS_API_KEY"] == "already-set"
    assert os.environ["OTHER_TEST_KEY"] == "xyz"
    monkeypatch.delenv("OTHER_TEST_KEY", raising=False)


def test_load_one_reads_missing_key(tmp_path, monkeypatch):
    monkeypatch.delenv("ENV_LOAD_UNIT_KEY", raising=False)
    env = tmp_path / ".env"
    env.write_text("ENV_LOAD_UNIT_KEY=unit-value\n", encoding="utf-8")
    load_dotenv(env)
    assert os.environ["ENV_LOAD_UNIT_KEY"] == "unit-value"
    monkeypatch.delenv("ENV_LOAD_UNIT_KEY", raising=False)


def test_osint_workspace_is_a_fallback_candidate():
    paths = candidate_env_paths()
    assert any(p.name == ".env" and p.parent.name == "OSINT WORKSPACE" for p in paths)
