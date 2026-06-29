---
title: "refactor: Drop Perplexity MCP, make built-in web research the only path + bake in source verification"
type: refactor
date: 2026-06-29
---

# refactor: Drop Perplexity MCP, make built-in web research the only path + bake in source verification

## Summary

Collapse the content-writing research skills from the current two-path model (Perplexity MCP primary → built-in `WebSearch`/`WebFetch` fallback) to a **single built-in path**, and bake **source-verification discipline** into every research step. Touches the 4 research skills, the profiler's template, the three docs, and the plugin version.

---

## Problem Frame

The research skills currently prefer a user-side Perplexity MCP and fall back to the built-in web tools. Two blind, skill-driven eval runs (recorded under `content-workspace/eval-runs/research-backends/`) put the two backends head to head on drafting LinkedIn posts. The built-in `WebSearch`/`WebFetch` path won both times (21–18, then 22–17). The decisive, repeatable signal was backend-attributable: **Perplexity returned confident, citation-shaped claims that did not survive verification** — a citation whose page didn't contain the claim (run 1) and multiple fabricated case studies with crisp fake percentages (run 2). The built-in path's "fetch the page and read it" step is itself the verification, and it surfaced primary sources.

Given that, keeping Perplexity as the named *primary* is backwards: it's an optional paid add-on that scored worse on the dimension that matters (verifiability), and the two-path text is carried in every research skill. The user's call is to drop it entirely. Separately, both runs showed the web (SEO/AI-generated "case studies") can fabricate too, so the verification discipline must be explicit in the skills regardless of backend.

---

## Requirements

### Research path

- R1. No content-writing skill names the Perplexity MCP or `perplexity_ask`/`perplexity_search`; each research skill describes one research path — `WebSearch` to find sources, then `WebFetch` the top results to read and cite them.
- R2. Each research skill's "API Integration Summary" collapses to a single built-in-web description (no Primary/Fallback MCP columns), and the "no API keys / zero keys" property is preserved.
- R3. `content-audience-profiler`'s `profile-template.md` no longer names "Perplexity research" as a data source (→ "Web research").
- R4. `post-enricher`'s `description` frontmatter names no specific vendor tool; every existing trigger phrase is preserved verbatim.

### Source verification

- R5. Each research step instructs the model to verify each cited stat/quote on its own source page before using it, to prefer primary or reputable sources over vendor/SEO blogs, and to discard fabricated-looking case studies (suspiciously crisp percentages, no confirmable company).

### Docs and release

- R6. `CLAUDE.md`, `README.md`, and `CONTRIBUTING.md` describe a single built-in web-research path (no "MCP-first" / "two-path"); a single power-user note — "you *may* use a Perplexity MCP to discover candidates faster, but verify each claim on its page" — lives in `CLAUDE.md` only, not in the skills.
- R7. The `content-writing` plugin version is bumped and the eval record carries the drop-Perplexity outcome.

---

## Key Technical Decisions

- **Drop Perplexity from the skills entirely (single built-in path):** the two eval runs show it isn't more reliable (it fabricated), it's an optional paid dependency, and `WebFetch`-read-the-page is the safer default. One path is also less skill text to maintain. (see `content-workspace/eval-runs/research-backends/.../result.md`)
- **Confine the "Perplexity can still help you discover faster" nuance to `CLAUDE.md`:** preserves the eval's "best of both" for power users without re-introducing two-path complexity into every skill body.
- **Verification discipline is backend-agnostic and stays even though Perplexity is gone:** Arm B (WebSearch) caught a fabricated SEO "FinOptic" case study, so "read the page, prefer primary sources, discard fake-looking stats" earns its place independently of which tool fetched the result.
- **`post-enricher` description: factual fix, not a trigger change:** replace only the "Uses Perplexity…" clause with a tool-agnostic "uses live web research…"; leave every trigger phrase untouched so triggering behavior is unchanged.
- **Version:** bump `content-writing` to 0.4.0. If the still-uncommitted 0.3.0 rewire (script removal) has not been released, this may instead fold into that 0.3.0 release — resolve at execution against whether 0.3.0 shipped.

---

## Implementation Units

### U1. post-enricher — collapse to a single built-in path + verification discipline (canonical)

- **Goal:** Establish the one-path + verification pattern the other skills will mirror.
- **Requirements:** R1, R2, R4, R5
- **Dependencies:** none
- **Files:** `plugins/content-writing/skills/post-enricher/SKILL.md`
- **Approach:** Rewrite the Prerequisites note, the Case Study and Quote "Primary — Perplexity MCP / Fallback — …" blocks, the Step 3 case/quote prose, the "Research returns weak results" / "No Perplexity MCP connected" edge cases, and the API Integration Summary table + rule line into a single `WebSearch → WebFetch` procedure. Remove `perplexity_ask`/`perplexity_search` mentions. In the `description` frontmatter, change the "Uses Perplexity to find recent, verifiable case studies and quotes" clause to a tool-agnostic phrasing; keep all trigger phrases. Add the verification discipline (R5) to the Case Study + Quote sections and the Step 5 Self-Check.
- **Patterns to follow:** the existing API-Integration-Summary shape already in the file (single "Web research" row), and the existing self-check checklist style.
- **Test scenarios:** Test expectation: none — skill-instruction edit. Verify by outcome: `grep -i perplexity` on the file returns nothing; the description's trigger phrases are byte-identical to before except the tool clause; the Self-Check includes a "verified on the source page" item.
- **Verification:** the skill reads as one research path with no Perplexity reference, and a reader is told to verify each cited claim on its page and discard fake-looking case studies.

### U2. Mirror the pattern into lookalike-content + writing-style-analyzer

- **Goal:** Apply U1's one-path + verification pattern to the two simpler research skills.
- **Requirements:** R1, R2, R5
- **Dependencies:** U1
- **Files:** `plugins/content-writing/skills/lookalike-content/SKILL.md`, `plugins/content-writing/skills/writing-style-analyzer/SKILL.md`
- **Approach:** In `lookalike-content`: rewrite Prerequisites, the Step 6 trending-topics "Primary — perplexity_ask / Fallback" block, the "No Perplexity MCP connected" edge case, and the final rule into the single path. In `writing-style-analyzer`: rewrite Prerequisites, the Step 3 API Integration table, the 3b LinkedIn and 3e indexed-content "Primary/Fallback" blocks, the LinkedIn edge case, and the final rule. Add the R5 verification line to each skill's research step.
- **Patterns to follow:** U1's rewritten post-enricher.
- **Test scenarios:** Test expectation: none — skill-instruction edit. Verify by outcome: `grep -i perplexity` on both files returns nothing; each retains a "no API keys" statement and a single `WebSearch`/`WebFetch` description.
- **Verification:** both skills describe one research path and carry the verification discipline.

### U3. content-audience-profiler + its profile-template

- **Goal:** Apply the pattern to the most Perplexity-heavy skill and its template.
- **Requirements:** R1, R2, R3, R5
- **Dependencies:** U1
- **Files:** `plugins/content-writing/skills/content-audience-profiler/SKILL.md`, `plugins/content-writing/skills/content-audience-profiler/profile-template.md`
- **Approach:** In `SKILL.md`: rewrite Prerequisites, the 2b competitors block, the 2e/2f/2g audience-research "Primary/Fallback" blocks, the "client website thin" and "Research failures" edge cases, and the API Integration Summary into the single built-in path; add R5 verification. In `profile-template.md`: replace "Perplexity research" with "Web research" on the 9 `**Data sources:**` lines, preserving the parenthetical descriptions and the rest of each line unchanged.
- **Patterns to follow:** U1's rewritten post-enricher; for the template, change only the tool name token.
- **Test scenarios:** Test expectation: none — skill/template edit. Verify by outcome: `grep -i perplexity` on both files returns nothing; the 9 template data-source lines still read sensibly with "Web research"; the SKILL retains its "no keys" + `WebFetch`-named-pages guidance.
- **Verification:** profiler describes one path with verification; template names no vendor tool.

### U4. Docs — CLAUDE.md, README, CONTRIBUTING

- **Goal:** Make the docs describe the single built-in path and house the lone power-user Perplexity note.
- **Requirements:** R6
- **Dependencies:** U1, U2, U3
- **Files:** `CLAUDE.md`, `README.md`, `CONTRIBUTING.md`
- **Approach:** In `CLAUDE.md`: retitle and rewrite the "Two-path research (MCP-first, built-in-web fallback)" section to a single built-in path; update the intro "Live research…" line and the path-discipline mention; add one power-user line ("you *may* connect a Perplexity MCP to discover candidates faster, but verify each claim on its page") and a verification-discipline line. In `README.md`: rewrite the Requirements "Web research" bullet to drop the "prefer Perplexity MCP when connected" phrasing. In `CONTRIBUTING.md`: rewrite the "live web research" guidance line to name only the built-in tools.
- **Patterns to follow:** the existing doc voice; keep the "no API keys required" framing.
- **Test scenarios:** Test expectation: none — docs edit. Verify by outcome: the only `perplexity` mention across the three docs is the single CLAUDE.md power-user note; no doc says "MCP-first" or "two-path".
- **Verification:** docs and skills agree on one built-in research path.

### U5. Version bump + eval-record outcome note

- **Goal:** Record the behavior change and the decision in the version + eval artifacts.
- **Requirements:** R7
- **Dependencies:** U1, U2, U3, U4
- **Files:** `plugins/content-writing/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `eval/research-backends/harness.md`
- **Approach:** Bump `version` in both manifests (0.3.0 → 0.4.0, or fold into 0.3.0 per the KTD if 0.3.0 is unreleased). Add a short note to `eval/research-backends/harness.md` recording the outcome: the two runs led to dropping Perplexity from the skills; the harness remains usable to re-test if a user connects an MCP.
- **Patterns to follow:** the existing manifest version fields; the harness's existing note style.
- **Test scenarios:** Test expectation: none — metadata/doc edit. Verify by outcome: both manifests show the new version; the harness names the drop-Perplexity outcome.
- **Verification:** version reflects the behavior change; the eval record explains why Perplexity was dropped.

---

## Scope Boundaries

- In scope: the 4 research skills, `profile-template.md`, the 3 docs, the plugin version, and a one-line eval-record note.
- The `post-enricher` description edit is a **factual tool-name fix**, not a triggering change — trigger phrases are preserved.

### Deferred to Follow-Up Work

- Re-running the full eval harness on a fresh topic to confirm the single-path skills behave (optional validation, not required to land this).
- The broader "bare skills repo" restructure (separate plan).

### Out of scope

- Changing any skill's trigger phrases or the `content-workspace/` contract.
- The non-research skills (`talking-point-extractor`, `linkedin-post-reviewer`) — they do no live research.
- The HTML guide siblings — grep confirms they carry no Perplexity references.

---

## System-Wide Impact

The research contract is a cross-cutting convention: `CLAUDE.md` documents it and all 4 skills follow it, so the skills and docs must change together (U1–U4) or they will disagree. The eval harness's "Arm A = Perplexity" remains as a historical record and a re-test path; it is not deleted. No code, data, or workspace-file behavior changes — these are prompt-instruction and doc edits.

---

## Risks & Dependencies

- **Trigger reliability (R4):** editing `post-enricher`'s description, even only the tool clause, is a change to the entire triggering signal. Mitigation: change only the "Uses Perplexity…" clause, keep every trigger phrase verbatim, and run the skill-creator trigger-eval (PORTING-NOTES.md §4) before declaring done.
- **Content loss during mechanical edits:** the profile-template "Perplexity research → Web research" swap and the per-skill block rewrites must preserve surrounding content (parentheticals, named pages, "no keys" lines). Mitigation: token-level swap for the template; diff-review each skill block.
- **Dependency on the uncommitted 0.3.0 rewire:** this plan sits on top of the still-uncommitted script-removal change set on `refactor/standalone-content-skills`; sequence the commits so the version bump is coherent.

---

## Sources / Research

- Eval results that drive the decision: `content-workspace/eval-runs/research-backends/2026-06-29-distribution-vs-positioning/result.md` and `.../2026-06-29-distribution-vs-positioning-blind/result.md` (gitignored; the harness + verdict are the durable record).
- Current Perplexity mention surface (counts confirmed via grep): `post-enricher` and `content-audience-profiler` SKILL.md (~14 each), `lookalike-content` and `writing-style-analyzer` (~9 each), `profile-template.md` (9 data-source lines), plus `CLAUDE.md` (the two-path section), `README.md`, `CONTRIBUTING.md`.
- Reusable comparison protocol: `eval/research-backends/harness.md` + `result-template.md`.
