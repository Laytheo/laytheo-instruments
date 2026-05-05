# OTS Stub Skill

A [Claude skill](https://www.anthropic.com/news/skills) that produces [Obsidian](https://obsidian.md) vault stubs conforming to the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system).

The OTS itself is a method, defended at length on laytheo.com. This skill is a companion tool: it does not argue for the method, it executes it. If you've already chosen to run an OTS-shaped vault, this skill produces the stubs.

## What it does

Hand it a name, and it returns a markdown code block ready to paste into Obsidian:

- A person, real or historical
- A place or institution
- A work (book, film, album, software, essay)
- An event
- An idea, concept, doctrine, or instrument
- A journal entry template

Each stub follows the OTS schema: type and subtype as wikilinks, the right field set for that type, ISO date for `created`, and atomic-note discipline (one note, one entity). Public, historical, and intellectual entities are verified against web sources where possible. Personal acquaintances (friends, family, private contacts) are out of scope; generate those from Obsidian templates instead.

## Installation

Drop the skill folder into your Claude skills directory. On Linux and macOS:

```
~/.claude/skills/ots-stubs/
```

The skill is a single `SKILL.md` file. No dependencies, no scripts.

## Usage

Invoke it the same way you invoke any skill. Examples:

- "Stub a Person note for J.R.R. Tolkien"
- "Make me an Idea note for subcreation"
- "Create an Obsidian entry for the Council of Nicaea"
- "I want to add Tolkien to my vault"

The skill returns a markdown code block. Paste it into Obsidian, save the file, done.

## What it does not do

- It does not invent new root types. The six are closed.
- It does not write Journal bodies on your behalf. The Journal type records your own dated witness; only you can produce its content.
- It does not include personal vault conventions (custom subtypes, family naming, CSS extensions). The skill ships the universal method.
- It does not produce essays or long-form notes about entities. Stubs are the unit of work.
- It does not generate stubs for personal acquaintances. Friends, family, and private contacts should be generated from Obsidian templates.

## License

CC0. Use it, fork it, modify it, ship your own version. No attribution required.

## See also

- [Ontological Type System](https://laytheo.com/instruments/ontological-type-system) for the method itself
- [OTS Discipline Pack](https://laytheo.com/instruments/ots-discipline-pack) for a foundational set of 45 discipline stubs to seed graph density
