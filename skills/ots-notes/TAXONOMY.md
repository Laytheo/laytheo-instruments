# Ontological Type System: method reference

The full methodology is described at
[laytheo.com/instruments/ontological-type-system](https://laytheo.com/instruments/ontological-type-system).
This file is the operational reference for producing OTS-compliant notes; it assumes
the method has already been adopted and just needs applying. It is deliberately
tool-neutral: it says what a compliant note looks like and how to classify one, not
how a particular tool should call an API or render output. The skill that uses it
carries that operational layer.

## What the system commits to

Notes represent things that exist in reality, not arbitrary mental categories. A
Person note is about a real human. A Work note is about a real artifact. A Place note
is about a real location or institution. Treat each note as a first careful act of
attention to the entity in question, not a filing exercise.

**The ontology is a method, not the end.** The method's stated purpose is a better
understanding of the Lord God's creation (a reader who does not share that framing can
read it as a better understanding of reality); the notes are organized to reflect real
things because ordering them truly is how that understanding is built, and because it
honours what is actually there. But the fidelity serves the understanding rather than
replacing it. This subordination has a practical consequence that comes up constantly:
a note can correspond perfectly well to something real and still not belong in the
vault, because it does nothing for the understanding the vault exists to build. See
**Does this earn its own note?**

## Six closed root types

- **Person**: any real human, living or dead, biblical, historical, contemporary, or personal
- **Place**: a location or institution (both physical places and organizational entities)
- **Work**: any artifact made by a person or group (books, songs, films, software, sermons, essays)
- **Event**: anything that happened, at a time, to participants, in a place
- **Idea**: an abstraction, concept, phenomenon, or instrument of thought
- **Journal**: one's own dated witness of reality (the daily note)

Subtypes are open: add subtypes freely under any root type. Types are closed: never
invent a seventh. If a request seems to demand one, find which of the six it actually
fits rather than proposing a new type.

## Core rules

Every OTS-compliant note follows these. They are not optional.

- **Frontmatter first, then body.** A YAML frontmatter block delimited by lines of three hyphens, then
  the body below. The schema carries the facts; the body carries what the schema cannot.
  See **Body shape** for how that body is structured.
- **Type and subtype as wikilinks.** `type` is one of `"[[Person]]"`, `"[[Place]]"`,
  `"[[Work]]"`, `"[[Event]]"`, `"[[Idea]]"`, `"[[Journal]]"`. `subtype` is a wikilink to
  a more specific category, or blank. Wikilink values are quoted strings in YAML.
- **Three required fields:** `type`, `subtype` (may be blank), `created` (ISO date
  `YYYY-MM-DD`, today's date unless the user specifies otherwise).
- **Atomic notes.** One note, one entity. "Tolkien and his works" is separate stubs for
  Tolkien and for each work, never one combined note.
- **No em dashes and no double-hyphen substitutes.** Commas, semicolons, colons, parentheses, or
  sentence breaks instead.
- **Empty fields are fine. Fabricated ones are not.** An unknown value stays blank. The
  schema tolerates blanks; it does not tolerate invented facts.
- **Grounding.** Verify before writing a factual claim. For a well-documented public
  figure or event that means research. For something known only through the user's own
  testimony, that means trusting what they told you and leaving the rest blank. Never
  fabricate detail either way, and if a subject can't be grounded at all, say so instead
  of producing a hollow note.
- **Wikilink only entities of independent note.** Relational list fields
  (`associations`, `spouses`, `partners`, `children`, `parents`, `participants`,
  `key_people`, `creator`, etc.) hold references to other entities. Only wikilink one if
  it plausibly merits its own note (a person, place, or work of independent public,
  historical, or intellectual significance). Private individuals with no note of their
  own (minor children, non-public parents and spouses, friends not otherwise notable)
  stay as plain text strings inside someone *else's* note. A wikilink is a promise that
  the target is worth a note; when in doubt, default to plain text.
- **Kinship fields are stricter than general notability.** For `parents`, `spouses`,
  `children`, and `partners`, a relative having their own public record is not by itself
  a reason to wikilink them: they must matter to the subject in their own right, normally
  by figuring in the work the subject is known for. The test is collaboration, not
  relation. If they worked with the subject on that work, link them; if the tie is only
  kinship, list them as plain text. Diagnosis: Matthew Henry's father Philip was an
  ejected minister with his own DNB entry, and Matthew wrote his biography, and the call
  was still plain text, so lean conservative. The user's own circle is the common
  exception, since those people usually already have notes. This applies to the note body
  as well as the frontmatter.
- **Be strict with associations.** The most easily abused list in the schema; it
  tempts a dump of every loosely-related entity, which clutters the graph and dilutes
  what a wikilink means. Apply two tests: the **productive-link test** (would a reader
  genuinely benefit from following this link from this note?) and the **defining-relation
  test** (if this association were removed, would something essential about the entity
  be lost?). Most notes have 2 to 5 associations; some have zero. More than five is a
  strong signal the list is doing biographical or topical inventory instead of naming
  defining relations. Career history, employers, and topical fields generally belong in
  body prose, not associations. Defining works (the ones most central to a person's
  identity) may stay in associations even though they're also Work notes elsewhere.
  Resist comprehensiveness; this list is not a CV.

## Body shape

A note body is a **reference card for someone who already met the subject**, not a
briefing that replaces the sources. It is read at a glance, months later, to reorient.

Length is not the variable that matters; apportionment is. A 200-word note whose whole
body is one paragraph reads worse than a 1,500-word note broken into named sections. The
failure to avoid is packing several topics into a single block of prose.

- **One job per paragraph.** The opening paragraph defines the thing and does nothing
  else. A second topic (objections, reception, major works, distinctions, examples)
  becomes its own section rather than another sentence. Test: if naming the paragraph's
  subject requires an "and," split it.
- **Paragraph cap: 3 sentences or roughly 75 words. Target 2.** Applies to every
  paragraph, not just the opener.
- **Name sections for their content**, not generically: "The Wager," "Distinguishing
  It," "Numbering traditions." Only the first section is generic (`## Description`,
  `## Bio`, `## Background`). A note with exactly one section is usually material that
  got compressed instead of apportioned.
- **Sections must be earned.** A thin subject correctly ends after one tight paragraph
  and `## Sources`. Never manufacture a heading to look structured; that is the
  predictable overcorrection to this whole section.
- **Substance goes in bold-lead bullets:** `- **Label.** One or two sentences.` A
  paragraph with a handle on it, which is why it scans.
- **Tables need two axes.** A table earns its place when the cell is the information
  (choice by world-state, statement by tradition). A flat list of related items is
  one-dimensional and stays bullets.
- **Table for the shape, prose for the reasons.** After a grid, one short labeled
  paragraph per group is good: the table shows what each position does, the prose says
  why. The 3-sentence cap still applies to each.
- **Scripture sits at the point of use when it is a specific verse.** Put the passage in
  a `> [!bible]+ Reference - KJV [[Book Chapter]]` callout exactly where the claim needs
  it, never gathered into an appendix; that is what makes it read as evidence rather than
  decoration. A general reference (a chapter, the passage range a group read, a book
  named in passing) can stay inline in the prose. Paraphrasing a specific verse loses the
  wording, which is usually the reason it was cited at all.
- **Sources carry accessed dates** when the note is web-grounded:
  `- https://example.com (accessed YYYY-MM-DD)`.
- **Never hard-wrap note bodies.** One line per paragraph or bullet; Obsidian does not
  reflow, and wrapping breaks editing on a phone. (This file is a skill document, not a
  vault note, so it wraps normally.)

**Two shapes, chosen deliberately.** Most reference notes are one of two things; pick
before writing rather than defaulting.

- **Definition-shaped** (most Person, Place, Work, Idea notes): a one or two sentence
  `## Description` or `## Bio`, then whatever named sections the material earns.
- **Argument-shaped** (a note whose subject is a contested claim): state the claim in one
  line, enumerate the instances, then give each instance its own section with its
  evidence attached. Near-outline prose, one-sentence paragraphs, `###` sub-heads, bold
  on the pivot phrase.

**Exempt:** Journal bodies, dictated memories, and essay drafts. Those are the user's own
voice and dated witness; imposing structure on them falsifies them.

**If the user keeps a fuller style note in their own vault,** it is authoritative and
carries worked examples; read it once per session. The rules above are the self-sufficient
floor when there is no such note.

## The six type templates

Default templates. If the user has a custom schema, use that instead.

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

## Bio

[One or two sentences: who the person is or was and why they matter. Stop there.]

[Then only the sections the material actually earns, named for their content, e.g.
"## Major works", "## Position in the debate". A thin subject ends here.]
```

`subtype` is blank by default. Vocational labels ("researcher," "musician,"
"theologian") are descriptive, not categorical, and belong in `roles`, not `subtype`;
there is no ontological taxonomy of kinds-of-person the way Idea/Place/Work have kinds
of thing. `roles` is a tight list (typically 3 to 5) of plain lowercase strings. Omit a
relational field entirely (don't leave `[]`) if it would never apply (e.g. omit
`spouses` for someone who never married). The bio adds what the schema can't carry:
significance, contribution, distinguishing context; name things truly, plainly, letting
facts carry their own weight.

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

`subtype` is typically `"[[Location]]"` (physical places) or `"[[Institution]]"`
(organizational entities: churches, universities, governments, companies). For
institutions, fill `address`/`city`/`country` if there's a primary location.

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

`subtype` examples: `"[[Book]]"`, `"[[Novel]]"`, `"[[Film]]"`, `"[[Album]]"`,
`"[[Essay]]"`, `"[[Software]]"`. `creator` is a list of wikilinks to Person notes.
`parent_work` points to a containing work (a book in a series points to the series; an
essay in a collection points to the collection).

**Fictional characters live inside their Work.** A character is not a Person (a Person
is a real human) and does not get a note of its own. Record the characters of a novel,
film, or series in a `## Characters` section of that Work's note, one bold-lead bullet
each, saying who they are and how they matter. Mythological figures follow the same rule
(Achilles is an entry on the *Iliad*). A real but semi-legendary author still gets a
Person note, with the historicity question stated plainly (Homer).

**TV episodes are sections of the series note.** Episodes are too numerous for a note
each, so an episode gets a section on its series note, headed with the episode's title
(`## <Episode title>`), the same way characters live in a `## Characters` section. An
episode earns its own Work note only when it is particularly famous or influential in its
own right; then its `parent_work` points at the series.

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

Dates can be exact (`YYYY-MM-DD`) or approximate text (`c. 325`). `era` is a broad
period (`Late Antiquity`, `20th century`, `Second Temple period`). `place` wikilinks a
Place note. `participants` wikilinks Person notes.

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

[One or two sentences defining the idea. Stop there.]

[Then only the sections the material earns, e.g. "## Distinguishing it", "## Standard
objections", "## Examples", carried in bold-lead bullets.]
```

`subtype` examples: `"[[Concept]]"`, `"[[Doctrine]]"`, `"[[Phenomenon]]"`,
`"[[Instrument]]"`, `"[[Lexeme]]"`. `definition` is a single quoted sentence.
`key_people` wikilinks Person notes who originated, defended, or are closely
associated with the idea.

### Journal

```yaml
---
type: "[[Journal]]"
subtype:
created: YYYY-MM-DD
---

[Body: prose recording the day's witness, with wikilinks to entities mentioned.]
```

`subtype` may be `"[[Dream]]"`, `"[[Sermon Note]]"`, or blank for a standard daily
entry. The body is the entire point: it is the user's own dated witness. It is not a
tool's to compose on their behalf; only format or lightly clean what they actually
provide.

## Handling ambiguous type assignments

Some entities are ambiguous between two types. Apply these heuristics, in order:

- **If it is an artifact made by someone, it is a Work.** *Hamlet* is a Work, not an
  Idea, even when asked for "a note about *Hamlet*."
- **If it is something that happened at a time, it is an Event.** The Council of
  Nicaea is an Event, not a Place. The Reformation is an Event (or series of Events),
  not an Idea, even though closely associated with theological ideas.
- **If it is a location or institution, it is a Place.** A specific parish church is a
  Place (Institution subtype), not a community of people, even though it has members.
- **If it is an abstraction or concept, it is an Idea.** Justification by faith is an
  Idea, not an Event. Subcreation is an Idea, not a Work, even though Tolkien wrote
  about it.
- **If it is a real human, it is a Person.** Rarely ambiguous, but worth stating: even
  a fictional character's author is a Person (the character is something else).

If two types both seem defensible after applying these, ask which one is preferred
rather than picking unilaterally. A short clarifying question costs less than a stub
that has to be redone.

## Does this earn its own note?

Two tests, in order. Most requests pass both without thought; this section is for when
that is not obvious, and for resisting the pull toward a note per mentioned thing.

**Ontology is necessary.** Does the thing have sufficient essence unto itself? The note
must correspond to something real: a person, a place, an artifact, an event, an idea
with an identity of its own rather than a category assembled for convenience. A name
coined to group material already covered elsewhere fails here, and no amount of
usefulness rescues it. Failing this ends the question.

**Pragmatism decides.** Passing the floor is not sufficient. The remaining question is
whether a link to it is reasonably likely to actually be written. A note nothing will
ever point at is a filing exercise, and the graph is worse for carrying it. When the
two tests disagree, this one wins.

**The flipside of pragmatism is the ceiling: the vault is not Wikipedia.** Coverage is
not the goal. A thing can be real, genuinely related, and still not earn a note,
because the vault records one person's engagement with creation rather than the sum of
what is knowable about it.

### The threshold moves by domain

The test is not a property of the thing. The same entity can earn a note in a subject
studied deeply and fail in one held at opinion level, because what decides it is how
much the owner actually wants to know the material.

A worked example: a note on the London Naval Treaty does not want a
Person note for every delegate who was present, only for the ones relevant to the areas
under study. The delegates are all equally real. They are not equally wanted.

This is deliberately subjective, and it is the owner's call rather than an agent's.
When the depth of interest in a subject is unclear, ask instead of assuming; assuming
high interest is how a vault turns into an encyclopedia.

### What does not earn a note is not discarded

It goes to one of two places, and saying which is part of the job:

- **Into an existing note where it naturally lives.** Usually the anchor the thing
  belongs to. Facts about an event belong in that event's note whether or not any
  particular claim about them earns a note of its own, so folding a note should migrate
  its substance upward rather than delete it.
- **Into the journal as an observation, linked to an existing note.** Dated witness, in
  the owner's voice, with the wikilink pointing at whatever note it does bear on.

If neither disposition fits and it still seems to need a link of its own, treat that as
a signal the ontology test was actually failed and the entity is not real.

## Scope boundaries

- **Stubs stay atomic and reference-shaped.** This method produces stubs, not essays or
  encyclopedia articles. That is a constraint on *form*, not on size: a long note built
  from named sections, bullets, and tables is in keeping, while a short note that is one
  undifferentiated paragraph is not. See **Body shape**.
- **The six types are closed.** Push back on a proposed seventh; find which of the six
  the candidate actually fits.
- **One entity per request by default.** "Stub Tolkien" is a single Person note. A
  cluster ("Tolkien and his major works") is produced only when asked for.
- **A Journal note's body belongs to the person living the day.** Format or lightly
  clean what they provide; don't compose it for them.

## Posture

A note represents a real entity in the vault; it will live there for years and
accumulate connections over time. A sloppy stub is a small but real injury to the
integrity of the knowledge graph. Take the care needed to get fields right, choose
associations that will pay rent, and leave blanks rather than fabricate. The method
exists to form attention; a note is worth attending to only if it was made with some.
