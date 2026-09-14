#!/bin/bash
# Opens email-draft.txt as an unsent draft in Apple Mail (macOS only).
# First line "אל:" -> recipient, second line "נושא:" -> subject, rest -> body.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$DIR/email-draft.txt"

TO="$(sed -n '1s/^אל: *//p' "$SRC")"
SUBJECT="$(sed -n '2s/^נושא: *//p' "$SRC")"
BODY="$(tail -n +3 "$SRC")"

osascript - "$TO" "$SUBJECT" "$BODY" <<'APPLESCRIPT'
on run argv
  set theTo to item 1 of argv
  set theSubject to item 2 of argv
  set theBody to item 3 of argv
  tell application "Mail"
    set msg to make new outgoing message with properties {subject:theSubject, content:theBody, visible:true}
    tell msg
      make new to recipient at end of to recipients with properties {address:theTo}
    end tell
    activate
  end tell
end run
APPLESCRIPT

echo "Draft opened in Mail: $SUBJECT"
