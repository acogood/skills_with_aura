#!/usr/bin/env python3
"""
Firecrawl content scraper for Writing Style Analyzer.

Extends the base firecrawl_scrape.py with a --blog-only mode that focuses
on finding and scraping blog/article content rather than product pages.

Usage:
  python firecrawl_scrape.py --domain flowops.com --blog-only
  python firecrawl_scrape.py --domain flowops.com              (all key pages, same as audience profiler)
  python firecrawl_scrape.py --url "https://example.substack.com/archive"

Requires: FIRECRAWL_API_KEY environment variable (or in .env file)
Install: pip install firecrawl-py python-dotenv
"""

import argparse
import json
import os
import re
import sys
import time

try:
    from firecrawl import FirecrawlApp
except ImportError:
    print("Error: firecrawl-py not installed. Run: pip install firecrawl-py")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# Blog/content paths to try
BLOG_PATHS = [
    "/blog",
    "/articles",
    "/resources",
    "/insights",
    "/news",
    "/posts",
    "/content",
    "/stories",
    "/journal",
    "/writing",
]

# Standard product/company paths (same as audience profiler)
STANDARD_PATHS = [
    "/",
    "/product",
    "/products",
    "/features",
    "/platform",
    "/solutions",
    "/use-cases",
    "/pricing",
    "/about",
    "/about-us",
    "/customers",
    "/why-us",
]


def get_api_key():
    """Get Firecrawl API key from environment."""
    key = os.environ.get("FIRECRAWL_API_KEY")
    if not key:
        print("Error: FIRECRAWL_API_KEY not set.", file=sys.stderr)
        sys.exit(1)
    return key


def scrape_url(app, url, retries=2):
    """Scrape a single URL with retries. Returns markdown content or None."""
    for attempt in range(retries + 1):
        try:
            result = app.scrape_url(url, params={"formats": ["markdown"]})
            if result and result.get("markdown"):
                return result["markdown"]
            return None
        except Exception as e:
            error_msg = str(e).lower()
            if "404" in error_msg or "not found" in error_msg:
                return None
            if attempt < retries and ("429" in error_msg or "500" in error_msg or "timeout" in error_msg):
                time.sleep(2 ** attempt)
                continue
            print(f"  Warning: Failed to scrape {url}: {e}", file=sys.stderr)
            return None


def extract_blog_post_links(markdown, domain):
    """Extract links to individual blog posts from a blog index page."""
    # Find all internal links
    links = re.findall(r'\[([^\]]*)\]\(((?:/|https?://)[^\)]+)\)', markdown)
    post_links = []

    for text, url in links:
        # Normalise to full URL
        if url.startswith("/"):
            full_url = f"{domain}{url}"
        elif url.startswith(domain):
            full_url = url
        else:
            continue  # skip external links

        # Skip navigation/footer links — look for blog-like URL patterns
        url_lower = url.lower()
        # Blog posts typically have date-like or slug-like paths
        if any(pattern in url_lower for pattern in ["/blog/", "/articles/", "/posts/", "/insights/", "/resources/", "/news/"]):
            # Skip index pages and category pages
            if url_lower.rstrip("/") not in [f"{p}" for p in BLOG_PATHS]:
                post_links.append(full_url)

    # Deduplicate while preserving order
    seen = set()
    unique_links = []
    for link in post_links:
        if link not in seen:
            seen.add(link)
            unique_links.append(link)

    return unique_links


def extract_nav_links(markdown, domain):
    """Extract navigation links from homepage markdown."""
    links = re.findall(r'\[([^\]]+)\]\((/[^\)]+)\)', markdown)
    relevant_keywords = ["blog", "article", "resource", "insight", "news", "post", "writing", "content"]
    nav_links = []
    for text, path in links:
        text_lower = text.lower()
        path_lower = path.lower()
        if any(kw in text_lower or kw in path_lower for kw in relevant_keywords):
            nav_links.append(path)
    return list(set(nav_links))[:3]


def scrape_blog(domain, max_posts=15):
    """Find and scrape blog posts from a domain."""
    app = FirecrawlApp(api_key=get_api_key())

    domain = domain.strip().rstrip("/")
    if not domain.startswith("http"):
        domain = f"https://{domain}"

    results = {}
    blog_index_url = None

    # Phase 1: Find the blog index page
    print(f"Looking for blog on {domain}...", file=sys.stderr)

    for path in BLOG_PATHS:
        url = f"{domain}{path}"
        print(f"  Trying {path}...", end=" ", file=sys.stderr)
        content = scrape_url(app, url)
        if content and len(content.strip()) > 200:
            blog_index_url = url
            print(f"✓ Found blog index", file=sys.stderr)
            break
        else:
            print("✗", file=sys.stderr)
        time.sleep(0.5)

    # Fallback: check homepage nav for blog links
    if not blog_index_url:
        print("  No standard blog path found. Checking homepage navigation...", file=sys.stderr)
        homepage_content = scrape_url(app, f"{domain}/")
        if homepage_content:
            nav_links = extract_nav_links(homepage_content, domain)
            for path in nav_links:
                url = f"{domain}{path}"
                print(f"  Trying nav link {path}...", end=" ", file=sys.stderr)
                content = scrape_url(app, url)
                if content and len(content.strip()) > 200:
                    blog_index_url = url
                    print(f"✓ Found blog via nav", file=sys.stderr)
                    break
                else:
                    print("✗", file=sys.stderr)
                time.sleep(0.5)

    if not blog_index_url:
        print("\n  No blog found. This site may not have a blog section.", file=sys.stderr)
        return {}

    # Phase 2: Extract links to individual blog posts
    blog_index_content = scrape_url(app, blog_index_url)
    if not blog_index_content:
        print("  Could not read blog index page.", file=sys.stderr)
        return {}

    post_links = extract_blog_post_links(blog_index_content, domain)
    print(f"\n  Found {len(post_links)} potential blog post links", file=sys.stderr)

    if not post_links:
        # If no post links found, the index page itself might have content
        print("  No individual post links found. Saving blog index content.", file=sys.stderr)
        results[blog_index_url] = blog_index_content
        return results

    # Phase 3: Scrape individual blog posts (up to max_posts)
    posts_to_scrape = post_links[:max_posts]
    print(f"  Scraping {len(posts_to_scrape)} most recent posts...\n", file=sys.stderr)

    for i, url in enumerate(posts_to_scrape):
        print(f"  [{i+1}/{len(posts_to_scrape)}] {url[:80]}...", end=" ", file=sys.stderr)
        content = scrape_url(app, url)
        if content and len(content.strip()) > 300:  # blog posts should have substance
            results[url] = content
            print(f"✓ ({len(content)} chars)", file=sys.stderr)
        else:
            print("✗ (too short or empty)", file=sys.stderr)
        time.sleep(0.5)

    print(f"\nDone. Scraped {len(results)} blog posts from {domain}", file=sys.stderr)
    return results


def scrape_domain(domain):
    """Scrape standard key pages from a domain (same as audience profiler)."""
    app = FirecrawlApp(api_key=get_api_key())

    domain = domain.strip().rstrip("/")
    if not domain.startswith("http"):
        domain = f"https://{domain}"

    results = {}
    for path in STANDARD_PATHS:
        url = f"{domain}{path}"
        print(f"  Trying {path}...", end=" ", file=sys.stderr)
        content = scrape_url(app, url)
        if content and len(content.strip()) > 100:
            results[url] = content
            print(f"✓ ({len(content)} chars)", file=sys.stderr)
        else:
            print("✗", file=sys.stderr)
        time.sleep(0.5)

    print(f"\nDone. Scraped {len(results)} pages from {domain}", file=sys.stderr)
    return results


def scrape_single_url(url):
    """Scrape a single URL."""
    app = FirecrawlApp(api_key=get_api_key())

    print(f"Scraping {url}...", file=sys.stderr)
    content = scrape_url(app, url)
    if content and len(content.strip()) > 100:
        print(f"  ✓ ({len(content)} chars)", file=sys.stderr)
        return {url: content}
    else:
        print(f"  ✗ (not found or empty)", file=sys.stderr)
        return {}


def main():
    parser = argparse.ArgumentParser(description="Scrape content using Firecrawl")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--domain", help="Domain to scrape")
    group.add_argument("--url", help="Single URL to scrape")
    parser.add_argument("--blog-only", action="store_true", help="Focus on blog/article content only")
    parser.add_argument("--max-posts", type=int, default=15, help="Max blog posts to scrape (default: 15)")
    parser.add_argument("--output", help="Output file path (default: stdout)", default=None)

    args = parser.parse_args()

    if args.url:
        results = scrape_single_url(args.url)
    elif args.blog_only:
        results = scrape_blog(args.domain, max_posts=args.max_posts)
    else:
        results = scrape_domain(args.domain)

    output = json.dumps(results, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Results saved to {args.output}", file=sys.stderr)
    else:
        print("\n--- SCRAPED CONTENT ---")
        print(output)


if __name__ == "__main__":
    main()
