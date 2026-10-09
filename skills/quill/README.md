# Quill

An essay-writing companion for a note vault. It carries an essay through six phases (capture and select, develop, compose and listen, review and adjudicate, verify and hand off, publish and QA) while keeping the thinking the user's: the agent completes the user's thought and never adds its own. State lives in a companion note (status, wireframe, section directives, source-quality ledger, review ledger, history), so a session can stop and resume cold.

## Use it

Point your agent at `SKILL.md` and ask it to set the method up for your notes. Then bring a spark, a named essay, or a half-finished draft.

## What it assumes

- A markdown vault (Obsidian or similar) organized by the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system), with a note tool your agent can call, for example an MCP server over your vault.
- A style guide note of your own, and optionally an editorial direction note. Without them the skill falls back to a short set of defaults.
- A publishing workflow of your own for the final phase; this skill hands off to it and does not replace it.
- The `witness` skill, which Quill calls at wrap-up.

## License

CC BY 4.0, per the repository's [LICENSING.md](../../LICENSING.md). Attribute as: *Quill, by Laytheo (https://laytheo.com), licensed under CC BY 4.0.*
