#!/usr/bin/env python3
"""Refresh stale 132-door language, volume counts, and voice credits."""
from pathlib import Path

ROOT = Path("/workspace")


def patch(rel, old, new, all=False):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("MISSING", rel, old[:80].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new) if all else text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def patch_if(rel, old, new, all=False):
    path = ROOT / rel
    if not path.exists():
        print("skip missing file", rel)
        return False
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("skip", rel, old[:60].replace("\n", " "))
        return False
    path.write_text(text.replace(old, new) if all else text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)
    return True


def bulk_replace(needle, repl, glob="**/*.html"):
    n = 0
    for path in ROOT.glob(glob):
        if "tools" in path.parts or path.suffix != ".html":
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            continue
        path.write_text(text.replace(needle, repl), encoding="utf-8")
        n += 1
    print(f"bulk {n} files:", needle[:50])


def main():
    # Quad-wave addenda on chapter rooms
    bulk_replace(
        "Chapter 132 remains a publication door without a printed title here.",
        "Chapter 132 is titled Misaka (巳坂). Chapter 133 is the next magazine door.",
    )
    bulk_replace(
        "Chapter 132 remains untitled here.",
        "Chapter 132 is titled Misaka (巳坂).",
    )
    bulk_replace(
        "132 stays a door.",
        "132 is Misaka.",
    )
    bulk_replace(
        "Chapter 132 is still a door, not a plot file.",
        "Chapter 132 is titled Misaka (巳坂). This desk still does not recap those panels.",
    )
    bulk_replace(
        "Chapter 132 stays a door.",
        "Chapter 132 is Misaka.",
    )
    bulk_replace(
        "we do not invent its title.",
        "the titled return is Misaka (巳坂).",
    )
    bulk_replace(
        "we do not invent its title",
        "the titled return is Misaka (巳坂)",
    )

    # Homepage
    patch("index.html", "Jump 2023 · 11 volumes · 4M+", "Jump 2023 · 12 volumes · 4M+")
    patch(
        "index.html",
        "Princess through Tipping Point, ch. 116–131",
        "Princess through Misaka, ch. 116–132",
    )
    patch("index.html", "Eleven spines, told in sentences", "Twelve Japanese spines, told in sentences")
    patch("index.html", "Still unnamed after chapter 131", "Still unnamed after chapter 132")
    patch(
        "index.html",
        "Issue 44, 28 September. Chapter 132’s door",
        "Issue 44 held Misaka. Chapter 133 is next",
    )
    patch(
        "index.html",
        '      <a class="home-row" href="guide/quad-doors.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol5.webp" alt="Quadruple wave"><b>Quadruple wave</b><small>Bonds, fight desks, volume reads, new essays</small></a>',
        '      <a class="home-row" href="guide/quad-doors.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol5.webp" alt="Quadruple wave"><b>Quadruple wave</b><small>Bonds, fight desks, volume reads, new essays</small></a>\n'
        '      <a class="home-row" href="manga/chapter-132.html"><img loading="lazy" decoding="async" src="assets/portraits/sojo.webp" alt="Chapter 132"><b>Chapter 132, Misaka</b><small>巳坂. Jump 2026 #44. 27 September</small></a>\n'
        '      <a class="home-row" href="guide/october-update.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol1.webp" alt="October update"><b>October update</b><small>The door became a title. 133 is a date</small></a>\n'
        '      <a class="home-row" href="fun/voices.html"><img loading="lazy" decoding="async" src="assets/portraits/chihiro-anime-art.jpg" alt="Voices"><b>Voices</b><small>Kimura, Seki, Konishi, Itō, Nemoto</small></a>',
    )

    # Chapter index table + copy
    patch(
        "manga/chapters.html",
        "Kagurabachi Chapter Index | Titles from Mission to Tipping Point",
        "Kagurabachi Chapter Index | Titles from Mission to Misaka",
        all=True,
    )
    patch(
        "manga/chapters.html",
        "“I'm Fine!” “Tipping Point.”",
        "“I'm Fine!” “Tipping Point.” “Misaka.”",
    )
    patch(
        "manga/chapters.html",
        "Chapter 132 is due Jump 2026 issue 44 (28 September 2026) after a health skip; the titled return is Misaka (巳坂).",
        "Chapter 132, “Misaka” (巳坂), printed 27 September 2026 (Jump 2026 #44) after the health skip. Chapter 133 is due Jump 2026 issue 45 (5 October 2026); we do not invent its title.",
    )
    # If the first 132 sentence was not already bulk-replaced, try the original
    patch_if(
        "manga/chapters.html",
        "Chapter 132 is due Jump 2026 issue 44 (28 September 2026) after a health skip; we do not invent its title.",
        "Chapter 132, “Misaka” (巳坂), printed 27 September 2026 (Jump 2026 #44) after the health skip. Chapter 133 is due Jump 2026 issue 45 (5 October 2026); we do not invent its title.",
    )
    patch(
        "manga/chapters.html",
        "118–120 stay unlinked. 132 is Misaka.",
        "118–120 stay unlinked. 132 is Misaka. 133 is a door.",
    )
    patch_if(
        "manga/chapters.html",
        "118–120 stay unlinked. 132 stays a door.",
        "118–120 stay unlinked. 132 is Misaka. 133 is a door.",
    )
    patch(
        "manga/chapters.html",
        '<tr><td><a href="chapter-131.html">131</a></td><td>Tipping Point</td><td>転換点</td></tr></tbody>',
        '<tr><td><a href="chapter-131.html">131</a></td><td>Tipping Point</td><td>転換点</td></tr>'
        '<tr><td><a href="chapter-132.html">132</a></td><td>Misaka</td><td>巳坂</td></tr></tbody>',
    )

    # Part 2
    patch("manga/part-2.html", "Ch. 116–131 · unfinished", "Ch. 116–132 · unfinished")
    patch(
        "manga/part-2.html",
        "Chapter 132 is a date: Jump 2026 issue 44, 28 September 2026, after the official health skip. File: <a href=\"../fun/september-2026-rest.html\">the September rest</a>.",
        "Chapter 132 is <a href=\"chapter-132.html\">Misaka</a> (巳坂), VIZ 27 September 2026, Jump 2026 #44, after the official health skip. This page does not recap those panels. Chapter 133 is <a href=\"chapter-133.html\">a date</a>: Jump 2026 issue 45. File: <a href=\"../fun/september-2026-rest.html\">the September rest</a>.",
    )
    patch(
        "manga/part-2.html",
        "Chapter 132 is titled Misaka (巳坂).",
        "The next magazine, chapter 133, remains a door.",
    )

    # Chapter 131 leftover door language
    patch(
        "manga/chapter-131.html",
        "Bureau choice. 132 is Misaka.",
        "Bureau choice. Next titled week: Misaka.",
    )
    patch(
        "manga/chapter-131.html",
        "then <a href=\"chapter-132.html\">the chapter 132 door</a>.",
        "then <a href=\"chapter-132.html\">chapter 132, Misaka</a>.",
    )

    # Jump 44 / September rest
    patch(
        "fun/jump-2026-44.html",
        "28 September 2026. A date, not a title.",
        "28 September 2026. The weekly word is Misaka.",
    )
    patch(
        "fun/jump-2026-44.html",
        "That is chapter 132’s magazine door. We do not invent the weekly title.",
        "That issue’s weekly word is now printed as Misaka (巳坂).",
    )
    patch(
        "fun/jump-2026-44.html",
        "Door: <a href=\"../manga/chapter-132.html\">chapter 132</a>.",
        "Titled room: <a href=\"../manga/chapter-132.html\">chapter 132, Misaka</a>.",
    )
    patch(
        "fun/jump-2026-44.html",
        'Ch. 132 door',
        "Misaka",
        all=True,
    )
    patch(
        "fun/index.html",
        "Issue 44. Chapter 132’s door.",
        "Issue 44. Misaka.",
    )
    patch(
        "fun/index.html",
        "Princess through Tipping Point. Ch. 116–131.",
        "Princess through Misaka. Ch. 116–132.",
    )
    patch(
        "fun/index.html",
        "Four million. Kiln. A door.",
        "Four million. Kiln. Misaka.",
    )
    patch(
        "fun/index.html",
        "Eleven spines</h3><p>Mission through Heroes, each with a room.",
        "Twelve spines</h3><p>Mission through Volume 12, each with a room.",
    )
    patch(
        "fun/index.html",
        '      <a class="card" href="english-volumes.html">',
        '      <a class="card" href="october-2026.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="October 2026"></div><div class="card-body"><h3>October 2026</h3><p>Misaka printed. 133 is a date.</p></div></a>\n'
        '      <a class="card" href="jump-2026-45.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Issue 45"></div><div class="card-body"><h3>Jump 2026 #45</h3><p>Chapter 133’s magazine date.</p></div></a>\n'
        '      <a class="card" href="english-volumes.html">',
    )

    # Official-only register
    patch(
        "guide/official-only.html",
        "Weekly titles through chapter 131, Tipping Point (転換点). Volume jackets 1–11 and the Volume 12 solicitation.",
        "Weekly titles through chapter 132, Misaka (巳坂). Volume jackets 1–12.",
    )
    patch(
        "guide/official-only.html",
        "Chapter 132’s title or plot until VIZ, MANGA Plus, or the Wikipedia chapter list this desk trusts prints it. The first Enchanted Blade’s name.",
        "Chapter 133’s title or plot until VIZ, MANGA Plus, or the Wikipedia chapter list this desk trusts prints it. The first Enchanted Blade’s name.",
    )
    patch(
        "guide/official-only.html",
        '132 door',
        "Misaka",
    )

    # Voices: Ito and Nemoto
    patch(
        "fun/voices.html",
        "Taihi Kimura is Chihiro. Tomokazu Seki is Kunishige. Katsuyuki Konishi is Shiba. The rest of the cast has not been announced.",
        "Taihi Kimura is Chihiro. Tomokazu Seki is Kunishige. Katsuyuki Konishi is Shiba. Miku Itō is Hinao. Miyari Nemoto is Char.",
    )
    patch(
        "fun/voices.html",
        "When Jump or the committee prints a name, it lands here.",
        "Hinao and Char joined the 2027 roll on 28 August 2026. When Jump or the committee prints a name, it lands here.",
    )
    patch(
        "fun/voices.html",
        "<p><strong>Katsuyuki Konishi</strong> as Togo Shiba. Teleport, mouth, extraction. The uncle in the booth. If the adaptation understands the book, Shiba is funny because he is tired.</p>",
        "<p><strong>Katsuyuki Konishi</strong> as Togo Shiba. Teleport, mouth, extraction. The uncle in the booth. If the adaptation understands the book, Shiba is funny because he is tired.</p>\n"
        "      <p><strong>Miku Itō</strong> as Hinao. Cafe Haru Haru. Introductions. The comic already had Akari Tadano in the booth; the series captioned the cafe again.</p>\n"
        "      <p><strong>Miyari Nemoto</strong> as Char Kyonagi. The last of a hunted clan. Announced with Itō on 28 August 2026.</p>",
    )
    patch(
        "fun/voices.html",
        "Hinao’s cafe has a voice in the comic. The series has not captioned her yet here. Keep the two lists separate until more names print.",
        "Hinao’s cafe has a voice in the comic and a second voice in the series. Keep the two lists separate. Char’s 2027 credit does not yet have a comic match on this desk.",
    )
    patch(
        "fun/voices.html",
        "Until then the cellar has three official voices and a comic quartet.",
        "Until more names print, the cellar has five official series voices and a comic quartet.",
    )
    patch(
        "fun/voices.html",
        '<nav class="related" aria-label="Related pages"><a href="../media/anime.html">Anime</a>',
        '<nav class="related" aria-label="Related pages"><a href="../media/ito-miku.html">Itō</a><a href="../media/nemoto.html">Nemoto</a><a href="../media/anime.html">Anime</a>',
    )

    # Anime page
    patch(
        "media/anime.html",
        "Taihi Kimura, Tomokazu Seki, Katsuyuki Konishi.",
        "Taihi Kimura, Tomokazu Seki, Katsuyuki Konishi, Miku Itō, Miyari Nemoto.",
    )
    patch_if(
        "media/anime.html",
        "Character pages for the announced three:",
        "Character pages for the announced five:",
    )

    # Volume 12 is out
    patch(
        "manga/volume-12.html",
        "Volume 12 is listed for 4 September 2026, ISBN 978-4-08-885177-8. English TBD. The volume guide expects chapters 106–115, Karma through Swordsmith, then the war book. The jacket has not been announced. Eleven spines are already on the shelf. This one is the solicited close.",
        "Volume 12 released 4 September 2026, ISBN 978-4-08-885177-8. English TBD. Wikipedia’s volume map prints Karma through Rock on this spine, then leaves 114 onward uncollected. Twelve Japanese books are on the shelf. The magazine continued through Misaka.",
    )
    patch(
        "fun/circulation.html",
        "Eleven Japanese volumes by May 2026. Volume 12 listed for 4 September.",
        "Eleven Japanese volumes by May 2026. Volume 12 released 4 September 2026.",
    )
    patch(
        "guide/series.html",
        "Eleven Japanese volumes as of 1 May 2026. Volume 12, 4 September 2026.",
        "Twelve Japanese volumes as of 4 September 2026.",
    )
    patch(
        "guide/reading-order.html",
        "Eleven Japanese Jump Comics are out. Volume 12 is solicited for 4 September 2026 and is expected to close Part 1 and open the war book.",
        "Twelve Japanese Jump Comics are out. Volume 12 released 4 September 2026 and is expected to close Part 1 and open the war book.",
    )
    patch(
        "guide/paper.html",
        "Eleven Japanese volumes by 1 May 2026. Volume 12 is expected to collect the close of Part 1 (chs. 106–115) and open the war book. VIZ’s English tankōbon started 5 November 2024. Eight English volumes are released or solicited through late 2026.",
        "Twelve Japanese volumes as of 4 September 2026. Volume 12 collects the close of Part 1 and opens the war book on paper. VIZ’s English tankōbon started 5 November 2024. Volume 8 is out; volume 9 is listed for 3 November 2026.",
    )
    patch(
        "guide/index.html",
        "Eleven jackets and one solicited close.",
        "Twelve Japanese jackets.",
    )
    patch(
        "guide/index.html",
        '      <a class="card" href="bond-map.html">',
        '      <a class="card" href="october-update.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="October update"></div><div class="card-body"><h3>October update</h3><p>Misaka filed. 133 stays a door.</p></div></a>\n'
        '      <a class="card" href="current-week.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Current week"></div><div class="card-body"><h3>Current week</h3><p>Latest titled room, next magazine date.</p></div></a>\n'
        '      <a class="card" href="bond-map.html">',
    )
    patch(
        "manga/index.html",
        "Princess through Tipping Point. Ch. 116–131.",
        "Princess through Misaka. Ch. 116–132.",
    )
    patch(
        "manga/index.html",
        "Eleven spines, told in sentences.",
        "Twelve spines, told in sentences.",
    )
    patch(
        "manga/index.html",
        '       <a class="card" href="part-2.html">',
        '       <a class="card" href="chapter-132.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Misaka"></div><div class="card-body"><h3>Chapter 132, Misaka</h3><p>巳坂. Jump 2026 #44.</p></div></a>\n'
        '       <a class="card" href="part-2.html">',
    )
    patch(
        "manga/synopses.html",
        "Eleven Japanese spines, one solicited twelfth.",
        "Twelve Japanese spines. The magazine continued.",
    )
    patch(
        "media/adaptations.html",
        "Eleven Japanese volumes as of 1 May 2026; volume 12 solicited for 4 September 2026.",
        "Twelve Japanese volumes as of 4 September 2026.",
    )
    patch(
        "fun/meme.html",
        "Eleven Japanese volumes by May 2026; volume 12 listed for 4 September.",
        "Twelve Japanese volumes as of 4 September 2026.",
    )
    patch(
        "fun/hokazono.html",
        "Eleven Japanese volumes by May 2026; volume 12 listed for 4 September.",
        "Twelve Japanese volumes as of 4 September 2026.",
    )
    patch(
        "faq.html",
        "Eleven Japanese tankōbon are out; volume 12 is solicited for 4 September 2026. The serial is through chapter 130 on this site’s last pass (3 September 2026), Part 2 already on the page.",
        "Twelve Japanese tankōbon are out as of 4 September 2026. The serial is through chapter 132, Misaka, on this site’s 3 October 2026 pass, Part 2 already on the page.",
        all=True,
    )
    patch(
        "collectibles/index.html",
        "Japanese Volume 11 is out. Volume 12, 4 September 2026, ISBN 978-4-08-885177-8. VIZ through Volume 8 on shelves or solicited; Volume 9 on 3 November 2026.",
        "Japanese Volume 12 is out (4 September 2026, ISBN 978-4-08-885177-8). VIZ Volume 8 is out; Volume 9 is listed for 3 November 2026.",
    )
    patch(
        "collectibles/index.html",
        "Voice credits already on this site: Taihi Kimura (Chihiro), Tomokazu Seki (Kunishige), Katsuyuki Konishi (Shiba).",
        "Voice credits already on this site: Taihi Kimura (Chihiro), Tomokazu Seki (Kunishige), Katsuyuki Konishi (Shiba), Miku Itō (Hinao), Miyari Nemoto (Char).",
    )
    patch(
        "collectibles/index.html",
        '     <p>ISBNs, chapter maps, and jacket faces live on the <a href="../manga/volumes.html">volume guide</a>.',
        '     <p>English objects this wave: <a href="english-volume-8.html">VIZ 8</a> and the <a href="english-volume-9.html">volume 9 date</a>. ISBNs, chapter maps, and jacket faces live on the <a href="../manga/volumes.html">volume guide</a>.',
    )

    # Timeline
    patch(
        "world/timeline.html",
        "Ch. 132 due Jump 2026 #44 after the 42/43 health skip. Title not printed on this desk.",
        "Ch. 132 Misaka (巳坂). Jump 2026 #44 after the 42/43 health skip.",
    )
    patch_if(
        "world/timeline.html",
        "Chapter 132 is due 28 September 2026 (Jump #44). The first blade is still unnamed.",
        "Chapter 132 is Misaka (巳坂), 27/28 September 2026 (Jump #44). Chapter 133 is due 4/5 October. The first blade is still unnamed.",
    )
    patch_if(
        "world/timeline.html",
        '<tr><td>Magazine, 28 Sep 2026</td><td>Ch. 132 Misaka (巳坂). Jump 2026 #44 after the 42/43 health skip.</td><td><a href="../manga/chapter-132.html">Ch. 132 door</a></td></tr>',
        '<tr><td>Magazine, 28 Sep 2026</td><td>Ch. 132 Misaka (巳坂). Jump 2026 #44 after the 42/43 health skip.</td><td><a href="../manga/chapter-132.html">Ch. 132 Misaka</a></td></tr>\n'
        '      <tr><td>Magazine, 5 Oct 2026</td><td>Ch. 133 due Jump 2026 #45. Title not printed on this desk.</td><td><a href="../manga/chapter-133.html">Ch. 133 door</a></td></tr>',
    )

    # Named person titles
    patch(
        "analysis/named-person-titles.html",
        "Chapter 114 is Kunishige Rokuhira. Chapter 123 is Chiaki.",
        "Chapter 114 is Kunishige Rokuhira. Chapter 123 is Chiaki. Chapter 132 is Misaka, the house.",
    )
    patch(
        "analysis/named-person-titles.html",
        "We do not invent a 132 name.",
        "Misaka is now on the list. We do not invent a 133 name.",
    )
    patch(
        "analysis/index.html",
        '      <a class="card" href="named-person-titles.html">',
        '      <a class="card" href="misaka-title.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Misaka as a title"></div><div class="card-body"><h3>Misaka as a title</h3><p>A house name as a weekly word.</p></div></a>\n'
        '      <a class="card" href="after-the-skip.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="After the skip"></div><div class="card-body"><h3>After the skip</h3><p>Illness, issue 44, then Misaka.</p></div></a>\n'
        '      <a class="card" href="named-person-titles.html">',
    )

    # Characters / world / media indexes
    patch_if(
        "characters/index.html",
        '      <a class="card" href="bonds.html">',
        '      <a class="card" href="shiba-and-ibuki.html"><div class="card-art p-sojo"><img src="../assets/portraits/sojo.webp" alt="Shiba and Ibuki"></div><div class="card-body"><span class="tag">Pairs</span><h3>Shiba and Ibuki</h3><p>Bureau friend. Kitakyushu swordsman.</p></div></a>\n'
        '      <a class="card" href="bonds.html">',
    )
    patch(
        "characters/ibuki.html",
        "The book has not printed that day.",
        "Chapter 132’s title is the house. This page still does not recap those panels. The book has not named the first blade.",
    )
    patch(
        "world/index.html",
        ' · <a href="first-blade.html">First blade</a>',
        ' · <a href="kitakyushu.html">Kitakyushu</a> · <a href="misaka-house.html">Misaka house</a> · <a href="first-blade.html">First blade</a>',
    )
    patch_if(
        "media/index.html",
        '    <h2>Four stills the videos pause</h2>',
        '    <p>Voice rooms this wave: <a href="kimura.html">Kimura</a>, <a href="seki.html">Seki</a>, <a href="konishi.html">Konishi</a>, <a href="ito-miku.html">Itō</a>, <a href="nemoto.html">Nemoto</a>. Licenses: <a href="crunchyroll.html">Crunchyroll</a>, <a href="muse-asia.html">Muse</a>.</p>\n'
        "    <h2>Four stills the videos pause</h2>",
    )
    patch(
        "factions/index.html",
        '<a href="bureau.html">Sorcery Bureau</a>',
        '<a href="bureau.html">Sorcery Bureau</a>, <a href="sorcery-bureau-and-misaka.html">bureau and Misaka</a>',
    )

    # Seitei war map description
    patch_if(
        "arcs/seitei-war-map.html",
        "Princess through Tipping Point. Talks 118–120 stay table-only. Kiln, reunion, bureau choice. No chapter 132 title.",
        "Princess through Misaka. Talks 118–120 stay table-only. Kiln, reunion, bureau choice, then a house name.",
    )
    patch_if(
        "arcs/seitei-war.html",
        "No chapter 132 title.",
        "Chapter 132 is Misaka.",
    )

    print("patch pass done")


if __name__ == "__main__":
    main()
