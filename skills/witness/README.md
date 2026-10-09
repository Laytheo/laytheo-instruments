# Witness

A skill for keeping a dated record of what you meet, in a note vault organized by the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system) (OTS). Something you watched, read, heard, or remembered lands in two places: the thing's own note (what it is) and your daily note (what it did to you), joined by a link so the thing's page gathers every time you met it.

It has four modes: **Enrich** (build notes for the empty links in an entry you wrote), **Witness X** (log a thing with your own phrase), **Discourse** (talk it through first), and **Memory** (record a remembered event as an Event note, with the reflection in today's daily note). The agent does the clerical work; the line is always yours.

## Make it yours

This is a starting point, not an install. It is one person's working method, written for an AI agent, and it is meant to be adapted. Give `SKILL.md` to your own agent and ask it to fit the method to you. Have it interview you first, on two fronts: the technical setup (where your notes live, and what tools it has to read and write them) and the method itself (how you actually keep notes, what you want to remember, and which parts of this practice fit you and which do not). Then let it rewrite the skill around your answers.

Once it is yours, say things like "witness this," "let's talk about it for my witness," or "help me record this memory."

## What it assumes

- A markdown vault (Obsidian or similar) with YAML frontmatter, wikilinks, and a daily note.
- A note tool your agent can call, for example an MCP server over your vault: search, list, read, create, update, and ideally an append-to-today operation.
- The `ots-notes` skill, which builds the entity notes.

## License

CC BY 4.0, per the repository's [LICENSING.md](../../LICENSING.md). Attribute as: *Witness, by Laytheo (https://laytheo.com), licensed under CC BY 4.0.*
