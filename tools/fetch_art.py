#!/usr/bin/env python3
"""Download identification art from the Kagurabachi wiki CDN and official sites."""
import hashlib
import os
import ssl
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CTX = ssl.create_default_context()
UA = "KagurabachiArchive/1.0 (fan encyclopedia; identification art)"


def wiki_url(filename, width=640):
    name = filename.replace(" ", "_")
    digest = hashlib.md5(name.encode("utf-8")).hexdigest()
    encoded = urllib.parse.quote(name)
    return (
        f"https://static.wikia.nocookie.net/kagurabachi/images/"
        f"{digest[0]}/{digest[:2]}/{encoded}/revision/latest/scale-to-width-down/{width}"
    )


def fetch(url, dest, min_bytes=4000):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) >= min_bytes:
        print(f"skip {dest}")
        return True
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as res:
            data = res.read()
            ctype = res.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        print(f"FAIL {e.code} {url}")
        return False
    except Exception as e:
        print(f"ERR {e} {url}")
        return False
    if "text/html" in ctype or len(data) < min_bytes:
        print(f"BAD {len(data)} {ctype} {url}")
        return False
    with open(dest, "wb") as f:
        f.write(data)
    print(f"ok  {len(data):7d}  {dest}")
    return True


CHAPTERS = [
    1, 2, 8, 9, 14, 18, 19, 23, 30, 31, 40, 44, 47, 56, 60, 63, 64, 83, 113,
]

NAMED = [
    "Cloud_Gouger.png",
    "Kuregumo.png",
    "Hiruhiko.png",
    "Hiruhiko_Portrait.png",
    "Azami.png",
    "Azami_Portrait.png",
    "Hishaku.png",
    "Kamunabi.png",
    "Datenseki.png",
    "Flame_Bone.png",
    "The_Tou.png",
    "Magatsumi.png",
    "Enten.png",
    "Kumeyuri.png",
    "Tobimune.png",
    "Yura_reveals_that_he_orchestrated_Kunishige's_murder.png",
    "Yura_strikes_Chihiro.png",
    "Chihiro_asks_Yura_why_he_killed_Kunishige.png",
    "The_Tou's_defense_of_the_Rakuzaichi.png",
    "Wall_of_Trees.png",
    "Sojo_holding_Cloud_Gouger.png",
    "JP_Volume_12.png",
    "Volume_12.png",
    "Color_Page_Chapter_1.png",
]

OFFICIAL = [
    (
        "https://anime.kagurabachi.jp/images/ogp.png",
        os.path.join(ROOT, "assets/covers/official-ogp.png"),
        2000,
    ),
]


def main():
    panels = os.path.join(ROOT, "assets/panels")
    portraits = os.path.join(ROOT, "assets/portraits")
    covers = os.path.join(ROOT, "assets/covers")

    for n in CHAPTERS:
        for ext in (".png", ".webp", ".jpg"):
            name = f"Chapter_{n}{ext}"
            dest = os.path.join(panels, f"ch{n:03d}{ext}")
            if fetch(wiki_url(name), dest):
                break

    for name in NAMED:
        dest = os.path.join(panels, name.replace(" ", "_").replace("'", ""))
        fetch(wiki_url(name), dest)

    for url, dest, minimum in OFFICIAL:
        fetch(url, dest, min_bytes=minimum)


if __name__ == "__main__":
    main()
