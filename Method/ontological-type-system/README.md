# The Ontological Type System

A classical realist method for organizing a personal knowledge vault in Obsidian. Six root types, atomic notes, dense semantic linking, and the daily journal as narrative spine.

This repository contains the practical reference for the system: the schema, the templates, worked examples, and an optional Claude skill for generating note stubs. The philosophical case for the method lives in a longer essay at [laytheo.com/instruments/ontological-type-system](https://laytheo.com/instruments/ontological-type-system). If you have not read that essay, start there. The system is not really about software; it is about a posture toward reality, and the schema only makes sense once the posture is established.

## The Posture in One Paragraph

Notes in your vault should represent things that exist. Not arbitrary mental categories, not moods, not projects, not "topics," but real entities: real people, real places, real artifacts, real happenings, real ideas, and your own dated witness of all of them. The vault is a partial, finite, humble map of a fragment of reality at the resolution you can attend to. This commitment, called classical realism, is the foundation of the system. If you adopt the schema without the posture, the system will dissolve under the pressure of your actual life. If you adopt the posture, the schema will feel inevitable.

## The Six Types

The system organizes every note under one of six root types. The set is closed by design.

| Type | Domain |
|------|--------|
| `[[Person]]` | Any real human, living or dead, biblical, historical, contemporary, or personal. |
| `[[Place]]` | A location or institution. Both physical places and organizational entities. |
| `[[Work]]` | Any artifact made by a person or group. Books, songs, films, software, sermons. |
| `[[Event]]` | Anything that happened, at a time, to participants, in a place. |
| `[[Idea]]` | An abstraction, concept, phenomenon, or instrument of thought. |
| `[[Journal]]` | One's own dated witness of reality. The daily note. |

Subtypes are an open frontier. If you find yourself making many notes of a particular flavor under an existing type, add a subtype freely. Composition under Work. Doctrine under Idea. Battle under Event. The default templates in this repo include three: `dream` (Journal), `lexeme` (Idea), and `sermon` (Event). Add your own.

Types are closed by design. The six root types encode a deliberate posture, and adding a seventh changes what the vault is for. Most candidates that come to mind on first encounter, like Project or Topic or Goal, fail to name a kind of thing that does not reduce to one of the six. Before adding a seventh type, make sure the candidate truly names a kind of thing that does not reduce to any of the existing six. The answer is almost always no.

## The Three Load-Bearing Properties

Every note has frontmatter. Three properties carry almost all of the system's weight.

**`type`** holds a wikilink to one of the six root types. Because it is a wikilink, every Person note backlinks to `[[Person]]`, every Idea note backlinks to `[[Idea]]`, and so on. The root type notes thus become live indices, populated automatically by the act of filing. The ontology is the index.

**`subtype`** holds a wikilink to a more specific category, or is left blank if no subtype applies. Same mechanism: subtypes accumulate their members through backlinks.

**`created`** holds the note's creation date in ISO format (`YYYY-MM-DD`). File system metadata is unreliable across syncs and backups; storing the date in the note itself ensures it survives.

Other fields are template-specific and may be empty. A historical figure's Person note will leave most personal contact fields blank. A friend's Person note will leave most historical fields blank. Empty frontmatter fields cost almost nothing.

## A Worked Example

To show how the six types interlock, here is a single cluster of notes built around Tolkien and *The Lord of the Rings*. One note for each type, all linked to one another through wikilinks.

A **Person** note for Tolkien:

```yaml
---
type: "[[Person]]"
subtype: "[[Author]]"
alternate_names:
  - John Ronald Reuel Tolkien
  - JRR Tolkien
birth_date: 1892-01-03
death_date: 1973-09-02
nationality: British
roles:
  - novelist
  - philologist
  - professor
associations:
  - "[[Oxford]]"
  - "[[The Inklings]]"
  - "[[Subcreation]]"
created: 2026-04-27
---
```

A **Work** note for *The Lord of the Rings*:

```yaml
---
type: "[[Work]]"
subtype: "[[Novel]]"
title: The Lord of the Rings
creator:
  - "[[Tolkien]]"
publication_year: 1954
associations:
  - "[[The Hobbit]]"
  - "[[The Silmarillion]]"
  - "[[Subcreation]]"
created: 2026-04-27
---
```

A **Place** note for Oxford:

```yaml
---
type: "[[Place]]"
subtype: "[[Location]]"
aliases: []
city: Oxford
country: England
region: Oxfordshire
associations:
  - "[[University of Oxford]]"
  - "[[The Inklings]]"
  - "[[Tolkien]]"
created: 2026-04-27
---
```

An **Event** note for the publication of the first volume:

```yaml
---
type: "[[Event]]"
subtype: "[[Publication]]"
date_start: 1954-07-29
date_end: 1954-07-29
era: 20th century
place: "[[London]]"
participants:
  - "[[Tolkien]]"
  - "[[Allen and Unwin]]"
associations:
  - "[[The Lord of the Rings]]"
  - "[[The Fellowship of the Ring]]"
created: 2026-04-27
---
```

An **Idea** note for subcreation:

```yaml
---
type: "[[Idea]]"
subtype: "[[Concept]]"
name: Subcreation
definition: "The artist's act of fashioning a secondary world that is internally consistent and meaningful, participating in but distinct from the primary creation."
aliases: []
key_people:
  - "[[Tolkien]]"
associations:
  - "[[On Fairy-Stories]]"
  - "[[Mythopoeia]]"
  - "[[The Lord of the Rings]]"
state: Seed
created: 2026-04-27
---
```

A **Journal** entry that weaves several of these together:

```markdown
---
type: "[[Journal]]"
subtype: 
created: 2026-04-27
---

Finished a reread of [[The Lord of the Rings]]. What stands out this time is how thoroughly [[Tolkien]] commits to [[Subcreation]] as a working principle: the languages, the genealogies, the maps. Nothing is decorative. Made me want to revisit [[On Fairy-Stories]] for the theory.
```

Six notes, fourteen wikilinks, and the system has done its work. Tolkien now backlinks to today, the novel now backlinks to today, subcreation now backlinks to today. The Person note for Tolkien backlinks from the Work note, the Place note, the Event note, and the Idea note. Two years from now, when you wonder when you last read *The Lord of the Rings*, or what you were thinking about Tolkien in spring 2026, the answer is one click away.

This is the system in miniature. The same pattern, repeated thousands of times over years, is a vault.

## The Daily Practice

The journal is structurally different from the other five types. The five entity types describe *what is*. The journal describes *what happened, when, and to whom*. Every wikilinked entity in a journal entry creates a backlink from that entity's note to the day. Over time, the journal becomes the time-indexed witness layer over the entity graph: a record of a life lived attentively, with the entities of that life linked into the days they touched it.

The discipline of daily journaling is not optional for the system to work as designed. Without it, the vault is a static encyclopedia. With it, the vault becomes a record. Even a single sentence per day, with a few wikilinks, is enough.

## The Production Layer

Two pipelines, both targeting the same canonical schema.

**Manual templates.** For personal entities (people you know, places you go, events from your own life), use Obsidian's template feature directly. Trigger a template, fill in the fields, save. This keeps personal content entirely local. No AI tool ever sees your friend's note, your family's note, the note about a private conversation. The templates in `templates/` are ready to drop into your vault's templates folder.

**AI-assisted stubs.** For public or historical entities (biblical figures, theologians, philosophical concepts, published works, historical events), an AI assistant can produce schema-conformant stubs in seconds. The schema is the contract; the AI fills in the template you designed. This repository includes a [Claude skill](./SKILL.md) that teaches Claude to produce stubs in the system's format. Adapt it for whatever AI tool you prefer, or skip this pipeline entirely and use templates throughout.

The split is principled. Personal content stays local for privacy. Public content gets accelerated for speed. The schema enforces consistency across both pipelines, so the AI-generated note and the manually-templated note are interchangeable in the graph.

## Optional Disciplines

Some elements of a working vault are not part of the core system. They are optional and depend on the practitioner's temperament.

**The `state` field** holds one of `Seed`, `Developing`, or `Stable`. The intent is that you periodically query for Seed notes and revisit them. If you are the sort of person who will actually do this, the field earns its keep. If you are not, it is dead metadata. Be honest about your own habits before adopting it.

**General principle**: do not add metadata you will not query. Every field in your frontmatter is a small tax on every note you create. Fields that pay rent are fields you actively use to find, group, or reason about notes. Fields that do not pay rent should be cut.

## What Is in This Repository

```
ontological-type-system/
├── README.md                # This file
├── SKILL.md                 # Claude skill for AI-assisted stubs
├── templates/               # Obsidian templates for manual use
│   ├── person.md
│   ├── place.md
│   ├── work.md
│   ├── event.md
│   ├── idea.md
│   ├── journal.md
│   ├── dream.md             # journal subtype
│   ├── lexeme.md            # idea subtype
│   └── sermon.md            # event subtype
├── examples/                # One worked example per type
│   ├── person-tolkien.md
│   ├── place-oxford.md
│   ├── work-the-lord-of-the-rings.md
│   ├── event-publication-fellowship.md
│   ├── idea-subcreation.md
│   └── journal-sample.md
└── LICENSE
```

The templates ship with reasonable defaults. Treat them as starting points, not as canon. Customize the field lists for your own life. The closed parts of the system are the six types and the posture; the open parts are everything else.

## Adopting the System

If you want to try this method, here is a reasonable order of operations.

1. Read the [essay at laytheo.com](https://laytheo.com/instruments/ontological-type-system). The schema will not survive contact with your life if the posture is not in place.
2. Set up a fresh Obsidian vault, or designate a section of an existing one for this experiment.
3. Copy the templates from `templates/` into your vault's templates folder. Customize the field lists if you already know what you want to track.
4. Make six notes by hand: one of each type. Use the examples in `examples/` as references. Do not skip Journal; start your daily note today.
5. Use the system for two weeks before adding any subtypes or optional fields. Let the friction of actual use teach you what is missing and what is excess.
6. If the system is serving you, formalize it: add subtypes you have discovered you need, customize templates, optionally add the `state` field if you will use it.
7. If you want AI-assisted stubs for public entities, install the [Claude skill](./SKILL.md) or adapt it for your tool of choice.

The method takes about two weeks to feel natural and several months to start forming the practitioner. There is no shortcut. The vault is a slow instrument.

## Further Reading

- The original essay: [Ontological Type System](https://laytheo.com/instruments/ontological-type-system) at laytheo.com
- Other instruments and writing: [laytheo.com](https://laytheo.com)

## License

The prose and methodology in this repository are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The templates and skill files are licensed under [MIT](./LICENSE). Adapt freely. Attribution to laytheo.com is appreciated.

## A Note on Origins

This system was developed and refined over several years of personal use, and is offered to the commons in the spirit that good tools should circulate. It is published under the Laytheo pen name; further writing on theology, technology, and related topics lives at [laytheo.com](https://laytheo.com). If you adopt the system, modify it, or improve it, the author would be glad to hear about it.
