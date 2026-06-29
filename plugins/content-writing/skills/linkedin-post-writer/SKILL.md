---
name: linkedin-post-writer
description: "Draft a ready-to-post LinkedIn post (2-3 hook/angle variants) from talking points and enrichment you've already gathered, matched to your audience profile and writing style card and written to LinkedIn best-practice rules so the draft passes review. Use when the user wants to write or draft a LinkedIn post, turn talking points into a post, or write up an enriched idea for LinkedIn. Also trigger on 'draft a LinkedIn post', 'write a post about', 'turn these talking points into a post', or 'write this up for LinkedIn'. Not for extracting talking points from source material (that's talking-point-extractor), not for adding stories/quotes/case studies to a point (that's post-enricher), not for reviewing or critiquing an existing draft (that's linkedin-post-reviewer), and not for blog posts, newsletters, ads, or other non-LinkedIn copy."
argument-hint: <topic, talking-point file, or pasted idea>
---

# LinkedIn Post Writer

> **Works standalone.** Run this skill on its own. It reads and writes under `content-workspace/` and
> uses anything useful already there (talking points in `content-workspace/talking-points/`, enrichment
> in `content-workspace/content/enrichments/`, an audience profile and style card in
> `content-workspace/profiles/`) — otherwise it asks you or proceeds without it. The other
> content-writing skills share this same workspace; see the project README for the full set. Nothing
> launches automatically.

## Overview

This skill turns the raw material you've already gathered — talking points and enrichment — into a
finished LinkedIn post. It is the **drafting** step that sits between `post-enricher` and
`linkedin-post-reviewer`:

```
talking-point-extractor → post-enricher → linkedin-post-writer (you are here) → linkedin-post-reviewer
```

One run produces **2-3 distinct hook/angle variants** of the same post, each a complete draft written
to LinkedIn's best-practice rules so it passes review cleanly. It reads your audience profile for *who*
you're writing to and your style card for *how* you sound, then composes posts that carry your voice
while obeying the platform's structural rules.

It **does not research** — the proof (stories, case studies, quotes, stats) comes from the enrichment
you already produced. If a draft needs proof that isn't there, the skill says so and points you back to
`post-enricher` rather than inventing a number.

## Arguments

`$ARGUMENTS` — a topic, a talking-point file reference, or a pasted idea/draft
(e.g., "the distribution-vs-positioning point", "write up the AI-slop take", or pasted text).

## Prerequisites

No API keys required, and **no web research** — this skill composes from material already in
`content-workspace/`. Works out of the box.

## Inputs

### 1. The core material (required — one of these)

The user can provide the source in three ways:

**Option A: Point to a talking-points file.** "Write a post from the Greg Isenberg talking points" or
"draft the distribution point." Search `content-workspace/talking-points/` for files starting with
`talking-points-` or `viral-talking-points-`, open the match, and present the points to pick from:

```
Here are the talking points in that file:

  1. [Educational] Nail your one-sentence value prop before you touch a channel
  2. [Spicy Take] Distribution won't save bad positioning
  3. [Data Nugget] 85% of the world still doesn't use AI

Which point do you want to write a post about? (pick a number, or "combine 2 and 3"):
```

**Option B: Paste or describe it directly.** The user pastes a talking point, a rough idea, or a few
lines. Use it as the core argument directly.

**Option C: Name a topic via `$ARGUMENTS`.** If the topic maps to an existing talking point, use it;
otherwise build the post from the topic plus whatever enrichment and profile context exist, and note
that no talking point backed it.

### 2. Enrichment (automatic)

Scan `content-workspace/content/enrichments/` for enrichment files matching the chosen point/topic.
If found, read it and pull the **story, case study, and authority quote** (with their source URLs) to
weave proof into the draft. If none is found, draft from the talking point's own `Source`/`Proof`
lines and note that the post would be stronger with enrichment (`post-enricher`).

### 3. Audience profile (automatic)

Scan `content-workspace/profiles/` for `.md` files with **"profile"** in the filename.
- One found → read it silently.
- Multiple found → ask which one to use.
- None found → ask "Who is this post for?" and use the answer.

Extract: who they are, their pain points, the vocabulary they use, and what they find credible. Write
*to* this reader — layman framing first, niche depth second (see write-for-a-no-context-reader below).

### 4. Writing style card (automatic)

Scan `content-workspace/profiles/` for `.md` files with **"style"** in the filename.
- One found → read it silently.
- Multiple found → ask which one to use.
- None found → proceed with a neutral, strong LinkedIn voice and say so.

Apply the style card's **abstract voice DNA** — attitude, hook patterns, close patterns, rhetorical
devices, syntax. See the reconciliation rule next when the card and LinkedIn rules disagree.

### Reconciling style card vs. LinkedIn platform rules

A style card may come from another surface (a Telegram/newsletter voice, say) and carry mechanics that
break LinkedIn's structural rules — emoji section headers, a binary emoji-vote CTA, ALL-CAPS labels.
When they conflict, **the LinkedIn hard rules below win on structure; the style card wins on voice.**
Keep the card's *register and rhetorical moves* (e.g., skeptical authority, specificity-as-authority,
humor-as-vaccine, contrarian-from-within); drop the *platform-breaking mechanics* (cap emoji at 1,
convert an emoji-vote into a specific open question). When you make this trade, say so in one line so
the user knows why their card wasn't copied literally.

## The drafting rules (embedded — mirrors `linkedin-post-reviewer`)

> These are the same hard rules `linkedin-post-reviewer` enforces, embedded here so a draft is written
> to pass review on the first try. **If the reviewer's checklist changes, update this block too** — the
> two are intentionally kept in sync.

**Hook (line 1-2):**
- 8-10 words. Hard cap. If it runs to 11+, cut it.
- Two main keywords that define the angle.
- Frame it as "how I" or a specific number — not "how to" (anyone can write "how to"; only you can
  write "how I").
- Statement + curiosity gap: tell enough to intrigue, not enough to satisfy.
- Rehook on line 2, below the "see more" cutoff, so the expand is earned.

**Body:**
- F-pattern. Short lines, ascending/descending list rhythm, ≤3 consecutive lines on mobile.
- One idea per block. One-liners ≤8-10 words.
- Write for a no-context reader: explain it like a smart friend with zero context. No jargon a reader
  would have to look up; layman framing first, depth later.
- No italics. No hashtags. **Max one emoji (zero is safer).**
- No outbound links in the body — first comment only.

**Ending + CTA:**
- Power-ending: the last line closes the loop the hook opened.
- CTA is a **specific open question** tied to the post's argument — never "Agree?" / "Thoughts?",
  never an emoji-only vote.

**Length:** a tight LinkedIn post, not an essay. Most land between ~120 and ~250 words.

## Producing 2-3 variants

Generate **2-3 variants of the same post that differ on hook and angle**, not reworded twins. Pick the
axes from the material — common ones:

- **Data-led** — open on the most surprising number from the enrichment/talking point.
- **Story-led** — open in a scene or a named person's moment, pay it off as the lesson.
- **Contrarian take** — open by naming the consensus, then break it with evidence.

If the chosen talking point already has a category (Educational / Spicy Take / Data Nugget / Story
Spark), let that suggest one variant and contrast it with a second angle so the user has a real choice.
Each variant is a *complete* post — hook, body, ending, CTA — not a fragment.

## Workflow

### Step 1 — Gather inputs
Resolve the core material (Option A/B/C), then load enrichment, audience profile, and style card per
the Inputs section. Identify the **single core argument**, the **proof** to weave in, and the **voice**.

### Step 2 — Draft 2-3 variants
Write each variant to the embedded rules, carrying the proof and the voice. Vary the hook/angle per
variant. Pull stories/quotes/stats only from enrichment or the talking point — do not invent proof.

### Step 3 — Self-check (rewrite before showing)
Run the embedded rules over **every variant** and fix any failure before presenting:
- [ ] Hook 8-10 words, two keywords, "how I"/number frame, curiosity gap, rehook on line 2?
- [ ] Body F-pattern, ≤3 mobile lines, no italics, no hashtags, ≤1 emoji, no body links?
- [ ] Power-ending closes the hook's loop? CTA is a specific open question (not "Agree?", not emoji vote)?
- [ ] Voice matches the style card (within platform rules)? Vocabulary matches the audience profile?
- [ ] Every stat/quote/example traces to enrichment or the talking point — nothing fabricated?

If any check fails, rewrite that variant. Do not present a draft that breaks a hard rule.

### Step 4 — Output and hand off
Save both formats (next section) and offer the reviewer handoff.

## Output

Save both markdown and HTML versions:

```bash
mkdir -p content-workspace/content/drafts
```

**Filenames** (use today's date and a short topic slug):
- `content-workspace/content/drafts/draft-YYYY-MM-DD-[slug].md`
- `content-workspace/content/drafts/draft-YYYY-MM-DD-[slug].html`

(Saved under `content/drafts/`, **not** `profiles/`, so the profile-scanning skills never mistake a
draft for an audience profile or style card.)

Read `draft-template.md` in this skill's directory for the exact markdown structure, and
`html-draft-guide.md` for the HTML styling requirements.

**Markdown output shape:**

```markdown
# LinkedIn Post Drafts — [Topic]
## Core argument: [one sentence]
## Audience: [profile name or description]
## Style: [style card name, or "neutral LinkedIn voice"]
## Proof source: [enrichment file / talking-point file, or "none — see post-enricher"]

---

### Variant 1 — [angle label, e.g. "Data-led"]

[Full post: hook line, rehook line, body in F-pattern, power-ending, specific-question CTA.]

**Why this angle:** [one line]
**First-comment link (optional):** [if the post references a source worth linking]

---

### Variant 2 — [angle label]

[Full post]

**Why this angle:** [one line]

---

### Variant 3 — [angle label]   (optional third)

[Full post]

**Why this angle:** [one line]
```

After saving, present the drafts and offer next steps (the user launches the next step — nothing
auto-runs):

```
Done — 3 LinkedIn drafts saved.

  content-workspace/content/drafts/draft-YYYY-MM-DD-[slug].md (+ .html)

Want to:
  1. Review a variant — run `linkedin-post-reviewer` on it (e.g. point it at the .md file or paste a variant)
  2. Tighten one variant — tell me which and what to change
  3. Generate another angle
  4. Done for now
```

If they pick 1, name the file path (or the chosen variant text) so they can hand it to
`linkedin-post-reviewer` — this skill does not invoke the reviewer itself.

## Edge Cases

- **No talking points and no pasted idea:** Ask for one — a topic, a point, or a few lines. Don't
  invent an argument from nothing.
- **No enrichment found:** Draft from the talking point's own proof lines; note the post would be
  stronger with `post-enricher` and offer to proceed anyway.
- **No style card:** Use a neutral, strong LinkedIn voice and say the draft isn't voice-matched yet.
- **No audience profile:** Ask "who is this for?" once; if the user declines, write to a generalist
  professional reader and note the assumption.
- **Style card conflicts with LinkedIn rules:** Apply the reconciliation rule — voice from the card,
  structure from the platform — and state the trade in one line.
- **User asks for one post, not variants:** Produce one strong draft; mention you can spin alternate
  angles if they want.
- **User asks to write a blog post / newsletter / ad / tweet:** Decline — "This skill is scoped to
  LinkedIn drafts." Point them to the relevant tool if one exists.
- **Proof in enrichment looks fabricated or unsourced:** Don't use it. Flag it and suggest re-running
  `post-enricher` to verify, or drafting without that claim.

## What This Skill Never Does

- Never extracts talking points from source material — that's `talking-point-extractor`.
- Never researches or adds new proof — that's `post-enricher`. It composes from what already exists.
- Never reviews or critiques a finished draft — that's `linkedin-post-reviewer`.
- Never writes non-LinkedIn copy (blogs, newsletters, ads, email).
- Never invents stats, quotes, or case studies. Unsourced proof is dropped, not shipped.
- Never auto-runs another skill. It saves drafts and offers the next step; the user launches it.

## File Structure

```
.claude/skills/linkedin-post-writer/
├── SKILL.md                ← you are here
├── draft-template.md       ← markdown output format (the 2-3 variants block)
└── html-draft-guide.md     ← HTML styling for the .html output

content-workspace/
├── talking-points/         ← input: post-ready points (read)
├── content/
│   ├── enrichments/        ← input: story/case-study/quote with sources (read)
│   └── drafts/             ← this skill's output (.md + .html)
└── profiles/               ← input: audience profile (*profile*) + style card (*style*) (read)
```

## API Integration Summary

| Need | How |
|---|---|
| **Web research** | Not used. This skill composes from talking points + enrichment already in `content-workspace/`. Proof comes from `post-enricher`, which did the verified research upstream. |

This skill performs **no live research**. If a future tweak ever needs a freshness check, it must use
the built-in `WebSearch`/`WebFetch` tools and verify each cited claim on its own source page — do NOT
create alternative research scripts. Fabricated or unsourced proof is dropped, never shipped.
