# Short links

Run `python tools/generate-shortlinks.py` to rebuild them. A GitHub Action (`.github/workflows/shortlinks.yml`) does this
automatically whenever the Discovery Lab folder changes.

- `morehumaned.com/dl/<name>` opens a Discovery Lab activity. `<name>` is the activity folder without its `sim-` or `ext-` prefix.
  Example: `/dl/computer-maintenance-troubleshooting`
- `/dl`, `/dl/primary`, `/dl/secondary`, `/dl/about`
- `/pilot`, `/tutorials`, `/videos`, `/about`, `/privacy`, `/workshops`, `/talk` (booking page)
- Spanish: `/piloto`, `/talleres`, `/sobre`

They are small redirect pages (GitHub Pages cannot do server redirects). They are marked noindex and point search engines at the long address.
The generator only manages the folders listed in `.shortlinks-manifest`. It never touches `discovery-lab/`.
