#!/bin/bash
# Uploads your changes (new or edited files) to GitHub so your other computers can get them.
# Run:   bash save.sh "what you changed"
set -e
LIB="$(cd "$(dirname "$0")" && pwd)"
cd "$LIB"
python3 scripts/build_tool.py >/dev/null
git add -A
if git diff --cached --quiet; then
  echo "Nothing new to save."
  exit 0
fi
git commit -m "${1:-Update library}"
git push
echo "Saved to GitHub."
