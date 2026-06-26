#!/usr/bin/env python3
"""
Perplexity API research script for Content Audience Profiler.

Sends a research query to Perplexity's Sonar model and returns a synthesised,
sourced answer. Used for audience research, competitor identification, and
deep pain point / language analysis.

Usage:
  python perplexity_research.py --query "What are the biggest pain points for Heads of Operations at mid-market SaaS companies?"
  python perplexity_research.py --query "Who are the top 5 competitors to FlowOps in workflow automation?" --output competitors.json

Output: JSON with the query, response text, and citations.

Requires: PERPLEXITY_API_KEY environment variable (or in .env file)
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


PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

# Using sonar-pro for deeper research with citations
DEFAULT_MODEL = "sonar-pro"


def get_api_key():
    """Get Perplexity API key from environment."""
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        print("Error: PERPLEXITY_API_KEY not set. Set it as an environment variable or in a .env file.")
        sys.exit(1)
    return key


def research(query, model=DEFAULT_MODEL):
    """Send a research query to Perplexity. Returns response text and citations."""
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # System prompt that guides Perplexity to return content-strategy-useful research
    system_prompt = (
        "You are a research assistant helping build a content audience profile. "
        "Your job is to provide specific, evidence-based insights about a target audience. "
        "Focus on: exact language and phrases the audience uses, specific pain points with "
        "frequency/severity indicators, named publications/communities/influencers they trust, "
        "and emotional drivers behind their professional decisions. "
        "Always cite your sources. Prefer recent data (last 12 months). "
        "Be specific — 'they care about ROI' is useless; '67% cite cross-functional alignment "
        "as their top challenge (Salesforce State of Ops, 2025)' is useful."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        "temperature": 0.1,  # low temperature for factual research
        "return_citations": True,
    }

    try:
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        result = {
            "query": query,
            "model": model,
            "response": data["choices"][0]["message"]["content"],
            "citations": data.get("citations", []),
        }

        return result

    except requests.exceptions.Timeout:
        print("Error: Perplexity API request timed out. Try again.", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Error: Perplexity API returned {e.response.status_code}: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Perplexity API request failed: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Research a topic using Perplexity API")
    parser.add_argument("--query", required=True, help="Research query to send to Perplexity")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Perplexity model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--output", help="Output file path (default: stdout)", default=None)

    args = parser.parse_args()

    print(f"Researching: {args.query[:80]}...", file=sys.stderr)
    result = research(args.query, args.model)
    print(f"Done. Response: {len(result['response'])} chars, {len(result['citations'])} citations", file=sys.stderr)

    output = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Results saved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
