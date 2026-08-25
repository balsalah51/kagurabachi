#!/usr/bin/env python3
"""Second expansion wave: unique scrape addenda for remaining major pages. No em-dashes."""
from pathlib import Path

ROOT = Path("/workspace")

def insert(rel, html):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for needle in ('<p class="related">', "</article>", "  </main>"):
        if needle in text:
            text = text.replace(needle, html + "\n        " + needle, 1)
            path.write_text(text, encoding="utf-8")
            print("expanded", rel)
            return
    print("skip", rel)


insert("characters/shiba.html", """
    <h2>Before the bureau, after the smith</h2>
    <p>Part 2 puts Shiba back in the job he had before the Kamunabi existed as a name: Soga guardian, already famous as a teenager, already sure Kunishige’s eyes are the only way to make Datenseki into a blade instead of a crater. Mashiro is still his partner then, still opposed to stealing ore for a picky civilian, still alive. Hasumi still runs the secret lab. Joji is still annoyed. Chapter 129’s fire is the friendship in real time: Shiba will risk himself so the smith keeps his eyes open. Later he will leave the bureau when that smith hides. The teleport is the same person at two ages.</p>
    <p>Cypic voice: Katsuyuki Konishi. Voiced comic: Jun Fukushima. He is not a bearer. He does not need to be. Cafe Haru Haru is the civilian door. Extraction is the art. When Yukisada splits the HQ barrier, Shiba cannot come in until the field is restored; when it is, he teleports Yura into the street where Chihiro and Samura are waiting, then evacuates civilians. The practical magic of the series is a man who used to guard a princess. See <a href="../manga/part-2.html">Part 2</a> and <a href="../characters/chiaki.html">Chiaki</a>.</p>
""")

insert("characters/uruha.html", """
    <h2>The candidate who was chosen</h2>
    <p>Natsuki Misaka was in the room for Kumeyuri. Uruha was chosen. That resentment is printed on Natsuki’s file, not inferred. Uruha mastered Iai White Purity by sixteen, treats the Rokuhira name as a vocation, and loses the will to live when Kunishige dies. Seeing Chihiro refills the oath. Samura’s Suzaku kills the contract and keeps the man. Crimson Recital limps back. He walks into HQ to keep Hakuri alive and then stands next to Natsuki against Yura and Hokuto, which is a cruel jacket joke: the man who got the blade and the man who wanted it, fighting the killer of Natsuki’s brother. Ro of the Masumi recovers Kumeyuri after Samura takes it off Hiruhiko. Files: <a href="natsuki.html">Natsuki</a>, <a href="kiri.html">Kiri</a> (raised in part by Uruha), <a href="../blades/kumeyuri.html">Kumeyuri</a>.</p>
""")

insert("characters/iori.html", """
    <h2>The school and the hotel</h2>
    <p>Kuguri and Toto are why the Masumi take her to the Kyoto Bloodshed Hotel. Sumi rides a motorcycle. Ikura, the classmate who sits next to her, trails Toto because he is the kind of loner she was kind to; his involvement helps the seal break when she shields him. Sengoku’s Reigen house is the veil. Chihiro copies Iai in the corridors. Hiruhiko wrecks the upper floors with Play. Samura arrives because two Enchanted Blades ping Owl. Kiri Shirakai is the other woman in the Iai family, a granddaughter at war with the founder rather than a daughter erased by a father. After Samura dies, Tobimune is in Iori’s hands. The support blade goes to the person he spent a religion keeping out of the ledger. See <a href="kuguri.html">Kuguri</a>, <a href="kiri.html">Kiri</a>, <a href="../world/iai.html">Iai</a>.</p>
""")

insert("characters/akemura.html", """
    <h2>Brother, uncle, mineral</h2>
    <p>Part 2 will not let this file stay a basement. Chiaki is his sister. Kunishige is his friend. The Mikaboshi are the old kings the Soga once drove off the mainland. Ariu’s insects are a camp of explainers’ original for Magatsumi’s kit; this archive files the camp next to the printed list, not as a caption. Malediction is still the crime. The talks are still talks. The kiln in chapters 125–129 is still making the steel that will make the flowers possible. Kasen wanted that steel as order. Yura offered a body. Samura died in the gap. Chihiro kept pieces. The <a href="../analysis/irishima.html">vein essay</a> is the mineral. The <a href="../manga/part-2.html">forge desk</a> is the magazine. The <a href="../world/techniques.html">insect kit</a> is the list without a three-count.</p>
""")

insert("characters/chiaki.html", """
    <h2>Ironworks</h2>
    <p>Chapter 123 is her name. Chapter 129 is her function in the kiln: Kunishige’s worst memories arrive in the fire first, then she arrives as the reason to keep the eyes open. Princess Soga is a title the government listens to because the clan has been a warning system for a thousand years. It is also a hostage tag. Giyu, Hiroto’s ambitious brother, is the kind of heir who might accept Mikaboshi demands that include handing her over. Shiba tells Kunishige not to lose hope when the title puts distance between them. Chihiro will inherit that hope as a bowl of goldfish instead of a prophecy. Enten’s household language is being assembled here as a relationship, not as a design document. See <a href="../manga/part-2.html">Part 2</a>, <a href="../analysis/irishima.html">Irishima’s vein</a>, <a href="kunishige.html">Kunishige</a>.</p>
""")

insert("characters/azami.html", """
    <h2>The table he sits on</h2>
    <p>Kasen is the director who leaked the address Azami spent capital protecting. Ichiki trained both Azami and Shiba. Yatsuru sealed Shinuchi with them. Izaru talks as if Kunishige stole national property. Kudo dies for Hakuri. Azami kills the Shigyu brothers when they punch into Level 1, then loses a corridor to Yura walking toward the cell. Coin was a clinic stimulant. He made it an executioner’s art, which earned his father’s ire. He is the strongest of the heads and still not enough once Magatsumi is a person in the building. Org: <a href="../factions/kamunabi.html">Kamunabi</a>. Leak: <a href="kasen.html">Kasen</a>.</p>
""")

insert("characters/hiruhiko.html", """
    <h2>The other young blade</h2>
    <p>Kuguri is the Hishaku swordsman who takes swordsmanship personally. Hiruhiko is the one who takes friendship personally. Both are in Kyoto. Toto pulls them out through the fire-gate when Samura arrives. Kumeyuri’s Play becomes demolition because Hiruhiko does not respect objects; Uruha’s Banquet was a different brief on the same steel. Natsuki wanted this sword. Uruha got it. Hiruhiko signed it after a false death. Ro recovered it. Eighteen, Blood Crane, killed at three, treats Chihiro as a peer-shaped friend. The ten’s loud younger blade. Org: <a href="../factions/hishaku.html">Hishaku</a>. Hotel partner: <a href="kuguri.html">Kuguri</a>. Blade: <a href="../blades/kumeyuri.html">Kumeyuri</a>.</p>
""")

insert("characters/char.html", """
    <h2>Why the stabilizer hunt exists</h2>
    <p>Datenseki pops the user unless Kunishige’s eyes (or a fake) intervene. Sojo’s fake was Kyonagi flesh. Char is the last of that clan. Tenri later dies on a half-stable stone trying to impress Kyora: jellyfish, then the crater, same lesson, smaller shop. Part 2’s smelting is the lesson taught in the correct order, with the correct eyes. Char is why Chihiro’s revenge has to share the page with a living person who is not a combatant. Hokuto opened Cloud Gouger so Sojo could buy it. Sojo bought it so he could hunt her. The method is a chain. See <a href="ibuki.html">Ibuki</a>, <a href="../world/datenseki.html">Datenseki</a>, <a href="../analysis/irishima.html">the vein</a>.</p>
""")

insert("characters/kyora.html", """
    <h2>The household</h2>
    <p>Two centuries, not a one-arc villain. The Tou are Soya, Tenri, Tamaki, Enji. Hakuri is the error. Magatsumi in a dying auctioneer’s hand is a proxy, not a contract; Akemura looks through and still does not get a new bearer. The Sazanami sold a listing Yura cracked. They did not join the ten. Full firm: <a href="../factions/sazanami.html">Sazanami</a>. Technique of the house: Isou and Storehouse, dual in Hakuri, historically almost unique. Tenri’s Datenseki death is Part 2’s kiln taught in the wrong shop.</p>
""")

insert("blades/magatsumi.html", """
    <h2>The catalog and the camps</h2>
    <p>Spider, Dragonfly, Centipede, Butterfly, Bee, Malediction. No three-count. Possession path. Master key of the wartime knot. Yura spends it at range through spirit left in the steel, then offers a body. Kasen wanted it as order. After chapter 119, explainers treat Ariu Mikaboshi’s Sumika as the original insect kit. File that camp next to the list. Do not caption the steel with a prince’s name until Jump does. Full kit: <a href="../world/techniques.html">catalog</a>. Mineral politics: <a href="../analysis/irishima.html">Irishima’s vein</a>. Leak: <a href="../characters/kasen.html">Kasen</a>.</p>
""")

insert("blades/tobimune.html", """
    <h2>Support, then inheritance</h2>
    <p>Crow, External Crow, Owl, Suzaku, External Suzaku, black flames. Forged for support, Chihiro says. Samura turned healing into resurrection: slash, contract dies, person walks. Owl at national scale is how the hotel becomes a beacon. Black Suzaku is dark power, life spent, Magatsumi’s drain stalled, Enten’s rot slowed, Tobimune sent to Iori. Kiri is the other Shirakai in the building. Iori is the daughter who was not supposed to hold this. Catalog: <a href="../world/techniques.html">techniques</a>.</p>
""")

insert("blades/kumeyuri.html", """
    <h2>Who wanted it</h2>
    <p>Fifth forged. Uruha chosen. Natsuki a candidate, resentment printed. Hiruhiko signed after Samura’s false death; Destructive Play wrecks the hotel because he does not respect objects. Samura takes it back. Ro recovers it. Banquet fools the senses; reinforced ears mitigate; fatal wounds can snap it. Play’s fluency scales with respect. Two briefs, one steel. Files: <a href="../characters/uruha.html">Uruha</a>, <a href="../characters/natsuki.html">Natsuki</a>, <a href="../characters/hiruhiko.html">Hiruhiko</a>. Catalog: <a href="../world/techniques.html">techniques</a>.</p>
""")

insert("arcs/vs-sojo.html", """
    <h2>The locksmith off-page</h2>
    <p>Hokuto killed Ibuki so this arc could have a customer. The Anti-Cloud Gouger Special Forces are the state’s apology after the original bearer was already a grave: Hagiwara, Kugara, Kazane, Harima, Uzuki, Kasahara. Four die. True Realm enters the vocabulary in chapter 14. Enten cuts Cloud Gouger. Sojo pops himself. Char lives. The method (open contract, sell steel) is Hishaku. The weather is Ibuki’s. The misreading is Sojo’s. Files: <a href="../characters/ibuki.html">Ibuki</a>, <a href="../characters/hokuto.html">Hokuto</a>, <a href="../factions/kamunabi.html">Kamunabi roster</a>.</p>
""")

insert("arcs/rakuzaichi.html", """
    <h2>The firm, not only the night</h2>
    <p>Two centuries of Rakuzaichi. Kyora, Hakuri, the Tou, the Storehouse. Tafuku’s domain makes Hiyuki containable. Kuguri is not here yet; he is a later hotel. Yura walks the floor as a lister, not as Magatsumi’s mouth. Tenri dies on fake Datenseki. Chihiro spends Cloud Gouger’s last charges, which are Ibuki’s leftover weather in a customer’s broken sword. Full household: <a href="../factions/sazanami.html">Sazanami</a>. Hiyuki’s partner: <a href="../characters/tafuku.html">Tafuku</a>.</p>
""")

insert("analysis/true-realm.html", """
    <h2>The catalog’s version</h2>
    <p>Extensions now printed: Kuro: Shred, Cloaked Mei, Mei: Shred, Nishiki: Support, Destructive Play, External Crow, External Suzaku, black Suzaku, Malediction. Dark power is the same lock at the brink. Magatsumi’s ordinary darkness is a diet, not a special mode. Enten’s True Realm is a purpose baked into the seventh blade, which is why Nishiki shrugs off Spider. Sojo’s is slaughter because he meant slaughter. The full grid is the <a href="../world/techniques.html">technique catalog</a>. Part 2’s kiln is where those purposes get written into ore before anyone has a brief.</p>
""")

insert("analysis/malediction.html", """
    <h2>The kiln that made the flowers possible</h2>
    <p>Part 2 is smelting the steel that will become this crime. Chiaki is hope in the fire. Akemura is not yet the uncle in the basement. Kasen will later want the masterpiece as order. The Kamunabi will file 200,000 civilians as victory. The vein essay is the mineral argument; this essay stays the political one. When Jump cuts back to the present, Akemura is wearing the bureau. The cover-up and the possession are the same institution at two ages. See <a href="irishima.html">Irishima’s vein</a>, <a href="../manga/part-2.html">Part 2</a>, <a href="../characters/kasen.html">Kasen</a>.</p>
""")

insert("analysis/enten-purpose.html", """
    <h2>The household in the kiln</h2>
    <p>Enten’s goldfish are not in Part 2 yet. Chiaki is. Shiba is. The picky dealer who barely eats is. The seventh blade’s language is being assembled as relationships before it is a design brief. Chapter 83 in the present says the brief cleanly: a retraction. Chapter 129 in the past shows why a retraction would one day be required. Catalog: <a href="../world/techniques.html">Nishiki as the purpose showing through the kit</a>. Forge: <a href="../manga/part-2.html">Part 2</a>.</p>
""")

insert("world/datenseki.html", """
    <h2>250 kilograms, one pair of eyes</h2>
    <p>Sojo fakes the eyes with Kyonagi flesh and pops. Tenri fakes them with a half-stable stone and pops. The Hishaku hire Datenseki troops at Kokugoku; the Steam Squad beats them, then dies to Hiruhiko. Part 2 is the correct shop: Kunishige’s eyes, a real swordsmith’s homework, fire that almost takes the man until Chiaki arrives. Subaru helps start the blades. The term yōtō is credited to him in craft notes. About 250 kilograms known in the present. The war is a fight over a vein. Essay: <a href="../analysis/irishima.html">Irishima’s vein</a>. Magazine: <a href="../manga/part-2.html">Ironworks</a>.</p>
""")

insert("world/locations.html", """
    <h2>Sanso, hotel, island</h2>
    <p>Kokugoku Hot Spring Sanso: Uruha, Steam Squad, Hiruhiko. Senkutsuji: Samura, Masumi, Owl’s later launch site. Subaru relocated when the pattern becomes obvious. Kyoto Bloodshed Hotel: Sengoku, Reigen, Kuguri’s classroom, Play’s demolition. Cafe Haru Haru: Hinao, Shiba’s civilian door. Irishima: talks 117–121, vein, Part 2. Kamunabi HQ: Yukisada in the barrier, Kudo’s death, the cell. The Storehouse walks because Hakuri walks. See <a href="../factions/kamunabi.html">Sanso on the Kamunabi page</a>, <a href="../manga/part-2.html">the island on the forge desk</a>.</p>
""")

insert("world/iai.html", """
    <h2>The family argument</h2>
    <p>Itsuo Shirakai, founder, misogynist, mountains, texts. Samura and Uruha, famous students. Kiri, granddaughter, odachi, vow to decapitate him, chapter 90. Iori, closed eyes when the seal breaks. Chihiro, copies Kuguri then the house then the bearers. Eyes closed is the curriculum, not theater. The school is larger than the founder. That is the only inheritance this book likes. Files: <a href="../characters/kiri.html">Kiri</a>, <a href="../characters/kuguri.html">Kuguri</a>, <a href="../characters/iori.html">Iori</a>.</p>
""")

insert("world/contracts.html", """
    <h2>How the ten use the knot</h2>
    <p>Kill bearer, open contract, sell or spend steel. Hokuto applies it to Ibuki. The Sanso hits try it on the rest. Samura’s Suzaku is the other method: cut the contract, keep the person. Magatsumi’s master key (Akemura dies, the five die) is why the Kamunabi keep a monster in a basement. Destroy Magatsumi, the knot comes apart. Enten is outside the knot. Chihiro can sign a dying Cloud Gouger anyway; multiple contracts in one nervous system are legal in this book. Yukisada is not a contract problem. He is a barrier problem. Catalog of what the steel does once signed: <a href="techniques.html">techniques</a>. Method: <a href="../factions/hishaku.html">Hishaku</a>.</p>
""")

insert("guide/story.html", """
    <h2>Through 129</h2>
    <p>Part 1: Vs. Sojo, Rakuzaichi, Sword Bearer Assassination, then Swordsmith. Part 2: Princess, four Talks and END, Start, Chiaki, Powerless, Smelting, Fire, Smelting, Smelting, Ironworks. Volume 12 is expected to close the corridor and open the war book on paper. The homepage rows stay one line. This guide stays four movements. The magazine desk for the fourth movement’s present tense is the <a href="../manga/part-2.html">forge page</a>. Names: <a href="cast.html">who is who</a>.</p>
""")

insert("guide/premise.html", """
    <h2>The raid’s paperwork</h2>
    <p>Kasen leaked the address. Hokuto and Uran were in the house. Ibuki died in the same campaign. Enten stayed. The six wartime blades left. Sanso fortresses locked the rest. Sojo bought weather in October. That is the premise with the captions filled in. Chihiro does not start the book knowing his uncle is the Sword Master or his mother is a princess in a fire. The book is the education. Part 2 is the kiln. See <a href="../characters/kasen.html">Kasen</a>, <a href="../characters/hokuto.html">Hokuto</a>, <a href="../characters/ibuki.html">Ibuki</a>.</p>
""")

insert("guide/blades.html", """
    <h2>The catalog door</h2>
    <p>This guide stays pictures and the extra context that would wreck the homepage. The named kit, extensions, dark power, and innate arts now live on the <a href="../world/techniques.html">technique catalog</a>. Ibuki is Cloud Gouger’s original. Subaru is a surviving unnamed bearer. Two wartime swords still have no printed titles. This archive will not invent them.</p>
""")

insert("guide/paper.html", """
    <h2>The 2026 object</h2>
    <p>Eleven Jump Comics volumes. Volume 12 on 4 September 2026. Chapter 129 on 23 August. Four million copies by April. Next Manga Award 2024. Daruma Best Action Manga 2026. Cypic April 2027, twenty-minute tour from July 2026. English Volume 9 on 3 November 2026. The desk that holds ISBNs without turning this guide into a spreadsheet is the <a href="../manga/publication.html">publication record</a> and the <a href="../manga/volumes.html">volume table</a>.</p>
""")

insert("manga/covers.html", """
    <h2>Volume 10’s four</h2>
    <p>Natsuki, Hokuto, Uruha, Yura. The Swordsmen. A Kamunabi squadron leader, the Hishaku who killed his brother, the bearer who got Kumeyuri, the mind who ordered the raid. Volume 11 is Heroes with quotation marks in the chapter index for a reason. Volume 12 is solicited to close Part 1 and open Irishima. Jacket studies on this page stay visual. The names under Volume 10 now have files: <a href="../characters/natsuki.html">Natsuki</a>, <a href="../characters/hokuto.html">Hokuto</a>.</p>
""")

insert("fun/first-read.html", """
    <h2>What chapters 1–20 still will not say</h2>
    <p>They will not say Kasen leaked the address. They will not name Ibuki as Cloud Gouger’s original. They will not tell you Chiaki is Chihiro’s mother or that Part 2 is a kiln. They will not list Twilight Wave or Lightning Menace. That is fine. Send this page and chapter 1 on MANGA Plus. When they want the captions, the <a href="../guide/cast.html">who is who</a> map is the next door, not a spoiler channel for chapter 9.</p>
""")

insert("fun/names.html", """
    <h2>New English desks</h2>
    <p>Twilight Wave for Hagure. Lightning Menace for Raiku. Blood Crane for Chizuru. Flame Bone of the Starving for Gasha no Enkotsu. Ironworks for Seitetsu Shi (chapter 129). Princess Soga. Sword Bearer / Shoyūsha. Vessel for the barrier seat. VIZ Eternal Contracts for Lifelong Contracts. This site’s list follows the names already used on the files. Full kit: <a href="../world/techniques.html">catalog</a>. Glossary: <a href="../world/glossary.html">glossary</a>.</p>
""")

insert("fun/meme.html", """
    <h2>After four million</h2>
    <p>The ironic Big Three posts got chapter 1 opened. Ninety-nine million Manga Plus views, then 4 million circulation by April 2026, a Next Manga Award, a Daruma, a Cypic date, a twenty-minute tour, and a war book in the magazine are people actually reading. The meme page can stay a history of a joke. The <a href="../manga/publication.html">publication record</a> is the joke’s aftermath as numbers. Sunday still lives under one tag. The legal way to be there is still shorter than the leak way.</p>
""")

insert("media/anime.html", """
    <h2>Tour and voices</h2>
    <p>First twenty minutes from July 2026: Anime Expo, Japan Expo, AnimagiC, Anime NYC. Full first episode in Japan Q2 2027. Taihi Kimura, Tomokazu Seki, Katsuyuki Konishi. Voiced comic: Shoya Ishige, Kenta Fujimaki, Jun Fukushima, Akari Tadano (Hinao). Cour length still unconfirmed. Elevator-ending camp still a camp. Publication numbers and the Daruma sit on the <a href="../manga/publication.html">publication record</a>. Character files for the announced three: <a href="../characters/chihiro.html">Chihiro</a>, <a href="../characters/kunishige.html">Kunishige</a>, <a href="../characters/shiba.html">Shiba</a>.</p>
""")

insert("media/index.html", """
    <h2>Part 2 on the desk</h2>
    <p>Do not Skypeia the flashback still holds through 129. The printed run is talks, princess, fire, Ironworks. Paternity rumors after 118 and 122 remain a camp. Magatsumi-as-Ariu after 119 remains a camp. The archive’s versions are the <a href="../manga/part-2.html">forge desk</a> and the <a href="../analysis/irishima.html">vein essay</a>, not a video that outruns the magazine. Goldfish-as-language and Sojo-as-worst-fan still hold against the printed pages.</p>
""")

insert("collectibles/index.html", """
    <h2>What to buy in 2026</h2>
    <p>Japanese Volume 11 is out. Volume 12, 4 September 2026, ISBN 978-4-08-885177-8. VIZ through Volume 8 on shelves or solicited; Volume 9 on 3 November 2026. World-tour tickets for the first twenty minutes are a memory unless a booklet SKU appears. Four million in circulation is the number the meme did not predict. Full dates: <a href="../manga/publication.html">publication record</a>. Jackets: <a href="../manga/covers.html">covers</a>. Extras: <a href="../fun/oneshots.html">bathhouse and Soya</a>.</p>
""")

insert("factions/index.html", """
    <h2>The three full files</h2>
    <p>This index used to be the whole org desk. It is now a door. <a href="kamunabi.html">Kamunabi</a> holds leadership, Hiyuki and Tafuku, Natsuki and Kiri, the Anti-Cloud Gouger roster, Masumi, Sanso. <a href="hishaku.html">Hishaku</a> holds the method and the eight printed names. <a href="sazanami.html">Sazanami</a> holds Kyora, Hakuri, the Tou, and the 208th. Soga and Mikaboshi stay here until Part 2 prints them a solo file. Ariu, Hiroto, Yoshinojo, Giyu, Hasumi, Mashiro live on the <a href="../manga/part-2.html">forge desk</a> and the <a href="../guide/cast.html">cast map</a>.</p>
""")

print("wave 2 done")
