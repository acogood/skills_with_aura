# Content Audience Profile Template

This document defines the exact output format for `content-audience-profile.md`. Follow this structure for every profile. For a complete worked example, see `worked-example.md` in this directory.

## Template Structure

The profile has a metadata header and 10 sections. Every section is required — if data is thin for a section, include it with a note about confidence level rather than omitting it.

---

## Metadata Header

```markdown
# Content Audience Profile: [Audience Label]

> **Last updated:** [Date]
> **Primary platform:** [LinkedIn / Newsletter / X / Other]
> **Audience tier this profile targets:** [Executive / Practitioner / End-user]
> **Client:** [Company name]
> **Industry:** [Client's industry]
```

The audience tier is critical. It determines which vocabulary register the entire profile uses. One profile = one tier. If the client needs multiple tiers, generate separate profiles.

---

## Section 1: Audience Identity

**What it captures:** Who they are, how they see themselves, how sophisticated they are.

**Why it's here:** Whatever writes from this profile reads this first to calibrate tone, depth, and specificity. The "how they see themselves" field drives what they'll share publicly (social JTBD). The sophistication level signals whether to explain concepts or use insider shorthand.

**Template:**

```markdown
## 1. Audience Identity

**Who they are:** [2-3 sentences. Job title, seniority, what they're accountable for, team size/scope. Be specific.]

**How they see themselves:** [2-3 sentences. Professional identity — what they take pride in, how they want to be perceived by peers.]

**Sophistication level:** [Beginner / Intermediate / Advanced / Expert. One sentence explaining what this means for content — e.g., "Expert: use insider references without explanation; defining in-group terms signals outsider."]
```

**Data sources:** Client website (who they say they serve), Perplexity research, competitor positioning.

---

## Section 2: Jobs to Be Done

**What it captures:** What outcome the audience is trying to achieve — functional, emotional, and social layers.

**Why it's here:** Resonant openers pull from the emotional/social jobs; insights land best when framed as serving the functional job. Content that addresses all three layers outperforms content that only hits the functional layer.

**Template:**

```markdown
## 2. Jobs to Be Done

**Primary job:**
When [specific circumstance], I want to [functional goal], so I can [desired outcome] without [specific pain they're trying to avoid].

**Emotional job:** [How they want to feel — e.g., confident, in control, not anxious about X]

**Social job:** [How they want to be seen — e.g., as the person who modernised the team, as pragmatic not trendy]
```

**Data sources:** Client website (what outcomes they promise), Perplexity research (aspirations + fears), G2 reviews (what users actually want).

---

## Section 3: Pain Points (Prioritised)

**What it captures:** Top 3 pain points, ranked by evidence, with the audience's exact language for each.

**Why it's here:** Content built from this profile should prioritise P1 topics and reference the "how they describe it" phrases. The ranking prevents low-priority topics from crowding out high-priority ones.

**Template:**

```markdown
## 3. Pain Points (Prioritised)

**🔴 P1: [Pain point name]**
[2-3 sentences: what it is, why it hurts, data point if available.]
- **How they describe it:** "[Exact phrase they use]"
- **Content opportunity:** [What type of content addresses this]

**🟠 P2: [Pain point name]**
[Same structure]

**🟡 P3: [Pain point name]**
[Same structure]

**Common objections / misconceptions:**
- [Objection 1 — what they believe that's wrong or incomplete]
- [Objection 2]
```

**Ranking criteria:** Frequency (how many mention it) × Severity (does it block decisions or just annoy?) × Addressability (can content actually help?). Frequency alone is misleading — pricing gets mentioned constantly but may not be the actual blocker.

**Data sources:** G2/Capterra reviews (ABSA-style — which aspects score negative?), Perplexity research (community complaints), X/Grok (unfiltered frustration), uploaded sales docs (objections).

---

## Section 4: Vocabulary Library

**What it captures:** Exact language mapping — what this audience says vs. what they don't say, plus in-group terms and outsider terms.

**Why it's here:** This is the highest-leverage section. Communication Accommodation Theory shows that matching the reader's language creates automatic psychological closeness. Using the wrong tier's language (e.g., executive language for practitioners) creates immediate disengagement. Check this table before generating any output from this profile.

**Template:**

```markdown
## 4. Vocabulary Library

| Concept | This audience says | They DON'T say (too generic / wrong tier) |
|---------|-------------------|-------------------------------------------|
| [Core concept 1] | "[Their exact phrase]" | "[Wrong-tier phrase]" |
| [Core concept 2] | "[Their exact phrase]" | "[Wrong-tier phrase]" |
| [Core concept 3] | "[Their exact phrase]" | "[Wrong-tier phrase]" |
| [Core concept 4] | "[Their exact phrase]" | "[Wrong-tier phrase]" |
| [Core concept 5] | "[Their exact phrase]" | "[Wrong-tier phrase]" |

**In-group terms they use without explanation:**
[List of acronyms, jargon, shorthand. Skills should use these naturally without defining them.]

**Terms that signal "outsider" / "vendor speak":**
[List of words that trigger disengagement — e.g., "synergy," "leverage," "solution."]
```

**Aim for 5-8 vocabulary pairs.** Focus on the concepts most likely to appear in content — pain points, solutions, outcomes, processes.

**Data sources:** G2 reviews (end-user language), Perplexity research (how professionals frame it), X/Grok (informal language), competitor websites (what language the audience has been primed to expect), client website (the language gap between how the client talks and how the audience talks).

---

## Section 5: Emotional Register & Validation Hooks

**What it captures:** The audience's default emotional state when consuming content, and ready-to-use validation phrases.

**Why it's here:** The research is clear — jumping straight to advice without first validating the reader's experience triggers cognitive resistance. Validation must come before persuasion. These hooks are ready-to-use openers that signal "I understand your situation" before pivoting to value.

**Template:**

```markdown
## 5. Emotional Register & Validation Hooks

**Their default emotional state when consuming content about [topic]:**
[2-3 sentences. Are they anxious? Skeptical? Overwhelmed? This sets the emotional tone for all content.]

**Validation hooks — use BEFORE offering insight or advice:**
- "[Validation hook 1 — describes a feeling or situation they'll recognise]"
- "[Validation hook 2]"
- "[Validation hook 3]"
- "[Validation hook 4]"
- "[Validation hook 5]"

**Emotional sequence that works with this audience:**
1. **Acknowledge** — [what to acknowledge first]
2. **Normalise** — [how to frame it as common / not their fault]
3. **Reframe** — [the insight or new perspective]
4. **Path forward** — [concrete next step]
```

**Validation hook quality bar:** A hook works if someone in this audience would read it and think "that's exactly my situation." If it's too generic to trigger that recognition, it's not specific enough.

**Important:** Include 5 hooks and rotate them rather than reusing one. Overuse of any single validation phrase leads to semantic satiation — it loses meaning through repetition.

**Data sources:** G2 reviews (emotional language), Perplexity research (community frustrations), X/Grok (unfiltered emotional expression), uploaded sales transcripts (how prospects describe their situation).

---

## Section 6: Content Triggers & Anti-Triggers

**What it captures:** What content pulls them in AND what makes them scroll past.

**Why it's here:** The triggers guide content creation. The anti-triggers are equally important — they're the guardrails that prevent content that feels tone-deaf. Includes persuasion principle mapping by audience stage.

**Template:**

```markdown
## 6. Content Triggers & Anti-Triggers

### What pulls them in

**Topics:**
- [Topic 1 + specific angle that makes it compelling]
- [Topic 2 + angle]
- [Topic 3 + angle]

**Formats that work on their primary platform:**
- [Format 1 + why it works for this audience]
- [Format 2 + why]

**Persuasion principles that resonate (mapped to stage):**
- Awareness → [e.g., Authority — they need to trust you before engaging]
- Consideration → [e.g., Social proof — peer validation]
- Decision → [e.g., Specificity — concrete details, not vague promises]

### What makes them scroll past (Anti-Triggers)

- [Anti-trigger 1 — specific content pattern + why it breaks resonance]
- [Anti-trigger 2]
- [Anti-trigger 3]
- [Anti-trigger 4]
```

**Data sources:** Perplexity research (what content this audience engages with), X/Grok (what gets engagement vs ignored), competitor content analysis (what the market is saturated with), G2 reviews (what claims audiences distrust).

---

## Section 7: Situational Framings

**What it captures:** 4 vivid, recognisable scenarios the audience is currently living through.

**Why it's here:** These activate narrative transportation — when readers recognise their situation in the opening of a content piece, they shift into a mode where everything that follows feels personally relevant. Use these as opening scenarios.

**Template:**

```markdown
## 7. Situational Framings

- **Situation 1:** "[Vivid, specific description of a moment they'll recognise]"
- **Situation 2:** "[Another recognisable scenario]"
- **Situation 3:** "[Another recognisable scenario]"
- **Situation 4:** "[Another recognisable scenario]"

**Specificity guidance:** This audience responds to [high / medium] specificity. [Brief note on what level of detail works — e.g., "Use specific tool names and metrics. Vague references to 'improving efficiency' feel generic."]
```

**Quality bar:** Each situation should be specific enough that someone in this audience thinks "that literally happened to me this week." Use specific tool names, specific moments (Monday morning, the vendor demo, the budget meeting), and specific emotional beats.

**Data sources:** G2 reviews (specific scenarios mentioned), Perplexity research (common situations), X/Grok (what moments trigger posts), uploaded sales transcripts (how prospects describe their situation).

---

## Section 8: Trusted Voices & Proof Types

**What it captures:** Who they listen to, what evidence they respect, what undermines credibility.

**Why it's here:** When a skill includes evidence or references in content, it needs to know what types of proof this audience actually trusts. A Fortune 500 case study might impress one audience and alienate another.

**Template:**

```markdown
## 8. Trusted Voices & Proof Types

**Who they listen to:**
- [Type of voice + why they trust them]

**What they read/consume:**
- [Specific publications, newsletters, podcasts, communities]

**Proof types that build credibility with this audience (ranked):**
1. [Strongest proof type]
2. [Second]
3. [Third]

**What undermines credibility:**
- [Credibility killer 1]
- [Credibility killer 2]
```

**Data sources:** Perplexity research (publications, influencers, communities), X/Grok (who gets engagement from this audience), competitor content (what proof types competitors use — is the audience primed for certain evidence formats?).

---

## Section 9: Platform-Specific Notes

**What it captures:** Format, voice, and engagement adjustments for each relevant platform.

**Why it's here:** When writing for a platform, read ONLY its relevant subsection. A LinkedIn post shouldn't read like a tweet. These notes capture the deviations from the base profile needed for each platform.

**Template:**

```markdown
## 9. Platform-Specific Notes

### LinkedIn
- **What works:** [Format, length, style specifics]
- **Voice adjustment:** [Any shift from base profile needed for LinkedIn]
- **Engagement pattern:** [How this audience engages — comments, shares, saves?]

### Newsletter / Email
- **What works:** [Format, length, style specifics]
- **Subject line approach:** [What gets opens]
- **Engagement pattern:** [Read fully? Skim? Forward?]

### X (Twitter)
- **What works:** [Format, length, style specifics]
- **Voice adjustment:** [Shift needed for X]

### Other: [Platform]
- [Notes as relevant]
```

Only include platforms relevant to the client. If their primary platform is LinkedIn and they don't use X, keep the X section minimal or note "Not a priority platform for this audience."

**Data sources:** Perplexity research (platform-specific engagement patterns), X/Grok (how the audience behaves on X specifically), competitor content (what formats competitors use on each platform).

---

## Section 10: Update & Measurement Log

**What it captures:** What metrics indicate the profile is accurate, and a revision history.

**Why it's here:** The monthly feedback loop reads this section to know what to measure. When performance data comes in, specific sections get updated — not the whole profile.

**Template:**

```markdown
## 10. Update & Measurement Log

**Key metrics to track (signals the profile is accurate):**
- [Metric 1]
- [Metric 2]
- [Metric 3]

**Profile revision history:**
| Date | Section updated | What changed | Why (data signal) |
|------|----------------|-------------|-------------------|
| [Date] | Full profile | Initial creation | Onboarding |
```

---

## Quality Rules (Apply to Every Profile)

1. **Be specific, not generic.** "They care about ROI" is useless. "67% cite cross-functional alignment as their top challenge (Salesforce, 2025)" is useful. If a statement could apply to any audience, cut it.

2. **Use their language, not yours.** If the audience says "shelfware," the profile says "shelfware" — not "underutilised technology investment." The vocabulary library should be reflected throughout the entire profile.

3. **Ground every claim in research.** Include data sources inline. If you're extrapolating or guessing, flag it explicitly with "[low confidence — extrapolated from broader data]."

4. **Prioritise by evidence, not intuition.** Pain points are ranked by frequency × severity from the data, not by what feels important.

5. **Include the negative.** Anti-triggers, credibility killers, outsider terms — the "what NOT to do" guidance is as valuable as the "what to do" guidance.

6. **One profile = one audience tier.** Never try to serve executives and practitioners in the same profile. The vocabulary alone would be contradictory.

---

## Profile Footer

```markdown
---

*This profile is designed to be read by AI content skills. Every section is structured for machine readability while remaining human-reviewable. Upload this file as context to any content generation tool to tailor output for this audience.*
```
