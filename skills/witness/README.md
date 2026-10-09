# Witness

A skill for keeping a dated record of what you meet, in a note vault organized by the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system) (OTS). Something you watched, read, heard, or remembered lands in two places: the thing's own note (what it is) and your daily note (what it did to you), joined by a link so the thing's page gathers every time you met it.

It has four modes: **Enrich** (build notes for the empty links in an entry you wrote), **Witness X** (log a thing with your own phrase), **Discourse** (talk it through first), and **Memory** (record a remembered event as an Event note, with the reflection in today's daily note). The agent does the clerical work; the line is always yours.

## Use it

Point your agent at `SKILL.md` and ask it to set the method up for your notes. Then say things like "witness this," "let's talk about it for my witness," or "help me record this memory."

## What it assumes

- A markdown vault (Obsidian or similar) with YAML frontmatter, wikilinks, and a daily note.
- A note tool your agent can call, for example an MCP server over your vault: search, list, read, create, update, and ideally an append-to-today operation.
- The `ots-notes` skill, which builds the entity notes.

## License

CC BY 4.0, per the repository's [LICENSING.md](../../LICENSING.md). Attribute as: *Witness, by Laytheo (https://laytheo.com), licensed under CC BY 4.0.*
