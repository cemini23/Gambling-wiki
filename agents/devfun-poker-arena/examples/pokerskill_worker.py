"""Run under Python 3.9 venv with PokerSkill installed.

Reads PokerSkill game state JSON from stdin; writes prompt JSON to stdout.
Used by pokerskill_adapter on cemini-prod (Py3.11 main venv cannot load cp39 .so).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Fallback if editable install breaks (upstream missing __init__.py pre-fix).
_SRC = Path("/opt/PokerSkill")
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


def main() -> int:
    try:
        raw = json.load(sys.stdin)
        from pokerskill_agent.schema import validate_game_state
        from pokerskill_agent._core import generate_prompt

        state = validate_game_state(raw)
        prompts = generate_prompt(state)
        json.dump(
            {
                "ok": True,
                "street": state["street"],
                "hero_position": state["hero_position"],
                "system_prompt": prompts["system_prompt"],
                "user_prompt": prompts["user_prompt"],
            },
            sys.stdout,
        )
        return 0
    except Exception as exc:
        json.dump({"ok": False, "error": str(exc)}, sys.stdout)
        return 1


if __name__ == "__main__":
    sys.exit(main())
