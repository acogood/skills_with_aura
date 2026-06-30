# Skills with Aura ✨

A small set of [Claude Code](https://code.claude.com) skills for marketers and content people:
research your audience, capture your voice, then turn raw material into LinkedIn (and long-form)
posts — drafted, enriched, and reviewed. No API keys, no setup beyond Claude Code.

## Use a skill

Every skill is a plain folder under [`skills/`](skills/). Install one by copying its folder into
your Claude Code skills directory:

```bash
git clone https://github.com/acogood/skills_with_aura
cp -r skills_with_aura/skills/linkedin-post-writer ~/.claude/skills/   # available everywhere
# …or scope it to one project:  cp -r skills_with_aura/skills/<name> .claude/skills/
```

Then just ask Claude Code for what you want — *"draft a LinkedIn post from these notes"* — and it
runs the matching skill, or name the skill directly. Take as many as you like.

## The skills — a suggested order

Run them in whatever order suits you; this is just the flow that tends to work. Each skill saves its
output to your machine, and the later skills read those files.

**Set up once — your voice & audience**

1. **writing-style-analyzer** — feed it your best writing; it saves a reusable **Style Card**.
2. **content-audience-profiler** — builds a research-backed **profile of who you're writing for**.

**Per post**

3. **talking-point-extractor** — turn a transcript, article, or notes into post-ready angles.
4. **post-enricher** — add a story, example, or verifiable stat so a point actually lands.
5. **linkedin-post-writer** — draft the post in 2–3 variants, matched to your Style Card + audience.
6. **linkedin-post-reviewer** — a blunt, opinionated critique against what actually performs, before you publish.

**Anytime**

7. **lookalike-content** — mine a pile of winning posts for what's working and generate fresh lookalike ideas.

## Where your work is saved

Skills read and write a `content-workspace/` folder in your current project — everything stays on
your machine:

```
content-workspace/
├── profiles/        audience profiles + style cards (shared across skills)
├── samples/ sources/        your inputs (writing samples, transcripts/articles)
└── talking-points/ content/ data/        generated angles, drafts, ideas
```

For a video source, paste YouTube's **Show transcript** panel or drop a captions file into
`content-workspace/sources/` — Claude can't reliably fetch captions on its own. See
[getting-a-transcript.md](skills/talking-point-extractor/getting-a-transcript.md).

## Contributing

A skill is a folder under `skills/` with a `SKILL.md`: YAML frontmatter (`name` matching the folder,
plus a `description` that says what it does and when to use it) followed by the instruction body.
Add or sharpen one and open a PR.

## License

[MIT](LICENSE).
