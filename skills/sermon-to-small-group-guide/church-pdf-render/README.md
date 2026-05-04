# church-pdf-render

A Claude skill that turns a small group guide markdown file into a branded
2-page PDF for your church. Designed to pair with the `small-group-guide`
skill, but works with any markdown matching its schema.

## What you get

- A printed-quality 2-page PDF: copper-accent masthead with your logo,
  serif title, copper section headings, big-idea callout, drop cap on the
  walk-through, italic personality callouts in warm brown, page footer
  with church name and page number, and a centered colophon at the end.
- All theme values (name, location, accent color, fonts) configurable via
  a single YAML file. No CSS editing required for a basic install.
- An auto-tighten retry: if a guide overflows to a third page, the renderer
  reruns at slightly smaller body size and tighter leading. Most guides
  fit on two pages without this; the retry catches the edge cases.
- A `--check` diagnostic mode that verifies your install before you render.

---

## First-time setup

You'll need to do five things, once:

### 1. Get the skill folder onto your computer

Download the zip (or clone this repo) and unzip it somewhere you'll remember.
You should see this structure:

```
church-pdf-render/
├── SKILL.md
├── README.md            ← you are here
├── church-config.yaml   ← you'll edit this
├── build.py
├── template.html
└── assets/
    ├── style.css.j2
    └── logo.png         ← you'll replace this
```

### 2. Replace the logo

Open the `assets/` folder. Replace `logo.png` with your church's logo.

The replacement file **must be named exactly `logo.png`** (lowercase, single
extension). If your download named it something like `logo (1).png` or
`Logo.PNG`, rename it.

Recommended logo specs:

- PNG format with transparent background
- Around 240 × 240 pixels, or larger (the renderer scales down to 40pt tall;
  starting at 2× that gives crisp output)
- Under 500 KB (the renderer warns if your file is over 2 MB)

If you don't have a logo handy, you can skip this step. The renderer will
fall back to a text wordmark (your church's name in copper caps).

### 3. Edit `church-config.yaml`

Open `church-config.yaml` in any text editor. The file has comments
explaining each field. At minimum, set:

- `church.name` — your church's name
- `church.location` — city and state/region

If you want to use a different accent color than the default copper
(`#BA7433`), set `theme.accent_color` to your hex color. Pick a single
distinctive color; the design uses this color in many places, and adding a
second accent flattens the first.

Save the file.

### 4. Install dependencies

You need Python 3.10+ and three Python packages:

```bash
pip install --break-system-packages markdown jinja2 PyYAML
```

(The `--break-system-packages` flag is needed on some recent Linux distros.
On macOS or Windows, you can drop it.)

You also need a Chrome or Chromium browser somewhere the script can find it.
On a typical desktop:

- **Linux Mint / Ubuntu / Debian:** `sudo apt install chromium`
- **macOS:** `brew install --cask google-chrome` (or have Chrome already)
- **Windows:** Chrome is usually already on PATH if installed normally

If you don't have admin rights or want a self-contained install, Playwright
will download a managed Chromium for you:

```bash
pip install --break-system-packages playwright
playwright install chromium
```

The script auto-discovers Chromium in this order: Puppeteer cache, Playwright
cache, system PATH, macOS standard install path.

For the auto-tighten retry to work you also need `pypdfium2`:

```bash
pip install --break-system-packages pypdfium2
```

This is optional but recommended. If neither `pypdfium2` nor `pdfinfo` is
available, the script can still render, but it can't detect overflow.

### 5. Verify the install

Run the doctor:

```bash
python3 build.py --check
```

You should see something like:

```
church-pdf-render preflight check
========================================
  [ok]   SKILL.md
  [ok]   template.html
  [ok]   style.css.j2
  [ok]   church-config.yaml
  [ok]   logo at /path/to/assets/logo.png (24 KB)
  [ok]   config loaded: First Baptist Church (Springfield, IL)
         accent color:  #BA7433
  [ok]   Python deps: markdown, jinja2, PyYAML
  [ok]   pypdfium2 (page-count check)
  [ok]   Chrome / Chromium: /usr/bin/chromium
========================================
All checks passed.
```

If anything fails, the doctor tells you exactly what's wrong and how to fix it.

---

## Using it

Once the install passes the doctor, render a guide:

```bash
python3 build.py path/to/guide.md
```

Output paths:

- If `/mnt/user-data/outputs/` exists (you're running inside a Claude sandbox),
  the PDF goes there with the same stem as the input.
- Otherwise, the PDF is written next to the input file.
- Or pass an explicit output path as the second argument.

For layout debugging, `--html-only` writes HTML instead of running Chrome:

```bash
python3 build.py path/to/guide.md --html-only
```

You can then open the HTML in any browser to see how the layout works without
the print-to-PDF step.

### Running through Claude

If you've installed this as a Claude skill (uploaded the zip via Settings →
Capabilities → Skills), you don't need to run `build.py` directly. Just give
Claude a sermon guide and ask for the PDF, and it will invoke the skill.
Phrases like "make the PDF" or "render the guide" should trigger it.

---

## Customizing the design beyond the config

The config covers the common-case theming: name, location, accent color, fonts.
For deeper changes (different page geometry, different section styling,
different bullet style, etc.), edit the CSS template directly:

```
assets/style.css.j2
```

Most layout values are intentionally locked because the design was tuned as a
unit. If you find yourself wanting to change a lot at once, fork the skill
and customize freely.

---

## Troubleshooting

**`build.py --check` fails with "Chrome / Chromium not found".**
Install one of the options in step 4 above. Re-run `--check` to confirm.

**The PDF renders but looks wrong (broken layout, no logo).**
Run `python3 build.py --check` first; that catches most install issues.
If everything checks out, render with `--html-only` and open the HTML in a
browser to inspect the layout in isolation.

**My logo is showing up at the wrong size.**
The masthead element is a fixed 40pt tall. Logo aspect ratio is preserved.
If your logo is unusually wide or tall, it may look off; consider cropping
or providing a square-ish version.

**The PDF is rendering as 3 pages.**
The auto-tighten retry should have kicked in. If it didn't, check the
console output — you may be missing `pypdfium2` or `pdfinfo`. Install
`pypdfium2` to enable the retry. If the guide is still too long after
tightening, trim a discussion question or compress a walk-through paragraph.

**The page footer is missing in my output.**
This is usually a Chromium version issue. The script uses CSS `@page`
rules for the footer, which Chromium has supported for years. Update
Chromium to a recent version.

**Italic callouts are showing up in my body text color, not warm brown.**
That means `walkthrough em` styling didn't apply. Likely cause: the input
markdown doesn't have the four expected H2 sections in their canonical names,
so the walk-through wasn't detected. Verify your guide markdown matches the
input contract in `SKILL.md`.

**The skill works locally but not in Claude.**
After uploading the zip, the skill needs to be enabled in Claude's UI.
Settings → Capabilities → Skills → toggle it on.

---

## What's hardcoded vs. configurable

| Element | Where it lives |
|---|---|
| Church name | `church-config.yaml` |
| Church location | `church-config.yaml` |
| Logo | `assets/logo.png` |
| Accent color | `church-config.yaml` |
| Italic callout color | `church-config.yaml` |
| Body and heading font stacks | `church-config.yaml` |
| Google Fonts URL | `church-config.yaml` |
| Masthead eyebrow text | `church-config.yaml` |
| Footer text | `church-config.yaml` (defaults to `{name}  ·  {eyebrow}`) |
| Page geometry, margins | `assets/style.css.j2` |
| Section styling | `assets/style.css.j2` |
| Bullet and number styling | `assets/style.css.j2` |
| Drop cap | `assets/style.css.j2` |
| Auto-tighten deltas | `build.py` |

If you find yourself needing to change something not in the config table,
that's a sign you're doing a deeper customization. Fork the skill.

---

## License

[Add your license of choice. Anthropic's Agent Skills are an open standard.]
