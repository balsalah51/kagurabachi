#!/usr/bin/env python3
"""Hub patches that mid_wire missed, plus wave-2 doors."""
from pathlib import Path

ROOT = Path("/workspace")


def patch(rel, old, new):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("MISSING", rel, old[:90].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def patch_if(rel, old, new):
    path = ROOT / rel
    if not path.exists():
        print("skip missing", rel)
        return False
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("skip", rel, old[:70].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def insert_before(rel, marker, block):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if block.strip()[:50] in text:
        print("already", rel)
        return False
    if marker not in text:
        print("NO MARKER", rel, marker[:60])
        return False
    path.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")
    print("inserted", rel)
    return True


def main():
    patch(
        "index.html",
        '"dateModified": "2026-10-03"',
        '"dateModified": "2026-10-17"',
    )
    patch(
        "index.html",
        '      <a class="home-row" href="manga/chapter-133.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="Chapter 133"><b>Chapter 133, live untitled</b><small>VIZ 4 October. No subtitle on this desk</small></a>',
        '      <a class="home-row" href="guide/brand-new-doors.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol5.webp" alt="Brand-new doors"><b>Brand-new doors</b><small>Version II, 剣豪, English 2–7, leftover pairs</small></a>',
    )
    patch_if(
        "index.html",
        "The door became a title. 133 is a date",
        "7 October desk. 133 is now Version II",
    )

    patch(
        "fun/year-2026.html",
        "Part 2’s kiln year. Daruma. Twelve spines. Misaka. A live untitled 133.",
        "Part 2’s kiln year. Daruma. Twelve spines. Two Misaka weeks. Then 剣豪.",
    )
    patch(
        "fun/year-2026.html",
        "Chapter 133 is <a href=\"../manga/chapter-133.html\">live untitled</a> as of 4 October 2026. Chapter 134 is <a href=\"../manga/chapter-134.html\">a date</a>.",
        "Chapter 133 is <a href=\"../manga/chapter-133.html\">Misaka Version II</a>. Chapter 134 is <a href=\"../manga/chapter-134.html\">Masters of the Sword</a>. Chapter 135 is <a href=\"../manga/chapter-135.html\">a date</a>.",
    )

    patch(
        "world/jump-simulpub.html",
        "Chapter 133 is live on that door as of 4 October 2026. Free windows move.",
        "Chapter 134, Masters of the Sword, is live on that door as of 11 October 2026. Free windows move. Chapter 135 is the next magazine date.",
    )

    patch(
        "guide/index.html",
        "<h3>October update</h3><p>133 is live. The subtitle is not.</p>",
        "<h3>October update</h3><p>The 7 October desk. 133 is now titled.</p>",
    )

    patch(
        "world/birthdays.html",
        '<td><a href="../characters/kunishige.html">Kunishige Rokuhira</a></td>',
        '<td><a href="kunishige-birthday.html">Kunishige Rokuhira</a></td>',
    )
    patch(
        "world/birthdays.html",
        '<td><a href="../characters/sojo.html">Genichi Sojo</a></td>',
        '<td><a href="sojo-birthday.html">Genichi Sojo</a></td>',
    )
    patch(
        "world/birthdays.html",
        '<td><a href="../characters/chihiro.html">Chihiro Rokuhira</a></td>',
        '<td><a href="chihiro-birthday.html">Chihiro Rokuhira</a></td>',
    )
    patch(
        "world/birthdays.html",
        '<td><a href="../characters/shiba.html">Togo Shiba</a></td>',
        '<td><a href="shiba-birthday.html">Togo Shiba</a></td>',
    )
    patch(
        "world/birthdays.html",
        '<td><a href="../characters/char.html">Char Kyonagi</a></td>',
        '<td><a href="char-birthday.html">Char Kyonagi</a></td>',
    )
    patch(
        "world/birthdays.html",
        "The full name list, dates or not, is the <a href=\"register.html\">name register</a>.",
        "Individual rooms: <a href=\"chihiro-birthday.html\">11 August</a>, <a href=\"kunishige-birthday.html\">5 June</a>, <a href=\"sojo-birthday.html\">6 June</a>, <a href=\"shiba-birthday.html\">15 October</a>, <a href=\"char-birthday.html\">21 December</a>. Essay: <a href=\"../analysis/five-dates-only.html\">five dates only</a>. The full name list, dates or not, is the <a href=\"register.html\">name register</a>.",
    )

    insert_before(
        "world/index.html",
        "      <nav class=\"related\" aria-label=\"Related pages\">",
        "       <p>Five printed birthdays now have their own rooms, starting at <a href=\"birthdays.html\">the calendar</a>. Leftover island nouns: <a href=\"sushi-subaru.html\">Sushi Subaru</a>, <a href=\"shokoku-datenseki.html\">Shokoku Datenseki</a>, <a href=\"candy-cigarettes.html\">candy cigarettes</a>, <a href=\"sumi-mandala.html\">Sumi’s mandala</a>. Shiba’s date inside the titled month: <a href=\"october-fifteen.html\">15 October</a>.</p>\n",
    )

    insert_before(
        "characters/bonds.html",
        "  <p>Official chapters live on",
        "  <h2>Still more leftover pairs</h2>\n"
        "  <p><a href=\"hakuri-and-hiyuki.html\">Hakuri and Hiyuki</a>. <a href=\"hakuri-and-shiba.html\">Hakuri and Shiba</a>. <a href=\"kuguri-and-hiruhiko.html\">Kuguri and Hiruhiko</a>. <a href=\"hiruhiko-and-iori.html\">Hiruhiko and Iori</a>. <a href=\"iori-and-kiri.html\">Iori and Kiri</a>. <a href=\"sojo-and-hagiwara.html\">Sojo and Hagiwara</a>. <a href=\"kazane-and-kugara.html\">Kazane and Kugara</a>. <a href=\"yura-and-bingo.html\">Yura and Bingo</a>. <a href=\"yura-and-toto.html\">Yura and Toto</a>. <a href=\"mashiro-and-ariu.html\">Mashiro and Ariu</a>. <a href=\"giyu-and-kunishige.html\">Giyu and Kunishige</a>. <a href=\"chihiro-and-kiri.html\">Chihiro and Kiri</a>. <a href=\"fushimi-and-samura.html\">Fushimi and Samura</a>. <a href=\"hiyuki-and-yura.html\">Hiyuki and Yura</a>. <a href=\"hokuto-and-samura.html\">Hokuto and Samura</a>. <a href=\"ichiki-and-yatsuru.html\">Ichiki and Yatsuru</a>. <a href=\"izaru-and-ichiki.html\">Izaru and Ichiki</a>.</p>\n",
    )

    insert_before(
        "fun/index.html",
        '      <a class="card" href="jump-2026-47.html">',
        '      <a class="card" href="november-2026.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="November 2026"></div><div class="card-body"><h3>November 2026</h3><p>English Enten listed. The magazine does not wait.</p></div></a>\n'
        '      <a class="card" href="five-printed-dates.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Five dates"></div><div class="card-body"><h3>Five printed dates</h3><p>The birthday desk as a fun door.</p></div></a>\n',
    )

    insert_before(
        "analysis/index.html",
        '      <a class="card" href="version-two.html">',
        '      <a class="card" href="wikipedia-titles.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Wikipedia titles"></div><div class="card-body"><h3>Wikipedia titles</h3><p>A chapter list. Not a recap wiki.</p></div></a>\n'
        '      <a class="card" href="kengo.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol10.webp" alt="剣豪"></div><div class="card-body"><h3>剣豪</h3><p>Masters of the Sword as a weekly word.</p></div></a>\n'
        '      <a class="card" href="english-shelf.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/vol9.jpg" alt="English shelf"></div><div class="card-body"><h3>English shelf</h3><p>VIZ trades 1 through 10.</p></div></a>\n'
        '      <a class="card" href="five-dates-only.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/chihiro.webp" alt="Five dates"></div><div class="card-body"><h3>Five dates only</h3><p>Merch calendars stay unmarked.</p></div></a>\n',
    )

    insert_before(
        "guide/index.html",
        '      <a class="card" href="mid-october-update.html">',
        '      <a class="card" href="brand-new-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Brand-new doors"></div><div class="card-body"><h3>Brand-new doors</h3><p>The 17 October wave, in one list.</p></div></a>\n'
        '      <a class="card" href="spoiler-134.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol10.webp" alt="134 without a recap"></div><div class="card-body"><h3>134 without a recap</h3><p>剣豪. Closed mouth on the panels.</p></div></a>\n',
    )

    patch(
        "collectibles/index.html",
        "English objects this wave: <a href=\"english-volume-8.html\">VIZ 8</a> and the <a href=\"english-volume-9.html\">volume 9 date</a>.",
        "English objects now have rooms through the shelf: <a href=\"english-volume-1.html\">1</a>, <a href=\"english-volume-2.html\">2</a>, <a href=\"english-volume-3.html\">3</a>, <a href=\"english-volume-4.html\">4</a>, <a href=\"english-volume-5.html\">5</a>, <a href=\"english-volume-6.html\">6</a>, <a href=\"english-volume-7.html\">7</a>, <a href=\"english-volume-8.html\">8</a>, <a href=\"english-volume-9.html\">9</a>, <a href=\"english-volume-10.html\">10</a>.",
    )

    patch_if(
        "manga/volumes.html",
        "English Volume 10 and 11 are still TBD.",
        "English volume 10 is solicited 2 February 2027 (ISBN 978-1-9747-6947-6); English 11 is still TBD.",
    )

    patch_if(
        "manga/part-2.html",
        "Ch. 116–134 · unfinished",
        "Ch. 116–134 · unfinished",
    )

    print("mid_wire2 done")


if __name__ == "__main__":
    main()
