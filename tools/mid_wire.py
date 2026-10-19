#!/usr/bin/env python3
"""Wire hubs for the 17 Oct brand-new-content wave."""
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
    patch("index.html", "<div><b>133</b><span>serialized chapters</span></div>", "<div><b>134</b><span>serialized chapters</span></div>")
    patch_if(
        "index.html",
        "Princess through a live 133, ch. 116–133",
        "Princess through Masters of the Sword, ch. 116–134",
    )
    patch_if(
        "index.html",
        "Still unnamed after the live 133",
        "Still unnamed after chapter 134",
    )
    patch_if(
        "index.html",
        "133 is live untitled. 134 is Jump #46",
        "133 is Version II. 134 is 剣豪. 135 is next",
    )
    patch(
        "index.html",
        '"dateModified": "2026-10-07"',
        '"dateModified": "2026-10-17"',
    )
    patch(
        "index.html",
        '      <a class="home-row" href="collectibles/english-volume-10.html"><img loading="lazy" decoding="async" src="assets/covers/vol9.jpg" alt="English 10"><b>English volume 10</b><small>2 February 2027. ISBN 978-1-9747-6947-6</small></a>',
        '      <a class="home-row" href="collectibles/english-volume-10.html"><img loading="lazy" decoding="async" src="assets/covers/vol9.jpg" alt="English 10"><b>English volume 10</b><small>2 February 2027. ISBN 978-1-9747-6947-6</small></a>\n'
        '      <a class="home-row" href="manga/chapter-133.html"><img loading="lazy" decoding="async" src="assets/portraits/sojo.webp" alt="Chapter 133"><b>Chapter 133, Misaka Version II</b><small>巳坂二号. Jump 2026 #45. 4 October</small></a>\n'
        '      <a class="home-row" href="manga/chapter-134.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol10.webp" alt="Chapter 134"><b>Chapter 134, Masters of the Sword</b><small>剣豪. Jump 2026 #46. 11 October</small></a>\n'
        '      <a class="home-row" href="guide/mid-october-update.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol1.webp" alt="Mid-October update"><b>Mid-October update</b><small>Wikipedia printed two words. 135 is a date</small></a>\n'
        '      <a class="home-row" href="world/shiba-birthday.html"><img loading="lazy" decoding="async" src="assets/portraits/chihiro.webp" alt="Shiba birthday"><b>Shiba’s 15 October</b><small>One of five printed birthdays</small></a>',
    )

    patch(
        "manga/chapters.html",
        "Kagurabachi Chapter Index | Titles from Mission to Misaka",
        "Kagurabachi Chapter Index | Titles from Mission to Masters of the Sword",
    )
    patch(
        "manga/chapters.html",
        "Chapter 133 is live on VIZ (4 October 2026) with no subtitle this desk will file. Chapter 134 is due Jump 2026 issue 46 (12 October 2026); we do not invent its title.",
        "Chapter 133, “Misaka Version II” (巳坂二号), printed 4 October 2026 (Jump 2026 #45). Chapter 134, “Masters of the Sword” (剣豪), printed 11 October 2026 (Jump 2026 #46). Chapter 135 is due Jump 2026 issue 47 (19 October 2026); we do not invent its title.",
    )
    patch(
        "manga/chapters.html",
        "118–120 stay unlinked. 132 is Misaka. 133 is live untitled. 134 is a door.",
        "118–120 stay unlinked. 132 is Misaka. 133 is Version II. 134 is 剣豪. 135 is a door.",
    )
    patch(
        "manga/chapters.html",
        '<tr><td><a href="chapter-133.html">133</a></td><td>Untitled here</td><td>第133話</td></tr></tbody>',
        '<tr><td><a href="chapter-133.html">133</a></td><td>Misaka Version II</td><td>巳坂二号</td></tr>'
        '<tr><td><a href="chapter-134.html">134</a></td><td>Masters of the Sword</td><td>剣豪</td></tr></tbody>',
    )

    patch_if("manga/part-2.html", "Ch. 116–133 · unfinished", "Ch. 116–134 · unfinished")
    patch_if(
        "manga/part-2.html",
        "Chapter 133 is live on VIZ with no subtitle this desk will file. Chapter 134 is the next magazine door.",
        "Chapter 133 is <a href=\"chapter-133.html\">Misaka Version II</a> (巳坂二号). Chapter 134 is <a href=\"chapter-134.html\">Masters of the Sword</a> (剣豪). Chapter 135 is the next magazine door.",
    )

    insert_before(
        "characters/bonds.html",
        "  <p>Official chapters live on",
        "  <h2>Mid-October leftover pairs</h2>\n"
        "  <p><a href=\"chihiro-and-chiaki.html\">Chihiro and Chiaki</a>. <a href=\"chihiro-and-akemura.html\">Chihiro and Akemura</a>. <a href=\"chiaki-and-akemura.html\">Chiaki and Akemura</a>. <a href=\"hakuri-and-kiri.html\">Hakuri and Kiri</a>. <a href=\"kiri-and-uruha.html\">Kiri and Uruha</a>. <a href=\"kiri-and-samura.html\">Kiri and Samura</a>. <a href=\"hagiwara-and-kugara.html\">Hagiwara and Kugara</a>. <a href=\"ro-and-samura.html\">Ro and Samura</a>. <a href=\"moku-and-sumi.html\">Moku and Sumi</a>. <a href=\"subaru-and-chihiro.html\">Subaru and Chihiro</a>. <a href=\"azami-and-kasen.html\">Azami and Kasen</a>. <a href=\"chiaki-and-hiroto.html\">Chiaki and Hiroto</a>. <a href=\"uruha-and-hokuto.html\">Uruha and Hokuto</a>. <a href=\"tafuku-and-chihiro.html\">Tafuku and Chihiro</a>. <a href=\"fushimi-and-uruha.html\">Fushimi and Uruha</a>. <a href=\"tenri-and-kyora.html\">Tenri and Kyora</a>. <a href=\"yoshinojo-and-hiroto.html\">Yoshinojo and Hiroto</a>. <a href=\"kazane-and-hagiwara.html\">Kazane and Hagiwara</a>.</p>\n",
    )

    insert_before(
        "fun/index.html",
        '      <a class="card" href="bathhouse-quest-2.html">',
        '      <a class="card" href="jump-2026-47.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Issue 47"></div><div class="card-body"><h3>Jump 2026 #47</h3><p>Chapter 135’s magazine date.</p></div></a>\n'
        '      <a class="card" href="mid-october-2026.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Mid-October"></div><div class="card-body"><h3>Mid-October 2026</h3><p>Version II, then 剣豪, then a countdown.</p></div></a>\n'
        '      <a class="card" href="shiba-october.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Shiba October"></div><div class="card-body"><h3>Shiba’s October</h3><p>15 October. One of five dates.</p></div></a>\n',
    )
    patch_if(
        "fun/index.html",
        "<h3>October 2026</h3><p>133 live untitled. English 10 solicited.</p>",
        "<h3>October 2026</h3><p>Version II. 剣豪. 135 is a date.</p>",
    )
    patch_if(
        "fun/index.html",
        "<h3>Jump 2026 #45</h3><p>Chapter 133 ran. No subtitle here.</p>",
        "<h3>Jump 2026 #45</h3><p>Misaka Version II. 巳坂二号.</p>",
    )
    patch_if(
        "fun/index.html",
        "<h3>Jump 2026 #46</h3><p>Chapter 134’s magazine date.</p>",
        "<h3>Jump 2026 #46</h3><p>Masters of the Sword. 剣豪.</p>",
    )
    patch_if(
        "fun/index.html",
        "Princess through a live 133. Ch. 116–133.",
        "Princess through Masters of the Sword. Ch. 116–134.",
    )

    insert_before(
        "analysis/index.html",
        '      <a class="card" href="../media/index.html">',
        '      <a class="card" href="version-two.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Version II"></div><div class="card-body"><h3>Version II</h3><p>A house name plus a number.</p></div></a>\n'
        '      <a class="card" href="kengo-versus-kenshi.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol10.webp" alt="剣豪"></div><div class="card-body"><h3>剣豪 versus 剣士たち</h3><p>Weekly rank. Jacket ensemble.</p></div></a>\n'
        '      <a class="card" href="two-casts.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/teaser-og.jpg" alt="Two casts"></div><div class="card-body"><h3>Two official casts</h3><p>Voiced comic versus Cypic.</p></div></a>\n',
    )

    insert_before(
        "guide/index.html",
        '      <a class="card" href="bond-map.html">',
        '      <a class="card" href="mid-october-update.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Mid-October"></div><div class="card-body"><h3>Mid-October update</h3><p>Version II, 剣豪, leftover pairs.</p></div></a>\n'
        '      <a class="card" href="after-version-two.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="After Version II"></div><div class="card-body"><h3>After Version II</h3><p>How to keep reading the war book.</p></div></a>\n',
    )
    patch_if(
        "guide/index.html",
        "<h3>Current week</h3><p>Misaka titled. 133 live. 134 a date.</p>",
        "<h3>Current week</h3><p>Version II. 剣豪. 135 a date.</p>",
    )

    insert_before(
        "collectibles/index.html",
        "     <h2>Circulation &amp; awards</h2>",
        "     <p>English volume 1, the first trade, now has its own door: <a href=\"english-volume-1.html\">5 November 2024</a> (ISBN 978-1-9747-4724-5).</p>\n\n",
    )

    insert_before(
        "media/index.html",
        "    <h2>The arguments</h2>",
        "    <p>Two official casts, split: <a href=\"two-chihiros.html\">Chihiro</a>, <a href=\"two-kunishiges.html\">Kunishige</a>, <a href=\"two-shibas.html\">Shiba</a>, <a href=\"two-hinaos.html\">Hinao</a>. Voiced-comic Shiba: <a href=\"fukushima.html\">Jun Fukushima</a>.</p>\n",
    )

    patch_if(
        "fun/year-2026.html",
        "A titled house, a live number, a date, and an English spine still in the mail.",
        "Two Misaka weeks, then 剣豪, then a date.",
    )

    print("mid_wire done")


if __name__ == "__main__":
    main()
