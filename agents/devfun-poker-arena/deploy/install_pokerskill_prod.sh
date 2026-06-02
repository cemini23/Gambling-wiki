#!/usr/bin/env bash
# Install PokerSkill into a Python 3.9 sidecar venv on cemini-prod.
# Main agent venv stays on 3.11; cp39 .so wheels load via pokerskill_worker.py.
#
# Usage:
#   ./deploy/install_pokerskill_prod.sh
#   ./deploy/install_pokerskill_prod.sh cemini-prod
set -euo pipefail

HOST="${1:-${CEMINI_PROD_HOST:-cemini-prod}}"
REMOTE_DIR="/opt/devfun-poker-arena"
VENV="${REMOTE_DIR}/venv-pokerskill"
POKERSKILL_SRC="${POKERSKILL_SRC:-/opt/PokerSkill}"

echo "==> Installing PokerSkill (Py3.9) on ${HOST}:${VENV}"

ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
REMOTE_DIR="${REMOTE_DIR}"
VENV="${VENV}"
POKERSKILL_SRC="${POKERSKILL_SRC}"

if ! command -v python3.9 >/dev/null 2>&1; then
  echo "Installing python3.9-venv..."
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -qq
  apt-get install -y python3.9-venv python3.9-dev git
fi

if [[ ! -d "\${POKERSKILL_SRC}/.git" ]]; then
  echo "Cloning PokerSkill to \${POKERSKILL_SRC}..."
  git clone --depth 1 https://github.com/lbn187/PokerSkill.git "\${POKERSKILL_SRC}"
fi

if [[ ! -x "\${VENV}/bin/python" ]]; then
  echo "Creating \${VENV}..."
  python3.9 -m venv "\${VENV}"
fi

"\${VENV}/bin/pip" install -q --upgrade pip wheel setuptools

# Upstream repo ships no pokerskill_agent/__init__.py — find_packages() installs metadata only.
if [[ ! -f "\${POKERSKILL_SRC}/pokerskill_agent/__init__.py" ]]; then
  echo "Adding missing pokerskill_agent/__init__.py (upstream packaging gap)..."
  printf '# PokerSkill package\\n' > "\${POKERSKILL_SRC}/pokerskill_agent/__init__.py"
fi

"\${VENV}/bin/pip" install -q --force-reinstall --no-cache-dir -e "\${POKERSKILL_SRC}"

echo "==> Verify import + worker smoke test"
"\${VENV}/bin/python" -c "
from pokerskill_agent._core import generate_prompt
from pokerskill_agent.schema import validate_game_state
s = validate_game_state({
    'hand_id': 1, 'street': 'preflop', 'hero_hole_cards': 'AsKd',
    'hero_position': 'BTN', 'legal_actions': ['f','k','c','b'],
    'action_history': [], 'pot': 2.5, 'hero_stack': 100, 'villain_stack': 100,
})
p = generate_prompt(s)
assert len(p['user_prompt']) > 50
print('PokerSkill OK — prompt chars:', len(p['user_prompt']))
"

cd "\${REMOTE_DIR}"
echo '{"hand_id":1,"street":"preflop","hero_hole_cards":"AsKd","hero_position":"BTN","legal_actions":["f","k","c","b"],"action_history":[],"pot":2.5,"total_pot":2.5,"hero_stack":100,"villain_stack":100}' \
  | "\${VENV}/bin/python" examples/pokerskill_worker.py | head -c 120
echo ""
echo "==> Done. Worker: \${VENV}/bin/python \${REMOTE_DIR}/examples/pokerskill_worker.py"
REMOTE

echo ""
echo "Restart lobby to pick up bridge: ssh ${HOST} systemctl restart cemini-devfun-poker-lobby"
