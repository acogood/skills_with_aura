# Skills with Aura ✨

**English** · [Русский](README.ru.md)

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
4. **talking-point-curator** — pick the angles that fit your chosen lane and rank them into a post queue.
5. **post-enricher** — add a story, example, or verifiable stat so a point actually lands.
6. **linkedin-post-writer** — draft the post in 2–3 variants, matched to your Style Card + audience.
7. **linkedin-post-reviewer** — a blunt, opinionated critique against what actually performs, before you publish.

   **Make it yours before you publish.** Don't ship AI slop — read the post end to end and rewrite the flat parts in your own voice: keep your punchy hooks (they drive the reach), cut the AI tells. For an extra pass, the external **[humanizer](https://github.com/blader/humanizer)** skill (`npx skills add blader/humanizer`) strips signs of AI writing — run it *partially*, so it removes tells without smoothing away your hooks.

8. **linkedin-final-check** — the last gate on the one variant you picked: a SHIP/HOLD verdict that it's publish-ready and free of AI slop.
9. **linkedin-meme-picker** — once a post clears the final check, turn it into a scroll-stopping visual: maps your hook and the sacred cow you poke to a fitting memegen.link template, verifies the image actually renders, and hands back a meme board (a lead plus alts).

**Anytime**

10. **lookalike-content** — mine a pile of winning posts for what's working and generate fresh lookalike ideas.

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
