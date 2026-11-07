#!/bin/zsh
# Records any missing Lior lines with ElevenLabs and rebuilds the page.
# The key comes from the macOS Keychain if you saved it there, otherwise from a popup.
cd "$(dirname "$0")"
KC_SERVICE="lior-store-builder-elevenlabs"
KEY=$(security find-generic-password -s "$KC_SERVICE" -w 2>/dev/null)
if [[ "$KEY" != sk_* ]]; then
  KEY=$(osascript -e 'text returned of (display dialog "Paste your ElevenLabs API key (starts with sk_)" default answer "" with hidden answer with title "Lior Store Builder AI")' 2>/dev/null)
  if [[ -z "$KEY" ]]; then echo "The popup was closed or left empty. Nothing was recorded."; exit 1; fi
  if [[ "$KEY" != sk_* ]]; then echo "That key doesn't start with sk_. Copy the API key itself from ElevenLabs, not its name or ID."; exit 1; fi
  SAVE=$(osascript -e 'button returned of (display dialog "Save this key in your Mac Keychain so you are not asked again?" buttons {"No", "Save"} default button "Save" with title "Lior Store Builder AI")' 2>/dev/null)
  [[ "$SAVE" == "Save" ]] && security add-generic-password -U -s "$KC_SERVICE" -a "$USER" -w "$KEY" && echo "Key saved in Keychain."
fi
ELEVENLABS_API_KEY="$KEY" python3 gen_voice.py && python3 build.py
