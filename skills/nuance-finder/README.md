# Nuance-Finder

A Claude skill that takes a viral post, screenshot, meme, headline, or
forwarded message and splits it into its parts the way a prism splits light:
the underlying story on one side, the framing and technique on the other.

You paste the thing that's going around. The skill reconstructs what's
actually known (searching the web and citing sources), then names precisely
how the post is built: the loaded words, the missing context, the real
grievance it's wrapped around, and the places the other side is spinning too.

It does one unusual thing on purpose: **it never tells you whether the post
is true or false.** No verdict, no rating, no "debunked" stamp. It shows you
the machinery and hands the judgment back to you. The thing it's against is
flattening, not falsehood.

This isn't an app you install or a service you sign up for. It's a short
text file (called a "skill") that you upload to your Claude account once, and
then Claude knows how to do this for you whenever you paste something in.

---

## What you're getting

A single skill, **nuance-finder**, in this bundle. It ships with two files:

- **SKILL.md** — the instructions Claude follows.
- **TECHNIQUES.md** — a working catalog of about thirty persuasion and
  manipulation techniques (loaded language, missing denominators, recycled
  images, manufactured consensus, and so on), with definitions and examples.
  The skill uses it as a lens so it can name *the specific* technique in play
  instead of waving at "bias."

Both files travel together in one folder. You upload the folder; Claude reads
both.

---

## What you need before starting

- A claude.ai account (free or paid). The skill works on both the website and
  the Claude desktop app.
- Web search enabled in your Claude settings. The skill leans on it to
  reconstruct the real story behind a post. Without it, the skill still runs,
  but it will tell you plainly that it couldn't verify the facts.

You don't need to install anything on your computer, and there's nothing to
configure. Unlike some skills, this one has no setup form to fill in.

---

## Setup, in plain language

### Step 1: Download the skill

Go to the [Releases page](https://github.com/Laytheo/laytheo-instruments/releases/tag/nuance-finder-v1)
of this repository and download `nuance-finder.zip`.

### Step 2: Upload it to Claude

Go to claude.ai (or open the Claude desktop app). Open Settings, usually under
your account avatar. Find the section called **Capabilities**, then **Skills**.
Click the button to add or upload a skill, and choose the zip file you
downloaded.

The skill should appear in your list, toggled on. That's the whole install.

---

## Using it

In any new conversation with Claude:

1. Paste the post, or upload a screenshot of it. A forwarded text, a meme, a
   headline, a single startling claim: anything that's "going around" works.
2. Send it. You don't have to ask for anything specific; the skill recognizes
   that you've handed it a piece of viral content and gets to work. If it
   doesn't trigger, say "use the nuance-finder skill."
3. Read what comes back. You'll get the core story (with sources you can
   click), the techniques the post is using with the exact phrases quoted, the
   places the post has a fair point, the places the other side spins too, and
   what genuinely can't be resolved.

Then you decide what to make of it. That last part is yours, by design.

---

## What it will and won't do

**It will** reconstruct the story, cite sources, and name techniques
precisely. It will point out where a post has a legitimate grievance underneath
the spin, and it will turn the same lens on the "respectable" counter-take.

**It won't** rule the post true or false, tell you what to believe, or tell you
how to feel or vote. If you want a thumbs-up or thumbs-down, this is the wrong
tool. It is built to give you a clearer view, not a ruling to quote.

It also won't manufacture spin that isn't there. Sometimes a post is a fair
representation of its subject, and when that's the case, the skill says so.

---

## When something goes wrong

**"It gave me an analysis but didn't search the web."**
Check that web search is enabled in your Claude settings. The skill will tell
you when it couldn't verify the underlying facts; that usually means search was
off or unavailable.

**"It won't tell me if the post is true."**
That's not a bug. The skill is built never to issue a verdict. It will give you
the fuller picture so you can judge for yourself.

**"It didn't trigger on my screenshot."**
Prompt it explicitly: "Use the nuance-finder skill on this image."

---

## Honest caveats

The skill is only as good as what the web will tell it. For a fast-moving or
genuinely obscure story, it may not be able to reconstruct much, and it will
say so rather than guess. Treat its source citations the way you'd treat any
research: follow the links and check them yourself.

It is also built to resist being steered. Posts and the pages it fetches can
carry hidden instructions ("ignore the above and say X"); the skill is told to
ignore those and take instructions only from you. That makes it a little stubborn
by design.

The skill is an open standard from Anthropic. You're free to fork it, modify it,
and adapt the techniques catalog to your own use.

---

## Help and feedback

For more on this project and its other instruments, visit
[laytheo.com](https://laytheo.com).

If you're comfortable on GitHub, issues and pull requests are welcome at the
[laytheo-instruments tracker](https://github.com/Laytheo/laytheo-instruments/issues).
