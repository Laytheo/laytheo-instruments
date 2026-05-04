# small-group-guide

A Claude skill that turns a sermon transcript into a small group discussion
guide for a local church. Designed to preserve the preacher's voice rather
than flatten the sermon into a generic theological summary.

## What it does

Given a sermon transcript, this skill produces a markdown guide with:

- **This week's big idea** — the central claim of the sermon, in 1-2 sentences
- **Theological anchor points** — 2-4 substantive theological claims the sermon made
- **Discussion questions** — 3-6 open-ended questions that don't telegraph their own answers
- **Sermon walk-through** — a beat-by-beat retelling that preserves personality moments, named sources, and rhetorical force

The output markdown is structured so the companion `church-pdf-render` skill
can render it as a 2-page printed handout. You can also use the markdown
output on its own — it's just a regular markdown file.

## Install

1. Download this folder as a zip (or clone this repo and zip the folder yourself).
2. Open `church-context.md` and fill in the fields for your church. **Do this before first use.** The skill reads this file at runtime.
3. Upload the zip to Claude:
   - In claude.ai: Settings → Capabilities → Skills → "+" → "Create skill" → upload zip
   - In Claude Code: place the unzipped folder in your skills directory
4. Verify the skill is enabled.

## Use

Paste a sermon transcript into a Claude conversation, or upload it as a file.
Phrases like "the sermon," "Sunday's preaching," "this week's message," or
just pasting a transcript should trigger the skill automatically.

You can also explicitly invoke it: "Use the small-group-guide skill."

## Output

The skill writes a markdown file with this structure:

```markdown
# {Sermon title}
*Preached by {Speaker} on {Date} | {Scripture reference}*

## This week's big idea
...

## Theological anchor points
- ...

## Discussion questions
1. ...

## Sermon walk-through
...with *italic callouts* for personality moments and named quotes...
```

## Length target

The skill aims for ~900 words total, with a soft ceiling around 1,100. This
is the band that consistently fits a 2-page printed handout via the companion
`church-pdf-render` skill. If your sermon is unusually rich, the skill will
trim a discussion question or compress a walk-through paragraph rather than
overflow. Density beats comprehensiveness.

## Pairing with `church-pdf-render`

The output markdown is the input contract for the `church-pdf-render` skill,
which produces a branded PDF for your congregation. The two skills are
independent — you can use either without the other — but they're designed to
chain together cleanly.

## Limitations and honest framing

This skill was built and tuned for a Reformed-leaning evangelical Protestant
context with named-pastor preaching, sermon-as-exposition, and the specific
category of "small group guide" as a thing your church does. It will adapt to
adjacent traditions (Reformed Baptist, Anglican, Methodist, non-denominational
evangelical) with the right `church-context.md` calibration. It is not a
universal small group guide generator.

If your church has homilies rather than expositional sermons, no small groups
in the same sense, or a substantially different liturgical tradition, the
skill's underlying assumptions may need to be adjusted. Fork freely.

## License

[Add your license of choice. Anthropic's Agent Skills are an open standard.]
