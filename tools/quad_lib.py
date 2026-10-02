#!/usr/bin/env python3
"""Shared writer for the quadruple-content wave. Printed facts only. No em-dashes."""
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("mega_pages", Path("/workspace/tools/mega_pages.py"))
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)

related = mp.related
VIZ = mp.VIZ
ROOT = mp.ROOT
HEAD = mp.HEAD
FOOT = mp.FOOT
PAGES = mp.PAGES

FOLDERS = {
    "analysis": "Essays",
    "fun": "Fun",
    "guide": "Guide",
    "factions": "Factions",
    "manga": "Manga",
    "media": "Media",
    "characters": "Characters",
    "world": "World",
    "arcs": "Story",
    "blades": "Blades",
    "collectibles": "Collectibles",
}


def crumb_for(rel, h1):
    folder = rel.split("/", 1)[0]
    label = FOLDERS.get(folder, "World")
    return f'<a href="../index.html">Archive</a> / <a href="index.html">{label}</a> / {h1}'


def write_long(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    if (ROOT / rel).exists():
        print("skip exists", rel)
        return False
    html = (
        HEAD.replace("{title}", title).replace("{desc}", desc)
        + f'<p class="crumb">{crumb}</p>\n'
        + '<header class="page-hero"><div>\n'
        + f'  <p class="kicker">{kicker}</p>\n'
        + f'  <h1>{h1}<span class="jp">{jp}</span></h1>\n'
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + f'<article class="article">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    PAGES.append(rel)
    print("wrote", rel)
    return True


def page(rel, title, desc, kicker, h1, jp, lede, sections, links):
    parts = []
    for heading, paras in sections:
        if heading:
            parts.append(f"  <h2>{heading}</h2>")
        for p in paras:
            parts.append(f"  <p>{p}</p>")
    parts.append(f"  <p>Official chapters live on {VIZ}. This desk does not host pages.</p>")
    parts.append("  " + related(links))
    return write_long(rel, title, desc, crumb_for(rel, h1), kicker, h1, jp, lede, "\n".join(parts))
