# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Claude Code plugin marketplace**, not an application. There is no build step, server, or test
runner. The deliverable is a set of **Agent Skills** (markdown instructions plus sibling reference
files) that Claude Code loads and executes. "Running" the code means installing the plugin into
Claude Code and prompting a skill into firing.

The catalog is `.claude-plugin/marketplace.json` (`pluginRoot: ./plugins`). Today it ships one
plugin, **`content-writing`** (`plugins/content-writing/`), a set of seven independent content skills.

## Working in this repo

Test changes by installing the local checkout into Claude Code and exercising the skill:

```text
/plugin marketplace add /path/to/skills_with_aura
/plugin install content-writing@skills-with-aura
```

Then prompt with realistic phrases **and near-miss phrases that should NOT trigger** — the
`description` frontmatter is the entire triggering signal, so trigger reliability is the main thing
to verify. The skill-creator skill has a trigger-eval loop for this.

Live research needs **no API keys and no scripts**. Each research skill uses Claude Code's built-in
**`WebSearch`** (find sources) and **`WebFetch`** (read the top results, and read specific pages — a
site, blog, or reviews page), and **verifies each cited claim on its own source page** before using
it. Skills are written to degrade gracefully when a source is absent.

## Architecture

### Built-in web research (one path)

Every skill that does live research uses Claude Code's **built-in web tools** — no MCP, no API keys,
no scripts:

| Need | How |
|---|---|
| Audience / topic / quote research | `WebSearch` to find sources → `WebFetch` the top 1-3 to read them → verify each cited claim on its page → synthesize + cite real URLs with an access date |
| Reading a specific page (site, blog, reviews) | `WebFetch` on the named URL |

`WebSearch` returns ranked links, not a synthesized answer, so the research step is a mini-procedure —
*search → fetch the strongest results → read → verify → synthesize → cite real URLs* — not a
one-liner; it keeps a "recent + verifiable" bar. `WebFetch` reads a known URL but does not
crawl/discover a site, so skills fetch known pages and ask the user for specific links when discovery
matters.

**Source-verification discipline (backend-agnostic):** the web can fabricate too — SEO/AI-generated
"case studies" with crisp fake percentages and no confirmable company. So every research step verifies
each cited stat/quote on its own source page before using it, prefers primary or reputable sources
over vendor/SEO blogs, and discards fabricated-looking claims. Each SKILL.md ends with an **"API
Integration Summary"** stating this and the rule: **use the built-in `WebSearch`/`WebFetch` and verify
each claim on its page — do NOT create alternative research scripts.** Honor that when editing a
skill's research step.

> **Power-user note (this file only — keep it out of the skills):** you *may* connect a Perplexity MCP
> to discover candidate sources faster, but it can return confident, citation-shaped claims that don't
> survive verification, so treat it as a discovery aid and still verify each claim on its real source
> page. Two blind eval runs put Perplexity head-to-head against the built-in path; the built-in path
> won both on verifiability, which is why the skills name only `WebSearch`/`WebFetch`.

### Source ingestion — transcripts are user-provided

The skills extract from **source text that already exists**; nothing in the plugin fetches a YouTube
transcript. Built-in `WebFetch`/`WebSearch` **can't reliably pull YouTube captions** — the watch page
is JS-rendered (markdown conversion strips it to nav/footer), the caption endpoints need signed tokens,
and the third-party transcript proxies block bots or are offline. So the portable, dependable path is **manual**:
the user pastes YouTube's own "Show transcript" panel, or drops a captions file into
`content-workspace/sources/`. The canonical how-to is
`plugins/content-writing/skills/talking-point-extractor/getting-a-transcript.md`.

> **Power-user note (this file only — keep it out of the skills' core path):** firecrawl, a web MCP, or
> `yt-dlp` fetch transcripts more reliably, but they are **optional extra installs** (some paid) and must
> never be assumed present — downstream users won't have them. Whatever the source, save it as text into
> `content-workspace/sources/` so the rest of the pipeline is identical for everyone. Never fabricate a
> transcript: if none can be obtained, give the user the manual steps and stop.

### Path discipline (the core portability rule)

Two namespaces, never mixed:

- **`${CLAUDE_PLUGIN_ROOT}/…`** — read-only files that ship with the plugin (reference corpora,
  templates, worked examples). Set by Claude Code to the install dir at runtime; **empty
  if a skill runs from a bare `.claude/skills/` checkout**, so local testing must go through the
  marketplace install above.
- **`content-workspace/…`** — all user inputs and generated outputs, created in the *user's* project
  (gitignored here). Never write into the plugin dir.

Never hardcode absolute or machine-specific paths in a skill.

### `content-workspace/` is the shared workspace

Skills are decoupled — they communicate through files under `content-workspace/`, not by calling
each other:

```
content-workspace/
├── profiles/        audience profiles + writing style cards — the shared read surface
├── samples/  sources/   user-dropped writing samples / transcripts (skill inputs)
├── talking-points/  content/  data/   generated outputs
```

The convention is **filename-substring discovery**: profile-reading skills scan
`content-workspace/profiles/` for `.md` files containing `"profile"` (audience) or `"style"`
(style card) in the name. Renaming the output files of `content-audience-profiler` /
`writing-style-analyzer` will silently break the other skills that look for them. Outputs are
namespaced to avoid false matches — e.g. `lookalike-content` writes its winning-content DNA to
`content-workspace/content/` (not `profiles/`), so it never collides with the audience-profile scan.

There is no fixed order and nothing auto-chains: each skill runs independently and the model (or
the user) picks what runs when. `content-audience-profiler` and `writing-style-analyzer` produce the
shared profile/style card the others can draw on; `talking-point-extractor`, `post-enricher`,
`linkedin-post-writer`, and `lookalike-content` each stand alone; `linkedin-post-writer` drafts a
LinkedIn post from those upstream outputs into `content-workspace/content/drafts/`, and
`linkedin-post-reviewer` reviews a draft directly (it uses no `content-workspace/`).

### Skill anatomy

Each skill is a folder under `plugins/content-writing/skills/<name>/` with a required `SKILL.md`
(YAML frontmatter `name`/`description`[/`argument-hint`] + an imperative body) and optional
sibling files (templates, HTML guides, references) that the body reads on demand. Skills that emit
client-facing artifacts produce **both `.md` and `.html`** (single-file, inline-CSS, print-friendly).

`linkedin-post-reviewer` is the outlier: it has no shared-profile dependency and reads no bundled
corpus — its full review methodology and voice card are embedded directly in its SKILL.md.

## Conventions when adding/editing skills

- `name` is kebab-case and **must match the folder name**.
- `description` is third-person, states *what + when* (trigger phrases) *and boundaries* (what it's
  NOT for) — this is the entire triggering signal, so make each boundary real and specific. Keep the
  body lean (< ~500 lines); push bulk into sibling files.
- A whole new plugin must be registered in the `plugins[]` array of
  `.claude-plugin/marketplace.json`; bump `version` in both `plugin.json` and `marketplace.json`
  when behavior changes.

## Licensing constraint (do not ignore)

Original skills/scripts are MIT (LICENSE). **Bundled third-party material is not.** The remaining
third-party-adjacent material is `plugins/content-writing/assets/examples/profiles/` — analytical
*profiles of* real public creators, shipped as worked examples (about real people; treat as
illustrative, not endorsements). Any newly bundled third-party reference must be recorded in NOTICE.md.
See NOTICE.md before touching `assets/`.

## Known rough edge

- Bundled example profiles live at `assets/examples/profiles/` but skills read from
  `content-workspace/profiles/` — a fresh user has none until they copy examples over.
