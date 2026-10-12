#!/bin/bash
# Usage: util_npm_pack.sh <pkg> <dest_dir>
# Downloads an npm package tarball (no scripts run) and extracts it into <dest_dir>/<pkgname-sanitized>/
set -e
pkg="$1"; dest="$2"
name=$(echo "$pkg" | sed 's#^@##; s#/#__#g')
mkdir -p "$dest/npm_$name"
tmp=$(mktemp -d)
( cd "$tmp" && npm pack "$pkg" --ignore-scripts --silent >/dev/null 2>&1 )
tgz=$(ls "$tmp"/*.tgz | head -1)
tar -xzf "$tgz" -C "$dest/npm_$name" --strip-components=1
rm -rf "$tmp"
echo "$pkg -> $dest/npm_$name ($(du -sh "$dest/npm_$name" | cut -f1))"
