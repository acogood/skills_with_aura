# Porting Notes

How these skills were extracted from their origin repo into this standalone plugin, and what
to refine. Internal scratch — safe to delete once the skills are settled.

## Provenance

Skills, scripts, and assets were copied from the private `ai-cmo` repo's
`kantent_podjehal/` tree on 2026-06-26. The six skills are verbatim copies except for the
path rewrites below.

## Path rewrites applied

To make the skills portable (they previously assumed the origin repo's directory layout):

| Original | Rewritten to | Why |
|---|---|---|
| `kantent_podjehal/scripts/*.py` | `${CLAUDE_PLUGIN_ROOT}/scripts/*.py` | Helper scripts now ship with the plugin |
| `…/kantent_podjehal/content/linkedin-comeback/…` (incl. absolute paths in `lara-acosta-reviewer`) | `${CLAUDE_PLUGIN_ROOT}/assets/linkedin-comeback/…` | Lara course + references bundled as read-only assets |
| `kantent_podjehal/<everything else>/` | `content-workspace/<…>/` | User inputs/outputs now live in a neutral working dir in the user's project |

`${CLAUDE_PLUGIN_ROOT}` is set by Claude Code to the plugin's install dir at runtime.

## Known rough edges to refine

1. **Example profiles discoverability.** Bundled examples live at
   `assets/examples/profiles/`, but skills read user profiles from `content-workspace/profiles/`.
   A fresh user has none until they copy examples over. Consider adding an explicit
   "if no profile in `content-workspace/profiles/`, offer the bundled examples in
   `${CLAUDE_PLUGIN_ROOT}/assets/examples/profiles/`" fallback to the profile-reading skills.
2. **`talking-point-extractor` still references AI-CMO workspace paths** (`ai-cmo-workspace/…`)
   in its "where to look for source files" section — harmless leftover from the origin repo;
   trim or generalize for a public audience.
3. **`${CLAUDE_PLUGIN_ROOT}` is only set when installed as a plugin.** If you run a skill from
   a bare `.claude/skills/` checkout (not installed via the marketplace), the variable is
   empty. Install via the marketplace for local testing.
4. **Eval the `description` fields.** Run the trigger eval loop (skill-creator) to confirm each
   description fires on the right prompts and ignores near-misses before you promote this widely.
