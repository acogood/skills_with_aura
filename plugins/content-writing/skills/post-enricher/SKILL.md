---
name: post-enricher
description: "Generate enrichment options (story, case study, authority quote) that elevate a talking point or draft post. Uses Perplexity to find recent, verifiable case studies and quotes. Use when the user wants to add a story to a post, find a relevant example or case study, add a quote from a credible source, make a post more compelling, or enrich content with proof and narrative. Also trigger on 'add a story', 'find me an example', 'make this more compelling', 'add credibility', 'enrich this post', or 'find a case study for this'. Not for writing a post from scratch — it adds proof or narrative to an existing point or draft."
argument-hint: <talking-point or topic>
---

# Post Enricher v2

## Overview

This skill takes a talking point or draft post and generates three enrichment options that make the content more compelling, credible, and memorable. Each enrichment type serves a different purpose — the user picks the one (or combination) that best fits their post.

The skill automatically reads the audience profile and writing style card from `content-workspace/profiles/` and can browse talking points from `content-workspace/talking-points/`. It uses Perplexity to research recent, verifiable case studies and quotes rather than relying solely on training knowledge.

## Arguments

$ARGUMENTS

## Prerequisites

### API Key

| Variable | Purpose |
|---|---|
| `PERPLEXITY_API_KEY` | Finding recent case studies, examples, and verified quotes |

This key should already be in your project root `.env` file from other skills.

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

**This is where Perplexity adds the most value.** Use it to find recent, verifiable examples rather than relying on training knowledge.

**Primary — Perplexity MCP (`perplexity_ask`):**
```
Find a recent real-world example or case study about [topic]. Must include specific company or person name, specific numbers or outcomes, and be from the last 24 months. Cite the source.
```

**Fallback — Python script (if MCP unavailable):**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Find a recent real-world example or case study about [topic]. Must include specific company or person name, specific numbers or outcomes, and be from the last 24 months. Cite the source."
```

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

**Primary — Perplexity MCP (`perplexity_ask`):**
```
Find a verified quote from a respected [industry] leader about [topic]. Must be correctly attributed with source. Focus on people that [audience role] would respect and follow.
```

**Fallback — Python script:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "Find a verified quote from a respected [industry] leader about [topic]. Must be correctly attributed with source. Focus on people that [audience role] would respect and follow."
```

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

**Case Study:** Use Perplexity to search for recent, verifiable examples. If Perplexity returns weak results, fall back to Claude's training knowledge but flag that the example may not be current.

**Quote:** Use Perplexity to search for verified quotes from people the audience respects. Cross-reference with the audience profile's "Trusted Voices" section if available. If you can't verify the attribution, say so.

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
- **Perplexity returns weak results:** Fall back to Claude's training knowledge. Flag that the example may not be current: "This example is from my training data — I'd recommend verifying it's still accurate."
- **User provides a very rough idea:** Extract the core argument first, confirm it with the user, then generate enrichments.
- **Talking point is already story-heavy:** Flag this and suggest the case study or quote instead.
- **Multiple strong options for one type:** Present the best one in the main output, and mention: "I had a strong alternative story about [X] — want to see that one too?"
- **No Perplexity API key and MCP unavailable:** Skip the research calls. Use Claude's training knowledge only. Note in the output that examples and quotes may not be the most recent available.

## API Integration Summary

| Tool | Primary | Fallback |
|---|---|---|
| **Perplexity** | `perplexity_ask` MCP tool | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/perplexity_research.py --query "..."` |

**CRITICAL: Use the script listed above. Do NOT create alternative scripts.** The `perplexity_research.py` handles authentication, retries, and error handling.
