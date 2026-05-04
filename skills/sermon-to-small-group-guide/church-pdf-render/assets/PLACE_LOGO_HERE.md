# Place your church logo here

The build script looks for `logo.png` in this folder. If it's not present,
the renderer falls back to a text wordmark (your church's name from
`church-config.yaml`).

Recommended logo specs:

- PNG format with transparent background
- ~240 × 240 pixels or larger (the renderer scales down to 40pt tall)
- Under 500 KB
- Filename **must** be exactly `logo.png` (lowercase, single .png extension)

To verify your logo is being picked up correctly, run:

    python3 build.py --check

from the parent folder.
