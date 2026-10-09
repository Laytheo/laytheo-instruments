# OTS Notes

A skill for creating and editing single notes in a vault organized by the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system) (OTS). The method is defended elsewhere; this skill executes it, one note at a time, with a duplicate check first and a body proportioned to what the user actually knows.

## Use it

Point your agent at `SKILL.md` and ask it to set the method up for your notes. It will read `TAXONOMY.md` (the method reference: six closed root types, stub rules, templates, association discipline, body shape) and then apply it whenever you say "make a note for X."

## What it assumes

- A markdown vault (Obsidian or similar) with YAML frontmatter and wikilinks.
- A note tool your agent can call, for example an MCP server over your vault: search, list, read, create, update.

## Files

- `SKILL.md`: the workflow for live note work.
- `TAXONOMY.md`: the method reference.

## License

CC BY 4.0, per the repository's [LICENSING.md](../../LICENSING.md). Attribute as: *OTS Notes, by Laytheo (https://laytheo.com), licensed under CC BY 4.0.*
