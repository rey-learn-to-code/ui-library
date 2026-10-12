#!/bin/bash
# Usage: util_clone.sh <github owner/repo> <dest_dir>  -> shallow clone, removes .git
set -e
repo="$1"; dest="$2"
mkdir -p "$(dirname "$dest")"
GIT_TERMINAL_PROMPT=0 git clone --depth 1 -q "https://github.com/$repo.git" "$dest"
rm -rf "$dest/.git"
echo "$repo -> $dest ($(du -sh "$dest" | cut -f1))"
