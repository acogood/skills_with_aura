---
name: post-enricher
description: "Generate enrichment options (story, case study, authority quote) that elevate a talking point or draft post. Uses live web research to find recent, verifiable case studies and quotes. Use when the user wants to add a story to a post, find a relevant example or case study, add a quote from a credible source, make a post more compelling, or enrich content with proof and narrative. Also trigger on 'add a story', 'find me an example', 'make this more compelling', 'add credibility', 'enrich this post', or 'find a case study for this'. Not for writing a post from scratch — it adds proof or narrative to an existing point or draft."
argument-hint: <talking-point or topic>
---

# Post Enricher v2

> **Works standalone.** Run this skill on its own. It reads and writes under `content-workspace/` and uses anything useful already there (an audience profile and style card in `content-workspace/profiles/`, or talking points in `content-workspace/talking-points/`) — otherwise it asks you or proceeds without it. The other content-writing skills share this same workspace; see the project README for the full set. Nothing launches automatically.

## Overview

This skill takes a talking point or draft post and generates three enrichment options that make the content more compelling, credible, and memorable. Each enrichment type serves a different purpose — the user picks the one (or combination) that best fits their post.

The skill automatically reads the audience profile and writing style card from `content-workspace/profiles/` and can browse talking points from `content-workspace/talking-points/`. It researches recent, verifiable case studies and quotes with the built-in `WebSearch`/`WebFetch` tools — finding sources, reading them, and verifying each claim on its page — rather than relying solely on training knowledge.

## Arguments

$ARGUMENTS

## Prerequisites

No API keys required. Research uses the built-in `WebSearch` + `WebFetch` tools — find sources, then
read the strongest ones and verify each claim on its own page before using it. Works out of the box —
nothing to configure.

## Inputs

### 1. Talking Point or Draft Post (Required)

The user can provide source material in three ways:

**Option A: Paste or describe it directly.** The user pastes a talking point, a rough draft, or describes a core idea. If provided via $ARGUMENTS, use it directly.

**Option B: Point to a talking points file.** The user says something like "enrich the AI agents talking points" or "add a story to my latest talking point." Search `content-workspace/talking-points/` for a matching file, open it, and present the talking points to pick from:

```
Here are the talking points in that file:

  1. [Educational] How to build an AI agent pipeline
  2. [Spicy Take] Most AI agent frameworks are overengineered
  3. [Data Nugget] 73% of AI agents fail in production

Which talking point do you want to enrich? (pick a number):
```

**Option C: Ask to see all talking points.** The user says "show me my talking points." Scan `content-workspace/talking-points/` for all talking point files (filenames starting with `talking-points-` or `viral-talking-points-`), group by date, show most recent first:

```
Talking points available:

  2026-03-01:
    1. talking-points-podcast-ep-42 (8 points)
    2. viral-talking-points-ai-agents-marketing (11 points)

  2026-02-28:
    3. talking-points-ahrefs-blog-post (6 points)

Which file? (1/2/3):
```

Then present the talking points within the chosen file to pick from.

Do NOT automatically scan and dump all talking points on the user unprompted. Only show the file list when they ask for it.

### 2. Audience Profile (Automatic)

Scan `content-workspace/profiles/` for `.md` files with "profile" in the filename.
- One found -> read it silently
- Multiple found -> ask which one to use
- None found -> ask the user "Who is this content for?" and use their answer

Extract from the profile: pain points, vocabulary library, trusted voices, proof types that build credibility. Use these to choose stories and examples from domains the audience respects.

### 3. Writing Style Card (Automatic)

Scan `content-workspace/profiles/` for `.md` files with "style" in the filename.
- One found -> read it silently
- Multiple found -> ask which one to use
- None found -> proceed without it

Match the tone, sentence length, and voice of the enrichments to the creator's style.

## The 3 Enrichment Types

### 1. Story Integration

A relevant story — historical, personal, or business — that makes the abstract concrete. The story reframes the reader's situation through a narrative they can feel.

**What makes a great story enrichment:**
- It directly maps to the core point of the post — not a generic anecdote
- It has a clear arc: situation -> tension -> resolution/lesson
- It's from a domain the audience respects or recognises
- It's specific: names, dates, numbers, details that make it real
- It's concise: 60-120 words
- The lesson connects back to the reader's situation explicitly

**Sources for stories:**
- Business history (company pivots, leadership decisions, product launches)
- Sports (coaching philosophy, team turnarounds, underdog wins)
- Science and research (experiments, discoveries, paradigm shifts)
- Historical figures (decisions, strategies, turning points)
- Personal stories the user has shared (if available in context)

**What to avoid:**
- Overused stories everyone has heard (Steve Jobs' Stanford speech, the marshmallow test)
- Stories that require too much context to understand
- Stories where the connection to the post is a stretch
- Fictional or unverifiable anecdotes

---

### 2. Example / Case Study

A mini case study or real-world example that proves the point. Not a full deep dive — just enough to make the reader go "ok, that's real."

**This is where live web research adds the most value.** Use it to find recent, verifiable examples rather than relying on training knowledge.

**Research it (`WebSearch` → `WebFetch`):**
`WebSearch` for a recent real-world example or case study about [topic] with a named company or
person, specific numbers or outcomes, from the last 24 months. Then `WebFetch` the top 1-3 results to
read them in full. Synthesize the example from what you actually read and cite the real source URL(s)
with an access date. Hold the bar: a named company/person, a specific number or outcome, last 24
months, verifiable — no unsourced claims.

**Verify before you use it:** confirm each stat or outcome on its own source page — don't trust a
number you only saw in a search snippet. Prefer primary or reputable sources (the company's own
report, a named publication) over vendor or SEO blogs. Discard fabricated-looking case studies —
suspiciously crisp percentages, a company you can't confirm exists, or claims that appear only on
content-marketing pages.

**What makes a great case study enrichment:**
- It's recent (ideally last 24 months) and verifiable
- It includes at least one specific number or outcome
- It names a real company, person, or product
- It directly demonstrates the post's core argument
- It's concise: 40-80 words
- It ends with a "so what" that ties back to the reader

**What to avoid:**
- Vague examples without specifics ("a company I know did this...")
- Examples that require the reader to already know the backstory
- Cherry-picked data that doesn't hold up to scrutiny
- Made up or unverifiable claims — if you're not confident it's real and recent, say so

---

### 3. Authority Quote

A quote from a respected figure that adds weight and credibility to the core argument.

**Research it (`WebSearch` → `WebFetch`):**
`WebSearch` for a verified quote from a respected [industry] leader about [topic], focusing on people
that [audience role] would respect and follow. Then `WebFetch` the source page to confirm the exact
wording and attribution before using it. Cite the source URL with an access date.

**Verify before you use it:** confirm the exact wording and attribution on a real page — prefer a
primary source (a transcript, the person's own post, a reputable publication) over a quote-aggregator
site. If you can't confirm the wording on a real page, don't use the quote.

If the audience profile has a "Trusted Voices" section, use those voices as a starting point for the search.

**What makes a great quote enrichment:**
- The person is respected by the target audience (not just generally famous)
- The quote directly supports the post's specific argument
- It's real, verifiable, and correctly attributed
- It's concise: 1-2 sentences max
- It adds a perspective the post doesn't already have

**What to avoid:**
- Generic motivational quotes that could apply to anything
- Quotes from controversial figures unless the controversy is relevant
- Misattributed quotes — if you cannot confidently verify a quote is real and correctly attributed, say so and offer to search for a verified alternative
- Long quotes that need trimming

## Workflow

### Step 1: Load Inputs

1. Get the talking point or draft (paste, file reference, $ARGUMENTS, or browse)
2. Load audience profile from `content-workspace/profiles/` (files with "profile" in name)
3. Load style card from `content-workspace/profiles/` (files with "style" in name)

### Step 2: Understand the Core Argument

Read the talking point or draft. Identify:
- **The single core argument** — what is the one thing this post is saying?
- **The audience's current situation** — what problem or question does this address?
- **The desired shift** — what should the reader think, feel, or do differently after reading?

### Step 3: Generate All 3 Enrichments

For each enrichment type, find the strongest option that directly maps to the core argument.

**Story:** Draw from Claude's knowledge of business, sports, science, and history. Prioritise lesser-known stories over cliches. If the audience profile mentions trusted voices or domains, prioritise stories from those domains.

**Case Study:** Use the built-in `WebSearch`/`WebFetch` tools to find recent, verifiable examples, and confirm each one on its source page. Only fall back to Claude's training knowledge if web research turns up nothing, and flag that the example may not be current.

**Quote:** Use the built-in `WebSearch`/`WebFetch` tools to find verified quotes from people the audience respects, confirming the wording on the source page. Cross-reference with the audience profile's "Trusted Voices" section if available. If you can't verify the attribution, say so.

Don't force it — if one type doesn't have a strong option, say so honestly rather than producing a weak enrichment.

### Step 4: Connect Each Enrichment Back

Every enrichment must end with an explicit connection back to the post's core argument and the reader's situation. The enrichment isn't decoration — it's proof.

### Step 5: Self-Check

Before presenting, verify each enrichment:
- [ ] Does it directly support the post's core argument (not just a vaguely related topic)?
- [ ] Is it specific (names, numbers, dates, details)?
- [ ] Is it concise (within the word limits)?
- [ ] Would this audience respect and recognise the source?
- [ ] Is it verifiable and accurately attributed?
- [ ] Did you open the source page and confirm the stat/quote there (not just trust a search snippet), and discard anything fabricated-looking — crisp fake percentages, an unconfirmable company?
- [ ] Does it end with a clear connection back to the reader's situation?
- [ ] Does it match the writing style card (if provided)?
- [ ] Does it use vocabulary from the audience profile?

### Step 6: Output

Save both markdown and HTML versions:

```bash
mkdir -p content-workspace/content/enrichments
```

**Filenames:**
- `content-workspace/content/enrichments/enrichment-YYYY-MM-DD-[talking-point-name].md`
- `content-workspace/content/enrichments/enrichment-YYYY-MM-DD-[talking-point-name].html`

Use today's date. Example: `enrichment-2026-04-07-ai-agent-pipeline.md`

Read `html-enrichment-guide.md` in this skill's directory for the HTML styling requirements.

**Markdown output format:**

```markdown
# Post Enrichment Options
## Core Argument: [1-sentence summary of the post's main point]
## Audience: [Audience from profile or user description]
## Style: [Style card name, or "No style card"]

---

### 1. Story Integration
**Story: [One-line label]**

[The story — 60-120 words, with specific details]

[Connection to the post and reader's situation — 1-2 sentences]

---

### 2. Example / Case Study
**Example: [Company/Person] — [One-line summary]**

[The case study — 40-80 words, with specific numbers and outcomes]

Source: [Publication, report, or public data source]

[Connection back to the post's core point — 1 sentence]

---

### 3. Authority Quote
**Quote: [Person's name], [Their relevant credential/role]**

"[The quote — 1-2 sentences max]"

Source: [Where this quote is from]

[Why this reinforces the core point for this audience — 1 sentence]

---

**Pick the enrichment that best fits your post — or combine a story with a quote for maximum impact.**
```

Present both files and ask the user which enrichment they want to use and whether they'd like help weaving it into their draft.

## Edge Cases

- **No strong story available:** Say so. "I couldn't find a story that directly maps to this argument. The case study is stronger for this one."
- **Can't verify a quote:** Don't include unverified quotes. Say: "I found a quote attributed to [person] but can't verify the exact wording. Want me to search for a confirmed alternative?"
- **Research returns weak results:** Re-run the `WebSearch` with different terms and `WebFetch` a few more results before giving up. Only if the web genuinely comes up empty, fall back to Claude's training knowledge and flag it: "This example is from my training data — I'd recommend verifying it's still accurate."
- **User provides a very rough idea:** Extract the core argument first, confirm it with the user, then generate enrichments.
- **Talking point is already story-heavy:** Flag this and suggest the case study or quote instead.
- **Multiple strong options for one type:** Present the best one in the main output, and mention: "I had a strong alternative story about [X] — want to see that one too?"

## API Integration Summary

| Need | How |
|---|---|
| **Web research** | Built-in `WebSearch` to find sources → `WebFetch` the top 1-3 to read them → verify each cited claim on its page → synthesize and cite real URLs with an access date |

**Use the built-in `WebSearch`/`WebFetch` tools, and verify every cited stat/quote on its own source page before using it.** No API keys are required — the skill runs with zero keys. Do NOT create alternative research scripts.
