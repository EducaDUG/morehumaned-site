"""Generates every page of the MoreHuman Ed site. Run: python tools/generate-pages.py
Content and layout live here. Edit this file, then regenerate; do not hand-edit the generated HTML."""
import os, json, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://morehumaned.com"
CAL = "https://cal.com/morehumaned/talk"
DL = "https://morehumaned.com/discovery-lab/"
MAIL = "mailto:hello@morehumaned.com"  # no longer used on the site
YT = "https://www.youtube.com/@morehumaned"

def w(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)

# ---------- Marks ----------
MARK = '<img class="mark-img" src="../assets/img/logo-mark-128.png" width="54" height="54" alt="">'

DL_MARK = ('<svg class="mark" viewBox="0 0 64 64" role="img" aria-label="Discovery Lab compass">'
           '<circle cx="32" cy="32" r="27" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".28"/>'
           '<circle cx="32" cy="32" r="19" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".18"/>'
           '<circle cx="32" cy="32" r="11" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".12"/>'
           '<g stroke="currentColor" stroke-width="1.5" opacity=".45"><path d="M32 2v7M32 55v7M2 32h7M55 32h7"/></g>'
           '<path d="M32 32 A27 27 0 0 1 53 21" fill="none" stroke="#40634C" stroke-width="2.5" stroke-linecap="round"/>'
           '<circle cx="45" cy="22" r="5" fill="#946A00"/><circle cx="32" cy="32" r="2.5" fill="currentColor"/></svg>')

def hero_visual(labels):
    t, a, j, c = labels
    students = "".join(
        f'<circle cx="{200+80*__import__("math").cos(__import__("math").radians(ang)):.1f}" '
        f'cy="{200+80*__import__("math").sin(__import__("math").radians(ang)):.1f}" r="3.2" fill="currentColor" opacity=".55"/>'
        for ang in range(0, 360, 30))
    return f'''<svg viewBox="-70 -10 540 420" role="img" aria-label="{H.escape(t)} / {H.escape(a)} / {H.escape(j)} / {H.escape(c)}">
<circle cx="200" cy="200" r="165" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".28"/>
<circle cx="200" cy="200" r="122" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".18"/>
<circle cx="200" cy="200" r="80" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".12"/>
<g stroke="currentColor" stroke-width="1.5" opacity=".45" fill="none"><path d="M200 18v26M200 356v26M18 200h26M356 200h26"/></g>
<g class="ring-spin">{students}</g>
<circle class="orbit2" cx="200" cy="200" r="190" fill="none" stroke="var(--signal)" stroke-width="2" stroke-dasharray="2 14" stroke-linecap="round" opacity=".7"/>
<g class="orbit"><path d="M256.4 44.9 A165 165 0 0 1 335 105" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>
<path d="M200 200 L335 105" stroke="var(--accent)" stroke-width="1.5" opacity=".55"/>
<circle class="pulse" cx="335" cy="105" r="9" fill="var(--signal)"/></g>
<circle cx="200" cy="200" r="5.5" fill="currentColor"/>
<text x="200" y="8" text-anchor="middle">{H.escape(t)}</text>
<text x="388" y="204" text-anchor="start">{H.escape(a)}</text>
<text x="200" y="402" text-anchor="middle">{H.escape(j)}</text>
<text x="12" y="204" text-anchor="end">{H.escape(c)}</text></svg>'''

WELCOME_ID = "pWLURit_sOc"
def video_block(title, label, vid=WELCOME_ID, poster="welcome-poster.jpg"):
    return (f'<a class="yt" href="https://youtu.be/{vid}" data-yt="{vid}" aria-label="{label}: {title}">'
            f'<img src="../assets/img/{poster}" width="960" height="540" alt="" loading="lazy">'
            f'<span class="yt__play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></a>')

# Published tutorials, newest first. Add each new video here (after it is public on YouTube).
VIDEOS = [
    dict(id="DT_bx6GEReA", poster="video3-poster.jpg",
         title_en="Turn quick notes into feedback, a weekly planner and a reusable checklist",
         title_es="Convierte notas rápidas en retroalimentación, una agenda semanal y una lista de verificación reutilizable",
         desc_en="Three tips: turning quick marking notes into personal feedback, a weekly planner from a list of tasks, and a checklist from a course presentation.",
         desc_es="Tres consejos: convertir notas rápidas de corrección en retroalimentación personal, una agenda semanal a partir de una lista de tareas y una lista de verificación a partir de una presentación del curso. El vídeo está en inglés."),
    dict(id="0MwhBLxHPfQ", poster="video2-poster.jpg",
         title_en="Email, differentiation and study guides in seconds: the real work is training your AI tools",
         title_es="Correos, diferenciación y guías de estudio en segundos: el verdadero trabajo es entrenar tus herramientas de IA",
         desc_en="Three tips: a warm email to families, one explanation adapted for three learners, and a study guide with quiz questions and a self-assessed activity.",
         desc_es="Tres consejos: un correo cálido a las familias, una explicación adaptada para tres estudiantes y una guía de estudio con cuestionario y una actividad de autoevaluación. El vídeo está en inglés."),
]
def video_cards(lang, start=0):
    out = ""
    for i, v in enumerate([v for v in VIDEOS if v["id"] != "PENDING"]):
        t = v["title_" + lang]; d = v["desc_" + lang]; tag = ("New" if lang == "en" else "Nuevo") if i == 0 else ("Video" if lang == "en" else "Vídeo"); pl = "Play video" if lang == "en" else "Reproducir vídeo"
        out += (f'<article class="reveal" style="--d:{(start+i)*90}ms"><div class="card vcard">{video_block(t, pl, v["id"], v["poster"])}'
                f'<span class="pill tag">{tag}</span><h3 style="font-size:var(--step-1)">{t}</h3><p>{d}</p></div></article>')
    return out

def ba_visual(l_label, r_label, l_cap, r_cap, hint):
    cols = [90, 195, 300, 405, 510]; rows = [118, 218, 318]
    pal = ["#2F7F7C", "#E3B230", "#2B3036", "#7DB5B1", "#2F5871", "#EDC04F", "#2F7F7C", "#2B3036", "#E3B230", "#7DB5B1", "#2F5871", "#2F7F7C", "#EDC04F", "#2B3036", "#E3B230"]
    def person(x, y, fill, cls="", delay=0):
        return (f'<g class="{cls}" style="--dl:{delay}ms"><circle cx="{x}" cy="{y}" r="15" fill="{fill}"/>'
                f'<path d="M{x-25},{y+44} Q{x-25},{y+20} {x},{y+20} Q{x+25},{y+20} {x+25},{y+44} Z" fill="{fill}"/></g>')
    beams = "".join(f'<rect x="{x-44}" y="48" width="88" height="350" rx="10" fill="#2B3036" opacity=".05"/>' for x in cols)
    same = "".join(person(x, y, "#B8BEC0") for y in rows for x in cols)
    left = (f'<svg viewBox="0 0 600 410" role="img" aria-label="{H.escape(l_label)}"><rect x="40" y="18" width="520" height="16" rx="8" fill="#2B3036" opacity=".55"/>'
            f'{beams}{same}</svg>')
    d = 0; lines = ""; people = ""
    for r, y in enumerate(rows):
        for c, x in enumerate(cols):
            col = pal[r * 5 + c]
            lines += f'<path class="ba__flow" d="M300,40 Q{(300+x)//2},{(40+y)//2-18} {x},{y-18}" stroke="{col}"/>'
            people += person(x, y, col, "ba__p", d); d += 160
    path = "M90,118 L195,118 L300,118 L405,118 L510,118 L510,218 L405,218 L300,218 L195,218 L90,218 L90,318 L195,318 L300,318 L405,318 L510,318 L510,218 L405,118 L300,218 L195,118 Z"
    spot = f'<circle class="ba__spot" r="36" fill="none" stroke="#E3B230" stroke-width="4" style="offset-path:path(&quot;{path}&quot;)"/>'
    compass = ('<circle cx="300" cy="40" r="20" fill="#FFFFFF" stroke="#2B3036" stroke-width="2"/>'
               '<path d="M300 26v28M286 40h28" stroke="#2B3036" stroke-width="2"/><circle cx="300" cy="40" r="5" fill="#E3B230"/>')
    right = f'<svg viewBox="0 0 600 410" role="img" aria-label="{H.escape(r_label)}">{lines}{compass}{people}{spot}</svg>'
    return (f'<div class="ba reveal from-right" style="--d:120ms;--pos:50%">'
            f'<div class="ba__stage"><div class="ba__layer ba__a">{left}<span class="ba__tag">{l_label}</span></div>'
            f'<div class="ba__layer ba__b">{right}<span class="ba__tag ba__tag--r">{r_label}</span></div>'
            f'<span class="ba__handle" aria-hidden="true"><i></i></span>'
            f'<input class="ba__range" type="range" min="0" max="100" value="50" aria-label="{H.escape(hint)}"></div>'
            f'<div class="ba__caps"><p>{l_cap}</p><p>{r_cap}</p></div></div>')

def thumb_icon(kind):
    icons = {
        "chat": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 10h32v20H22l-8 7v-7H8z"/><path d="M15 18h18M15 24h11"/></svg>',
        "grid": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="8" y="8" width="14" height="14" rx="2"/><rect x="26" y="8" width="14" height="14" rx="2"/><rect x="8" y="26" width="14" height="14" rx="2"/><circle cx="33" cy="33" r="7"/></svg>',
        "mail": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="11" width="34" height="26" rx="3"/><path d="M8 14l16 12 16-12"/></svg>',
    }
    return f'<div class="thumb">{icons[kind]}</div>'

# ---------- Copy ----------
T = {
"en": dict(
  nav=[("index.html#explore","Ideas"),("tutorials.html","Videos"),("about.html","About"),("privacy.html","About this site")],
  skip="Skip to content", langname="ES", menu="Menu",
  tag="Tips, ideas and reflections on keeping people at the centre of learning.",
  foot_note="A personal, independent project. Nothing here is for sale.",
  foot_cols=[("Explore",[("index.html#explore","Ideas"),("tutorials.html","Videos"),("about.html","About"),("privacy.html","About this site")]),
             ("Elsewhere",[("https://www.youtube.com/@morehumaned","YouTube"),("https://morehumaned.com/discovery-lab/","Discovery Lab")])],
  labels=("Time","Attention","Judgement","Care"),
),
"es": dict(
  nav=[("index.html#explorar","Ideas"),("index.html#tutorials","Vídeos"),("index.html#sobre","Sobre mí"),("../en/privacy.html","Sobre este sitio")],
  skip="Ir al contenido", langname="EN", menu="Menú",
  tag="Ideas, consejos y reflexiones para mantener a las personas en el centro del aprendizaje.",
  foot_note="Un proyecto personal e independiente. Nada aquí está a la venta.",
  foot_cols=[("Explorar",[("index.html#explorar","Ideas"),("index.html#tutorials","Vídeos"),("index.html#sobre","Sobre mí")]),
             ("En otros lugares",[("https://www.youtube.com/@morehumaned","YouTube"),("https://morehumaned.com/discovery-lab/","Discovery Lab"),("../en/privacy.html","Sobre este sitio (en inglés)")])],
  labels=("Tiempo","Atención","Criterio","Cuidado"),
),
}

SWITCH = {("en","index.html"):"../es/index.html", ("es","index.html"):"../en/index.html"}
ALT = {("en","index.html"):("es","index.html"), ("es","index.html"):("en","index.html")}

# ---------- Language flags (as on Discovery Lab) ----------
FLAG_UK = ('<svg viewBox="0 0 60 30" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
           '<clipPath id="fs"><path d="M0,0 v30 h60 v-30 z"/></clipPath><clipPath id="ft"><path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z"/></clipPath>'
           '<g clip-path="url(#fs)"><path d="M0,0 v30 h60 v-30 z" fill="#012169"/>'
           '<path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/>'
           '<path d="M0,0 L60,30 M60,0 L0,30" clip-path="url(#ft)" stroke="#C8102E" stroke-width="4"/>'
           '<path d="M30,0 v30 M0,15 h60" stroke="#fff" stroke-width="10"/><path d="M30,0 v30 M0,15 h60" stroke="#C8102E" stroke-width="6"/></g></svg>')
FLAG_ES = ('<svg viewBox="0 0 60 40" aria-hidden="true" focusable="false"><rect width="60" height="40" fill="#AA151B"/>'
           '<rect y="10" width="60" height="20" fill="#F1BF00"/></svg>')

def lang_switch(lang, sw):
    en_cls = "flag current" if lang == "en" else "flag"
    es_cls = "flag current" if lang == "es" else "flag"
    en_href = "#" if lang == "en" else sw
    es_href = "#" if lang == "es" else sw
    en = (f'<span class="{en_cls}" role="img" aria-label="English" lang="en" aria-current="true">{FLAG_UK}</span>' if lang == "en"
          else f'<a class="{en_cls}" href="{en_href}" hreflang="en" lang="en" aria-label="English" title="English">{FLAG_UK}</a>')
    es = (f'<span class="{es_cls}" role="img" aria-label="Español" lang="es" aria-current="true">{FLAG_ES}</span>' if lang == "es"
          else f'<a class="{es_cls}" href="{es_href}" hreflang="es" lang="es" aria-label="Español" title="Español">{FLAG_ES}</a>')
    return f'<span class="lang-switch" role="group" aria-label="Language">{en}{es}</span>'

def head_and_shell(lang, fname, title, desc, body, bodyclass=""):
    c = T[lang]
    other = "es" if lang == "en" else "en"
    canon = f"{DOMAIN}/{lang}/{fname}"
    if (lang, fname) == ("en", "index.html"):
        canon = f"{DOMAIN}/"
    alt = ""
    if (lang, fname) in ALT:
        al, af = ALT[(lang, fname)]
        alt = (f'<link rel="alternate" hreflang="{lang}" href="{canon}">'
               f'<link rel="alternate" hreflang="{al}" href="{DOMAIN}/{al}/{af}" >'.replace(f"{DOMAIN}/en/index.html", f"{DOMAIN}/") +
               f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">')
    sw = SWITCH.get((lang, fname), f"../{other}/index.html")
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in c["nav"])
    foot = ""
    for ttl, links in c["foot_cols"]:
        foot += f'<div><h4>{ttl}</h4><ul>' + "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in links) + '</ul></div>'
    ld = ""
    org = {"@type": "Organization", "name": "MoreHuman Ed", "url": DOMAIN, "logo": DOMAIN + "/assets/img/logo-mark-512.png",
           "description": "A personal, independent space for tips, ideas and reflections about learning.",
           "founder": {"@type": "Person", "name": "Diego Guevara", "jobTitle": "Science educator"},
           "knowsLanguage": ["en", "es"], "sameAs": [YT]}
    graph = [dict(org, **{"@context": "https://schema.org"})]
    graph.append({"@context": "https://schema.org", "@type": "WebSite", "name": "MoreHuman Ed", "url": DOMAIN, "inLanguage": lang})
    graph.append({"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": canon,
                  "inLanguage": lang, "isPartOf": {"@type": "WebSite", "url": DOMAIN},
                  "accessibilityFeature": ["largePrint", "displayTransformability", "readingOrder", "highContrastDisplay"]})
    ld = "".join('<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False) + '</script>' for g in graph)
    locale = "en_NZ" if lang == "en" else "es_ES"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{canon}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="MoreHuman Ed">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{locale}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3F4F2">
<link rel="alternate" type="text/plain" href="{DOMAIN}/llms.txt" title="llms.txt">
<link rel="icon" type="image/png" sizes="64x64" href="../assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<link rel="preload" href="../assets/fonts/atkinson-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/public-sans-latin-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/tokens.css?v=3">
<link rel="stylesheet" href="../assets/site.css?v=3">
<link rel="stylesheet" href="../assets/motion.css?v=3">
<link rel="stylesheet" href="../assets/brandplus.css?v=3">
<script>document.documentElement.classList.add('js')</script>
{ld}
</head>
<body>
<a class="skip-link" href="#main">{c["skip"]}</a>
<header class="site-head"><div class="shell site-head__inner">
<a class="wordmark" href="index.html">{MARK}<span class="wordmark__text">MoreHuman&nbsp;Ed</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="{c["menu"]}"><span></span></button>
<nav class="nav" id="site-nav" aria-label="Main">{nav}{lang_switch(lang, sw)}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="shell site-foot__inner">
<div><a class="wordmark" href="index.html">{MARK}<span class="wordmark__text">MoreHuman&nbsp;Ed</span></a>
<p style="margin-top:1rem">{c["tag"]}</p><p style="margin-top:.5rem;font-size:.85rem">{c["foot_note"]}</p></div>
{foot}
</div></footer>
<script src="../assets/site.js?v=3" defer></script>
<script src="../assets/motion.js?v=3" defer></script>
<script src="../assets/brandplus.js?v=3" defer data-panel></script>
</body>
</html>
'''

def rv(i, extra=""):
    return f'class="reveal {extra}" style="--d:{i*90}ms"'.replace('  ', ' ')

# ---------- HOME ----------
def home(lang):
    if lang == "en":
        X = dict(
          h_eyebrow="A personal space for sharing what I'm learning",
          h1='Tips, ideas and reflections on keeping <em>people</em> at the centre of learning.',
          lede="I'm Diego, a teacher. I'm exploring how AI, research and human connection can help us rethink learning, and I share what I find because I enjoy it and I hope something here helps another teacher.",
          b1="Read the ideas", b2="Watch the videos", by="By Diego Guevara, science educator.",
          wl_eyebrow="Start here", wl_h="Welcome to MoreHuman Ed", wl_p="A six-minute hello: why I'm sharing this, and what you will find here.", wl_play="Play video", wl_title="Welcome to MoreHuman Ed", wl_note="Plays from YouTube only when you press play.",
          ex_eyebrow="What I'm exploring", ex_h="Six questions I keep coming back to",
          ex_cards=[("AI and human intelligence","Where technology helps, where it gets in the way, and what should always stay human."),
                    ("Human connection and learning","Why feeling noticed is so often where learning begins."),
                    ("Evidence and research","What the research says, how sure we can be, and what I'm still unsure about."),
                    ("Teacher wellbeing and workload","How routine work crowds out the attention students deserve, and what might help."),
                    ("Student independence","Critical thinking and ownership of learning in an age of instant answers."),
                    ("Systems and improvement","Small, careful changes that make a working day a little calmer.")],
          p_eyebrow="A question I keep asking", p_h="One approach for everyone fits no one.",
          p_1="Every classroom holds people who learn in different ways. Noticing each of them is hard when teachers are tired and the day is full of routine work.",
          p_2="I don't think the answer is asking teachers to do more. I'm exploring how to remove what does not need a human, so what does can have room.",
          p_hint="Drag to compare the two approaches", p_l="The blanket approach", p_lc="Everyone receives the same thing. Differences go unseen.",
          p_r="When teachers have room", p_rc="Each learner is noticed and supported in the way that fits them.",
          a_eyebrow="Ideas I return to", a_h="Three ideas",
          a_cards=[("Reduce routine work","Repetitive tasks crowd out attention. I'm curious about what can be simplified safely, and what should not be."),
                   ("Protect professional judgement","Technology can draft. People review, decide and speak with learners and families."),
                   ("Make room for each learner","Time and mental space are the real resource. I'm exploring how to give some back.")],
          t_eyebrow="Videos", t_h="Short videos of tips", t_p="Things I've found useful, shared in the hope they help another teacher. Nothing is for sale.", t_all="See all videos",
          n_eyebrow="Notes", n_h="Written notes are on the way", n_p="Reflections and reading notes, about one a month. There is no schedule and no pressure. I would rather write one thing worth reading.",
          s_eyebrow="About this site", s_h="A personal, independent project", s_p="Nothing here is for sale and no services are offered. Examples are invented, and I say so. I use AI to help draft, and I read and edit everything myself. The views are my own.", s_a="Read more",
          ab_eyebrow="About", ab_h="Diego Guevara",
          ab_p=["I'm a science educator and I teach students of different ages and subjects. I'm curious about how AI, research and human connection can help us rethink learning.",
                "This is a personal place where I think out loud: what I'm noticing, what I'm unsure about, and ideas I'm still testing.",
                f'I also build <a href="{DL}">Discovery Lab</a>, a free collection of interactive science simulations for my students.'],
          ab_a="More about me", ab_alt="Diego, a science educator",
          f_eyebrow="Join in", f_h="Something that works for you?", f_p="Share it in the comments on any video. I read them, and I learn from them.", f_b1="Watch on YouTube",
          ids=dict(explore="explore", approach="approach", about="about"), files=dict(tut="tutorials.html", priv="privacy.html", about="about.html"))
    else:
        X = dict(
          h_eyebrow="Un espacio personal para compartir lo que voy aprendiendo",
          h1='Ideas, consejos y reflexiones para mantener a las <em>personas</em> en el centro del aprendizaje.',
          lede="Soy Diego, docente. Exploro cómo la IA, la investigación y la conexión humana pueden ayudarnos a repensar el aprendizaje, y comparto lo que encuentro porque lo disfruto y espero que algo de esto ayude a otra persona que enseña.",
          b1="Leer las ideas", b2="Ver los vídeos", by="Por Diego Guevara, educador científico.",
          wl_eyebrow="Empieza aquí", wl_h="Te damos la bienvenida a MoreHuman Ed", wl_p="Un saludo de seis minutos: por qué comparto esto y qué vas a encontrar aquí. El vídeo está en inglés.", wl_play="Reproducir vídeo", wl_title="Welcome to MoreHuman Ed", wl_note="Se reproduce desde YouTube solo cuando pulsas el botón.",
          ex_eyebrow="Lo que exploro", ex_h="Seis preguntas a las que vuelvo una y otra vez",
          ex_cards=[("IA e inteligencia humana","Dónde ayuda la tecnología, dónde estorba y qué debería seguir siendo siempre humano."),
                    ("Conexión humana y aprendizaje","Por qué sentirse visto es tantas veces el principio del aprendizaje."),
                    ("Evidencia e investigación","Qué dice la investigación, con cuánta seguridad podemos decirlo y de qué sigo sin estar seguro."),
                    ("Bienestar y carga docente","Cómo el trabajo rutinario le quita al estudiante la atención que merece, y qué podría ayudar."),
                    ("Independencia del estudiante","Pensamiento crítico y responsabilidad sobre el propio aprendizaje en tiempos de respuestas instantáneas."),
                    ("Sistemas y mejora","Cambios pequeños y cuidadosos que hacen la jornada un poco más tranquila.")],
          p_eyebrow="Una pregunta que me repito", p_h="Un mismo enfoque para todos no sirve a nadie.",
          p_1="En cada aula hay personas que aprenden de maneras distintas. Atender a cada una es difícil cuando el profesorado está cansado y el día está lleno de tareas rutinarias.",
          p_2="No creo que la respuesta sea pedirle más al profesorado. Exploro cómo quitar lo que no necesita a una persona, para que lo que sí la necesita tenga espacio.",
          p_hint="Arrastra para comparar los dos enfoques", p_l="El enfoque para todos", p_lc="Todos reciben lo mismo. Las diferencias pasan desapercibidas.",
          p_r="Cuando el docente tiene espacio", p_rc="Cada persona que aprende es vista y acompañada de la manera que le conviene.",
          a_eyebrow="Ideas a las que vuelvo", a_h="Tres ideas",
          a_cards=[("Reducir el trabajo rutinario","Las tareas repetitivas le quitan atención al aula. Me interesa saber qué se puede simplificar con seguridad y qué no."),
                   ("Proteger el criterio profesional","La tecnología puede proponer. Las personas revisan, deciden y hablan con quienes aprenden y con sus familias."),
                   ("Dar espacio a cada persona que aprende","El tiempo y el espacio mental son el verdadero recurso. Exploro cómo devolver algo de ambos.")],
          t_eyebrow="Vídeos", t_h="Vídeos breves con consejos", t_p="Cosas que me han resultado útiles, compartidas con la esperanza de que ayuden a otra persona que enseña. Nada está a la venta. Los vídeos están en inglés.", t_all="",
          n_eyebrow="Notas", n_h="Las notas escritas están en camino", n_p="Reflexiones y notas de lectura, más o menos una al mes. No hay calendario ni presión. Prefiero escribir una cosa que merezca la pena leer.",
          s_eyebrow="Sobre este sitio", s_h="Un proyecto personal e independiente", s_p="Nada aquí está a la venta ni se ofrece ningún servicio. Los ejemplos son inventados, y lo digo. Uso la IA para ayudarme a redactar, y lo leo y edito todo yo mismo. Las opiniones son mías.", s_a="",
          ab_eyebrow="Sobre mí", ab_h="Diego Guevara",
          ab_p=["Soy educador científico y doy clase a estudiantes de distintas edades y materias. Me interesa cómo la IA, la investigación y la conexión humana pueden ayudarnos a repensar el aprendizaje.",
                "Este es un lugar personal donde pienso en voz alta: lo que voy notando, de lo que no estoy seguro y las ideas que sigo poniendo a prueba.",
                f'También creo <a href="{DL}">Discovery Lab</a>, una colección gratuita de simulaciones científicas interactivas para mis estudiantes.'],
          ab_a="", ab_alt="Diego, educador científico",
          f_eyebrow="Súmate", f_h="¿Algo que te funciona?", f_p="Cuéntalo en los comentarios de cualquier vídeo. Los leo y aprendo de ellos.", f_b1="Ver en YouTube",
          ids=dict(explore="explorar", approach="enfoque", about="sobre"), files=dict(tut=None, priv="../en/privacy.html", about=None))
    I = X["ids"]; F = X["files"]
    _bt = {"en": ["Every room holds someone who needs to be noticed.", "Technology drafts. People decide.", "Time to listen is the real resource."],
           "es": ["En cada sala hay alguien que necesita ser visto.", "La tecnología propone. Las personas deciden.", "El tiempo para escuchar es el verdadero recurso."]}[lang]
    _bi = [("room-1","A presenter speaking to a seated group beside a projector screen" if lang=="en" else "Una persona hablando a un grupo sentado junto a una pantalla","Quilia"),
           ("room-2","A person talking with a small group at a flipchart" if lang=="en" else "Una persona conversando con un grupo pequeño junto a un rotafolios","Centre for Ageing Better"),
           ("room-3","A teacher explaining an idea to a class" if lang=="en" else "Un docente explicando una idea a la clase","LexScope")]
    def _pb(k):
        n,alt,who=_bi[k]
        return f'<div class="photo-break reveal"><img src="../assets/img/photos/{n}.jpg" width="1000" height="750" alt="{alt}" loading="lazy" data-parallax><div class="photo-break__text"><p>{_bt[k]}</p><small>Photo: {who} / Unsplash</small></div></div>'
    BRK1, BRK2, BRK3 = _pb(0), _pb(1), _pb(2)
    _tw = ["Notice","Listen","Wonder","Every learner","Time to think","More human"] if lang == "en" else ["Observar","Escuchar","Preguntarse","Cada persona","Tiempo para pensar","Más humano"]
    TICK = "".join(f"<span>{w}</span>" for w in _tw)
    cards = "".join(f'<article {rv(i)}><div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{p}</p></div></article>' for i, (t, p) in enumerate(X["a_cards"]))
    ex = "".join(f'<article {rv(i)}><div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(X["ex_cards"]))
    tut = video_cards(lang)
    t_all = f'<p style="margin-top:2rem"><a href="{F["tut"]}">{X["t_all"]} &rarr;</a></p>' if F["tut"] and X["t_all"] else ""
    s_a = f'<p style="margin-top:1rem"><a href="{F["priv"]}">{X["s_a"]} &rarr;</a></p>' if X["s_a"] else (f'<p style="margin-top:1rem"><a href="{F["priv"]}">Sobre este sitio (en inglés) &rarr;</a></p>' if lang == "es" else "")
    ab_a = f'<p><a href="{F["about"]}">{X["ab_a"]} &rarr;</a></p>' if F["about"] else ""
    abp = "".join(f"<p>{p}</p>" for p in X["ab_p"])
    return f'''
<section class="hero"><span class="hero__blob b1" aria-hidden="true"></span><span class="hero__blob b2" aria-hidden="true"></span><div class="shell hero__grid">
<div><span class="eyebrow">{X["h_eyebrow"]}</span>
<h1>{X["h1"]}</h1>
<p class="hero__lede">{X["lede"]}</p>
<div class="btns"><a class="btn" href="#{I["explore"]}">{X["b1"]} <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn ghost" href="#tutorials">{X["b2"]}</a></div>
<p class="hero__by" style="margin-top:2rem;font-family:var(--font-data);font-size:var(--step--1);color:var(--ink-3)">{X["by"]}</p></div>
<div class="hero__visual" aria-hidden="false">{hero_visual(T[lang]["labels"])}</div>
</div></section>

<div class="ticker" aria-hidden="true"><div class="ticker__track">{TICK}{TICK}</div></div>

<section class="welcome" id="welcome"><div class="shell welcome__grid">
<div class="reveal from-left">{video_block(X["wl_title"], X["wl_play"])}</div>
<div class="reveal from-right" style="--d:120ms"><span class="eyebrow">{X["wl_eyebrow"]}</span><span class="rule"></span><h2>{X["wl_h"]}</h2><p>{X["wl_p"]}</p><p class="welcome__note">{X["wl_note"]}</p></div>
</div></section>

<section id="{I["explore"]}"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["ex_eyebrow"]}</span><span class="rule"></span><h2>{X["ex_h"]}</h2></div>
<div class="grid-3 bento">{ex}</div></div></section>

{BRK1}

<section class="tint" id="problem"><div class="shell problem">
<div class="problem__copy reveal from-left"><span class="eyebrow">{X["p_eyebrow"]}</span><span class="rule"></span><h2>{X["p_h"]}</h2><p>{X["p_1"]}</p><p>{X["p_2"]}</p></div>
{ba_visual(X["p_l"], X["p_r"], X["p_lc"], X["p_rc"], X["p_hint"])}
</div></div></section>

<section class="dark" id="{I["approach"]}"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["a_eyebrow"]}</span><span class="rule"></span><h2>{X["a_h"]}</h2></div>
<div class="grid-3 bento">{cards}</div></div></section>

{BRK2}

<section class="tint library" id="tutorials"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["t_eyebrow"]}</span><span class="rule"></span><h2>{X["t_h"]}</h2><p>{X["t_p"]}</p></div>
<div class="grid-3 bento">{tut}</div>{t_all}</div></section>

<section id="notes"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["n_eyebrow"]}</span><span class="rule"></span><h2>{X["n_h"]}</h2><p>{X["n_p"]}</p></div></div></section>

{BRK3}

<section class="tint" id="site"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["s_eyebrow"]}</span><span class="rule"></span><h2>{X["s_h"]}</h2><p>{X["s_p"]}</p>{s_a}</div></div></section>

<section id="{I["about"]}"><div class="shell about-grid">
<img class="portrait reveal from-left" src="../assets/img/diego-portrait.jpg" width="340" height="340" alt="{X["ab_alt"]}" loading="lazy">
<div class="prose reveal from-right" style="--d:100ms"><span class="eyebrow">{X["ab_eyebrow"]}</span><span class="rule"></span><h2>{X["ab_h"]}</h2>{abp}{ab_a}</div>
</div></section>

<section class="final"><div class="shell reveal">
<span class="eyebrow">{X["f_eyebrow"]}</span><span class="rule"></span>
<h2>{X["f_h"]}</h2><p>{X["f_p"]}</p>
<div class="btns"><a class="btn on-dark" href="{YT}">{X["f_b1"]} <span class="arrow" aria-hidden="true">&rarr;</span></a></div>
</div></section>
'''

def tutorials():
    return f'''
<section class="page-hero"><div class="shell"><span class="eyebrow">Videos</span><h1 class="reveal">Tips, shared in the hope they help.</h1>
<p class="hero__lede">Short videos with things I've found useful. Nothing is for sale and nothing is promised.</p></div></section>
<section class="welcome"><div class="shell welcome__grid">
<div class="reveal from-left">{video_block("Welcome to MoreHuman Ed", "Play video")}</div>
<div class="reveal from-right" style="--d:120ms"><span class="eyebrow">Start here</span><span class="rule"></span><h2>Welcome to MoreHuman Ed</h2><p>A six-minute hello: why I'm sharing this, and what you will find here.</p><p class="welcome__note">Plays from YouTube only when you press play.</p></div>
</div></section>
<section class="tint library"><div class="shell"><div class="section-head reveal"><span class="eyebrow">Library</span><span class="rule"></span><h2>All videos</h2><p>Something that works for you? Share it in the comments on any video.</p></div>
<div class="grid-3 bento">{video_cards("en")}</div></div></section>
'''

def about():
    return '''
<section class="page-hero"><div class="shell"><span class="eyebrow">About</span><h1 class="reveal">A science educator, thinking out loud.</h1>
<p class="hero__lede">I'm exploring how technology can strengthen the human side of education.</p></div></section>
<section><div class="shell about-grid">
<img class="portrait reveal from-left" src="../assets/img/diego-portrait.jpg" width="340" height="340" alt="Diego, a science educator" loading="lazy">
<div class="prose reveal from-right" style="--d:100ms">
<p>I'm a science educator. I teach students of different ages and subjects, and I'm fascinated by how the principles of learning connect across disciplines and generations.</p>
<p>My background is in science and ecology, and I have worked in teaching, leadership and educational technology.</p>
<p>What I keep noticing is that technology helps most when it protects time and attention for people. This site is where I explore that: what seems to work, what doesn't, and what the research says.</p>
<p>I work in English and Spanish.</p>
<p>I also build <a href="https://morehumaned.com/discovery-lab/">Discovery Lab</a>, a free collection of interactive science simulations for my students.</p>
<p>This is a personal, independent project. Nothing here is for sale and I am not offering services. You can read more on <a href="privacy.html">About this site</a>.</p>
</div></div></section>
'''

def privacy():
    return '''
<section class="page-hero"><div class="shell"><span class="eyebrow">About this site</span><h1 class="reveal">A personal, independent project.</h1>
<p class="hero__lede">Nothing here is for sale.</p></div></section>
<section><div class="shell prose">
<ul class="tick reveal"><li>No services are offered, and there is nothing to book or sign up for.</li><li>Examples are invented, and I say so. No learner, family or colleague information appears.</li><li>I use AI to help draft and organise, and I read, check and edit everything myself.</li><li>I try to cite sources, and to say what I'm unsure about.</li><li>The views here are my own.</li></ul>
<h2 class="reveal">Privacy</h2>
<p>This site uses no cookies, no tracking and no forms. The video player loads from YouTube, in its privacy-enhanced mode, only if you press play. Nothing is loaded from YouTube before that.</p>
</div></section>
'''

pages = [
 ("en","index.html","MoreHuman Ed | Tips, ideas and reflections on learning","A personal space to explore how AI, research and human connection can help us rethink learning. Tips, videos and reflections from a science educator.",home("en")),
 ("en","tutorials.html","Videos | MoreHuman Ed","Short videos with tips on teaching and technology, shared in the hope they help another teacher.",tutorials()),
 ("en","about.html","About | MoreHuman Ed","Diego Guevara, a science educator exploring how technology can strengthen the human side of learning.",about()),
 ("en","privacy.html","About this site | MoreHuman Ed","A personal, independent project. Nothing is for sale, and the site uses no cookies or tracking.",privacy()),
 ("es","index.html","MoreHuman Ed | Ideas, consejos y reflexiones sobre el aprendizaje","Un espacio personal para explorar cómo la IA, la investigación y la conexión humana pueden ayudarnos a repensar el aprendizaje.",home("es")),
]
for lang, fname, title, desc, body in pages:
    w(f"{lang}/{fname}", head_and_shell(lang, fname, title, desc, body))

# root page: the English home, served at / (Spanish browsers are sent to /es/)
import re as _re
_en = next(pg for pg in pages if pg[0] == "en" and pg[1] == "index.html")
_html = head_and_shell("en", "index.html", _en[2], _en[3], _en[4])
_html = _html.replace('../assets/', 'assets/').replace('../es/', 'es/')
_html = _re.sub(r'href="(tutorials|about|privacy)\.html"', r'href="en/\1.html"', _html)
_redirect = ('<script>try{if(/^es\\b/i.test(navigator.language||"")&&!/[?&]lang=en/.test(location.search))'
             '{location.replace("es/index.html")}}catch(e){}</script>\n</head>')
_html = _html.replace('</head>', _redirect, 1)
w("index.html", _html)
w("404.html", '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found | MoreHuman Ed</title><meta name="robots" content="noindex">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/img/favicon-64.png">
<link rel="stylesheet" href="/assets/tokens.css?v=3"><link rel="stylesheet" href="/assets/site.css?v=3"></head>
<body><main id="main"><section class="hero"><div class="shell"><span class="eyebrow">404</span>
<h1 style="margin-top:1rem">That page wandered off.</h1>
<p class="hero__lede">Try the <a href="/">home page</a> or la <a href="/es/index.html">página en español</a>.</p></div></section></main></body></html>
''')

urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{l}/{f}" for l, f, _, _, _ in pages if (l, f) != ("en", "index.html")]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"<url><loc>{u}</loc></url>" for u in urls] + ["</urlset>"]
w("sitemap.xml", "\n".join(sm) + "\n")
print("ok", len(pages), "pages")
