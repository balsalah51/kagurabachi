#!/usr/bin/env python3
"""Link chapter rooms in the index and patch hub copy."""
from pathlib import Path
import re

ROOT = Path("/workspace")

ROOMS = {
    1, 8, 9, 14, 18, 23, 27, 37, 44, 47, 50, 51, 57, 60, 62, 67, 70, 76,
    82, 83, 90, 91, 98, 100, 104, 108, 109, 115, 116, 117, 121, 122, 123,
    124, 125, 126, 127, 128, 129, 130,
}


def link_chapter_table():
    path = ROOT / "manga/chapters.html"
    html = path.read_text(encoding="utf-8")

    def repl(m):
        n = int(m.group(1))
        if n in ROOMS:
            return f"<tr><td><a href=\"chapter-{n}.html\">{n}</a></td>"
        return m.group(0)

    html2, n = re.subn(r"<tr><td>(\d+)</td>", repl, html)
    # prose: mention rooms
    old = (
        "Close readings on this site: <a href=\"chapter-1.html\">1, Mission</a>; "
        "<a href=\"chapter-18.html\">18, Roar</a>; <a href=\"chapter-115.html\">115, Swordsmith</a>; "
        "<a href=\"chapter-129.html\">129, Ironworks</a>; <a href=\"chapter-130.html\">130, I'm Fine!</a>. "
        "The <a href=\"part-2.html\">Part 2 page</a> writes the uncollected run in sentences."
    )
    new = (
        "Chapter rooms on this site cover the issues people actually search: "
        "<a href=\"chapter-1.html\">1</a>, <a href=\"chapter-14.html\">True Realm</a>, "
        "<a href=\"chapter-18.html\">Roar</a>, <a href=\"chapter-44.html\">The Curtain Falls</a>, "
        "<a href=\"chapter-76.html\">Banquet</a>, <a href=\"chapter-82.html\">Enten vs Tobimune</a>, "
        "<a href=\"chapter-117.html\">Irishima Talks</a>, <a href=\"chapter-125.html\">Smelting</a>, "
        "<a href=\"chapter-129.html\">Ironworks</a>, <a href=\"chapter-130.html\">I'm Fine!</a>, "
        "and the rest of the linked numbers in the table. Not every weekly title has a room. "
        "The table is still the authority for titles. The <a href=\"part-2.html\">Part 2 page</a> "
        "writes the uncollected run in sentences."
    )
    if old in html2:
        html2 = html2.replace(old, new)
    else:
        print("WARN: chapters prose needle missing")
    path.write_text(html2, encoding="utf-8")
    print("linked", n, "chapter rows")


def volume_diffs():
    path = ROOT / "manga/volumes.html"
    html = path.read_text(encoding="utf-8")
    needle = "<h2>Volume summaries</h2>"
    block = """<h2>Magazine versus the tankōbon</h2>
     <p>Fandom’s Volume 1 page logs the diffs we can stand behind without inventing later jackets. Chapter 1 is largely the same story, but some panels are expanded in the book and show more of the workshop than the magazine. Many of Char’s Volume 1 panels were redrawn; she looks less scruffy than the weekly pages. Azami’s badge is a later-book clarification. We will add a row here when we have seen a later volume’s own redraw list. We will not invent one from memory.</p>
     <p>The tankōbon is also a different object because of extras the magazine does not carry: <em>Genichi Sojo’s Bathhouse Quest</em> (two parts) and <em>Soya Sazanami’s Memories, Begone!</em> Color leads in Jump do not always reprint. Buy the book for those. <a href="omake.html">Volume extras</a>. Profile facts harvested from extras and can badges: <a href="../world/profiles.html">profiles</a>.</p>
     <h2>Volume summaries</h2>"""
    if needle not in html:
        raise SystemExit("volumes needle missing")
    if "Magazine versus the tankōbon" not in html:
        html = html.replace(needle, block, 1)
        path.write_text(html, encoding="utf-8")
        print("added volume diffs")
    else:
        print("volume diffs already present")


if __name__ == "__main__":
    link_chapter_table()
    volume_diffs()
