# Post Template Library

A library of **proven post structures** — whole-post beat sequences, not hook/angle reskins. The
writer reads this file, scores each template on intent fit, gates it on whether the available proof can
honestly fill its beats, and writes one complete post per qualifying template. See `SKILL.md`
("Selecting templates") for how selection and the proof-fit gate work.

These are **structures, de-identified to rhetorical patterns**. No creator names, no real posts. Each
worked example below is a freshly-written generic illustration of the beats — not a source post, not
something to copy. The point is the *shape*; the words are filled per-user from real material.

---

## Template schema

Every template carries the same six fields:

| Field | What it holds |
|---|---|
| **Name** | The rhetorical-pattern name (de-identified — describes the move, not a person). |
| **Best for** | The intent signals that make this template fit — what the talking point is *trying to do*. The selection score is how well the point matches these. |
| **Category affinity** | Which talking-point categories (Educational / Spicy Take / Data Nugget / Story Spark) this pattern leans toward. Used to nudge the score and **break ties** — never to hard-map a category to a template. |
| **Proof requirements** | A checklist of what the talking point + enrichment **must** supply. This is the **gate**: if any required item is missing and can't be filled honestly from the material, the template is **disqualified** — never filled with invented proof. |
| **Beats** | The ordered structural sequence. A template-based draft must hit these beats, in order, in the user's genuine voice. |
| **Worked example** | One invented, generic post that walks the beats, with a beat map. Illustration only. |

### How the proof gate reads

A template **qualifies** only when every line in its proof-requirements checklist can be satisfied
from the real material (talking point + enrichment + profile/style). If a required beat would have to be
filled with a made-up number, a fabricated result, or a quote nobody said, the template is
**disqualified** — it does not get written. This is what keeps templates as scaffolds rather than
mad-libs, and it preserves the writer's never-invent-proof promise.

### Beats yield to the LinkedIn hard rules

A beat is a *structural intent*, not a literal instruction. Where a beat collides with a LinkedIn hard
rule from `SKILL.md` (for example, a soft-sell beat vs. the specific-open-question CTA rule), the **hard
rule wins** — convert the beat to satisfy the rule and state the trade in one line. Optional beats are
marked as such and may be dropped entirely when they fight a hard rule.

---

## Adding a template

To add a template, copy the block below and fill every field. You do **not** need to touch `SKILL.md` —
selection reads this file generically, so a well-formed entry is picked up automatically.

```markdown
## Template: [Rhetorical-pattern name]

**Best for:** [The intent signals — what the talking point is trying to do. Be specific; this is what
the score matches against.]

**Category affinity:** [Educational / Spicy Take / Data Nugget / Story Spark — primary, then secondary.
Used to nudge the score and break ties only.]

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] [What the material must contain — item 1]
- [ ] [item 2]
- [ ] [item 3]

**Beats (in order):**
1. [beat]
2. [beat]
   …

**Worked example** (invented illustration — generic, obeys the LinkedIn hard rules):

> [A complete post that walks the beats.]

Beat map: [beat 1] → "[the line]"; [beat 2] → "[the line]"; …
```

Keep the worked example **generic and freshly written** — no creator names, no real posts. Make it obey
the LinkedIn hard rules (8–10-word hook, F-pattern, no hashtags, ≤1 emoji, specific-open-question CTA)
so it doubles as a passing example.

---

## Template: Counterintuitive FAQ

**Best for:** Advice or wisdom posts that answer a recurring audience question with a contrarian answer
the writer has earned the right to give. Pick this when the point is "everyone asks me X, and my answer
surprises them," and the writer can back the surprise with first-hand experience.

**Category affinity:** Educational (primary), Spicy Take (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real, recurring question the audience actually asks (or one the writer is repeatedly asked).
- [ ] First-hand experience or a result that gives the writer authority to answer it.
- [ ] A genuine counterintuitive answer — the consensus says one thing, the writer's lived answer says
      another — grounded in that experience, not a hot take for its own sake.
- [ ] 3–5 concrete benefits the counterintuitive approach actually buys (real, not hypothetical).
- [ ] A real cost of the conventional approach (what staying the default way actually fails at).

**Beats (in order):**
1. Proof + aspirational outcome — open with the credible result the reader wants.
2. The question someone asked — the recurring question, in the audience's own words.
3. "My answer:" promise — name that an answer is coming, and that it's not the obvious one.
4. The short counterintuitive answer — the surprise, stated plainly.
5. The cost of inaction — what the conventional answer quietly costs.
6. "This is what X buys you" — a list of 3–5 concrete benefits of the counterintuitive move.
7. The stakes — the surface problem vs. the deeper failure underneath it.
8. The how — the keep-it-simple essentials, small enough to act on.
9. Reinforce the warning — restate the cost so the choice is sharp.
10. Engagement question — a specific open question tied to the argument.

**Worked example** (invented illustration — generic, obeys the LinkedIn hard rules):

> I doubled my rates and lost zero clients.
>
> Everyone told me I'd price myself out. The opposite happened.
>
> The question I get most: "How do I raise rates without scaring people off?"
>
> My answer: stop selling hours.
>
> Hours invite comparison. Outcomes don't. Price the result and the rate stops being the conversation.
>
> Keep selling time and you stay a line item — the first thing cut when budgets tighten.
>
> Pricing the outcome buys you three things:
> - Clients who argue about value, not your hourly rate
> - Projects scoped to a finish line, not an open clock
> - Room to get faster without earning less
>
> The surface problem is "my rates are too low." The real one is that nobody can see what they're buying.
>
> The fix is smaller than it sounds:
> - Name the outcome in one sentence
> - Put one number next to it
> - Delete the hourly breakdown
>
> Sell time and you'll always be negotiating it. Sell the outcome and you're negotiating the result.
>
> What's the last thing you priced by the hour that you should have priced by the outcome?

Beat map: proof + outcome → "I doubled my rates and lost zero clients."; the question → "How do I raise
rates without scaring people off?"; "my answer:" promise → "My answer: stop selling hours.";
counterintuitive answer → "Hours invite comparison. Outcomes don't."; cost of inaction → "Keep selling
time and you stay a line item…"; benefits list → the three "pricing the outcome buys you" bullets;
stakes → "The surface problem… The real one…"; the how → the three "the fix" bullets; reinforce the
warning → "Sell time and you'll always be negotiating it."; engagement question → "What's the last thing
you priced by the hour…?"

---

## Template: Old Way vs New Way

**Best for:** Contrarian or trend-naming posts where the writer has insider authority and there's a
clear before→after shift in how something is done. Pick this when the point is "the default playbook
flipped and most people haven't noticed," and the writer can name both the old way and the new way
concretely.

**Category affinity:** Spicy Take (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A clear before→after shift — both the old way and the new way are nameable, not vague vibes.
- [ ] 2–3 concrete examples of the shift across segments or cases.
- [ ] An analogous everyday behavior the reader already does (the "borrowed behavior" the new way
      mirrors).
- [ ] First-person proof that the writer has operated the new way — a result, a moment, a number.
- [ ] Insider credibility on the topic (why the writer would know the shift before others).

**Beats (in order):**
1. Insider teaser + counterintuitive claim — the flip, plus a line that signals you saw it early.
2. Old way vs new way — name what's actually first now, with 2–3 segmented examples.
3. Related everyday scenario — a borrowed behavior the reader already does, to make the new way obvious.
4. How it works today — the new funnel/process in plain steps.
5. First-person proof — the result or moment that shows the writer lives the new way.
6. Engagement question — a specific open question tied to the shift.

**Worked example** (invented illustration — generic, obeys the LinkedIn hard rules):

> Hiring stopped starting with the résumé two years ago.
>
> Most managers haven't noticed. The best ones already moved.
>
> Old way: post a role, screen résumés, interview the shortlist.
> New way: watch who's already doing the work in public, then reach out.
>
> - Engineers get found by their pull requests, not their CV
> - Marketers get hired off the threads they wrote for free
> - Designers get the DM because of the portfolio they post weekly
>
> It's the same move you already make as a customer. You don't read the menu first — you check the
> photos and the reviews. You trust shown over stated.
>
> So the work flips. The new funnel is: be visible, get pulled in, talk later.
>
> I filled my last two roles without opening a single résumé. Both came from people whose public work
> I'd watched for months.
>
> Where are you still leading with the résumé when you could be watching the work?

Beat map: insider teaser + counterintuitive claim → "Hiring stopped starting with the résumé two years
ago." + "Most managers haven't noticed. The best ones already moved."; old vs new + segmented examples →
"Old way:… New way:…" + the engineers/marketers/designers bullets; everyday scenario → "the same move
you already make as a customer… check the photos and the reviews."; how it works today → "the new funnel
is: be visible, get pulled in, talk later."; first-person proof → "I filled my last two roles without
opening a single résumé."; engagement question → "Where are you still leading with the résumé…?"

---

## Template: System Retrospective

**Best for:** Educational posts where the writer achieved a concrete result with a repeatable system and
can hand the reader the steps. Pick this when the point is "here's the exact process that got me a
result, and you can run it too," and the writer can name the steps honestly.

**Category affinity:** Educational (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A concrete past result the writer achieved with a repeatable system or process.
- [ ] A nameable first step.
- [ ] 2–3 concrete, repeatable steps that make up the system — specific, not filler.
- [ ] A real objection (usually effort or time) the writer can dismantle from experience.
- [ ] Enough specificity that the steps are genuinely the writer's, not generic advice dressed as a
      system.

**Beats (in order):**
1. Credibility + topic + concrete past result — the result up front, with the topic named.
2. First step — the smallest first move, to show it started small.
3. 2–3 numbered templated examples — the repeatable steps of the system.
4. Dismantle the effort objection — name the "I don't have time" pushback and answer it from experience.
5. Creator endorsement — the "if I had to start over…" line that vouches for the system. *(Any soft-sell
   here is optional and yields to the CTA hard rule — convert it to the engagement question.)*
6. Engagement question — a specific open question tied to the system.

**Worked example** (invented illustration — generic, obeys the LinkedIn hard rules):

> I grew a newsletter to 10,000 readers in a year.
>
> No ads, no viral post. Just one repeatable loop.
>
> The first step was the smallest: I wrote one issue and asked five people to forward it.
>
> Then I ran the same three moves every week:
> 1. Turn one reader question into the next issue
> 2. End every issue with a single, specific ask
> 3. Reply to every reply within a day
>
> "I don't have time for that" — I hear it constantly. It took me under three hours a week. The system
> did the remembering, so I didn't have to.
>
> If I had to start over tomorrow, I'd skip the fancy tools entirely and run those three moves from a
> plain inbox.
>
> What's the one repeatable move you could run every week without fail?

Beat map: credibility + result → "I grew a newsletter to 10,000 readers in a year." + "No ads, no viral
post. Just one repeatable loop."; first step → "I wrote one issue and asked five people to forward it.";
numbered examples → the three weekly moves; dismantle the objection → "'I don't have time for that'… It
took me under three hours a week."; creator endorsement → "If I had to start over tomorrow, I'd skip the
fancy tools…"; engagement question → "What's the one repeatable move you could run every week without
fail?"
