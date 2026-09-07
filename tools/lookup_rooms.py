#!/usr/bin/env python3
"""Chapter rooms and lookup tables: timeline, profiles, fight log, technique index."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Kagurabachi Archive</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+JP:wght@400;500;600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/site.css">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
"""

FOOT = """
  </main>
  <div id="site-footer"></div>
  <script src="../js/site.js"></script>
</body>
</html>
"""

VIZ = (
    '<a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> or '
    '<a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>'
)


def write(rel, title, desc, crumb, kicker, h1, jp, lede, body, extra=""):
    html = (
        HEAD.format(title=title, desc=desc)
        + f'<p class="crumb">{crumb}</p>\n'
        + f'<header class="page-hero"><div>\n  <p class="kicker">{kicker}</p>\n'
        + f'  <h1>{h1}<span class="jp">{jp}</span></h1>\n'
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + extra
        + f'<article class="article">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def ch_nav(prev, nxt, extras):
    links = []
    if prev:
        links.append(f'<a href="chapter-{prev[0]}.html">Ch. {prev[0]} {prev[1]}</a>')
    links.append('<a href="chapters.html">Chapter index</a>')
    if nxt:
        links.append(f'<a href="chapter-{nxt[0]}.html">Ch. {nxt[0]} {nxt[1]}</a>')
    for href, label in extras:
        links.append(f'<a href="{href}">{label}</a>')
    return '<nav class="related" aria-label="Related pages">' + "".join(links[:8]) + "</nav>"


def chapter(n, en, jp, kicker, lede, body, prev, nxt, extras):
    rel = f"manga/chapter-{n}.html"
    title = f"Kagurabachi Chapter {n} “{en}”"
    desc = f"Kagurabachi chapter {n}, {en}: a room for the issue, not a substitute. Official reading on VIZ and MANGA Plus."
    crumb = f'<a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter {n}'
    write(
        rel,
        title,
        desc,
        crumb,
        kicker,
        f"Chapter {n} - “{en}”",
        jp,
        lede,
        body + "\n    " + ch_nav(prev, nxt, extras),
    )


# --- Chapter rooms (high-search issues; not a dump of all 130) ---

chapter(
    8,
    "Norisaku Madoka: I Will Change",
    "円 法炸 〜俺は変わるんだ〜",
    "Volume 1 · Vs. Sojo",
    "A Daruma sorcerer decides to go straight. The title is his name and a promise. Sojo treats both as a leak.",
    f"""
  <p>Read it official: {VIZ}. This page is a room for the issue, not a substitute. Chapter 8 is still Volume 1. Char has already said she has seen an Enchanted Blade. Madoka, Sojo’s employee, is the confirmation. His art is exploding Daruma. Chihiro and Shiba beat him. He decides to stop being a sorcerer and go home.</p>
  <h2>The promise</h2>
  <p>The English title keeps his full name. The Japanese title adds the sentence: I will change. The book is not joking. A man who worked for a customer tries to walk back into a civilian life. Sojo kills him for talking. The chapter’s title becomes a grave marker before Volume 2 opens.</p>
  <p>He is not Hishaku. He is payroll. <a href="../characters/sojo.html">Sojo</a> is a sale, not one of the ten. File: <a href="../characters/madoka.html">Norisaku Madoka</a>. Street: <a href="../world/underworld.html">underworld</a>. Arc: <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
  <h2>What it plants</h2>
  <ul>
    <li><strong>Talking is lethal</strong> around Cloud Gouger’s customer.</li>
    <li><strong>Char’s sighting is real</strong> because Madoka is real.</li>
    <li><strong>Civilian exit is not granted</strong> by wanting it. The cafe and the shop are the exceptions the later book keeps spending people to protect.</li>
  </ul>
""",
    (1, "Mission"),
    (9, "Enten vs Cloud Gouger"),
    [("../characters/madoka.html", "Madoka"), ("../arcs/vs-sojo.html", "Vs. Sojo")],
)

chapter(
    9,
    "Enten vs. Cloud Gouger",
    "淵天vs刳雲",
    "Volume 2 opener",
    "The title of Volume 2 is also chapter 9. Two Enchanted Blades occupy the same street for the first time.",
    f"""
  <p>Read it official: {VIZ}. Volume 2 takes this title and keeps it through chapter 18. Chapter 9 is the first time Enten and Cloud Gouger share a page as a match, not a rumor. Sojo has the weather. Chihiro has the seventh blade the Kamunabi never registered.</p>
  <h2>The first meeting of two kits</h2>
  <p>Mei, Yui, Kou against Kuro, Aka, Nishiki. True Realm is still five issues away. This issue is the demonstration that a Lifelong Contract is not a metaphor: the steel answers one nervous system. Chihiro is already losing the street. Char is already the prize Sojo wants as a stabilizer.</p>
  <p>The Anti-Cloud Gouger Special Forces are being built for this sword in the same city. They are not in this panel yet as a finished squad. The state’s version of the job arrives later and dies later. Blade files: <a href="../blades/enten.html">Enten</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
  <h2>Where the title sends you</h2>
  <p>Chapter 14 names True Realm. Chapter 18, “Roar,” is the cut. This room is the opening bell. Arc: <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
""",
    (8, "Madoka"),
    (14, "True Realm"),
    [("../blades/enten.html", "Enten"), ("../blades/cloud-gouger.html", "Cloud Gouger")],
)

chapter(
    14,
    "True Realm",
    "本領",
    "Volume 2 · Vs. Sojo",
    "Honryō enters the vocabulary. Not a transformation gauge. The wielder’s intent locking with the steel.",
    f"""
  <p>Read it official: {VIZ}. Chapter 14 is the issue the technique catalog keeps pointing at. True Realm (本領, Honryō) is the brief, meant: the blade when the person finally means it. Sojo’s Cloud Gouger “gains slaughter.” Enten’s True Realm, named later, is Magatsumi’s death. Same word. Different lock.</p>
  <h2>What the issue is not</h2>
  <p>It is not a power-up montage. The Anti-Cloud Gouger Special Forces have already noted that the Enchanted Blades have more in them than the present-tense wielders are spending. Chapter 14 is the book agreeing, then showing what “more” costs when the customer is Sojo.</p>
  <p>Dark power (Kuroi chikara) is the later, blacker cousin: the lock at the edge of death, or when the blade itself is dying. Mei: Shred. Suzaku’s black flames. Magatsumi’s ordinary darkness. File: <a href="../analysis/true-realm.html">the essay</a>, <a href="../world/techniques.html">technique catalog</a>, <a href="technique-index.html">technique index</a>.</p>
""",
    (9, "Enten vs Cloud Gouger"),
    (18, "Roar"),
    [("../analysis/true-realm.html", "True Realm essay"), ("../world/techniques.html", "Techniques")],
)

chapter(
    23,
    "Storehouse",
    "蔵",
    "Volume 3 · Rakuzaichi",
    "The Sazanami subspace gets its own title. Kura is the building. The auction house is the sign on the street.",
    f"""
  <p>Read it official: {VIZ}. Chapter 23 names the architecture the rest of the auction is about. The Storehouse (蔵, Kura) is a subspace. Kyora stores loot and people in it. Hakuri will inherit it. Chihiro later surrenders Enten on purpose so the seventh blade can scout the Kura on its own charge.</p>
  <h2>Why the title is a place</h2>
  <p>Early chapters are objects and meals. The auction speaks in rooms. Storehouse is the first room that is also a weapon. Dual inheritance, Isou plus Kura, is historically almost unique in the clan. Hakuri is still the discarded son in this issue. The architecture is already waiting.</p>
  <p>Longer file: <a href="../world/storehouse.html">the Storehouse</a>. Clan: <a href="../factions/sazanami.html">Sazanami</a>. Arc: <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>. Registration as a technique: <a href="../world/registration.html">Sazanami registration</a>.</p>
""",
    (18, "Roar"),
    (27, "Mr. Inazuma"),
    [("../world/storehouse.html", "Storehouse"), ("../characters/hakuri.html", "Hakuri")],
)

chapter(
    27,
    "Mr. Inazuma",
    "Mr.イナズマ",
    "Volume 3 closer",
    "A child trying to break into the auction for his sister. Chihiro is already the kind of swordsman who gets her out.",
    f"""
  <p>Read it official: {VIZ}. Volume 3 ends on a civilian name. Yuu Inazuma, who calls himself Mr. Inazuma, is trying to break into the 208th Rakuzaichi because his sister is inside it. The auction warehouses people. That is not a metaphor the later chapters invent. It is this issue’s job.</p>
  <h2>What the title refuses</h2>
  <p>The long book could have closed Volume 3 on Hiyuki or Kyora. It closes on a child with a fake adult name. Chihiro gets the sister and the other hostages out when the Storehouse comes apart. The reunion is the argument against treating the Rakuzaichi as a heist.</p>
  <p>File: <a href="../characters/inazuma.html">Yuu Inazuma</a>. The auction: <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>. The civilian door: <a href="../world/civilian.html">civilian sorcerers</a>.</p>
""",
    (23, "Storehouse"),
    (37, "Equal"),
    [("../characters/inazuma.html", "Inazuma"), ("../arcs/rakuzaichi.html", "Rakuzaichi")],
)

chapter(
    37,
    "Equal",
    "対等",
    "Volume 5 opener",
    "The title Volume 4 wore on the jacket becomes an issue. Hakuri and Chihiro are the relationship the clan refused to grant.",
    f"""
  <p>Read it official: {VIZ}. Volume 4 is titled <em>Equal</em>. Chapter 37 keeps the word on the weekly page. Hakuri has begun to wake Isou. The discarded son was scattering his own spirit energy. When he chooses Chihiro, the architecture answers. Dual inheritance is the rare thing. Equality is the rarer one.</p>
  <h2>What equal is not</h2>
  <p>It is not a power ranking. Soya wanted possession. Kyora wanted a warehouse that would outlive his children. Tenri wanted a father’s pride badly enough to eat a half-stable Datenseki tool. Equal is the title the clan would not print on a son. The book prints it on a partnership.</p>
  <p>Hakuri’s file: <a href="../characters/hakuri.html">Hakuri</a>. Volume 4 jacket: <a href="volumes.html">volume guide</a>. The later Storehouse war is chapters 38–44.</p>
""",
    (27, "Mr. Inazuma"),
    (44, "The Curtain Falls"),
    [("../characters/hakuri.html", "Hakuri"), ("../world/storehouse.html", "Storehouse")],
)

chapter(
    44,
    "The Curtain Falls",
    "閉幕",
    "Volume 5 · Rakuzaichi",
    "The 208th Rakuzaichi ends. Prisoners leave. Kyora dies looking through Shinuchi. The firm ends with the building.",
    f"""
  <p>Read it official: {VIZ}. Chapter 44 is the auction’s last page as a going concern. Chihiro has spent Cloud Gouger’s residual charge to take Enten back. Kyora, dying, touches Magatsumi. The Sword Master looks through an auctioneer’s eyes. Hiyuki’s Flame Bone and Chihiro’s goldfish keep the building from becoming a second island long enough for the prisoners to leave.</p>
  <h2>What falls</h2>
  <p>Two centuries of Rakuzaichi. The Storehouse as Kyora’s will. Tenri is already dead. Soya crawls out of rubble later with amnesia. Hakuri walks out with the inheritance the clan called useless. Chihiro will hand Magatsumi to the Kamunabi and keep Enten by joining them. That deal is the next issue’s politics. This issue is the curtain.</p>
  <p>Arc: <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>. Kyora: <a href="../characters/kyora.html">Kyora</a>. Shinuchi as a title: <a href="../world/shinuchi.html">Shinuchi</a>.</p>
""",
    (37, "Equal"),
    (47, "Uruha"),
    [("../arcs/rakuzaichi.html", "Rakuzaichi"), ("../characters/kyora.html", "Kyora")],
)

chapter(
    47,
    "Uruha",
    "漆羽",
    "Volume 6 opener · Sword Bearer",
    "The long book starts naming people. Yoji Uruha, Kumeyuri’s bearer, is the first Sanso the Hishaku spend a chapter on.",
    f"""
  <p>Read it official: {VIZ}. Chapter 47 opens Sword Bearer Assassination. A Sanso is attacked. Uruha is the prodigy loyal to the Rokuhira name, the man who mastered Iai White Purity by sixteen, the bearer who loses the will to live when he hears Kunishige is dead and then meets the son. Kumeyuri is his steel. Natsuki was a candidate. Uruha was chosen.</p>
  <h2>Why the title is a person</h2>
  <p>The auction spoke in architecture. The long book speaks in names: Uruha, Samura, Iori, Natsuki, Kiri. Chapter 47 is the first of those name-titles. The train, Hiruhiko, Kokugoku, and Senkutsuji are the commute this issue starts. File: <a href="../characters/uruha.html">Uruha</a>. Blade: <a href="../blades/kumeyuri.html">Kumeyuri</a>. Arc: <a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a>.</p>
""",
    (44, "The Curtain Falls"),
    (50, "Interception"),
    [("../characters/uruha.html", "Uruha"), ("../arcs/sword-bearer.html", "Sword Bearer")],
)

chapter(
    50,
    "Interception",
    "迎撃",
    "Volume 6 · the train",
    "Hiruhiko boards. The Sanso box does not hold. The fight spills toward a kabuki house.",
    f"""
  <p>Read it official: {VIZ}. Chapter 50 is the train. Chihiro and Hakuri are moving Uruha. Hiruhiko of the Hishaku intercepts. Blood Crane, origami that cuts and lifts. The Hishaku’s idea of a Lifelong Contract is a kill. The Kamunabi’s idea of safety was a box on rails.</p>
  <h2>What gets intercepted</h2>
  <p>Not only a bearer. The state’s logistics. Kokugoku’s Steam Squad has already paid. Fushimi’s Smoke Axe does not save the fortress. The fight that starts here ends in a theater, then a temple. Train file: <a href="../world/train.html">the train interception</a>. Hiruhiko: <a href="../characters/hiruhiko.html">Hiruhiko</a>. Sanso: <a href="../world/sanso.html">Sanso</a>.</p>
""",
    (47, "Uruha"),
    (51, "Samura"),
    [("../world/train.html", "The train"), ("../characters/hiruhiko.html", "Hiruhiko")],
)

chapter(
    51,
    "Samura",
    "座村",
    "Volume 6 · Senkutsuji",
    "Seiichi Samura, Tobimune, Iai White Purity. The fastest bearer gets his own title the week the temple needs him.",
    f"""
  <p>Read it official: {VIZ}. Chapter 51 is the other name the long book had to print. Samura is blind by choice, echolocation off a sheathed blade, sunglasses and candy cigarettes the Masumi will later copy. Tobimune is the support blade: Crow, Owl, Suzaku. Hakuri’s job in this stretch is to put that steel back in the man’s hands.</p>
  <h2>The temple is already a surgery</h2>
  <p>Senkutsuji is where the Masumi serve him. Pine-sorcery hirelings hit the grounds. Samura clears the attack once the blade arrives. What he does with Uruha after that is chapter 57’s collapse. This issue is the man, not yet the cut. File: <a href="../characters/samura.html">Samura</a>. Blade: <a href="../blades/tobimune.html">Tobimune</a>. Place: <a href="../world/senkutsuji.html">Senkutsuji</a>.</p>
""",
    (50, "Interception"),
    (57, "Collapse"),
    [("../characters/samura.html", "Samura"), ("../world/senkutsuji.html", "Senkutsuji")],
)

chapter(
    57,
    "Collapse",
    "崩壊",
    "Volume 7 opener",
    "The temple falls. Samura cuts Uruha down. It looks like a Hishaku pact. It is Suzaku.",
    f"""
  <p>Read it official: {VIZ}. Chapter 57 is the title people search when they want the betrayal. Samura has a deal with the Hishaku that looks like this: eliminate bearers, deliver blades, kill the Sword Master, then die with the ten. He cuts Uruha down at Senkutsuji. The temple collapses. Chihiro is still in the theater with Hiruhiko.</p>
  <h2>What the collapse is hiding</h2>
  <p><span class="spoiler">Suzaku can kill a Lifelong Contract and keep the person. Uruha walks later. The cut is a surgery that has to look like murder so Magatsumi’s knot does not spend the other bearers when a man is “saved.” Owl goes up over Japan. Hiruhiko signs Kumeyuri in the vacancy.</span></p>
  <p>Arc: <a href="../arcs/sword-bearer.html">Sword Bearer</a>. Essay on the support blade: <a href="../analysis/owl.html">Owl over Japan</a>. Uruha’s innate art returns as <a href="../world/crimson-recital.html">Crimson Recital</a>.</p>
""",
    (51, "Samura"),
    (60, "Resurrection"),
    [("../characters/samura.html", "Samura"), ("../characters/uruha.html", "Uruha")],
)

chapter(
    60,
    "Resurrection",
    "黄泉がえり",
    "Volume 7 · Suzaku",
    "The Japanese title is a return from the underworld. Chihiro does not stay dead. Neither, later, does Uruha.",
    f"""
  <p>Read it official: {VIZ}. Chapter 60 is the week the long book admits Tobimune’s flames are not only a burn. Samura has already used Suzaku as policy. Chihiro is cut down and does not stay down. Shiba is in the room the way he has been in every room that was supposed to be a grave.</p>
  <h2>What resurrection costs</h2>
  <p>Suzaku heals the bearer and burns others. After the war Samura advanced it into a contract-killing revival: slash with Suzaku, the Lifelong Contract dies, the person walks. External Suzaku and the black-flame spend come later. This issue is the first time the present tense has to live with a man who can undo a death the plot just paid for.</p>
  <p>Blade: <a href="../blades/tobimune.html">Tobimune</a>. Technique catalog: <a href="../world/techniques.html">techniques</a>. The Masumi, freed and then not free of Iori: <a href="../factions/masumi.html">Masumi</a>.</p>
""",
    (57, "Collapse"),
    (62, "Iori"),
    [("../blades/tobimune.html", "Tobimune"), ("../analysis/owl.html", "Owl")],
)

chapter(
    62,
    "Iori",
    "イヲリ",
    "Volume 7 · Easy Does It",
    "Samura’s daughter gets the title. Memory-sealed. The Hishaku want her as a handle. The Masumi move her anyway.",
    f"""
  <p>Read it official: {VIZ}. Chapter 62 is the other name the hotel stretch cannot start without. Iori Samura trained as a child, was sent away, and had the Masumi erase her father so she could live as a student. The seal frays because she still loved him and because Tobimune is in the country. It breaks later when she shields a classmate.</p>
  <h2>Operation Easy Does It</h2>
  <p>The Masumi take her toward the Kyoto Bloodshed Hotel. Chihiro starts learning Iai by copying. Toto has Samura’s blood as a sample. Kuguri is the unwilling instructor on the road. File: <a href="../characters/iori.html">Iori</a>. Operation: <a href="../world/easy-does-it.html">Easy Does It</a>. Hotel: <a href="../world/hotel.html">Kyoto Bloodshed Hotel</a>.</p>
""",
    (60, "Resurrection"),
    (67, "Kyoto Bloodshed Hotel"),
    [("../characters/iori.html", "Iori"), ("../world/easy-does-it.html", "Easy Does It")],
)

chapter(
    67,
    "Kyoto Bloodshed Hotel",
    "ザ殺戮ホテル",
    "Volume 8 · the house style",
    "The hotel gets the title. Chihiro copies Iai. Iori’s seal is already failing. Hiruhiko is already in the building.",
    f"""
  <p>Read it official: {VIZ}. Chapter 67 names the room Volume 8 will wreck. Yojiro Sengoku runs the Kyoto Bloodshed Hotel and taught the staff Reigen One-Sword Style. Chihiro copies Kuguri and the house with his eyes open, then closed. Iori is upstairs. The Masumi are trying to hold a seal that love and a support blade have already loosened.</p>
  <h2>Why a hotel</h2>
  <p>A Sanso was a box. A temple was a surgery. A hotel is a civilian building asked to hide a girl the Hishaku have already smelled. Toto reads Sengoku’s head later. Hiruhiko’s Play takes the upper floors apart in chapter 76. This issue is the check-in. Place: <a href="../world/hotel.html">the hotel</a>. School: <a href="../world/iai.html">Iai White Purity</a>. Reigen: <a href="../world/reigen.html">Reigen</a>.</p>
""",
    (62, "Iori"),
    (70, "Iai White Purity Style"),
    [("../world/hotel.html", "The hotel"), ("../characters/sengoku.html", "Sengoku")],
)

chapter(
    70,
    "Iai White Purity Style",
    "居合白禊流",
    "Volume 8 · the school",
    "Itsuo Shirakai’s speed religion gets a weekly title. Eyes closed. Chihiro copies it in a hotel corridor.",
    f"""
  <p>Read it official: {VIZ}. Chapter 70 is the school as an issue, not a footnote. Iai White Purity Style (居合白禊流) is Itsuo Shirakai’s answer to unmatched speed. Samura and Uruha are the famous students. Kiri is the granddaughter who brought an odachi to a school that told her not to. Chihiro copies by sight, then by closing his eyes, off Kuguri and the hotel staff.</p>
  <h2>What the title is doing</h2>
  <p>The book has already shown you the style on Samura. This issue names the syllabus while a Hishaku swordsman is the unwilling tutor. Kuguri scorns people who treat swordsmanship as a game and then cannot leave the boy who just improvised the school. File: <a href="../world/iai.html">Iai White Purity</a>. Copy essay: <a href="../analysis/copy.html">Chihiro copies by sight</a>. Itsuo: <a href="../characters/itsuo.html">Itsuo Shirakai</a>.</p>
""",
    (67, "Kyoto Bloodshed Hotel"),
    (76, "Banquet"),
    [("../world/iai.html", "Iai"), ("../analysis/copy.html", "Copy by sight")],
)

chapter(
    76,
    "Banquet",
    "宴",
    "Volume 9 · Kumeyuri",
    "Kumeyuri’s first named technique on the weekly title. Hallucination as a room. Play is already tearing the hotel.",
    f"""
  <p>Read it official: {VIZ}. Chapter 76 is the issue people search when they want the hotel fight as a word. Banquet (宴) is Kumeyuri’s intoxicating hallucination. Reinforced ears mitigate. A fatal wound can snap it. Play (遊) is the other named technique: move nearby objects; fluency scales with respect. Hiruhiko does not respect objects. The upper hotel comes apart.</p>
  <h2>Who is at the table</h2>
  <p>Hiruhiko holds Kumeyuri in Uruha’s vacancy. Chihiro has Enten. Iori’s memories are back. Samura is about to arrive because two Enchanted Blades in one city are an Owl problem. Ro will recover Kumeyuri after the Hishaku extract Hiruhiko. Essay: <a href="../analysis/play.html">Play, objects, Banquet</a>. Blade: <a href="../blades/kumeyuri.html">Kumeyuri</a>.</p>
""",
    (70, "Iai White Purity Style"),
    (82, "Enten vs Tobimune"),
    [("../analysis/play.html", "Play"), ("../blades/kumeyuri.html", "Kumeyuri")],
)

chapter(
    82,
    "Enten vs. Tobimune",
    "淵天 VS飛宗",
    "Volume 9 · the support blade",
    "The seventh blade against the fastest bearer’s support steel. Chihiro says the workshop brief out loud.",
    f"""
  <p>Read it official: {VIZ}. Chapter 82 is the match the cover studies keep pointing at. Enten versus Tobimune. Goldfish versus feathers. Chihiro has copied Iai. Samura has Owl up and a daughter in the same city. The Hishaku are already inside Kamunabi headquarters on the other side of the country.</p>
  <h2>What the versus is for</h2>
  <p>Not a ranking. A conversation with a man who blinded himself and then tried to erase himself from his daughter. Chihiro knows the Seitei War’s covered crime and Kunishige’s guilt. He says Enten was forged to destroy the other Enchanted Blades. Chapter 83 will put that sentence on the title. This issue is the fight that makes the sentence necessary.</p>
  <p>Blades: <a href="../blades/enten.html">Enten</a>, <a href="../blades/tobimune.html">Tobimune</a>. Purpose essay: <a href="../analysis/enten-purpose.html">what Enten was forged for</a>.</p>
""",
    (76, "Banquet"),
    (83, "The Enten"),
    [("../blades/enten.html", "Enten"), ("../blades/tobimune.html", "Tobimune")],
)

chapter(
    83,
    "The Enten",
    "淵天",
    "Volume 9 · the brief",
    "The title and the sword are the same word. Kunishige’s seventh blade, said cleanly: a retraction.",
    f"""
  <p>Read it official: {VIZ}. Volume 9 is titled <em>Enten</em>. Chapter 83 is the weekly page that earns the jacket. Chihiro tells Samura the workshop brief: the seventh blade is not a trophy. Its True Realm is Magatsumi’s death. Samura, who has been trying to spend himself as atonement, has to hear that a boy already owns the tool for the job he was going to die doing.</p>
  <h2>What opens</h2>
  <p>Samura opens his eyes. Iori is in the city. The Hishaku assault on headquarters is the other half of the week. Kudo will die for Hakuri. Uruha is already walking because Suzaku already did the surgery. File: <a href="../blades/enten.html">Enten</a>. Essay: <a href="../analysis/enten-purpose.html">what Enten was forged for</a>. Volume jacket: <a href="covers.html">cover studies</a>.</p>
""",
    (82, "Enten vs Tobimune"),
    (90, "Kiri"),
    [("../blades/enten.html", "Enten"), ("../analysis/enten-purpose.html", "The brief")],
)

chapter(
    90,
    "Kiri",
    "斬ちゃん",
    "Volume 10 · HQ",
    "Kiri Shirakai, two-meter odachi, granddaughter of the man who said she could not. The Japanese title is the affectionate one.",
    f"""
  <p>Read it official: {VIZ}. Chapter 90 gives the long book another name-title. Kiri Shirakai (白廻 斬) is a Kamunabi squadron leader. Five-shaku blade. Dance-like movement because the sword is too long to bully. She was raised in part by Uruha and Samura and still wants to decapitate Itsuo for the school’s bigotry. In headquarters she escorts Hakuri toward Shinuchi.</p>
  <h2>Why ちゃん</h2>
  <p>The English title is just Kiri. The Japanese title is 斬ちゃん, the diminutive the swordsmen around her use. The book is allowed to be fond in a basement that is about to lose the Sword Master. File: <a href="../characters/kiri.html">Kiri</a>. Grandfather: <a href="../characters/itsuo.html">Itsuo</a>. HQ: <a href="../world/hq.html">Kamunabi headquarters</a>.</p>
""",
    (83, "The Enten"),
    (91, "Natsuki"),
    [("../characters/kiri.html", "Kiri"), ("../world/hq.html", "HQ")],
)

chapter(
    91,
    "Natsuki",
    "奈ツ基",
    "Volume 10 · Lightning Menace",
    "Ibuki’s brother. Kumeyuri candidate. Volume 10’s jacket face. The title is just his name because the resentment is already loud.",
    f"""
  <p>Read it official: {VIZ}. Chapter 91 is Natsuki Misaka as a weekly title. Lightning Menace (Raiku) is voltage in the body, not Cloud Gouger’s Mei. He kept training after Ibuki put the sword down. Uruha was chosen for Kumeyuri. Natsuki is in headquarters to fight Hishaku and to stand next to the man he still has not forgiven for being picked.</p>
  <h2>The swordsmen</h2>
  <p>Uruha is walking again. Hokuto is in the building. Yura is already spending Shinuchi at range. Kasen’s leak is on the table. Natsuki’s chapter is the brother the war jackets left out. File: <a href="../characters/natsuki.html">Natsuki</a>. Ibuki: <a href="../characters/ibuki.html">Ibuki</a>. Volume 10: <a href="volumes.html">The Swordsmen</a>.</p>
""",
    (90, "Kiri"),
    (98, "Hagiwara"),
    [("../characters/natsuki.html", "Natsuki"), ("../characters/uruha.html", "Uruha")],
)

chapter(
    98,
    "Ikuto Hagiwara, Worthless Commander",
    "無能隊長 萩原幾兎",
    "Volume 11 · the cruel title",
    "The ACG commander still in HQ. Both legs gone. Kugara as a hallucination. The title is the book being cruel on purpose.",
    f"""
  <p>Read it official: {VIZ}. Chapter 98 is the cruelest title in the index. Ikuto Hagiwara commanded six people against one sword. Four graves. He lost both legs. Jikai, magnetism, is still useful in a basement. He hallucinates Kugara, childhood friend since age five, mask and all. The chapter title calls him worthless. The pages do not let you agree for free.</p>
  <h2>What the title is doing</h2>
  <p>The long book has started putting quotation marks on the press’s words. This one does not need quotes. 無能隊長 is an insult the squad already heard from a country that wanted Cloud Gouger handled cleanly. Hagiwara is still in the Yukisada math. File: <a href="../characters/hagiwara.html">Hagiwara</a>. Unit: <a href="../world/acg.html">Anti-Cloud Gouger</a>. Kugara: <a href="../characters/kugara.html">Kugara</a>.</p>
""",
    (91, "Natsuki"),
    (100, "Sword Master"),
    [("../characters/hagiwara.html", "Hagiwara"), ("../world/acg.html", "ACG")],
)

chapter(
    100,
    "Sword Master",
    "剣聖",
    "Volume 11 · the cell",
    "Quotes on the English index. Akemura Soga in the basement. Yura has come to talk to a man the press already named.",
    f"""
  <p>Read it official: {VIZ}. Chapter 100 puts 剣聖 on the weekly page the way the Kamunabi put it on a cover-up. Akemura Soga, Magatsumi’s Lifelong Contract, Chihiro’s uncle, still sane enough to explain Malediction as policy. Yura came to kill him for the blade and stays to offer a body instead.</p>
  <h2>The masterpiece in the room</h2>
  <p>Shinuchi is the auction-house name. Magatsumi is the steel. The Sword Master is the man. If he dies, the other five wartime bearers die with him. That knot is why the cell exists. Chapter 100 is the week the knot starts standing up. File: <a href="../characters/akemura.html">Akemura</a>. Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Essay: <a href="../analysis/malediction.html">Malediction</a>.</p>
""",
    (98, "Hagiwara"),
    (104, "Heroes"),
    [("../characters/akemura.html", "Akemura"), ("../blades/magatsumi.html", "Magatsumi")],
)

chapter(
    104,
    "Heroes",
    "英雄",
    "Volume 11 title issue",
    "Quotes on the English index. The press already used the word. Volume 11 wears it as a jacket.",
    f"""
  <p>Read it official: {VIZ}. Volume 11 is titled <em>Heroes</em>. Chapter 104 is the weekly page that puts quotes around the word the Kamunabi printed on the Sword Bearers after Malediction. Snow, goldfish, Enten raised. The Sword Master is already using Yura. The chapter index keeps the quotation marks for a reason.</p>
  <h2>Who the word spends</h2>
  <p>Samura, Uruha, Ibuki, Subaru, the still-unnamed, Akemura. Heroes is a press category. The book has spent a hundred issues refusing it. This issue hangs the word on a fight that will end with Enten in pieces and a girl holding Tobimune. Jacket: <a href="covers.html">cover studies</a>. Titles essay: <a href="../analysis/titles.html">what the titles are doing</a>.</p>
""",
    (100, "Sword Master"),
    (108, "Enten vs Magatsumi"),
    [("../analysis/titles.html", "Titles"), ("volumes.html", "Volume 11")],
)

chapter(
    108,
    "Enten vs. Magatsumi",
    "淵天 VS勾罪",
    "Part 1 corridor · the brief, spent",
    "The seventh blade against the masterpiece. True Realm as a job, not a speech.",
    f"""
  <p>Read it official: {VIZ}. Chapter 108 is the versus the seventh blade was forged for. Enten against Magatsumi. Goldfish against flowers and insects. Chihiro and Samura have already been dumped onto the street over headquarters. Yura offered the body. Akemura took it.</p>
  <h2>The retraction, used</h2>
  <p><span class="spoiler">The corridor that runs 106–115 is the present tense spending Enten on the thing it was for. Chapter 108 is the first title that says the names in a versus. Chapter 115 will leave the blade in pieces. Samura’s black Suzaku is the later stall. This issue is the job starting.</span></p>
  <p>Purpose: <a href="../analysis/enten-purpose.html">what Enten was forged for</a>. Magatsumi: <a href="../blades/magatsumi.html">Magatsumi</a>. Part 1 closer: <a href="chapter-115.html">Swordsmith</a>.</p>
""",
    (104, "Heroes"),
    (109, "Tobimune vs Magatsumi"),
    [("../blades/enten.html", "Enten"), ("../blades/magatsumi.html", "Magatsumi")],
)

chapter(
    109,
    "Tobimune vs. Magatsumi",
    "飛宗 VS勾罪",
    "Part 1 corridor · the support blade spent",
    "Samura’s steel against the masterpiece. A support kit asked to stall a national crime.",
    f"""
  <p>Read it official: {VIZ}. Chapter 109 is the other versus in the corridor. Tobimune against Magatsumi. Crow, Owl, Suzaku against Spider, vitality drain, the insect kit. Samura has already opened his eyes and chosen the boy’s brief over his own suicide math.</p>
  <h2>What a support blade can still do</h2>
  <p><span class="spoiler">Suzaku’s black flames, dark power, are the spend that stalls Magatsumi’s wide drain long enough for Chihiro to leave. Samura dies in that math. Iori inherits Tobimune. Owl over Japan becomes a girl with her father’s sword.</span> File: <a href="../blades/tobimune.html">Tobimune</a>. Essay: <a href="../analysis/owl.html">Owl</a>. Iori: <a href="../characters/iori.html">Iori</a>.</p>
""",
    (108, "Enten vs Magatsumi"),
    (115, "Swordsmith"),
    [("../blades/tobimune.html", "Tobimune"), ("../characters/samura.html", "Samura")],
)

chapter(
    116,
    "Princess",
    "姫",
    "Part 2 opener",
    "The present tense is over. Chiaki Soga, Princess Soga, foresight as a warrant. Chihiro has not been born.",
    f"""
  <p>Read it official: {VIZ}. Part 1 ended on chapter 115, “Swordsmith.” Chapter 116 opens the war book on a rank. Princess (姫). Chiaki Soga holds the Princess Soga title. Foresight is inherited proof of Izanami. She and Akemura were elevated from a lower branch when the main-line prophetess died without children. The government listens because the clan has been a warning system for a thousand years.</p>
  <h2>What the title refuses to stay for</h2>
  <p>There is no press conference. The page goes to Irishima. The island in the sea is the old Mikaboshi kings coming back for Datenseki. The talks are what you do when a princess can see a war and a bureau still wants a treaty. File: <a href="../characters/chiaki.html">Chiaki</a>. Office: <a href="../world/princess.html">Princess Soga</a>. Part 2: <a href="part-2.html">the forge</a>.</p>
""",
    (115, "Swordsmith"),
    (117, "Irishima Talks"),
    [("../characters/chiaki.html", "Chiaki"), ("../world/princess.html", "Princess Soga")],
)

chapter(
    117,
    "The Irishima Talks",
    "杁島会談",
    "Part 2 · 117–121",
    "The conference gets a title, then four numbered plates, then END. This room is the door for the whole talks.",
    f"""
  <p>Read it official: {VIZ}. Chapters 117 through 121 are one conference with five weekly titles: The Irishima Talks; Parts 2, 3, and 4; then END. This page is the door. Japan wants the vein. The Mikaboshi want Irishima and a foothold. Ariu, crown prince, uses Sumika: insect constructs, poisoned air, a body that can live with Datenseki.</p>
  <h2>Who is at the table</h2>
  <p>Hiroto Soga, clan head, Kurotsuchi, directional gravity. Yoshinojo Soga, the grinning older swordsman. Both will die on this island later; they are not dead in these chapters. Hasumi runs a secret Datenseki lab and is not yet sure Kunishige is the answer. Shiba already is sure. Mashiro, Shiba’s partner, opposes taking stolen ore to a picky smith. Joji is the annoyed senior at the lab.</p>
  <p>The negotiation is the war before the blades: what a state will prefer to a living island. We do not invent a unique beat for Parts 2, 3, and 4 that the magazine did not split into separate encyclopedia facts. The five issues are one talks. END is <a href="chapter-121.html">chapter 121</a>. Island: <a href="../world/irishima.html">Irishima</a>. Vein essay: <a href="../analysis/irishima.html">Irishima’s vein</a>.</p>
""",
    (116, "Princess"),
    (121, "Talks END"),
    [("../world/irishima.html", "Irishima"), ("../characters/ariu.html", "Ariu")],
)

chapter(
    121,
    "The Irishima Talks END",
    "杁島会談 終",
    "Part 2 · the conference closes",
    "終, end. The talks stop being a table and become a process. Chapter 122 is titled Start.",
    f"""
  <p>Read it official: {VIZ}. Chapter 121 is the last plate of 杁島会談. The conference has used four numbered pieces and this END. Japan and the Mikaboshi have said what they will trade. Chiaki as cargo is already in the air as a demand. The Bureau’s lab still does not have a blade. Shiba still wants to walk a mineral to a picky smith.</p>
  <h2>What END hands to Start</h2>
  <p>Chapter 122 is 始動, Start. The process begins. English explainers after 118 and 122 floated paternity rumors; face, eye, and the absence of insect sorcery still point at Kunishige as Chihiro’s father. The rumor stays a camp. Kunishige’s eyes are the only printed way to stabilize Datenseki. That is the plot. Door for the whole talks: <a href="chapter-117.html">chapter 117</a>.</p>
""",
    (117, "Irishima Talks"),
    (122, "Start"),
    [("../world/irishima.html", "Irishima"), ("../factions/soga.html", "Soga and Mikaboshi")],
)

chapter(
    122,
    "Start",
    "始動",
    "Part 2 · the process",
    "The talks have ended. The kiln has not. 始動 is the verb after 終.",
    f"""
  <p>Read it official: {VIZ}. Chapter 122 sits between END and Chiaki. The conference is over. The ore is still a political object. Hasumi’s lab is still powerless in the sense chapter 124 will print. Shiba’s certainty about Kunishige’s eyes is the start the Bureau has been refusing.</p>
  <h2>What starts</h2>
  <p>Not the first named blade. Not Enten. The walk from a negotiation table to a workshop that does not yet have a goldfish bowl. Subaru Urita will be in that shop when the steel finally comes up. Mashiro is still alive. Akemura is still a brother, not a cell. File: <a href="part-2.html">Part 2</a>. Eyes and veins: <a href="../world/veins.html">veins in steel</a>.</p>
""",
    (121, "Talks END"),
    (123, "Chiaki"),
    [("../world/smelting.html", "Smelting"), ("../characters/hasumi.html", "Hasumi")],
)

chapter(
    123,
    "Chiaki",
    "千晃",
    "Part 2 · the person",
    "The princess as a name, not only a title. Romantically tied to Kunishige. Akemura still her younger brother.",
    f"""
  <p>Read it official: {VIZ}. Chapter 123 is the second name-title of Part 2. 116 was the office. This is the person. Chiaki Soga is Chihiro’s mother. She is romantically involved with Kunishige. Akemura is her younger brother, not yet the Sword Master, still the friend a smith can trust. Giyu Soga, Hiroto’s ambitious younger brother, is the kind of heir who might accept Mikaboshi demands that include handing her over.</p>
  <h2>Foresight as a hostage tag</h2>
  <p>The clan is not a single will. Foresight is a warrant the government listens to. It is also the reason a ceasefire can be priced in a woman. Chapter 130 will put that price on a letter. This issue is the person the letter will try to ship. File: <a href="../characters/chiaki.html">Chiaki</a>. Giyu: <a href="../characters/giyu.html">Giyu</a>.</p>
""",
    (122, "Start"),
    (124, "Powerless"),
    [("../characters/chiaki.html", "Chiaki"), ("../world/princess.html", "Princess Soga")],
)

chapter(
    124,
    "Powerless",
    "無力",
    "Part 2 · before the fire",
    "The bureau’s Datenseki research, the army’s first year, and a civilian smith who has not yet looked at the stone.",
    f"""
  <p>Read it official: {VIZ}. Chapter 124 is the last honest title before the fire starts lying that a man is a weapon. 無力 is the lab, the army, and Kunishige’s civilian smallness. Hokazono talked to a real swordsmith so the workshop pages would not be cosplay. Powerless is that homework before the kiln.</p>
  <h2>Who is powerless</h2>
  <p>Hasumi’s secret research. Joji’s seniority. Mashiro’s objection to stolen ore. Shiba’s certainty that does not yet have a blade to point at. The Mikaboshi, who already live with Datenseki and do not need Kunishige’s eyes. The next issue is Smelting. This one is the admission. File: <a href="../world/datenseki.html">Datenseki</a>. Author on pacing and craft: <a href="../fun/pacing.html">pacing</a>.</p>
""",
    (123, "Chiaki"),
    (125, "Smelting"),
    [("../world/datenseki.html", "Datenseki"), ("../characters/kunishige.html", "Kunishige")],
)

chapter(
    125,
    "Smelting",
    "製鉄",
    "Part 2 · the kiln opens",
    "The archive’s smithing manual begins. Datenseki as work. The first blade is still not a montage.",
    f"""
  <p>Read it official: {VIZ}. Chapter 125 opens the smelting run: 125 製鉄, 126 火, 127 弐, 128 参, 129 肆 Ironworks. About 250 kilograms of Datenseki are known in the present; here the vein is still a political object. Unstable, it pops the user. Kunishige’s eyes watch detail until the mineral can be a blade instead of a crater.</p>
  <h2>What is not on the table</h2>
  <p>The goldfish bowl is later. Enten does not exist. Chihiro has not been born. This is the kiln that will make Magatsumi possible, which will make Malediction possible, which will make Enten necessary. Subaru is the colleague the process will need. File: <a href="../world/smelting.html">smelting</a>. Veins: <a href="../world/veins.html">veins in steel</a>. The first blade, still unnamed after 130: <a href="../world/first-blade.html">first blade</a>.</p>
""",
    (124, "Powerless"),
    (126, "Fire"),
    [("../world/smelting.html", "Smelting"), ("../world/veins.html", "Veins")],
)

chapter(
    126,
    "Fire",
    "火",
    "Part 2 · then the rest",
    "Fire is not a metaphor in a smith’s shop. After this issue the serial took an announced month.",
    f"""
  <p>Read it official: {VIZ}. Chapter 126 is why the book then rested. 火. The kiln as a hazard, not a montage. Hokazono announced the break after this issue; 127–130 returned in August 2026. The title is the element, not a mood.</p>
  <h2>What fire is doing</h2>
  <p>Datenseki does not become tamahagane because a princess hopes. It becomes steel because a pair of eyes stay open in heat that wants to take the shop. Chapter 129 will put Chiaki in that fire as memory, then as the reason to keep looking. Chapter 130 will put steel on the floor. This issue is the verb. Rest file: <a href="../fun/hiatus.html">the 2026 rest</a>.</p>
""",
    (125, "Smelting"),
    (127, "Smelting Part 2"),
    [("../fun/hiatus.html", "The 2026 rest"), ("../world/smelting.html", "Smelting")],
)

chapter(
    127,
    "Smelting, Part 2",
    "製鉄 弐",
    "August 2026 return",
    "The book comes back from rest still in the kiln. Part 2 of the smelting, not a new location.",
    f"""
  <p>Read it official: {VIZ}. Chapter 127 is 製鉄 弐, the second plate. The announced rest is over. The process is not. Subaru Urita, prolific smith and sushi chef, is the colleague in the room when the work refuses to become a highlight reel. Sand-Bone One-Sword Style and duplication are his later present-tense kit. Here he is a smith watching another smith’s eyes.</p>
  <h2>What Part 2 of smelting refuses</h2>
  <p>A named first blade. A montage. A skip to Malediction. The Irishima clock is still running in the background: talks over, handover not yet a dated letter. File: <a href="../characters/subaru.html">Subaru</a>. Style: <a href="../world/sand-bone.html">Sand-Bone</a>.</p>
""",
    (126, "Fire"),
    (128, "Smelting Part 3"),
    [("../characters/subaru.html", "Subaru"), ("../world/smelting.html", "Smelting")],
)

chapter(
    128,
    "Smelting, Part 3",
    "製鉄 参",
    "August 2026 · third plate",
    "The third 製鉄. Still not Ironworks. Still not a finished sword.",
    f"""
  <p>Read it official: {VIZ}. Chapter 128 is 製鉄 参. One more weekly title before 129’s 肆. The first Enchanted Blade is labor, failure, heat, and a pair of eyes. The Bureau’s lab is still learning that Shiba was right. Hasumi is coming to trust the work. Joji is still annoyed.</p>
  <h2>The next plate</h2>
  <p>Chapter 129, “Ironworks,” 23 August 2026, puts Kunishige at the edge and Chiaki in the fire as the reason the eyes stay open. Chapter 130 pulls tamahagane from a collapsed furnace. This issue is the third refusal to skip. Close readings: <a href="chapter-129.html">Ironworks</a>, <a href="chapter-130.html">I'm Fine!</a>.</p>
""",
    (127, "Smelting Part 2"),
    (129, "Ironworks"),
    [("../world/smelting.html", "Smelting"), ("chapter-129.html", "Ironworks")],
)

print("chapter rooms done")
