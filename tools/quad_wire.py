#!/usr/bin/env python3
"""Wire quadruple-wave rooms into indexes. Run after generators."""
from pathlib import Path

ROOT = Path("/workspace")


def patch(rel, old, new):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if new in text and old not in text:
        print("already", rel, old[:40].replace("\n", " "))
        return
    if old not in text:
        raise SystemExit(f"missing needle in {rel}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched", rel)


def main():
    patch(
        "index.html",
        '      <a class="home-row" href="guide/mega-doors.html"><img loading="lazy" decoding="async" src="assets/panels/ch001.png" alt="Mega doors"><b>Mega update doors</b><small>Leftover titles, volumes, leftover kit</small></a>',
        '      <a class="home-row" href="guide/mega-doors.html"><img loading="lazy" decoding="async" src="assets/panels/ch001.png" alt="Mega doors"><b>Mega update doors</b><small>Leftover titles, volumes, leftover kit</small></a>\n'
        '      <a class="home-row" href="guide/quad-doors.html"><img loading="lazy" decoding="async" src="assets/covers/jp-vol5.webp" alt="Quadruple wave"><b>Quadruple wave</b><small>Bonds, fight desks, volume reads, new essays</small></a>\n'
        '      <a class="home-row" href="characters/bonds.html"><img loading="lazy" decoding="async" src="assets/portraits/chihiro.webp" alt="Printed bonds"><b>Printed bonds</b><small>Household, auction, Iai, kiln pairs</small></a>\n'
        '      <a class="home-row" href="world/battle-index.html"><img loading="lazy" decoding="async" src="assets/panels/ch009.png" alt="Fight desks"><b>Fight desks</b><small>Raid, weather, auction, hotel, HQ</small></a>',
    )

    patch(
        "characters/index.html",
        '    <h2>Chihiro’s circle</h2>',
        '    <p>This wave’s pair rooms live on <a href="bonds.html">printed bonds</a>: household, auction, Iai school, Hishaku jobs, cafe, kiln. They are printed jobs, not shipping essays.</p>\n    <h2>Chihiro’s circle</h2>',
    )
    patch(
        "characters/index.html",
        '      <a class="card" href="chihiro.html">',
        '      <a class="card" href="bonds.html"><div class="card-art p-chihiro"><img src="../assets/portraits/chihiro.webp" alt="Printed bonds"></div><div class="card-body"><span class="tag">Pairs</span><h3>Printed bonds</h3><p>Who stood next to whom, as printed.</p></div></a>\n      <a class="card" href="chihiro.html">',
    )

    patch(
        "analysis/index.html",
        '      <a class="card" href="part-two-clock.html">',
        '      <a class="card" href="two-deadlocks.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Two Deadlocks"></div><div class="card-body"><h3>Two Deadlocks</h3><p>拮抗, then 均衡. Same English.</p></div></a>\n'
        '      <a class="card" href="two-futures.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Two Futures"></div><div class="card-body"><h3>Two Futures</h3><p>Hotel hope, then the kiln door.</p></div></a>\n'
        '      <a class="card" href="two-daybreaks.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Two Daybreaks"></div><div class="card-body"><h3>Two Daybreaks</h3><p>夜更け and 黎明.</p></div></a>\n'
        '      <a class="card" href="smelting-sequence.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Smelting sequence"></div><div class="card-body"><h3>The smelting sequence</h3><p>125–129 as labor.</p></div></a>\n'
        '      <a class="card" href="boxes-fail.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/hakuri.webp" alt="Boxes"></div><div class="card-body"><h3>Boxes that do not hold</h3><p>Sanso, cell, walking Kura.</p></div></a>\n'
        '      <a class="card" href="closed-eye.html"><div class="card-art p-chihiro"><img loading="lazy" decoding="async" src="../assets/portraits/chihiro.webp" alt="Closed eyes"></div><div class="card-body"><h3>Closed eyes</h3><p>Iai as ethics. Then a draw.</p></div></a>\n'
        '      <a class="card" href="storehouse-religion.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/kyora.webp" alt="Storehouse religion"></div><div class="card-body"><h3>Storehouse as religion</h3><p>Cage, then a building that walks.</p></div></a>\n'
        '      <a class="card" href="customer-vs-bearer.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Customer vs bearer"></div><div class="card-body"><h3>Customer versus bearer</h3><p>Receipt, then nervous system.</p></div></a>\n'
        '      <a class="card" href="seventh-apology.html"><div class="card-art blade-enten"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="Seventh as apology"></div><div class="card-body"><h3>The seventh as apology</h3><p>A bowl, not a trophy.</p></div></a>\n'
        '      <a class="card" href="three-count.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="Three-count"></div><div class="card-body"><h3>The three-count</h3><p>Most blades. Not Magatsumi.</p></div></a>\n'
        '      <a class="card" href="quoted-press.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol11.webp" alt="Quoted press"></div><div class="card-body"><h3>Quoted press</h3><p>Strongest. Sword Master. Heroes.</p></div></a>\n'
        '      <a class="card" href="meal-method.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Meals as method"></div><div class="card-body"><h3>Meals as method</h3><p>Plate before True Realm.</p></div></a>\n'
        '      <a class="card" href="false-death.html"><div class="card-art blade-tobimune"><img loading="lazy" decoding="async" src="../assets/portraits/samura.webp" alt="False death"></div><div class="card-body"><h3>False death as surgery</h3><p>Suzaku. Switch. The look lies.</p></div></a>\n'
        '      <a class="card" href="daughter-cargo.html"><div class="card-art p-iori"><img loading="lazy" decoding="async" src="../assets/portraits/iori.webp" alt="Daughter as cargo"></div><div class="card-body"><h3>Daughter as cargo</h3><p>Seal, shield, last send.</p></div></a>\n'
        '      <a class="card" href="volume-jackets.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Jackets"></div><div class="card-body"><h3>Jackets as arguments</h3><p>Eleven spines and one solicitation.</p></div></a>\n'
        '      <a class="card" href="rest-weeks.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Rest weeks"></div><div class="card-body"><h3>Rest weeks as print</h3><p>A missing magazine is not a title.</p></div></a>\n'
        '      <a class="card" href="color-dark.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Dark power"></div><div class="card-body"><h3>When color goes black</h3><p>Mei Shred. Black Suzaku. Diet.</p></div></a>\n'
        '      <a class="card" href="bowl-hope.html"><div class="card-art blade-enten"><img loading="lazy" decoding="async" src="../assets/fun/enten.png" alt="Bowl as hope"></div><div class="card-body"><h3>Bowl as hope</h3><p>Goldfish, not prophecy.</p></div></a>\n'
        '      <a class="card" href="princess-office.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Princess as office"></div><div class="card-body"><h3>Princess as office</h3><p>Warrant, then someone would trade it.</p></div></a>\n'
        '      <a class="card" href="sword-master-press.html"><div class="card-art p-akemura"><img loading="lazy" decoding="async" src="../assets/portraits/akemura.webp" alt="Sword Master press"></div><div class="card-body"><h3>Sword Master as press name</h3><p>Quotes around a basement man.</p></div></a>\n'
        '      <a class="card" href="named-person-titles.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Named titles"></div><div class="card-body"><h3>Chapters named for people</h3><p>A title that is only a name.</p></div></a>\n'
        '      <a class="card" href="war-as-kiln.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="War as kiln"></div><div class="card-body"><h3>War as kiln</h3><p>Part 2 as labor, not a reel.</p></div></a>\n'
        '      <a class="card" href="part-two-clock.html">',
    )

    patch(
        "guide/index.html",
        '      <a class="card" href="mega-doors.html">',
        '      <a class="card" href="mega-doors.html">',
    )
    patch(
        "guide/index.html",
        '      <a class="card" href="mega-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol2.webp" alt="Mega doors"></div><div class="card-body"><h3>Mega update</h3><p>New rooms this wave, from printed facts.</p></div></a>',
        '      <a class="card" href="mega-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol2.webp" alt="Mega doors"></div><div class="card-body"><h3>Mega update</h3><p>New rooms this wave, from printed facts.</p></div></a>\n'
        '      <a class="card" href="quad-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol5.webp" alt="Quadruple wave"></div><div class="card-body"><h3>Quadruple wave</h3><p>Bonds, fights, volume reads, essays.</p></div></a>\n'
        '      <a class="card" href="after-sojo.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="After Sojo"></div><div class="card-body"><h3>After Sojo</h3><p>The auction is the next building.</p></div></a>\n'
        '      <a class="card" href="after-rakuzaichi.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/uruha.webp" alt="After Rakuzaichi"></div><div class="card-body"><h3>After Rakuzaichi</h3><p>The long book names Uruha.</p></div></a>\n'
        '      <a class="card" href="after-hotel.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/portraits/hiruhiko.webp" alt="After the hotel"></div><div class="card-body"><h3>After the hotel</h3><p>Eyes shut. A basement still to lose.</p></div></a>\n'
        '      <a class="card" href="spoiler-ladder.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Spoiler ladder"></div><div class="card-body"><h3>Spoiler ladder</h3><p>Stop signs you can move.</p></div></a>\n'
        '      <a class="card" href="newcomer-hour.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/hokazono-commemorative.jpg" alt="Newcomer hour"></div><div class="card-body"><h3>Newcomer hour</h3><p>Official door first. Then chapter 1.</p></div></a>\n'
        '      <a class="card" href="official-only.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/viz-social.jpg" alt="Official-only"></div><div class="card-body"><h3>Official-only desk</h3><p>What this archive will not file.</p></div></a>\n'
        '      <a class="card" href="who-dies.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/panels/ch001.png" alt="Who dies"></div><div class="card-body"><h3>Who dies, printed</h3><p>A labeled door onto the graves.</p></div></a>\n'
        '      <a class="card" href="who-holds.html"><div class="card-art blade-enten"><img loading="lazy" decoding="async" src="../assets/panels/enten.webp" alt="Who holds"></div><div class="card-body"><h3>Who holds what</h3><p>Contracts and receipts.</p></div></a>',
    )

    patch(
        "fun/index.html",
        '      <a class="card" href="volume-spines.html">',
        '      <a class="card" href="year-2023.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="2023"></div><div class="card-body"><h3>2023</h3><p>First issue. Meme. Mission.</p></div></a>\n'
        '      <a class="card" href="year-2024.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol2.webp" alt="2024"></div><div class="card-body"><h3>2024</h3><p>Volume 1. Next Manga. Plus views.</p></div></a>\n'
        '      <a class="card" href="year-2025.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol8.webp" alt="2025"></div><div class="card-body"><h3>2025</h3><p>Two million, then three.</p></div></a>\n'
        '      <a class="card" href="year-2026.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol11.webp" alt="2026"></div><div class="card-body"><h3>2026</h3><p>Four million. Kiln. A door.</p></div></a>\n'
        '      <a class="card" href="jump-issue-doors.html"><div class="card-art"><img loading="lazy" decoding="async" src="../assets/covers/jp-vol1.webp" alt="Jump issues"></div><div class="card-body"><h3>Jump issue doors</h3><p>First week, rests, return.</p></div></a>\n'
        '      <a class="card" href="bathhouse-quest-2.html"><div class="card-art p-sojo"><img loading="lazy" decoding="async" src="../assets/portraits/sojo.webp" alt="Bathhouse 2"></div><div class="card-body"><h3>Bathhouse Quest #2</h3><p>The second extra. Buy the book.</p></div></a>\n'
        '      <a class="card" href="volume-spines.html">',
    )

    patch(
        "manga/index.html",
        '       <p><a href="volumes.html">Volume guide</a>',
        '       <p><a href="volume-1-read.html">Reading Volume 1</a> · <a href="volume-11-read.html">Reading Volume 11</a> · <a href="volume-12-read.html">Reading Volume 12</a> · <a href="../arcs/vs-sojo-map.html">Vs. Sojo map</a> · <a href="../arcs/seitei-war-map.html">Seitei War map</a></p>\n'
        '       <p><a href="volumes.html">Volume guide</a>',
    )

    patch(
        "arcs/index.html",
        '       <a class="card" href="seitei-war.html">',
        '       <a class="card" href="vs-sojo-map.html"><div class="card-art blade-kuregumo"><img loading="lazy" decoding="async" src="../assets/panels/ch009.png" alt="Vs. Sojo map"></div><div class="card-body"><span class="tag">Map</span><h3>Vs. Sojo map</h3><p>Titles 1–18 as a commute.</p></div></a>\n'
        '       <a class="card" href="rakuzaichi-map.html"><div class="card-art p-kyora"><img loading="lazy" decoding="async" src="../assets/panels/ch019.png" alt="Rakuzaichi map"></div><div class="card-body"><span class="tag">Map</span><h3>Rakuzaichi map</h3><p>19–46. Listing to punk.</p></div></a>\n'
        '       <a class="card" href="sword-bearer-map.html"><div class="card-art p-samura"><img loading="lazy" decoding="async" src="../assets/panels/ch047.png" alt="Sword Bearer map"></div><div class="card-body"><span class="tag">Map</span><h3>Sword Bearer map</h3><p>47–115. Box to Swordsmith.</p></div></a>\n'
        '       <a class="card" href="seitei-war-map.html"><div class="card-art p-akemura"><img loading="lazy" decoding="async" src="../assets/panels/ch113.png" alt="Seitei War map"></div><div class="card-body"><span class="tag">Map</span><h3>Seitei War map</h3><p>116–131. Table-only 118–120.</p></div></a>\n'
        '       <a class="card" href="seitei-war.html">',
    )

    patch(
        "factions/index.html",
        '    <p>This index is now a door. <a href="kamunabi.html">Kamunabi</a>',
        '    <p>Job lists this wave: <a href="hishaku-jobs.html">Hishaku jobs</a>, <a href="kamunabi-faces.html">Kamunabi faces</a>, <a href="tou-jobs.html">Tou jobs</a>.</p>\n'
        '    <p>This index is now a door. <a href="kamunabi.html">Kamunabi</a>',
    )

    patch(
        "world/index.html",
        '      <nav class="related" aria-label="Related pages"><a href="glossary.html">Glossary</a>',
        '      <p>This wave’s place and fight doors: <a href="battle-index.html">fight desks</a>, <a href="workshop-cellar.html">cellar</a>, <a href="cafe-interior.html">cafe interior</a>, <a href="auction-floor.html">auction floor</a>, <a href="hotel-floors.html">hotel floors</a>, <a href="hq-basement.html">HQ basement</a>.</p>\n'
        '      <nav class="related" aria-label="Related pages"><a href="glossary.html">Glossary</a>',
    )

    # fix who-dies bad link if the page exists
    who = ROOT / "guide/who-dies.html"
    if who.exists():
        t = who.read_text(encoding="utf-8")
        t = t.replace("../world/named-graves.html", "../analysis/named-graves.html")
        who.write_text(t, encoding="utf-8")
        print("fixed who-dies graves link")

    print("wire done")


if __name__ == "__main__":
    main()
