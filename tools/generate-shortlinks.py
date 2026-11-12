"""Generates short links for morehumaned.com (the Discovery Lab and service links were removed in the 2026-11 repositioning). Run: python tools/generate-shortlinks.py

GitHub Pages cannot do server redirects, so each short link is a tiny page at /<code>/index.html that sends the
visitor on (meta refresh + script, no flash of content). Search engines are told the long address is the real one.

  /dl/<name>   one page per Discovery Lab activity (name = activity folder without the sim-/ext- prefix)
  /dl/primary, /dl/secondary, /dl/about
  /pilot /tutorials /about /privacy /workshops /talk /videos and Spanish /piloto /talleres /sobre

Safe to re-run any time: it deletes and rebuilds /dl and the other short-link folders it owns. It never touches
discovery-lab/ itself (that folder is synced automatically from the Discovery Lab project)."""
import os, re, shutil, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://morehumaned.com"
CAL = "https://cal.com/morehumaned/talk"
GENERATED = os.path.join(ROOT, ".shortlinks-manifest")  # list of folders this script owns, so a re-run can clean up

PAGE = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Redirecting | MoreHuman Ed</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{abs}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace({js}+location.search+location.hash)</script>
<style>body{{font:16px/1.5 system-ui,sans-serif;background:#F3F4F2;color:#2B3036;display:grid;place-items:center;min-height:100vh;margin:0}}a{{color:#23706D}}</style>
</head><body><p>Taking you to <a href="{target}">{label}</a>&hellip;</p></body></html>
'''

def w(rel, target, label):
    absu = target if target.startswith("http") else DOMAIN + target
    path = os.path.join(ROOT, rel, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PAGE.format(abs=absu, target=H.escape(target, quote=True), js=repr(target).replace("'", '"'), label=H.escape(label)))

links = {}   # short path -> (target, label)

# --- main site (kept deliberately small)
for code, target, label in [
    ("tutorials", "/en/tutorials.html", "the videos"), ("videos", "/en/tutorials.html", "the videos"),
    ("about", "/en/about.html", "About Diego"), ("privacy", "/en/privacy.html", "About this site"),
]:
    links[code] = (target, label)
seen = {}

# --- rebuild
old = []
if os.path.exists(GENERATED):
    old = [l.strip() for l in open(GENERATED, encoding="utf-8") if l.strip()]
for folder in old:                              # remove what a previous run made (only folders listed in the manifest)
    p = os.path.join(ROOT, folder)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, "index.html")) and "Redirecting | MoreHuman Ed" in open(os.path.join(p, "index.html"), encoding="utf-8").read():
        shutil.rmtree(p)
for rel, (target, label) in sorted(links.items()):
    w(rel, target, label)
with open(GENERATED, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(sorted(links)) + "\n")
print(f"ok {len(links) + 1} short links ({len(seen)} Discovery Lab activities)")
