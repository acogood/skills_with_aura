# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Claude Code plugin marketplace**, not an application. There is no build step, server, or test
runner. The deliverable is a set of **Agent Skills** (markdown + a few Python helpers) that Claude
Code loads and executes. "Running" the code means installing the plugin into Claude Code and
prompting a skill into firing.

The catalog is `.claude-plugin/marketplace.json` (`pluginRoot: ./plugins`). Today it ships one
plugin, **`content-writing`** (`plugins/content-writing/`), a set of six independent content skills.

## Working in this repo

Test changes by installing the local checkout into Claude Code and exercising the skill:

```text
/plugin marketplace add /path/to/skills_with_aura
/plugin install content-writing@skills-with-aura
```

Then prompt with realistic phrases **and near-miss phrases that should NOT trigger** — the
`description` frontmatter is the entire triggering signal, so trigger reliability is the main thing
to verify. The skill-creator skill has a trigger-eval loop for this (see PORTING-NOTES.md §4).

The three Python research helpers in `plugins/content-writing/scripts/` are standalone CLIs
(`requests` + optional `python-dotenv`), each reading one API key from the environment or a project
`.env`:

```bash
python3 scripts/perplexity_research.py --query "..." [--model sonar-pro] [--output f.json]   # PERPLEXITY_API_KEY
python3 scripts/firecrawl_scrape.py (--domain X | --url X) [--blog-only] [--max-posts N]      # FIRECRAWL_API_KEY
python3 scripts/xai_research.py --query "..." [--model grok-3-latest]                         # XAI_API_KEY
```

All three print JSON to stdout (status/errors to stderr) and `sys.exit(1)` on missing key or API
failure. Skills are written to degrade gracefully when a key/source is absent.

## Architecture

### Two-path research (MCP-first, script-fallback)

Every skill that does live research prefers an **MCP tool** when present and falls back to the
bundled Python script only when it isn't:

| Source | Primary | Fallback |
|---|---|---|
| Perplexity | `perplexity_ask` MCP tool | `scripts/perplexity_research.py` |
| Firecrawl | `scripts/firecrawl_scrape.py` | — |
| xAI / Grok | `scripts/xai_research.py` | — |

Each SKILL.md ends with an **"API Integration Summary"** stating this and a hard rule: **use the
named scripts; do NOT create alternative scripts.** Honor that — the scripts centralize auth,
retries, and error handling. When editing a skill's research step, route through these, don't inline
new ones.

### Path discipline (the core portability rule)

Two namespaces, never mixed:

- **`${CLAUDE_PLUGIN_ROOT}/…`** — read-only files that ship with the plugin (scripts, reference
  corpora, templates, worked examples). Set by Claude Code to the install dir at runtime; **empty
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
shared profile/style card the others can draw on; `talking-point-extractor`, `post-enricher`, and
`lookalike-content` each stand alone; `linkedin-post-reviewer` reviews a draft directly (it uses no
`content-workspace/`).

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
See NOTICE.md and PORTING-NOTES.md before touching `assets/`.

## Known rough edges (from PORTING-NOTES.md)

- Bundled example profiles live at `assets/examples/profiles/` but skills read from
  `content-workspace/profiles/` — a fresh user has none until they copy examples over.
