#!/usr/bin/env python3
"""
Gemini Writing Tool - Send a prompt to Gemini and get a response.

Usage:
  python3 tools/gemini-write.py "Your prompt here"
  python3 tools/gemini-write.py --file input.txt
  python3 tools/gemini-write.py --file input.txt --system "You are a Hebrew copywriter"
"""

import sys
import os
import argparse
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDlnlvIjrtEpq8W4edkT_igSl2N-NffId8")
MODEL = "gemini-2.0-flash"

def run(prompt: str, system_instruction: str = None, model_name: str = MODEL):
    genai.configure(api_key=API_KEY)

    kwargs = {}
    if system_instruction:
        kwargs["system_instruction"] = system_instruction

    model = genai.GenerativeModel(model_name, **kwargs)
    response = model.generate_content(prompt)
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to Gemini")
    parser.add_argument("prompt", nargs="?", help="The prompt text")
    parser.add_argument("--file", "-f", help="Read prompt from file")
    parser.add_argument("--system", "-s", help="System instruction for Gemini")
    parser.add_argument("--model", "-m", default=MODEL, help=f"Model name (default: {MODEL})")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            prompt = f.read()
    elif args.prompt:
        prompt = args.prompt
    elif not sys.stdin.isatty():
        prompt = sys.stdin.read()
    else:
        print("Error: provide a prompt, --file, or pipe input", file=sys.stderr)
        sys.exit(1)

    model_name = args.model
    result = run(prompt, args.system, model_name)
    print(result)

if __name__ == "__main__":
    main()
