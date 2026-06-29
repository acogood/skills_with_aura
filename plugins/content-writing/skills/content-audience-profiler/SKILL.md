---
name: content-audience-profiler
description: "Build a comprehensive, research-backed content audience profile by scraping a client's website, researching their audience across the web, and synthesising everything into a reusable 10-section audience profile. Use when the user wants to build an audience profile for CONTENT CREATION, understand their content audience, or define who they're writing for. Also trigger on 'audience profile', 'content persona', 'who are we writing for', 'audience research for content', or 'onboard a new client'. Do NOT trigger during AI CMO pipeline enrichment work."
argument-hint: <client-domain>, <target-audience>
---

# Content Audience Profiler v2

## Overview

This skill creates a detailed, actionable content audience profile for a client. It's a reusable reference: whenever you (or another content skill) write for this audience later, the profile sets the tone, depth, and vocabulary so the content reads like it was written by someone who deeply understands the reader.

The profile answers: **what makes this audience stop scrolling, click, read, engage, and share?** It captures vocabulary, emotional register, pain points, situational framings, and platform-specific guidance — everything a content skill needs to write something that feels like it was written by someone who deeply understands the reader.

The skill produces two outputs:
- `content-audience-profile-[slug].md` — machine-readable profile for other skills
- `content-audience-profile-[slug].html` — clean, modern web page for the client to review and share

## Arguments

$ARGUMENTS

## Prerequisites

This skill requires three API keys set as environment variables (or in a `.env` file in the project root):

| Variable | Service | Purpose |
|---|---|---|
| `FIRECRAWL_API_KEY` | [firecrawl.dev](https://firecrawl.dev) | Website and review page scraping |
| `PERPLEXITY_API_KEY` | [perplexity.ai](https://perplexity.ai/settings/api) | Deep audience research |
| `XAI_API_KEY` | [console.x.ai](https://console.x.ai) | X/Twitter audience language |

Before starting, verify all three keys are available. If any are missing, tell the user which ones they need to set up and where to get them.

## Inputs

### Required (3 inputs — ask before starting)

1. **Client domain** — their website URL (e.g., `flowops.com`)
2. **Target audience** — one sentence describing who they create content for (e.g., "Heads of Operations at mid-market SaaS companies")
3. **Primary content platform** — LinkedIn, Newsletter, X, or Other

### Optional (offer after automated research, don't block on these)

- Uploaded files: sales decks, call transcripts, content samples, LinkedIn posts
- These enrich the profile but aren't required for a strong first draft

## Workflow

Follow these steps in order. The goal is to minimise user effort — the skill does the heavy lifting.

### Step 1: Collect Inputs

Ask for the three required inputs. If the user provides them in their initial message or via $ARGUMENTS, skip straight to Step 2.

### Step 2: Automated Research

This step requires no user input. Run all research in sequence.

**2a. Scrape client website**

Use the Firecrawl scraping script:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --domain <client-domain>
```

This attempts to scrape: homepage, /product, /features, /platform, /solutions, /use-cases, /pricing, /about. Pages that 404 are skipped. If the homepage has navigation links to product/feature pages with non-standard URLs, the script extracts and follows those too.

Save the output — you'll need it for profile generation.

**2b. Identify competitors**

**Primary method — Perplexity MCP tool:**

Use the `perplexity_ask` MCP tool:
```
Who are the top 4-5 direct competitors to [company name] in [their category]? Return company names and domains only.
```

**Fallback — Python script (if MCP unavailable):**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Who are the top 4-5 direct competitors to [company name] in [their category]? Return company names and domains only."
```

Present the competitor list to hold for the confirmation checkpoint (Step 3).

**2c. Scrape competitor websites**

Run Firecrawl on the top 2-3 competitor domains (same page pattern as 2a):

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --domain <competitor-domain>
```

**2d. Scrape G2/Capterra reviews (if they exist)**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --url "https://www.g2.com/products/<product-name>/reviews"
```

If the page 404s or returns no review content, skip gracefully. Not every company has G2 reviews. Note in the final output which sections have thinner data because reviews weren't available.

**2e. Deep audience research — Perplexity Call 1 (pain points & language)**

**Primary — MCP (`perplexity_ask`):**
```
What are the biggest pain points and frustrations for [audience role] in [industry]? How do they describe these problems in their own words? What do they complain about in forums, Reddit, and community discussions? Include specific language and phrases they use. Cite sources.
```

**Fallback — script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "What are the biggest pain points and frustrations for [audience role] in [industry]? How do they describe these problems in their own words? What do they complain about in forums, Reddit, and community discussions? Include specific language and phrases they use. Cite sources."
```

**2f. Deep audience research — Perplexity Call 2 (content habits & identity)**

**Primary — MCP (`perplexity_ask`):**
```
What content does [audience role] in [industry] consume? Who do they trust and follow? What publications, newsletters, podcasts, and communities are they active in? How do they want to be perceived professionally? What does success look like to them? Cite sources.
```

**Fallback — script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "What content does [audience role] in [industry] consume? Who do they trust and follow? What publications, newsletters, podcasts, and communities are they active in? How do they want to be perceived professionally? What does success look like to them? Cite sources."
```

**2g. X/Twitter audience research — Grok**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xai_research.py --query "What are [audience role] in [industry] talking about on X/Twitter? What topics, frustrations, and conversations are getting engagement? What language and phrases do they use when discussing [topic area]? Who are the voices they engage with most?"
```

**2h. LinkedIn audience research — Perplexity**

LinkedIn blocks direct scraping. Use Perplexity to find indexed LinkedIn content from the target audience:

**Primary — MCP (`perplexity_ask`):**
```
Find recent LinkedIn posts and discussions by [audience role] in [industry] about [topic area]. What language do they use? What topics get the most engagement? What are they complaining about or celebrating? Include specific phrases and examples.
```

**Fallback — script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Find recent LinkedIn posts and discussions by [audience role] in [industry] about [topic area]. What language do they use? What topics get the most engagement? What are they complaining about or celebrating? Include specific phrases and examples."
```

**2i. Parse uploaded files (if any)**

If the user provided files, read them and extract audience-relevant signals: pain point language, objections, how the client talks about their customers, what questions prospects ask.

### Step 3: Confirmation Checkpoint

Before generating the full profile, present a quick summary for the user to confirm or adjust. Keep this fast — yes/no/tweak questions, not open-ended.

Present:
1. **"Here's the audience I've identified:"** — 2-3 sentence description synthesised from website + research. Ask: "Sound right, or would you adjust?"
2. **"Competitors I found:"** — list of 4-5 with domains. Ask: "Any to swap or add?"
3. **"Top pain points from research:"** — ranked list of 3-4. Ask: "Anything missing or wrong?"

Apply any adjustments before proceeding.

### Step 4: Optional Enrichment

After the confirmation checkpoint, offer:

> "These are optional but would make the profile stronger:
> - Upload any content samples (LinkedIn posts, newsletters, blog posts)
> - Upload any customer-facing docs (sales decks, call transcripts, support FAQs)
>
> Skip? No problem — I have enough for a strong first draft."

If the user provides files, parse them and integrate the signals into the profile.

### Step 5: Generate the Profile

Synthesise ALL gathered data into the 10-section profile. Read `profile-template.md` in this skill's directory for the exact template structure and section-by-section guidance. See `worked-example.md` for a complete worked example (FlowOps case study).

The profile template has 10 sections:

1. **Audience Identity** — who they are, how they see themselves, sophistication level
2. **Jobs to Be Done** — primary functional job + emotional and social jobs
3. **Pain Points (Prioritised)** — top 3, ranked, with exact language
4. **Vocabulary Library** — what they say vs. what they don't say, in-group terms, outsider terms
5. **Emotional Register & Validation Hooks** — default emotional state, 5 ready-to-use validation hooks, emotional sequence
6. **Content Triggers & Anti-Triggers** — what pulls them in AND what makes them scroll past
7. **Situational Framings** — 4 vivid, recognisable scenarios to use as content openers
8. **Trusted Voices & Proof Types** — who they listen to, what proof they respect, what undermines credibility
9. **Platform-Specific Notes** — format/voice/engagement notes for each relevant platform
10. **Update & Measurement Log** — metrics to track, revision history

**Critical quality rules:**
- Every claim should be grounded in the research data gathered in Step 2. If you're guessing, flag it.
- Use the audience's actual language in the profile, not your paraphrasing of it.
- The vocabulary library is the highest-leverage section. Get this right.
- Pain points must be ranked by evidence (frequency x severity), not by what feels important.
- Validation hooks should be specific enough that a real person in this audience would think "that's exactly my situation."
- Anti-triggers are as important as triggers — they're the guardrails that prevent tone-deaf content built from this profile.

### Step 6: Generate the HTML Version

After writing the markdown profile, generate a single-file HTML page with the same content, styled as a clean, modern, client-facing document.

Read `html-template-guide.md` in this skill's directory for the HTML template structure and styling requirements.

The HTML version should be:
- **Single file** — all CSS inline, no external dependencies
- **Clean and modern** — good typography (use a Google Font loaded via CDN), generous whitespace, subtle section dividers
- **Scannable** — clear section headers, the vocabulary library as a well-formatted table, validation hooks that stand out visually
- **Print-friendly** — include print media queries
- **Branded** — include the client's company name prominently. If you extracted a primary brand colour from their website, use it as an accent colour. Otherwise default to a neutral professional palette.

### Step 7: Save and Deliver

Generate a slug from the audience name (e.g., "Mid-Market Ops Leaders" -> `mid-market-ops-leaders`).

Save both files to `content-workspace/profiles/`:

```bash
mkdir -p content-workspace/profiles
```

- `content-workspace/profiles/content-audience-profile-[slug].md`
- `content-workspace/profiles/content-audience-profile-[slug].html`

Present both files to the user and provide a brief summary:
- Which sections had the strongest research backing
- Which sections are thinner (e.g., reviews weren't available, X data was sparse)
- Any areas where the user should apply their own judgment or provide additional input

## Edge Cases

**Client has no G2/Capterra reviews:** Skip the review scraping step. Note in the delivery summary that pain point language is based on community/forum research rather than product reviews. Suggest the user validate the vocabulary library with their sales team.

**Very niche audience:** Research may be thin. Do your best with available data, clearly flag where you're extrapolating from broader audience research, and suggest the user validate with their own audience knowledge.

**Very broad audience (e.g., "marketers"):** Push back gently before starting research. "Marketers" is too broad — a CMO and a junior social media manager have completely different content triggers. Ask the user to narrow to a specific role and seniority level.

**Client website is thin or uninformative:** Some early-stage companies have minimal websites. Lean more heavily on Perplexity research and competitor analysis to build the profile. Note in the delivery that the profile is primarily research-based rather than grounded in the client's own positioning.

**API failures:** If any API call fails (Firecrawl timeout, Perplexity rate limit, Grok error), log the error, skip that step, and note it in the delivery summary. The profile can still be generated with partial data — just flag which sections are affected.

**Multiple audiences:** One profile per run. If the client needs profiles for multiple audience segments, tell them to run the skill again with different audience descriptions. Each profile is saved as a separate file.

## API Integration Summary

| Tool | Primary | Fallback |
|---|---|---|
| **Perplexity** | `perplexity_ask` MCP tool | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "..."` |
| **Firecrawl** | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py` (has domain/blog scraping logic) | — |
| **xAI/Grok** | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xai_research.py --query "..."` | — |

**CRITICAL: Use the scripts listed above. Do NOT create alternative scripts.** They handle authentication, retries, and error handling.
