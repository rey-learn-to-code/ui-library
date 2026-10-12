#!/bin/bash
# Gets the newest version of the UI Library from GitHub and refreshes the Claude skill.
# Run:   bash update.sh
set -e
LIB="$(cd "$(dirname "$0")" && pwd)"
cd "$LIB"
git pull --ff-only
bash "$LIB/install.sh"
