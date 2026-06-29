# Eval: Research backends (Perplexity MCP vs. built-in WebSearch)

> **Outcome (2026-06-29): Perplexity was dropped from the skills.** Two blind runs of this harness on
> drafting LinkedIn posts went to the built-in `WebSearch`/`WebFetch` arm (21–18, then 22–17). The
> decisive, repeatable signal was verifiability: Perplexity returned confident, citation-shaped claims
> that didn't survive a page check (a citation whose page didn't contain the claim; fabricated case
> studies with crisp fake percentages), while the built-in "fetch the page and read it" step *is* the
> verification. The content skills now describe a **single built-in path** and name no MCP; the lone
> "you *may* connect a Perplexity MCP to discover candidates faster, but verify each claim on its
> page" note lives in `CLAUDE.md` only. This harness is **kept, not deleted** — re-run it (Arm A vs.
> Arm B) to re-test the comparison if you connect a Perplexity MCP.

A **reusable, rerunnable** protocol for comparing the two research backends weighed for the content
skills — **Arm A: Perplexity MCP** vs. **Arm B: built-in `WebSearch`/`WebFetch` fallback** — by their
downstream effect on a drafted LinkedIn post.

You give it one **topic** and a **profile + style card**; it runs the same research-then-draft flow
twice (once per backend), saves both arms' raw research **and** drafted post, then scores them side
by side against the rubric below. Same protocol works for any topic with no edits — just change the
topic.

> **Why two arms, run this way.** This compares the dropped MCP backend against the contract the
> skills now ship (see each skill's *API Integration Summary* and `CLAUDE.md` → *Built-in web
> research*). The MCP can't be
> uninstalled mid-session, so **Arm B is run by instructing yourself to ignore the MCP** and use only
> the built-in web tools — that faithfully simulates a no-MCP environment.

---

## Inputs (collect before starting)

1. **Topic / angle** — the subject of the LinkedIn post (e.g. "why most RAG demos fail in
   production"). One line.
2. **Audience profile** — a `content-workspace/profiles/*profile*.md` file. If none exists, build one
   first with `content-audience-profiler` (the eval is about *your* voice, so this matters).
3. **Writing style card** — a `content-workspace/profiles/*style*.md` file. If none exists, build one
   first with `writing-style-analyzer`.
4. *(Optional)* **Research skill under test** — default is a direct research-then-draft pass (below).
   You can instead route the research step through `post-enricher` (proof for a talking point) or
   `lookalike-content` (trending-topic research); the arms and rubric are identical either way.

If the profile or style card is missing, **stop and build them first** — a fair voice-fit score
depends on them.

---

## Setup

Pick a run slug and create the run folder under the gitignored workspace (never commit run outputs):

```bash
RUN="$(date +%Y-%m-%d)-<topic-slug>"        # e.g. 2026-06-29-rag-demos-fail
mkdir -p "content-workspace/eval-runs/research-backends/$RUN"
```

Read the audience profile and style card once, up front — **both arms draft against the same
profile + style card** so the only variable is the research backend.

---

## Isolation — run each arm blind (recommended)

The cleanest run gives **each arm its own fresh subagent** (Agent tool) that:
- knows nothing about the other arm, the comparison, or any prior run (no shared context → no
  knowledge leak), and
- is locked to one backend — Arm A: Perplexity MCP only; Arm B: `WebSearch`/`WebFetch` only, with
  the MCP declared unavailable.

Have each subagent **execute the real enrichment skill** (`post-enricher`) — read its `SKILL.md` and
follow it — rather than improvising research, so you're testing the skill+backend, not an ad-hoc
procedure. The orchestrator then only scores the sealed outputs and runs the spot-checks.

Why this matters: if one agent runs both arms back-to-back, Arm A's findings (and gaps — e.g. "the
MCP couldn't find a quote") leak into how hard you search in Arm B, even with independent queries.
Blind subagents remove that. After both return, **independently re-open one cited URL per arm
yourself** — don't trust an arm's own "verified" label. (Running both arms in one context still
works as a quick-look; label it the weaker method.)

---

## Arm A — Perplexity MCP

1. **Research the topic.** Use the Perplexity MCP (`perplexity_ask`, or `perplexity_search` +
   `perplexity_research` for depth). Gather, for the topic:
   - 1-2 recent, verifiable **case studies / examples** (named company or person, a real number or
     outcome, ideally last 24 months),
   - 1-2 supporting **stats or facts**, and
   - optionally 1 **authority quote** (correctly attributed).
   Keep every source URL and its publish date.
2. **Save the raw research** verbatim (the answer text + the list of cited URLs with publish dates)
   to `…/$RUN/arm-a-research.md`.
3. **Draft the LinkedIn post.** Using the audience profile + style card, write one post on the topic
   that weaves in the proof from step 1. Match the style card's hook pattern, length, and voice.
   Save to `…/$RUN/arm-a-post.md`.
4. **Note practicals** as you go: rough latency, whether anything failed or degraded, friction.

## Arm B — built-in WebSearch fallback (ignore the MCP)

> **Hard rule for this arm:** do **not** call any `perplexity_*` MCP tool. Use only `WebSearch` and
> `WebFetch`. This is the no-MCP path the skills fall back to.

1. **Research the topic** with the fallback mini-procedure: `WebSearch` for the same things (case
   study, stats, quote) → `WebFetch` the top 1-3 results for each query to read them in full →
   synthesize. Record the real source URLs **with an access date** (today). Hold the same bar as
   Arm A: recent, specific, verifiable.
2. **Save the raw research** verbatim to `…/$RUN/arm-b-research.md` (synthesized findings + the URLs
   you actually fetched, with access dates).
3. **Draft the LinkedIn post** from Arm B's research only, using the *same* audience profile + style
   card. Save to `…/$RUN/arm-b-post.md`.
4. **Note practicals**: rough latency, fetch failures (paywalls, blocked pages like LinkedIn), how
   gracefully it degraded.

> Keep the arms independent: don't let Arm A's findings leak into Arm B's draft. Research each arm
> from scratch.

---

## Scoring rubric

Score **each arm** 1-5 on every dimension (5 = best). Judge research dimensions against the *raw
research* file; judge post quality against the *drafted post*.

| # | Dimension | What a 5 looks like | What a 1 looks like |
|---|---|---|---|
| 1 | **Recency** | Evidence is current (much within the last few months; nothing older than ~24 months unless evergreen) | Stale or undated; can't tell when it's from |
| 2 | **Specificity** | Named companies/people, real numbers, concrete outcomes | Vague, generic ("a company improved results") |
| 3 | **Source verifiability** | Every claim ties to a citable URL you can open; access/publish dates present | Unsourced assertions; dead, invented, or missing links |
| 4 | **Post quality / voice-fit** | Reads like the style card's voice for this audience; strong hook, right length, proof lands naturally | Off-voice, generic, weak hook, or proof bolted on |
| 5 | **Practical** | Fast, no failures, degraded gracefully when a source was unavailable | Slow, errored, or stalled on blocked/paywalled pages |

**Verifiability is the integrity gate.** Before scoring 4-5 on dimensions 1-3 for *either* arm,
spot-check 1-2 cited URLs actually open and say what the research claims. A confident but unsourced
or broken citation caps verifiability at 2 — note it.

### Verdict

- **Total** each arm (out of 25) and name the **winner per dimension**.
- Write a 2-3 sentence **verdict**: which backend produced the better-supported, better-voiced post
  for this topic, and the main trade-off (e.g. "MCP was faster and better-cited; WebSearch matched
  on specifics but spent latency on fetches and hit a paywall").
- Add a **recommendation**: when is the fallback good enough, and where does it visibly lose? Feed
  recurring gaps back into the skills' fallback mini-procedure.

---

## Record the result

Fill in `result-template.md` (copy it into the run folder) and save as
`…/$RUN/result.md`. That file is the deliverable — both drafted posts plus the side-by-side scores
and verdict.

```bash
cp eval/research-backends/result-template.md "content-workspace/eval-runs/research-backends/$RUN/result.md"
# then fill it in
```

## Rerunning

Run again on a **new topic** by repeating from *Setup* with a new `RUN` slug — no edits to this
harness or the template. To compare backends across topics, keep each run in its own folder and read
the verdicts together.
