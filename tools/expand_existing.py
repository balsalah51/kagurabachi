#!/usr/bin/env python3
"""Insert unique 2026-scrape addenda into existing encyclopedia pages. No em-dashes."""
from pathlib import Path

ROOT = Path("/workspace")

ADDENDA = {
    "characters/chihiro.html": """
    <h2>2026 files that touch this one</h2>
    <p>Chihiro copies Iai off <a href="kuguri.html">Kuguri</a> at the Kyoto Bloodshed Hotel before he ever draws against Samura with his eyes shut on purpose. The hotel is a school. Kuguri is an unwilling instructor. <a href="tafuku.html">Tafuku</a> is the Kamunabi partner who starts as an enemy at the auction and learns the same lesson Hiyuki does: this boy will spend a body without spending the people inside the building. <a href="kasen.html">Kasen</a> is why the raid happened; Chihiro’s deal with the bureau (Magatsumi to the state, Enten in his hand) assumes a director who wants blades sealed. Kasen wanted them used. Those are not the same Kamunabi.</p>
    <p>Hinao’s Cafe Haru Haru is the civilian door Shiba uses when the coat is too loud. Voiced comic: Shoya Ishige. Cypic: Taihi Kimura. Official character art on this page is the anime sheet. By the end of Part 1 the notes in his head include a new Enten and even a new Cloud Gouger, which is how you know the revenge engine has become a smith’s ledger. Part 2 does not stay with him. It goes to the kiln that will make the ledger necessary. See <a href="../manga/part-2.html">Part 2</a> and <a href="../world/techniques.html">Enten’s kit</a>.</p>
""",
    "characters/kunishige.html": """
    <h2>The colleague and the kiln</h2>
    <p><a href="subaru.html">Subaru Urita</a> took a liking to him immediately: another smith, impossible eyes, a project that would become six war crimes and a seventh apology. Subaru is a sushi chef first. Kunishige is a picky weapons dealer who barely ate. Together they start the Enchanted Blades. Part 2’s smelting chapters (125–129) are that start, shown as labor. Chapter 129, Ironworks, puts Chiaki in the fire as the reason he keeps his eyes open. Shiba is already the friend who will not let him quit. Mashiro is still alive and still opposed to stealing ore for a civilian. Hasumi’s lab is still failing.</p>
    <p>Kasen later leaks the address because a director thinks order lives in Magatsumi. Azami and Kudo spent political capital the other way. The raid is three Hishaku, including Hokuto and Uran. Enten stays with the son. The wartime six leave. Volume 12 will carry “Kunishige Rokuhira” and “Swordsmith” as present-tense titles before the war book opens. Cypic voice: Tomokazu Seki. Voiced comic: Kenta Fujimaki. See <a href="../analysis/irishima.html">Irishima’s vein</a>.</p>
""",
    "characters/sojo.html": """
    <h2>The original bearer</h2>
    <p>Cloud Gouger had a master before the customer. <a href="ibuki.html">Ibuki Misaka</a> was Samura’s equal in the war, retired afterward, and was murdered by <a href="hokuto.html">Hokuto</a> so the Lifelong Contract would open. Yura sold the weather sword to Sojo in early October. Recaps that start the blade with Sojo are doing Ibuki’s grave a disservice. Sojo found cloaked Mei. He did not invent weather. He was the worst reader of a sword that already had a brief.</p>
    <p>Natsuki, the younger Misaka, kept training and still wants to stand beside bearers the press named. Lightning Menace is voltage in the body, not Mei. Volume 10 puts Natsuki on a jacket with Hokuto. Sojo is already dead by then, a bathhouse extra packed next to a Datenseki suicide. The customer is a Volume 2 problem. The contract-opening is a Hishaku method. See <a href="../blades/cloud-gouger.html">Cloud Gouger</a> and the <a href="../world/techniques.html">technique catalog</a>.</p>
""",
    "characters/hiyuki.html": """
    <h2>The other half of the act</h2>
    <p><a href="tafuku.html">Tafuku Mihara</a> is the partner this file used to leave as a caption. Duel domain: two people, one match, then the street returns. He looks like a sumo wrestler and fights like a referee. Together they are how the Kamunabi wishes it looked. The Anti-Cloud Gouger Special Forces are how it looked in the first book: six specialists, four dead. Hiyuki’s Flame Bone is still one of the few innate arts the text will stand next to an Enchanted Blade. Tafuku’s domain is how the bureau practices not burning the prefecture.</p>
    <p>Kasen’s leak and Akemura standing up in Yura make the perfect act insufficient. A skeleton on a permission slip does not beat Magatsumi. The <a href="../factions/kamunabi.html">Kamunabi page</a> is the org chart. The <a href="../analysis/flame-bone.html">Flame Bone essay</a> is the license. This addendum is the partner.</p>
""",
    "characters/samura.html": """
    <h2>The school around him</h2>
    <p><a href="kiri.html">Kiri Shirakai</a> is the founder’s granddaughter, raised in part by Samura and Uruha, carrying a two-meter odachi into a curriculum that told her women cannot. Itsuo still texts from the mountains. Iori is the daughter whose memories he erased. Chihiro copies the closed-eye draw off Kuguri, then off the house, then off Samura himself. The school is larger than the fastest bearer. Black Suzaku is dark power: he spends his life, stalls Magatsumi’s drain, sends Tobimune to Iori, dies. The <a href="../world/iai.html">Iai page</a> is the curriculum. The <a href="../world/techniques.html">Tobimune kit</a> is the support blade he was given because Kunishige thought someone should keep other people alive.</p>
""",
    "characters/yura.html": """
    <h2>The ten, named</h2>
    <p>The Hishaku are not a vibe. They are eight printed names and two still unlabeled. <a href="hokuto.html">Hokuto</a> opened Cloud Gouger by killing Ibuki. <a href="kuguri.html">Kuguri</a> courted a blade without a contract and forgot a kidnapping when Chihiro’s Iai got serious. Hiruhiko is the loud eighteen-year-old. Toto tracks by blood. Uran froze the raid. Bingo eats corpses through lion-dancer heads and then gets sleepy. Yukisada, seventeen, sits in the HQ barrier as a Vessel and will not die of decapitation. Yura is the mind who ordered the raid, sold a sword, listed a masterpiece, signed Samura, walked to the cell, and offered a body. Full org: <a href="../factions/hishaku.html">Hishaku</a>. The director who hired them without meaning to keep them: <a href="kasen.html">Kasen</a>.</p>
""",
    "characters/hakuri.html": """
    <h2>The firm around him</h2>
    <p>The Sazanami are two centuries of auction, not a supporting cast. Kyora is the eleventh head. The Tou are Soya, Tenri, Tamaki, Enji. Tenri dies on fake Datenseki. Soya crawls out with amnesia and a volume extra about memories he would like to misplace. Hakuri is the only living Sazanami to hold both Isou and the Storehouse. That is why Magatsumi can be hidden when Yukisada splits the Kamunabi barrier, and why Chihiro’s deal with the bureau has logistics. Full household: <a href="../factions/sazanami.html">Sazanami</a>. Arc: <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>.</p>
""",
    "blades/cloud-gouger.html": """
    <h2>Who held it</h2>
    <p>Ibuki Misaka, wartime, Samura’s equal, retired, murdered by Hokuto. Sojo, customer, cloaked Mei, True Realm as slaughter, Datenseki suicide. Chihiro, dying contract, Mei: Shred, black because the blade is dying, last charges at the Rakuzaichi, pieces in the bag, notes toward forging it again. Natsuki never held it. Lightning Menace is the family rhyme without Datenseki. Files: <a href="../characters/ibuki.html">Ibuki</a>, <a href="../characters/hokuto.html">Hokuto</a>, <a href="../characters/natsuki.html">Natsuki</a>. Kit: <a href="../world/techniques.html">technique catalog</a>.</p>
""",
    "blades/enten.html": """
    <h2>The catalog version</h2>
    <p>Kuro, Kuro: Shred, Aka, Nishiki, Nishiki: Support. True Realm: Magatsumi’s death. Dark power is not Enten’s usual color; the goldfish stay a household even when the coat is black. The full list with the other four named blades sits on the <a href="../world/techniques.html">technique catalog</a>. Part 2’s kiln is why this seventh sword will have to exist. Chiaki in the fire, chapter 129, is the hope that becomes a bowl instead of a prophecy. See <a href="../manga/part-2.html">Part 2</a>.</p>
""",
    "arcs/sword-bearer.html": """
    <h2>The long book’s new files</h2>
    <p>Volume 10, <em>The Swordsmen</em>, is Natsuki, Hokuto, Uruha, Yura on one jacket. Kasen’s leak is printable in that book. Kiri escorts Hakuri toward Shinuchi. Yukisada sits in the barrier. Tafuku’s perfect act is not the HQ’s tool; the basement does not use referees. Kuguri’s hotel classroom is how Chihiro arrives at Enten versus Tobimune with his eyes already shut. Ibuki is the grave under Cloud Gouger’s residual charges. Subaru is relocated rather than spent. The org pages for this arc are <a href="../factions/hishaku.html">Hishaku</a> and <a href="../factions/kamunabi.html">Kamunabi</a>.</p>
""",
    "guide/series.html": """
    <h2>Where the numbers sit now</h2>
    <p>Eleven Japanese volumes as of 1 May 2026. Volume 12, 4 September 2026. Chapter 129, Ironworks, 23 August 2026. Over 4 million copies in circulation by April 2026. Next Manga Award, print, 2024. Daruma for Best Action Manga, 2026. Cypic, Takeuchi, Sasaki, April 2027. The desk that holds those facts without wrecking this guide’s lede is the <a href="../manga/publication.html">publication record</a>. The uncollected war book is the <a href="../manga/part-2.html">forge page</a>. Names: <a href="cast.html">who is who</a>.</p>
""",
    "fun/hokazono.html": """
    <h2>The 2026 shelf</h2>
    <p>Circulation crossed 4 million by April 2026. Volume 11, <em>Heroes</em>, 1 May. Volume 12 solicited for 4 September. Japan Expo Daruma for Best Action Manga. The first twenty minutes of the Cypic series toured from July 2026. He talked to a real swordsmith so Part 2’s smelting would not be cosplay. Chapter 129 puts that homework inside a fire Chiaki has to pull him through. The author page’s older jokes (Naruto, Winter Soldier, goldfish not koi) are still true. The new fact is that the kiln is on the page. See <a href="../manga/publication.html">publication</a> and <a href="../analysis/irishima.html">Irishima’s vein</a>.</p>
""",
}

for rel, html in ADDENDA.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    needle = '<p class="related">'
    if needle not in text:
        needle = "</article>"
        if needle not in text:
            print("skip, no anchor", rel)
            continue
        text = text.replace(needle, html + "\n     </article>", 1)
    else:
        text = text.replace(needle, html + "\n        " + needle, 1)
    path.write_text(text, encoding="utf-8")
    print("expanded", rel)

print("done")
