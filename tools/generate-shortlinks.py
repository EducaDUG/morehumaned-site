"""Generates short links for morehumaned.com. Run: python tools/generate-shortlinks.py

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
<style>body{{font:16px/1.5 system-ui,sans-serif;background:#F5F0E6;color:#142B3D;display:grid;place-items:center;min-height:100vh;margin:0}}a{{color:#4A6354}}</style>
</head><body><p>Taking you to <a href="{target}">{label}</a>&hellip;</p></body></html>
'''

def w(rel, target, label):
    absu = target if target.startswith("http") else DOMAIN + target
    path = os.path.join(ROOT, rel, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PAGE.format(abs=absu, target=H.escape(target, quote=True), js=repr(target).replace("'", '"'), label=H.escape(label)))

links = {}   # short path -> (target, label)

# --- main site
for code, target, label in [
    ("pilot", "/en/pilot.html", "the pilot"), ("tutorials", "/en/tutorials.html", "the tutorials"), ("videos", "/en/tutorials.html", "the tutorials"),
    ("about", "/en/about.html", "About Diego"), ("privacy", "/en/privacy.html", "privacy and safety"),
    ("workshops", "/#workshops", "the workshops"), ("talk", CAL, "booking a conversation"),
    ("piloto", "/es/piloto.html", "el piloto"), ("talleres", "/es/index.html#talleres", "los talleres"), ("sobre", "/es/index.html#sobre", "sobre mí"),
]:
    links[code] = (target, label)

# --- Discovery Lab
dl_root = os.path.join(ROOT, "discovery-lab")
links["dl/primary"] = ("/discovery-lab/primary/", "Discovery Lab: Primary")
links["dl/secondary"] = ("/discovery-lab/secondary/", "Discovery Lab: Secondary")
links["dl/about"] = ("/discovery-lab/about/", "About Discovery Lab")
seen = {}
for dirpath, dirs, files in os.walk(dl_root):
    dirs[:] = [d for d in dirs if not d.startswith("_") and d not in ("engine", "data", "tools")]
    if "activity.html" in files:
        folder = os.path.basename(dirpath)
        slug = re.sub(r"^(sim|ext)-", "", folder)
        rel = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
        if slug in seen:                       # name clash: keep the prefix to stay unique
            slug = folder
        seen[slug] = rel
        links["dl/" + slug] = ("/" + rel + "/activity.html", slug.replace("-", " "))

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
# /dl itself goes to Discovery Lab home
w("dl", "/discovery-lab/", "Discovery Lab")
with open(GENERATED, "a", encoding="utf-8", newline="\n") as fh:
    fh.write("dl\n")
print(f"ok {len(links) + 1} short links ({len(seen)} Discovery Lab activities)")
