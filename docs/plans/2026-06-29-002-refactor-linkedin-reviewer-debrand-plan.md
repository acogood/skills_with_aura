---
title: "refactor: De-brand the Lara Acosta reviewer into linkedin-post-reviewer"
type: refactor
status: ready
depth: standard
created: 2026-06-29
---

# refactor: De-brand the Lara Acosta reviewer into `linkedin-post-reviewer`

## Summary

The `lara-acosta-reviewer` skill is built end-to-end around a named real person and ~1 MB of
**paid, copyrighted course material** bundled under `plugins/content-writing/assets/linkedin-comeback/`.
This refactor turns it into a generic, opinionated **`linkedin-post-reviewer`**: the useful review
methodology (hook discipline, scannable formatting, cadence, modes) stays — re-expressed in original
wording and embedded directly in the SKILL.md body — while the person's name, persona, named
acquaintances, verbatim course quotes, branded framework coinages, and the bundled course corpus are
all removed. Every cross-reference across the repo (README, CLAUDE.md, the marketplace catalog,
NOTICE.md, PORTING-NOTES.md) is swept clean, and the plugin version is bumped.

**Scope guardrail:** the other five skills are untouched, and no new review capability is added — this
is a rename + functional-methods rewrite + reference sweep + git-history purge, nothing more.

**Copyright framing (read this honestly):** this plan reduces *practical* copyright and association
risk — it removes the redistributable paid material from both the working tree and git history
(U2 + U5), strips the verbatim quotes, and replaces the author's branded coinages with generic descriptions, keeping only uncopyrightable functional methods
in original wording. It is **not** a legal guarantee. If the user needs certainty, a lawyer should
review.

---

## Problem Frame

The skill cannot be shipped or shared without copyright/association exposure, for two distinct reasons:

1. **Redistribution risk (the hard one).** `plugins/content-writing/assets/linkedin-comeback/`
   (22 files, ~1 MB) is a verbatim course transcript plus PDF/markdown excerpts of a *paid* course.
   `SKILL.md` also reproduces source text near-verbatim in **at least three places** (the two "Voice Anchors" plus the duplicated italics peeve in the Voice Card, SKILL.md line 72). Shipping
   any of them copies protected expression. NOTICE.md already flags this directory as not-redistributable.
2. **Association risk (the softer one).** The skill reviews "in Lara Acosta's voice," encodes her
   signature phrasings, names real acquaintances ("my friend Mark", "Yvette the accountant"), cites
   "240K followers", and uses her branded framework names (FaceTime Effect, Halo Effect, Unfair
   Advantage Effect, Content Trifecta, Literally Academy). The user wants no association with her.

The *methodology* the skill applies — 8–10 word hooks, curiosity gaps, scannable line formatting, a
roughly 80/15/5 content mix, posting cadence, engagement-over-volume — are functional ideas and
widely-shared best practices, not protectable expression. The user explicitly wants this "necessary
info" kept and embedded, just stripped of the source and the brand.

The skill name is referenced in 6 files; the asset path in 0 other files (it is used only by this
skill), which keeps the blast radius small and well-bounded.

---

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R1 | Skill renamed to `linkedin-post-reviewer`; folder name and frontmatter `name:` match. | User (name choice) |
| R2 | No remaining association with the named author anywhere in the shipped repo — name, persona, signature phrasings, named acquaintances, follower count, and branded coinages all gone. | User ("not associated with her") |
| R3 | All mentions of "her course" removed; the bundled paid course material removed from the working tree (`git rm`, U2) and purged from git history (U5). | User ("remove any mentions of her course"; asset-disposition choice) |
| R4 | The review methodology is preserved and embedded in the SKILL.md body, expressed in original wording under generic names. | User ("include the necessary info … embed it into the skill's body") |
| R5 | The skill remains functional standalone — no dangling file reads, no reference to the removed asset corpus, no broken cross-links. | Quality bar |
| R6 | An opinionated, direct, blunt review voice is preserved — original and unattributed. | User (voice choice) |
| R7 | Repo metadata stays consistent and accurate — versions bumped, catalog/README/licensing docs updated, JSON still valid. | CLAUDE.md conventions |

---

## Key Technical Decisions

**KTD1 — New name: `linkedin-post-reviewer`.** Functional, parallel to the repo's other skill names
(`post-enricher`, `writing-style-analyzer`). "Reviewer," not "assistant," because the skill's scope is
review-only — it never drafts. The folder must be renamed to match (CLAUDE.md: `name` is kebab-case and
must match the folder name).

**KTD2 — Functional-methods rewrite, not a find-and-replace.** The copyright safety rests on the
idea/expression dichotomy (the *methods* are uncopyrightable), **not** on a literal clean-room
procedure — the implementer has seen the source, so the rewrite must actively clear its distinctive
*phrasing*, not just swap framework names. Keep the uncopyrightable functional methods,
re-stated in original wording; delete the protected expression (verbatim quotes, the bundled corpus)
and the persona. A mechanical name swap would leave the branded coinages and signature voice intact, so
the SKILL.md body is rewritten rather than patched.

**KTD3 — Rename branded coinages to generic descriptors.** Directional mapping (final wording is the
implementer's call):

| Branded coinage (remove) | Generic descriptor (keep the method) |
|---|---|
| FaceTime Effect | "write for a no-context reader / explain-it-to-a-friend clarity" |
| Halo Effect | "presence over connections / be seen in action" |
| Unfair Advantage Effect | "niche on yourself / your specific combination is uncopyable" |
| Content Trifecta | "content mix (~80% expertise / ~15% growth / ~5% reach)" |
| Content Themes (not Pillars) | "fluid themes over rigid pillars" |
| Literally Academy / "literally is her brand" | (removed entirely) |

Plain functional terms already in the file (hook, F-pattern/scannable formatting, power-ending,
CTA-as-question, self-comments, engagement-over-posting) are generic and stay as descriptors.

**KTD4 — Embed methodology in the body; drop the external-reference dependency.** Remove the
`## Pinned Context` section that reads `${CLAUDE_PLUGIN_ROOT}/assets/linkedin-comeback/…`. After the
rewrite the skill reads no bundled corpus — its checklists live in the SKILL.md body. This is what makes
R4 and R5 hold simultaneously.

**KTD5 — Remove course files from the working tree (`git rm -r`), then purge them from history (U5).**
`git rm` alone only removes the files from HEAD — the ~1 MB corpus sits in the initial commit and stays
recoverable, so a cloned/shared repo would still distribute it. Working-tree removal (U2) is paired with
a history purge (U5) to actually eliminate the exposure; the material lingers in history only until U5
runs, and the user keeps any personal copy outside the repo. (User chose `git rm` over
gitignore-and-keep; the history purge completes that choice.)

**KTD6 — Preserve an opinionated, original review voice.** Define an original "review register" in the
body — direct, blunt, willing to call out clichés and tells, lightly mocking of filler — without lifting
the source author's signature catchphrases or naming any real person. (User-chosen over a neutral
reviewer.)

**KTD7 — Version bump 0.1.0 → 0.2.0** in both `plugins/content-writing/.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json` (behavior change, per CLAUDE.md).

**KTD8 — Keep NOTICE.md; remove only the course bullet.** The `assets/examples/profiles/` creator style
cards remain as legitimately-bundled third-party-adjacent material, so NOTICE.md and the README license
note stay — only the `linkedin-comeback` bullet is deleted.

---

## Reference / Touch Surface

Everything that mentions the skill, the author, or the course. (Confirmed by repo-wide grep; the
example-profile "declarative" hits were false positives on the substring "lara".)

| File | What's there | Unit |
|---|---|---|
| `plugins/content-writing/skills/lara-acosta-reviewer/SKILL.md` | The whole skill — frontmatter, persona, coinages, verbatim quotes, pinned-asset reads, dangling `feedback_li_cadence_premise.md` ref | U1 |
| `plugins/content-writing/assets/linkedin-comeback/` (22 files, ~1 MB) | Paid course transcript + excerpts; referenced only by this skill | U2 |
| `README.md:35` | Skill table row ("in Lara Acosta's voice using her real frameworks…") | U3 |
| `README.md:47` | Compose example ("review the LinkedIn draft in Lara's voice") | U3 |
| `README.md:101` | `assets/` layout comment ("bundled reference material + worked examples") | U3 |
| `.claude-plugin/marketplace.json:16–17` | Plugin description ("a Lara Acosta-voiced LinkedIn reviewer", line 16) + `version` (line 17) | U3 |
| `plugins/content-writing/.claude-plugin/plugin.json` | `version` | U3 |
| `CLAUDE.md:94` | Architecture mention of the skill by name | U4 |
| `CLAUDE.md:104–106` | "Skill anatomy" outlier paragraph (lazy-loads bundled course corpus) | U4 |
| `CLAUDE.md:117–122` | Licensing-constraint section (names the paid course material) | U4 |
| `NOTICE.md:10–16` | Third-party-content bullet for the course | U4 |
| `PORTING-NOTES.md:19` | Porting-history row naming the Lara course + the skill | U4 |

---

## Implementation Units

### U1. Rename the skill folder and clean-room-rewrite SKILL.md

- **Goal:** Produce `linkedin-post-reviewer/SKILL.md` — a generic, opinionated LinkedIn post reviewer
  with its methodology embedded and all author/course/quote content removed.
- **Requirements:** R1, R2, R4, R5, R6.
- **Dependencies:** none (this is the anchor unit; the new name it establishes is consumed by U3/U4).
- **Files:**
  - `git mv plugins/content-writing/skills/lara-acosta-reviewer/` → `plugins/content-writing/skills/linkedin-post-reviewer/` (preserves history)
  - Rewrite `plugins/content-writing/skills/linkedin-post-reviewer/SKILL.md`
- **Approach:**
  - **Frontmatter:** `name: linkedin-post-reviewer`. New third-person `description` stating *what +
    when* (trigger phrases: "review this LinkedIn post / draft / hook", "review my LinkedIn week",
    "is this hook strong", "should I post this on LinkedIn?") *and boundaries* (NOT for drafting new
    posts; NOT for non-LinkedIn copy — blog/email/ads). No author name, no course reference.
  - **Delete** the `## Pinned Context` section and every `${CLAUDE_PLUGIN_ROOT}/assets/linkedin-comeback/…`
    read (KTD4), the `## Voice Anchors (verbatim from the course transcript)` section (the two
    word-for-word quotes — replace with an original 2–3 line calibration note describing the
    quote-back-then-react pattern in original words), and the "Course §…" pointers in the frameworks
    table.
  - **Rename** branded coinages to generic descriptors per KTD3.
  - **Rewrite the Voice Card** into an original "review register" spec (KTD6): blunt, direct,
    calls out clichés/filler/tells, lightly mocking — with **no** signature catchphrases lifted from the
    source and **no** named real people (drop "Mark/Yvette/Jody/Justin Welsh", "240K followers",
    "Literally Academy", the "literally"-as-brand note). Generic example openers/sign-offs may be used,
    but invent them.
  - **Remove** the dangling `feedback_li_cadence_premise.md` citation and the "Anton's Skeptical
    Practitioner banned-phrase list" cross-references (personal artifacts not in the repo); restate the
    cadence rule generically ("don't soften the cadence target on observed behavior alone — question the
    bottleneck instead").
  - **Keep** the functional methodology in original wording: hook discipline, body/formatting
    discipline, cadence + engagement rules, the four modes (`review-week`, `review-post`, `review-hook`,
    `coach`), output formats, and edge cases.
- **Patterns to follow:** other SKILL.md files in `plugins/content-writing/skills/` for frontmatter
  shape and the imperative body style; CLAUDE.md "Conventions when adding/editing skills" (kebab-case
  name matches folder; description states what + when + boundaries; body < ~500 lines).
- **Test scenarios (trigger-eval + content):**
  - *Triggers (must fire):* "review this LinkedIn post"; "check my LinkedIn draft before I post"; "is
    this hook strong enough?"; "review my LinkedIn posts for the week"; "should I post this on a Sunday?"
    (coach mode).
  - *Near-misses (must NOT fire):* "write me a LinkedIn post" (drafting → other skills); "review this
    blog post / cold email / ad" (non-LinkedIn copy); "analyze this creator's writing style"
    (`writing-style-analyzer`); "pull talking points from this transcript" (`talking-point-extractor`).
  - *Content checks:* zero occurrences of `lara`, `acosta`, `literally academy`, `facetime effect`,
    `halo effect`, `unfair advantage`, `content trifecta`, `240k`, or the named acquaintances; no
    verbatim transcript quote; no `${CLAUDE_PLUGIN_ROOT}/assets/linkedin-comeback` read; no
    `feedback_li_cadence_premise` reference; hook/body/cadence checklists and all four modes present; an
    opinionated voice spec present.
- **Verification:** Install the local checkout into Claude Code and prompt the trigger and near-miss
  phrases above (per PORTING-NOTES.md §4 trigger-eval loop); confirm fires/no-fires match. `grep -iE`
  the file for the banned term list — author names word-boundaried (`\blara\b`, `\bacosta\b`) plus
  `justin welsh`, `yvette`, `jody`, `literally academy`, `facetime effect`, `halo effect`,
  `unfair advantage`, `content trifecta`, `240k` — → zero hits; eyeball the generic name "Mark"
  (not greppable repo-wide). Skill produces a review with no file-not-found errors.

### U2. Remove the bundled paid course material

- **Goal:** Delete the redistributable paid corpus from the repo.
- **Requirements:** R3, R5.
- **Dependencies:** U1 (so the rewritten SKILL.md no longer references these files before they're
  removed — avoids a broken intermediate commit).
- **Files:** `git rm -r plugins/content-writing/assets/linkedin-comeback/` (all 22 files).
- **Approach:** Straight removal. Confirm beforehand that no file outside this directory references the
  path (already verified: zero external references).
- **Test scenarios:** none — pure deletion; covered by verification below.
- **Verification:** `plugins/content-writing/assets/linkedin-comeback/` no longer exists in the working
  tree; `grep -rn "linkedin-comeback" .` (excluding `.git/` and `docs/plans/`) returns nothing. (This
  grep only reaches zero once U3 and U4 also land — README, CLAUDE.md, NOTICE.md, and PORTING-NOTES.md
  reference the path until then — so treat it as an end-state check, not a per-unit gate.)

### U3. De-brand the catalog, README, and version metadata

- **Goal:** Update everything a user or Claude sees in discovery, and bump the version.
- **Requirements:** R1, R2, R3, R7.
- **Dependencies:** U1 (new name), U2 (assets removed, so docs can describe them as gone).
- **Files:**
  - `README.md` — table row (`:35`): new name + de-branded one-line description ("Reviews LinkedIn
    drafts — playbooks, posts, hooks — against an embedded best-practices checklist, in an opinionated
    direct voice"). Compose example (`:47`): drop "in Lara's voice". Assets layout comment (`:101`):
    "worked examples" (course material no longer bundled).
  - `.claude-plugin/marketplace.json` — plugin `description` (`:16`): replace "a Lara Acosta-voiced
    LinkedIn reviewer" with "an opinionated LinkedIn post reviewer"; bump `version` 0.1.0 → 0.2.0.
  - `plugins/content-writing/.claude-plugin/plugin.json` — bump `version` 0.1.0 → 0.2.0.
- **Approach:** Surgical text edits; keep "six skills" counts unchanged (count is unchanged).
- **Test scenarios:**
  - Both JSON files parse (`python3 -m json.tool` or equivalent) after edit.
  - README table still lists six skills; the renamed row reads correctly and names no person.
- **Verification:** `grep -i "lara\|acosta" README.md .claude-plugin/marketplace.json
  plugins/content-writing/.claude-plugin/plugin.json` → zero hits; both versions read `0.2.0`; JSON
  valid.

### U4. Update the contributor and licensing docs

- **Goal:** Bring the internal docs and the licensing surface in line with the removed material.
- **Requirements:** R2, R3, R7.
- **Dependencies:** U1 (new name), U2 (assets removed).
- **Files:**
  - `CLAUDE.md` — `:94` rename the skill mention; `:104–106` rewrite the "outlier" paragraph (it's still
    the outlier — no `content-workspace/` dependency, methodology embedded in its body — but it no longer
    lazy-loads a bundled course corpus); `:117–122` rewrite the Licensing-constraint section to drop the
    `linkedin-comeback` sentence and re-point the "third-party material is not MIT" rule at
    `assets/examples/profiles/` (profiles of real public creators), keeping the "record in NOTICE.md"
    rule.
  - `NOTICE.md` — delete the `linkedin-comeback` bullet (`:10–16`); keep the header, intro, the
    `assets/examples/profiles/` bullet, and the closing owner-removal line.
  - `PORTING-NOTES.md` — `:19` revise the porting-history row so it no longer names the author or the
    course (either drop the row or restate it generically as "removed in 0.2.0"); scan the rest of the
    file for any other course/author mention while here.
- **Approach:** Edit for accuracy, not erasure of history — PORTING-NOTES may record the *removal* as a
  fact, just without naming the author or course.
- **Test scenarios:**
  - CLAUDE.md no longer asserts a bundled course corpus exists; the licensing section names only material
    that still ships.
  - NOTICE.md no longer references the course but still covers the example profiles.
- **Verification (the overall acceptance gate):** word-boundary the author-name terms (the kept
  `assets/examples/profiles/` cards contain "declarative"/"declaration", which embed the substring
  "lara"), and add the named acquaintances U1 removes:
  `grep -rIniE "\b(lara|acosta|justin welsh|yvette|jody)\b|literally academy|facetime effect|halo effect|unfair advantage|content trifecta|linkedin-comeback|240k" .`
  excluding `.git/` and `docs/plans/` → **zero hits**. The generic first name "Mark" isn't greppable
  repo-wide (matches "market"/"remark"), so U1's file-scoped content check covers it instead.

### U5. Purge the course material from git history

- **Goal:** Eliminate the redistribution exposure for real — remove the paid corpus from git history,
  not just from HEAD.
- **Requirements:** R3.
- **Dependencies:** U2 (working-tree removal lands first).
- **Files:** history operation (not a file edit) — every blob under
  `plugins/content-writing/assets/linkedin-comeback/` across all commits.
- **Approach:** Rewrite history to drop the path, e.g.
  `git filter-repo --path plugins/content-writing/assets/linkedin-comeback --invert-paths` (or, if the
  repo has never been pushed, a fresh squash / `git checkout --orphan` re-init). **This rewrites commit
  hashes** — every commit from the first touch onward changes. If the repo is already shared/pushed,
  coordinate a force-push and have collaborators re-clone; if it has never been published, run this
  before the first public push and the disruption is nil.
- **Execution note:** confirm publication status before running — the right mechanism depends on whether
  history is already shared (see Open Questions).
- **Test scenarios:** none — history operation; covered by verification below.
- **Verification:** `git log --all --oneline -- plugins/content-writing/assets/linkedin-comeback/`
  returns nothing, and a fresh clone contains no trace of the corpus.

---

## Scope Boundaries

**In scope:** renaming and functional-methods-rewriting the one reviewer skill; removing the bundled course
corpus; sweeping every author/course reference across README, CLAUDE.md, the marketplace catalog,
NOTICE.md, and PORTING-NOTES.md; bumping the plugin version.

**Non-goals (true non-goals):**
- The other five skills — untouched.
- New review capabilities, new modes, or methodology beyond what already exists.
- Changing how the skill triggers *conceptually* (it still reviews LinkedIn drafts) — only the
  description wording changes to drop the author and broaden trigger phrasings.
- Re-licensing or altering the `assets/examples/profiles/` creator style cards.

**Deferred to Follow-Up Work:**
- A skill-creator trigger-eval *harness run* (scripted variance analysis) beyond the manual
  install-and-prompt check in U1 — nice-to-have, not blocking.
- Any rewrite of the example-profile style cards (they describe public creators and are governed by
  NOTICE.md's second bullet; out of this change's intent).

---

## Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Incomplete de-branding** — a stray author/coinage string survives somewhere. | Medium | The word-boundaried grep gate in U4 must return zero before done. The gate catches *named* terms only; surviving distinctive *phrasing* (mockery lines, peeve wording) is caught by the U1 manual rewrite + file-scoped content check, not the gate. |
| **Paid material recoverable from git history** — `git rm` leaves the corpus in the initial commit. | High if published as-is | U5 purges history; gate any public push on U5 completing (see Open Questions). |
| **Trigger regression** — the new generic description over-fires (any "review my writing") or under-fires. | Medium | U1 trigger-eval with explicit near-misses against the other skills; tune the description's boundary clause until fires/no-fires are clean. |
| **Over-sanitizing the methodology** — the rewrite strips so much that the review loses its usefulness. | Medium | KTD2/KTD3 keep the functional checklists intact (they're uncopyrightable); only names, quotes, and persona are removed. Verify the hook/body/cadence checklists and all four modes survive. |
| **Broken intermediate commit** — assets removed before SKILL.md stops referencing them. | Low | U2 depends on U1; land the rewrite first (or squash). |
| **False sense of legal safety.** | Low | The Summary states this is practical risk-reduction, not legal certainty; the README/NOTICE no longer overclaim. |

---

## Open Questions

The three material forks (new name, voice posture, asset disposition) were resolved with the user before
planning: `linkedin-post-reviewer`, keep an opinionated original voice, `git rm` the course files.

**Surfaced by review — resolve before/while executing:**
- **History-purge timing (U5, P1).** Has this repo already been pushed or shared publicly? If yes, U5 is
  a coordinated history rewrite (`git filter-repo`) + force-push + collaborator re-clone; if it has never
  been published, run U5 before the first public push for zero disruption. Confirm publication status
  before running U5.
- **Differentiated value proposition (optional, P2).** A generic de-branded reviewer risks reading as a
  commodity checklist. Optionally lead the SKILL.md `description` and catalog/README copy with the
  specific *enforced* rule-set (hard 8–10-word hook cap, F-pattern/mobile-line discipline, cadence floor,
  self-comment protocol) rather than the phrase "best-practices checklist." Aligns with the kept
  opinionated voice; not required for the copyright goal.

---

## Acceptance

The refactor is complete when:
1. The skill lives at `plugins/content-writing/skills/linkedin-post-reviewer/SKILL.md` with matching
   `name:`, embeds its methodology, and names no person/course.
2. `plugins/content-writing/assets/linkedin-comeback/` is gone from the working tree.
3. The repo-wide word-boundaried grep gate (the U4 command, excluding `.git/` and `docs/plans/`) returns
   zero hits — word boundaries on the author names prevent false positives on "declarative" in the kept
   example-profile cards.
4. Installing the local checkout and prompting the U1 trigger/near-miss phrases yields correct
   fires/no-fires and a working review.
5. `marketplace.json` and `plugin.json` are valid JSON at version `0.2.0`; README and licensing docs are
   accurate.
6. `git log --all -- plugins/content-writing/assets/linkedin-comeback/` returns nothing — the corpus is
   gone from history, not just HEAD (U5).
