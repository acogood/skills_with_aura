# Contributing

Thanks for wanting to add to **Skills with Aura**. This repo is a Claude Code plugin
marketplace — contributions are usually a new skill, or an improvement to an existing one.

## Add or improve a skill

Skills live at `plugins/content-writing/skills/<skill-name>/`. Each is a folder with a
`SKILL.md` plus optional supporting files:

```
<skill-name>/
├── SKILL.md          # required — frontmatter + instructions
├── references/       # docs/rubrics loaded on demand
├── scripts/          # executable helpers (run, not read)
└── assets/           # templates the skill writes from
```

### `SKILL.md` frontmatter

```yaml
---
name: my-skill                 # kebab-case, matches the folder name
description: "Third-person 'what + when'. Name the trigger phrases and the boundaries
  (what it's NOT for). This string is the entire triggering signal — keep it specific."
---
```

Rules that keep triggering reliable (per Anthropic's skill-authoring guidance):

1. **Third person** in `description` ("Generates…", not "I generate…").
2. **What + when** — state what it does *and* the contexts/phrases that should trigger it.
3. **Boundaries** — say what it is *not* for to avoid false triggers.
4. **Imperative body** — instructions use "Read…", "Run…", "Write…".
5. Keep the body lean (aim < 500 lines); push bulk into `references/`.

### Portable paths — important

Skills must not hardcode machine-specific paths. Use these conventions:

- **Bundled files** (reference corpora, templates, HTML guides that ship with the plugin):
  reference them via `${CLAUDE_PLUGIN_ROOT}/…` — e.g.
  `Read ${CLAUDE_PLUGIN_ROOT}/skills/<skill-name>/template.md`.
- **User inputs & outputs** (profiles, sources, generated content): read/write under
  `content-workspace/…` in the user's project, never inside the plugin install dir.

For **live web research**, don't bundle a key-reading script — use the built-in `WebSearch` /
`WebFetch` tools, which need no API keys, and verify each cited claim on its own source page before
using it.

## Register a new plugin

If you add a whole new plugin (not just a skill), add it to the `plugins[]` array in
`.claude-plugin/marketplace.json` with its `name`, `source` (folder under `./plugins`),
`description`, and `version`.

## Test locally before a PR

Add the marketplace from your local checkout and install:

```text
/plugin marketplace add /path/to/skills_with_aura
/plugin install content-writing@skills-with-aura
```

Then exercise the skill with a few realistic prompts — including near-miss prompts that
should *not* trigger it.

## PR checklist

- [ ] `SKILL.md` has valid frontmatter (`name` matches folder, `description` follows the rules above).
- [ ] No hardcoded absolute or machine-specific paths (`${CLAUDE_PLUGIN_ROOT}` / `content-workspace/`).
- [ ] No secrets, API keys, or private endpoints committed.
- [ ] New third-party reference material is noted in [NOTICE.md](NOTICE.md).
- [ ] Version bumped in `plugin.json` / `marketplace.json` if behavior changed.
