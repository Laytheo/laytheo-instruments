#!/usr/bin/env python3
"""
church-pdf-render build script.

Renders a small group guide markdown file (output of the
small-group-guide skill, or any markdown matching its
schema) as a branded PDF for a local church.

Configuration lives in `church-config.yaml` next to this script.

Usage:
    python3 build.py <input.md> [output.pdf] [--html-only]
    python3 build.py --check        # run preflight diagnostics, no render
    python3 build.py --version      # print version info

If output.pdf is omitted, writes to /mnt/user-data/outputs/{stem}.pdf
when that directory exists, otherwise next to the input file.
"""

from __future__ import annotations

import argparse
import base64
import glob
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VERSION = "1.0.0"

SKILL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SKILL_DIR / "church-config.yaml"
TEMPLATE_PATH = SKILL_DIR / "template.html"
STYLE_TEMPLATE_PATH = SKILL_DIR / "assets" / "style.css.j2"
LOGO_PATH = SKILL_DIR / "assets" / "logo.png"

REQUIRED_SECTIONS = [
    "This week's big idea",
    "Theological anchor points",
    "Discussion questions",
    "Sermon walk-through",
]

# CSS variable overrides applied on the auto-tighten retry pass.
# These deltas were calibrated to recover ~1 page of vertical space.
TIGHTEN_OVERRIDES = """
:root {
    --body-size: 9.5pt;
    --body-leading: 1.4;
    --h2-top: 12pt;
    --walk-gap: 5pt;
}
"""


# ---------------------------------------------------------------------------
# Friendly dependency import
# ---------------------------------------------------------------------------

def _missing_dep(name: str, install_hint: str) -> "None":
    print(
        f"ERROR: Required Python package '{name}' is not installed.\n"
        f"Install it with:\n  {install_hint}",
        file=sys.stderr,
    )
    sys.exit(2)


try:
    import markdown as md_lib  # type: ignore
except ImportError:
    _missing_dep("markdown", "pip install --break-system-packages markdown")

try:
    from jinja2 import Template, Environment  # type: ignore
except ImportError:
    _missing_dep("jinja2", "pip install --break-system-packages jinja2")

# Custom Jinja Environment for the CSS template. CSS uses `{` and `}` as
# block delimiters, so we use `[[ ... ]]` for the CSS template instead of
# the default `{{ ... }}`. The HTML template uses standard delimiters.
CSS_JINJA_ENV = Environment(
    variable_start_string="[[",
    variable_end_string="]]",
    block_start_string="[%",
    block_end_string="%]",
    comment_start_string="[#",
    comment_end_string="#]",
)

try:
    import yaml  # type: ignore
except ImportError:
    _missing_dep("PyYAML", "pip install --break-system-packages PyYAML")


# ---------------------------------------------------------------------------
# Configuration loading
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "church": {
        "name": "Example Community Church",
        "location": "City, State",
    },
    "theme": {
        "accent_color": "#BA7433",
        "callout_italic_color": "#5a3d1f",
        "body_font": "'Source Serif Pro', 'Source Serif 4', 'Charter', 'Iowan Old Style', Georgia, serif",
        "heading_font": "'Inter', 'Helvetica Neue', Arial, sans-serif",
        "google_fonts_url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400&display=swap",
    },
    "masthead": {
        "eyebrow": "Small Group Guide",
    },
    "footer": {
        "text": None,
    },
}


def deep_merge(base: dict, overlay: dict) -> dict:
    """Merge overlay into base recursively. Overlay values win when not None."""
    result = {k: (v.copy() if isinstance(v, dict) else v) for k, v in base.items()}
    for k, v in (overlay or {}).items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = deep_merge(result[k], v)
        elif v is not None:
            result[k] = v
    return result


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(
            f"WARNING: {CONFIG_PATH} not found. Using default values.\n"
            f"Copy church-config.yaml from the skill repo and customize it for your church.",
            file=sys.stderr,
        )
        return DEFAULT_CONFIG
    try:
        loaded = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        sys.exit(f"ERROR: church-config.yaml is not valid YAML: {exc}")
    if not isinstance(loaded, dict):
        sys.exit("ERROR: church-config.yaml must be a YAML mapping at the top level.")
    return deep_merge(DEFAULT_CONFIG, loaded)


def derive_footer_text(config: dict) -> str:
    explicit = config.get("footer", {}).get("text")
    if explicit:
        return explicit
    name = config["church"]["name"]
    eyebrow = config["masthead"]["eyebrow"]
    return f"{name}  ·  {eyebrow}"


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def parse_guide(text: str) -> dict:
    lines = text.splitlines()

    title = None
    byline = None
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            body_start = i + 1
            continue
        if title is not None and line.strip().startswith("*") and line.strip().endswith("*"):
            byline = line.strip().strip("*").strip()
            body_start = i + 1
            break
        if title is not None and line.strip():
            body_start = i
            break

    if title is None:
        sys.exit("ERROR: Could not find H1 title in guide markdown.")
    if byline is None:
        sys.exit("ERROR: Could not find italic byline line ('*Preached by ...*') after title.")

    preacher, date_label, scripture = parse_byline(byline)
    sections = split_h2_sections(lines[body_start:])

    missing = [s for s in REQUIRED_SECTIONS if s not in sections]
    if missing:
        sys.exit(f"ERROR: Guide markdown is missing required H2 section(s): {missing}")

    return {
        "title": title,
        "preacher": preacher,
        "date_label": date_label,
        "scripture": scripture,
        "big_idea_html": render_paragraphs(sections["This week's big idea"]),
        "anchors": parse_unordered_list(sections["Theological anchor points"]),
        "questions": parse_ordered_list(sections["Discussion questions"]),
        "walkthrough_html": render_paragraphs(sections["Sermon walk-through"]),
    }


def parse_byline(byline: str):
    if "|" not in byline:
        sys.exit(f"ERROR: Byline missing '|' separator: {byline!r}")
    left, right = [p.strip() for p in byline.split("|", 1)]
    scripture = right
    m = re.match(r"^Preached by\s+(.+?)(?:\s+on\s+(.+))?$", left)
    if not m:
        sys.exit(f"ERROR: Could not parse byline: {byline!r}")
    preacher = m.group(1).strip()
    date_label = m.group(2).strip() if m.group(2) else None
    return preacher, date_label, scripture


def split_h2_sections(lines):
    sections, current, buffer = {}, None, []

    def flush():
        if current is not None:
            sections[current] = buffer.copy()

    for line in lines:
        if line.startswith("## "):
            flush()
            current = line[3:].strip()
            buffer = []
        else:
            buffer.append(line)
    flush()
    return sections


def parse_unordered_list(lines):
    items, current = [], []
    for line in lines:
        if re.match(r"^\s*[-*]\s+", line):
            if current:
                items.append(render_inline(" ".join(current).strip()))
            current = [re.sub(r"^\s*[-*]\s+", "", line)]
        elif line.strip() and current:
            current.append(line.strip())
        elif not line.strip() and current:
            items.append(render_inline(" ".join(current).strip()))
            current = []
    if current:
        items.append(render_inline(" ".join(current).strip()))
    return items


def parse_ordered_list(lines):
    items, current = [], []
    for line in lines:
        if re.match(r"^\s*\d+\.\s+", line):
            if current:
                items.append(render_inline(" ".join(current).strip()))
            current = [re.sub(r"^\s*\d+\.\s+", "", line)]
        elif line.strip() and current:
            current.append(line.strip())
        elif not line.strip() and current:
            items.append(render_inline(" ".join(current).strip()))
            current = []
    if current:
        items.append(render_inline(" ".join(current).strip()))
    return items


def render_inline(text: str) -> str:
    html = md_lib.markdown(text)
    return re.sub(r"^\s*<p>(.*)</p>\s*$", r"\1", html, flags=re.DOTALL)


def render_paragraphs(lines) -> str:
    text = "\n".join(lines).strip()
    return md_lib.markdown(text) if text else ""


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def load_logo_data_uri(*, verbose: bool = False) -> "str | None":
    if not LOGO_PATH.exists():
        print(
            f"WARNING: {LOGO_PATH} not found. Falling back to text wordmark.\n"
            f"Place your church logo at {LOGO_PATH} (PNG, transparent background recommended, "
            f"~240px tall at 2x for crisp PDF rendering).",
            file=sys.stderr,
        )
        return None
    data = LOGO_PATH.read_bytes()
    size_kb = len(data) // 1024
    if verbose:
        print(f"Logo: {LOGO_PATH} ({size_kb} KB)", file=sys.stderr)
    if size_kb > 2000:
        print(
            f"WARNING: Logo is {size_kb} KB. That's much larger than needed for a 40pt-tall "
            f"masthead element. Consider downsizing to keep PDF file sizes reasonable.",
            file=sys.stderr,
        )
    b64 = base64.b64encode(data).decode("ascii")
    suffix = LOGO_PATH.suffix.lstrip(".").lower()
    mime = "image/png" if suffix == "png" else f"image/{suffix}"
    return f"data:{mime};base64,{b64}"


def render_stylesheet(config: dict, footer_text: str) -> str:
    template = CSS_JINJA_ENV.from_string(STYLE_TEMPLATE_PATH.read_text(encoding="utf-8"))
    return template.render(
        accent_color=config["theme"]["accent_color"],
        callout_italic_color=config["theme"]["callout_italic_color"],
        body_font=config["theme"]["body_font"],
        heading_font=config["theme"]["heading_font"],
        footer_text=footer_text,
    )


def render_html(fields: dict, config: dict, *, tighten: bool = False) -> str:
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    footer_text = config["footer"]["text"] or derive_footer_text(config)
    return template.render(
        stylesheet=render_stylesheet(config, footer_text),
        tighten_overrides=TIGHTEN_OVERRIDES if tighten else "",
        logo_data_uri=load_logo_data_uri(),
        google_fonts_url=config["theme"]["google_fonts_url"],
        church_name=config["church"]["name"],
        church_location=config["church"]["location"],
        masthead_eyebrow=config["masthead"]["eyebrow"],
        **fields,
    )


def find_chrome(*, verbose: bool = False) -> str:
    """
    Locate a Chrome or Chromium binary.

    Order matters: prefer browsers installed under the current user's cache
    (works in Anthropic's claude.ai sandbox), then system-wide installs
    (works on a developer's local machine).
    """
    candidates: list[str] = []
    candidates += sorted(glob.glob(str(Path.home() / ".cache/puppeteer/chrome/linux-*/chrome-linux64/chrome")), reverse=True)
    candidates += sorted(glob.glob("/root/.cache/puppeteer/chrome/linux-*/chrome-linux64/chrome"), reverse=True)
    candidates += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"), reverse=True)
    candidates += sorted(glob.glob(str(Path.home() / ".cache/ms-playwright/chromium-*/chrome-linux/chrome")), reverse=True)
    candidates += [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in candidates:
        path = c if "/" in c and Path(c).exists() else (shutil.which(c) if "/" not in c else None)
        if path:
            if verbose:
                print(f"Chrome: {path}", file=sys.stderr)
            return path
    sys.exit(
        "ERROR: Could not find Chrome or Chromium. Install one of:\n"
        "  Linux Mint / Ubuntu:  sudo apt install chromium\n"
        "  macOS:                brew install --cask google-chrome\n"
        "  Cross-platform:       pip install playwright && playwright install chromium"
    )


def render_pdf(html: str, output_path: Path) -> None:
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_html = Path(tmpdir) / "guide.html"
        tmp_html.write_text(html, encoding="utf-8")
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={output_path}",
            f"file://{tmp_html.resolve()}",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if not output_path.exists():
            sys.exit(
                f"ERROR: Chrome failed to render PDF.\n"
                f"stdout: {result.stdout}\n"
                f"stderr: {result.stderr}"
            )


def page_count(pdf_path: Path) -> int:
    try:
        import pypdfium2 as pdfium  # type: ignore
        pdf = pdfium.PdfDocument(str(pdf_path))
        try:
            return len(pdf)
        finally:
            pdf.close()
    except ImportError:
        pass
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        result = subprocess.run([pdfinfo, str(pdf_path)], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":", 1)[1].strip())
    print(
        "WARNING: Could not count pages (no pypdfium2 or pdfinfo). Auto-tighten retry skipped.",
        file=sys.stderr,
    )
    return -1


# ---------------------------------------------------------------------------
# Doctor / preflight
# ---------------------------------------------------------------------------

def doctor() -> int:
    """Run preflight checks and report status. Returns shell-style exit code."""
    print("church-pdf-render preflight check")
    print("=" * 40)
    failures = 0

    # Skill files
    for label, path in [
        ("SKILL.md", SKILL_DIR / "SKILL.md"),
        ("template.html", TEMPLATE_PATH),
        ("style.css.j2", STYLE_TEMPLATE_PATH),
        ("church-config.yaml", CONFIG_PATH),
    ]:
        if path.exists():
            print(f"  [ok]   {label}")
        else:
            print(f"  [FAIL] {label} missing at {path}")
            failures += 1

    # Logo
    if LOGO_PATH.exists():
        size_kb = LOGO_PATH.stat().st_size // 1024
        note = ""
        if size_kb > 2000:
            note = f" (warning: {size_kb} KB is larger than needed)"
        print(f"  [ok]   logo at {LOGO_PATH} ({size_kb} KB){note}")
    else:
        print(f"  [WARN] no logo at {LOGO_PATH}")
        print(f"         The renderer will fall back to a text wordmark.")
        print(f"         Place your church logo there (PNG, transparent bg recommended).")

    # Config
    try:
        config = load_config()
        print(f"  [ok]   config loaded: {config['church']['name']} ({config['church']['location']})")
        print(f"         accent color:  {config['theme']['accent_color']}")
    except SystemExit as e:
        print(f"  [FAIL] config: {e}")
        failures += 1

    # Python deps (if we got here, markdown/jinja2/yaml all imported)
    print(f"  [ok]   Python deps: markdown, jinja2, PyYAML")

    # Optional: pypdfium2 for page count
    try:
        import pypdfium2  # noqa: F401
        print(f"  [ok]   pypdfium2 (page-count check)")
    except ImportError:
        if shutil.which("pdfinfo"):
            print(f"  [ok]   pdfinfo (page-count check, pypdfium2 not installed)")
        else:
            print(f"  [WARN] no page-count tool (pypdfium2 or pdfinfo)")
            print(f"         Auto-tighten retry will be skipped if a guide overflows.")
            print(f"         Install with: pip install --break-system-packages pypdfium2")

    # Chrome / Chromium
    try:
        chrome = find_chrome(verbose=False)
        print(f"  [ok]   Chrome / Chromium: {chrome}")
    except SystemExit as e:
        print(f"  [FAIL] Chrome / Chromium not found")
        print(f"         {e}")
        failures += 1

    print("=" * 40)
    if failures == 0:
        print("All checks passed.")
        return 0
    print(f"{failures} check(s) failed. Resolve them before rendering.")
    return 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def resolve_output_path(input_path: Path, html_only: bool) -> Path:
    """Pick a sensible default output path."""
    suffix = ".html" if html_only else ".pdf"
    sandbox_outputs = Path("/mnt/user-data/outputs")
    if sandbox_outputs.exists():
        return sandbox_outputs / f"{input_path.stem}{suffix}"
    return input_path.parent / f"{input_path.stem}{suffix}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--check", action="store_true", help="Run preflight diagnostics and exit")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    parser.add_argument("--html-only", action="store_true", help="Write HTML instead of PDF (debugging)")
    parser.add_argument("input", type=Path, nargs="?", help="Path to the guide markdown file")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        default=None,
        help="Path to write the PDF (default: /mnt/user-data/outputs/{stem}.pdf "
             "if available, else next to the input file)",
    )
    args = parser.parse_args()

    if args.version:
        print(f"church-pdf-render {VERSION}")
        return

    if args.check:
        sys.exit(doctor())

    if args.input is None:
        parser.error("input markdown file is required (or use --check)")
    if not args.input.exists():
        sys.exit(f"ERROR: Input file not found: {args.input}")

    config = load_config()

    text = args.input.read_text(encoding="utf-8")
    fields = parse_guide(text)

    output_path = args.output or resolve_output_path(args.input, args.html_only)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if args.html_only:
        html = render_html(fields, config, tighten=False)
        output_path.write_text(html, encoding="utf-8")
        print(f"Wrote HTML: {output_path}")
        return

    # Pass 1: render at default layout
    html = render_html(fields, config, tighten=False)
    render_pdf(html, output_path)
    pages = page_count(output_path)
    print(f"First pass: {pages if pages > 0 else '?'} page(s) -> {output_path}")

    # Pass 2: auto-tighten if overflow
    if pages > 2:
        print("Overflow detected; re-rendering with tightened layout.")
        html = render_html(fields, config, tighten=True)
        render_pdf(html, output_path)
        pages = page_count(output_path)
        print(f"Tightened pass: {pages} page(s) -> {output_path}")
        if pages > 2:
            print(
                "WARNING: Guide still exceeds 2 pages after tightening. "
                "Content may need to be trimmed.",
                file=sys.stderr,
            )

    size_kb = output_path.stat().st_size // 1024
    print(f"Done. {output_path} ({size_kb} KB, {pages if pages > 0 else '?'} page(s))")


if __name__ == "__main__":
    main()
