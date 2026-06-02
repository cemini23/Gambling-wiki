#!/usr/bin/env python3
"""Run cemini_decide with preflop chart Auto Research wired in."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import agent as agent_mod  # noqa: E402
import cemini_decide  # noqa: E402

agent_mod.retrieve_solver_context = cemini_decide.retrieve_solver_context

if __name__ == "__main__":
    argv = ["--agent", str(_EXAMPLES / "cemini_decide.py"), *sys.argv[1:]]
    raise SystemExit(agent_mod.main(argv))
