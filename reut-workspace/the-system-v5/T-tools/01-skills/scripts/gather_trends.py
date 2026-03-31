#!/usr/bin/env python3
"""Gather trending tech/SaaS posts from X via Grok API."""

import requests
import os
import sys

def main():
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("ERROR: XAI_API_KEY not set. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    url = "https://api.x.ai/v1/responses"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "grok-4-fast-non-reasoning",
        "stream": False,
        "input": [
            {
                "role": "user",
                "content": "What are the 5 most trendy and popular tech, SaaS tweets of today?",
            }
        ],
        "tools": [{"type": "x_search"}, {"type": "web_search"}],
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Grok API request failed: {e}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    found_output = False
    for item in data.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    print(c["text"])
                    found_output = True

    if not found_output:
        print("WARNING: No output_text found in API response.", file=sys.stderr)
        print("Raw response:", data, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
