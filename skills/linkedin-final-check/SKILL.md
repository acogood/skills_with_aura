---
name: linkedin-final-check
description: "Final pre-publish gate for ONE chosen LinkedIn post. Re-reads the single draft you're about to post and returns a SHIP / HOLD / UNVERIFIED verdict with a specific blocker list, confirming the post is free of AI-writing tells (dash pile-ups, curly quotes, one reframe carrying the whole post, forced triads, ceremony, aphorism formulas) and clears the practical publish blockers (leftover template scaffolding, literal ** formatting, unfilled placeholders, claims it can't trace). Use when the user has picked a final variant and asks 'is this ready to publish', 'final check before I post', 'does this sound AI', 'is this free of AI slop', 'give it a last look', or 'publish-ready?'. Not for critiquing, comparing, coaching, or rewriting drafts/hooks/a weekly batch (that's linkedin-post-reviewer), not for drafting or re-angling a post (that's linkedin-post-writer), and not for non-LinkedIn copy."
argument-hint: <the final chosen post — a draft file path (+ which variant), or pasted text>
---

# LinkedIn Final Check

> **Works standalone.** Point it at the one draft you're about to publish, or paste the post in. It reads
> that single post, runs two gates, and returns a ship/hold verdict in the conversation. It doesn't use
> `content-workspace/` beyond reading the draft file you name. Nothing launches automatically.

## What this is (and what it is not)

This is the **last stop before you hit Post**. You've already drafted (`linkedin-post-writer`) and maybe
critiqued variants (`linkedin-post-reviewer`); you've picked the one you're going to publish. This skill
re-reads *that one post* and answers a single question: **is it ready to publish and free of AI slop?**

It is a **gate, not a coach.** It returns a binary verdict plus the exact blockers, not a menu of
alternative angles. If you want variant-by-variant critique, rewrites, hook coaching, or a strategic call
("should I post this at all?"), that's `linkedin-post-reviewer`. If you want to change the post's argument
or structure, that's `linkedin-post-writer`.

```
linkedin-post-writer → linkedin-post-reviewer → linkedin-final-check (you are here) → publish
```

## Input — the one post you're about to publish

Resolve to a single post body:
- **A drafts file with variants.** Read it. If it holds multiple variants, ask which one the user chose
  (or use the variant they name). Check **only that variant**. Note the file's `Proof source` / enrichment
  reference if present — that is the provenance Gate B checks against.
- **A pasted post.** Check it as given. There is no provenance, so factual claims can only be flagged for
  the user to confirm, never marked verified (see Gate B).

**Isolate the publishable text.** A drafts file carries scaffolding that must NOT ship: the header block
(`Core argument`, `Audience`, `Style`, `Proof source`), the template-selection note, and each variant's
`Why this template / what it needs` and `First-comment link` lines. The post that goes to LinkedIn is the
hook-to-CTA body only. Check that body; treat the scaffolding as metadata, and flag it only if it looks
like it would get pasted into the post by mistake.

## Gate A — AI-slop scan (two tiers)

**Rendering bugs (hard blockers — they break on LinkedIn regardless of voice):**
- **Literal `**bold**` or `_italics_` in the body.** LinkedIn renders the asterisks/underscores as raw
  characters, so this is a visible formatting bug.
- **Curly quotes** (`“ ” ‘ ’`). Convert to straight (`" '`).
- **More than one emoji** (zero is safer), emoji section headers, or hashtag stuffing.

**Cadence tells (contextual — flag as patterns, weigh against the style card; a single instance is not a
blocker):**
- **Dashes as an AI pile-up.** Em/en dashes are a tell only when they become the default connector in an
  even, machine-ish rhythm. They are not slop on their own — if the post's style card names dashes as a
  device (many voices use them), keep the ones that serve a genuine aside and flag only the mechanical
  pile-up.
- **One reframe carrying the post.** The antithesis move ("not X, it's Y" / "you can't A, you can B")
  reworded three, four, five times reads as machine-written. Once or twice is a sharp move.
- **Forced rule-of-three** where the third item is filler.
- **A run of clipped one-line fragments** long enough to read as engineered drama, not emphasis.
- **Ceremony / signposting / aphorism formulas** — "the real question is", "at its core", "here's the
  thing", "let's dive in", "X is the currency of Y", "X is a testament to".
- **Filler / hedging** — "in order to", "it's important to note that", stacked qualifiers.
- **Vague attribution** — "studies show", "experts agree" with no named source.

## Gate B — publish-readiness

**True publish blockers (a HOLD):**
- [ ] **No leftover scaffolding** in the publishable text — no `Why this template` note, no template label,
      no header metadata pasted into the post.
- [ ] **No unfilled placeholders** — no `[slug]`, `[topic]`, `[name]`, `TODO`, or worked-example wording
      left in from a template.
- [ ] **No rendering bug** from Gate A (literal `**`/`_`, curly quotes, emoji/hashtag spam).
- [ ] **Claims are traceable.** Verify each stat/quote/example against the draft's stated provenance (its
      `Proof source` / enrichment). A claim that contradicts the provenance is a HOLD. A claim with no
      provenance to check against is **UNVERIFIED**, not SHIP (see verdict). This skill does not itself do
      web research; it checks the post against the material it was given.

**Performance heuristics (note them, do not block on them):** these come from `linkedin-post-writer` /
`linkedin-post-reviewer` and shape reach, but a post can be publishable without a perfect score. Mention
any that are off so the user can choose, and say plainly that they are not ship-stoppers:
- Hook 8–10 words with a "how I"/number frame and a curiosity gap; rehook on line 2.
- F-pattern body, ≤3 consecutive mobile lines.
- Power-ending that closes the hook's loop; a specific-open-question CTA.
- Roughly 120–250 words.
- First-comment link named if the post references a source (the writer treats this as optional; surface it,
  don't require it).

## What is NOT slop (do not flag — this protects the voice)

This gate removes machine tells; it does **not** neutralize a real voice. When in doubt, keep the human
choice.
- **One or two short emphatic lines.** Native LinkedIn rhythm, not staccato drama.
- **A single sharp reframe.** The antithesis move is a tool; only its *repetition* is the tell.
- **Dashes named by the style card.** If the card lists dashes as signature punctuation, they are voice,
  not slop — only an AI-cadence pile-up is.
- **A deliberate register** — skeptical authority, contrarian-from-within, numbers-as-authority, dry humor.
- **Specific numbers, named people, real sources, odd concrete detail.** Human signals. Preserve them.
- **Fancy-but-correct words** ("leverage", "unlock", "transform", "ostensibly"). Not slop on their own.
  This gate flags *patterns*, never a word list.

## Verdict

Lead with the verdict, then the blockers, then the offer.

- **SHIP** — clears both gates, and every factual claim is either traceable to the provenance or contains
  none. Say "Ship it," name the one or two things that make it land, and stop. Don't manufacture problems.
- **HOLD** — one or more blockers (a rendering bug, leftover scaffolding, a placeholder, a claim that
  contradicts its provenance, or a cadence pile-up bad enough to read as machine-written). List each as:
  the exact line, what's wrong (named tell or rule), and the concrete fix. Rendering bugs first (fast,
  non-negotiable), then cadence, then readiness.
- **UNVERIFIED** — the post is otherwise clean but carries a factual claim (stat, named study, quote) that
  you cannot trace to any provided provenance. Name the claim(s) and tell the user exactly what to confirm
  before posting. Do not upgrade to SHIP on the user's behalf.

**Output shape:**

```markdown
**Verdict: SHIP**   (or **HOLD — N blockers**, or **UNVERIFIED — N claims to confirm**)

{One or two sentences: why. For SHIP, the two things that work. For HOLD/UNVERIFIED, the headline problem.}

## Blockers   (omit if SHIP)
1. **{tell or rule}** — line: "{quoted text}" → {the fix}.
2. ...

## Confirm before posting   (UNVERIFIED only)
- "{quoted claim}" — no provenance in the draft; verify the source or cut it.

## Nice-to-have   (optional, non-blocking performance heuristics)
- {e.g. hook is 12 words; tightening to 9 would lift reach — your call}
```

After a HOLD, offer to apply the **rendering-bug** fixes (curly quotes, stray `**`/`_`) yourself, since
those are safe and voice-neutral. Leave cadence and structural rewrites to the user or
`linkedin-post-writer` unless they ask you to do them.

## Self-check before sending
- Did you check only the **publishable body**, not the scaffolding?
- Is every blocker a real rendering bug, a real tell (weighed against the style card), or an untraceable
  claim — not a personal-taste nit or a performance heuristic dressed as a blocker?
- Did you resist marking a claim "verified" when you only had the post's body to go on?
- Does your own verdict avoid the peeves it polices (no "Agree?" energy, no manufactured positivity)?

## Edge Cases
- **Multiple variants, none named.** Ask which one they're publishing. Don't check all three — this is a
  single-post gate.
- **Draft still has open template placeholders.** Automatic HOLD — it isn't a finished post yet; point back
  to `linkedin-post-writer`.
- **Pasted post, no provenance, carries hard stats.** UNVERIFIED, not HOLD and not SHIP — the numbers may
  be fine, but you can't confirm them from body text. Say what to check.
- **Post is clean and fully traceable.** Give the SHIP verdict (short). A gate that only ever finds problems
  is broken.
- **User wants a full critique, rewrites, alternate angles, or a strategic "should I post this?".** That's
  `linkedin-post-reviewer` or `linkedin-post-writer` — say so and hand off.
- **Non-LinkedIn copy.** Decline — "This gate is scoped to LinkedIn posts."

## What This Skill Never Does
- Never drafts or re-angles a post — that's `linkedin-post-writer`.
- Never runs a multi-variant, hook-coaching, or weekly critique with rewrites — that's
  `linkedin-post-reviewer`.
- Never invents or "fixes" proof, and never marks an untraceable claim verified. It returns UNVERIFIED.
- Never flags a banned-word list or neutralizes a deliberate voice — it removes machine *patterns* only,
  and defers to the style card.
- Never auto-runs another skill.

## Keeping in sync
The AI-slop list here is the same two-tier list the writer avoids (`linkedin-post-writer`) and the reviewer
flags (`linkedin-post-reviewer`) — rendering bugs as hard fails, cadence tells as style-aware patterns. It
is duplicated on purpose so each skill stays self-contained; if one changes, update all three.
