#!/usr/bin/env python3
"""Link the 55 new rooms into indexes. Idempotent enough to run once."""
from pathlib import Path

ROOT = Path("/workspace")
NEW_CHS = [4, 5, 7, 19, 20, 32, 41, 45, 48, 56, 59, 66, 75, 80, 92, 97, 99, 105, 106, 110, 113, 114]


def patch(rel, old, new):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if new in text and old not in text:
        print("already", rel, old[:40])
        return
    if old not in text:
        raise SystemExit(f"missing needle in {rel}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)


def link_chapters_table():
    path = ROOT / "manga/chapters.html"
    text = path.read_text(encoding="utf-8")
    for n in NEW_CHS:
        old = f"<td>{n}</td>"
        new = f'<td><a href="chapter-{n}.html">{n}</a></td>'
        if old not in text:
            if new in text:
                print("already linked", n)
                continue
            raise SystemExit(f"chapter cell missing: {n}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print("linked chapter table")


link_chapters_table()

patch(
    "manga/chapters.html",
    "Chapter rooms on this site cover the issues people actually search: <a href=\"chapter-1.html\">1</a>, <a href=\"chapter-14.html\">True Realm</a>, <a href=\"chapter-18.html\">Roar</a>, <a href=\"chapter-44.html\">The Curtain Falls</a>, <a href=\"chapter-76.html\">Banquet</a>, <a href=\"chapter-82.html\">Enten vs Tobimune</a>, <a href=\"chapter-117.html\">Irishima Talks</a>, <a href=\"chapter-125.html\">Smelting</a>, <a href=\"chapter-129.html\">Ironworks</a>, <a href=\"chapter-130.html\">I'm Fine!</a>, and the rest of the linked numbers in the table.",
    "Chapter rooms on this site cover the issues people actually search: <a href=\"chapter-1.html\">1</a>, <a href=\"chapter-4.html\">Sorcery and the Enchanted Blade</a>, <a href=\"chapter-5.html\">A Good Meal</a>, <a href=\"chapter-19.html\">Knight of Darkness</a>, <a href=\"chapter-48.html\">Steam Squad</a>, <a href=\"chapter-76.html\">Banquet</a>, <a href=\"chapter-113.html\">Rock</a>, <a href=\"chapter-114.html\">Kunishige Rokuhira</a>, <a href=\"chapter-130.html\">I'm Fine!</a>, and the rest of the linked numbers in the table.",
)

patch(
    "manga/chapters.html",
    "Close readings: <a href=\"chapter-1.html\">1</a>, <a href=\"chapter-18.html\">18</a>, <a href=\"chapter-115.html\">115</a>, <a href=\"chapter-129.html\">129</a>, <a href=\"chapter-130.html\">130</a>.",
    "Close readings: <a href=\"chapter-1.html\">1</a>, <a href=\"chapter-19.html\">19</a>, <a href=\"chapter-48.html\">48</a>, <a href=\"chapter-113.html\">113</a>, <a href=\"chapter-115.html\">115</a>, <a href=\"chapter-130.html\">130</a>. Volume 12: <a href=\"volume-12.html\">solicited spine</a>.",
)

# World index link bar
patch(
    "world/index.html",
    " · <a href=\"first-blade.html\">First blade</a> · <a href=\"../factions/hishaku.html\">Hishaku</a>",
    " · <a href=\"first-blade.html\">First blade</a> · <a href=\"kuro.html\">Kuro</a> · <a href=\"mei.html\">Mei</a> · <a href=\"suzaku.html\">Suzaku</a> · <a href=\"tamahagane.html\">Tamahagane</a> · <a href=\"handover.html\">Handover</a> · <a href=\"teleport.html\">Teleport</a> · <a href=\"../factions/hishaku.html\">Hishaku</a>",
)

# Technique catalog: link named kit
TECH_LINKS = [
    ("<strong>Kuro 涅</strong>", '<strong><a href="kuro.html">Kuro 涅</a></strong>'),
    ("<strong>Aka 猩</strong>", '<strong><a href="aka.html">Aka 猩</a></strong>'),
    ("<strong>Nishiki 錦</strong>", '<strong><a href="nishiki.html">Nishiki 錦</a></strong>'),
    ("<strong>Mei 鳴</strong>", '<strong><a href="mei.html">Mei 鳴</a></strong>'),
    ("<strong>Yui 結</strong>", '<strong><a href="yui.html">Yui 結</a></strong>'),
    ("<strong>Kou 降</strong>", '<strong><a href="kou.html">Kou 降</a></strong>'),
    ("<strong>Banquet 宴</strong>", '<strong><a href="banquet-art.html">Banquet 宴</a></strong>'),
    ("<strong>Crow 鴉</strong>", '<strong><a href="crow.html">Crow 鴉</a></strong>'),
    ("<strong>Suzaku 雀</strong>", '<strong><a href="suzaku.html">Suzaku 雀</a></strong>'),
    ("<strong>Shiba’s teleport</strong>", '<strong><a href="teleport.html">Shiba’s teleport</a></strong>'),
    ("<strong>Azami’s Coin (Koin)</strong>", '<strong><a href="coin.html">Azami’s Coin (Koin)</a></strong>'),
    ("<strong>Hakuri’s Isou and Storehouse</strong>", '<strong>Hakuri’s <a href="isou.html">Isou</a> and Storehouse</strong>'),
    ("<strong>Tafuku’s duel domain</strong>", '<strong>Tafuku’s <a href="duel-domain.html">duel domain</a></strong>'),
    ("<strong>Hiroto Soga’s Kurotsuchi</strong>", '<strong>Hiroto Soga’s <a href="kurotsuchi.html">Kurotsuchi</a></strong>'),
    ("<strong>Ariu Mikaboshi’s Sumika</strong>", '<strong>Ariu Mikaboshi’s <a href="sumika.html">Sumika</a></strong>'),
    ("<strong>Kudo’s Warrior’s Path</strong>", '<strong>Kudo’s <a href="warriors-path.html">Warrior’s Path</a></strong>'),
    ("<strong>Hagiwara’s Jikai</strong>", '<strong>Hagiwara’s <a href="jikai.html">Jikai</a></strong>'),
    ("<strong>Mashiro’s Akuu</strong>", '<strong>Mashiro’s <a href="akuu.html">Akuu</a></strong>'),
]
for old, new in TECH_LINKS:
    patch("world/techniques.html", old, new)

# Technique index name cells
INDEX_LINKS = [
    ("<tr><td>Kuro 涅</td>", '<tr><td><a href="kuro.html">Kuro 涅</a></td>'),
    ("<tr><td>Aka 猩</td>", '<tr><td><a href="aka.html">Aka 猩</a></td>'),
    ("<tr><td>Nishiki 錦</td>", '<tr><td><a href="nishiki.html">Nishiki 錦</a></td>'),
    ("<tr><td>Mei 鳴</td>", '<tr><td><a href="mei.html">Mei 鳴</a></td>'),
    ("<tr><td>Yui 結</td>", '<tr><td><a href="yui.html">Yui 結</a></td>'),
    ("<tr><td>Kou 降</td>", '<tr><td><a href="kou.html">Kou 降</a></td>'),
    ("<tr><td>Banquet 宴</td>", '<tr><td><a href="banquet-art.html">Banquet 宴</a></td>'),
    ("<tr><td>Crow 鴉</td>", '<tr><td><a href="crow.html">Crow 鴉</a></td>'),
    ("<tr><td>Suzaku 雀</td>", '<tr><td><a href="suzaku.html">Suzaku 雀</a></td>'),
    ("<tr><td>Teleportation</td>", '<tr><td><a href="teleport.html">Teleportation</a></td>'),
    ("<tr><td>Coin (Koin)</td>", '<tr><td><a href="coin.html">Coin (Koin)</a></td>'),
    ("<tr><td>Isou</td>", '<tr><td><a href="isou.html">Isou</a></td>'),
    ("<tr><td>Duel domain</td>", '<tr><td><a href="duel-domain.html">Duel domain</a></td>'),
    ("<tr><td>Kurotsuchi</td>", '<tr><td><a href="kurotsuchi.html">Kurotsuchi</a></td>'),
    ("<tr><td>Sumika</td>", '<tr><td><a href="sumika.html">Sumika</a></td>'),
    ("<tr><td>Warrior’s Path (Shitō)</td>", '<tr><td><a href="warriors-path.html">Warrior’s Path (Shitō)</a></td>'),
    ("<tr><td>Jikai</td>", '<tr><td><a href="jikai.html">Jikai</a></td>'),
    ("<tr><td>Akuu</td>", '<tr><td><a href="akuu.html">Akuu</a></td>'),
    ("<tr><td>Gansui</td>", '<tr><td><a href="gansui.html">Gansui</a></td>'),
    ("<tr><td>Foresight</td>", '<tr><td><a href="../analysis/foresight.html">Foresight</a></td>'),
]
# Yukisada vessel row
INDEX_LINKS.append(
    (
        "<tr><td>Regeneration (Hishaku)</td><td>Yukisada</td><td>Survives decapitation; Vessel</td><td><a href=\"../characters/yukisada.html\">Yukisada</a></td></tr>",
        "<tr><td>Regeneration (Hishaku)</td><td>Yukisada</td><td>Survives decapitation; <a href=\"vessel.html\">Vessel</a></td><td><a href=\"../characters/yukisada.html\">Yukisada</a></td></tr>",
    )
)
for old, new in INDEX_LINKS:
    patch("world/technique-index.html", old, new)

# Analysis cards
patch(
    "analysis/index.html",
    '<a class="card" href="../media/index.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/teaser-og.jpg" alt="Anime teaser visual"></div><div class="card-body"><h3>YouTube</h3><p>Theories catalogued, not stacked.</p></div></a>',
    '''<a class="card" href="hakuri.html"><div class="card-art p-chihiro"><img loading="lazy" decoding="async" src="../assets/portraits/hakuri.webp" alt="Hakuri and the architecture"></div><div class="card-body"><h3>Hakuri and the architecture</h3><p>Isou, Storehouse, the walking Kura.</p></div></a>
      <a class="card" href="suzaku.html"><div class="card-art blade-tobimune"><img loading="lazy" decoding="async" src="../assets/portraits/samura.webp" alt="Suzaku, the cut that keeps"></div><div class="card-body"><h3>Suzaku, the cut that keeps</h3><p>Contract surgery. Then the life spend.</p></div></a>
      <a class="card" href="foresight.html"><div class="card-art p-akemura"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Foresight as an office"></div><div class="card-body"><h3>Foresight as an office</h3><p>Princess Soga. Warrant, then cargo.</p></div></a>
      <a class="card" href="../media/index.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/teaser-og.jpg" alt="Anime teaser visual"></div><div class="card-body"><h3>YouTube</h3><p>Theories catalogued, not stacked.</p></div></a>''',
)

patch(
    "analysis/index.html",
    '<a href="copy.html">Copying</a> is a smith’s son shutting his eyes in a Hishaku’s hallway.',
    '<a href="copy.html">Copying</a> is a smith’s son shutting his eyes in a Hishaku’s hallway. <a href="hakuri.html">Hakuri</a> is the architecture answering. <a href="suzaku.html">Suzaku</a> is the cut that keeps. <a href="foresight.html">Foresight</a> is an office.',
)

# Fun cards
patch(
    "fun/index.html",
    '<a class="card" href="hiatus.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="The 2026 rest"></div><div class="card-body"><h3>The 2026 rest</h3><p>After Fire. Before Ironworks.</p></div></a>',
    '''<a class="card" href="hiatus.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="The 2026 rest"></div><div class="card-body"><h3>The 2026 rest</h3><p>After Fire. Before Ironworks.</p></div></a>
      <a class="card" href="enten-oneshot.html"><div class="card-art blade-enten"><img loading="lazy" decoding="async" src="../assets/covers/hokazono-commemorative.jpg" alt="The Enten one-shot"></div><div class="card-body"><h3>The Enten one-shot</h3><p>炎天. Tezuka. Not 淵天.</p></div></a>
      <a class="card" href="circulation.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Circulation"></div><div class="card-body"><h3>Circulation</h3><p>350,000 to 4 million. The count.</p></div></a>''',
)

# Homepage fresh steel
patch(
    "index.html",
    '<a class="home-row" href="world/first-blade.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="The first blade"><b>The first blade</b><small>Still unnamed after chapter 130</small></a>',
    '''<a class="home-row" href="world/first-blade.html"><img loading="lazy" decoding="async" src="assets/panels/ch113.png" alt="The first blade"><b>The first blade</b><small>Still unnamed after chapter 130</small></a>
      <a class="home-row" href="manga/chapter-19.html"><img loading="lazy" decoding="async" src="assets/portraits/hiyuki.webp" alt="Chapter 19"><b>Chapter 19, Knight of Darkness</b><small>Hiyuki arrives. Volume 3 opens</small></a>
      <a class="home-row" href="world/kuro.html"><img loading="lazy" decoding="async" src="assets/panels/enten.webp" alt="Kuro"><b>Kuro, Aka, Nishiki</b><small>Enten’s kit, each with a room</small></a>
      <a class="home-row" href="manga/volume-12.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol11.webp" alt="Volume 12"><b>Volume 12</b><small>4 September 2026. Karma through Swordsmith</small></a>
      <a class="home-row" href="analysis/suzaku.html"><img loading="lazy" decoding="async" src="assets/portraits/samura.webp" alt="Suzaku"><b>Suzaku</b><small>The cut that keeps. Then the life spend</small></a>''',
)

# Manga guide
patch(
    "manga/index.html",
    '<a href="chapter-130.html">Chapter 130</a> · <a href="covers.html">Cover studies</a>',
    '<a href="chapter-130.html">Chapter 130</a> · <a href="volume-12.html">Volume 12</a> · <a href="covers.html">Cover studies</a>',
)
patch(
    "manga/index.html",
    '<a class="card" href="author-comments.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/hokazono-commemorative.jpg" alt="Author comments"></div><div class="card-body"><h3>Author comments</h3><p>The boxes that changed the dates.</p></div></a>',
    '''<a class="card" href="author-comments.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/hokazono-commemorative.jpg" alt="Author comments"></div><div class="card-body"><h3>Author comments</h3><p>The boxes that changed the dates.</p></div></a>
       <a class="card" href="volume-12.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol11.webp" alt="Volume 12"></div><div class="card-body"><h3>Volume 12</h3><p>Solicited 4 September 2026. Karma through Swordsmith.</p></div></a>
       <a class="card" href="chapter-19.html"><div class="card-art p-hiyuki"><img loading="lazy" decoding="async" src="../assets/portraits/hiyuki.webp" alt="Chapter 19"></div><div class="card-body"><h3>Chapter 19, Knight of Darkness</h3><p>Hiyuki arrives. The auction starts.</p></div></a>
       <a class="card" href="chapter-48.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch056.png" alt="Chapter 48"></div><div class="card-body"><h3>Chapter 48, Steam Squad</h3><p>Named in a title. Buried the same week.</p></div></a>
       <a class="card" href="chapter-113.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Chapter 113 Rock"></div><div class="card-body"><h3>Chapter 113, Rock</h3><p>The island splash. First blade still unnamed.</p></div></a>''',
)

# Volumes + synopses
patch(
    "manga/volumes.html",
    "Volume 12 (4 September 2026, ISBN 978-4-08-885177-8) is expected to close Part 1 (chs. 106–115) and open the war book.",
    '<a href="volume-12.html">Volume 12</a> (4 September 2026, ISBN 978-4-08-885177-8) is expected to close Part 1 (chs. 106–115) and open the war book.',
)
patch(
    "manga/synopses.html",
    '<h2 id="volume-12">Volume 12 (solicited) and the uncollected close</h2>',
    '<h2 id="volume-12">Volume 12 (solicited) and the uncollected close</h2>\n      <p>Dedicated room: <a href="volume-12.html">Volume 12</a>.</p>',
)
patch(
    "fun/hokazono.html",
    "<li><em>Enten</em> (炎天), 100th Tezuka Award, printed in <em>Jump Giga</em> Spring 2021. Different story, same hunger for a named sword.</li>",
    "<li><em>Enten</em> (炎天), 100th Tezuka Award, printed in <em>Jump Giga</em> Spring 2021. Different story, same hunger for a named sword. Room: <a href=\"enten-oneshot.html\">the one-shot</a>.</li>",
)
patch(
    "manga/publication.html",
    "<h2>Circulation</h2>",
    '<h2>Circulation</h2>\n      <p>The count as its own room: <a href="../fun/circulation.html">circulation</a>.</p>',
)
print("done")
