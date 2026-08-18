"""Load gitignored .env into os.environ without printing values.

Order: process env (wins) → this wiki `.env` → sibling OSINT WORKSPACE `.env`.
THE_ODDS_API_KEY is held on the OSINT laptop `.env`; do not duplicate it here.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def candidate_env_paths() -> list[Path]:
    """Wiki-local first, then OSINT laptop .env (Projects, then Desktop alias)."""
    paths = [ROOT / ".env"]
    extras = [
        ROOT.parent / "OSINT WORKSPACE" / ".env",
        Path.home() / "Projects" / "OSINT WORKSPACE" / ".env",
        Path.home() / "Desktop" / "OSINT WORKSPACE" / ".env",
    ]
    seen = {p.resolve() for p in paths}
    for p in extras:
        try:
            resolved = p.resolve()
        except OSError:
            resolved = p
        if resolved not in seen:
            paths.append(p)
            seen.add(resolved)
    return paths


def _load_one(env_path: Path) -> None:
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def load_dotenv(path: Path | None = None) -> None:
    if path is not None:
        _load_one(path)
        return
    for env_path in candidate_env_paths():
        _load_one(env_path)
