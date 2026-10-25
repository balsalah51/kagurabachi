#!/usr/bin/env python3
"""Second door for every room, in the same folder.

Each notes page restates that room's outline, a few lines already printed
there, and the neighboring files. It does not add plot. Do not run
tools/seo_apply.py afterward: its llms writer would drop hand-kept lines.
"""

from __future__ import annotations

import html as htmlmod
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path("/workspace")
LASTMOD = "2026-10-25"
ORIGIN = "https://kagurabachi.org"

# folder, crumb and sitemap heading, hub label, search section
FOLDERS = [
    ("guide", "Guide", "Guide notes", "guide"),
    ("characters", "Characters", "Character notes", "characters"),
    ("blades", "Enchanted Blades", "Blade notes", "blades"),
    ("manga", "Manga", "Manga notes", "manga"),
    ("arcs", "Story arcs", "Story notes", "arcs"),
    ("world", "World", "World notes", "world"),
    ("factions", "Factions", "Faction notes", "factions"),
    ("analysis", "Essays", "Essay notes", "analysis"),
    ("fun", "Fun", "Fun notes", "fun"),
    ("media", "Media", "Media notes", "media"),
    ("collectibles", "Collectibles", "Collectible notes", "collectibles"),
]
FOLDER_META = {f[0]: f for f in FOLDERS}
ROOT_SKIP = {"index.html", "search.html", "sitemap.html", "404.html", "privacy.html"}
SITEMAP_H2 = [f[1] for f in FOLDERS]
SITEMAP_H2_FRONT = ["Front door"] + SITEMAP_H2

VIZ = (
    '<p>Official chapters stay on '
    '<a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> and '
    '<a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. '
    "This door does not host them.</p>"
)


def no_dash(s: str) -> str:
    s = s.replace(" \u2014 ", ", ")
    s = s.replace("\u2014", ", ")
    s = s.replace(" \u2013 ", " - ")
    s = s.replace("\u2013", "-")
    s = s.replace("&mdash;", ", ")
    s = s.replace("&#8212;", ", ")
    s = s.replace("&ndash;", "-")
    return s


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def attr(s: str) -> str:
    return esc(s).replace('"', "&quot;")


def clip(s: str, n: int) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n:
        return s
    cut = s[: n - 1].rsplit(" ", 1)[0]
    return (cut or s[: n - 1]).rstrip(" ,;:") + "."


def notes_label(name: str) -> str:
    if name.lower().endswith(" notes"):
        return name + ", second door"
    return name + " notes"


def main_slice(html: str) -> str:
    m = re.search(r"<main\b[^>]*>(.*)</main>", html, re.S | re.I)
    body = m.group(1) if m else html
    body = re.sub(r'<p class="crumb">.*?</p>', "", body, flags=re.S | re.I)
    body = re.sub(r'<nav class="related".*?</nav>', "", body, flags=re.S | re.I)
    return body


def headings(body: str) -> list[tuple[int, str]]:
    found = []
    for m in re.finditer(r"<h([23])\b[^>]*>(.*?)</h\1>", body, re.S | re.I):
        label = strip_tags(m.group(2))
        if label:
            found.append((int(m.group(1)), label))
        if len(found) >= 30:
            break
    return found


def paragraphs(body: str) -> list[str]:
    paras = []
    for m in re.finditer(r"<p(\s[^>]*)?>(.*?)</p>", body, re.S | re.I):
        attrs = m.group(1) or ""
        if any(k in attrs for k in ("lede", "crumb", "notes-door", "kicker")):
            continue
        inner = m.group(2).strip()
        low = inner.lower()
        if any(tok in low for tok in ("<img", "<figure", "<script", "<style", "<nav", "</article", "<h2", "<h3")):
            continue
        plain = strip_tags(inner)
        if len(plain) < 40:
            continue
        if len(inner) > 1600:
            inner = esc(plain[:700].rstrip())
        paras.append(no_dash(inner))
        if len(paras) >= 2:
            break
    return paras


def list_lines(body: str) -> list[str]:
    lines = []
    for m in re.finditer(r"<li\b[^>]*>(.*?)</li>", body, re.S | re.I):
        inner = m.group(1)
        if "<img" in inner.lower():
            continue
        plain = strip_tags(inner)
        if len(plain) < 30:
            continue
        lines.append(esc(clip(plain, 220)))
        if len(lines) >= 6:
            break
    return lines


def internal_links(body: str, self_name: str, src: Path) -> list[tuple[str, str]]:
    seen = set()
    links = []
    for m in re.finditer(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body, re.S | re.I):
        href = m.group(1).strip().split("#", 1)[0]
        if not href or href.startswith(("http://", "https://", "mailto:", "javascript:")):
            continue
        if href.endswith("-notes.html") or href.endswith("/notes.html") or href == "notes.html":
            continue
        if not (href.endswith(".html") or href.endswith("/")):
            continue
        if href in seen or href == self_name:
            continue
        if not (src.parent / href).resolve().exists():
            continue
        label = strip_tags(m.group(2)) or href
        seen.add(href)
        links.append((href, label))
        if len(links) >= 8:
            break
    return links


def page_identity(html: str, fallback: str) -> tuple[str, str, str, str]:
    name = fallback
    jp = ""
    m = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, re.S | re.I)
    if m:
        inner = m.group(1)
        jm = re.search(r'<span class="jp">(.*?)</span>', inner, re.S | re.I)
        if jm:
            jp = strip_tags(jm.group(1))
            inner = inner[: jm.start()] + inner[jm.end() :]
        got = strip_tags(inner)
        if got:
            name = got
    lede = ""
    lm = re.search(r'<p class="lede">(.*?)</p>', html, re.S | re.I)
    if lm:
        lede = strip_tags(lm.group(1))
    desc = lede
    dm = re.search(r'<meta name="description" content="(.*?)"', html, re.S | re.I)
    if dm:
        desc = strip_tags(htmlmod.unescape(dm.group(1))) or lede
    return name, jp, lede, desc


@dataclass
class Room:
    src: Path
    folder: str
    stem: str
    name: str
    jp: str
    lede: str
    desc: str
    heads: list[tuple[int, str]]
    paras: list[str]
    lines: list[str]
    links: list[tuple[str, str]]
    notes_label: str
    prev: "Room | None" = None
    nxt: "Room | None" = None
    crumb: str = ""
    hub_label: str = ""
    section: str = "site"

    @property
    def url_path(self) -> str:
        name = f"{self.stem}-notes.html"
        return f"{self.folder}/{name}" if self.folder else name

    @property
    def source_loc(self) -> str:
        if self.folder:
            return f"{ORIGIN}/{self.folder}/{self.stem}.html"
        return f"{ORIGIN}/{self.stem}.html"

    @property
    def notes_loc(self) -> str:
        return f"{ORIGIN}/{self.url_path}"


def collect() -> list[Room]:
    rooms: list[Room] = []
    files: list[Path] = []
    for folder, *_ in FOLDERS:
        files.extend(sorted((ROOT / folder).glob("*.html")))
    files.extend(sorted(ROOT.glob("*.html")))
    for path in files:
        if path.name in ROOT_SKIP or path.name == "index.html":
            continue
        if path.name == "notes.html" or path.stem.endswith("-notes"):
            continue
        rel_parent = path.parent.relative_to(ROOT).as_posix()
        folder = "" if rel_parent == "." else rel_parent
        if folder and folder not in FOLDER_META:
            continue
        if path.parent == ROOT and path.name not in {"about.html", "faq.html"}:
            continue
        html = path.read_text(encoding="utf-8")
        body = main_slice(html)
        name, jp, lede, desc = page_identity(html, path.stem.replace("-", " "))
        meta = FOLDER_META.get(folder)
        room = Room(
            src=path,
            folder=folder,
            stem=path.stem,
            name=name,
            jp=jp,
            lede=lede,
            desc=desc,
            heads=headings(body),
            paras=paragraphs(body),
            lines=list_lines(body),
            links=internal_links(body, path.name, path),
            notes_label=notes_label(name),
            crumb=meta[1] if meta else "Archive",
            hub_label=meta[2] if meta else "Front door notes",
            section=meta[3] if meta else "site",
        )
        rooms.append(room)
    by_folder: dict[str, list[Room]] = {}
    for room in rooms:
        by_folder.setdefault(room.folder, []).append(room)
    for group in by_folder.values():
        group.sort(key=lambda r: r.src.name.casefold())
        for i, room in enumerate(group):
            room.prev = group[i - 1] if i else None
            room.nxt = group[i + 1] if i + 1 < len(group) else None
    return rooms


def outline_html(heads: list[tuple[int, str]]) -> str:
    if not heads:
        return "<p>This room has no subheadings. The title and the lede are the whole shape.</p>"
    items = []
    for level, label in heads:
        if level == 3:
            items.append(f"<li>{esc(label)}</li>")
        else:
            items.append(f"<li><strong>{esc(label)}</strong></li>")
    return '<ul class="map-list">\n' + "\n".join(items) + "\n</ul>"


def related(pairs: list[tuple[str, str]]) -> str:
    anchors = "".join(f'<a href="{attr(href)}">{esc(label)}</a>' for href, label in pairs)
    return f'<nav class="related" aria-label="Related pages">{anchors}</nav>'


def json_ld(url: str, title: str, desc: str, crumbs: list[tuple[str, str]]) -> str:
    graph = [
        {
            "@type": "WebSite",
            "@id": f"{ORIGIN}/#website",
            "name": "Kagurabachi Archive",
            "alternateName": [
                "Kagurabachi Encyclopedia",
                "Kagurabachi.org",
                "Kagurabachi wiki",
                "KB",
                "カグラバチ 資料庫",
            ],
            "url": f"{ORIGIN}/",
            "inLanguage": "en",
            "description": "Independent encyclopedia for Takeru Hokazono’s Kagurabachi: characters, Enchanted Blades, manga guide, and analysis.",
            "publisher": {"@id": f"{ORIGIN}/#org"},
            "potentialAction": {
                "@type": "SearchAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": f"{ORIGIN}/search.html?q={{search_term_string}}",
                },
                "query-input": "required name=search_term_string",
            },
        },
        {
            "@type": "Organization",
            "@id": f"{ORIGIN}/#org",
            "name": "Kagurabachi Archive",
            "url": f"{ORIGIN}/",
            "description": "Independent encyclopedia for Takeru Hokazono’s Kagurabachi.",
            "logo": {
                "@type": "ImageObject",
                "url": f"{ORIGIN}/assets/logo.png",
                "width": 512,
                "height": 512,
            },
        },
        {
            "@type": "WebPage",
            "@id": url,
            "url": url,
            "name": title,
            "description": desc,
            "isPartOf": {"@id": f"{ORIGIN}/#website"},
            "inLanguage": "en",
            "dateModified": LASTMOD,
            "publisher": {"@id": f"{ORIGIN}/#org"},
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": name,
                    "item": item,
                }
                for i, (name, item) in enumerate(crumbs)
            ],
        },
    ]
    raw = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return raw.replace("<", "\\u003c")


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <script>!function(){try{var m=document.cookie.match(/(?:^|; )kb-theme=(dark|light)/);if(m)document.documentElement.setAttribute("data-theme",m[1])}catch(e){}}()</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  <meta name="description" content="__DESC__">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+JP:wght@400;500;600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="__PRE__css/site.css">
  <link rel="canonical" href="__URL__">
  <link rel="alternate" hreflang="en" href="__URL__">
  <link rel="alternate" hreflang="x-default" href="__URL__">
  <link rel="search" type="application/opensearchdescription+xml" title="Kagurabachi Archive" href="https://kagurabachi.org/opensearch.xml">
  <link rel="manifest" href="https://kagurabachi.org/manifest.webmanifest">
  <link rel="apple-touch-icon" href="https://kagurabachi.org/assets/logo.png">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="theme-color" content="#9b1419">
  <meta name="google-adsense-account" content="ca-pub-1074015774205047">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1074015774205047" crossorigin="anonymous"></script>
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Kagurabachi Archive">
  <meta property="og:locale" content="en_US">
  <meta property="og:url" content="__URL__">
  <meta property="og:title" content="__TITLE__">
  <meta property="og:description" content="__DESC__">
  <meta property="og:image" content="https://kagurabachi.org/assets/logo.png">
  <meta property="og:image:alt" content="__TITLE__">
  <meta property="og:image:width" content="512">
  <meta property="og:image:height" content="512">
  <meta property="og:image:type" content="image/png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="__TITLE__">
  <meta name="twitter:description" content="__DESC__">
  <meta name="twitter:image" content="https://kagurabachi.org/assets/logo.png">
  <meta name="twitter:image:alt" content="__TITLE__">
  <script type="application/ld+json">
__LD__
  </script>
</head>
<body>
<noscript>
<nav class="crawl-nav" aria-label="Site"><a href="__PRE__index.html">Home</a> · <a href="__PRE__search.html">Search</a> · <a href="__PRE__faq.html">FAQ</a> · <a href="__PRE__characters/index.html">Characters</a> · <a href="__PRE__blades/index.html">Blades</a> · <a href="__PRE__manga/index.html">Manga</a> · <a href="__PRE__arcs/index.html">Story</a> · <a href="__PRE__sitemap.html">Site map</a> · <a href="__PRE__notes.html">Notes</a></nav>
</noscript>

  <div id="site-header"></div>
  <main id="main" class="wrap">
__CRUMB__
<header class="page-hero"><div>
  <p class="kicker">__KICKER__</p>
  <h1>__H1____JP__</h1>
  <p class="lede">__LEDE__</p>
</div></header>
<article class="article brief notes-room">
__BODY__
</article>

  </main>
  <div id="site-footer"></div>
  <script src="__PRE__js/site.js"></script>
</body>
</html>
"""


def render(path: Path, title: str, desc: str, kicker: str, h1: str, jp: str, lede: str, crumb: str, body: str, url: str, crumbs: list[tuple[str, str]]) -> None:
    pre = "../" if path.parent != ROOT else ""
    jp_html = f'<span class="jp">{esc(jp)}</span>' if jp else ""
    desc = clip(no_dash(desc), 220)
    title = no_dash(title)
    page = PAGE
    page = page.replace("__TITLE__", attr(title))
    page = page.replace("__DESC__", attr(desc))
    page = page.replace("__PRE__", pre)
    page = page.replace("__URL__", url)
    page = page.replace("__LD__", json_ld(url, title, desc, crumbs))
    page = page.replace("__CRUMB__", crumb)
    page = page.replace("__KICKER__", esc(kicker))
    page = page.replace("__H1__", esc(h1))
    page = page.replace("__JP__", jp_html)
    page = page.replace("__LEDE__", esc(clip(no_dash(lede), 320)))
    page = page.replace("__BODY__", body)
    page = no_dash(page)
    if "\u2014" in page or "\u2013" in page:
        raise SystemExit(f"dash left in {path}")
    if "<img" in page.lower():
        raise SystemExit(f"image left in {path}")
    path.write_text(page, encoding="utf-8")


def write_room(room: Room) -> str:
    parts = [
        f"<p>{esc(room.name)} has a second door on this shelf. It keeps the outline, the lines already printed on the room, and the neighboring files.</p>",
        "<h2>Outline</h2>",
        outline_html(room.heads),
    ]
    if room.paras:
        parts.append("<h2>Already on the page</h2>")
        parts.extend(f"<p>{p}</p>" for p in room.paras)
    elif room.lines:
        parts.append("<h2>Already on the page</h2>")
        parts.append('<ul class="map-list">')
        parts.extend(f"<li>{line}</li>" for line in room.lines)
        parts.append("</ul>")
    if room.links:
        parts.append("<h2>Doors from that room</h2>")
        parts.append('<ul class="map-list">')
        for href, label in room.links:
            parts.append(f'<li><a href="{attr(href)}">{esc(label)}</a></li>')
        parts.append("</ul>")
    beside = []
    if room.prev:
        beside.append(f'Before it: <a href="{room.prev.stem}-notes.html">{esc(room.prev.notes_label)}</a>')
    if room.nxt:
        beside.append(f'After it: <a href="{room.nxt.stem}-notes.html">{esc(room.nxt.notes_label)}</a>')
    if beside:
        parts.append("<h2>Beside it</h2>")
        parts.append("<p>" + ". ".join(beside) + ".</p>")
    parts.append(VIZ)
    pairs = [
        (f"{room.stem}.html", room.name),
        ("notes.html", room.hub_label),
        ("index.html", room.crumb if room.folder else "Home"),
    ]
    if room.prev:
        pairs.append((f"{room.prev.stem}-notes.html", room.prev.notes_label))
    if room.nxt:
        pairs.append((f"{room.nxt.stem}-notes.html", room.nxt.notes_label))
    parts.append(related(pairs))
    body = "\n".join(parts)
    pre = "../" if room.folder else ""
    home = f"{pre}index.html"
    if room.folder:
        crumb = (
            f'<p class="crumb"><a href="{home}">Archive</a> / '
            f'<a href="index.html">{esc(room.crumb)}</a> / '
            f'<a href="notes.html">Notes</a> / {esc(room.name)}</p>'
        )
        crumbs = [
            ("Home", f"{ORIGIN}/"),
            (room.crumb, f"{ORIGIN}/{room.folder}/"),
            ("Notes", f"{ORIGIN}/{room.folder}/notes.html"),
            (room.notes_label, room.notes_loc),
        ]
    else:
        crumb = (
            f'<p class="crumb"><a href="{home}">Archive</a> / '
            f'<a href="notes.html">Notes</a> / {esc(room.name)}</p>'
        )
        crumbs = [
            ("Home", f"{ORIGIN}/"),
            ("Notes", f"{ORIGIN}/notes.html"),
            (room.notes_label, room.notes_loc),
        ]
    lede = room.lede or room.desc or room.name
    desc = f"{room.notes_label}. {lede}"
    title = f"{room.notes_label} | Kagurabachi"
    url = room.notes_loc
    render(
        ROOT / room.url_path,
        title,
        desc,
        room.crumb,
        room.notes_label,
        room.jp,
        lede,
        crumb,
        body,
        url,
        crumbs,
    )
    return strip_tags(body)[:800]


def write_hub(folder: str, rooms: list[Room]) -> str:
    if folder:
        _, crumb_name, hub_label, _section = FOLDER_META[folder]
        path = ROOT / folder / "notes.html"
        url = f"{ORIGIN}/{folder}/notes.html"
        listed = sorted(rooms, key=lambda r: (r.notes_label.casefold(), r.stem))
        items = "\n".join(
            f'<li><a href="{r.stem}-notes.html">{esc(r.notes_label)}</a></li>' for r in listed
        )
        body = "\n".join(
            [
                f"<p>These doors restate the rooms already filed under <a href=\"index.html\">{esc(crumb_name)}</a>. They do not add a chapter, a name, or a fight.</p>",
                '<ul class="map-list">',
                items,
                "</ul>",
                VIZ,
                related(
                    [
                        ("index.html", crumb_name),
                        ("../notes.html", "All notes"),
                        ("../sitemap.html", "Site map"),
                    ]
                ),
            ]
        )
        crumb = (
            f'<p class="crumb"><a href="../index.html">Archive</a> / '
            f'<a href="index.html">{esc(crumb_name)}</a> / Notes</p>'
        )
        crumbs = [
            ("Home", f"{ORIGIN}/"),
            (crumb_name, f"{ORIGIN}/{folder}/"),
            (hub_label, url),
        ]
        kicker = crumb_name
        lede = "A second door for every room on this shelf. Same folder, same names, the outline beside the file."
        pre_home = "../"
    else:
        hub_label = "Front door notes"
        path = ROOT / "notes.html"
        url = f"{ORIGIN}/notes.html"
        shelf = "\n".join(
            f'<li><a href="{folder_name}/notes.html">{esc(label)}</a></li>'
            for folder_name, _crumb, label, _sec in FOLDERS
        )
        front = sorted(rooms, key=lambda r: (r.notes_label.casefold(), r.stem))
        front_items = "\n".join(
            f'<li><a href="{r.stem}-notes.html">{esc(r.notes_label)}</a></li>' for r in front
        )
        body = "\n".join(
            [
                "<p>Every shelf keeps a notes index in its own folder. The front-door rooms are listed under the shelves.</p>",
                "<h2>Shelves</h2>",
                '<ul class="map-list">',
                shelf,
                "</ul>",
                "<h2>Front door</h2>",
                '<ul class="map-list">',
                front_items,
                "</ul>",
                VIZ,
                related(
                    [
                        ("index.html", "Home"),
                        ("sitemap.html", "Site map"),
                        ("guide/notes.html", "Guide notes"),
                        ("characters/notes.html", "Character notes"),
                    ]
                ),
            ]
        )
        crumb = '<p class="crumb"><a href="index.html">Archive</a> / Notes</p>'
        crumbs = [
            ("Home", f"{ORIGIN}/"),
            (hub_label, url),
        ]
        kicker = "Archive"
        lede = "Notes doors for the front of the archive, and the index of every shelf."
    render(
        path,
        f"{hub_label} | Kagurabachi",
        lede,
        kicker,
        hub_label,
        "註",
        lede,
        crumb,
        body,
        url,
        crumbs,
    )
    return strip_tags(body)[:800]


def add_related(text: str, href: str, label: str) -> str:
    m = re.search(r'<nav class="related"[^>]*>', text)
    if not m:
        return text
    end = text.find("</nav>", m.end())
    if end < 0:
        return text
    if f'href="{href}"' in text[m.end() : end]:
        return text
    return text[: m.end()] + f'<a href="{href}">{esc(label)}</a>' + text[m.end() :]


def patch_sources(rooms: list[Room]) -> None:
    for room in rooms:
        text = room.src.read_text(encoding="utf-8")
        extra = ""
        if room.src.as_posix().endswith("guide/updates.html") and 'id="shelf-notes"' not in text:
            extra += (
                '<h2 id="shelf-notes">Shelf notes</h2>\n'
                "  <p>Each room now has a notes door in the same folder. The door restates the outline of that room and the lines already printed there. "
                'Shelf indexes start at <a href="../notes.html">front door notes</a>.</p>\n  '
            )
        if 'class="notes-door"' not in text:
            extra += (
                f'<p class="notes-door">Notes for this room live on <a href="{room.stem}-notes.html">{esc(room.notes_label)}</a>: '
                "the outline, the lines already on the page, and the rooms beside it.</p>\n"
            )
        if extra:
            m = re.search(r'<nav class="related"', text)
            if m:
                text = text[: m.start()] + extra + text[m.start() :]
            else:
                m = re.search(r"</article>", text) or re.search(r"</main>", text)
                if not m:
                    raise SystemExit(f"no insert point in {room.src}")
                text = text[: m.start()] + extra + text[m.start() :]
        text = add_related(text, f"{room.stem}-notes.html", "Notes")
        room.src.write_text(text, encoding="utf-8")


def patch_indexes() -> None:
    for folder, crumb_name, hub_label, _sec in FOLDERS:
        path = ROOT / folder / "index.html"
        text = path.read_text(encoding="utf-8")
        if 'class="notes-door"' not in text:
            sentence = (
                f'<p class="notes-door">Every room on this shelf has a notes door in the same folder. '
                f'<a href="notes.html">{esc(hub_label)}</a> is the list.</p>\n'
            )
            if "</header>" not in text:
                raise SystemExit(f"no header in {path}")
            text = text.replace("</header>", "</header>\n" + sentence, 1)
        text = add_related(text, "notes.html", "Notes")
        path.write_text(text, encoding="utf-8")
    for name in ("index.html", "search.html", "sitemap.html"):
        path = ROOT / name
        text = add_related(path.read_text(encoding="utf-8"), "notes.html", "Notes")
        path.write_text(text, encoding="utf-8")


def insert_map(path: Path, groups: dict[str, list[tuple[str, str]]]) -> None:
    text = path.read_text(encoding="utf-8")
    for heading in SITEMAP_H2_FRONT:
        pat = re.compile(
            r"(<h2>" + re.escape(heading) + r"</h2>\s*<ul class=\"map-list\">)(.*?)(</ul>)",
            re.S,
        )
        m = pat.search(text)
        if not m:
            raise SystemExit(f"{path} missing heading {heading}")
        body = m.group(2)
        fresh = []
        for label, href in groups.get(heading, []):
            if f'href="{href}"' in body:
                continue
            fresh.append((label, href))
        if not fresh:
            continue
        hub = [item for item in fresh if item[1].endswith("/notes.html") or item[1] == "notes.html"]
        rest = [item for item in fresh if item not in hub]
        rest.sort(key=lambda item: item[0].casefold())
        ordered = hub + rest
        extra = "".join(
            f'        <li><a href="{href}">{esc(label)}</a></li>\n' for label, href in ordered
        )
        if not body.endswith("\n"):
            body += "\n"
        text = text[: m.start()] + m.group(1) + body + extra + m.group(3) + text[m.end() :]
    path.write_text(text, encoding="utf-8")


def sitemap_block(loc: str) -> str:
    return (
        "  <url>\n"
        f"    <loc>{loc}</loc>\n"
        f"    <lastmod>{LASTMOD}</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n"
        "    <priority>0.6</priority>\n"
        "  </url>\n"
    )


def insert_sitemap(locs: list[tuple[str, str]]) -> list[str]:
    """locs is (after_this_source_loc, new_loc)."""
    path = ROOT / "sitemap.xml"
    xml = path.read_text(encoding="utf-8")
    missing = []
    for after, loc in locs:
        if f"<loc>{loc}</loc>" in xml:
            continue
        needle = f"<loc>{after}</loc>"
        i = xml.find(needle)
        if i < 0:
            missing.append(after)
            continue
        j = xml.find("</url>", i)
        j = xml.find("\n", j) + 1
        xml = xml[:j] + sitemap_block(loc) + xml[j:]
    if missing:
        fallback = []
        for after, loc in locs:
            if after in missing and f"<loc>{loc}</loc>" not in xml:
                fallback.append(sitemap_block(loc))
        if fallback:
            anchor = "<loc>https://kagurabachi.org/sitemap.html</loc>"
            i = xml.find(anchor)
            j = xml.rfind("<url>", 0, i)
            xml = xml[:j] + "".join(fallback) + xml[j:]
    path.write_text(xml, encoding="utf-8")
    return missing


def search_entry(url_path: str, title: str, jp: str, desc: str, section: str, aliases: list[str], text: str) -> dict:
    clean_aliases = []
    for alias in aliases:
        alias = re.sub(r"\s+", " ", alias).strip()
        if alias and alias not in clean_aliases:
            clean_aliases.append(alias)
    return {
        "url": "/" + url_path,
        "title": title,
        "jp": jp,
        "desc": clip(desc, 240),
        "section": section,
        "aliases": clean_aliases,
        "text": re.sub(r"\s+", " ", text).strip()[:800],
    }


def append_search(entries: list[dict]) -> int:
    path = ROOT / "assets" / "search-index.json"
    raw = path.read_text(encoding="utf-8")
    existing = json.loads(raw)
    fresh = {e["url"]: e for e in entries}
    ordered = []
    seen = set()
    added = 0
    for entry in existing:
        url = entry["url"]
        if url in fresh:
            ordered.append(fresh[url])
        else:
            ordered.append(entry)
        seen.add(url)
    for entry in entries:
        if entry["url"] not in seen:
            ordered.append(entry)
            seen.add(entry["url"])
            added += 1
    path.write_text(json.dumps(ordered, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))
    return added


def patch_llms() -> None:
    path = ROOT / "llms.txt"
    text = path.read_text(encoding="utf-8")
    if f"{ORIGIN}/notes.html" in text:
        return
    lines = ["- [Front door notes](https://kagurabachi.org/notes.html)"]
    for folder, _crumb, label, _sec in FOLDERS:
        lines.append(f"- [{label}]({ORIGIN}/{folder}/notes.html)")
    block = "\n".join(lines) + "\n"
    needle = "\n## Citation\n"
    if needle not in text:
        raise SystemExit("llms.txt missing Citation")
    path.write_text(text.replace(needle, "\n" + block + needle, 1), encoding="utf-8")


def main() -> None:
    rooms = collect()
    texts: dict[str, str] = {}
    for room in rooms:
        texts[room.url_path] = write_room(room)
    by_folder: dict[str, list[Room]] = {}
    for room in rooms:
        by_folder.setdefault(room.folder, []).append(room)
    hub_text: dict[str, str] = {}
    for folder, _c, label, section in FOLDERS:
        hub_text[f"{folder}/notes.html"] = write_hub(folder, by_folder.get(folder, []))
        hub_text[f"{folder}/notes.html"] = (label, section, hub_text[f"{folder}/notes.html"])  # type: ignore
    root_body = write_hub("", by_folder.get("", []))
    patch_sources(rooms)
    patch_indexes()

    groups: dict[str, list[tuple[str, str]]] = {h: [] for h in SITEMAP_H2_FRONT}
    groups["Front door"].append(("Front door notes", "notes.html"))
    for room in rooms:
        heading = room.crumb if room.folder else "Front door"
        groups[heading].append((room.notes_label, room.url_path))
    for folder, crumb_name, label, _sec in FOLDERS:
        groups[crumb_name].append((label, f"{folder}/notes.html"))
    insert_map(ROOT / "sitemap.html", groups)
    insert_map(ROOT / "search.html", groups)

    locs = []
    for room in rooms:
        locs.append((room.source_loc, room.notes_loc))
    for folder, *_ in FOLDERS:
        locs.append((f"{ORIGIN}/{folder}/", f"{ORIGIN}/{folder}/notes.html"))
    locs.append((f"{ORIGIN}/", f"{ORIGIN}/notes.html"))
    missing = insert_sitemap(locs)

    entries = []
    for room in rooms:
        entries.append(
            search_entry(
                room.url_path,
                room.notes_label,
                room.jp,
                f"{room.notes_label}. {room.lede or room.desc}",
                room.section,
                [room.notes_label, room.name, room.stem.replace("-", " "), room.jp],
                texts[room.url_path],
            )
        )
    entries.append(
        search_entry(
            "notes.html",
            "Front door notes",
            "註",
            "Notes doors for the front of the archive, and the index of every shelf.",
            "site",
            ["Front door notes", "notes", "註"],
            root_body,
        )
    )
    for folder, crumb_name, label, section in FOLDERS:
        _label, _section, body = hub_text[f"{folder}/notes.html"]
        entries.append(
            search_entry(
                f"{folder}/notes.html",
                label,
                "註",
                f"A second door for every room on the {crumb_name} shelf.",
                section,
                [label, f"{folder} notes", "註"],
                body,
            )
        )
    added = append_search(entries)
    patch_llms()

    html_count = len([p for p in ROOT.rglob("*.html") if ".git" not in p.parts])
    print(f"rooms {len(rooms)}")
    print(f"html {html_count}")
    print(f"search added {added}")
    print(f"sitemap missing anchors {len(missing)}")
    if missing:
        print("\n".join(missing[:20]))


if __name__ == "__main__":
    main()
