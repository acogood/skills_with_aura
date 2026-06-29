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

No API keys required. Like the Content Audience Profiler, this skill researches with built-in tooling:

- **Reading pages** (the client's or a creator's blog, newsletter archive, profile) uses the
  built-in `WebFetch` tool on named URLs.
- **Finding indexed content** (LinkedIn/X posts, articles) uses the built-in `WebSearch` to find
  sources, then `WebFetch` to read them — relying on the actual on-page wording, not a search snippet.

Built-in `WebFetch` reads a known URL but doesn't *crawl/discover* a site, so to gather many samples
(Modes 1 & 3) fetch a blog/archive index, follow the post links it lists, and ask the user to paste
or link specific posts when discovery falls short. Mode 2 needs no live lookups beyond the client
website — it reads the existing audience profile.

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

This step varies by mode. Use the built-in research tooling below for all live lookups.

**API Integration:**

| Need | How |
|---|---|
| **Finding indexed content** (LinkedIn/X posts, articles) | Built-in `WebSearch` to find sources → `WebFetch` the top results to read them → confirm the wording on the page → cite real URLs |
| **Reading a specific page** (blog, newsletter archive, profile) | Built-in `WebFetch` on the named URL |

**Use the built-in `WebSearch`/`WebFetch` tools, and confirm each sample's wording on its own source page before relying on it.** No API keys are required — the skill runs with zero keys. Built-in `WebFetch` reads a known URL but does not crawl/discover a site, so ask the user for specific links when sample discovery falls short. Do NOT create alternative research scripts.

---

**MODE 1: Capture My Style**

Goal: gather 10-20 writing samples from the client's own content.

**3a. Read client blog posts**

Use the built-in `WebFetch` tool. First fetch the blog/article index — try `/blog`, `/articles`,
`/resources`, `/insights`, `/news` on the client domain. Read the list of post links the index
returns, then `WebFetch` each individual post. Aim for the 10-15 most recent posts.

`WebFetch` reads a known URL but doesn't discover pages, so if no standard blog index exists (some
sites use unusual URL structures), ask the user for the blog URL or specific post links. Make sure
you're reading authored content (posts/articles), not product/marketing copy.

**3b. Gather LinkedIn posts (if URL provided)**

Try `WebFetch` on the LinkedIn profile URL first. LinkedIn blocks most automated fetching, so if it
returns an error or empty/minimal content, find indexed posts instead:

**Find indexed posts (`WebSearch` → `WebFetch`):**
`WebSearch` for "[creator name] [company] LinkedIn posts" and `WebFetch` any publicly indexed posts
it surfaces, reading the full text on the page. If it comes up thin (common — LinkedIn is hard to
fetch), ask the user to paste a few representative posts. Use the actual on-page wording — don't
reconstruct a post from a search snippet.

**3c. Gather X/Twitter posts (if handle provided)**

There's no API pull for X. Try, in order: `WebFetch` on specific post URLs the user provides;
`WebSearch` for indexed posts (e.g. "[creator] X posts about [topic]") and `WebFetch` what it
surfaces; or ask the user to paste 10-20 representative posts. X content is often not fetchable, so
the pasted-sample route is usually the most reliable for capturing voice.

**3d. Read newsletter archive (if URL provided)**

Use `WebFetch` on the archive page. For Substack, the archive URL is typically
`<publication>.substack.com/archive`. Fetch the archive page to get links to individual issues, then
`WebFetch` 5-10 recent issues.

**3e. Search for indexed content**

**Find indexed content (`WebSearch` → `WebFetch`):**
`WebSearch` for "[creator name] [company] articles posts", then `WebFetch` the strongest results to
read the full pieces on the page. Cite the source URLs, and rely on the wording you actually read —
not a search snippet.

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

**3b. Read the client website for brand signals**

Use `WebFetch` on the client's homepage and a couple of positioning pages (`/about`, a product or
solutions page). Extract from the website:
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

**LinkedIn fetching fails (Modes 1 & 3):** This is common — LinkedIn blocks automated fetching aggressively. Use the built-in `WebSearch` to find indexed LinkedIn posts and `WebFetch` what it surfaces, or ask the user to paste a few. If samples are still limited, note in the delivery that LinkedIn samples are thin.

**No audience profile exists (Modes 2 & 3):** Mode 2 requires an audience profile — offer to run the Content Audience Profiler first or switch modes. Mode 3 can work without an audience profile (just analyse the creator), but the adaptation step will be weaker.

**Samples from very different contexts:** If gathered samples span blog posts, LinkedIn, and X, the voice may differ across platforms. Identify the dominant voice and note platform-specific variations in the Style Card.

**Target creator has very little public content (Mode 3):** If we can't gather enough samples from the target creator, tell the user what we found and suggest alternatives — a different creator, uploading samples manually, or switching to Mode 2.

**The client's existing style is weak (Mode 1):** If the analysis reveals inconsistent voice, heavy jargon, or generic corporate tone, flag it honestly in the delivery. Suggest Mode 2 or Mode 3 for a stronger foundation.
