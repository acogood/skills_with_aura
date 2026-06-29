---
name: talking-point-extractor
description: "Extract post-ready talking points from content (transcripts, articles, docs) organized into Educational, Spicy Take, Data Nugget, and Story Spark categories. Use when the user wants to pull content ideas, talking points, or social media angles from existing content for CONTENT CREATION purposes."
argument-hint: <source-description or file path>
---

# Talking-Point Extractor

## Overview

This skill scans raw content (transcripts, articles, documents, or pasted text) and extracts structured talking points that can be turned into high-performing social posts. It groups findings into 4 categories, each with specific field requirements, and tailors everything to a target audience.

The output is a clean markdown file, grouped by category, ready to hand off to a content writer or feed into a content creation workflow.

## Arguments

Source: $ARGUMENTS

## When to Use This Skill

Use this skill when:
- User wants to extract talking points or content ideas from existing content
- User provides a transcript, article, or doc and wants post-worthy angles
- User mentions repurposing long-form content into short-form posts
- User asks for viral angles, social media hooks, or content ideas from source material
- User wants to find the best insights in a piece of content for their audience

**Not for drafting finished posts** — it produces angles and talking points, not final copy.

## Inputs Required

### 1. Raw Content (Required)
The source material to extract from. Can be:
- Pasted text directly in the chat
- A file path provided by the user
- Files in `content-workspace/sources/` (scan automatically)
- Any document the user names — a report, blog post, meeting notes, or other working file in their project

If the user points at a file or pastes text, use that directly. If they name a topic without a path (e.g., "the positioning doc"), scan `content-workspace/sources/` and ask which file they mean when it's ambiguous.

### 2. Audience Profile (Recommended)
An audience profile file that describes who the content is for. Check for existing profiles in `content-workspace/profiles/` and offer to use one if found.

If no audience profile is available, ask the user to describe their target audience in a sentence or two (e.g., "CMOs at B2B SaaS companies" or "early-stage startup founders"). Use this to tailor hooks, value statements, and applications throughout.

## Workflow

### Step 1: Load Inputs

1. **Read the raw content.**
   - If the user provided a file path, read that file
   - If $ARGUMENTS names a document without a full path (e.g., "the positioning doc"), check `content-workspace/sources/` and the user's project for a matching file
   - If the user pasted text, use it directly
   - If none of the above, scan `content-workspace/sources/` for files and list them for the user to pick
2. **Read the audience profile.**
   - Check `content-workspace/profiles/` for existing audience profiles
   - If one or more exist, ask the user which to use (or auto-select if there's only one)
   - If no profile exists, ask the user for a brief audience description before proceeding

### Step 2: Extract Talking Points

Scan the entire source content once. For each passage, ask: "Could this become a standalone, high-value post for this audience?"

Extract up to **3 talking points per category** (12 max total). Only keep points that meet all three of these bars:
- **Clarity** — The idea is crisp and easy to grasp
- **Novelty** — It's fresh or surprising for the target audience
- **Proof** — It's grounded with a stat, quote, example, or story from the source

If a category has zero qualifying points, omit it entirely from the output.

### Step 3: Structure Each Talking Point

Every talking point must follow the field structure for its category (see Category Definitions below). Apply these voice and style rules across all categories:

**Voice & Style Rules:**
- Active verbs only. No hedging words like "maybe", "I think", "perhaps", "could potentially"
- Maximum 22 words per sentence. If a sentence is longer, split or trim it
- Every Hook must use one of: an open loop, a contrast, or a surprising number
- All Titles, Hooks, and Value fields must speak directly to the target audience and reference outcomes they care about

## Category Definitions

### 1. Educational
A lesson, framework, or how-to step the audience can learn from and act on.

**Fields:**
- **Title** — Speaks directly to the audience
- **Hook** — Opens a curiosity gap, contrast, or surprising fact
- **Core Insight** — Up to 3 bullets. Each bullet MUST include a concrete supporting detail (statistic, named example, explicit contrast, or quote from the source)
- **Application** — Must begin with "You can apply this by ..." and give a clear action step
- **Value** — A specific, measurable, or observable outcome for the audience (not a generic benefit)
- **Source** — Quoted phrase from the source + location (timestamp, paragraph, or section)
- **Emotion Tag** — One word: Surprise / Validation / Urgency / Curiosity / Relief

### 2. Spicy Take
A provocative, divisive opinion that challenges conventional thinking. Must imply a challenge (e.g., "Most experts get X wrong...").

**Fields:**
- **Title** — Speaks directly to the audience
- **Hook** — Must imply a challenge to the status quo
- **Hot Take** — The provocative opinion, stated boldly
- **Proof** — Evidence or reasoning from the source that supports the take
- **Value** — What the audience gains from this perspective
- **Source** — Quoted phrase + location
- **Emotion Tag** — One word

### 3. Data Nugget
One jaw-dropping statistic with a clear takeaway. The number always comes first.

**Fields:**
- **Title** — Speaks directly to the audience
- **Hook** — Number comes first
- **Data** — The statistic, number-first
- **Action** — What the audience should do based on this data
- **Context** — Why this number matters or what it compares to
- **Value** — Specific outcome for the audience
- **Source** — Quoted phrase + location
- **Emotion Tag** — One word

### 4. Story Spark
A short personal or illustrative story with a clear moral. Story must be ≤60 words. Lesson must be ≤20 words.

**Fields:**
- **Title** — Speaks directly to the audience
- **Hook** — Sets up the story with an open loop or contrast
- **Story** — Maximum 60 words
- **Lesson** — Maximum 20 words
- **Value** — What the audience gains from this story
- **Source** — Quoted phrase + location
- **Emotion Tag** — One word

## Output Format

Create a markdown file with all extracted points grouped by category. Use this structure:

```markdown
# Talking Points: [Brief description of source content]
## Audience: [Audience role/description]
## Source: [Name or description of original content]
---

## Educational

### [Title]
**Hook:** [Hook text]
**Core Insight:**
- [Bullet 1 with concrete detail]
- [Bullet 2 with concrete detail]
- [Bullet 3 with concrete detail — optional]

**Application:** You can apply this by [specific action step]
**Value:** [Specific, observable outcome]
**Source:** "[Quoted phrase]", [location]
**Emotion Tag:** [One word]

---

[Repeat for additional Educational points, up to 3]

## Spicy Take

### [Title]
**Hook:** [Hook text]
**Hot Take:** "[Provocative opinion]"
**Proof:** [Supporting evidence from source]
**Value:** [What audience gains]
**Source:** "[Quoted phrase]", [location]
**Emotion Tag:** [One word]

---

[Repeat for additional Spicy Takes, up to 3]

## Data Nugget

### [Title]
**Hook:** [Number-first hook]
**Data:** [Statistic, number first]
**Action:** [What to do with this data]
**Context:** [Why it matters]
**Value:** [Specific outcome]
**Source:** "[Quoted phrase]", [location]
**Emotion Tag:** [One word]

---

[Repeat for additional Data Nuggets, up to 3]

## Story Spark

### [Title]
**Hook:** [Hook text]
**Story:** [≤60 words]
**Lesson:** [≤20 words]
**Value:** [What audience gains]
**Source:** "[Quoted phrase]", [location]
**Emotion Tag:** [One word]
```

Omit any category that has zero qualifying points.

## Delivery

1. Generate a slug from the source description (e.g., "positioning report" → `positioning-report`)
2. Get today's date in YYYY-MM-DD format
3. Save the file to `content-workspace/talking-points/talking-points-{slug}-{YYYY-MM-DD}.md`
4. Give a brief summary: how many points extracted, which categories had the strongest material, and any notable gaps (e.g., "No Data Nuggets — the source didn't contain quantitative claims")

## Quality Checklist

Before finalizing, verify every talking point:
- Hook uses an open loop, contrast, or surprising number
- No sentence exceeds 22 words
- No hedging language (maybe, I think, perhaps, could potentially)
- All verbs are active voice
- Source field has a direct quote and location from the original content
- Value field describes a specific outcome, not a vague benefit
- Educational bullets each contain a concrete supporting detail
- Spicy Takes challenge conventional thinking
- Data Nuggets lead with the number
- Story Sparks stay within 60-word story / 20-word lesson limits

## Edge Cases

- **Short source (under 500 words):** Extract what's there. Don't pad with weak material. Note the limitation to the user.
- **No audience profile and user doesn't describe one:** Default to general professional audience. Flag this in the output header and suggest providing an audience profile for better results.
- **Highly technical source:** Translate jargon to match the audience's level of expertise.
- **No stories in source:** Omit Story Spark entirely. Don't fabricate.
- **No data/stats in source:** Omit Data Nugget entirely. Don't invent numbers.
