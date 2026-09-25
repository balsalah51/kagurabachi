#!/usr/bin/env python3
"""Second wave of printed-topic rooms for the mega update."""
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("mega_pages", Path("/workspace/tools/mega_pages.py"))
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)

write = mp.write
related = mp.related
VIZ = mp.VIZ


def main():
    extras = [
        ("world/daruma.html", "Exploding Daruma | Norisaku Madoka | Kagurabachi",
         "Madoka’s exploding Daruma: Sojo’s employee, then a man who goes home.",
         "Vs. Sojo · Daruma", "Exploding Daruma", "達磨",
         "Chapter 8 titles his name and a promise.",
         f"""
  <p>Norisaku Madoka’s art is exploding Daruma. He works for Sojo. Chihiro and Shiba beat him. He decides to stop being a sorcerer and go home. Chapter 8 is “Norisaku Madoka: I Will Change.” This page is the toy, not the man.</p>
  <p>Person: <a href="../characters/madoka.html">Madoka</a>. Chapter: <a href="../manga/chapter-8.html">8</a>. Customer: <a href="../characters/sojo.html">Sojo</a>. Official: {VIZ}.</p>
    {related([("../characters/madoka.html", "Madoka"), ("../manga/chapter-8.html", "Ch. 8"), ("../arcs/vs-sojo.html", "Vs. Sojo"), ("../characters/sojo.html", "Sojo")])}
"""),
        ("world/puppet-armor.html", "Hokuto’s Puppet Armor | Kagurabachi",
         "Hokuto’s puppet armor: Ibuki’s killer, Volume 10 jacket, Hishaku.",
         "Hishaku · Hokuto", "Puppet armor", "北兜",
         "The man who opened Cloud Gouger’s contract.",
         f"""
  <p>Hokuto’s printed art is puppet armor. He kills Ibuki Misaka. The Lifelong Contract on Cloud Gouger opens. The Hishaku sell the sword to Sojo, a customer. Volume 10’s jacket puts Hokuto with Natsuki, Uruha, and Yura.</p>
  <p>Person: <a href="../characters/hokuto.html">Hokuto</a>. Ibuki: <a href="../characters/ibuki.html">Ibuki</a>. Org: <a href="../factions/hishaku.html">Hishaku</a>.</p>
    {related([("../characters/hokuto.html", "Hokuto"), ("../characters/ibuki.html", "Ibuki"), ("../blades/cloud-gouger.html", "Cloud Gouger"), ("../manga/volume-10.html", "Volume 10")])}
"""),
        ("world/uran-ice.html", "Uran’s Ice | Hishaku | Kagurabachi",
         "Uran’s ice: breath that freezes. Named Hishaku. Present at the workshop raid.",
         "Hishaku · 右嵐", "Uran’s ice", "右嵐",
         "A raid art. Not Cloud Gouger’s Yui.",
         f"""
  <p>Uran (右嵐) is named Hishaku. Ice. Breath that freezes. The register puts her on the raid that killed Kunishige. This is not Yui. Yui is Cloud Gouger’s ice cages. Uran is a person.</p>
  <p>Person: <a href="../characters/uran.html">Uran</a>. Yui: <a href="yui.html">Yui</a>. Raid: <a href="raid.html">the raid</a>.</p>
    {related([("../characters/uran.html", "Uran"), ("yui.html", "Yui"), ("raid.html", "Raid"), ("../factions/hishaku.html", "Hishaku")])}
"""),
        ("world/blood-track.html", "Toto’s Blood Tracking | Hishaku | Kagurabachi",
         "Toto’s blood tracking and fire-gate as habit. Iori job. Sengoku’s head as a sample.",
         "Hishaku · 斗斗", "Blood tracking", "斗斗",
         "A habit, a job, a sample.",
         f"""
  <p>Toto (斗斗) is named Hishaku. Blood tracking. Fire-gate as habit. The Iori job. Sengoku’s head as a sample. Two of the ten remain unnamed. This page files the tracking so it is not only a register line.</p>
  <p>Person: <a href="../characters/toto.html">Toto</a>. Gate: <a href="fire-gate.html">fire-gate</a>. Hotel teacher: <a href="../characters/sengoku.html">Sengoku</a>.</p>
    {related([("../characters/toto.html", "Toto"), ("fire-gate.html", "Fire-gate"), ("../factions/hishaku.html", "Hishaku"), ("../characters/iori.html", "Iori")])}
"""),
        ("world/five-shaku.html", "Kiri’s Five-Shaku Blade | Kagurabachi",
         "Kiri Shirakai’s two-meter odachi, five-shaku blade, chapter 90, vow to decapitate Itsuo.",
         "Shirakai · 斬", "Five-shaku blade", "五尺",
         "A curriculum that told her women cannot.",
         f"""
  <p>Kiri Shirakai (白廻 斬) carries a two-meter odachi, a five-shaku blade, into a school that said women cannot. Chapter 90 titles her. Granddaughter of Itsuo. Vow to decapitate him. Squadron leader. The Iai house is larger than Samura.</p>
  <p>Person: <a href="../characters/kiri.html">Kiri</a>. Chapter: <a href="../manga/chapter-90.html">90</a>. School: <a href="iai.html">Iai</a>. Itsuo: <a href="../characters/itsuo.html">Itsuo</a>.</p>
    {related([("../characters/kiri.html", "Kiri"), ("../manga/chapter-90.html", "Ch. 90"), ("iai.html", "Iai"), ("../characters/itsuo.html", "Itsuo")])}
"""),
        ("world/misaka-brothers.html", "The Misaka Brothers | Ibuki and Natsuki | Kagurabachi",
         "Ibuki held Cloud Gouger. Natsuki holds Lightning Menace. One contract, one rhyme.",
         "Bearers · 巳坂", "The Misaka brothers", "巳坂",
         "Wartime steel and a Kamunabi voltage.",
         f"""
  <p>Ibuki Misaka carried Cloud Gouger through the Seitei War. Hokuto killed him. The contract opened. Natsuki Misaka is the brother: Lightning Menace, squadron leader, Kumeyuri candidate, Volume 10 jacket. The family rhyme without Datenseki.</p>
  <p>Files: <a href="../characters/ibuki.html">Ibuki</a>, <a href="../characters/natsuki.html">Natsuki</a>, <a href="lightning-menace.html">Raiku</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
    {related([("../characters/ibuki.html", "Ibuki"), ("../characters/natsuki.html", "Natsuki"), ("lightning-menace.html", "Raiku"), ("../manga/chapter-91.html", "Ch. 91")])}
"""),
        ("world/kagari-clan.html", "The Kagari Heredity | Flame Bone | Kagurabachi",
         "Flame Bone of the Starving is a Kagari hereditary. Hiyuki wears a license to work.",
         "Kamunabi · Kagari", "The Kagari heredity", "Kagari",
         "A skeleton you inherit, then ask permission to spend.",
         f"""
  <p>Flame Bone of the Starving is a Kagari hereditary. Hiyuki Kagari wears pieces of a giant flaming skeleton. The Kamunabi license how much: ribs, torso, a line. The text will stand it next to an Enchanted Blade. This page is the family word, not the fight.</p>
  <p>Art: <a href="flame-bone.html">Flame Bone</a>. Person: <a href="../characters/hiyuki.html">Hiyuki</a>. Essay: <a href="../analysis/flame-bone.html">essay</a>.</p>
    {related([("flame-bone.html", "Flame Bone"), ("../characters/hiyuki.html", "Hiyuki"), ("../analysis/flame-bone.html", "Essay"), ("../factions/kamunabi.html", "Kamunabi")])}
"""),
        ("world/april-first.html", "April 1 Noon | Irishima’s Beach | Kagurabachi",
         "April 1 noon, Irishima’s beach: the handover clock printed in chapter 130.",
         "Part 2 · 4/1", "April 1 noon", "四月一日",
         "Three days from the shop’s March 29 clock.",
         f"""
  <p>Chapter 130 prints the beach: April 1, noon, Irishima. Japan has accepted a Mikaboshi demand to hand Chiaki over. The shop’s clock is March 29. Three days. The <a href="handover.html">handover letter</a> is the paper. This page is the date.</p>
  <p>Chapter: <a href="../manga/chapter-130.html">130</a>. Princess: <a href="princess.html">Chiaki</a>. Island: <a href="irishima.html">Irishima</a>. We do not invent chapter 132’s beach.</p>
    {related([("handover.html", "Handover"), ("../manga/chapter-130.html", "Ch. 130"), ("three-day-beach.html", "Three days"), ("irishima.html", "Irishima")])}
"""),
        ("world/march-twenty-nine.html", "March 29 | The Shop Clock | Kagurabachi",
         "March 29 is the shop clock in chapter 130. The beach is April 1.",
         "Part 2 · kiln", "March 29", "三月二十九日",
         "The furnace and the calendar in the same room.",
         f"""
  <p>Chapter 130’s shop is dated March 29. Tamahagane comes out of a collapsed furnace. Subaru says it will make a terrifying sword. The beach is April 1, three days later. This page files the shop date so the kiln is not only a mineral page.</p>
  <p><a href="smelting.html">Smelting</a>. <a href="tamahagane.html">Tamahagane</a>. <a href="../manga/chapter-130.html">I'm Fine!</a>.</p>
    {related([("april-first.html", "April 1"), ("smelting.html", "Smelting"), ("../characters/subaru.html", "Subaru"), ("../manga/chapter-130.html", "Ch. 130")])}
"""),
        ("world/three-day-beach.html", "Three Days | Shop to Beach | Kagurabachi",
         "Three days between the shop’s March 29 and Irishima’s April 1 noon.",
         "Part 2 · clock", "Three days", "三日",
         "A reunion title and a treaty date.",
         f"""
  <p>The present-tense calendar on this site already tracks October and November. Part 2 adds a tighter clock: March 29 in the shop, April 1 noon on Irishima’s beach, three days. Chapter 130’s title tries to keep the reunion small. The date does not.</p>
  <p><a href="present.html">Present tense</a>. <a href="april-first.html">April 1</a>. <a href="../manga/chapter-130.html">130</a>.</p>
    {related([("march-twenty-nine.html", "March 29"), ("april-first.html", "April 1"), ("present.html", "Present"), ("../manga/part-2.html", "Part 2")])}
"""),
        ("world/extension-kit.html", "Blade Extensions | Shred, Cloak, External | Kagurabachi",
         "Printed extensions: Kuro: Shred, Mei: Shred, cloaked Mei, External Crow, External Suzaku, Nishiki: Support, Destructive Play, Black Suzaku.",
         "Catalog · extensions", "Blade extensions", "派生",
         "The same names, spent harder.",
         f"""
  <p>The catalog already lists extensions as spends, not new swords. <a href="kuro-shred.html">Kuro: Shred</a>. <a href="mei-shred.html">Mei: Shred</a>. <a href="cloaked-mei.html">Cloaked Mei</a> (unofficial phrase). <a href="nishiki-support.html">Nishiki: Support</a>. <a href="external-crow.html">External Crow</a>. <a href="external-suzaku.html">External Suzaku</a>. <a href="black-suzaku.html">Black Suzaku</a>. <a href="destructive-play.html">Destructive Play</a>.</p>
  <p>Parent catalog: <a href="techniques.html">techniques</a>. Index: <a href="technique-index.html">rows</a>.</p>
    {related([("techniques.html", "Catalog"), ("kuro-shred.html", "Kuro: Shred"), ("mei-shred.html", "Mei: Shred"), ("dark-power.html", "Dark power")])}
"""),
        ("factions/mikaboshi.html", "The Mikaboshi | Irishima | Kagurabachi",
         "Mikaboshi: the island nation that rose, Datenseki as architecture, talks 117–121.",
         "Seitei War · 箕加星", "Mikaboshi", "箕加星",
         "Irishima and a foothold. Datenseki as a body.",
         f"""
  <p>The Mikaboshi are the old island kings coming back for Datenseki. Ariu, crown prince, insect sorcery (Sumika), a body that can live with the stone. Japan wants the vein. They want Irishima and a foothold. Undersea habitat is Datenseki as architecture. Two Hishaku are still unnamed; this faction is not them.</p>
  <p>Island: <a href="../world/irishima.html">Irishima</a>. Talks: <a href="../world/irishima-talks.html">117–121</a>. Habitat: <a href="../world/undersea.html">undersea</a>. Ariu: <a href="../characters/ariu.html">Ariu</a>.</p>
    {related([("../world/irishima.html", "Irishima"), ("../world/irishima-talks.html", "Talks"), ("../characters/ariu.html", "Ariu"), ("../world/sumika.html", "Sumika")])}
"""),
        ("analysis/equal-jacket.html", "Equal as a Jacket | Kagurabachi Essay",
         "Volume 4 titles Equal. The jacket is two figures at storehouse dusk. Hakuri is the brief.",
         "Essay · Volume 4", "Equal as a jacket", "対等",
         "They meet in the middle. The clan never granted it.",
         f"""
  <p>Volume 4’s title is <em>Equal</em>. The jacket is two figures at storehouse dusk. Hakuri was beaten into believing he had no talent. Chihiro does not pick him up as a tool. Chapter 37 titles the weekly word. The spine keeps it.</p>
  <p><a href="../manga/volume-4.html">Volume 4</a>. <a href="../manga/chapter-37.html">Chapter 37</a>. <a href="hakuri.html">Hakuri essay</a>.</p>
    {related([("../manga/volume-4.html", "Volume 4"), ("../characters/hakuri.html", "Hakuri"), ("hakuri.html", "Essay"), ("../world/storehouse.html", "Storehouse")])}
"""),
        ("analysis/sojo-customer.html", "Sojo, Customer | Kagurabachi Essay",
         "Sojo bought Cloud Gouger. He is not Hishaku. The register already says so. This essay files the mistake people search.",
         "Essay · underworld", "A customer, not a member", "客",
         "The Hishaku sold a sword. He paid.",
         f"""
  <p>Yura’s people had the six wartime blades. Hokuto killed Ibuki. They sold Cloud Gouger to Genichi Sojo in early October. Customer, not a member. The ten are eight named and two unnamed. Sojo is the weather in Volume 2, then a crater, then a dying contract in Chihiro’s bag.</p>
  <p><a href="../characters/sojo.html">Sojo</a>. <a href="sojo-fan.html">worst fan</a>. <a href="../factions/hishaku.html">Hishaku</a>.</p>
    {related([("../characters/sojo.html", "Sojo"), ("sojo-fan.html", "Fan essay"), ("../factions/hishaku.html", "Hishaku"), ("../blades/cloud-gouger.html", "Cloud Gouger")])}
"""),
        ("analysis/workshop-kitchen.html", "The Workshop Was a Kitchen | Kagurabachi Essay",
         "Before True Realm, the book titles meals. The cellar held swords. The table held a bowl.",
         "Essay · house", "The workshop was a kitchen", "台所",
         "Goldfish won because the house had to stay visible.",
         f"""
  <p>Hokazono almost used koi. Goldfish won because the bowl recorded who the fish liked more. Chapter 5 titles a good meal. The raid empties a house that cooked. Enten manifests the household. Magatsumi manifests a national sin. The kitchen is the argument.</p>
  <p><a href="../fun/bowl.html">Bowl</a>. <a href="../fun/goldfish.html">Goldfish</a>. <a href="meals.html">Meals essay</a>.</p>
    {related([("meals.html", "Meals"), ("../world/workshop.html", "Workshop"), ("../fun/bowl.html", "Bowl"), ("../world/food.html", "Food")])}
"""),
        ("analysis/part-two-clock.html", "Part 2’s Clock | Kagurabachi Essay",
         "March 29, April 1, three days. The war book counts workshop hours, not press conferences.",
         "Essay · Part 2", "Part 2’s clock", "時計",
         "The kiln and the beach share one week.",
         f"""
  <p>Part 1’s present tense is October into November. Part 2 adds a shop date and a treaty date three days apart. Chapter 130 holds both. Chapter 131 is Tipping Point. Chapter 132 is not printed on this desk yet. The useful YouTube caution still stands: twenty to forty chapters of ground.</p>
  <p><a href="../manga/part-2.html">Part 2</a>. <a href="../world/three-day-beach.html">Three days</a>. <a href="../guide/part-2.html">Forge door</a>.</p>
    {related([("../manga/part-2.html", "Part 2"), ("../world/march-twenty-nine.html", "March 29"), ("../manga/chapter-131.html", "Ch. 131"), ("../world/timeline.html", "Timeline")])}
"""),
        ("fun/first-issue.html", "Jump 2023 Issue 42 | Kagurabachi’s First Week",
         "Chapter 1, Mission, Weekly Shōnen Jump 2023 #42, 19 September. Most-viewed new title on MANGA Plus that week.",
         "Fun · debut", "The first issue", "2023#42",
         "19 September 2023. Mission. The shop, then the raid.",
         f"""
  <p>Chapter 1, “Mission” (すべきこと), ran in Weekly Shōnen Jump 2023 issue 42 on 19 September. VIZ and MANGA Plus carried the English the same week. It was the most-viewed new title on MANGA Plus in its first week. Volume 1, 2 February 2024, takes that title.</p>
  <p>Close reading: <a href="../manga/chapter-1.html">Mission</a>. Volume: <a href="../manga/volume-1.html">1</a>. Series: <a href="../guide/series.html">the series</a>.</p>
    {related([("../manga/chapter-1.html", "Ch. 1"), ("../manga/volume-1.html", "Volume 1"), ("../guide/series.html", "Series"), ("../manga/publication.html", "Publication")])}
"""),
        ("guide/volume-map.html", "Kagurabachi Volume Map | 1–12",
         "Eleven jackets and one solicited close, each with a room. Chapter ranges, ISBNs, jacket faces.",
         "Guide · spines", "Volume map", "巻",
         "The commute by tankōbon.",
         f"""
  <p>Volume 1 holds 1–8. Volume 2 holds 9–18. 3–5 are the auction. 6–11 are the long book through Transformation. Volume 12 is solicited 4 September 2026. Each of 1–11 now has a room; 12 already did.</p>
  <p>Doors: <a href="../manga/volume-1.html">1</a> · <a href="../manga/volume-5.html">5</a> · <a href="../manga/volume-11.html">11</a> · <a href="../manga/volume-12.html">12</a>. Table: <a href="../manga/volumes.html">ISBN guide</a>.</p>
    {related([("../manga/volumes.html", "ISBN table"), ("../fun/volume-spines.html", "Spines"), ("../manga/synopses.html", "Synopses"), ("reading-order.html", "Reading order")])}
"""),
        ("manga/chapter-doors.html", "Kagurabachi Chapter Rooms | Every Linked Weekly Title",
         "A directory of chapter rooms on this encyclopedia, including the leftover titles from the mega update.",
         "Manga · doors", "Chapter rooms", "話部屋",
         "Not every Sunday has a close reading. Every leftover title now has a door.",
         f"""
  <p>The <a href="chapters.html">chapter index</a> is the title authority. This page is the room list. 118–120 stay in the table only. Chapter 131 is <a href="chapter-131.html">Tipping Point</a>. Official chapters: {VIZ}.</p>
  <p>Beginner map: <a href="../guide/chapter-map.html">chapter map</a>. Part 2: <a href="part-2.html">the forge</a>.</p>
    {related([("chapters.html", "Index"), ("../guide/chapter-map.html", "Map"), ("chapter-1.html", "Ch. 1"), ("chapter-131.html", "Ch. 131")])}
"""),
        ("world/quoted-headlines.html", "Strongest, Sword Master, Heroes | Kagurabachi Headlines",
         "Three weekly titles the index keeps in quotes: the press words Volume 11 argues with.",
         "Volume 11 · quotes", "Quoted headlines", "見出し",
         "The book is arguing with a headline.",
         f"""
  <p>“Strongest.” “Sword Master.” “Heroes.” The chapter index keeps the quotation marks. Volume 11 wears Heroes on snow. The Kamunabi printed those words on Sword Bearers after Malediction. The weekly pages put them in quotes and keep cutting.</p>
  <p>Essay: <a href="../analysis/quotation-marks.html">quotes</a>. Rooms: <a href="../manga/chapter-99.html">99</a>, <a href="../manga/chapter-100.html">100</a>, <a href="../manga/chapter-104.html">104</a>.</p>
    {related([("../analysis/quotation-marks.html", "Essay"), ("../manga/volume-11.html", "Volume 11"), ("malediction.html", "Malediction"), ("../manga/chapter-104.html", "Heroes")])}
"""),
    ]
    for rel, title, desc, kicker, h1, jp, lede, body in extras:
        folder = "World"
        if rel.startswith("analysis/"):
            folder = "Essays"
        elif rel.startswith("fun/"):
            folder = "Fun"
        elif rel.startswith("guide/"):
            folder = "Guide"
        elif rel.startswith("factions/"):
            folder = "Factions"
        elif rel.startswith("manga/"):
            folder = "Manga"
        write(
            rel, title, desc,
            f'<a href="../index.html">Archive</a> / <a href="index.html">{folder}</a> / {h1}',
            kicker, h1, jp, lede, body,
        )
    print("more", len(extras))


if __name__ == "__main__":
    main()
