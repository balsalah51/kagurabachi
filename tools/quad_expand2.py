#!/usr/bin/env python3
"""Second deepen pass: unique longer addenda on character, blade, and world hubs."""
from pathlib import Path

ROOT = Path("/workspace")
MARK = "<!-- quad-wave-2 -->"

BLOCKS = {
    "characters/azami.html": """
    <h2>The friend who stayed</h2>
    <p>Azami’s printed job is political capital spent inside a bureau that later leaks. He hid Kunishige after the Malediction with Shiba, then stayed when Shiba left. He warned Chihiro off Sojo. The first book proves the warning and ignores it. The Rakuzaichi deal, Magatsumi to the state, imagines his kind of director. Kasen is the director the deal actually gets. Pair rooms: <a href="azami-and-kunishige.html">Azami and Kunishige</a>, <a href="chihiro-and-azami.html">Chihiro and Azami</a>. Faces: <a href="../factions/kamunabi-faces.html">Kamunabi faces</a>.</p>
    <p>Kudo dies in the building Azami stayed to influence. Hiyuki is the pointed end that still has to live with both directors. Ichiki trained him and Shiba. The leadership table is a room, not a moveset. This file is the man who wanted blades sealed and still could not stop a mailing address.</p>
""",
    "characters/uruha.html": """
    <h2>Name loyalty, then surgery</h2>
    <p>Chapter 47 titles him. The Sanso fails. Steam Squad dies. Senkutsuji looks like a pact and is Suzaku. Switch is the receipt. Ro recovers Kumeyuri. Play, when he held it, is the respectful argument Hiruhiko later spends as contempt. Pairs: <a href="chihiro-and-uruha.html">Chihiro</a>, <a href="uruha-and-samura.html">Samura</a>. Desks: <a href="../world/battle-sanso.html">Sanso</a>, <a href="../world/battle-senkutsuji.html">temple</a>. Essay: <a href="../analysis/false-death.html">false death</a>.</p>
""",
    "characters/hiruhiko.html": """
    <h2>Loud job in the ten</h2>
    <p>Eighteen. Blood Crane. Play. Sanso hit. Hotel demolition. Banquet as architecture. He is not the mind. Yura is. Pair: <a href="yura-and-hiruhiko.html">Yura and Hiruhiko</a>, <a href="chihiro-and-hiruhiko.html">Chihiro</a>. Desks: <a href="../world/battle-sanso.html">Sanso</a>, <a href="../world/battle-hotel-play.html">Play</a>. Jobs: <a href="../factions/hishaku-jobs.html">Hishaku jobs</a>.</p>
""",
    "characters/hokuto.html": """
    <h2>Opened weather</h2>
    <p>He murdered Ibuki so Cloud Gouger’s contract opened. He wants a real fight. Volume 10 puts him on a jacket with Natsuki. Pairs: <a href="ibuki-and-hokuto.html">Ibuki</a>, <a href="hokuto-and-natsuki.html">Natsuki</a>. Register: <a href="../analysis/customer-vs-bearer.html">customer versus bearer</a>.</p>
""",
    "characters/kuguri.html": """
    <h2>Unwilling syllabus</h2>
    <p>Twilight Wave. Unrequited blade. Chapter 69 is his face title. Chihiro copies Iai off him. Pair: <a href="chihiro-and-kuguri.html">the classroom pair</a>. Desk: <a href="../world/battle-hotel-iai.html">hotel Iai</a>. Essay: <a href="../analysis/copy.html">copy</a>.</p>
""",
    "characters/natsuki.html": """
    <h2>The rhyme without the mineral</h2>
    <p>Chapter 91 titles him. Lightning Menace is voltage in the body, not Mei. He never held Cloud Gouger. Volume 10’s cloth is cruel on purpose. Pairs: <a href="ibuki-and-natsuki.html">Ibuki</a>, <a href="hokuto-and-natsuki.html">Hokuto</a>. Kit: <a href="../world/lightning-menace.html">Lightning Menace</a>.</p>
""",
    "characters/iori.html": """
    <h2>Cargo, then choice</h2>
    <p>Chapter 62 names her. Car Chase is 63. Ikura breaks the seal. Black Suzaku sends Tobimune. Pairs: <a href="samura-and-iori.html">Samura</a>, <a href="chihiro-and-iori.html">Chihiro</a>, <a href="ro-and-iori.html">Ro</a>. Essay: <a href="../analysis/daughter-cargo.html">daughter as cargo</a>.</p>
""",
    "characters/kyora.html": """
    <h2>Eleventh head</h2>
    <p>Two centuries of auction. Storehouse as environmental control. He looks through Shinuchi and sees the Sword Master. Pair: <a href="hakuri-and-kyora.html">Hakuri</a>. Desk: <a href="../world/battle-rakuzaichi.html">208th</a>. Essay: <a href="../analysis/storehouse-religion.html">religion</a>.</p>
""",
    "characters/tenri.html": """
    <h2>Mineral grave</h2>
    <p>Short blades. Datenseki pop. Sojo already died this way. Pair: <a href="hakuri-and-tenri.html">Hakuri</a>. Desk: <a href="../world/battle-tenri.html">the stone</a>. Mineral: <a href="../world/datenseki.html">Datenseki</a>.</p>
""",
    "characters/soya.html": """
    <h2>Heir, then blank</h2>
    <p>Household Isou. Amnesia after the firm. The extra asks for memories gone. Pair: <a href="hakuri-and-soya.html">Hakuri</a>. Fight: <a href="../world/battle-hakuri-soya.html">the clash</a>. Extra: <a href="../fun/soya-memories.html">Memories, Begone!</a>.</p>
""",
    "characters/char.html": """
    <h2>Last Kyonagi</h2>
    <p>Witness. Regeneration as a shopping list Sojo failed to cash. Birthday 21 December. Pairs: <a href="chihiro-and-char.html">Chihiro</a>, <a href="sojo-and-char.html">Sojo</a>. Clan: <a href="../factions/kyonagi.html">Kyonagi</a>.</p>
""",
    "characters/hinao.html": """
    <h2>The chair</h2>
    <p>Cafe Haru Haru. Broker. Civilian hour. Pair: <a href="hinao-and-shiba.html">Shiba</a>. Place: <a href="../world/cafe-interior.html">interior</a>.</p>
""",
    "characters/tafuku.html": """
    <h2>The referee</h2>
    <p>Duel domain. Two people, one match, then the street. Pair: <a href="hiyuki-and-tafuku.html">Hiyuki</a>. Kit: <a href="../world/duel-domain.html">domain</a>.</p>
""",
    "characters/kudo.html": """
    <h2>Warrior’s Path</h2>
    <p>Dies for Hakuri so the walking Kura leaves HQ week. Pair: <a href="hakuri-and-kudo.html">Hakuri</a>. Desk: <a href="../world/battle-hq.html">HQ</a>.</p>
""",
    "characters/kasen.html": """
    <h2>Stationery</h2>
    <p>A director who thinks order lives in Magatsumi. The leak is mail. Pair: <a href="yura-and-kasen.html">Yura</a>. Essay: <a href="../analysis/leak.html">the leak</a>.</p>
""",
    "characters/akemura.html": """
    <h2>Master key</h2>
    <p>Sword Master is a press name. Magatsumi is a knot. Yura offers a body. Pair: <a href="yura-and-akemura.html">Yura</a>. Essay: <a href="../analysis/sword-master-press.html">press name</a>. Fight: <a href="../world/battle-enten-magatsumi.html">Enten vs Magatsumi</a>.</p>
""",
    "characters/subaru.html": """
    <h2>Colleague</h2>
    <p>Sushi first. Duplication. Relocated when boxes fail. Pair: <a href="subaru-and-kunishige.html">Kunishige</a>. Kit: <a href="../world/subaru-duplication.html">duplication</a>.</p>
""",
    "characters/giyu.html": """
    <h2>Would trade the office</h2>
    <p>The clan is not a chorus. Pair: <a href="chiaki-and-giyu.html">Chiaki</a>. Essay: <a href="../analysis/princess-office.html">princess as office</a>.</p>
""",
    "characters/mashiro.html": """
    <h2>The partner who said no</h2>
    <p>Opposed to stealing ore for a civilian. Alive in the talks. Pair: <a href="mashiro-and-shiba.html">Shiba</a>.</p>
""",
    "characters/kiri.html": """
    <h2>Odachi anyway</h2>
    <p>Chapter 90. The founder said no. She escorts Hakuri. Pair: <a href="kiri-and-itsuo.html">Itsuo</a>.</p>
""",
    "characters/itsuo.html": """
    <h2>Founder, mountain, bigot</h2>
    <p>The curriculum works. The rule does not get washed. Pair: <a href="kiri-and-itsuo.html">Kiri</a>. School: <a href="../world/iai.html">Iai</a>.</p>
""",
    "characters/toto.html": """
    <h2>Trail and gate</h2>
    <p>Blood track. Fire-gate. Sengoku’s head. Pair: <a href="toto-and-sengoku.html">Sengoku</a>. Jobs: <a href="../factions/hishaku-jobs.html">the ten</a>.</p>
""",
    "characters/yukisada.html": """
    <h2>Seventeen, a building</h2>
    <p>Vessel. Will not stay dead from decapitation. Desk: <a href="../world/battle-hq.html">HQ week</a>. Kit: <a href="../world/vessel.html">Vessel</a>.</p>
""",
    "characters/sengoku.html": """
    <h2>Reigen house</h2>
    <p>The hotel’s owner becomes a trail. Pair: <a href="toto-and-sengoku.html">Toto</a>. Place: <a href="../world/hotel-floors.html">floors</a>.</p>
""",
    "characters/ro.html": """
    <h2>Child-look recovery</h2>
    <p>Recovers Kumeyuri after surgery. Pair: <a href="ro-and-iori.html">Iori</a>. Clan: <a href="../factions/masumi.html">Masumi</a>.</p>
""",
    "blades/enten.html": """
    <h2>This wave’s Enten doors</h2>
    <p>True Realm is Magatsumi’s death. The seventh is an apology. Fights: <a href="../world/battle-enten-tobimune.html">vs Tobimune</a>, <a href="../world/battle-enten-magatsumi.html">vs Magatsumi</a>. Essays: <a href="../analysis/seventh-apology.html">apology</a>, <a href="../analysis/enten-purpose.html">purpose</a>, <a href="../analysis/bowl-hope.html">bowl</a>. Volume 9’s spine agrees.</p>
""",
    "blades/cloud-gouger.html": """
    <h2>Register, again</h2>
    <p>Ibuki, then opened contract, then Sojo the customer, then Chihiro’s dying charges. Not Natsuki. Fight: <a href="../world/battle-chihiro-sojo.html">vs Sojo</a>. Essay: <a href="../analysis/customer-vs-bearer.html">customer versus bearer</a>. Brothers: <a href="../world/misaka-brothers.html">Misaka</a>.</p>
""",
    "blades/magatsumi.html": """
    <h2>Diet, not a three-count</h2>
    <p>Insect kit plus Malediction (蠱). Fights: <a href="../world/battle-enten-magatsumi.html">Enten</a>, <a href="../world/battle-tobimune-magatsumi.html">Tobimune</a>. Essays: <a href="../analysis/three-count.html">three-count</a>, <a href="../analysis/sword-master-press.html">press name</a>, <a href="../analysis/malediction.html">Malediction</a>.</p>
""",
    "blades/tobimune.html": """
    <h2>Support brief</h2>
    <p>Owl, Crow, Suzaku. Given so someone would keep people alive. Fights: <a href="../world/battle-enten-tobimune.html">vs Enten</a>, <a href="../world/battle-tobimune-magatsumi.html">vs Magatsumi</a>, <a href="../world/battle-senkutsuji.html">temple</a>. Essay: <a href="../analysis/owl.html">Owl</a>.</p>
""",
    "blades/kumeyuri.html": """
    <h2>Respect or contempt</h2>
    <p>Play, Banquet. Uruha’s version versus Hiruhiko’s hotel. Desk: <a href="../world/battle-hotel-play.html">Play</a>. Essay: <a href="../analysis/play.html">Play</a>. Surgery: <a href="../analysis/false-death.html">false death</a>.</p>
""",
    "arcs/vs-sojo.html": """
    <h2>Map and after</h2>
    <p><a href="vs-sojo-map.html">Chapter map 1–18</a>. <a href="../guide/after-sojo.html">After Sojo</a>. <a href="../world/battle-chihiro-sojo.html">Fight desk</a>. <a href="../world/battle-acg.html">ACG</a>. Sojo remains a customer.</p>
""",
    "arcs/rakuzaichi.html": """
    <h2>Map and after</h2>
    <p><a href="rakuzaichi-map.html">Chapter map 19–46</a>. <a href="../guide/after-rakuzaichi.html">After the auction</a>. <a href="../world/battle-rakuzaichi.html">Fight desk</a>. <a href="../analysis/storehouse-religion.html">Religion</a>.</p>
""",
    "arcs/sword-bearer.html": """
    <h2>Map and hotel door</h2>
    <p><a href="sword-bearer-map.html">Chapter map 47–115</a>. <a href="../guide/after-hotel.html">After the hotel</a>. <a href="../world/battle-index.html">Fight desks</a>. <a href="../analysis/quoted-press.html">Quoted press</a>.</p>
""",
    "arcs/seitei-war.html": """
    <h2>Map and kiln</h2>
    <p><a href="seitei-war-map.html">Chapter map 116–131</a>. 118–120 table-only. <a href="../analysis/smelting-sequence.html">Smelting sequence</a>. <a href="../analysis/war-as-kiln.html">War as kiln</a>. Chapter 132 stays a door.</p>
""",
    "world/workshop.html": """
    <h2>Cellar satellite</h2>
    <p>The downstairs failure now has <a href="workshop-cellar.html">its own room</a>. Raid desk: <a href="battle-raid.html">the raid fight</a>. Household pair: <a href="../characters/chihiro-and-kunishige.html">father and son</a>.</p>
""",
    "world/cafe.html": """
    <h2>Interior satellite</h2>
    <p><a href="cafe-interior.html">Cafe interior</a>. Pair: <a href="../characters/hinao-and-shiba.html">Hinao and Shiba</a>. Meals: <a href="../analysis/meal-method.html">method</a>.</p>
""",
    "world/hotel.html": """
    <h2>Floors and desks</h2>
    <p><a href="hotel-floors.html">Floors</a>. <a href="battle-hotel-iai.html">Classroom</a>. <a href="battle-hotel-play.html">Play</a>. <a href="../guide/after-hotel.html">After</a>.</p>
""",
    "world/hq.html": """
    <h2>Basement satellite</h2>
    <p><a href="hq-basement.html">Basement</a>. <a href="battle-hq.html">HQ week</a>. <a href="../analysis/boxes-fail.html">Boxes</a>.</p>
""",
    "world/storehouse.html": """
    <h2>Religion and walk</h2>
    <p><a href="../analysis/storehouse-religion.html">Religion essay</a>. <a href="auction-floor.html">Auction floor</a>. <a href="../characters/hakuri-and-kyora.html">Hakuri and Kyora</a>.</p>
""",
    "world/iai.html": """
    <h2>Closed lids</h2>
    <p><a href="../analysis/closed-eye.html">Closed eyes</a>. <a href="../analysis/copy.html">Copy</a>. <a href="battle-hotel-iai.html">Classroom</a>.</p>
""",
    "manga/part-2.html": """
    <h2>Kiln doors this wave</h2>
    <p><a href="../arcs/seitei-war-map.html">Seitei War map</a>. <a href="../analysis/smelting-sequence.html">Smelting sequence</a>. <a href="../analysis/war-as-kiln.html">War as kiln</a>. <a href="../world/irishima-table.html">Talks table</a>. Chapter 132 remains untitled here.</p>
""",
    "guide/reading-order.html": """
    <h2>Stop signs</h2>
    <p>Use <a href="spoiler-ladder.html">the spoiler ladder</a> if you are mid-book. <a href="newcomer-hour.html">Newcomer hour</a> if you have not opened chapter 1. <a href="official-only.html">Official-only desk</a> for what this archive will not invent. After each movement: <a href="after-sojo.html">Sojo</a>, <a href="after-rakuzaichi.html">auction</a>, <a href="after-hotel.html">hotel</a>.</p>
""",
    "fun/hokazono.html": """
    <h2>Year rooms</h2>
    <p>Publication by year: <a href="year-2023.html">2023</a>, <a href="year-2024.html">2024</a>, <a href="year-2025.html">2025</a>, <a href="year-2026.html">2026</a>. Rests: <a href="../analysis/rest-weeks.html">rest weeks as print</a>.</p>
""",
}


def insert(rel, html):
    path = ROOT / rel
    if not path.exists():
        print("missing", rel)
        return False
    text = path.read_text(encoding="utf-8")
    if MARK in text:
        return False
    if "</article>" not in text:
        # some indexes wrap differently; append before footer
        if '<div id="site-footer">' in text:
            text = text.replace('<div id="site-footer">', f'<article class="article">{html}</article>\n  <div id="site-footer">', 1)
            path.write_text(text, encoding="utf-8")
            print("appended", rel)
            return True
        print("no anchor", rel)
        return False
    text = text.replace("</article>", f"{MARK}\n{html}\n    </article>", 1)
    path.write_text(text, encoding="utf-8")
    print("expanded", rel)
    return True


def main():
    n = 0
    for rel, html in BLOCKS.items():
        if insert(rel, html):
            n += 1
    print("expand2", n)


if __name__ == "__main__":
    main()
