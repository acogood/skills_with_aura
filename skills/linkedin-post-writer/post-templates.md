# Post Template Library

A library of **proven post structures** — whole-post beat sequences, not hook/angle reskins. The
writer reads this file, scores each template on intent fit, gates it on whether the available proof can
honestly fill its beats, and writes one complete post per qualifying template. See `SKILL.md`
("Selecting templates") for how selection and the proof-fit gate work.

These are **structures, de-identified to rhetorical patterns**. No creator names, no real posts. Each
worked example below is a freshly-written generic illustration of the beats — and each *fill-in
template* is a placeholder skeleton — not a source post, not something to copy verbatim. The point is
the *shape*; the words are filled per-user from real material.

---

## Template schema

Every template carries the same fields:

| Field | What it holds |
|---|---|
| **Name** | The rhetorical-pattern name (de-identified — describes the move, not a person). |
| **Best for** | The intent signals that make this template fit — what the talking point is *trying to do*. The selection score is how well the point matches these. |
| **Category affinity** | Which talking-point categories (Educational / Spicy Take / Data Nugget / Story Spark) this pattern leans toward. Used to nudge the score and **break ties** — never to hard-map a category to a template. |
| **Proof requirements** | A checklist of what the talking point + enrichment **must** supply. This is the **gate**: if any required item is missing and can't be filled honestly from the material, the template is **disqualified** — never filled with invented proof. |
| **Beats** | The ordered structural sequence. A template-based draft must hit these beats, in order, in the user's genuine voice. |
| **Worked example** *or* **Fill-in template** | Either a concrete generic post that walks the beats (with a beat map), or a placeholder skeleton to fill in. Both are de-identified illustrations only. |
| **Hard-rule notes** *(optional)* | Present when a beat collides with a LinkedIn hard rule (body links, "comment X" CTAs, hashtags, >1 emoji). Names the conflict and how to reconcile it. |

### How the proof gate reads

A template **qualifies** only when every line in its proof-requirements checklist can be satisfied
from the real material (talking point + enrichment + profile/style). If a required beat would have to be
filled with a made-up number, a fabricated result, a quote nobody said, a client who doesn't exist, or a
lead magnet/event that isn't real, the template is **disqualified** — it does not get written. This is
what keeps templates as scaffolds rather than mad-libs, and it preserves the writer's never-invent-proof
promise.

### Beats yield to the LinkedIn hard rules

A beat is a *structural intent*, not a literal instruction. Where a beat collides with a LinkedIn hard
rule from `SKILL.md`, the **hard rule wins** — convert the beat to satisfy the rule and state the trade
in one line. The common reconciliations, called out per-template under **Hard-rule notes**:

- **Body link** (a "get it here / register here / check it out at [link]" line) → move the link to the
  **first comment**; the body keeps the tease, not the URL.
- **"Comment X to get it"** engagement-bait CTA → convert to a **specific open question**, and offer the
  resource via the first comment.
- **Hashtags** → drop them. **More than one emoji** → cap at one (zero is safer).
- **A hook over 10 words** (several proven openers run long) → tighten the first line to 8–10 words while
  keeping the curiosity gap.

Optional beats are marked as such and may be dropped entirely when they fight a hard rule.

> **Note on contributed templates.** Many entries below were captured from real high-performing LinkedIn
> posts and de-identified to their structural pattern (no names, no verbatim text). Several are openly
> promotional (lead-magnet, event, or service CTAs). They're kept because the *rhetorical arc* is
> valuable — the hard-rule notes and the skill's reconciliation step (R12) handle the CTA mechanics at
> drafting time.

---

## Adding a template

To add a template, copy the block below and fill every field. You do **not** need to touch `SKILL.md` —
selection reads this file generically, so a well-formed entry is picked up automatically.

```markdown
## Template: [Rhetorical-pattern name]

**Best for:** [The intent signals — what the talking point is trying to do. Be specific; this is what
the score matches against.]

**Category affinity:** [Educational / Spicy Take / Data Nugget / Story Spark — primary, then secondary.]

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] [What the material must contain — item 1]
- [ ] [item 2]

**Beats (in order):**
1. [beat]
2. [beat]

**Worked example** (or **Fill-in template**) — generic, de-identified.

**Hard-rule notes:** [only if a beat collides with a hard rule — name it and the reconciliation.]
```

Keep examples **generic and freshly written** — no creator names, no real posts. Where you give a
concrete worked example, make it obey the LinkedIn hard rules so it doubles as a passing example.

---

## Template index

| # | Template | Best-for (one line) | Category lean |
|---|---|---|---|
| 1 | Counterintuitive FAQ | Answer a recurring question with an earned contrarian answer | Educational |
| 2 | Old Way vs New Way | Name a before→after shift most people haven't noticed | Spicy Take |
| 3 | System Retrospective | Hand over the repeatable system behind a result | Educational |
| 4 | Hero & Villain Contrast | Debunk a surface signal everyone over-trusts | Spicy Take |
| 5 | Internal Dialogue Reframe | A decision that stung, then taught you something | Story Spark |
| 6 | Provocative Brand Manifesto | A bold positioning stance backed by a real result | Spicy Take |
| 7 | Mid-Conversation Recommendation | One favored tactic, what fails, what works | Educational |
| 8 | Underdog Comeback | Failure despite credentials → an unconventional fix | Story Spark |
| 9 | Underrated Tool Spotlight | Recommend a tool/method you genuinely use | Educational |
| 10 | Curated Lessons List | "X lessons from Y" with real, attributed sources | Educational |
| 11 | Results-Backed Lead Magnet | Real results → tease a real guide | Data Nugget |
| 12 | Boring-but-Profitable Framework | An unglamorous method that quietly works | Educational |
| 13 | Milestone Retrospective | A milestone + the lessons from the journey | Story Spark |
| 14 | Transformation-to-Invite | A transformation that sets up a real event | Story Spark |
| 15 | Fear-Deflation Manifesto | The feared obstacle that never materialized | Spicy Take |
| 16 | Client Process Walkthrough | A client problem solved by your process | Educational |
| 17 | Future Pacing | Paint the reader's future to motivate action now | Spicy Take |
| 18 | Two Camps Divergence | Same situation, two responses — which are you? | Spicy Take |
| 19 | Then-vs-Now Transformation | A dated before→now arc that doubles as a case study | Story Spark |
| 20 | Testimonial Spotlight | Let a real customer's words do the selling | Data Nugget |
| 21 | Permission-Granting Take | Release the reader from a limiting belief | Spicy Take |
| 22 | Identity Defense | Defend a judged choice + invite self-reflection | Story Spark |
| 23 | Rebrand Debunk | Expose hyped jargon as old fundamentals | Spicy Take |
| 24 | Stop-Start Reframe | "Stop X, start Y" with a system-vs-human reframe | Spicy Take |
| 25 | I-Was-Wrong Trend Adoption | A trend you dismissed, then rode | Story Spark |

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

---

## Template: Hero & Villain Contrast

**Best for:** Spicy, myth-busting takes that attack a *surface signal* people over-trust (a prestigious
logo, a credential, a follower count) by pairing it against the overlooked opposite. Pick this when the
point is "stop judging by X — judge by what actually matters."

**Category affinity:** Spicy Take (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real contrast you've genuinely observed (a good outcome from an unimpressive source, and a bad
      one from an impressive source).
- [ ] The superficial signal people default to — named specifically.
- [ ] The better criteria you'd judge by instead (2–3), drawn from experience.

**Beats (in order):**
1. Establish hero & villain — two mirrored lines: the bad outcome from the "impressive" source, the
   good outcome from the "unimpressive" one.
2. Name the hidden pattern — the surface signal everyone is really reacting to.
3. The overlooked opposite — the counter-case that breaks the signal.
4. Key takeaway — "don't decide based on [signal]; decide based on [criterion 1], [2], [3]."

**Fill-in template** (de-identified skeleton):

```text
I've [verb] [negative quality] [subject/role] from [impressive context].

I've [verb] [positive quality] [subject/role] from [unimpressive context].

You can be a [metaphor] and claim that [success/result] your entire [career/life].

You can also be a [positive quality] [subject/role] who made the best of [unfavourable circumstances].

Don't [make decisions] based on [the superficial signal everyone defaults to].

[Make decisions] based on [criterion 1], [criterion 2], and [criterion 3].
```

---

## Template: Internal Dialogue Reframe

**Best for:** Story-driven posts where a deliberate decision stung at first, then taught you something —
told through the raw first reaction and the corrected second thought. Pick this when the lesson lives in
a moment of vulnerability you can narrate honestly.

**Category affinity:** Story Spark (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real decision you made on purpose that initially challenged or stung you.
- [ ] The genuine raw first reaction AND the corrected second thought (both real, not invented dialogue).
- [ ] A lesson you actually drew from sitting with the discomfort.

**Beats (in order):**
1. Vulnerable admission — a decision that signals self-awareness.
2. The immediate problem — the first thing that challenged your approach.
3. More context — the inciting incident, briefly.
4. The vulnerable feeling + raw first thought (in quotes).
5. The corrected second thought — the internal turn, moments later.
6. Self-directed reframe — the discomfort is the point; if it never makes you feel this, you chose wrong.
7. Key takeaway.

**Fill-in template** (de-identified skeleton):

```text
I [made a decision that signals self-awareness].

First thing [that happened challenged your existing approach].

I'd [made that choice], on purpose, because I knew [it would lead to a desirable outcome].

[More context about the initial inciting incident].

[It] made me feel [vulnerable emotion].

First thought: "[raw reactive response]."

Second thought, about [short timeframe] later:
"[correcting phrase]. This is the exact reason you [made that decision]."

You wanted [the thing that came with the discomfort]. Now you have to actually sit in that feeling
instead of running from it.

If [decision] never makes you feel a bit [vulnerable emotion], you've [made the wrong choice].

[Key takeaway].
```

---

## Template: Provocative Brand Manifesto

**Best for:** Bold positioning posts that open by provoking the reader, name a cultural trend, then plant
a flag for how you/your brand do it differently — backed by a real result. Pick this when the point is a
stance you can defend with proof and the audience tolerates a sharp voice.

**Category affinity:** Spicy Take (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real cultural trend or status quo you're reacting to.
- [ ] A genuine positioning stance you've actually taken.
- [ ] A real result / social proof that the stance is working (a number, an outcome).

**Beats (in order):**
1. Provocative direct address — name the reader's (and everyone's) flaw.
2. Cultural trend — the observation everyone's nodding at.
3. Brand positioning — "we leaned all the way into it."
4. Core principle + social proof — why it works, plus a real result.
5. Reframe — what the system/algorithm/market actually rewards.
6. Strategic choices + result — the values you chose and the outcome.
7. Key takeaway — "if your [output] feels [safe], that's why it's not working."
8. Engagement question.

**Fill-in template** (de-identified skeleton):

```text
Sorry to tell you this BUT...

You're [provocative quality].

And so is the rest of the world.

There's a trend going around right now saying [cultural observation].

And we've fully leaned into it. To bring some [quality/value] back. And the [result area] genuinely
shows.

Because in a world of [status quo], the only way to get [desired outcome] is to [required action]. It's
exactly why our [recent achievement] reached [specific result].

The [system] isn't trying to [feared assumption]. It's trying to [positive reframe]. So when you [follow
the crowd], you're working against the [system].

We chose [value 1]. We chose [value 2]. We chose to [distinctive decision]. And [the outcome].

So if your [work/output] feels [safe/generic] right now... that's probably exactly why it's not working.

[Key takeaway].

[Specific open question for the audience].
```

**Hard-rule notes:** drop any hashtags; cap emoji at one; keep the genuine open question and drop any
"repost if you agree" bait.

---

## Template: Mid-Conversation Recommendation

**Best for:** Educational posts that drop the reader mid-thought with your single favorite way to do
something, then separate what fails from what works. Pick this when you have one strong, opinionated
recommendation and the nuance behind it.

**Category affinity:** Educational (primary), Spicy Take (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A specific tactic/method you genuinely favor above the alternatives.
- [ ] Knowledge of the common and worst versions that fail (from experience).
- [ ] Concrete success criteria and the tactics that hit them.

**Beats (in order):**
1. Mid-conversation entry hook — "My favorite way to do this: (by far)".
2. The short answer / suggested action.
3. What doesn't work — the common version, then the worst version.
4. Success criteria — numbered outcomes the right version produces.
5. The tactics that achieve them.
6. Restate the recommendation (and a secondary one).
7. Delayed-payoff reassurance — "feels useless at first, then changes everything".
8. Key takeaway + a supporting stat or fact.

**Fill-in template** (de-identified skeleton):

```text
My favorite way to do this:
(By far)

[Short-phrase answer].

But not just any [answer]. [Common version] doesn't work. [Worst version] is worst of all.

[Answer] works when it makes people:
1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]

Which generally means you're:
- [Tactic 1]
- [Tactic 2]

[Secondary recommendation] helps a lot too. I definitely recommend it. But turn [primary recommendation]
into a habit too.

[Key takeaway, supported by a relevant stat/fact].
```

---

## Template: Underdog Comeback

**Best for:** Story posts where credentials and effort failed, until an unconventional action turned it
around — ending on a counterintuitive lesson. Pick this when the writer has a genuine rejection-to-result
arc.

**Category affinity:** Story Spark (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real failure/rejection despite real credentials or effort.
- [ ] A genuine unconventional action the writer took in response.
- [ ] A real, measurable result from that action, and the lesson it taught.

**Beats (in order):**
1. Vulnerable admission — failure despite the credentials ("X years, Y degrees, 0 results").
2. Emotional consequence — the negative self-label it created.
3. The big decision — the unconventional action.
4. Actionable advice — 2–3 suggestions for the reader in the same spot.
5. The measurable result of the unconventional action.
6. Counterintuitive lesson — reframe the negative label into an asset.
7. Engagement question.

**Fill-in template** (de-identified skeleton):

```text
I [vulnerable admission that highlights a common pain point].

[X years of credentials/actions]. [Another credential]. But [0 result].

The consistent [failures] made me feel [negative self-label].

So I started [unconventional action].

If you're not seeing any luck either:
- [Actionable suggestion 1]
- [Actionable suggestion 2]
- [Actionable suggestion 3]

[Time period] of [unconventional action] → [specific measurable result].

Lesson? [Counterintuitive reframe of your negative label].

[One-line philosophical close].

[Specific open question for the audience].
```

---

## Template: Underrated Tool Spotlight

**Best for:** Educational posts recommending a specific tool/resource you actually use, with the exact
reusable method and the result it gives. Pick this when you can show, not just name, the value — and you
have no undisclosed sponsorship.

**Category affinity:** Educational (primary), Data Nugget (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A specific tool/resource you genuinely use, plus a reusable prompt/method.
- [ ] Real outputs/results you've actually gotten from it.
- [ ] Honest disclosure (genuinely not sponsored, or disclose if it is).

**Beats (in order):**
1. Tool recommendation — "[tool] is the most underrated [category], and it's free/accessible".
2. Practical use case — the exact reusable prompt/method.
3. Desirable output — 2–3 specific results it produces.
4. Direct CTA — where to find it.
5. Anti-sell + extra benefit — "not sponsored, I just like it; here's the deeper use."
6. Photo context (if an image accompanies).

**Fill-in template** (de-identified skeleton):

```text
I really think "[tool/resource]" is the most underrated [category] right now. And it's completely
[free/accessible].

Here's my favorite [prompt/method] for [desired outcome]:
"[Exact reusable prompt/method]."

[Short timeframe] later, I get [result 1], [result 2], and [result 3].

Not sponsored — I just really like it. Especially because I can then [deeper use case].
```

**Hard-rule notes:** the "check it out at [link]" line is a body link → move the URL to the first
comment; the body keeps the recommendation, not the URL.

---

## Template: Curated Lessons List

**Best for:** Educational list posts — "I [studied X], here are the most important lessons" — built from
real, attributable sources. Pick this when the writer has genuinely done the work and the lessons are
specific.

**Category affinity:** Educational (primary), Data Nugget (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] The writer genuinely did the work named (read the books, ran the experiments, etc.).
- [ ] Real, attributable quotes/lessons — **never** a fabricated quote or a misattributed one.
- [ ] Enough genuine items to fill the count (typically 3–7).

**Beats (in order):**
1. Time-investment promise — "I've [done X a lot]; here are [N] of the most important lessons I've
   applied."
2. The numbered list of lessons/quotes — each with its real source.
3. Engagement question — "I have more. Should I do a part 2?"

**Fill-in template** (de-identified skeleton):

```text
I've [studied/read X]+ on [topic]. Here are [N] of the most important lessons I've learned and applied to
my [life/business]:

1. "[Quote/Lesson 1]." ([Real author] — [Real source])
2. "[Quote/Lesson 2]." ([Real author] — [Real source])
3. "[Quote/Lesson 3]." ([Real author] — [Real source])

I have [N] more. Should I do a part 2?
```

**Hard-rule notes:** the "should I do a part 2?" line is an acceptable specific question; quotes must be
verbatim and correctly attributed — if a quote can't be verified, drop it (gate).

---

## Template: Results-Backed Lead Magnet

**Best for:** Posts that stack real results, extract the single variable behind them, then offer a real
guide. Pick this only when the numbers and the guide genuinely exist. Heavily promotional — use sparingly.

**Category affinity:** Data Nugget (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] Real results with real numbers (never invent revenue or outcomes).
- [ ] A real single variable / repeatable method that genuinely drove them.
- [ ] An actual lead magnet/guide that exists and contains what's promised.

**Beats (in order):**
1. Results social proof — the real numbers, listed.
2. Quick clarification — these were different offers/contexts.
3. The common pattern — the single variable that drove the results.
4. Method behind it — the same playbook used across all.
5. More proof — a historical result for credibility.
6. Tease the guide's contents — the value points.
7. Exclusivity reframe — "we usually only share this with clients."
8. Reason for the giveaway.
9. CTA to get it.
10. Minimum-value guarantee — "even if you only do one thing…".

**Fill-in template** (de-identified skeleton):

```text
We've had [X] different [result-level] outcomes in [year]:
- [Item 1]: [$ amount/result]
- [Item 2]: [$ amount/result]
- [Item 3]: [$ amount/result]

Almost all were different [offers/contexts]. But the one thing they had in common: [percentage]% of our
[results] came from [single variable].

Not a coincidence — we used the exact same [playbook] for all of them.

So I made a full guide breaking down:
- [Value point 1]
- [Value point 2]
- [Value point 3]

Typically we only share this with [exclusive group]. But I'm tired of seeing people [common failure
mode].

[CTA to get the guide.]

PS — even if you only implement [1 tactic], I promise you'll [specific result].
```

**Hard-rule notes:** the "Comment 'X' and I'll send it" CTA is engagement-bait and collides with the
specific-open-question rule → convert the close to a specific open question and deliver the guide via the
first comment. Drop profanity if it's off the user's voice. This template is the most promotional in the
library — gate **hard** on real results and a real guide.

---

## Template: Boring-but-Profitable Framework

**Best for:** Counterintuitive educational posts that disarm with "this advice is boring" then deliver a
named, repeatable framework that quietly works. Pick this when the writer's edge is discipline over
novelty.

**Category affinity:** Educational (primary), Spicy Take (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A genuinely unglamorous but effective approach the writer uses.
- [ ] A real result it produces.
- [ ] A nameable framework plus a concrete example of running it.

**Beats (in order):**
1. Pattern interrupt — "the following advice is boring."
2. Credibility anchor — "but it [produces an impressive result] every [period]."
3. Introduce the named framework.
4. Explain it briefly.
5. A concrete example of doing it.
6. Core idea — repeatable actions compound.
7. Practical advice.
8. Counterintuitive advice — "embrace a bit of boredom."
9. Reframe — boredom means it's working.
10. *(Optional)* free-resource CTA.

**Fill-in template** (de-identified skeleton):

```text
The following advice is boring.

But it [generates an impressive result for me] every [time period].

If you really want to [achieve desired outcome], focus on what I call the '[named framework].'

Work out what you need to do every single [period] to experience [result 1] and [result 2]. Every
[period] we do [example action 1], [example action 2], etc.

When you're [at a specific stage], it's all about [activity] — and it's fun. But at some point you
[engage in the beneficial action]. So you've got to embrace a little bit of [reframed negative feeling].

All it means is that [high-level positive outcome], and you have a [named framework] guaranteed to [drive
the outcome] as long as you want it to.

[Specific open question for the audience].
```

**Hard-rule notes:** any "get it here [link]" resource CTA is optional and yields to the
specific-open-question CTA rule — if kept, move the link to the first comment.

---

## Template: Milestone Retrospective

**Best for:** Journey posts — "how I built [achievement] in [timeframe], and the lessons" — where the
value is the hard-won lessons, each carried by a real story or mistake. Distinct from System
Retrospective (which hands over a repeatable *system*); this hands over *lessons from a journey*.

**Category affinity:** Story Spark (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real milestone achieved in a real timeframe.
- [ ] Genuine lessons, each with a real anecdote, mistake, or observation.
- [ ] *(If an event/CTA is used)* a real event/resource.

**Beats (in order):**
1. "How I built [achievement] in [timeframe] (and [N] lessons I learnt along the way)."
2. Numbered lessons — each a header plus a personal anecdote / mistake / advice.
3. Engagement question (or CTA).

**Fill-in template** (de-identified skeleton):

```text
How I built a [specific achievement] in [timeframe].
(And [N] lessons I learnt along the way)

1. [Lesson header]
[Personal anecdote / challenge overcome / mistake you made / advice for the reader].

2. [Lesson header]
[Personal anecdote / challenge overcome / mistake you made / advice for the reader].

3. [Lesson header]
[Personal anecdote / challenge overcome / mistake you made / advice for the reader].

[Specific open question for the audience].
```

**Hard-rule notes:** the two-line title runs long — tighten the first line to an 8–10-word hook. Any
event/registration link → first comment.

---

## Template: Transformation-to-Invite

**Best for:** Posts that earn attention with a real transformation, handle the obvious objections, then
invite the reader to a real live event. Pick this only when the event and the numbers are genuine.
Promotional — use sparingly.

**Category affinity:** Story Spark (primary), Data Nugget (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real transformation (a modest start → a big result, with real numbers).
- [ ] A real method, and the real objections it overcomes.
- [ ] An actual event with real details (date, format) to invite to.

**Beats (in order):**
1. Impressive transformation — "I started [activity] for [modest goal]; now [big result]."
2. Shared frustrations with the usual alternatives.
3. The method that works for you.
4. Handle the objections.
5. Results — a revenue share or metric.
6. Tease the reveal.
7. Event details.
8. What you'll learn (value breakdown).
9. Register CTA.
10. Engagement question.

**Fill-in template** (de-identified skeleton):

```text
I started [activity] to get to [modest original goal].
Fast forward [timeframe], it got me to [dramatically larger result].

Most [alternatives] are:
- [problem 1]
- [problem 2]

But for me, [your method] has been the gift that keeps on giving. Even with:
- [common objection 1]
- [common objection 2]

It still [delivers an impressive ongoing result], for [surprisingly low cost]. And it accounts for
[percentage]% of our [key metric].

On [day/date] at [time], I'm sharing everything I know — LIVE.

What you'll learn:
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

[Register CTA.]

[Specific open question for the audience].
```

**Hard-rule notes:** the registration link → first comment; cap emoji at one. Gate hard — never fabricate
an event or the numbers.

---

## Template: Fear-Deflation Manifesto

**Best for:** Big-idea posts that name a fear the reader is frozen by, then deflate it with the writer's
own experience and a pattern observed in others. Pick this when the point is "the obstacle you're
afraid of never actually shows up."

**Category affinity:** Spicy Take (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real false belief/fear the writer once held, and the moment it was disproven.
- [ ] Specific feared obstacles that genuinely didn't materialize.
- [ ] A pattern the writer has actually observed in others (clients, peers).

**Beats (in order):**
1. Bold universal claim / uncomfortable truth.
2. Personal admission of the false belief you held.
3. The moment it was revealed as unfounded.
4. Name the specific feared obstacles (2–4).
5. Single-line deflation — none of it happened.
6. A mundane reason each fear never materialized.
7. Coaching observation — you've seen the pattern in others (social proof).
8. Reframe the broader system/environment.
9. A second personal proof point.
10. The realization — what the fear actually cost, and that it protected nothing.
11. "You don't need [X], [Y], [Z] — you just need to start [action]."
12. Reflection question.

**Fill-in template** (de-identified skeleton):

```text
[Bold universal claim about what's possible].

That's the uncomfortable truth most people never figure out.

[Personal admission of the false belief you held for years]. [What that looked like in practice].

[The moment that revealed the fear was unfounded].

[Name the specific fears or obstacles you anticipated — 2–4 concretely].

[Single-line deflation: none of that happened].

[Give each feared obstacle a mundane reason it never materialised].

I've watched this play out with [people I coach]. [The pattern — over-preparing, polishing, delay]. Then
[what actually happens when they finally act].

[Reframe the broader system or environment].

But if you decide to [take the hard route]? [What actually happens.]

The people who [achieve the outcome] aren't [positive trait] than everyone else. They just figured out
that [the key realisation].

You don't need [requisite 1]. You don't need [requisite 2]. You don't need [requisite 3]. You just need
to start [key next action].

[Specific reflection question for the audience].
```

**Hard-rule notes:** any "start here [link]" lead-magnet CTA → first comment.

---

## Template: Client Process Walkthrough

**Best for:** Service-positioning posts that open on a relatable client problem, then walk the reader
through your actual process and the result. Pick this when you have a real engagement and nameable steps.

**Category affinity:** Educational (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real client/engagement with a relatable problem (anonymized is fine).
- [ ] Your genuine, nameable process steps.
- [ ] A real, concrete client result.

**Beats (in order):**
1. Process promise — "When I [do service] for [client type], here's how I make sure [outcome]."
2. A client with a relatable problem.
3. Transition — "it starts way before [the obvious part]."
4. The numbered process steps, each with why it matters.
5. The concrete client result — within a short timeframe.
6. One-line philosophy about what the service should do at its best.
7. Reinforce positioning — "if you have [the symptom], that's the gap I fill."
8. CTA.

**Fill-in template** (de-identified skeleton):

```text
When I [do service] for [client type], here's how I make sure [I achieve the desirable outcome].

A [client type] reached out [time period] ago because they'd been [doing the thing] for [timeframe], had
[positive quality], but [state the problem] — and couldn't figure out why.

So I walked them through my process, and it starts way before I [do the obvious part]:

1. [Step 1 — the key actions, and why they matter].
2. [Step 2 — the key actions, and why they matter].
3. [Step 3 — the key actions, and why they matter].

Within [short timeframe], [client] had [specific, concrete result] — no [effort-intensive alternative].

[One-sentence philosophy about the service at its best.]

If [you have the symptom in the opening], that's exactly the gap I fill.

[Specific open question for the audience].
```

**Hard-rule notes:** the "drop an emoji and I'll review a few" close is engagement-bait → convert to a
specific open question; cap emoji at one.

---

## Template: Future Pacing

**Best for:** Motivational posts that vividly place the reader in a desirable future, then trace it back
to one pivotal behavior. Pick this when you want to sell a vision and make inaction feel costly.

**Category affinity:** Spicy Take (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A credible desirable future for the reader, grounded in a real method (not empty hype).
- [ ] The single pivotal insight/behavior that makes the difference.
- [ ] Real costs of inaction the writer can stand behind.

**Beats (in order):**
1. Big promise — "this will blow your mind."
2. Future pacing — "it's [time] from now and you're [a desirable scene + 3 outcomes]."
3. The single thing that made the difference.
4. Costs of inaction.
5. Handle the objection (it's not about virality/luck).
6. The pivotal insight.
7. Broader strategy.
8. Reinforce the cost of inaction.
9. Reframe as arithmetic — one action × many days.
10. Transformation statements — "that's how [identity before] become [identity after]."
11. Motivational directives.
12. "[Time] from now, you'll be where you are or where you want to be" + question.

**Fill-in template** (de-identified skeleton):

```text
This will blow your mind...

It's [time frame] from now and you're [everyday mundane scene]:
- [Specific desirable outcome 1]
- [Specific desirable outcome 2]
- [Specific desirable outcome 3]

Here's what made the difference: [core behaviour or decision]. Because [short supporting truth].

No matter how [quality that didn't save them], [absolute negative consequence of not doing the thing].

But [reframe — the common misconception]. It starts with one thing: [the single pivotal insight].

[Cost of inaction 1]. [Cost of inaction 2]. [Cost of inaction 3 — most painful].

[Reframe the outcome as logic, not luck.] [Reduce it to simple arithmetic.]

That's how [identity before] become [identity after].

[Short motivating directive 1]. [Short motivating directive 2].

Because [time frame] from now, you'll either be exactly where you are today or exactly where you want to
be.

[Specific open question for the audience].
```

**Hard-rule notes:** any lead-magnet link → first comment; cap emoji at one; tighten the opening to an
8–10-word hook.

---

## Template: Two Camps Divergence

**Best for:** Spicy, reflective posts built on a shared hardship that two kinds of people respond to
oppositely — ending on "which camp are you?" Pick this when the writer has a genuine observation and a
clear philosophical stance.

**Category affinity:** Spicy Take (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real shared experience or observation the audience relates to.
- [ ] A genuine divergence in responses the writer has actually seen.
- [ ] A philosophical stance the writer holds about the difference.

**Beats (in order):**
1. Tease the controversial take — "I might get crucified for this."
2. Tie to a piece of content / interaction / moment that prompted it.
3. The shared formative experience (escalate it).
4. Camp one's response — blame / limitation.
5. Camp two's response — "so what, we win anyway."
6. Curiosity framing — "how can two people go through the same thing…?"
7. Philosophical takeaway — control your reactions.
8. "Which camp do you fall into?" question.

**Fill-in template** (de-identified skeleton):

```text
I might get crucified for this, but oh well.

I saw [a piece of content / moment] recently and it got me thinking.

A lot of us who [shared background] experienced [difficult or formative situation]. A lot of us [second
shared experience]. A lot of us [third — escalates the weight].

Some of us take those experiences and say because of that [negative outcome]. We blame [external cause]
for [current result].

Then some of us say [same external cause] happened, but so what — we're going to [declaration of intent]
anyway.

I find this fascinating. How can two people go through the exact same situation and one decides it's
[outcome A] while the other decides it's [outcome B]?

[One-sentence core belief — what separates the two camps.]

[Key takeaway.] Which camp do you fall into?
```

---

## Template: Then-vs-Now Transformation

**Best for:** "Be your own case study" posts — a dated before, a stacked now, the obstacles in between,
and the one decision that changed everything. Pick this when the writer has a real transformation that
doubles as proof for an offer.

**Category affinity:** Story Spark (primary), Data Nugget (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real before→now transformation with real wins and real obstacles.
- [ ] A genuine turning-point decision.
- [ ] *(If a CTA is used)* a real offer.

**Beats (in order):**
1. "In [month/year] I [significant decision] with [humanising detail]. It's [now]. Here's where we are:"
2. A list of life/business wins.
3. "None of this was handed to me."
4. The obstacles overcome.
5. "But I made one decision that changed everything" — the decision.
6. Persistence shown — the actions you took.
7. "And slowly, then all at once — everything changed." + the one thing that made it possible.
8. CTA.

**Fill-in template** (de-identified skeleton):

```text
In [month and year], I [made a significant life/business decision] with [humanising detail].

It's [current year]. Here's where we are now:
- [Win 1]
- [Win 2]
- [Win 3]

None of this was handed to me.
[Obstacle 1]. [Obstacle 2]. [Obstacle 3].

But I made one decision that changed everything: [the decision].

[Expand on the actions/persistence you showed.]

And slowly, then all at once — everything changed. [One sentence naming the thing that made it possible.]

[Specific open question for the audience.]
```

**Hard-rule notes:** any "book a call here [link]" CTA → first comment.

---

## Template: Testimonial Spotlight

**Best for:** Minimal social-proof posts where a real customer's words do the selling, with a short warm
caption. Pick this only when a genuine testimonial exists. Note: this template leans on a testimonial
*asset* (usually an image) — as a text-only post it's thin.

**Category affinity:** Data Nugget (primary), Story Spark (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A REAL testimonial / piece of customer feedback (verbatim, with permission) — **never fabricated**.
- [ ] A genuine reason for the writer's short warm caption.

**Beats (in order):**
1. A short, warm one-liner.
2. The real testimonial / feedback (as an image asset, or quoted with permission).

**Fill-in template** (de-identified skeleton):

```text
[Short, warm one-liner — e.g. "I love what I get to do."]

[Real testimonial / positive feedback from a client — verbatim, with permission. Usually pasted as a
screenshot image.]
```

**Hard-rule notes:** the persuasion lives in the testimonial asset; the writer produces only the caption.
If no real testimonial exists, **disqualify** — do not invent one. If presented as text, attribute
honestly and keep it short.

---

## Template: Permission-Granting Take

**Best for:** Contrarian posts that release the reader from a limiting belief rather than teaching them
something new. Pick this when the audience already knows what to do but is held back by a should/should-not
rule the writer can dismantle.

**Category affinity:** Spicy Take (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A genuinely contrarian stance the writer holds.
- [ ] A specific reader behavior the writer is validating.
- [ ] A real reason the behavior is rational or necessary.

**Beats (in order):**
1. "Oddly unpopular take: [contrarian stance]."
2. Name the target reader — "if you're [doing the behavior]…".
3. Permission-granting statements — "you don't have to [expectation]; it's okay to [behavior]."
4. Philosophical takeaway.
5. Restate the contrarian stance.

**Fill-in template** (de-identified skeleton):

```text
Oddly unpopular take:
[Core contrarian stance.]

If you are [the behaviour being defended]… don't apologize for it.

You don't have to [social expectation 1].
You don't have to [social expectation 2].
It's okay if you're in your [name the season/phase].
It's okay to be [word society uses as criticism].

[One or two sentences reframing the behaviour as rational or necessary.]

[Key takeaway / restated stance.]
```

---

## Template: Identity Defense

**Best for:** Posts that defend a personal choice others judge ("I'm a proud [identity]"), back it with
outcomes, acknowledge the objection, and invite the reader to self-assess. Pick this when the writer
owns a contested identity and can make it useful to the reader.

**Category affinity:** Story Spark (primary), Spicy Take (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real identity/choice others might judge, plus real outcomes it produced.
- [ ] An honest objection the writer can acknowledge.
- [ ] A genuinely useful principle/quote and real self-assessment questions.

**Beats (in order):**
1. Core idea — "Just because you [fit], doesn't mean you [belong]."
2. Identity claim — "I'm a proud [identity]."
3. Positive outcomes that built credibility.
4. Acknowledge the objection (it's not easy).
5. Pivot — "but you know what's worse?"
6. Risk of inaction (regret).
7. A genuinely helpful quote/principle.
8. Reflective questions + a motivating close (and an optional self-assessment checklist).

**Fill-in template** (de-identified skeleton):

```text
Just because you [fit/qualify], doesn't mean you [belong/should stay].

I'm a proud [identity others might judge]. [That choice] changed my life:
- [Positive outcome 1]
- [Positive outcome 2]
- [Positive outcome 3]

But let me be clear: [briefly acknowledge the objection]. [Empathise with the difficulty.]

But you know what's worse? [Sum up the risk of inaction.]

I fall back on this when I'm [struggling with the trade-off]: "[a genuinely useful principle/quote]."

[Reflective question]? I hope you choose [growth trajectory].

[X] questions to ask if you're [considering the choice]:
1/ [Self-assessment question]?
2/ [Self-assessment question]?
3/ [Self-assessment question]?
```

**Hard-rule notes:** the quote must be real or clearly generic wisdom (not a fabricated attribution); cap
emoji at one.

---

## Template: Rebrand Debunk

**Best for:** Spicy takes that expose hyped new jargon as repackaged fundamentals, using a simple
filtering framework. Pick this when the writer has the insider standing to say "it's just [the original
thing]."

**Category affinity:** Spicy Take (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real rebrand/hype cycle in the writer's niche, with the new names and the recycled advice.
- [ ] First-hand knowledge that it's old fundamentals in new packaging.
- [ ] *(If a CTA is used)* the genuine slice that actually IS new, or a real event.

**Beats (in order):**
1. "[Familiar concept] has been getting a rebrand" + the new names.
2. The recycled advice list (in quotes).
3. Apply the filtering framework — "what would the novice and the expert both agree on?"
4. Verdict — "it's just [the original concept]" — and how much of the advice that covers.
5. The writer's take.
6. *(Optional)* event/resource CTA — including the honest slice that IS new.

**Fill-in template** (de-identified skeleton):

```text
[Familiar concept] has been getting a rebrand for months.
[New name 1], [New name 2], [New name 3]...

Then every week I read [content] pushing new '[rebrand name]' tactics:
"[Recycled advice 1]"
"[Recycled advice 2]"
"[Recycled advice 3]"

The filter kicks in: looking at these [rebrand name] tactics, what would the "novice" and the "expert"
both agree on?

Answer: "It's just [the original concept]."

That's 90% of the [rebrand name] advice out there — [decades]-old [original discipline] tactics
repackaged as revolutionary findings.

[Your take.]

[Specific open question for the audience.]
```

**Hard-rule notes:** any event/registration link → first comment; this pattern often pairs with a meme
image (e.g. a bell-curve), which is fine but optional.

---

## Template: Stop-Start Reframe

**Best for:** Directive contrarian posts — "stop [common thing], start [alternative]" — built on a
system-vs-human reframe and a two-column outcomes contrast. Pick this when the writer can argue a durable
principle against a chased trend.

**Category affinity:** Spicy Take (primary), Educational (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real common error the writer sees, plus the better alternative.
- [ ] A genuine reframe — the durable constant vs. the thing people chase.
- [ ] Real outcomes of each approach.

**Beats (in order):**
1. "Stop [common thing]. Start [alternative]."
2. Name the common error (the obsession).
3. Why it doesn't work.
4. Core reframe — the counterintuitive truth.
5. Approach 1 + its negative outcomes.
6. Approach 2 + its positive outcomes.
7. Why approach 2 wins — the constant vs. the changing.
8. Ironic payoff — do the right thing and the system rewards you anyway.
9. Key takeaway.

**Fill-in template** (de-identified skeleton):

```text
Stop [doing the common thing]. Start [doing the alternative].

We've become obsessed with [behaviour]. But [the system] doesn't [work the way the story says]. It
doesn't [value] your [human quality]. [Humans/the right group] do.

And here's what most people forget: [core reframe — a counterintuitive way of seeing it]. [One sentence
that makes it visceral.]

When you [do the wrong thing]:
- [Negative outcome 1]
- [Negative outcome 2]

When you [do the right thing]:
- [Positive outcome 1]
- [Positive outcome 2]

[The system] will change tomorrow. But [the human constant] remains constant.

And the best part? When you stop [chasing the system] and start [the alternative], [the system] often
rewards you anyway — because [platforms/markets] ultimately want [the simple thing].

[Key takeaway.]
```

---

## Template: I-Was-Wrong Trend Adoption

**Best for:** Story posts where the writer dismissed a trend, was proven wrong, and rode it — ending on a
conviction about where it's going. Pick this when the writer has a genuine "I called it wrong, then
adapted" arc with real numbers.

**Category affinity:** Story Spark (primary), Spicy Take (secondary).

**Proof requirements** (the gate — every item must be satisfiable from real material, or disqualify):
- [ ] A real trend the writer dismissed, then embraced, with real numbers along the way.
- [ ] The genuine turning point and the broader industry shift.
- [ ] The writer's real current status.

**Beats (in order):**
1. "I remember being shocked [people offered me $X for Y]. Now I [charge/do far more]. Here's the story:"
2. Set the scene — when you first saw the trend.
3. You dismissed it.
4. The turning point — evidence kept coming.
5. The industry shift.
6. The positive impact on you.
7. "So yeah, I was wrong" admission.
8. Future prediction — the trend has legs.
9. Supportive market logic.
10. Your transformation — current status with real numbers.
11. Belief statement + engagement question / resource tease.

**Fill-in template** (de-identified skeleton):

```text
I remember being shocked that [people/brands] used to [offer me X / do Y]. Now I [do far more than that].
Here's the full story:

[Year] was when I first saw [others doing the new thing]. I told myself [dismissive rationalisation] —
this would pass.

But [the evidence kept coming]. I started [engaging with it] (still convinced it wouldn't last).

Then [next year] happened — the first year [the market] really started [the shift]. I also [hit a
personal milestone] that year.

So yeah, I was wrong.

I firmly believe [the trend] will only gain traction. [One or two sentences of market logic for why.]

Being early gave me an advantage. Now in [year], I'm [current status with specific numbers].

[Belief statement.] [Specific open question for the audience.]
```

**Hard-rule notes:** any "check my comments / link below" resource tease must point to the first comment,
not a body URL.
