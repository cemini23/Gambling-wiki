#!/usr/bin/env bash
# install_nfl_slate_prefetch.sh — hourly NFL slate prefetch LaunchAgent (gambling-wiki)
set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.cemini.nfl-slate-prefetch.gambling"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
BIN_DIR="$HOME/bin"
WRAPPER="$BIN_DIR/cemini-nfl-slate-prefetch-gambling"
LOG_DIR="$HOME/Library/Logs/cemini"
PYTHON="${PYTHON:-python3}"

mkdir -p "$BIN_DIR" "$LOG_DIR" "$WIKI_ROOT/briefs/slate-prefetch"

cat > "$WRAPPER" <<EOF
#!/usr/bin/env bash
set -euo pipefail
cd "$WIKI_ROOT"
exec "$PYTHON" scripts/nfl_slate_prefetch_run.py "\$@"
EOF
chmod +x "$WRAPPER"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${WRAPPER}</string>
  </array>
  <key>WorkingDirectory</key>
  <string>${WIKI_ROOT}</string>
  <key>StartCalendarInterval</key>
  <array>
    <dict><key>Minute</key><integer>5</integer></dict>
  </array>
  <key>StandardOutPath</key>
  <string>${LOG_DIR}/nfl-slate-prefetch-gambling.out.log</string>
  <key>StandardErrorPath</key>
  <string>${LOG_DIR}/nfl-slate-prefetch-gambling.err.log</string>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl enable "gui/$(id -u)/${LABEL}"
launchctl kickstart -k "gui/$(id -u)/${LABEL}"

echo "Installed ${LABEL}"
echo "  Wrapper: ${WRAPPER}"
echo "  Logs:    ${LOG_DIR}/nfl-slate-prefetch-gambling.{out,err}.log"
echo "  Manual:  ${WRAPPER}"
echo ""
echo "Prefetch stubs → ${WIKI_ROOT}/briefs/slate-prefetch/"
echo "Complete hub in Cursor per wiki/concepts/nfl-weekly-slate-hub-workflow.md"
