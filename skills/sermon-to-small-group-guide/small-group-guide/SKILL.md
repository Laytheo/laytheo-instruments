---
name: small-group-guide
description: Convert a sermon transcript into a small group discussion guide for a local church. Use this skill whenever a user provides a sermon transcript (or refers to "the sermon," "this week's message," "Sunday's preaching") and wants discussion questions, small group materials, recap notes, or anything a community group leader would use during the week. Trigger this even if the user just pastes a transcript without explicit instructions; the most likely intent is a small group guide. The skill is tuned to preserve the preacher's voice, distinctive illustrations, and named sources rather than flattening the sermon into a generic theological summary.
---

# Sermon to Small Group Guide

## Purpose

Most AI-generated small group guides fail in the same way: they read like a theological summary of *what the pastor talked about* rather than a guide that helps a group re-encounter the actual sermon. The pastor's anecdote about his neighbor, the half-quoted line from Bonhoeffer, the joke that landed, the moment the room got quiet — these are the things small group members remember on Tuesday night, and they are exactly what gets flattened out by default.

This skill produces a guide that does the opposite: it anchors itself in the **actual flow and texture of the sermon**, then derives the theology and questions from there.

## Church context (REQUIRED)

This skill performs best when calibrated to a specific local church. **Before using this skill, fill in `church-context.md` in this folder.** The skill reads that file at runtime and uses its values to calibrate language, identify the speaker, and match congregational vocabulary.

If `church-context.md` is missing or unfilled, the skill will produce a guide tuned to a generic Protestant default, which is usable but less faithful to your congregation's voice. The skill will warn you when this happens.

The fields in `church-context.md`:

- **Church name and location** — for the byline and any contextual references
- **Tradition** — e.g., Reformed Baptist, Anglican, Methodist, Pentecostal, non-denominational evangelical
- **Primary teaching pastor** — name; note other elders or regular guest preachers, and identify the speaker from the transcript when possible
- **Congregational vocabulary** — phrases your church uses regularly (e.g., "the gospel," "the Lord," "brothers and sisters," "covenant community," "the Word")
- **Theological frame** — distinctive emphases (e.g., Scripture as authoritative; Christ-centered preaching; emphasis on grace, sanctification, life-on-life discipleship)
- **Audience for the guide** — most often small group / community group leaders, mostly lay leaders, facilitating discussion in homes during the week

Calibrate language to match this context. Avoid academic jargon, ecumenical hedging, or generic "spiritual" framing that could come from any tradition.

## Output structure

Always produce exactly this structure, in this order, as Markdown:

```
# [Sermon title or main passage]
*Preached by [Speaker] on [date if known] | [Primary text]*

## This week's big idea
[1-2 sentences naming the central claim of the sermon in the preacher's own framing.]

## Theological anchor points
[2-4 bullets. Each is a substantive theological claim the sermon made, phrased concretely. Not "God is love" but "God's love for his enemies is what makes Romans 5 scandalous, not just sweet."]

## Discussion questions
[3-6 open-ended questions. Let the sermon decide how many. Mix comprehension, application, and tension-surfacing questions. Avoid yes/no. Avoid generic "how does this apply to your life this week?" filler.]

## Sermon walk-through
[A beat-by-beat retelling of the sermon, in 4-8 short paragraphs. This is the heart of the guide. Trace the actual movement of the sermon: where it opened, what passages it walked through, how it pivoted, where it landed. See "How to handle moments in the walk-through" below for the three categories of moments to preserve and how to format each.]
```

## How to handle moments in the walk-through

The walk-through is where most guides fail. The fix is to distinguish three different categories of thing the preacher does, and treat each one differently. Mixing them visually (e.g., italicizing everything) creates noise and obscures signal.

### Category 1: Personality moments

Personal anecdotes, jokes, asides, distinctive turns of phrase, moments of rhetorical force. These are the things that make a sermon *this* sermon and not a generic talk on the same passage.

**Format:** Inline italicized callout, paraphrased faithfully. Name the anecdote so the leader can reference it.

Examples:
- *The preacher opened with a story about his daughter asking him about heaven during bedtime.*
- *Aside about how his kids react to summer heat — got a big laugh.*
- *Long pause before the line: "We don't drift toward holiness."*
- *He returned to the opening illustration about the broken fence to land the application.*

### Category 2: Non-Scripture quotes and named sources

When the preacher quotes a theologian, author, hymn, or other extra-biblical source, **include the actual quoted material**. The source's wording is often what gives the quote its force.

**Format:** Italicized callout that names the source and embeds the quote in regular quotation marks.

Examples:
- *Quoted Bonhoeffer in* Life Together: *"the Christian needs another Christian who speaks God's Word to him... again and again when he becomes uncertain."*
- *Cited a Tim Keller sermon on this passage: the disciples were more afraid after the storm was calmed than during it.*
- *Read the Heidelberg Catechism Q&A 1 in full.*
- *Quoted John Owen:* *"Be killing sin or it will be killing you."*

If the transcript clearly has a quote but the source is unnamed or garbled, render it as a quote and flag the uncertainty: *Quoted what sounded like Lewis: "..." (source unconfirmed).*

### Category 3: Scripture cross-references

When the preacher cites or alludes to a Bible passage other than the primary text, **just give the citation parenthetically in the regular prose**. No italics, no callout. The leader doesn't need the text — they have a Bible. They need to know which passage was invoked so they can look it up.

Examples:
- "He turned to the Psalms to argue that sleep is an image of trust, not indifference (Ps. 4:8)."
- "He grounded the divine prerogative of rebuking the sea in the Old Testament (Ps. 107; Job 38)."
- "He briefly connected the passage to Paul's argument in Romans 8."

### What is NOT a personality moment

A common failure mode is over-italicizing. These do **not** get callout treatment:
- "He read the passage." (just say it in prose, or skip)
- "He outlined three points." (just say it in prose)
- "He emphasized verse 38." (just say it in prose, or work the emphasis into the paragraph)

A callout is for something a leader would want to *recall and reference*, not for narrating sermon mechanics.

### Discipline

Personality callouts and non-Scripture quote callouts should average **no more than two per paragraph** in the walk-through. If you find yourself wanting more, you're probably treating ordinary sermon mechanics as moments. Demote them to prose or cut.

## Length target

The guide is published as a 2-page printed handout. The companion `church-pdf-render` skill handles the layout and includes an auto-tighten retry that absorbs small length variance.

**Operationally: aim for ~900 words total, with a soft ceiling around 1,100.**

That's the band where the renderer reliably produces a clean 2-page PDF. The renderer can absorb modest overflow (it auto-tightens the layout once if the first pass spills to a third page), but it cannot rescue a 1,500-word guide from running long. Density beats comprehensiveness. If a sermon is unusually rich, cut a discussion question or compress a walk-through paragraph before exceeding the ceiling. If a sermon is unusually thin, you may go shorter — there is no minimum.

When trimming, the priority order from least cuttable to most cuttable:
1. Personality callouts in the walk-through (these are the highest-value, hardest to recover)
2. Non-Scripture quote callouts (also high value)
3. The walk-through prose around the callouts (compressible)
4. Discussion questions beyond the third
5. Theological anchor points beyond the third

## Tone and voice

- Write *for the leader*, not *about the sermon*. The guide is a tool, not a book report.
- Match the church's register as you've calibrated it in `church-context.md`: warm, direct, scripturally grounded, no churchy throat-clearing.
- Refer to the preacher by first name on second reference (e.g., a first name after the first introduction with title). If the preacher is unnamed in the transcript or unfamiliar, use "the preacher" or "the speaker."
- Don't editorialize on the sermon's quality. Don't add theology the sermon didn't make.
- When the preacher cites a source (a theologian, an author, a Bible commentator, a hymn), name the source in the guide. This is one of the highest-value things you can do.

## What to actively avoid

These are the failure modes that make AI sermon guides feel useless. Avoid them:

- **Flattening to a generic theological summary.** If the guide could plausibly have been written from a one-line description of the sermon's topic, it has failed.
- **Padding the questions with "how does this make you feel" or "what is one thing you can do this week."** These are the discussion-question equivalent of stock photos.
- **Questions that telegraph their own answer.** "Would the answer still hold if the boat had gone down?" is leading; a small group leader can already feel the expected response. Better: "When has God answered a prayer in a way that made him seem bigger and more unsettling, not safer?" — a real question with no rehearsed answer.
- **Dropping the personality moments.** The anecdote about the preacher's grandfather, the off-hand reference to a Tim Keller sermon, the joke about local weather — these are load-bearing for memory and connection. They go in.
- **Hedging.** "Some Christians believe..." "It could be argued..." Not the register here. The sermon made claims; reflect them.
- **Inventing.** If the transcript doesn't support a quote, an illustration, or a theological move, don't supply one from your own knowledge of the topic.

## When the transcript is rough

Sermon transcripts are often auto-generated and messy: missing punctuation, garbled proper nouns, no speaker labels, repeated filler words, sometimes auto-translated from a different language. Work with what's there:

- If a quoted source is mangled (e.g., "Bond Hoffer"), use your judgment to identify it (Bonhoeffer) and render it correctly. If you're not confident, render it phonetically and flag it parenthetically.
- If proper nouns appear in another language because of auto-translation (e.g., a sermon transcript that was OCR'd in Spanish translates "Achan" as "Eakon" or "Hulen Street" as "Hewland Street"), render them in their standard English forms.
- If you can't tell whether something is a quote, an anecdote, or a riff, mark it as a "moment" rather than miscategorizing it.
- If the transcript is too fragmentary to identify a coherent sermon arc, say so plainly at the top of the output and produce what you can.
