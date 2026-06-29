---
name: writing-style-analyzer
description: "Analyse writing samples and reverse-engineer a creator's style into a reusable Style Card, or construct a new style from an audience profile. Three modes: capture an existing style (scraping + samples), design a new style based on an audience profile, or model after a creator you admire. Use when the user wants to create a writing style card, capture a voice, analyse writing style, build a voice profile, design a content voice, or onboard a client's writing style. Also trigger on 'style card', 'writing style', 'capture this voice', 'what style should we write in', 'model after a creator', or 'create a voice for content'. Not for audience research or drafting posts — it defines the voice to write in."
argument-hint: <style-name>
---

# Writing Style Analyzer v2

> **Works standalone.** Run this skill on its own. It reads and writes under `content-workspace/` and uses anything useful already there (an audience profile in `content-workspace/profiles/` for Mode 2, or samples in `content-workspace/samples/`) — otherwise it asks you or proceeds without it. The other content-writing skills share this same workspace; see the project README for the full set. Nothing launches automatically.

## Overview

This skill creates a Writing Style Card — a concise, reusable reference file that captures how content should be written. Whenever you (or another content skill) write content later, this file sets the voice.

The skill operates in three modes:
- **Mode 1: Capture my style** — scrape the client's existing content and reverse-engineer their voice
- **Mode 2: Design a style for me** — construct an optimal style based on their audience profile and brand
- **Mode 3: Model after a creator** — analyse an admired creator's style and adapt it for the client

All three modes produce the same output: a Style Card as both `.md` and `.html` files.

## Arguments

Style name: $ARGUMENTS

## Prerequisites

This skill uses the same API keys as the Content Audience Profiler:

| Variable | Service | Purpose |
|---|---|---|
| `FIRECRAWL_API_KEY` | [firecrawl.dev](https://www.firecrawl.dev) | Content scraping (Modes 1 & 3) |
| `PERPLEXITY_API_KEY` | [perplexity.ai](https://perplexity.ai/settings/api) | Finding indexed content (Modes 1 & 3) |
| `XAI_API_KEY` | [console.x.ai](https://console.x.ai) | X/Twitter content (Modes 1 & 3) |

Mode 2 does not require any API keys — it reads the existing audience profile and client website.

Before starting, verify the required keys are available for the selected mode. If any are missing, tell the user which ones to set up.

## Workflow

### Step 1: Present Mode Selection

When the skill triggers, present the three options clearly:

```
Writing Style Analyzer

How do you want to build your writing style?

  1. Capture my style — I have content I'm happy with, analyse it
  2. Design a style for me — Build a style based on my audience profile
  3. Model after a creator — Base it on a creator I admire

Pick a number (1/2/3):
```

If the user's initial message already implies a mode (e.g., "create a style card based on my audience profile"), skip the menu and confirm the mode.

### Step 2: Collect Mode-Specific Inputs

---

**MODE 1: Capture My Style**

The client domain is the only required input. Everything else enriches the analysis but isn't blocking.

```
I'll scrape your website blog automatically. To get a richer analysis,
provide any of these (all optional — press enter to skip):

  - LinkedIn profile URL:
  - X/Twitter handle:
  - Newsletter archive URL (Substack, Beehiiv, etc.):
  - Or upload/paste content samples directly

Client domain: [ask if not already known]
```

Present all optional inputs at once — don't drip-feed them across multiple prompts.

The skill also reads writing samples from `content-workspace/samples/` if any `.md` or `.txt` files are present there. These are included automatically in addition to scraped content.

---

**MODE 2: Design a Style For Me**

No inputs needed beyond the client domain. The skill reads the existing audience profile.

First, scan `content-workspace/profiles/` for audience profile files (`.md` files with "profile" in the filename):

**If one profile found:**
```
Found: content-audience-profile-[slug].md
I'll use this to design your style. Generating now.
```

**If multiple profiles found:**
```
Found audience profiles:
  1. content-audience-profile-ops-leaders.md
  2. content-audience-profile-enterprise-ctos.md

Which profile should I base the style on? (1/2):
```

**If no profiles found:**
```
No audience profile found in content-workspace/profiles/.
I need an audience profile to design your style.

Options:
  1. Run the Content Audience Profiler first (recommended)
  2. Point me to the file if it's saved elsewhere
  3. Switch to Mode 1 or Mode 3 instead
```

---

**MODE 3: Model After a Creator**

```
Who do you want to model after?

  - Creator name: [required]
  - Their website/blog URL: [required — need at least one content source]

Optional (helps me gather more samples):
  - Their LinkedIn profile URL:
  - Their X/Twitter handle:
  - Their newsletter URL:
```

The creator name and at least one content URL are required. Everything else is optional enrichment.

---

### Step 3: Gather Source Material

This step varies by mode. Use the shared Python scripts for all API calls.

**API Integration:**

| Tool | Primary | Fallback |
|---|---|---|
| **Perplexity** | `perplexity_ask` MCP tool | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "..."` |
| **Firecrawl** | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py` (has domain/blog scraping logic) | — |
| **xAI/Grok** | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xai_research.py --query "..."` | — |

**CRITICAL — Use these exact scripts. Do NOT create new scripts or rename them.**

---

**MODE 1: Capture My Style**

Goal: gather 10-20 writing samples from the client's own content.

**3a. Scrape client blog posts**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --domain <client-domain> --blog-only
```

The `--blog-only` flag tells the script to focus on blog/article pages rather than product pages. It looks for `/blog`, `/articles`, `/resources`, `/insights`, `/news` paths and follows links to individual posts. Aim for 10-15 most recent posts.

If the standard blog scraper doesn't find blog content (some sites use unusual URL structures), fall back to the general scraper:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --domain <client-domain>
```

Then manually identify which pages contain authored content vs. product/marketing copy.

**3b. Scrape LinkedIn profile (if URL provided)**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --url "<linkedin-profile-url>"
```

LinkedIn blocks most scrapers. If Firecrawl returns an error or empty/minimal results, fall back to Perplexity:

**Primary — MCP (`perplexity_ask`):**
```
Find recent LinkedIn posts written by [creator name] at [company]. Return the full text of their most notable LinkedIn posts. Focus on posts with high engagement.
```

**Fallback — script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Find recent LinkedIn posts written by [creator name] at [company]. Return the full text of their most notable LinkedIn posts. Focus on posts with high engagement."
```

**3c. Pull X/Twitter posts (if handle provided)**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xai_research.py --query "Show me the 20 most recent posts from @<handle>. Return the full text of each post, not summaries."
```

**3d. Scrape newsletter archive (if URL provided)**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --url "<newsletter-archive-url>"
```

For Substack, the archive URL is typically `<publication>.substack.com/archive`. Scrape the archive page to get links to individual issues, then scrape 5-10 recent issues.

**3e. Search for indexed content**

**Primary — MCP (`perplexity_ask`):**
```
Find recent content, posts, and articles written by [creator name] at [company]. Return the full text or detailed summaries of their most notable pieces.
```

**Fallback — script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Find recent content, posts, and articles written by [creator name] at [company]. Return the full text or detailed summaries of their most notable pieces."
```

**3f. Read samples from content-workspace/samples/**

Check `content-workspace/samples/` for `.md` and `.txt` files. Read all found files and include them in the sample set. If the user uploaded or pasted content, include that too.

**3g. Quality check**

Count total samples gathered. Present to the user:

```
Sample collection complete:
  - Blog posts: [X]
  - LinkedIn posts: [X]
  - X/Twitter posts: [X]
  - Newsletter issues: [X]
  - Local samples: [X]
  - Other: [X]
  - Total: [X] samples

[If >= 10]: Good sample size. Proceeding with analysis.
[If 5-9]: Decent sample size. The analysis will work but could be stronger with more samples. Want to add any, or shall I proceed?
[If < 5]: Limited samples — the style card may miss patterns. I'd recommend adding more. You can paste LinkedIn posts, forward newsletters, or upload docs. Want to add more, or proceed with what we have?
```

---

**MODE 2: Design a Style For Me**

Goal: gather brand signals and audience context to construct an optimal style.

**3a. Read the audience profile**

Read the selected audience profile from `content-workspace/profiles/`. Extract:
- Audience sophistication level (determines formality and jargon level)
- Vocabulary library (the style should use "this audience says" language, not "they DON'T say" language)
- Emotional register (drives tone — skeptical audience = direct, evidence-first; aspirational audience = energetic, vision-forward)
- Platform-specific notes (LinkedIn style differs from newsletter style)
- Content triggers and anti-triggers (what resonates and what to avoid)
- Trusted voices section (what kind of voice earns credibility with this audience)

**3b. Scrape client website for brand signals**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/firecrawl_scrape.py --domain <client-domain>
```

Extract from the website:
- Brand voice signals — how do they currently present themselves? Formal/casual? Technical/accessible?
- Company personality — are they the scrappy challenger, the established authority, the friendly guide?
- Values and positioning — what do they stand for?

**3c. Determine primary platform**

Check the audience profile's platform-specific notes. If the primary platform isn't clear, ask the user.

---

**MODE 3: Model After a Creator**

Goal: gather 10-20 samples from the target creator and the client's audience context.

**3a-3e: Same as Mode 1**, but targeting the creator's content instead of the client's.

**3f: Read the client's audience profile**

Read the audience profile from `content-workspace/profiles/` to identify where the target creator's style aligns with the client's audience and where it might need adapting.

---

### Step 4: Analyse and Generate Style Card

Read `style-card-template.md` in this skill's directory for the exact output format and section-by-section guidance.

The analysis approach varies by mode:

---

**MODE 1: Capture My Style**

Reverse-engineer patterns from the gathered samples. Scan for consistent patterns across these dimensions:

- **Voice & Tone**: attitude, formality, POV, energy, emotional range
- **Structure & Formatting**: openers, pacing, line breaks, bullets vs paragraphs, scannability
- **Hook Patterns**: recurring opening moves (4-6 patterns)
- **Close Patterns**: recurring closing moves (4-6 patterns)
- **Rhetorical Devices**: contrast, questions, data usage, anecdotes, analogies, repetition
- **Syntax & Mechanics**: sentence length, punctuation, emphasis, emoji, numbers, edge
- **Vocabulary**: signature phrases, jargon level, words they avoid

If samples show conflicting patterns (e.g., blog posts are formal but LinkedIn is casual), identify the dominant pattern and note the variation. The Style Card should reflect how the creator writes most of the time.

**Quality flag**: If the samples show weak or inconsistent patterns — no clear voice, heavy jargon, generic corporate tone — note this in the delivery summary and suggest the client consider Mode 2 or Mode 3 for a stronger foundation.

---

**MODE 2: Design a Style For Me**

Construct the style from audience context and brand signals. For each dimension of the Style Card, make a deliberate design choice based on:

| Style dimension | Primary input | Logic |
|---|---|---|
| Voice & Tone | Audience emotional register + brand personality | Skeptical audience -> direct, no-BS tone. Aspirational audience -> energetic, forward-looking. |
| Formality | Audience sophistication level | Expert audience -> peer-level, in-group language. Beginner -> accessible, no unexplained jargon. |
| Structure | Primary platform | LinkedIn -> structured with line breaks. Newsletter -> flowing paragraphs. X -> tight and punchy. |
| Hook patterns | Audience content triggers | Design 4-6 hook types that align with what pulls the audience in. |
| Close patterns | Audience engagement patterns | If the audience comments -> end with questions. If they share -> end with quotable takeaways. |
| Vocabulary | Audience vocabulary library | Use the "this audience says" column. Avoid the "they DON'T say" column. |
| Devices | Audience proof types + credibility signals | If they trust specific data -> build in data citation habits. If they trust stories -> build in anecdote patterns. |

The resulting Style Card should feel intentionally designed, not generic.

---

**MODE 3: Model After a Creator**

Two-phase process:

**Phase 1: Reverse-engineer the creator's style** — same analysis as Mode 1, applied to the target creator's content.

**Phase 2: Adapt for the client's audience** — cross-reference the creator's style with the client's audience profile. For each style dimension, note:
- What carries over directly (the creator's strengths that align with the audience)
- What needs adjusting (where the creator's style doesn't fit the client's audience)

Add an "Adaptation Notes" section at the end of the Style Card (see template).

---

### Step 5: Generate the HTML Version

After writing the markdown Style Card, generate a single-file HTML page with the same content. Read `html-style-guide.md` in this skill's directory for the HTML template structure and styling requirements.

Same design principles as the audience profile HTML:
- Single file, all CSS inline
- Clean, modern typography (Google Font via CDN)
- Scannable — the Do/Don't table and Vocab sections should be visually clear
- Print-friendly
- Client name and style name prominent at the top

---

### Step 6: Save and Deliver

Generate a slug from the style name (e.g., "Kieran's LinkedIn Voice" -> `kierans-linkedin-voice`).

Save both files to `content-workspace/profiles/`:

```bash
mkdir -p content-workspace/profiles
```

- `content-workspace/profiles/writing-style-card-[slug].md`
- `content-workspace/profiles/writing-style-card-[slug].html`

Present both files and provide a summary:
- The style name and 2-3 sentence description of what's most distinctive about the voice
- Which mode was used and what data informed the analysis
- Sample count and source breakdown (Modes 1 & 3)
- Any areas where patterns were conflicting or data was thin
- For Mode 1: flag if the existing style showed weaknesses (suggest Mode 2 or 3)
- For Mode 3: the key adaptations made for the client's audience

---

## Edge Cases

**Fewer than 5 samples (Modes 1 & 3):** Proceed but flag that the analysis may miss patterns. The Style Card will be less reliable — emphasise this in the delivery summary. Suggest adding more samples or switching modes.

**Client has no blog (Mode 1):** Lean on LinkedIn, X, newsletter, uploaded samples, and files from `content-workspace/samples/`. If total samples are still low, suggest Mode 2 or 3 instead.

**LinkedIn scraping fails (Modes 1 & 3):** This is common — LinkedIn blocks scraping aggressively. Always fall back to Perplexity to search for indexed LinkedIn posts. If Perplexity also returns limited results, note in the delivery that LinkedIn samples are thin.

**No audience profile exists (Modes 2 & 3):** Mode 2 requires an audience profile — offer to run the Content Audience Profiler first or switch modes. Mode 3 can work without an audience profile (just analyse the creator), but the adaptation step will be weaker.

**Samples from very different contexts:** If gathered samples span blog posts, LinkedIn, and X, the voice may differ across platforms. Identify the dominant voice and note platform-specific variations in the Style Card.

**Target creator has very little public content (Mode 3):** If we can't gather enough samples from the target creator, tell the user what we found and suggest alternatives — a different creator, uploading samples manually, or switching to Mode 2.

**The client's existing style is weak (Mode 1):** If the analysis reveals inconsistent voice, heavy jargon, or generic corporate tone, flag it honestly in the delivery. Suggest Mode 2 or Mode 3 for a stronger foundation.
