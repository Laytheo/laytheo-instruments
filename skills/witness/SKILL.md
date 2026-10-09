---
name: witness
description: Witness something the user encountered or remembered into their note vault. Covers four modes. Enrich (build notes for the empty links in an entry they wrote), Witness X (log a thing they met, with their own phrase), Discourse (talk a thing through first, then log it), and Memory (record a remembered past event as an Event note, with the reflection witnessed into today's daily note). Use when the user says "witness this," "let's talk about it for my witness," "I was listening to X, let's talk about it," "enrich today's note," "help me record this memory," or starts telling a story from long ago that no journal covered. Not for recordings they made, not for a bare note with no witness, not for essay drafting.
---

# Witness: something met, talked through, and kept

## Purpose

In the Ontological Type System (OTS), every time the user types a line in their daily note and links to something, they have witnessed it. That manual witness is most of them, and it needs no help. This skill is for the cases where the user wants to attend to a thing with more care than a line allows: they open the agent and say, roughly, "I was listening to a video about this; let's talk about it for my witness." It also covers the other case, a story that surfaces from the past and no journal ever covered (Memory mode, below).

The agent does not create the witnessing. Mostly it does the clerical work: it places the thing in its world so the user knows what they actually met, builds the thing's note, and formats the witness. When the user is still working out what they think, it can also ask what struck them, so their own reaction gets developed. Then it files two things. The thing keeps its own note (the object). The daily note keeps the user's experience of it (the witness). The link joins them, so opening the thing's page later shows the user's witnesses as backlinks.

**The witness is the user's thought, completed; never your thought, added.** What the user gets from the agentic route is that they bring the spark of an idea and the agent helps develop it if necessary. So you may complete the thought: say in plain words what they pointed at, at the resolution they met it. You may never add one: no angle, application, comparison, or claim they did not make or take up.

A worked case (illustrative). Suppose the user's whole input is: "The meat shower reminds me of the engine video, how he keeps explaining until the weird thing is obvious." An agent that answers with a long analysis of both and then condenses that analysis into the witness, plus an application the user never mentioned, has failed. The witness wanted is:

```markdown
- [[Jimmy Akin's Mysterious World]] / [[Technology Connections]]
    - The Kentucky meat shower reminded me of the engine video: both take something that looks strange and explain it step by step until it is obvious.
```

Their sentence, with one clause naming the pattern they pointed at. Nothing in it is new content; it says what they meant.

## Met, not used (the qualifying test)

**Witness what happened to the user, not what they only used.** *To meet a thing is to encounter it for its own sake: for the first time, or personally rather than instrumentally.* Quick test: **did I meet it today, or only use it today?**

- **Met:** a first encounter (a new concept, fact, or term, even with no feeling about it yet), or a personal one (it moved them, a memory surfaced, they loved or hated something in it). A re-encounter counts when it is personal (a remembered book that still makes them cry).
- **Used:** the thing served something else, an example, a source, an analogy, an argument. "This will make a great example" and "useful for the argument" are judgments of use; they belong in the project's own note (an essay companion's candidate material), which links the thing anyway, so its backlinks survive.
- **Apply it to the line, not the topic.** The same thing can be met or used depending on what the user says about it. Phrase the witness as the meeting ("I love what he's doing there", "the term and its provenance were new to me"), never as the assessment.
- **Long sittings collapse into one bullet.** A session that touches many things (an essay sitting, a long research conversation) is witnessed as one top bullet for the session, linking the project, with the met things as its sub-bullets. Used things stay out of the daily note.

## Four modes

Witnessing is linking a thing in the user's daily note with their experience of it. The modes differ in who writes the line and who builds the thing's note. In every mode, **the line is the user's**.

| Mode | The user says | You do |
|---|---|---|
| **Enrich** | "Enrich" (today's note by default), after writing the entry themselves | Build notes for the empty links in what they wrote. Never touch their words |
| **Witness X** (the default) | "Witness *Technology Connections*," often with a phrase | Place the thing, build or update its note, write the bullet from their phrase |
| **Discourse** | "Let's talk about it for my witness," or they sound unsure what they think | Place the thing, ask, draw them out, then compose the bullet from their answers |
| **Memory** | "Help me record this memory," or they start telling a story from long ago | Let them tell it, interview lightly, draft an Event note and a reflection, write on approval |

**Enrich.** Ask your note tool for the unresolved links in the note. For each dead link: check whether it is a near-miss for an existing note (typo, casing, singular or plural; confirm with a search) and repair the link if so; otherwise classify it and create the note per step 4 of the sitting. Fix nothing else in the user's entry except an obvious typo inside a link. Show the plan (each orphan, its proposed type and subtype, any repairs) and proceed on their OK. One level only: do not chase the new notes' own orphans.

**Witness X.** Skip step 2. If the user gave a phrase, the bullet is built from it. If they gave only the name, ask for one line ("One line from you?"); if they still give nothing, write only the link line. A bare link is a witness too. Never write their experience for them.

**Discourse.** Offer it, do not impose it. It is the right tool where attention is hardest: **people**, and **things that move or unsettle the user**, where they do not yet know what they think.

**Memory.** See "Memory mode" below.

## Where this skill ends

| If what the user is telling you is... | Use instead |
|---|---|
| A recording they made (a conversation, a meeting, a sermon, a call) | Your transcription workflow, then a step that turns the transcript into notes |
| A request for a note on something with no wish to witness it ("stub X") | `ots-notes` |
| An essay in progress | `quill` (Quill calls this skill at wrap-up, in Witness X mode, for the entities the user engaged) |

If it is unclear whether something is a remembered event or a fresh encounter, ask once. A thing the user met today is a witness; a thing that surfaced from years ago is a memory.

## The sitting (Enrich, Witness X, Discourse)

### 1. Place it in its world (short)

Before asking anything, find out what the thing is, so the conversation is about the real thing and not your guess. Web search, and check the sources. Then say, in a few sentences, only what orients the user: what it is, who made it, when, and the one or two facts that matter. No lecture, no survey of opinions, and nothing you could not source.

- Verify every proper noun and date before you state it. A wrong fact in the frame poisons the witness.
- If it is a person, work, or event the user already knows well, say less. If it is something they said they had never heard of, say a little more.
- If a claim is contested, say so in a clause and move on.
- If it was a coworker's remark or an in-person conversation, there is nothing to look up about the speaker. Place the *subject* of the remark if it has one, and otherwise skip this step.

End the frame with the question in step 2. Do not stack questions behind it.

### 2. Ask what struck them, if they want to think it through

**Most witnesses do not need this step.** For many, the primary utility is the clerical work: the populated entity note and a properly formatted bullet, especially when the user is working from a phone. The questions are a feature that emerged, not the point. If the user has already said what they think, go to step 3 with their words. If they have not, or seem to be working out what they think, offer once ("Want to talk through what struck you, or should I just log it?") and follow their lead.

When they do want to think it through, ask what struck them, or what impact it had. Then draw out their own reaction with a question or two, and no more:

- "What struck you about it?"
- "Why that?"
- "What did it rouse, if anything?"
- "Did you change your mind partway through?"

Rules for this step:

- **Do not draft their reaction for them, and do not suggest one.** No "you might feel that..." and no menu of angles. If the answer is one line, a follow-up question is better than a guess.
- **Do not supply parallels, applications, or further angles of your own.** If you offer one and the user does not take it up in their own words, it stays out of the witness. A witness that reads like your reply compressed is a defect, however good the reply was.
- If they react at length, let them. If they have nothing to say beyond the link, that is a legitimate witness; do not manufacture one.
- If they mention a second thought, a softening, or a second thing it reminded them of, that is material for the bullet (see step 3).

### 3. Draft the witness bullet and show it

Write it in the user's established shape, and **show them the bullet in chat before writing anything**:

```markdown
- [[Jimmy Akin's Mysterious World]] / [[The Kentucky Meat Shower]]
    - What happened, in their terms.
    - What it roused.
    - A second thought, if they had one.
```

- **The top bullet is the entity link or links, joined by " / ".** The source and the thing it was about (a show and its topic, a channel and its subject, a speaker and the idea) share one bullet when one thought connects them. A single entity gets a single link. This differs from the plain-text top bullet you would use for a recorded conversation that has no note; here the thing has a note, so the top bullet links it.
- **Then first-person sub-bullets of one or two sentences each:** what happened, what it roused, and a second thought if they gave one. Three sentences means it is two bullets or one fact too many.
- **It is an echo of what the user could recall walking away, not a summary of the thing.** The facts you gathered in step 1 live in the thing's note; the daily note carries the user's experience. Keep a number or proper noun only when it *is* the memory.
- **Compose from the user's turns only.** Your own replies in this conversation feed the thing's note and the choice of links, never the wording of the line. An agent that has just written an analysis reuses it without noticing, so the rule is structural, not a matter of care. Before showing the bullet, check each clause: did they say it, or point at it?
- **Complete, never add.** Keep their phrasing, their hedges, their jokes; fix transcription noise. You may finish a thought they started: a clause that names the pattern they pointed at, or a proper noun that names exactly what they meant ("the engine video" becomes "[[Technology Connections]]"). You may not add a claim, angle, application, or comparison they did not make.
- **Propose connections; the user decides.** If you notice a relation they did not make (a second work, a person, an idea), offer it in chat. It goes into the line only if they take it up in their own words, and then the second link joins the top bullet with " / ".
- **Link the entity, display the user's word.** If they said "Akin" and the note is `Jimmy Akin's Mysterious World`, pipe it: `[[Jimmy Akin's Mysterious World|Akin]]`, in the sub-bullet prose. The top-bullet link may use the note title. Never silently swap the user's word for the full title.
- **Never hard-wrap.** One bullet is one line, however long. Raw markdown only: never fence the bullet in the vault write (the code fence above is only how it is shown in this document and in chat).
- **No tags, no "Recorded, about N minutes" line, no provenance line.** Provenance is not something the user would write in their own journal.

Revise from their edits. If they edit your bullet shorter, take the shorter form as the signal for the next one.

### 4. Create or enrich the entity note

Do this alongside the witness, not after it, so the link resolves.

1. **Duplicate check first, always.** Search the vault for the name, and list the likely type folder if the search is unclear. If a note exists, enrich it, preferring a section edit or an append over a full overwrite; if not, create one.
2. **Follow `ots-notes` for the note**: read its `TAXONOMY.md` for type and subtype, classify, and keep associations genuinely defining (a new orphan link is weighed skeptically).
3. **Real, grounded body.** An empty stub is never acceptable. Read your note style guide once per session before composing (one job per paragraph, cap three sentences, sections named for their content, bold-lead bullets for substance, never hard-wrapped). Ground every fact in a source from step 1.
4. **Sources carry accessed dates:** `- https://example.com (accessed YYYY-MM-DD)`, using today's date.
5. **Proportion to engagement: knowledge grows at the rate of attention.** The body's depth matches what the user actually knows of the thing right now, not how much there is to find. A thing they met once is a tight paragraph and `## Sources`.
   - **On a re-encounter** (the note already exists): add only what *this* encounter taught them, into the section it belongs to, with any new source. Never use a second witness as the excuse for a research dump. If this encounter taught them nothing new about the thing itself, leave the note alone; the witness and its backlink are the growth.
   - **`state` tracks the user's engagement, not the thing's importance:** `Seed` = met once, a sketch; `Developing` = they have met it again and the note has grown from what they learned; `Stable` = they know it well and the note says what they would say. Move Seed to Developing yourself when a re-encounter adds to the body, and say so in the report. Never set `Stable` on your own; suggest it, and let the user confirm.
6. **The user's reaction does not go in the entity note.** Subjective response is witnessed in the daily note and never stored on the object. The entity note says what the thing is; the witness says what it did to them.

A series, show, or channel the episode came from usually deserves its own note too (the source of the encounter), so that the top bullet's two links both resolve. If only one of the two exists, create the missing one the same way, and say so.

### 5. Write

On the user's OK:

- **Prefer an append-to-today tool** for the daily note write if your note tool offers one: give it the first link, the remaining links to share the bullet, and the echo built from the user's own words. It should append at the current end of today's note, in the time-of-day section the user is writing in. If it records links by note title, check the result and fix any display word you piped.
- If the tool reports the thought is already witnessed, do **not** work around it by appending another bullet; edit the existing bullet in place.
- If the user had already typed a bare line for the thing in their own prose, extend that line instead of duplicating it.
- Create the entity note **before** the daily-note write, so the link resolves.

**Time-of-day headings.** If the user's daily notes run under `## Morning`, `## Afternoon`, `## Evening`, and sometimes `## Bedtime`, apply this rule by their local time: Morning before 12:00, Afternoon 12:00 to 17:00, Evening from 17:00. When a write lands in today's note, add the current period's heading only if it is missing and the clock has moved forward past the note's last period heading (or the note has none yet); then write the bullet under it. Never insert an earlier heading than one the user wrote, never reorder or rename their headings, never touch their prose, and never auto-add `## Bedtime` (if they typed it, write under it). If your append tool already does this, let it; for any write made another way, apply the rule yourself.

### 6. Report, briefly

Say what landed: the bullet, which notes were created or enriched, and any suggested links the tool returned (stripped orphans) so the user can decide whether they are worth stubbing. Do not create those silently. If the user named a second thing in passing that deserves its own witness, offer it as the next one.

## Memory mode: remembered events

A story that surfaces unbidden, usually from childhood, that no journal entry ever covered. The user describes it out loud, you act as a **witness**, and it lands as a properly typed, linked Event note with the reflection filed where reflection belongs. The value is not transcription. It is drawing out what the user would have skipped and doing the sorting they do not want to do in the moment.

### The one rule that matters

**Do not rewrite their words.**

These memories are dictated. They read as speech, and that is correct. "The front room, as we always called it." "That's a whole other story." A recollection is testimony, and smoothing testimony into cleaner prose falsifies it.

- Fix obvious transcription noise (a dropped word, a mangled homophone). Nothing else.
- Never summarize. Never tighten. Never improve a phrase.
- Never reorder the account into a better narrative.
- If a sentence is unclear, ask, do not repair it.

### The convention (why the pieces go where they go)

A remembered happening is still an **Event**, because it happened. The subtype `[[Memory]]` marks the *mode of access*, known by recollection rather than by contemporaneous record. So there is never a judgment call about the type. Memory notes add two fields the base Event template lacks: `era`, a link to an Era note (an Event with subtype `[[Era]]`, or however your vault groups life phases), and an optional `provenance`.

| What | Where | Why |
|---|---|---|
| The recollection | The Event note | It is testimony about the past |
| What the user makes of it now | **Today's daily note** | Reflection is dated by when the user reflected, and the Journal is the one OTS type indexed by date of writing |
| A general claim the memory is evidence for | An **Idea** note | A claim buried in one memory is stuck there; promoted, it accumulates evidence from many |
| What a room or a period was like | A **Place** or **Era** note | Scene-setting belongs to neither incident and will be referenced by other memories |

Interiority splits by owner. What the user felt **at the time** is recollection and stays on the Event. Their verdict **today** is reflection and goes to the day.

`created:` on a memory note means the day the user *remembered* it, not the day it happened. This is the one Event subtype where those diverge.

### The sitting

1. **Let them tell it. Uninterrupted.** Do not open with questions. Do not interject with structure while they are still remembering.
2. **Then ask at most two or three questions**, and only ones the account actually left open. Never run the whole list. An interrogation kills the capture, and the capture is the whole point.
   - Who else was there?
   - Where exactly?
   - Roughly when, in life-phase terms (not a date)?
   - Were you there, or were you told this?
   - What are you unsure of?
   - Was that one occasion or two?
3. **Ask for the reflection separately, at the end.** "What do you make of it now?" Keep the answer out of the Event note.
4. **Check the existing eras** before assigning one, so you reuse `[[High School]]` instead of inventing `[[High School Years]]`: list the Era folder of your vault. If the era the user names has no note yet, say so and offer to make one. Do not invent its contents; an era is the user's life, and its body has to come from them.
5. **Show the draft in chat and wait.** The review is the point, not overhead. Show the title, the frontmatter you intend, the body, and the reflection separately so the user can see the split.
6. **Then write once** for the whole sitting: the Event note or notes, and the reflection into today's daily note.

### The witness shape

The reflection lands in the day note as an indented sub-bullet **under** the memory's wikilink, not as a paragraph with the link trailing after it. The memory is the anchor and the thought attaches to it. For example (invented):

```
- [[The Summer the Creek Flooded]]
    - I was never so sure of anything as I was that nothing could happen to us.
```

When a sitting produces several memories, attach each reflection under the memory it is about.

### Graph awareness: link the entity, display the user's word

When People and Places that already have notes are named in the recollection, link them. **The link displays the word the user actually said.** They say "Desmond", the note is "Desmond Philips", the link is `[[Desmond Philips|Desmond]]`, which Obsidian renders as "Desmond". A piped link satisfies the do-not-rewrite rule and graph connectivity at the same time, where a bare `[[Desmond Philips]]` would force a choice between them.

Resolve short forms from the event's own `participants` and `place` first, so "Desmond" links only when the user already told you Desmond Philips was there. Leave ambiguous bare first names alone rather than guessing.

Link only People and Places automatically, because an Idea title like "Baptism" appears in ordinary sentences and would over-link. If the user names something notable that has **no** note, mention it afterward as a candidate. Do not create it.

**This convention is not memory-only.** Any link you write anywhere in the vault whose target differs from the user's word should be piped. Never silently substitute a full title for the word the user used.

### Splitting

One note per incident. If a dictation holds two distinct happenings, write two events, not one. Say what you are splitting and why, and let the user overrule you.

**Listen for the user flagging a second memory in passing** ("...which is its own story", "that's a whole other thing"). That is a backlog signal: say you noticed and offer to capture it next, rather than folding it in or walking past it.

Scene-setting that belongs to neither incident goes in a Place or Era note, and you should offer that rather than folding it into a memory. If the reflection contains a general claim rather than a mood, tell the user afterward that it wants an Idea note of its own. Do not create either silently.

### Titling

Title with the handle the user would use to raise it in conversation. A line someone actually said makes the strongest title. Avoid dated or generic labels ("1997 Garage Incident").

### Dates

Leave `date_start` and `date_end` **empty** unless the user actually knows them. `era` carries position in time. A guessed date reads as fact a decade later, and bracketing a range would read as duration rather than uncertainty. The user's own hedging ("either fourth or maybe fifth grade") stays in the prose, where it already belongs.

Set `date_end` **only if the memory genuinely spanned time.** A single occasion takes `date_start` alone; equal start and end dates read as a deliberate one-day span rather than a point in time.

### Provenance

Omit it for the ordinary case. Mark `told` only for family lore the user holds as memory but did not witness, or `inferred` for something reconstructed from evidence. Never mark `firsthand`; the field's *presence* is the signal.

### Participants

List everyone present, including people with no note in the vault. Keep unresolved links deliberately: an invented example, `[[Aunt Jane]]` with no note behind her is the record that she was there. Do not strip them and do not offer to create a Person note for every name.

## The attention review

When the user asks what they have been paying attention to (or, at most monthly, offer it at the end of a sitting), open a view of notes ranked by how many daily notes witness them (in Obsidian, a Base over backlinks does this). The useful question is two-sided: what does the user attend to, and what is missing (people who never appear, things they meant to care about)? Talk it through; write nothing to the daily note unless they ask.

## Things this skill does not do

- **Do not push the agentic route for ordinary moments.** Most of the time the user will write their own reflection, and the agent should not become the default way to do it. If they just want a note for the thing, or are dropping a link into their own prose, that is `ots-notes`, or nothing at all.
- **Do not witness people the user has not asked to witness.** A coworker's remark can be the subject, but personal notes on third parties stay thin and grounded in what the user said.
- **Do not read past daily notes for context.** The only daily note this skill touches is today's, to write into it. Do not browse past days for themes.
- **Do not move the user's reaction into essay material.** If a witness turns into an essay seed, say so after, and let the user decide; that is `quill`'s job.

## Tools

This skill assumes a note tool over your vault (for example an MCP server). It needs these operations; names vary.

| What | Operation |
|---|---|
| Place the thing | web search; verify names, dates and sources |
| Check a note exists | search by name; list a folder |
| Create the entity note | create a note with type, title, subtype, fields, body |
| Enrich an existing one | update by section, append, or replace |
| Write the witness | append a bullet to today's daily note, with links |
| Fix a bullet already written | replace text in today's note |
| Rename a note the user drafted live | a rename that repoints inbound links, never a plain file move |
| Write a remembered event (Memory mode) | create an Event note and write the reflection into today's note |

## Privacy

A vault is private, and the daily note especially. What the user says in a witness goes into the chat and the vault and nowhere else: not a scratchpad, a commit message, a pull request body, or a session summary. Never quote a witness or a memory back outside the conversation; refer to the note by title. Memories are among the most sensitive material in a vault. Do not browse the memory folder for context or themes the user did not ask about.
