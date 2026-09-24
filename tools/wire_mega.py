#!/usr/bin/env python3
"""Wire mega-update rooms into indexes. Idempotent enough to run once."""
from pathlib import Path
import re

ROOT = Path("/workspace")

LEFTOVER = [
    2, 3, 6, 10, 11, 12, 13, 15, 16, 17, 21, 22, 24, 25, 26, 28, 29, 30, 31,
    33, 34, 35, 36, 38, 39, 40, 42, 43, 46, 49, 52, 53, 54, 55, 58, 61, 63,
    64, 65, 68, 69, 71, 72, 73, 74, 77, 78, 79, 81, 84, 85, 86, 87, 88, 89,
    93, 94, 95, 96, 101, 102, 103, 107, 111, 112,
]
SKIP_SOLO = {118, 119, 120}


def patch(rel, old, new):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if new in text and old not in text:
        print("already", rel, old[:50].replace("\n", " "))
        return
    if old not in text:
        raise SystemExit(f"missing needle in {rel}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)


def link_chapters_table():
    path = ROOT / "manga/chapters.html"
    text = path.read_text(encoding="utf-8")
    for n in LEFTOVER:
        if n in SKIP_SOLO:
            continue
        old = f"<td>{n}</td>"
        new = f'<td><a href="chapter-{n}.html">{n}</a></td>'
        if old not in text:
            if new in text:
                print("already linked", n)
                continue
            raise SystemExit(f"chapter cell missing: {n}")
        text = text.replace(old, new, 1)
    # add 131 row if the table still ends at 130
    if "chapter-131.html" not in text:
        m = re.search(
            r"<tr><td>(?:<a href=\"chapter-130.html\">)?130(?:</a>)?</td><td>[^<]+</td><td>[^<]+</td></tr>",
            text,
        )
        if not m:
            raise SystemExit("could not find chapter 130 row")
        row131 = '<tr><td><a href="chapter-131.html">131</a></td><td>Tipping Point</td><td>転換点</td></tr>'
        text = text.replace(m.group(0), m.group(0) + row131, 1)
        print("added chapter 131 row")
    path.write_text(text, encoding="utf-8")
    print("linked leftover chapter table")


def main():
    link_chapters_table()

    patch(
        "manga/chapters.html",
        "Kagurabachi Chapter Index | Titles from Mission to I'm Fine!",
        "Kagurabachi Chapter Index | Titles from Mission to Tipping Point",
    )
    # title may appear several times; replace remaining I'm Fine! index titles carefully
    path = ROOT / "manga/chapters.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "Titles from Mission to I'm Fine!",
        "Titles from Mission to Tipping Point",
    )
    text = text.replace(
        "Titles from Mission to I&#x27;m Fine!",
        "Titles from Mission to Tipping Point",
    )
    path.write_text(text, encoding="utf-8")

    patch(
        "manga/chapters.html",
        "After chapter 126 the book took an announced month; 127–130 returned in August 2026 on the smelting and the reunion. Chapter 131 is due 6 September 2026.",
        "After chapter 126 the book took an announced month; 127–130 returned in August 2026 on the smelting and the reunion. Chapter 131, “Tipping Point” (転換点), printed 6 September 2026 (Jump 2026 #41). Chapter 132 is due Jump 2026 issue 44 (28 September 2026) after a health skip; we do not invent its title. 118–120 stay table-only; use <a href=\"../world/irishima-talks.html\">the talks room</a>.",
    )

    # Homepage stats and fresh steel
    patch("index.html", "<div><b>130</b><span>serialized chapters</span></div>",
          "<div><b>131</b><span>serialized chapters</span></div>")
    patch(
        "index.html",
        '<a class="home-row" href="manga/part-2.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="Part 2"><b>Part 2</b><small>Princess through I\'m Fine!, ch. 116–130</small></a>',
        '<a class="home-row" href="manga/part-2.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="Part 2"><b>Part 2</b><small>Princess through Tipping Point, ch. 116–131</small></a>',
    )
    patch(
        "index.html",
        '<a class="home-row" href="world/first-blade.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="The first blade"><b>The first blade</b><small>Still unnamed after chapter 130</small></a>',
        '''<a class="home-row" href="world/first-blade.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="The first blade"><b>The first blade</b><small>Still unnamed after chapter 131</small></a>
      <a class="home-row" href="manga/chapter-131.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="Chapter 131"><b>Chapter 131, Tipping Point</b><small>Jump 2026 #41. 6 September</small></a>
      <a class="home-row" href="fun/september-2026-rest.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol1.webp" alt="September rest"><b>The September rest</b><small>Issue 44, 28 September. Chapter 132’s door</small></a>
      <a class="home-row" href="manga/volume-1.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol1.webp" alt="Volume 1"><b>Volume rooms</b><small>Mission through Heroes, each with a jacket</small></a>
      <a class="home-row" href="world/owl.html"><img loading="lazy" decoding="async" src="assets/portraits/samura.webp" alt="Owl"><b>Owl, Play, Flame Bone</b><small>Printed kit, now with rooms</small></a>
      <a class="home-row" href="guide/mega-doors.html"><img loading="lazy" decoding="async" src="assets/panels/ch001.png" alt="Mega doors"><b>Mega update doors</b><small>Leftover titles, volumes, leftover kit</small></a>''',
    )

    # Part 2
    patch(
        "manga/part-2.html",
        "Chapter 131 is due 6 September 2026. This entry moves when it prints.",
        'Chapter 131 is <a href="chapter-131.html">Tipping Point</a> (転換点), VIZ 6 September 2026, Jump 2026 #41. This page does not invent those panels. Chapter 132 is a date: Jump 2026 issue 44, 28 September 2026, after the official health skip. File: <a href="../fun/september-2026-rest.html">the September rest</a>.',
    )
    patch(
        "manga/part-2.html",
        '<p class="kicker">Ch. 116–130 · unfinished</p>',
        '<p class="kicker">Ch. 116–131 · unfinished</p>',
    )

    # Hiatus
    patch(
        "fun/hiatus.html",
        "We do not invent chapter 131’s title or plot.",
        'Chapter 131 printed as “Tipping Point.” The September health skip is a different rest: <a href="september-2026-rest.html">September 2026</a>. We do not invent chapter 132’s title.',
    )

    # Timeline
    patch(
        "world/timeline.html",
        "Chapter 131 is due 6 September 2026 in the magazine. This table moves when it prints.",
        'Chapter 131, “Tipping Point,” printed 6 September 2026. Chapter 132 is due 28 September 2026 (Jump #44). The first blade is still unnamed. Clocks: <a href="march-twenty-nine.html">March 29</a>, <a href="april-first.html">April 1</a>.',
    )
    patch(
        "world/timeline.html",
        '<tr><td>April 1, noon</td><td><span class="spoiler">Letter sets Irishima’s beach for the Chiaki handover. Three days from the March 29 clock.</span></td><td><a href="../manga/chapter-130.html">Ch. 130</a></td></tr>',
        '<tr><td>April 1, noon</td><td><span class="spoiler">Letter sets Irishima’s beach for the Chiaki handover. Three days from the March 29 clock.</span></td><td><a href="../manga/chapter-130.html">Ch. 130</a> · <a href="april-first.html">April 1</a></td></tr>\n      <tr><td>Magazine, 6 Sep 2026</td><td>Ch. 131 Tipping Point (転換点). Jump 2026 #41. Panels not recapped here.</td><td><a href="../manga/chapter-131.html">Ch. 131</a></td></tr>\n      <tr><td>Magazine, 28 Sep 2026</td><td>Ch. 132 due Jump 2026 #44 after the 42/43 health skip. Title not printed on this desk.</td><td><a href="../manga/chapter-132.html">Ch. 132 door</a></td></tr>',
    )

    # First blade
    patch(
        "world/first-blade.html",
        "The chapters through 130 show the kiln, the eyes, Chiaki as the reason the work stays open, and tamahagane coming out of a collapsed furnace.",
        "The chapters through 131’s listing still show the kiln, the eyes, Chiaki as the reason the work stays open, and tamahagane coming out of a collapsed furnace.",
    )
    patch(
        "world/technique-index.html",
        "The first blade</a> is still unnamed after chapter 130.",
        "The first blade</a> is still unnamed after chapter 131.",
    )

    # Manga guide
    patch(
        "manga/index.html",
        "The chapter index on this site runs through 130, “I'm Fine!” (30 August 2026).",
        "The chapter index on this site runs through 131, “Tipping Point” (6 September 2026).",
    )
    patch(
        "manga/index.html",
        '<a href="chapter-130.html">Chapter 130</a> · <a href="volume-12.html">Volume 12</a>',
        '<a href="chapter-130.html">Chapter 130</a> · <a href="chapter-131.html">Chapter 131</a> · <a href="volume-1.html">Volume 1</a> · <a href="volume-12.html">Volume 12</a>',
    )
    patch(
        "manga/index.html",
        "<h3>Part 2: the forge</h3><p>Princess through I'm Fine! Ch. 116–130.</p>",
        "<h3>Part 2: the forge</h3><p>Princess through Tipping Point. Ch. 116–131.</p>",
    )
    patch(
        "manga/publication.html",
        "The <a href=\"chapters.html\">chapter index</a> is the title list through 130.",
        "The <a href=\"chapters.html\">chapter index</a> is the title list through 131, “Tipping Point.”",
    )
    patch(
        "manga/volume-12.html",
        "Chapter 131 is due 6 September 2026. We do not invent its title.",
        'Chapter 131 is <a href="chapter-131.html">Tipping Point</a>. Chapter 132 is a date, not a title on this desk.',
    )

    # World index bar
    patch(
        "world/index.html",
        ' · <a href="kuro.html">Kuro</a> · <a href="mei.html">Mei</a> · <a href="suzaku.html">Suzaku</a>',
        ' · <a href="owl.html">Owl</a> · <a href="play.html">Play</a> · <a href="flame-bone.html">Flame Bone</a> · <a href="insect-kit.html">Insect kit</a> · <a href="kuro.html">Kuro</a> · <a href="mei.html">Mei</a> · <a href="suzaku.html">Suzaku</a>',
    )
    patch(
        "world/index.html",
        'Part 2 returns to Irishima: Chiaki, the talks, the ore, Kunishige before he was a hermit, Ironworks, <a href="../manga/chapter-130.html">chapter 130</a>.',
        'Part 2 returns to Irishima: Chiaki, the talks, the ore, Kunishige before he was a hermit, Ironworks, <a href="../manga/chapter-130.html">chapter 130</a>, <a href="../manga/chapter-131.html">chapter 131</a>.',
    )

    # Technique catalog leftover links
    TECH = [
        ("<strong>Kuro: Shred 涅千</strong>", '<strong><a href="kuro-shred.html">Kuro: Shred 涅千</a></strong>'),
        ("<strong>Nishiki: Support*</strong>", '<strong><a href="nishiki-support.html">Nishiki: Support*</a></strong>'),
        ("<strong>Cloaked Mei*</strong>", '<strong><a href="cloaked-mei.html">Cloaked Mei*</a></strong>'),
        ("<strong>Mei: Shred 鳴千</strong>", '<strong><a href="mei-shred.html">Mei: Shred 鳴千</a></strong>'),
        ("<strong>Spider 蛛</strong>", '<strong><a href="spider.html">Spider 蛛</a></strong>'),
        ("<strong>Dragonfly 蜻</strong>", '<strong><a href="dragonfly.html">Dragonfly 蜻</a></strong>'),
        ("<strong>Centipede 蜈</strong>", '<strong><a href="centipede.html">Centipede 蜈</a></strong>'),
        ("<strong>Butterfly 蝶</strong>", '<strong><a href="butterfly.html">Butterfly 蝶</a></strong>'),
        ("<strong>Bee 蜂</strong>", '<strong><a href="bee.html">Bee 蜂</a></strong>'),
        ("<strong>Malediction 蠱 (Kodoku)</strong>", '<strong><a href="malediction.html">Malediction 蠱 (Kodoku)</a></strong>'),
        ("<strong>Play 遊</strong>", '<strong><a href="play.html">Play 遊</a></strong>'),
        ("<strong>Destructive Play*</strong>", '<strong><a href="destructive-play.html">Destructive Play*</a></strong>'),
        ("<strong>External Crow*</strong>", '<strong><a href="external-crow.html">External Crow*</a></strong>'),
        ("<strong>Owl 梟</strong>", '<strong><a href="owl.html">Owl 梟</a></strong>'),
        ("<strong>External Suzaku*</strong>", '<strong><a href="external-suzaku.html">External Suzaku*</a></strong>'),
        ("<strong>Suzaku: Black Flames*</strong>", '<strong><a href="black-suzaku.html">Suzaku: Black Flames*</a></strong>'),
        ("<strong>Hiyuki’s Flame Bone</strong>", '<strong>Hiyuki’s <a href="flame-bone.html">Flame Bone</a></strong>'),
        ("<strong>Natsuki’s Lightning Menace (Raiku)</strong>", '<strong>Natsuki’s <a href="lightning-menace.html">Lightning Menace (Raiku)</a></strong>'),
        ("<strong>Hokuto’s armored puppet</strong>", '<strong>Hokuto’s <a href="puppet-armor.html">armored puppet</a></strong>'),
        ("<strong>Kuguri’s Twilight Wave (Hagure)</strong>", '<strong>Kuguri’s <a href="twilight-wave.html">Twilight Wave (Hagure)</a></strong>'),
        ("<strong>Hiruhiko’s Blood Crane (Chizuru)</strong>", '<strong>Hiruhiko’s <a href="blood-crane.html">Blood Crane (Chizuru)</a></strong>'),
        ("<strong>Toto’s blood tracking</strong>", '<strong>Toto’s <a href="blood-track.html">blood tracking</a></strong>'),
        ("<strong>Bingo’s Mako</strong>", '<strong>Bingo’s <a href="mako.html">Mako</a></strong>'),
        ("<strong>Uran’s ice</strong>", '<strong>Uran’s <a href="uran-ice.html">ice</a></strong>'),
        ("<strong>Char’s Kyonagi regeneration</strong>", '<strong>Char’s <a href="kyonagi-regen.html">Kyonagi regeneration</a></strong>'),
        ("<strong>Izaru’s bead chains</strong>", '<strong>Izaru’s <a href="bead-chains.html">bead chains</a></strong>'),
        ("<strong>Subaru’s duplication</strong>", '<strong>Subaru’s <a href="subaru-duplication.html">duplication</a></strong>'),
        ("<strong>True Realm</strong> (Honryō)", '<strong><a href="honryo.html">True Realm</a></strong> (Honryō)'),
    ]
    for old, new in TECH:
        patch("world/techniques.html", old, new)

    # Analysis cards
    patch(
        "analysis/index.html",
        '<a href="foresight.html">Foresight</a> is an office.',
        '<a href="foresight.html">Foresight</a> is an office. <a href="sojo-customer.html">Sojo, customer</a> is the register’s correction. <a href="meals.html">Meals</a> are the method before True Realm. <a href="part-two-clock.html">Part 2’s clock</a> is three days.',
    )
    patch(
        "analysis/index.html",
        '<a class="card" href="../media/index.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/teaser-og.jpg" alt="Anime teaser visual"></div><div class="card-body"><h3>YouTube</h3><p>Theories catalogued, not stacked.</p></div></a>',
        '''<a class="card" href="meals.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Meals in the title list"></div><div class="card-body"><h3>The plate before the cut</h3><p>Food, Tea, Peace. Then True Realm.</p></div></a>
      <a class="card" href="sojo-customer.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Sojo, customer"></div><div class="card-body"><h3>Sojo, customer</h3><p>He paid for a sword. He is not Hishaku.</p></div></a>
      <a class="card" href="part-two-clock.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Part 2 clock"></div><div class="card-body"><h3>Part 2’s clock</h3><p>March 29. April 1. Three days.</p></div></a>
      <a class="card" href="quotation-marks.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol11.webp" alt="Quotes on the press"></div><div class="card-body"><h3>Quotes on the press</h3><p>Strongest. Sword Master. Heroes.</p></div></a>
      <a class="card" href="../media/index.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/teaser-og.jpg" alt="Anime teaser visual"></div><div class="card-body"><h3>YouTube</h3><p>Theories catalogued, not stacked.</p></div></a>''',
    )

    # Fun cards
    patch(
        "fun/index.html",
        '<a class="card" href="circulation.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Circulation"></div><div class="card-body"><h3>Circulation</h3><p>350,000 to 4 million. The count.</p></div></a>',
        '''<a class="card" href="circulation.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Circulation"></div><div class="card-body"><h3>Circulation</h3><p>350,000 to 4 million. The count.</p></div></a>
      <a class="card" href="september-2026-rest.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="September rest"></div><div class="card-body"><h3>The September rest</h3><p>Issue 44. Chapter 132’s door.</p></div></a>
      <a class="card" href="first-issue.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="First issue"></div><div class="card-body"><h3>The first issue</h3><p>2023 #42. Mission. Most-viewed new title.</p></div></a>
      <a class="card" href="chapter-titles.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Chapter titles"></div><div class="card-body"><h3>Chapter titles</h3><p>Meals, names, quotation marks.</p></div></a>
      <a class="card" href="volume-spines.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol11.webp" alt="Volume spines"></div><div class="card-body"><h3>Eleven spines</h3><p>Mission through Heroes, each with a room.</p></div></a>''',
    )
    patch(
        "fun/index.html",
        "<h3>Part 2</h3><p>Princess, talks, Ironworks. Ch. 116–129.</p>",
        "<h3>Part 2</h3><p>Princess through Tipping Point. Ch. 116–131.</p>",
    )

    # Guide cards
    patch(
        "guide/index.html",
        '<a class="card" href="reading-order.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="How to read"></div><div class="card-body"><h3>How to read</h3><p>Chapter 1 through Part 2. Volumes versus the weekly issue.</p></div></a>',
        '''<a class="card" href="reading-order.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="How to read"></div><div class="card-body"><h3>How to read</h3><p>Chapter 1 through Part 2. Volumes versus the weekly issue.</p></div></a>
      <a class="card" href="chapter-map.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Chapter map"></div><div class="card-body"><h3>Chapter map</h3><p>Every weekly title. Leftover rooms linked.</p></div></a>
      <a class="card" href="volume-map.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Volume map"></div><div class="card-body"><h3>Volume map</h3><p>Eleven jackets and one solicited close.</p></div></a>
      <a class="card" href="technique-map.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="Technique map"></div><div class="card-body"><h3>Technique map</h3><p>Blade kit and innate doors.</p></div></a>
      <a class="card" href="mega-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol2.webp" alt="Mega doors"></div><div class="card-body"><h3>Mega update</h3><p>New rooms this wave, from printed facts.</p></div></a>''',
    )

    # Factions
    patch(
        "factions/index.html",
        "Soga and Mikaboshi: <a href=\"soga.html\">the clan page</a>.",
        "Soga: <a href=\"soga.html\">the clan page</a>. Mikaboshi: <a href=\"mikaboshi.html\">the island kings</a>. Leadership table: <a href=\"leadership.html\">the heads</a>.",
    )
    patch(
        "factions/index.html",
        '<a href="soga.html">Soga and Mikaboshi</a>.',
        '<a href="soga.html">Soga</a>, <a href="mikaboshi.html">Mikaboshi</a>, <a href="leadership.html">leadership</a>.',
    )

    # Guide part-2
    patch(
        "guide/part-2.html",
        "The printed run through 130 is still the talks, the kiln, and one beach that has not happened yet.",
        "The printed run through 131 is still the talks, the kiln, one reunion, and a magazine word titled Tipping Point. Chapter 132 is a date, not a title here.",
    )

    # Footer extras
    js = (ROOT / "js/site.js").read_text(encoding="utf-8")
    old_f = '<li><a href="${R}manga/part-2.html">Part 2</a></li>'
    new_f = '<li><a href="${R}manga/part-2.html">Part 2</a></li>\n            <li><a href="${R}manga/chapter-131.html">Chapter 131</a></li>\n            <li><a href="${R}guide/volume-map.html">Volume map</a></li>'
    if new_f not in js:
        if old_f not in js:
            raise SystemExit("footer part-2 missing")
        (ROOT / "js/site.js").write_text(js.replace(old_f, new_f, 1), encoding="utf-8")
        print("patched js/site.js footer")
    else:
        print("already js footer")

    # llms
    patch(
        "llms.txt",
        "Part 2 starts at chapter 116. Latest close reading on this site: chapter 130, I'm Fine! (30 Aug 2026).",
        "Part 2 starts at chapter 116. Latest titled chapter room: chapter 131, Tipping Point (6 Sep 2026). Chapter 132 is a publication door (Jump 2026 #44, 28 Sep 2026) without a printed title on this desk.",
    )
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    extra = (
        "- [Chapter 131 Tipping Point](https://kagurabachi.org/manga/chapter-131.html)\n"
        "- [Volume map](https://kagurabachi.org/guide/volume-map.html)\n"
        "- [Technique map](https://kagurabachi.org/guide/technique-map.html)\n"
        "- [September 2026 rest](https://kagurabachi.org/fun/september-2026-rest.html)\n"
    )
    if "chapter-131.html" not in llms:
        llms = llms.replace(
            "- [Chapter index](https://kagurabachi.org/manga/chapters.html)\n",
            "- [Chapter index](https://kagurabachi.org/manga/chapters.html)\n" + extra,
        )
        (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
        print("patched llms.txt hubs")

    # Malediction printed kanji is 蠱, not 呪禍
    mal = ROOT / "world/malediction.html"
    mt = mal.read_text(encoding="utf-8")
    if "呪禍" in mt:
        mal.write_text(mt.replace("呪禍", "蠱"), encoding="utf-8")
        print("fixed malediction kanji to 蠱")

    # seo overrides for new hubs
    seo = ROOT / "tools/seo_apply.py"
    st = seo.read_text(encoding="utf-8")
    if "manga/chapter-131.html" not in st:
        st = st.replace(
            '"manga/chapter-114.html": "Kagurabachi Chapter 114 “Kunishige Rokuhira”",',
            '"manga/chapter-114.html": "Kagurabachi Chapter 114 “Kunishige Rokuhira”",\n'
            '    "manga/chapter-131.html": "Kagurabachi Chapter 131 “Tipping Point”",\n'
            '    "manga/chapter-132.html": "Kagurabachi Chapter 132 | Jump 2026 Issue 44",',
        )
        st = st.replace(
            '"manga/chapters.html": "Kagurabachi Chapter Index | Titles from Mission to I\'m Fine!",',
            '"manga/chapters.html": "Kagurabachi Chapter Index | Titles from Mission to Tipping Point",',
        )
        st = st.replace(
            '"world/register.html": "Kagurabachi Name Register | Every Named Figure Through Ch. 130",',
            '"world/register.html": "Kagurabachi Name Register | Every Named Figure Through Ch. 131",',
        )
        seo.write_text(st, encoding="utf-8")
        print("patched seo title overrides")
    terms_old = '    "world/duel-domain.html": ("Duel Domain", None),\n}'
    terms_new = '''    "world/duel-domain.html": ("Duel Domain", None),
    "world/owl.html": ("Owl", "梟"),
    "world/play.html": ("Play", "遊"),
    "world/kuro-shred.html": ("Kuro: Shred", "涅千"),
    "world/mei-shred.html": ("Mei: Shred", "鳴千"),
    "world/spider.html": ("Spider", "蛛"),
    "world/dragonfly.html": ("Dragonfly", "蜻"),
    "world/centipede.html": ("Centipede", "蜈"),
    "world/butterfly.html": ("Butterfly", "蝶"),
    "world/bee.html": ("Bee", "蜂"),
    "world/flame-bone.html": ("Flame Bone", None),
    "world/lightning-menace.html": ("Lightning Menace", "雷躯"),
    "world/honryo.html": ("True Realm", "本領"),
    "world/mako.html": ("Mako", "魔咬"),
}
'''
    st = seo.read_text(encoding="utf-8")
    if '"world/owl.html": ("Owl", "梟")' not in st:
        if terms_old not in st:
            raise SystemExit("TECHNIQUE_TERMS closer missing")
        seo.write_text(st.replace(terms_old, terms_new, 1), encoding="utf-8")
        print("patched TECHNIQUE_TERMS")
    else:
        print("already TECHNIQUE_TERMS")

    print("wire done")


if __name__ == "__main__":
    main()
