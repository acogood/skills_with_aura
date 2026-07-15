---
name: talking-point-curator
description: "Select and rank the talking points that fit a defined content strategy or topic cluster from talking-point-extractor's output, producing a prioritized post queue (a reason, a reach score, and a swing/filler role per pick) to hand to post-enricher or linkedin-post-writer. Use when the user has one or more extracted talking-point files and wants to decide WHICH points to actually post for a specific lane, angle, or topic cluster — e.g. 'curate my talking points', 'pick the best talking points for my AI-and-work lane', 'which of these fit my cluster', 'build my post queue', 'narrow these down'. Not for extracting talking points from a source (that's talking-point-extractor), not for adding stories/quotes/stats to a point (post-enricher), not for drafting the finished post (linkedin-post-writer), and not for reviewing a finished draft (linkedin-post-reviewer)."
argument-hint: <topic cluster / strategy, or path to a strategy file>
---

# Talking-Point Curator

> **Works standalone.** Run this skill on its own. It reads and writes under `content-workspace/` and
> uses anything useful already there (extracted points in `content-workspace/talking-points/`, a saved
> content strategy in `content-workspace/profiles/`, an audience profile) — otherwise it asks you or
> proceeds without it. The other content skills share this same workspace; see the project README for
> the full set. Nothing launches automatically.

## Overview

`talking-point-extractor` produces *more* points than you should post. This skill is the **selection**
step that turns that pile into a ranked queue: it reads every extracted talking point, scores each one
against a defined content strategy (topic cluster + angle + who it's for + what you're optimising for),
and outputs the shortlist worth drafting — each with a reason, a reach score, and a suggested role
(swing vs. filler). It sits between extraction and drafting:

```
talking-point-extractor → talking-point-curator (you are here) → post-enricher → linkedin-post-writer → linkedin-post-reviewer
```

It **selects and ranks only** — it never invents a talking point, rewrites a hook, or fabricates a
number. If the material is thin for the cluster, it says so instead of padding the queue.

## Arguments

`$ARGUMENTS` — the topic cluster / lane to curate for (e.g. "my AI-and-work spicy-take lane"), or a
path to a saved strategy file. Optional; if absent, the skill looks for a saved strategy, then asks.

## When to Use This Skill

Use it when:
- The user has extracted talking points and wants to pick which ones to post for a specific angle.
- The user names a lane, cluster, or theme and wants the best-fitting points surfaced.
- The user asks to "curate", "narrow down", "shortlist", "prioritise", or "build a post queue".
- Talking points span several sources/topics and the user wants only those on-strategy.

**Not for** extracting points from a source (`talking-point-extractor`), adding proof
(`post-enricher`), drafting the post (`linkedin-post-writer`), or reviewing a draft
(`linkedin-post-reviewer`).

## Inputs

### 1. Extracted talking points (required)

Scan `content-workspace/talking-points/` for `.md` files (extractor output — names start with
`talking-points-` or `viral-talking-points-`). Read every file the strategy could touch; each `###`
block under a category (Educational / Spicy Take / Data Nugget / Story Spark) is one candidate.

If the folder is empty, stop and tell the user to run `talking-point-extractor` first — this skill
selects from existing points, it does not create them.

### 2. Content strategy (defines the cluster)

Resolve the strategy in this order:

1. **A saved strategy file.** Scan `content-workspace/profiles/` for `.md` files with **"strategy"** or
   **"cluster"** in the filename. If one exists, read it — it defines the topic cluster(s), preferred
   angle/buckets, audience, what to optimise for, and any sacred cows to attack or non-goals to avoid.
   (These filenames omit "profile"/"style", so the profile-scanning skills never mistake a strategy for
   an audience profile or style card.)
2. **The invoking prompt / `$ARGUMENTS`.** If the user described the cluster inline, use that.
3. **Ask.** If neither exists, ask three short questions before scoring:
   - What topics/themes belong in this cluster? (2–5 keywords)
   - Who is it for, and what do they care about?
   - What are you optimising for — reach/virality, or authority with a specific audience — and any
     format bias (e.g. lead with spicy/contrarian, deprioritise how-to)?
   Then offer to **save it** as `content-workspace/profiles/content-strategy-<slug>.md` so future runs
   skip the questions.

### 3. Audience profile (optional)

If the strategy doesn't name an audience and a profile exists in `content-workspace/profiles/` (`.md`
with "profile" in the name), read it for the audience-resonance axis. Otherwise proceed without it.

## The selection rubric

Score every candidate talking point against the resolved strategy on these axes. Cluster fit is a hard
filter; the rest set the rank.

1. **Cluster fit (hard filter).** Is the point inside the strategy's topic cluster(s)? Drop
   clearly-out-of-cluster points — list them under "left out" so nothing vanishes silently.
2. **Angle / bucket fit.** Does the point's category match the strategy's preferred buckets? (A
   reach-first lane weights **Spicy Take** and counterintuitive **Data Nugget** up, and **Educational**
   / **Story Spark** down to filler; an authority-first lane may weight differently.) Category informs
   the score; it never hard-maps.
3. **Reach potential.** Score the built-in virality signals in the point:
   - A hook that **challenges** a consensus or makes a bold claim (stops the scroll, invites a fight).
   - A high-arousal **Emotion Tag** — Surprise / Urgency rank above Curiosity, which ranks above
     Validation / Relief.
   - A concrete, **surprising number** stated first.
   - **Borrowed authority**: a named source in the `Source` field (a person, company, or study) the post
     can newsjack — the no-name's shortcut to credibility.
   - "Makes some uncomfortable, wins fans on the other side" — a clear us/them or sacred-cow target.
4. **Audience resonance.** Does it hit the strategy audience's real stakes (money, status, career, fear,
   time), not just an interesting idea?
5. **Goal alignment (tiebreaker).** If the strategy names an underlying goal (e.g. "signal AI-growth
   competence to people who hire"), prefer points that advance it when reach is otherwise equal.

Then **de-duplicate**: when two points make near-identical arguments (common across sources), keep the
stronger one and note the merge. Spread the queue across sub-topics so it doesn't repeat one beat.

## Workflow

1. **Load inputs** — read the talking-points files and resolve the strategy (saved file → prompt → ask).
2. **Score & rank** — run the rubric over every candidate. Apply the cluster hard-filter, score the rest,
   de-duplicate, and rank.
3. **Assign roles** — tag the top points as **swing** (high reach potential — the daily bet) or
   **filler** (on-cluster but lower-arousal — variety/credibility between swings).
4. **Write the queue** — output the shortlist (default top ~12, or a week's worth; never a silent cap —
   state how many were considered and how many dropped).
5. **Hand off** — tell the user they can feed a queued point to `post-enricher` (to add proof) or
   `linkedin-post-writer` (to draft). This skill does not invoke them.

## Output format

Get today's date (YYYY-MM-DD) and a slug from the cluster name, then write to
`content-workspace/content/post-queue-<cluster-slug>-<YYYY-MM-DD>.md`. (Under `content/`, **not**
`talking-points/`, so the extractor's output and this selection never get confused; **not** under
`profiles/`, so the profile scanners ignore it.)

```markdown
# Post Queue: [Cluster name]
## Strategy: [saved file name, or "defined inline this session"]
## Optimising for: [reach / authority / …] · Audience: [who]
## Considered: [N points across M files] · Queued: [K] · Dropped: [N−K] (see "Left out")
---

## Swing posts (high reach potential — your daily bet)

### 1. [Hook — verbatim from the talking point]
- **Category:** [Educational / Spicy Take / Data Nugget / Story Spark]
- **From:** `talking-points-<slug>-<date>.md` → "[section title]"
- **Borrow authority:** [named source to newsjack, or "none — stands alone"]
- **Why it fits:** [one line — which rubric signals it scored on]
- **Reach score:** [High / Medium] · **Emotion:** [tag]

[repeat, ranked]

## Filler posts (on-cluster, lower arousal — variety between swings)

### [Hook]
- [same fields]

## Left out (out of cluster or merged — nothing dropped silently)

- "[hook]" — [reason: out of cluster / merged into #N / low reach]
```

After saving, summarise in chat: how many points were considered vs. queued, which sources were
strongest for this cluster, any gaps ("no strong Data Nuggets on-cluster — the sources were light on
numbers"), and the handoff:

```
Queue saved → content-workspace/content/post-queue-<slug>-<date>.md

Next:
  1. Enrich a swing point — run post-enricher on it
  2. Draft a swing point — run linkedin-post-writer on it
  3. Re-curate for a different cluster
  4. Done
```

## Edge Cases

- **No talking-points files:** Stop; tell the user to run `talking-point-extractor` first. Don't invent
  points.
- **No strategy and user won't define one:** Curate for a generic "broad professional reach" cluster
  (weight Spicy Takes and surprising numbers up), and flag that a saved strategy would sharpen the pick.
- **Few points survive the cluster filter:** Return the honest short queue and say the sources are thin
  for this cluster — suggest extracting from more on-topic sources rather than padding with off-cluster
  points.
- **Many near-duplicates:** Keep the strongest of each, note the merges, and tell the user the raw pile
  was repetitive.
- **User wants a different cluster from the saved one:** Use the inline cluster for this run; offer to
  save it as a second strategy file.

## What This Skill Never Does

- Never extracts talking points from a source — that's `talking-point-extractor`.
- Never adds or researches proof — that's `post-enricher`.
- Never drafts or rewrites a post — that's `linkedin-post-writer`.
- Never reviews a finished draft — that's `linkedin-post-reviewer`.
- Never invents a talking point, rewrites a hook, or fabricates a number. It selects and ranks only.
- Never auto-runs another skill. It saves the queue and offers the next step; the user launches it.

## File Structure

```
skills/talking-point-curator/
└── SKILL.md                ← you are here

content-workspace/
├── talking-points/         ← input: extracted points, all categories (read)
├── profiles/               ← input: content strategy (*strategy* / *cluster*) + optional audience profile (read)
└── content/
    └── post-queue-*.md     ← this skill's output (the ranked queue)
```

## API Integration Summary

| Need | How |
|---|---|
| **Web research** | Not used. This skill selects from talking points already in `content-workspace/`. Any research happened upstream in `talking-point-extractor` / `post-enricher`. |

This skill performs **no live research**. If a future tweak ever needs one, it must use the built-in
`WebSearch`/`WebFetch` tools and verify each cited claim on its own source page — do NOT create
alternative research scripts. It never fabricates or edits talking points; it only ranks what exists.
