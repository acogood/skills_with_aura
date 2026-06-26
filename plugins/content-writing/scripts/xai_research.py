#!/usr/bin/env python3
"""
xAI (Grok) research script for Content Audience Profiler.

Queries Grok to extract audience language patterns, engagement signals,
and trending topics from X/Twitter. Grok has native access to X data,
making it uniquely useful for understanding how audiences talk informally.

Usage:
  python xai_research.py --query "What are Heads of Operations talking about on X? What frustrations and topics get engagement? What language do they use?"

Output: JSON with the query and Grok's response.

Requires: XAI_API_KEY environment variable (or in .env file)
Install: pip install requests python-dotenv
"""

import argparse
import json
import os
import sys

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


XAI_API_URL = "https://api.x.ai/v1/chat/completions"
DEFAULT_MODEL = "grok-3-latest"


def get_api_key():
    """Get xAI API key from environment."""
    key = os.environ.get("XAI_API_KEY")
    if not key:
        print("Error: XAI_API_KEY not set. Set it as an environment variable or in a .env file.")
        sys.exit(1)
    return key


def research(query, model=DEFAULT_MODEL):
    """Send a research query to Grok. Returns response text."""
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    system_prompt = (
        "You are a research assistant analysing X/Twitter conversations for a content strategy project. "
        "Your job is to find how a specific professional audience talks on X — their language, "
        "frustrations, topics that get engagement, and voices they interact with. "
        "Focus on: exact phrases and language patterns (informal, unfiltered), "
        "topics currently getting engagement and replies, "
        "named accounts/voices this audience engages with, "
        "and the emotional tone of their posts (frustrated, aspirational, humorous, etc.). "
        "Be specific — include real examples of language patterns and topics where possible."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        "temperature": 0.1,
    }

    try:
        response = requests.post(XAI_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        result = {
            "query": query,
            "model": model,
            "response": data["choices"][0]["message"]["content"],
        }

        return result

    except requests.exceptions.Timeout:
        print("Error: xAI API request timed out. Try again.", file=sys.stderr)
        return {"query": query, "model": model, "response": "", "error": "timeout"}
    except requests.exceptions.HTTPError as e:
        print(f"Error: xAI API returned {e.response.status_code}: {e.response.text}", file=sys.stderr)
        return {"query": query, "model": model, "response": "", "error": str(e)}
    except Exception as e:
        print(f"Error: xAI API request failed: {e}", file=sys.stderr)
        return {"query": query, "model": model, "response": "", "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Research X/Twitter audience language using Grok")
    parser.add_argument("--query", required=True, help="Research query about audience behaviour on X")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Grok model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--output", help="Output file path (default: stdout)", default=None)

    args = parser.parse_args()

    print(f"Researching X/Twitter: {args.query[:80]}...", file=sys.stderr)
    result = research(args.query, args.model)

    if result.get("error"):
        print(f"Warning: Grok query returned an error: {result['error']}", file=sys.stderr)
        print("The profile can still be generated — X/Twitter data will be thinner.", file=sys.stderr)
    else:
        print(f"Done. Response: {len(result['response'])} chars", file=sys.stderr)

    output = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Results saved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
