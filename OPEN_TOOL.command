#!/bin/bash
# Double-click this file to open the UI Library lookup page (keep the Terminal window open while using it).
cd "$(dirname "$0")"
python3 scripts/build_tool.py >/dev/null
PORT=8765
(sleep 1; open "http://localhost:$PORT/tool/") &
python3 -m http.server $PORT --bind 127.0.0.1
