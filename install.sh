#!/bin/bash
# Sets up the UI Library on this computer.
# Run it once after downloading (cloning) the library:   bash install.sh
# Optional: bash install.sh --fonts   also downloads the 543 fonts that support Vietnamese (~1 GB).
set -e
LIB="$(cd "$(dirname "$0")" && pwd)"
echo "UI Library folder: $LIB"

# 1) Python 3 is needed for the lookup page and the download scripts.
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is missing. On a Mac run:  xcode-select --install   then run this file again."
  exit 1
fi

# 2) Teach Claude Code where the library is (installs the 'ui-library' skill).
SKILL_DIR="$HOME/.claude/skills/ui-library"
mkdir -p "$SKILL_DIR"
sed "s#{{LIBRARY_PATH}}#$LIB#g" "$LIB/claude-skill/ui-library/SKILL.md" > "$SKILL_DIR/SKILL.md"
echo "Installed Claude skill -> $SKILL_DIR/SKILL.md"

# 3) Make the double-click launcher runnable.
chmod +x "$LIB/OPEN_TOOL.command" "$LIB/install.sh" "$LIB/update.sh" 2>/dev/null || true

# 4) Optional font download.
if [ "$1" = "--fonts" ]; then
  python3 -I "$LIB/scripts/download_fonts.py" --vietnamese
fi

echo
echo "Done. Next:"
echo "  - Open the lookup page: double-click OPEN_TOOL.command"
echo "  - Download fonts when you need them:  python3 -I scripts/download_fonts.py \"Be Vietnam Pro\""
echo "  - 3D materials: see assets/3d-materials/README.md"
echo "  - Get the newest version later:  bash update.sh"
