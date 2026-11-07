#!/bin/bash
# Daily vault backup: commit everything new in the vault and push to GitHub.
# Runs from launchd (~/Library/LaunchAgents/com.reut.vault-backup.plist), daily 21:00.
# Exclusions (meetings, voice kits, animated-reel renders) live in the vault .gitignore.
# Safety: aborts without committing if a staged file looks like it holds a secret.
# Files over 50MB are unstaged and skipped (GitHub hard limit is 100MB).

VAULT="/Users/reutamariyo/Documents/Obsidian Vault"
FAIL_DIR="$VAULT/reut-workspace/the-system-v5/backups/github"
LOG="$HOME/Library/Logs/vault-backup.log"
STAMP="$(date '+%Y-%m-%d %H:%M')"

log() { echo "[$STAMP] $*" >> "$LOG"; }

fail() {
  log "FAILED: $1"
  mkdir -p "$FAIL_DIR"
  {
    echo "# Backup failure – $STAMP"
    echo
    echo "$1"
    echo
    echo "Log: \`$LOG\`"
  } > "$FAIL_DIR/BACKUP_FAILURE_$(date '+%Y-%m-%d_%H%M%S').md"
  exit 1
}

cd "$VAULT" || fail "Could not open the vault folder. macOS may be blocking access to Documents; give /bin/bash Full Disk Access."

git add -A || fail "git add failed."

if git diff --cached --quiet; then
  log "Nothing new to back up."
else
  # Skip oversized files
  git diff --cached --name-only --diff-filter=AM -z | while IFS= read -r -d '' f; do
    if [ -f "$f" ] && [ "$(stat -f%z "$f")" -gt 50000000 ]; then
      git reset -q -- "$f"
      log "Skipped (over 50MB): $f"
    fi
  done

  # Secret scan on staged content
  if git diff --cached -U0 | grep -qE 'shpat_[a-f0-9]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}|xox[bp]-[0-9A-Za-z-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY'; then
    git reset -q
    fail "Aborted: a staged file looks like it contains an API key or token. Nothing was committed or pushed. Find it with: git add -A && git diff --cached | grep -nE 'shpat_|sk-ant-|ghp_|github_pat_|AKIA|xox[bp]-|PRIVATE KEY'"
  fi

  COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')
  git commit -q -m "Daily backup: $(date '+%Y-%m-%d'), $COUNT files" || fail "git commit failed."
  log "Committed $COUNT files."
fi

# Push even when nothing new was committed, in case an earlier push failed
if git status -sb | head -1 | grep -q 'ahead'; then
  OUT=$(git push -q origin main 2>&1) || fail "git push failed: $OUT"
  log "Pushed to GitHub."
fi
