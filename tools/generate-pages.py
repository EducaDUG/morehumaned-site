"""Generates every page of the MoreHuman Ed site. Run: python tools/generate-pages.py
Content and layout live here. Edit this file, then regenerate; do not hand-edit the generated HTML."""
import os, json, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://morehumaned.com"
CAL = "https://cal.com/morehumaned/talk"
DL = "https://educadug.github.io/discovery-lab/"
MAIL = "mailto:hello@morehumaned.com"

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
           '<circle cx="45" cy="22" r="5" fill="#B5551F"/><circle cx="32" cy="32" r="2.5" fill="currentColor"/></svg>')

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
  nav=[("index.html#approach","Approach"),("index.html#workshops","Workshops"),("tutorials.html","Tutorials"),("index.html#discovery-lab","Discovery Lab"),("about.html","About")],
  cta="Book a conversation", skip="Skip to content", langname="ES", menu="Menu",
  tag="Practical systems that give teachers and trainers room to notice every learner.",
  foot_note="Independent educator, Dunedin, New Zealand.",
  foot_cols=[("Explore",[("index.html#workshops","Workshops"),("pilot.html","Pilot"),("tutorials.html","Tutorials"),("about.html","About")]),
             ("Connect",[("https://educadug.github.io/discovery-lab/","Discovery Lab"),("privacy.html","Privacy and safety"),("mailto:hello@morehumaned.com","hello@morehumaned.com")])],
  labels=("Time","Attention","Judgement","Care"),
),
"es": dict(
  nav=[("index.html#enfoque","Enfoque"),("index.html#talleres","Talleres"),("piloto.html","Piloto"),("index.html#discovery-lab","Discovery Lab"),("index.html#sobre","Sobre mí")],
  cta="Reservar una conversación", skip="Ir al contenido", langname="EN", menu="Menú",
  tag="Sistemas prácticos para que docentes y formadores tengan tiempo y espacio para atender a cada persona que aprende.",
  foot_note="Educador independiente, Dunedin, Nueva Zelanda.",
  foot_cols=[("Explorar",[("index.html#talleres","Talleres"),("piloto.html","Piloto para escuelas"),("index.html#sobre","Sobre mí")]),
             ("Contacto",[("https://educadug.github.io/discovery-lab/","Discovery Lab"),("../en/privacy.html","Privacidad y seguridad (en inglés)"),("mailto:hello@morehumaned.com","hello@morehumaned.com")])],
  labels=("Tiempo","Atención","Criterio","Cuidado"),
),
}

SWITCH = {("en","index.html"):"../es/index.html",("en","pilot.html"):"../es/piloto.html",
          ("es","index.html"):"../en/index.html",("es","piloto.html"):"../en/pilot.html"}
ALT = {("en","index.html"):("es","index.html"),("en","pilot.html"):("es","piloto.html"),
       ("es","index.html"):("en","index.html"),("es","piloto.html"):("en","pilot.html")}


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
    if fname == "index.html":
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "Organization", "name": "MoreHuman Ed",
            "url": DOMAIN, "description": desc, "founder": {"@type": "Person", "name": "Diego Guevara"}},
            ensure_ascii=False) + '</script>'
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
<meta name="theme-color" content="#F5F0E6">
<link rel="icon" type="image/png" sizes="64x64" href="../assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<link rel="preload" href="../assets/fonts/fraunces-latin-1.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/public-sans-latin-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/tokens.css">
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="../assets/motion.css">
<script>document.documentElement.classList.add('js')</script>
{ld}
</head>
<body>
<a class="skip-link" href="#main">{c["skip"]}</a>
<header class="site-head"><div class="shell site-head__inner">
<a class="wordmark" href="index.html">{MARK}<span class="wordmark__text">MoreHuman&nbsp;Ed</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="{c["menu"]}"><span></span></button>
<nav class="nav" id="site-nav" aria-label="Main">{nav}{lang_switch(lang, sw)}<a class="btn" href="{CAL}">{c["cta"]}</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="shell site-foot__inner">
<div><a class="wordmark" href="index.html">{MARK}<span class="wordmark__text">MoreHuman&nbsp;Ed</span></a>
<p style="margin-top:1rem">{c["tag"]}</p><p style="margin-top:.5rem;font-size:.85rem">{c["foot_note"]}</p></div>
{foot}
</div></footer>
<div class="float-cta"><a class="btn" href="{CAL}">{c["cta"]} <span class="arrow" aria-hidden="true">&rarr;</span></a></div>
<script src="../assets/site.js" defer></script>
<script src="../assets/motion.js" defer></script>
</body>
</html>
'''

def rv(i, extra=""):
    return f'class="reveal {extra}" style="--d:{i*90}ms"'.replace('  ', ' ')

# ---------- HOME ----------
def home(lang):
    if lang == "en":
        X = dict(
          h_eyebrow="Practical systems for schools and training organisations",
          h1='Give teachers and trainers more time and mental space to <em>notice</em> every learner.',
          lede="MoreHuman Ed helps schools, training organisations and educators turn repetitive work and scattered technology experiments into practical, safe systems, so teachers and trainers can listen, notice and support each learner.",
          b1="Explore workshops", b2="Watch a tutorial", by="By Diego Guevara, science educator and learning-systems designer.",
          ph_eyebrow="In the room", ph_h="Real rooms, real people, room to notice each one.",
          who_eyebrow="Who it is for", who_h="For people who teach, train and lead learning",
          who_cards=[("Schools and school leaders","Principals, deputy heads and teaching teams who want to give teachers time back and keep the human side of teaching strong."),
                     ("Training organisations and institutions","Training providers, vocational and professional institutes and corporate learning teams who want practical systems that save trainer time without lowering quality."),
                     ("Trainers and adult educators","Independent trainers, facilitators and lecturers who want clearer workflows, better feedback habits and more time to notice the people in the room.")],
          p_eyebrow="The problem", p_h="One approach for everyone fits no one.",
          p_1="Every classroom and every training room holds people who learn in different ways. Teaching to each of them is hard when teachers and trainers are tired and the day is full of routine work.",
          p_2="The answer is not asking teachers and trainers to do more. It is removing what does not need a human, so what does can have room.",
          p_l="The blanket approach", p_lc="Everyone receives the same thing. Differences go unseen.",
          p_r="When teachers have room", p_rc="Each learner is noticed and supported in the way that fits them.",
          a_eyebrow="The approach", a_h="Three ideas behind the work",
          a_cards=[("Reduce routine work","Find the repetitive tasks that crowd out attention, and turn them into simple, repeatable workflows."),
                   ("Protect professional judgement","Technology drafts. Teachers and trainers review, decide, and speak with learners and families. Nothing leaves the organisation without a human."),
                   ("Make room for each learner","Time and mental space are the real resource. The aim is to give them back, so teachers and trainers can notice, listen and respond.")],
          w_eyebrow="Workshops", w_h="Ways to work together", w_p="Small, practical and reversible. Pricing is shared on inquiry, so it fits the size of your school or organisation.",
          w_for="For", w_prob="Problem it addresses", w_out="Practical outcome", w_dur="Duration",
          w_cards=[("Staff workshop","90 minutes","Teaching and training teams","Routine work is crowding out time to notice individual learners.","Two practical workflows chosen for your team and tried in real work.","Learn more",
                    "pilot.html"),
                   ("Team pilot","About three weeks","Schools and training organisations ready to test one change","Good ideas rarely survive a busy term without support.","A 14-day trial, a follow-up conversation and a short, anonymous impact summary.","See the pilot","pilot.html"),
                   ("Build a revision website","Hands-on session","Teachers, trainers and departments","Learners need clear, self-paced revision, and teachers and trainers need to build it quickly.","A working revision site you can reuse and adapt, built step by step.","Ask about this",
                    MAIL + "?subject=Revision%20website%20session")],
          pr_eyebrow="How it works", pr_h="From a busy week to one useful change",
          pr_steps=[("Understand your context","A short conversation about your people, your priorities and where time leaks."),
                    ("Choose a focused workflow","We pick one or two practical changes that fit, rather than trying to change everything."),
                    ("Support implementation","Teachers and trainers try them in real work, with help close at hand."),
                    ("Measure what changed","Confidence, use and estimated time saved are reviewed honestly, including what was hard.")],
          t_eyebrow="Tutorials", t_h="Short, practical videos", t_p="A growing library of tutorials on simple systems that return time and attention to teachers and trainers.",
          t_cards=[("chat","Coming soon","Why teachers are drained, and the one shift that helps","The main idea behind MoreHuman Ed."),
                   ("grid","Coming soon","Build a revision website in 30 minutes","A clear walk-through for any teacher."),
                   ("mail","Coming soon","One system, many families","Communicating clearly without adding to your workload.")],
          t_all="See all tutorials",
          d_eyebrow="See the approach in action", d_h="Discovery Lab: learning by doing.",
          d_p="Discovery Lab is an interactive science-learning project built around exploration, evidence and hands-on simulation. It shows the kind of human-centred learning experience MoreHuman Ed helps educators design.",
          d_chips=["Interactive simulations","Built around evidence","Free to use"], d_btn="Explore Discovery Lab",
          e_eyebrow="Evidence and trust", e_h="Honest evidence, careful with data",
          e_1="What we measure", e_1l=["Teacher and trainer confidence, before and after","How often the workflows are used","Estimated time saved","How it feels for attention to learners","What was hard to implement"],
          e_2="Privacy and safety", e_2l=["No learner-identifiable data needed","Demonstrations use invented examples","Teachers and trainers approve everything before use","Case studies only with written approval"], e_2a="Read the full approach",
          e_3="Pilot results and case studies", e_3p="As schools and organisations complete pilots, results appear here. Nothing is shown without their approval, and no numbers are promised in advance.",
          ab_eyebrow="About", ab_h="Diego Guevara",
          ab_p=["Diego Guevara is a science educator, teacher trainer and learning-systems designer who helps schools and training organisations use practical technology to reduce routine work without losing the human heart of teaching and learning.",
                "Through MoreHuman Ed, Diego explores how technology can strengthen human judgement, connection and care."],
          ab_a="More about Diego", ab_alt="Diego, an independent educator based in Dunedin, New Zealand",
          f_eyebrow="Next step", f_h="Let's find one practical way to give your teachers and trainers time back.",
          f_p="A relaxed 20-minute conversation. No pressure.", f_b1="Discuss a pilot", f_b2="Email me",
          ids=dict(approach="approach", workshops="workshops", about="about"), files=dict(pilot="pilot.html", tut="tutorials.html", priv="privacy.html", about="about.html"))
    else:
        X = dict(
          h_eyebrow="Sistemas prácticos para escuelas y organizaciones de formación",
          h1='Dale a docentes y formadores más tiempo y espacio mental para <em>atender</em> a cada persona que aprende.',
          lede="MoreHuman Ed ayuda a escuelas, organizaciones de formación y educadores a convertir el trabajo repetitivo y los experimentos tecnológicos dispersos en sistemas prácticos y seguros, para que docentes y formadores puedan escuchar, observar y acompañar a cada persona que aprende.",
          b1="Ver los talleres", b2="Ver el piloto", by="Por Diego Guevara, educador científico y diseñador de sistemas de aprendizaje.",
          ph_eyebrow="En la sala", ph_h="Salas reales, personas reales, espacio para ver a cada una.",
          who_eyebrow="Para quién es", who_h="Para quienes enseñan, forman y lideran el aprendizaje",
          who_cards=[("Escuelas y equipos directivos","Directores, jefes de estudios y equipos docentes que quieren devolver tiempo al profesorado y mantener fuerte la parte humana de enseñar."),
                     ("Organizaciones e instituciones de formación","Entidades de formación, institutos profesionales y equipos de aprendizaje corporativo que quieren sistemas prácticos que ahorren tiempo a los formadores sin bajar la calidad."),
                     ("Formadores y educadores de adultos","Formadores independientes, facilitadores y profesores que quieren flujos de trabajo más claros, mejores hábitos de retroalimentación y más tiempo para atender a las personas de la sala.")],
          p_eyebrow="El problema", p_h="Un mismo enfoque para todos no sirve a nadie.",
          p_1="En cada aula y en cada sala de formación hay personas que aprenden de maneras distintas. Atender a cada una es difícil cuando docentes y formadores están cansados y el día está lleno de tareas rutinarias.",
          p_2="La solución no es pedirles más. Es quitar lo que no necesita a una persona, para que lo que sí la necesita tenga espacio.",
          p_l="El enfoque para todos", p_lc="Todos reciben lo mismo. Las diferencias pasan desapercibidas.",
          p_r="Cuando el docente tiene espacio", p_rc="Cada persona que aprende es vista y acompañada de la manera que le conviene.",
          a_eyebrow="El enfoque", a_h="Tres ideas detrás del trabajo",
          a_cards=[("Reducir el trabajo rutinario","Identificar las tareas repetitivas que le quitan atención al aula y convertirlas en flujos de trabajo simples y repetibles."),
                   ("Proteger el criterio profesional","La tecnología propone. Docentes y formadores revisan, deciden y hablan con quienes aprenden y con sus familias. Nada sale de la organización sin una persona."),
                   ("Dar espacio a cada persona que aprende","El tiempo y el espacio mental son el verdadero recurso. El objetivo es devolverlos para poder observar, escuchar y responder.")],
          w_eyebrow="Talleres", w_h="Formas de trabajar juntos", w_p="Pequeños, prácticos y reversibles. El precio se comparte a consulta, para ajustarlo al tamaño de la escuela u organización.",
          w_for="Para quién", w_prob="Problema que atiende", w_out="Resultado práctico", w_dur="Duración",
          w_cards=[("Taller para el profesorado","90 minutos","Equipos docentes y de formación","El trabajo rutinario le quita tiempo a la atención individual.","Dos flujos de trabajo prácticos, elegidos para su equipo y probados en el trabajo real.","Más información","piloto.html"),
                   ("Piloto para equipos","Unas tres semanas","Escuelas y organizaciones de formación listas para probar un cambio","Las buenas ideas rara vez sobreviven a un trimestre ocupado sin apoyo.","Una prueba de 14 días, una conversación de seguimiento y un breve resumen anónimo del impacto.","Ver el piloto","piloto.html"),
                   ("Crear un sitio de repaso","Sesión práctica","Docentes, formadores y departamentos","Quienes aprenden necesitan repasar con claridad y a su ritmo, y docentes y formadores necesitan crearlo rápido.","Un sitio de repaso funcional, que se puede reutilizar y adaptar, creado paso a paso.","Preguntar",
                    MAIL + "?subject=Sesi%C3%B3n%20sitio%20de%20repaso")],
          pr_eyebrow="Cómo funciona", pr_h="De una semana ocupada a un cambio útil",
          pr_steps=[("Entender su contexto","Una conversación breve sobre su equipo, sus prioridades y dónde se escapa el tiempo."),
                    ("Elegir un flujo de trabajo","Escogemos uno o dos cambios prácticos que encajen, en lugar de intentar cambiarlo todo."),
                    ("Acompañar la implementación","Docentes y formadores los prueban en su trabajo real, con ayuda cerca."),
                    ("Medir qué cambió","Se revisan con honestidad la confianza, el uso y el tiempo estimado ahorrado, incluyendo lo que costó.")],
          t_eyebrow="Tutoriales", t_h="Vídeos breves y prácticos", t_p="Una biblioteca en crecimiento sobre sistemas sencillos que devuelven tiempo y atención a docentes y formadores.",
          t_cards=[("chat","Próximamente","Por qué los docentes están agotados y el cambio que ayuda","La idea central de MoreHuman Ed."),
                   ("grid","Próximamente","Crea un sitio de repaso en 30 minutos","Una guía clara para cualquier docente."),
                   ("mail","Próximamente","Un sistema, muchas familias","Comunicar con claridad sin sumar carga de trabajo.")],
          t_all="",
          d_eyebrow="El enfoque en acción", d_h="Discovery Lab: aprender haciendo.",
          d_p="Discovery Lab es un proyecto interactivo de aprendizaje de las ciencias basado en la exploración, la evidencia y la simulación práctica. Muestra el tipo de experiencia de aprendizaje centrada en las personas que MoreHuman Ed ayuda a diseñar.",
          d_chips=["Simulaciones interactivas","Basado en evidencia","De uso gratuito"], d_btn="Explorar Discovery Lab",
          e_eyebrow="Evidencia y confianza", e_h="Evidencia honesta, cuidado con los datos",
          e_1="Qué medimos", e_1l=["La confianza de docentes y formadores, antes y después","Con qué frecuencia se usan los flujos de trabajo","El tiempo estimado ahorrado","Cómo se siente la atención a quienes aprenden","Qué costó implementar"],
          e_2="Privacidad y seguridad", e_2l=["No se necesitan datos que identifiquen a quienes aprenden","Las demostraciones usan ejemplos inventados","Docentes y formadores aprueban todo antes de usarlo","Casos de estudio solo con aprobación escrita"], e_2a="",
          e_3="Resultados del piloto y casos de estudio", e_3p="Cuando escuelas y organizaciones completen sus pilotos, los resultados aparecerán aquí. Nada se muestra sin su aprobación, y no se prometen cifras por adelantado.",
          ab_eyebrow="Sobre mí", ab_h="Diego Guevara",
          ab_p=["Diego Guevara es educador científico, formador de docentes y diseñador de sistemas de aprendizaje. Ayuda a escuelas y organizaciones de formación a usar tecnología práctica para reducir el trabajo rutinario sin perder el corazón humano de la enseñanza y el aprendizaje.",
                "A través de MoreHuman Ed, Diego explora cómo la tecnología puede fortalecer el criterio, la conexión y el cuidado humanos."],
          ab_a="", ab_alt="Diego, educador independiente en Dunedin, Nueva Zelanda",
          f_eyebrow="Siguiente paso", f_h="Encontremos una forma práctica de devolver tiempo a sus docentes y formadores.",
          f_p="Una conversación relajada de 20 minutos. Sin compromiso.", f_b1="Hablar de un piloto", f_b2="Escríbeme",
          ids=dict(approach="enfoque", workshops="talleres", about="sobre"), files=dict(pilot="piloto.html", tut=None, priv="../en/privacy.html", about=None))
    I = X["ids"]; F = X["files"]
    _bt = {"en": ["Every room holds someone who needs to be noticed.", "Technology drafts. People decide.", "Time to listen is the real resource."],
           "es": ["En cada sala hay alguien que necesita ser visto.", "La tecnología propone. Las personas deciden.", "El tiempo para escuchar es el verdadero recurso."]}[lang]
    _bi = [("workshop-1","A presenter speaking to a seated group beside a projector screen" if lang=="en" else "Una persona presentando a un grupo sentado junto a una pantalla","Quilia"),
           ("workshop-3","A facilitator leading a small-group workshop at a flipchart" if lang=="en" else "Una facilitadora dirigiendo un taller en grupo","Centre for Ageing Better"),
           ("workshop-4","A teacher explaining an idea to a class" if lang=="en" else "Un docente explicando una idea a la clase","LexScope")]
    def _pb(k):
        n,alt,who=_bi[k]
        return f'<div class="photo-break reveal"><img src="../assets/img/photos/{n}.jpg" width="1000" height="750" alt="{alt}" loading="lazy" data-parallax><div class="photo-break__text"><p>{_bt[k]}</p><small>Photo: {who} / Unsplash</small></div></div>'
    BRK1, BRK2, BRK3 = _pb(0), _pb(1), _pb(2)
    _tw = ["Notice","Listen","Support","Every learner","Time to think","More human"] if lang == "en" else ["Observar","Escuchar","Acompañar","Cada persona","Tiempo para pensar","Más humano"]
    TICK = "".join(f"<span>{w}</span>" for w in _tw)
    ws = ""
    for i, (ttl, dur, who, prob, out, btn, href) in enumerate(X["w_cards"]):
        ws += f'''<article {rv(i)}><div class="card workshop"><span class="pill">{dur}</span><h3 style="margin-top:1rem">{ttl}</h3>
<dl><div><dt>{X["w_for"]}</dt><dd>{who}</dd></div><div><dt>{X["w_prob"]}</dt><dd>{prob}</dd></div><div><dt>{X["w_out"]}</dt><dd>{out}</dd></div></dl>
<a class="btn ghost" href="{href}">{btn} <span class="arrow" aria-hidden="true">&rarr;</span></a></div></article>'''
    cards = "".join(f'<article {rv(i)}><div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{p}</p></div></article>' for i, (t, p) in enumerate(X["a_cards"]))
    steps = "".join(f'<li {rv(i)}><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(X["pr_steps"]))
    tut = "".join(f'<article {rv(i)}><div class="card">{thumb_icon(k)}<span class="pill tag">{tag}</span><h3 style="font-size:var(--step-1)">{t}</h3><p>{d}</p></div></article>' for i, (k, tag, t, d) in enumerate(X["t_cards"]))
    t_all = f'<p style="margin-top:2rem"><a href="{F["tut"]}">{X["t_all"]} &rarr;</a></p>' if F["tut"] else ""
    chips = "".join(f'<span class="pill">{c}</span>' for c in X["d_chips"])
    e1 = "".join(f"<li>{x}</li>" for x in X["e_1l"]); e2 = "".join(f"<li>{x}</li>" for x in X["e_2l"])
    e2a = f'<p style="margin-top:1rem"><a href="{F["priv"]}">{X["e_2a"]} &rarr;</a></p>' if X["e_2a"] else ""
    ab_a = f'<p><a href="{F["about"]}">{X["ab_a"]} &rarr;</a></p>' if F["about"] else ""
    who = "".join(f'<article {rv(i)}><div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(X["who_cards"]))
    tiles = '<i></i>' * 15
    abp = "".join(f"<p>{p}</p>" for p in X["ab_p"])
    return f'''
<section class="hero"><span class="hero__blob b1" aria-hidden="true"></span><span class="hero__blob b2" aria-hidden="true"></span><div class="shell hero__grid">
<div><span class="eyebrow">{X["h_eyebrow"]}</span>
<h1>{X["h1"]}</h1>
<p class="hero__lede">{X["lede"]}</p>
<div class="btns"><a class="btn" href="#{I["workshops"]}">{X["b1"]} <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn ghost" href="{F["tut"] or F["pilot"]}">{X["b2"]}</a></div>
<p class="hero__by" style="margin-top:2rem;font-family:var(--font-data);font-size:var(--step--1);color:var(--ink-3)">{X["by"]}</p></div>
<div class="hero__visual" aria-hidden="false">{hero_visual(T[lang]["labels"])}</div>
</div></section>

<div class="ticker" aria-hidden="true"><div class="ticker__track">{TICK}{TICK}</div></div>

<section id="who"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["who_eyebrow"]}</span><span class="rule"></span><h2>{X["who_h"]}</h2></div>
<div class="grid-3">{who}</div></div></section>

{BRK1}

<section class="tint" id="problem"><div class="shell problem">
<div class="problem__copy reveal from-left"><span class="eyebrow">{X["p_eyebrow"]}</span><span class="rule"></span><h2>{X["p_h"]}</h2><p>{X["p_1"]}</p><p>{X["p_2"]}</p></div>
<div class="compare reveal from-right" style="--d:120ms">
<div class="panel"><span class="label">{X["p_l"]}</span><div class="tiles" aria-hidden="true">{tiles}</div><p>{X["p_lc"]}</p></div>
<div class="panel"><span class="label">{X["p_r"]}</span><div class="tiles varied" aria-hidden="true">{tiles}</div><p>{X["p_rc"]}</p></div>
</div></div></section>

<section class="dark" id="{I["approach"]}"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["a_eyebrow"]}</span><span class="rule"></span><h2>{X["a_h"]}</h2></div>
<div class="grid-3">{cards}</div></div></section>

<section class="tint" id="{I["workshops"]}"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["w_eyebrow"]}</span><span class="rule"></span><h2>{X["w_h"]}</h2><p>{X["w_p"]}</p></div>
<div class="grid-3">{ws}</div></div></section>

<section id="process"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["pr_eyebrow"]}</span><span class="rule"></span><h2>{X["pr_h"]}</h2></div>
<ol class="process">{steps}</ol></div></section>

{BRK2}

<section class="tint library" id="tutorials"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["t_eyebrow"]}</span><span class="rule"></span><h2>{X["t_h"]}</h2><p>{X["t_p"]}</p></div>
<div class="grid-3">{tut}</div>{t_all}</div></section>

<section id="discovery-lab"><div class="shell">
<div class="dl-feature reveal zoom">
<div><span class="eyebrow">{X["d_eyebrow"]}</span><h2>{X["d_h"]}</h2><p>{X["d_p"]}</p><div class="shared">{chips}</div>
<a class="btn" href="{DL}">{X["d_btn"]} <span class="arrow" aria-hidden="true">&rarr;</span></a></div>
{DL_MARK}</div></div></section>

<section class="tint evidence" id="trust"><div class="shell">
<div class="section-head reveal"><span class="eyebrow">{X["e_eyebrow"]}</span><span class="rule"></span><h2>{X["e_h"]}</h2></div>
<div class="grid-3">
<article {rv(0)}><div class="card"><h3>{X["e_1"]}</h3><ul>{e1}</ul></div></article>
<article {rv(1)}><div class="card"><h3>{X["e_2"]}</h3><ul>{e2}</ul>{e2a}</div></article>
<article {rv(2)}><div class="card ghost-card"><h3>{X["e_3"]}</h3><p>{X["e_3p"]}</p></div></article>
</div></div></section>

{BRK3}

<section id="{I["about"]}"><div class="shell about-grid">
<img class="portrait reveal from-left" src="../assets/img/diego-portrait.jpg" width="340" height="340" alt="{X["ab_alt"]}" loading="lazy">
<div class="prose reveal from-right" style="--d:100ms"><span class="eyebrow">{X["ab_eyebrow"]}</span><span class="rule"></span><h2>{X["ab_h"]}</h2>{abp}{ab_a}</div>
</div></section>

<section class="final"><div class="shell reveal">
<span class="eyebrow">{X["f_eyebrow"]}</span><span class="rule"></span>
<h2>{X["f_h"]}</h2><p>{X["f_p"]}</p>
<div class="btns"><a class="btn on-dark" href="{CAL}">{X["f_b1"]} <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn ghost" style="color:var(--surface);border-color:#ffffff66" href="{MAIL}">{X["f_b2"]}</a></div>
</div></section>
'''

# ---------- PILOT ----------
def pilot(lang):
    if lang == "en":
        return '''
<section class="page-hero"><div class="shell"><span class="eyebrow">For schools and training organisations</span><h1 class="reveal">Teacher Time &amp; Attention Pilot</h1>
<p class="hero__lede">A small, useful and reversible way to give your teachers and trainers back time and mental space.</p>
<div class="btns"><a class="btn" href="''' + CAL + '''">Book a conversation <span class="arrow" aria-hidden="true">&rarr;</span></a></div></div></section>
<section class="tint"><div class="shell"><div class="section-head reveal"><span class="eyebrow">What is included</span><span class="rule"></span><h2>Five parts, one clear arc</h2></div>
<ol class="steps">
<li class="reveal"><strong>90-minute staff workshop.</strong> Practical, hands-on, built around real teaching moments.</li>
<li class="reveal" style="--d:80ms"><strong>Two workflows chosen for your team.</strong> We pick them together, based on where your people lose the most time.</li>
<li class="reveal" style="--d:160ms"><strong>14-day implementation period.</strong> Teachers and trainers try the workflows in their own work, with support.</li>
<li class="reveal" style="--d:240ms"><strong>45-minute follow-up.</strong> We review what worked and what did not.</li>
<li class="reveal" style="--d:320ms"><strong>Short anonymous impact summary.</strong> A plain one-page report for your leadership team.</li>
</ol></div></section>
<section><div class="shell prose">
<h2 class="reveal">Safe by design</h2>
<ul class="tick reveal"><li>No learner-identifiable data is required at any point.</li><li>Demonstrations use invented examples.</li><li>Teachers review and approve everything before it is used.</li><li>You approve any case study before it is published.</li></ul>
<p><a href="privacy.html">Read the full privacy and safety approach</a></p>
<h2 class="reveal">How we measure</h2>
<p>Before and after, we ask teachers about their confidence, how much they used the workflows, their estimate of time saved and how it felt for attention to learners. We also record what was hard. I do not promise a number of hours saved before measuring it.</p>
<h2 class="reveal">Pricing</h2>
<p>The first two schools or organisations receive a founding rate in exchange for honest feedback and, if you are happy to, a short testimonial.</p>
<p class="notice">Pricing is shared on inquiry, so it can fit the size of your school or organisation. Email me with a few lines about your people and what they are carrying, and I will send a short proposal.</p>
<h2 class="reveal">Good questions</h2>
<h3>Do we need special tools?</h3><p>No. We use tools your staff can already access, and your organisation decides which ones are acceptable.</p>
<h3>What do you need from us?</h3><p>A room, 90 minutes with staff, and one person to be the contact during the 14 days.</p>
<h3>Can we stop at any point?</h3><p>Yes. The pilot is small and reversible by design.</p>
</div></section>
<section class="final"><div class="shell reveal"><span class="eyebrow">Next step</span><span class="rule"></span><h2>Talk it through.</h2><p>A relaxed 20-minute conversation. No pressure.</p>
<div class="btns"><a class="btn on-dark" href="''' + CAL + '''">Book a conversation <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn ghost" style="color:var(--surface);border-color:#ffffff66" href="''' + MAIL + '''">Email me</a></div></div></section>
'''
    return '''
<section class="page-hero"><div class="shell"><span class="eyebrow">Para escuelas y organizaciones de formación</span><h1 class="reveal">Piloto de Tiempo y Atención docente</h1>
<p class="hero__lede">Una forma pequeña, útil y reversible de devolver tiempo y espacio mental a docentes y formadores.</p>
<div class="btns"><a class="btn" href="''' + CAL + '''">Reservar una conversación <span class="arrow" aria-hidden="true">&rarr;</span></a></div></div></section>
<section class="tint"><div class="shell"><div class="section-head reveal"><span class="eyebrow">Qué incluye</span><span class="rule"></span><h2>Cinco partes, un recorrido claro</h2></div>
<ol class="steps">
<li class="reveal"><strong>Taller de 90 minutos para el profesorado.</strong> Práctico y basado en momentos reales de enseñanza.</li>
<li class="reveal" style="--d:80ms"><strong>Dos flujos de trabajo elegidos para su equipo.</strong> Se escogen juntos, según dónde se pierde más tiempo.</li>
<li class="reveal" style="--d:160ms"><strong>14 días de implementación.</strong> Los docentes prueban los flujos en su trabajo, con apoyo.</li>
<li class="reveal" style="--d:240ms"><strong>Seguimiento de 45 minutos.</strong> Se revisa qué funcionó y qué no.</li>
<li class="reveal" style="--d:320ms"><strong>Resumen breve y anónimo del impacto.</strong> Un informe de una página para el equipo directivo.</li>
</ol></div></section>
<section><div class="shell prose">
<h2 class="reveal">Seguro desde el diseño</h2>
<ul class="tick reveal"><li>En ningún momento se requieren datos que identifiquen a quienes aprenden.</li><li>Las demostraciones usan ejemplos inventados.</li><li>Docentes y formadores revisan y aprueban todo antes de usarlo.</li><li>Su organización aprueba cualquier caso de estudio antes de publicarlo.</li></ul>
<h2 class="reveal">Precio</h2>
<p class="notice">El precio se comparte a consulta, para ajustarlo al tamaño de la escuela u organización. Escríbeme unas líneas sobre tu equipo y te envío una propuesta breve.</p>
</div></section>
<section class="final"><div class="shell reveal"><span class="eyebrow">Siguiente paso</span><span class="rule"></span><h2>Hablemos.</h2><p>Una conversación relajada de 20 minutos. Sin compromiso.</p>
<div class="btns"><a class="btn on-dark" href="''' + CAL + '''">Reservar una conversación <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn ghost" style="color:var(--surface);border-color:#ffffff66" href="''' + MAIL + '''">Escríbeme</a></div></div></section>
'''

def tutorials():
    cards = "".join(f'<article class="reveal" style="--d:{i*90}ms"><div class="card">{thumb_icon(k)}<span class="pill tag">Coming soon</span><h3 style="font-size:var(--step-1)">{t}</h3><p>{d}</p></div></article>'
                    for i, (k, t, d) in enumerate([
                        ("chat", "Why teachers are drained, and the one shift that helps", "The main idea behind MoreHuman Ed."),
                        ("grid", "Build a revision website in 30 minutes", "A clear walk-through for any teacher."),
                        ("mail", "One system, many families", "Communicating clearly without adding to your workload.")]))
    return f'''
<section class="page-hero"><div class="shell"><span class="eyebrow">Tutorials</span><h1 class="reveal">Practical, short, human.</h1>
<p class="hero__lede">Videos on simple systems that return time and attention to teachers and trainers. Each one comes with a short written summary.</p></div></section>
<section class="tint library"><div class="shell"><div class="section-head reveal"><span class="eyebrow">First videos</span><span class="rule"></span><h2>Coming soon</h2></div>
<div class="grid-3">{cards}</div></div></section>
'''

def about():
    return f'''
<section class="page-hero"><div class="shell"><span class="eyebrow">About</span><h1 class="reveal">Science educator and learning-systems designer.</h1>
<p class="hero__lede">Technology that gives teachers and trainers the time and energy to notice every learner.</p></div></section>
<section><div class="shell about-grid">
<img class="portrait reveal from-left" src="../assets/img/diego-portrait.jpg" width="340" height="340" alt="Diego, an independent educator based in Dunedin, New Zealand" loading="lazy">
<div class="prose reveal from-right" style="--d:100ms">
<p>Diego Guevara is a science educator, teacher trainer and learning-systems designer who helps schools and training organisations use practical technology to reduce routine work without losing the human heart of teaching and learning.</p>
<p>Drawing on experience across science, ecology, education and international online learning, he creates clear workflows that give teachers and trainers more time and mental space to notice and support every learner.</p>
<p>Through MoreHuman Ed, Diego explores how technology can strengthen human judgement, connection and care.</p>
<p>Diego is based in Dunedin, New Zealand, and works in English and Spanish.</p>
<p>He works from the classroom outward: testing small changes, supporting teachers as they use them, and checking honestly whether they improve the working day. The aim is not to automate the relationship between teachers and students. It is to protect it.</p>
<p><strong>Side project:</strong> Diego also builds <a href="{DL}">Discovery Lab</a>, a separate collection of interactive simulations.</p>
<p>Get in touch: <a href="{MAIL}">hello@morehumaned.com</a></p>
</div></div></section>
'''

def privacy():
    return '''
<section class="page-hero"><div class="shell"><span class="eyebrow">Privacy and safety</span><h1 class="reveal">Careful by default.</h1>
<p class="hero__lede">Schools and training organisations hold sensitive information. The way I work is designed to need none of it.</p></div></section>
<section><div class="shell prose">
<ul class="tick reveal"><li>No student names or identifiable records in demonstrations. I use invented examples and say so.</li><li>No autonomous contact with students or families. Technology drafts, people decide and send.</li><li>Human approval before anything is published outside the school.</li><li>Clear handling of any school information: it is only used for the agreed purpose and is not shared.</li><li>A review of any third-party tool before it is suggested, and a privacy impact assessment if a system needs personal information.</li><li>Case studies and testimonials only with the school's written approval.</li></ul>
<p>This approach is designed with the New Zealand Privacy Act 2020 in mind.</p>
<p>Questions: <a href="mailto:hello@morehumaned.com">hello@morehumaned.com</a></p>
</div></section>
'''

pages = [
 ("en","index.html","MoreHuman Ed | Room to notice every learner","Practical systems that give teachers and trainers room to notice every learner. Workshops, tutorials and a safe pilot for schools and training organisations.",home("en")),
 ("en","pilot.html","Teacher Time & Attention Pilot | MoreHuman Ed","A small, safe, reversible pilot: a 90-minute workshop, two workflows, 14 days of implementation and a short impact summary.",pilot("en")),
 ("en","tutorials.html","Tutorials | MoreHuman Ed","Short practical videos on simple systems that return time and attention to teachers.",tutorials()),
 ("en","about.html","About | MoreHuman Ed","Diego Guevara, science educator, teacher trainer and learning-systems designer in Dunedin, New Zealand.",about()),
 ("en","privacy.html","Privacy and safety | MoreHuman Ed","How MoreHuman Ed keeps school, organisation and learner information safe.",privacy()),
 ("es","index.html","MoreHuman Ed | Espacio para atender a cada persona que aprende","Sistemas prácticos para que docentes y formadores tengan tiempo y espacio para atender a cada persona que aprende.",home("es")),
 ("es","piloto.html","Piloto de Tiempo y Atención docente | MoreHuman Ed","Un piloto pequeño, seguro y reversible: taller de 90 minutos, dos flujos de trabajo y un resumen breve de impacto.",pilot("es")),
]
for lang, fname, title, desc, body in pages:
    w(f"{lang}/{fname}", head_and_shell(lang, fname, title, desc, body))

# root page: the English home, served at / (Spanish browsers are sent to /es/)
import re as _re
_en = next(pg for pg in pages if pg[0] == "en" and pg[1] == "index.html")
_html = head_and_shell("en", "index.html", _en[2], _en[3], _en[4])
_html = _html.replace('../assets/', 'assets/').replace('../es/', 'es/')
_html = _re.sub(r'href="(pilot|tutorials|about|privacy)\.html"', r'href="en/\1.html"', _html)
_redirect = ('<script>try{if(/^es\\b/i.test(navigator.language||"")&&!/[?&]lang=en/.test(location.search))'
             '{location.replace("es/index.html")}}catch(e){}</script>\n</head>')
_html = _html.replace('</head>', _redirect, 1)
w("index.html", _html)
w("404.html", '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found | MoreHuman Ed</title><meta name="robots" content="noindex">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/img/favicon-64.png">
<link rel="stylesheet" href="/assets/tokens.css"><link rel="stylesheet" href="/assets/site.css"></head>
<body><main id="main"><section class="hero"><div class="shell"><span class="eyebrow">404</span>
<h1 style="margin-top:1rem">That page wandered off.</h1>
<p class="hero__lede">Try the <a href="/">home page</a> or la <a href="/es/index.html">página en español</a>.</p></div></section></main></body></html>
''')

urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{l}/{f}" for l, f, _, _, _ in pages if (l, f) != ("en", "index.html")]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"<url><loc>{u}</loc></url>" for u in urls] + ["</urlset>"]
w("sitemap.xml", "\n".join(sm) + "\n")
print("ok", len(pages), "pages")
