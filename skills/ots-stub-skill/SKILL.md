---
name: ontological-type-system
description: Generate Obsidian vault note stubs that conform to the Ontological Type System, a classical realist method organized around six closed root types (Person, Place, Work, Event, Idea, Journal). Use this skill whenever the user asks for a stub, vault note, Obsidian note, or schema-conformant note for any entity (a historical figure, a book, a place, an event, a concept, a journal entry), or when they reference "OTS," "ontological typing," or paste a wikilink like [[Person]] and ask Claude to fill in a note. Trigger even when the user does not say "stub" explicitly: phrases like "make me a note for Augustine," "create an Obsidian entry for the Council of Nicaea," or "I want to add Tolkien to my vault" all warrant this skill. The output is always a markdown code block ready to paste into Obsidian.
---

# Ontological Type System

This skill produces Obsidian vault notes that conform to the Ontological Type System, a classical realist method for personal knowledge management. The full methodology is described at [laytheo.com/instruments/ontological-type-system](https://laytheo.com/instruments/ontological-type-system) and in the [method README](../../methods/ontological-type-system/README.md). Read those before adopting the method itself; this skill assumes the user has already chosen to use the system and just needs help producing notes quickly.

## What the system commits to

The user's vault is built on a classical realist commitment: notes represent things that exist in reality, not arbitrary mental categories. Every note the skill produces should reflect this. A Person note is a note about a real human. A Work note is a note about a real artifact. A Place note is a note about a real location or institution. The skill's job is to produce stubs that respect this posture; treat each stub as the user's first careful act of attention to the entity in question.

The system is organized around six closed root types:

- **Person**: any real human, living or dead, biblical, historical, contemporary, or personal
- **Place**: a location or institution (both physical places and organizational entities)
- **Work**: any artifact made by a person or group (books, songs, films, software, sermons, essays)
- **Event**: anything that happened, at a time, to participants, in a place
- **Idea**: an abstraction, concept, phenomenon, or instrument of thought
- **Journal**: one's own dated witness of reality (the daily note)

Subtypes are open: the user may add subtypes freely under any root type. Types are closed: do not invent a seventh type. If a request seems to demand one, the right move is to find which of the six it actually fits, not to propose a new type.

## Core output rules

Every stub the skill produces follows these rules. They are not optional.

**Output a markdown code block.** The user will paste the output directly into an Obsidian note. Do not surround the stub with prose, explanations, or commentary unless the user explicitly asks for them. A clean code block is the default.

**Frontmatter first, then body.** Every note begins with a YAML frontmatter block delimited by `---`. The body, if any, follows below the closing `---`. For most stubs, the body is short or empty; the schema does the work, not the prose.

**Type and subtype as wikilinks.** The `type` field is always one of `"[[Person]]"`, `"[[Place]]"`, `"[[Work]]"`, `"[[Event]]"`, `"[[Idea]]"`, or `"[[Journal]]"`. The `subtype` field is a wikilink to a more specific category, or left blank. Wikilink values must be quoted strings in YAML.

**Three required fields.** Every note has `type`, `subtype` (may be blank), and `created` (ISO date `YYYY-MM-DD`). Use today's date for `created` unless the user specifies otherwise.

**Atomic notes.** One note, one entity. Do not pack multiple entities into a single stub. If the user asks for "Tolkien and his works," produce separate stubs for Tolkien and for each work, not one combined note.

**No em dashes.** Do not use em dashes (—) or double hyphens (`--`) anywhere in the stub. Use commas, semicolons, colons, parentheses, or sentence breaks instead.

**Empty fields are fine.** When a field doesn't apply or the answer is unknown, leave it blank rather than fabricating. A historical figure's `email` field stays empty. An obscure work's `publication_year` stays empty if uncertain. The schema tolerates blanks; it does not tolerate hallucinations.

**Wikilink only entities of independent note.** Relational list fields (`associations`, `spouses`, `partners`, `children`, `parents`, `participants`, `key_people`, `creator`, etc.) hold references to other entities. Only wikilink an entity if it plausibly merits its own note in the user's vault, meaning a person, place, or work of independent public, historical, or intellectual significance. Private family members (minor children, non-public parents and spouses, friends not otherwise notable) stay as plain text strings. The vault is built on real connections, not orphan stubs; a wikilink is a promise that the target is worth a note. When in doubt, default to plain text and let the user upgrade to a wikilink later. The same logic governs `associations`: wikilink real entities the user is likely to encounter, not abstract topics.

## The six type templates

These are the default templates. The user may customize their own field lists; if they have shared their custom schema, use that instead. Otherwise, default to these.

### Person

```yaml
---
type: "[[Person]]"
subtype: 
alternate_names: []
birth_date: 
death_date: 
nationality: 
roles: []
spouses: []
partners: []
children: []
parents: []
associations: []
created: YYYY-MM-DD
---
```

Notes on Person: `subtype` examples include `"[[Theologian]]"`, `"[[Philosopher]]"`, `"[[Author]]"`, `"[[Scientist]]"`. `roles` is a list of plain strings (lowercase, e.g., `bishop`, `novelist`, `professor`). `spouses`, `partners`, `children`, `parents` reference other people; wikilink them only when the related person is of independent note (a published author, a public figure, a historically documented relation), and use plain text otherwise. Private family members (minor children, non-public parents and spouses) stay as plain strings. Use `partners` for non-marital relationships. Omit fields entirely (don't just leave blank) if they would never apply to the entity in question (e.g., omit `spouses` for someone who never married, rather than leaving it as `[]`).

### Place

```yaml
---
type: "[[Place]]"
subtype: 
aliases: []
address: 
city: 
country: 
region: 
associations: []
created: YYYY-MM-DD
---
```

Notes on Place: `subtype` is typically `"[[Location]]"` or `"[[Institution]]"`. Use `Location` for physical places (cities, regions, geographic features, buildings). Use `Institution` for organizational entities (churches, universities, governments, companies). For institutions, fill `address`/`city`/`country` if the institution has a primary location.

### Work

```yaml
---
type: "[[Work]]"
subtype: 
title: 
parent_work: 
creator: []
publication_year: 
associations: []
created: YYYY-MM-DD
---
```

Notes on Work: `subtype` examples include `"[[Book]]"`, `"[[Novel]]"`, `"[[Film]]"`, `"[[Album]]"`, `"[[Essay]]"`, `"[[Software]]"`. `creator` is a YAML list of wikilinks to Person notes. `parent_work` points to a containing work (e.g., a book in a series points to the series; an essay in a collection points to the collection).

### Event

```yaml
---
type: "[[Event]]"
subtype: 
date_start: 
date_end: 
era: 
place: 
participants: []
associations: []
created: YYYY-MM-DD
---
```

Notes on Event: dates can be exact (`YYYY-MM-DD`) or approximate text (e.g., `c. 325`). `era` is a broad period like `Late Antiquity`, `20th century`, or `Second Temple period`. `place` is a wikilink to a Place note. `participants` is a list of wikilinks to Person notes.

### Idea

```yaml
---
type: "[[Idea]]"
subtype: 
name: 
definition: 
aliases: []
key_people: []
associations: []
state: Seed
created: YYYY-MM-DD
---

## Description

[One concise paragraph explaining the idea.]
```

Notes on Idea: `subtype` examples include `"[[Concept]]"`, `"[[Doctrine]]"`, `"[[Phenomenon]]"`, `"[[Instrument]]"`, `"[[Lexeme]]"`. `definition` is a single quoted sentence. `key_people` is a list of wikilinks to Person notes who originated, defended, or are closely associated with the idea. The Idea type is the only type that gets a default body section (`## Description`); fill it with one paragraph in plain prose.

### Journal

```yaml
---
type: "[[Journal]]"
subtype: 
created: YYYY-MM-DD
---

[Body: prose recording the day's witness, with wikilinks to entities mentioned.]
```

Notes on Journal: `subtype` may be `"[[Dream]]"`, `"[[Sermon Note]]"`, or left blank for a standard daily entry. The journal entry's filename is typically the date (`2026-04-27.md`). The body is the entire point of a Journal note: prose that records what the user did, read, thought, or noticed, with wikilinks to every entity mentioned. Even one sentence with a few wikilinks is enough.

## Research behavior

When generating a stub for a public or historical entity (a real person, a published work, a known place, a documented event, a recognized idea), use web search to verify uncertain fields. Birth dates, death dates, publication years, founding dates, geographic details, and other factual fields should be researched rather than guessed. If a field cannot be verified with reasonable confidence, leave it blank.

Do not research personal entities. If the user asks for a stub about their friend, family member, employer, or any private entity, generate a structurally complete template with empty fields and let the user fill it in. Do not search the web for personal information about individuals.

If web search is unavailable in the current environment, generate the stub from training data and explicitly note (in a brief line above the code block) that fields could not be verified and the user should double-check dates and other specifics before relying on them.

## Handling ambiguous type assignments

Some entities are ambiguous between two types. Apply these heuristics, in order:

**If it is an artifact made by someone, it is a Work.** *Hamlet* is a Work, not an Idea. Even if the user asks "make me a note about *Hamlet*," produce a Work note.

**If it is something that happened at a time, it is an Event.** The Council of Nicaea is an Event, not a Place. The Reformation is an Event (or a series of Events), not an Idea, even though it is closely associated with theological ideas.

**If it is a location or institution, it is a Place.** A specific parish church is a Place (Institution subtype), not a community of people, even though it has members. The Roman Senate is a Place (Institution subtype), not an Event.

**If it is an abstraction or concept, it is an Idea.** Justification by faith is an Idea, not an Event. Subcreation is an Idea, not a Work, even though Tolkien wrote about it.

**If it is a real human, it is a Person.** This is rarely ambiguous, but worth stating: even fictional characters' authors are Persons (the character is something else; ignore characters for now unless the user asks).

If two types both seem defensible after applying these heuristics, ask the user which one they prefer rather than picking unilaterally. A short clarifying question costs less than producing a stub the user has to redo.

## One stub per request

The default is one note per request. If the user says "stub Tolkien," produce a single Person note for Tolkien. Do not also produce stubs for *The Lord of the Rings*, Oxford, or anything else unless the user explicitly asks.

If the user wants a cluster, they will say so: "stub Tolkien and his major works," "give me Person, Work, and Place notes for the Augustine cluster," "make a full set for the Council of Nicaea." When asked for a cluster, produce one code block per note, with a brief label above each (e.g., "Person note for Tolkien:") to make pasting easier.

## Output format examples

### Example 1: Single Person stub

User: "stub a Person note for J.R.R. Tolkien"

Output:

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

### Example 2: Single Idea stub with body

User: "make me an Idea note for subcreation"

Output:

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
state: Seed
created: 2026-04-27
---

## Description

Subcreation is Tolkien's term, developed most fully in his essay "On Fairy-Stories," for the artist's vocation to fashion a coherent secondary world. The subcreator does not rival the primary Creator but participates in creation by making something that bears its own internal consistency and meaning. Tolkien's Middle-earth, with its languages, histories, and geography, is the paradigmatic instance.
```

### Example 3: Cluster request

User: "stub Tolkien, *The Lord of the Rings*, and Oxford"

Output:

Person note for Tolkien:

```yaml
---
type: "[[Person]]"
subtype: "[[Author]]"
[...full stub...]
---
```

Work note for *The Lord of the Rings*:

```yaml
---
type: "[[Work]]"
subtype: "[[Novel]]"
[...full stub...]
---
```

Place note for Oxford:

```yaml
---
type: "[[Place]]"
subtype: "[[Location]]"
[...full stub...]
---
```

### Example 4: Personal entity (no research)

User: "make a Person stub for my friend Andrew"

Output:

```yaml
---
type: "[[Person]]"
subtype: "[[Friend]]"
alternate_names: []
birth_date: 
nationality: 
roles: []
spouses: []
partners: []
children: []
parents: []
associations: []
created: 2026-04-27
---
```

(No web search performed; fields left blank for the user to fill in privately.)

## What this skill does not do

This skill produces stubs. It does not produce essays, encyclopedia articles, or long-form notes about entities. The Ontological Type System is built on atomic notes; a stub that becomes a 2000-word essay about Augustine has missed the point. Body text, when present, should be one paragraph or shorter.

This skill does not invent new types. The six root types are closed. If the user proposes a seventh type, push back and find which of the six the candidate actually fits.

This skill does not include user-specific defaults. The user's home church, their preferred subtypes, their personal vault conventions, their custom CSS or template extensions, are not part of this skill. The skill ships the universal method.

This skill does not write Journal entries on behalf of the user. The Journal type records the user's own dated witness; only the user can produce its content. The skill can produce a Journal template (as shown above) for the user to fill in, but should not generate the body prose itself unless the user provides the content and asks for formatting help.

## A final note on posture

When producing a stub, treat the act with the seriousness the system asks for. The note represents a real entity in the user's vault; it will live there for years and accumulate connections to other notes over time. A sloppy stub is a small but real injury to the integrity of the user's knowledge graph. Take the small care needed to get fields right, to choose associations that will pay rent, and to leave blanks rather than fabricate. The user has chosen this method because they want their note-taking to form their attention. Help them by producing notes worth attending to.
