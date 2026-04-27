# sermon-guide

A Claude skill that turns a sermon transcript into a small group discussion guide.

## Why this exists

Most AI-generated sermon notes flatten the sermon. They read like a theological summary of *what the pastor talked about* rather than a guide that helps a small group re-encounter the actual sermon. The pastor's anecdote about his neighbor, the half-quoted line from a theologian, the joke that landed, the moment the room got quiet: these get smoothed away by default, even though they are exactly what people remember mid-week and exactly what makes a sermon *this* sermon.

This skill is tuned to do the opposite. It anchors itself in the actual flow and texture of the preaching, then derives the theology and discussion questions from there. Personality moments, named non-Scripture sources, and Scripture cross-references are each preserved differently, so a leader can scan the guide and find what they need.

## What it produces

A Markdown guide with four sections:

1. **Big idea** (1-2 sentences)
2. **Theological anchor points** (2-4 concrete claims)
3. **Discussion questions** (3-6, sermon-specific, no filler)
4. **Sermon walk-through** (4-8 short paragraphs tracing the actual sermon arc, with inline callouts for personality moments and named sources, and parenthetical Scripture citations)

Target length is 600-800 words. Hard cap at 800.

## Who it's for

Small group, community group, life group, or home group leaders who need a guide to facilitate discussion during the week. The output is designed to be scanned on a phone before group starts and used as a tool, not read as a book report.

## How to use it

1. Drop the `sermon-guide/` directory into your Claude skills folder (or wherever your environment loads skills from).
2. Edit the **Church context** section of `SKILL.md` to match your congregation. This is where you tell the skill what tradition you're in, who your regular preachers are, and what vocabulary your church uses. Without this, the output will drift toward a generic register that could come from any tradition. See the next section for what to fill in.
3. Provide a sermon transcript to Claude. The skill should trigger automatically; if not, you can ask Claude to "use the sermon-guide skill" or "generate a small group guide for this sermon."
4. The transcript can be rough (auto-generated, no punctuation, missing speaker labels). The skill is built to work with messy input.

## Configuring church context

Open `SKILL.md` and find the section titled **Church context**. Replace the example values with your own:

- **Tradition**: e.g., Reformed Presbyterian, non-denominational evangelical, Anglican, Southern Baptist, Pentecostal, etc. Be specific enough that the model can calibrate theological framing.
- **Primary teaching pastor and other regular preachers**: names so the skill can attribute correctly when the transcript is ambiguous.
- **Congregational vocabulary**: phrases your church actually uses ("the gospel," "covenant community," "the Word," "doing life together," etc.). The skill will match this register.
- **Theological frame**: a few short notes on emphases your tradition cares about (sacramental, charismatic, expository, missional, etc.).

The more specific you make this section, the less generic the output will be.

## Status

Early, working draft. Originally tuned and tested for a single congregation. Pending evaluation across other congregations and feedback from actual small group leaders. Issues, forks, and pull requests welcome.

## License

Dual-licensed. Prose and methodology under [CC BY 4.0](../../LICENSE-CC-BY-4.0); code and templates under [MIT](../../LICENSE). See [`LICENSING.md`](../../LICENSING.md) for the boundary and the full text of each license.

When using or adapting prose or methodology from this project, attribute as follows:

> *sermon-guide, by Laytheo (https://laytheo.com), licensed under CC BY 4.0.*

If the work has been modified, indicate that changes were made.
