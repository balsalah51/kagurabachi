#!/usr/bin/env python3
"""Wire hubs for the biggest-update wave. Printed-fact links only."""
from pathlib import Path

ROOT = Path("/workspace")


def patch(rel, old, new, all=False):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("MISSING", rel, old[:90].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new) if all else text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def patch_if(rel, old, new):
    path = ROOT / rel
    if not path.exists():
        print("skip missing", rel)
        return False
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("skip", rel, old[:60].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def insert_before(rel, marker, block):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if block.strip()[:40] in text:
        print("already", rel)
        return False
    if marker not in text:
        print("NO MARKER", rel, marker[:60])
        return False
    path.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")
    print("inserted", rel)
    return True


def main():
    # Homepage stats + fresh steel
    patch("index.html", "<div><b>132</b><span>serialized chapters</span></div>", "<div><b>133</b><span>serialized chapters</span></div>")
    patch(
        "index.html",
        "Princess through Misaka, ch. 116–132",
        "Princess through a live 133, ch. 116–133",
    )
    patch(
        "index.html",
        "Still unnamed after chapter 132",
        "Still unnamed after the live 133",
    )
    patch(
        "index.html",
        "Issue 44 held Misaka. Chapter 133 is next",
        "133 is live untitled. 134 is Jump #46",
    )
    patch(
        "index.html",
        '      <a class="home-row" href="analysis/suzaku.html"><img loading="lazy" decoding="async" src="assets/portraits/samura.webp" alt="Suzaku"><b>Suzaku</b><small>The cut that keeps. Then the life spend</small></a>',
        '      <a class="home-row" href="analysis/suzaku.html"><img loading="lazy" decoding="async" src="assets/portraits/samura.webp" alt="Suzaku"><b>Suzaku</b><small>The cut that keeps. Then the life spend</small></a>\n'
        '      <a class="home-row" href="manga/chapter-133.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="Chapter 133"><b>Chapter 133, live untitled</b><small>VIZ 4 October. No subtitle on this desk</small></a>\n'
        '      <a class="home-row" href="collectibles/licenses.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol1.webp" alt="Licenses"><b>Official licenses</b><small>Sixteen publishers. Three Spanish rows</small></a>\n'
        '      <a class="home-row" href="fun/awards.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol2.webp" alt="Awards"><b>Awards desk</b><small>Next Manga, Eisner, Daruma, BookScan</small></a>\n'
        '      <a class="home-row" href="guide/ultra-doors.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol5.webp" alt="Biggest update"><b>Biggest update doors</b><small>Licenses, leftover pairs, tour stops</small></a>\n'
        '      <a class="home-row" href="collectibles/english-volume-10.html"><img loading="lazy" decoding="async" src="assets/covers/vol9.jpg" alt="English 10"><b>English volume 10</b><small>2 February 2027. ISBN 978-1-9747-6947-6</small></a>',
    )
    patch("index.html", '"dateModified": "2026-10-03"', '"dateModified": "2026-10-07"')

    # Chapters index
    patch(
        "manga/chapters.html",
        "Chapter 133 is due Jump 2026 issue 45 (5 October 2026); we do not invent its title.",
        "Chapter 133 is live on VIZ (4 October 2026) with no subtitle this desk will file. Chapter 134 is due Jump 2026 issue 46 (12 October 2026); we do not invent its title.",
    )
    patch(
        "manga/chapters.html",
        "118–120 stay unlinked. 132 is Misaka. 133 is a door.",
        "118–120 stay unlinked. 132 is Misaka. 133 is live untitled. 134 is a door.",
    )
    patch_if(
        "manga/chapters.html",
        '<tr><td><a href="chapter-132.html">132</a></td><td>Misaka</td><td>巳坂</td></tr></tbody>',
        '<tr><td><a href="chapter-132.html">132</a></td><td>Misaka</td><td>巳坂</td></tr>'
        '<tr><td><a href="chapter-133.html">133</a></td><td>Untitled here</td><td>第133話</td></tr></tbody>',
    )

    # Part 2
    patch_if("manga/part-2.html", "Ch. 116–132 · unfinished", "Ch. 116–133 · unfinished")
    patch_if(
        "manga/part-2.html",
        "The next magazine, chapter 133, remains a door.",
        "Chapter 133 is live on VIZ with no subtitle this desk will file. Chapter 134 is the next magazine door.",
    )

    # Bonds
    insert_before(
        "characters/bonds.html",
        "  <p>Official chapters live on",
        '  <h2>Leftover pairs this wave</h2>\n'
        "  <p><a href=\"natsuki-and-uruha.html\">Natsuki and Uruha</a>. <a href=\"chihiro-and-yura.html\">Chihiro and Yura</a>. <a href=\"azami-and-shiba.html\">Azami and Shiba</a>. <a href=\"sojo-and-kunishige.html\">Sojo and Kunishige</a>. <a href=\"hakuri-and-uruha.html\">Hakuri and Uruha</a>. <a href=\"yura-and-hokuto.html\">Yura and Hokuto</a>. <a href=\"samura-and-kunishige.html\">Samura and Kunishige</a>. <a href=\"uruha-and-kunishige.html\">Uruha and Kunishige</a>. <a href=\"chihiro-and-hinao.html\">Chihiro and Hinao</a>. <a href=\"hiyuki-and-azami.html\">Hiyuki and Azami</a>. <a href=\"ichiki-and-azami.html\">Ichiki and Azami</a>. <a href=\"char-and-hakuri.html\">Char and Hakuri</a>. <a href=\"kuguri-and-yura.html\">Kuguri and Yura</a>. <a href=\"kasen-and-shiba.html\">Kasen and Shiba</a>. <a href=\"natsuki-and-chihiro.html\">Natsuki and Chihiro</a>. <a href=\"bingo-and-yukisada.html\">Bingo and Yukisada</a>.</p>\n",
    )

    # Fun cards
    insert_before(
        "fun/index.html",
        '      <a class="card" href="bathhouse-quest-2.html">',
        '      <a class="card" href="awards.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol2.webp" alt="Awards"></div><div class="card-body"><h3>Awards</h3><p>Next Manga, Eisner, Daruma, charts.</p></div></a>\n'
        '      <a class="card" href="october-2026.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="October 2026"></div><div class="card-body"><h3>October 2026</h3><p>133 live untitled. 134 is a date.</p></div></a>\n'
        '      <a class="card" href="jump-2026-46.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Issue 46"></div><div class="card-body"><h3>Jump 2026 #46</h3><p>Chapter 134’s magazine date.</p></div></a>\n'
        '      <a class="card" href="four-million.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Four million"></div><div class="card-body"><h3>Four million</h3><p>April 2026. The meme was wrong.</p></div></a>\n',
    )
    patch(
        "fun/index.html",
        "<h3>October 2026</h3><p>Misaka printed. 133 is a date.</p>",
        "<h3>October 2026</h3><p>133 live untitled. English 10 solicited.</p>",
    )
    patch(
        "fun/index.html",
        "<h3>Jump 2026 #45</h3><p>Chapter 133’s magazine date.</p>",
        "<h3>Jump 2026 #45</h3><p>Chapter 133 ran. No subtitle here.</p>",
    )
    patch(
        "fun/index.html",
        "Princess through Misaka. Ch. 116–132.",
        "Princess through a live 133. Ch. 116–133.",
    )

    # Analysis cards
    insert_before(
        "analysis/index.html",
        '      <a class="card" href="../media/index.html">',
        '      <a class="card" href="live-untitled.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Live untitled"></div><div class="card-body"><h3>Live untitled</h3><p>A chapter can be out and still unnamed here.</p></div></a>\n'
        '      <a class="card" href="license-map.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="License map"></div><div class="card-body"><h3>License map</h3><p>Sixteen publishers. Three Spanish rows.</p></div></a>\n'
        '      <a class="card" href="volume-lag.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/vol9.jpg" alt="Volume lag"></div><div class="card-body"><h3>Volume lag</h3><p>Japanese 12 is out. English 10 is 2027.</p></div></a>\n',
    )

    # Guide cards
    insert_before(
        "guide/index.html",
        '      <a class="card" href="bond-map.html">',
        '      <a class="card" href="ultra-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Biggest update"></div><div class="card-body"><h3>Biggest update</h3><p>Licenses, leftover pairs, tour stops.</p></div></a>\n'
        '      <a class="card" href="legal-map.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/viz-social.jpg" alt="Legal map"></div><div class="card-body"><h3>Legal map</h3><p>Sunday chapter. Territorial book. 2027 stream.</p></div></a>\n'
        '      <a class="card" href="october-desk.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="October desk"></div><div class="card-body"><h3>October desk</h3><p>What this archive knew on 7 October.</p></div></a>\n',
    )
    patch(
        "guide/index.html",
        "<h3>October update</h3><p>Misaka filed. 133 stays a door.</p>",
        "<h3>October update</h3><p>133 is live. The subtitle is not.</p>",
    )
    patch(
        "guide/index.html",
        "<h3>Current week</h3><p>Latest titled room, next magazine date.</p>",
        "<h3>Current week</h3><p>Misaka titled. 133 live. 134 a date.</p>",
    )

    # Collectibles
    insert_before(
        "collectibles/index.html",
        "     <h2>Circulation &amp; awards</h2>",
        '     <h2>Territorial licenses</h2>\n'
        "     <p>The official comics page now prints sixteen territorial publishers beside Shueisha. Start at <a href=\"licenses.html\">the license map</a>. English volume 10 is listed for 2 February 2027: <a href=\"english-volume-10.html\">the solicitation</a>. Japanese volume 13 is still <a href=\"../manga/volume-13-door.html\">a door</a>.</p>\n\n",
    )
    patch(
        "collectibles/index.html",
        "As of 1 May 2026 there are 11 Japanese volumes. Volume 12 is listed for 4 September 2026",
        "As of 4 September 2026 there are 12 Japanese volumes. Volume 12 released 4 September 2026",
    )
    patch(
        "collectibles/index.html",
        "Eleven volumes out; twelfth solicited.",
        "Twelve volumes out. Volume 13 is a door until the official comics page lists it.",
    )
    patch(
        "collectibles/index.html",
        "Vols. 1–8 have announced dates through August 2026; Vol. 9 is listed 3 November 2026; later volumes TBA.",
        "Vols. 1–8 are out; Vol. 9 is listed 3 November 2026; Vol. 10 is listed 2 February 2027 (ISBN 978-1-9747-6947-6).",
    )
    patch(
        "collectibles/index.html",
        "French edition via Kana (noted on Volume 11 promo). Other territorial editions follow local Jump licenses.",
        "French edition via Kana. The full official table: Star Comics, Elex, Daewon, Ivrea, Planeta, Panini (Mexico and Brazil), SMM Plus, Xiling, Tong Li, Jade Dynasty, CREW, Carlsen, DEVIR. Map: <a href=\"licenses.html\">licenses</a>.",
    )

    # Media editions stale line
    patch_if(
        "media/editions.html",
        "Volumes 10 and 11 English were still TBD when this page was filed.",
        "English volume 10 is listed for 2 February 2027 (ISBN 978-1-9747-6947-6). Volume 11 English is still TBA.",
    )

    # Media index mention
    insert_before(
        "media/index.html",
        "    <h2>The arguments</h2>",
        '    <p>New staff and tour rooms: <a href="takeuchi.html">Takeuchi</a>, <a href="sasaki.html">Sasaki</a>, <a href="world-tour.html">world tour</a>, <a href="official-site.html">official sites</a>, <a href="jump-channel.html">volume 12 PVs</a>. The 2024 Toyo Keizai line sits on <a href="cygames-report.html">the Cygames report</a>.</p>\n',
    )

    # October update lede refresh
    patch_if(
        "guide/october-update.html",
        "What this archive refreshed in October 2026: Misaka as a titled room, a 133 door, voice rooms, English volume doors, and stale volume counts.",
        "October 2026 desk: Misaka titled, chapter 133 live untitled, chapter 134 a date, official license rooms, award desks, English volume 10.",
    )

    # Publication English 10
    patch_if(
        "manga/publication.html",
        "English Volume 8 is out; Volume 9 is listed for 3 November 2026.",
        "English Volume 8 is out; Volume 9 is listed for 3 November 2026; Volume 10 is listed for 2 February 2027 (ISBN 978-1-9747-6947-6).",
    )

    # Fun year 2026
    patch_if(
        "fun/year-2026.html",
        "Chapter 132 is Misaka",
        "Chapter 132 is Misaka; chapter 133 is live untitled as of 4 October",
    )

    print("ultra_wire done")


if __name__ == "__main__":
    main()
