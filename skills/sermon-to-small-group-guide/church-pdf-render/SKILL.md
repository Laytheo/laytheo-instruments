---
name: church-pdf-render
description: Render a finished small group guide markdown file into a branded PDF for a local church. Use this skill whenever a user has a small group guide written in markdown (typically the output of the small-group-guide skill) and wants the publication-ready PDF, or whenever the user mentions "make the PDF," "render the guide," or wants to give small group leaders a printable handout. Trigger this even if the user just pastes a guide markdown without explicit instructions; if it has the small-group-guide structure, the most likely intent is to render it.
---

# Church Small Group Guide PDF Renderer

## What this skill does

Takes a small group guide written in the standardized markdown format (the output of the `small-group-guide` skill) and renders it as a branded 2-page PDF for a local church. Theme values (church name, location, accent color, fonts, logo) are read from `church-config.yaml` at the skill root, so the same skill works for any congregation that customizes the config.

The script targets a 2-page PDF. If the rendered output spills onto a 3rd page, it automatically retries once with a tightened layout (smaller body, tighter leading, tighter section margins). If it still spills, it warns but writes the PDF anyway.

## Setup before first use

This skill requires three things to be set up by the user (one time):

1. **Customize `church-config.yaml`** — fill in your church's name, location, accent color, and fonts. See the comments in that file for guidance.
2. **Place your church's logo at `assets/logo.png`** — PNG with transparent background recommended, ~240px tall at 2x for crisp PDF rendering. If missing, the renderer falls back to a text wordmark and warns.
3. **Verify the install with `python3 build.py --check`** — this preflights all dependencies, the logo, the config, and the Chrome binary, and reports what's missing without rendering anything.

See `README.md` in this folder for full setup instructions including dependency installation.

## Input contract

The input is a markdown file matching the schema produced by `small-group-guide`:

```markdown
# {Title}
*Preached by {Preacher} on {Date} | {Scripture reference}*

## This week's big idea
{One paragraph}

## Theological anchor points
- {Bullet 1}
- {Bullet 2}

## Discussion questions
1. {Question}
2. {Question}

## Sermon walk-through
{Multiple paragraphs, with italic callouts using *...* syntax}
```

The H1 line is the title. The italic byline contains preacher and scripture separated by `|`. The four H2 sections are stable. Walk-through paragraphs may contain `*italic*` callouts.

The "on {Date}" segment in the byline is optional.

## How to use this skill

1. Locate the markdown guide. It will be either at `/mnt/user-data/uploads/` or already in the working directory. If only raw guide text was pasted in chat, write it to a file in `/home/claude/` first.
2. Run the build script:
   ```bash
   python3 /path/to/skill/build.py <input.md> [output.pdf]
   ```
   If `<output.pdf>` is omitted, the script writes to `/mnt/user-data/outputs/{stem}.pdf` when available, otherwise next to the input file. The `--html-only` flag may appear in any position for layout debugging.
3. Use `present_files` to surface the PDF.

## Files in this skill

- `SKILL.md` — this file
- `README.md` — installation and setup instructions for users
- `church-config.yaml` — user-customized theme and brand values
- `build.py` — markdown parser and Chrome headless renderer with auto-tighten retry
- `template.html` — Jinja2 template for the document
- `assets/style.css.j2` — CSS template (theme values interpolated from config)
- `assets/logo.png` — user-provided church logo

## Auto-tighten retry

The default layout targets ~900 body words on 2 pages. If the rendered PDF spills to 3 pages, the script re-renders once with these CSS variable overrides:

- `--body-size`: 10pt → 9.5pt
- `--body-leading`: 1.45 → 1.4
- `--h2-top`: 16pt → 12pt
- `--walk-gap`: 7pt → 5pt

If it still spills, the script writes the PDF anyway and prints a warning suggesting the content be trimmed.

## Diagnostics

The build script supports `--check` (run preflight diagnostics with no render) and `--version`. Use `--check` whenever something seems off — it will tell you whether the config is parseable, whether the logo is the expected shape, whether Chrome was found and where, and whether page-count tools are available.

## Locked design tokens

Most layout values are locked and not exposed in the config, because the design was calibrated as a unit. Specifically: page geometry (US Letter, 0.6/0.8/0.7 inch margins), section heading style, big-idea callout treatment, anchor-point bullets, question numbering, drop cap, page-break hygiene, and the secondary text color. If you need to change these, fork the skill and edit the CSS template.

What's exposed in the config: church name, location, masthead eyebrow text, footer text, accent color, callout italic color, body font stack, heading font stack, Google Fonts URL.
