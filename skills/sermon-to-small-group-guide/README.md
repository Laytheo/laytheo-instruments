# Church Skills for Claude

Two Claude skills that turn a sermon transcript into a printable, branded
small-group discussion guide for your church.

You give Claude a sermon recording's transcript. The first skill writes the
guide. The second skill renders it as a 2-page PDF in your church's colors,
with your logo. Hand it to small group leaders before Tuesday night.

This isn't an app you install or a service you sign up for. It's two short
text files (called "skills") that you upload to your Claude account once,
and then Claude knows how to do this for you whenever you ask.

---

## What you're getting

There are two skills in this bundle:

**1. small-group-guide.** Reads a sermon transcript and writes
the guide as a Markdown document. The guide has a "big idea," a few
theological anchor points, discussion questions that don't telegraph their
own answers, and a beat-by-beat walk-through of the sermon that preserves
the preacher's anecdotes, jokes, and rhetorical force, so a small group
leader can actually re-encounter the sermon during the week.

**2. church-pdf-render.** Reads the Markdown guide and renders it as a
2-page PDF with your church's branding: logo at the top, your accent color,
your church name in the footer.

The two are designed to chain together. Most of the time you'll give Claude
a transcript, get a guide, glance through it, and ask for the PDF.

---

## What you need before starting

- A claude.ai account (free or paid). The skills work on both the website
  and the Claude desktop app.
- Your church's logo as a PNG file. Transparent background is best. Roughly
  square is best. A few hundred pixels on each side is plenty.
- A few minutes to fill out two short questionnaire-style files (one per
  skill) so Claude knows what church you're at.
- Optional: a hex color code for your church's brand color. If you don't
  know what hex codes are, the bundle ships with a warm copper that works
  fine — you can skip this and come back to it later.

You don't need to install anything on your computer. You don't need to use
a terminal. The "skills" are just folders with text files in them, and
Claude does the actual work.

---

## Setup, in plain language

### Step 1: Download the skills

Go to the [Releases page](https://github.com/Laytheo/laytheo-instruments/releases/tag/sermon-to-small-group-guide-v1) of this repository and download both zip
files: `small-group-guide.zip` and `church-pdf-render.zip`.

Don't unzip them yet. Or if you do unzip them out of habit, you'll need to
re-zip them later before uploading. Either way is fine. Where the zips end
up on your computer doesn't matter; you'll be uploading them to Claude.

### Step 2: Open the first skill and fill it in

Unzip `small-group-guide.zip`. You'll see a folder with three
files inside. Open the file called `church-context.md` in any text editor
your computer has — TextEdit on Mac, Notepad on Windows, Notes will work in
a pinch. The file looks like a form with prompts and answers.

Fill in the answers for your church:

- **Church name** — what your church is called (e.g., "a local church")
- **Church location** — your city and state (e.g., "a US city")
- **Tradition** — your tradition or denomination
  (e.g., "Reformed Baptist," "non-denominational evangelical," "Methodist")
- **Primary teaching pastor** — your pastor's name
- **Congregational vocabulary** — phrases your church uses regularly
  (the file has examples like "the gospel," "the Lord," "brothers and sisters" —
  edit these to match how your church talks)
- **Theological frame** — what your church emphasizes
  (the file has examples — edit them or leave them if they fit)
- **Audience** — who reads the guide (usually small group leaders)

You don't need to be precise or fancy. Claude reads this to calibrate the
voice of the guide. The more specific you are, the better the guide will
match your church's tone.

Save the file when you're done. Close the text editor.

### Step 3: Re-zip the folder

You need the folder to end up back in a zip file before uploading.

- **On Mac:** right-click the `small-group-guide` folder, choose
  "Compress." That makes a zip.
- **On Windows:** right-click the folder, choose "Send to" → "Compressed
  (zipped) folder."

Set the zipped file aside; you'll upload it in a minute.

### Step 4: Open the second skill and fill it in

Unzip `church-pdf-render.zip`. You'll see a folder with several files. Two
of them matter for setup:

**4a. Edit `church-config.yaml`.** Open it in a text editor. The file looks
like a form with prompts. Fill in the values:

- The line with `name:` — put your church's name in quotes
- The line with `location:` — put your city and state in quotes
- The line with `accent_color:` — leave it as `"#BA7433"` for the default
  copper color, or put your church's brand color in if you have one

Other lines control fonts and so on. You can ignore them; the defaults
work. Save the file.

**4b. Replace the logo.** Open the `assets` folder inside the skill folder.
You'll see a file called `PLACE_LOGO_HERE.md` (you can ignore it) and
nothing else.

Put your church's logo file in this folder. The file must be named exactly
`logo.png` — lowercase, with `.png` at the end and nothing else. If your
file is named something else (like `logo (1).png` or `Logo.PNG`), rename
it to `logo.png` first.

If you don't have a logo handy, that's okay. Skip this step. The PDF will
just print your church's name as text in the masthead instead of a logo.

### Step 5: Re-zip the second folder

Same as Step 3. Right-click the `church-pdf-render` folder, compress it
into a zip.

### Step 6: Upload both skills to Claude

Go to claude.ai (or open the Claude desktop app). Open Settings — usually
under your account avatar in the lower-left or top-right depending on the
interface. Look for a section called **Capabilities**, then **Skills**.

Click the button to add or create a skill. Choose to upload a zip file.
Upload `small-group-guide.zip` first. Then repeat for
`church-pdf-render.zip`.

Both skills should appear in your skills list, toggled on.

That's the install. You're done.

---

## Using it

In any new conversation with Claude:

1. Paste your sermon transcript into the message box, or upload it as a
   file. Most churches record sermons and have an auto-generated transcript
   somewhere (YouTube captions, Otter.ai, your media platform). The
   transcript can be messy. Claude handles that.
2. Send the message. You don't have to ask for anything specific. Claude
   will recognize that it's a sermon and produce the guide.
3. When you see the guide, take a moment to read it. If you want to change
   anything, say so in plain English: "make question 3 less pointed,"
   "add a question about prayer," "the pastor's name is the pastor, not
   what you guessed."
4. When the guide looks right, ask for the PDF. Just say "make the PDF" or
   "render this guide." Claude will use the second skill and hand you back
   a downloadable PDF.

The PDF should be ready to print.

---

## When something goes wrong

**"I uploaded the skill but it doesn't seem to be doing anything."**
Check your Skills settings. The skill needs to be toggled on. Sometimes
uploads succeed but the skill stays disabled. If it's on and Claude still
isn't using it, you can prompt it explicitly: "Use the
small-group-guide skill."

**"The guide came out but it doesn't sound like our church."**
Open `church-context.md` again and add more specific language. The
"Congregational vocabulary" section is the one that does the most work.
You'll need to re-zip and re-upload the skill for changes to take effect.

**"The PDF is missing my logo."**
The file inside the zip needs to be at exactly
`assets/logo.png` (lowercase, single `.png` extension). Some zip programs
will save it as `logo (1).png` or similar; rename before re-zipping.

**"The PDF rendered but my color is wrong."**
Open `church-config.yaml`, find the line `accent_color:`, set it to your
hex color in quotes (like `"#1f4e79"` for navy blue). Re-zip, re-upload.

**"The guide is the wrong length."**
The skill targets about a page-and-a-half of body text, which usually fills
two PDF pages. If your guide is too long, ask Claude to "trim a discussion
question" or "shorten the walk-through." If it's too short, the underlying
sermon may have been short — that's fine, the PDF will still look good.

**"I want to change the design more than the config allows."**
The fonts, page size, drop cap, and section styling are locked because
they were tuned together. If you want to change those, you'll need to edit
the CSS file inside the second skill (`assets/style.css.j2`). That's an
intermediate-level task; if you're not comfortable with CSS, ask Claude to
help you change one specific thing at a time.

---

## What if you have a developer friend?

Both skills include a more detailed `README.md` inside the folder, written
for developers. There's also a diagnostic command that runs preflight
checks on the install before you try a real render. If you have someone
technical helping you, point them at the per-skill READMEs.

For everyone else, the steps above are everything you need. Upload the
skills, paste a transcript, get a guide, get a PDF.

---

## Honest caveats

This was built for an evangelical Protestant context with named pastors and
expositional preaching. It will adapt to adjacent traditions (Reformed
Baptist, Anglican, Methodist, non-denominational evangelical) without
trouble. If your church is liturgically very different — Catholic, Orthodox,
Pentecostal, etc. — the guide structure may not fit, and you may need to
edit the underlying skill instructions. That's a more involved customization
and probably needs a developer's help.

The skills are an open standard from Anthropic. You're free to fork them,
modify them, share them, and break them in any way that's useful to your
congregation.

---

## Help and feedback

For more on this project and its other instruments, visit [laytheo.com](https://laytheo.com).

If you're comfortable on GitHub, issues and pull requests are welcome at the [laytheo-instruments tracker](https://github.com/Laytheo/laytheo-instruments/issues).
