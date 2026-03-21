# Skill: Running the Grok & Search Scripts

When asked to run the Lior Scout, you have permission to execute local Python scripts to gather data.

## API Connection Details

- **Endpoint:** `https://api.x.ai/v1/responses` (Responses API, NOT chat/completions)
- **Auth:** Use the `XAI_API_KEY` environment variable (set in `~/.zshrc`)
- **Model:** Must use a `grok-4` family model (e.g., `grok-4-fast-non-reasoning`) — grok-3 does NOT support search tools
- **Tools:** Use `{"type": "x_search"}` and `{"type": "web_search"}` for live data

## Execution Steps

1. **X & Web Search (Primary):** Use the xAI Responses API with `x_search` and `web_search` tools to pull real-time trending posts and news. Example payload:
   ```json
   {
     "model": "grok-4-fast-non-reasoning",
     "stream": false,
     "input": [{"role": "user", "content": "your query"}],
     "tools": [{"type": "x_search"}, {"type": "web_search"}]
   }
   ```
2. **Fallback Search:** If the xAI API is unavailable, use the `googlesearch-python` library or a SERP search using the `SERP_API_KEY`.
3. **RSS Feeds:** Use the `feedparser` library to pull from TechCrunch, The Verge, OpenAI blog, and Hugging Face.
4. **Hand-off:** Pull the raw data, then apply the instructions from `A-agents/the-lior-scout.md` to format the final output.

## Required Python Packages
- `openai` (for fallback chat completions)
- `requests` (for Responses API calls)
- `feedparser` (for RSS)
- `googlesearch-python` (for fallback web search)
- `beautifulsoup4` (for scraping)