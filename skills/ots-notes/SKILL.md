---
name: ots-notes
description: Create or update a single note in an OTS (Ontological Type System) vault ad hoc during a conversation. Use when the user asks for a stub or note for something mentioned in passing ("make me a note for X," "stub this," "add a Work note for that book"), wants an existing note edited (add a field, add an association, fix frontmatter, extend a body section), or asks whether a note already exists. Always check for an existing note before creating one. Not for essay drafting (use quill), witnessing an encounter or a memory (use witness), or bulk filing of existing notes.
---

# OTS Notes: ad hoc note creation and editing

## Purpose

Most vault work goes through a skill built for its situation: `quill` for essay drafting, `witness` for encounters and remembered events. What is missing is the plain case: the user mentions a person, book, place, or idea in conversation and wants a stub for it, or wants an existing note tweaked, right now, without any of those specialized flows applying. That gap is where inconsistency creeps in (a note made without checking for a duplicate, or with a shape that drifted from the others). This skill is the default for that case.

**Read `TAXONOMY.md` in this skill's folder first.** It is the method reference: the six root types, the core stub rules, the six type templates, association discipline, and the ambiguous-type heuristics. This file is only what is specific to working live against a real vault through a note tool.

## Where this skill's authority ends

| If the request is... | Use instead |
|---|---|
| Drafting or revising an essay, or its companion note | `quill` |
| Witnessing something the user met, or recording a remembered event | `witness` |
| Filing many loose notes into type and subtype folders | A bulk filing pass, not this skill |
| Cataloging a transcript | Your transcription workflow |

This skill owns: creating a new stub for one entity mentioned in conversation, editing an existing note (frontmatter fields, associations, a body section) outside those workflows, and checking whether a note already exists before doing either. If a request is ambiguous between this skill and one of the above, ask; do not guess.

## One divergence from the taxonomy: personal acquaintances are in scope

TAXONOMY.md is written so it can be used without vault access, so its Person guidance assumes public, historical, or intellectual figures. With a live vault, personal acquaintances (family, friends, coworkers) are legitimately in scope. Ground those notes the same way as any other: from what the user actually says, never invented, and thin is fine (see Grounding below). The rest of the taxonomy's Person guidance (blank `subtype`, `roles` for vocation, the bio convention) applies unchanged.

## Workflow

1. **Check for an existing note first, always.** Search by name (or list the likely type folder to browse) before ever creating a note. A duplicate stub is worse than a slightly slower conversation. If one is found, the request is an update, not a create.

2. **Classify.** Decide the type and, when it is reasonably clear, the subtype using the taxonomy's heuristics. If genuinely ambiguous between two types after applying them, ask the user rather than picking.

3. **Ground the body.**
   - Public or historical entity: verify facts with a web search before writing them. Never fabricate; leave a field blank (or say so and skip the note entirely) rather than guess.
   - Private entity, or anything the user described themselves: trust what they said, write only that, and leave the rest blank. A two-sentence bio from a short mention is a legitimate Seed, not an unfinished note; do not pad it to look fuller than the grounding supports.

4. **Shape it.** If the user keeps a note style guide in their vault, read it once per session before composing a body. The taxonomy's **Body shape** section is the same rules in brief and is the fallback. The short version: one job per paragraph, cap three sentences, name sections for their content, bold-lead bullets for substance, tables only when the content has two axes, and never manufacture a section the material does not earn. The standing complaint about agentic notes is the wall of prose, so an all-prose body with a single generic section is the failure to watch for.

5. **Keep it proportioned.** Three places this goes wrong:
   - **The body's depth matches the user's own current understanding of the subject, not how much material exists to write about it.** Length is a symptom of this, not the target: do not research a topic thoroughly and then write to that thoroughness. Seed the note at the level of knowledge the user actually has of the thing right now. Read that level from what they have said or shown in the conversation, not from how well documented the topic happens to be. A bare "stub X" with no elaboration defaults to a first encounter: roughly a paragraph describing what the thing is. If the user has been explaining or working through the subject at some length before asking for the note, the note can reflect that same depth, because that is real engagement, not research thoroughness dressed up as it. Use research to verify accuracy of what is written, not to add scope beyond what the user's own engagement supports; when genuinely unsure how much they know, default to the shallow case. A bare frontmatter stub is still never acceptable: the floor is a real paragraph, and the ceiling is the user's own current grasp of the thing.
   - **This is a starting point, not a ceiling.** The note is expected to grow as the user's engagement deepens, the same way an essay's companion note accumulates through drafting. A thin Seed today is not a problem to solve now; it is the honest state of the note until the user comes back to it with more. The `state` field tracks this: `Seed` (met once, a sketch), `Developing` (met again, the note has grown), `Stable` (the user knows it well and the note says what they would say). Never set `Stable` on your own.
   - **Associations stay genuinely defining, and orphans get extra scrutiny.** The taxonomy's two tests already exclude topical fields. Apply that with real force: a broad intellectual discipline (`Philosophy of Religion`, `Metaphysics`, `Epistemology`) almost never passes the defining-relation test for a specific idea or argument and belongs in prose, if anywhere, not in `associations`. Reserve associations for entities the note's identity actually depends on (a direct parent or sibling form, a specific work or concept it cannot be explained without). Weigh a **new orphan link** (no note exists yet) more skeptically than a link to something that already has a note; if an association is only "maybe useful once that note exists," leave it out rather than manufacture the phantom link now. `key_people` earns more latitude for orphans than `associations` does, since it is a narrow, well-defined field (who originated, defended, or is closely tied to the idea) rather than a topical catch-all.

6. **Write it.** Create a new note with type, title, subtype, body, and fields; update an existing one by a surgical mode (replace, section, append) in preference to a full overwrite, which should be a last resort even when previewed.

7. **Report what happened**, briefly: what was created or changed, and any suggested links the tool returned (orphan wikilinks it stripped) so the user can decide whether those are worth stubbing too. Do not silently create them.

## Shapes of Work notes

Two Work shapes recur, and getting them wrong clutters the graph.

- **Fictional characters** go in a `## Characters` section of their Work note, not in Person notes (a Person is a real human).
- **TV episodes** are sections on the series note, not notes of their own, each headed with its title, unless an episode is particularly famous or influential in its own right. The taxonomy states the rule in full under the Work template.
- **The user's reaction never goes on the entity note.** A note says what a thing is; what it did to the user is witnessed in their daily note (see `witness`).

For example, a podcast gets one Work note with subtype `[[Podcast]]`; a single memorable episode joins it as a section headed with the episode's title, and only a famous or influential episode earns its own Work note with `parent_work` pointing at the podcast.

## Confirmation: preview only on judgment calls

Do not preview every note before writing it. Two things make that unnecessary as the default:

- **It is reversible.** A note can be corrected or extended after the fact as easily as it could have been fixed before writing. Front-loading a review on every note trades that cheap after-the-fact fix for a slow conversation.
- **Most requests are not judgment calls.** A note for a well-documented historical figure, with a standard field set and a factual paragraph, is very unlikely to need correcting. That is especially true in a batch ("stub these five authors"), where confirming each one individually defeats the point of asking for a batch.

So: **write directly and report the result** when the type is unambiguous, the facts are well grounded (a clean web-search hit, or something the user stated plainly), and any associations are obvious calls under the taxonomy's two tests.

**Preview first** (show type, subtype, title, fields, and body, and wait for a go-ahead) when:
- The type or subtype genuinely needs a judgment call, not just a lookup.
- An association is a close call under the productive-link and defining-relation tests, or the list is getting long.
- Facts came back thin, contested, or unverifiable, and the note is being written anyway because the user still wants something on record.
- The write is a full overwrite of an existing note, since that can discard content.

## Tools

This skill assumes a note tool over your vault (for example an MCP server). It needs these operations; names vary.

| What | Operation |
|---|---|
| Check if a note exists | search by name, or list a folder to browse |
| Create a new note | create with type, title, subtype, body, fields |
| Edit an existing note | update by replace, section, or append; overwrite as a last resort |
| Read a note before editing it | read, optionally by heading |
| See what links here or from here | backlinks and outbound links |

## Prose rules for notes

No em dashes and no double hyphens as a substitute; use commas, semicolons, colons, parentheses, or new sentences. Never hard-wrap a note body (one line per paragraph or bullet).
