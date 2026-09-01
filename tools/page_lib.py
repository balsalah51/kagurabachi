#!/usr/bin/env python3
"""Shared HTML wrappers for Kagurabachi Archive pages. No em-dashes."""
from pathlib import Path

ROOT = Path("/workspace")

FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+JP:wght@400;500;600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap"


def page(rel, title, desc, body, depth=1):
    prefix = "../" * depth
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Kagurabachi Archive</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/site.css">
  <meta name="google-adsense-account" content="ca-pub-1074015774205047">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1074015774205047" crossorigin="anonymous"></script>
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
{body}
  </main>
  <div id="site-footer"></div>
  <script src="{prefix}js/site.js"></script>
</body>
</html>
"""
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel, "words", len(html.split()))
    print("note: run tools/seo_apply.py after generating pages so canonical, Open Graph, JSON-LD, and related links land.")


def crumb(*parts):
    bits = ['<a href="../index.html">Archive</a>']
    for item in parts[:-1]:
        if isinstance(item, tuple):
            bits.append(f'<a href="{item[1]}">{item[0]}</a>')
        else:
            bits.append(item)
    last = parts[-1]
    bits.append(last if isinstance(last, str) else last[0])
    return f'<p class="crumb">{" / ".join(bits)}</p>'


def hero(kicker, title, jp, lede):
    return f"""<header class="page-hero"><div>
      <p class="kicker">{kicker}</p>
      <h1>{title}<span class="jp">{jp}</span></h1>
      <p class="lede">{lede}</p>
    </div></header>
"""


def infobox(name, jp, portrait_class, img, caption, rows):
    dls = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    img_tag = f'<img src="{img}" alt="{caption}">' if img else ""
    return f"""<aside class="infobox">
      <div class="infobox-head"><h2>{name}</h2><span class="jp">{jp}</span></div>
      <div class="portrait {portrait_class}">{img_tag}
        <div class="portrait-caption">{caption}</div>
      </div>
      <dl>{dls}</dl>
    </aside>"""
