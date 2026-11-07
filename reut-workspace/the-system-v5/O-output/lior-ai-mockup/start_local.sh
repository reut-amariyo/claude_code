#!/bin/zsh
# Runs Lior Store Builder AI on this Mac so the microphone works in the call.
# Chrome allows the mic on localhost. Answers come from the prepared bank, all in Lior's recorded voice.
cd "$(dirname "$0")"
lsof -ti tcp:8765 | xargs kill 2>/dev/null
nohup python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 &
sleep 1
open -a "Google Chrome" "http://localhost:8765/lior-store-builder-ai.html"
echo "Running at http://localhost:8765/lior-store-builder-ai.html  (close this terminal tab to stop)"
