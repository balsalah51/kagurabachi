#!/usr/bin/env python3
"""Write 55 encyclopedia rooms on named subjects this site already prints."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <script>!function(){try{var m=document.cookie.match(/(?:^|; )kb-theme=(dark|light)/);if(m)document.documentElement.setAttribute("data-theme",m[1])}catch(e){}}()</script>
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

PAGES = []


def write(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    html = (
        HEAD.replace("{title}", title).replace("{desc}", desc)
        + f'<p class="crumb">{crumb}</p>\n'
        + f'<header class="page-hero"><div>\n  <p class="kicker">{kicker}</p>\n'
        + f'  <h1>{h1}<span class="jp">{jp}</span></h1>\n'
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + f'<article class="article">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    if path.exists():
        raise SystemExit(f"refusing to overwrite {rel}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    PAGES.append(rel)
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
    write(
        f"manga/chapter-{n}.html",
        f"Kagurabachi Chapter {n} “{en}”",
        f"Kagurabachi chapter {n}, {en}: a room for the issue, not a substitute. Official reading on VIZ and MANGA Plus.",
        f'<a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter {n}',
        kicker,
        f"Chapter {n} - “{en}”",
        jp,
        lede,
        body + "\n    " + ch_nav(prev, nxt, extras),
    )


def add(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    write(rel, title, desc, crumb, kicker, h1, jp, lede, body)


# --- 22 chapter rooms ---

chapter(
    4,
    "Sorcery and the Enchanted Blade",
    "妖術と妖刀",
    "Volume 1 · Vs. Sojo",
    "The first weekly title that names both the street art and the steel. True Realm is still ten issues away.",
    f"""
  <p>Read it official: {VIZ}. This page is a room for the issue, not a substitute. Chapter 4 sits in Volume 1 after “Witness.” Char has already said she has seen an Enchanted Blade. The book now titles the two things the street is mixing: sorcery (妖術) and the Enchanted Blade (妖刀).</p>
  <h2>What the title is doing</h2>
  <p>Early chapters are objects and meals. This one is the vocabulary lesson. Enten is already cutting in cafes. Spirit energy leaves the body as a shape that can be steered. The seventh blade is still a household object with goldfish, not a national listing. The <a href="../world/techniques.html">technique catalog</a> will later split Kuro, Aka, and Nishiki. This issue is the sentence before the kit gets names on the page.</p>
  <p>Volume 1 is still <em>Mission</em>. Chapter 8 will title a Daruma sorcerer’s promise. Chapter 9 will put two Enchanted Blades in the same street. File: <a href="../blades/enten.html">Enten</a>, <a href="../world/sorcery.html">sorcery</a>, <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
""",
    (1, "Mission"),
    (5, "A Good Meal"),
    [("../blades/enten.html", "Enten"), ("../world/sorcery.html", "Sorcery")],
)

chapter(
    5,
    "A Good Meal",
    "ごちそう",
    "Volume 1 · meals",
    "A revenge manga that titles food before True Realm. Char has to eat. The workshop was a kitchen.",
    f"""
  <p>Read it official: {VIZ}. Chapter 5 is the meal title the index keeps pointing at. “A Good Meal.” Chapter 15 will be “Food.” Chapter 17 will be “Tea.” Before Enten versus Cloud Gouger, the book keeps seating people.</p>
  <h2>Why the plate is the point</h2>
  <p>Char needs to eat. Chihiro needs to remember the workshop was a kitchen. The <a href="../analysis/titles.html">titles essay</a> says a hunt that will not spend innocents still has to feed them. The bowl on the table and a plate in a cafe are the same grammar. Sojo’s people eat and die later in the same volume. This issue is the good meal, not the crater.</p>
  <p>File: <a href="../world/food.html">meals</a>, <a href="../characters/char.html">Char</a>, <a href="../world/cafe.html">Cafe Haru Haru</a>. Official chapters only. We do not host them.</p>
""",
    (4, "Sorcery and the Enchanted Blade"),
    (7, "Smoke Signal"),
    [("../world/food.html", "Meals"), ("../characters/char.html", "Char")],
)

chapter(
    7,
    "Smoke Signal",
    "狼煙",
    "Volume 1 · Vs. Sojo",
    "The hunt becomes visible. Madoka’s promise is the next title. Sojo is already weather in the same city.",
    f"""
  <p>Read it official: {VIZ}. Chapter 7 is still Volume 1. The English title is a signal fire. The Japanese is 狼煙. Char’s sighting is already on the table. The underworld job is becoming a hunt other people can see.</p>
  <h2>What it plants</h2>
  <p>Chapter 8 will title Norisaku Madoka’s full name and a promise. Sojo treats talking as a leak. This issue is the smoke before that grave marker. Azami is already warning. Shiba is already the exit. Cloud Gouger is already in a customer’s hand. The Anti-Cloud Gouger Special Forces are being built for that sword in the same city; they are not a finished squad on this page.</p>
  <p>Street: <a href="../world/underworld.html">underworld</a>. Customer: <a href="../characters/sojo.html">Sojo</a>. Next room: <a href="chapter-8.html">chapter 8</a>. Arc: <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
""",
    (5, "A Good Meal"),
    (8, "Madoka"),
    [("../world/underworld.html", "Underworld"), ("../characters/sojo.html", "Sojo")],
)

chapter(
    19,
    "Knight of Darkness",
    "闇の騎士",
    "Volume 3 opener · Rakuzaichi",
    "The title of Volume 3 is also chapter 19. Hiyuki arrives. The auction is already being built.",
    f"""
  <p>Read it official: {VIZ}. Volume 3 takes this title and keeps it through chapter 27. Chapter 18, “Roar,” bisected Cloud Gouger. Chapter 19 opens the 208th Rakuzaichi by sending the Kamunabi’s pointed end. Hiyuki Kagari is Flame Bone of the Starving. The jacket puts her with Chihiro and Kyora: flame-orange against auction green-black.</p>
  <h2>The state’s first offer</h2>
  <p>Vs. Sojo was one customer and a weather sword. The auction is a market that has listed Shinuchi. Hiyuki is the obstacle first: the state telling the smith’s son that the masterpiece is their problem. Chapter 20 will title her as the Kamunabi’s weapon. Chapter 23 will title the Storehouse. This issue is the arrival.</p>
  <p>File: <a href="../characters/hiyuki.html">Hiyuki</a>, <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>, <a href="../analysis/flame-bone.html">Flame Bone</a>. Volume: <a href="volumes.html">Volume 3</a>.</p>
""",
    (18, "Roar"),
    (20, "The Kamunabi's Weapon"),
    [("../characters/hiyuki.html", "Hiyuki"), ("../arcs/rakuzaichi.html", "Rakuzaichi")],
)

chapter(
    20,
    "The Kamunabi's Weapon",
    "神奈備の武器",
    "Volume 3 · Rakuzaichi",
    "Flame Bone as a permission slip. The title says weapon. The person is Hiyuki.",
    f"""
  <p>Read it official: {VIZ}. Chapter 20 is the issue people search when they want the bureau’s pointed end as a word. “The Kamunabi’s Weapon.” Hiyuki is hereditary skeleton, licensed, stood next to Enchanted Blades in the text. Tafuku’s duel domain is the matching room: two people, one match, then the street returns.</p>
  <h2>Not Enten</h2>
  <p>The seventh blade is a household retraction. Flame Bone is a national tool with a handler. The <a href="../analysis/flame-bone.html">Flame Bone essay</a> is the longer argument. This room is the weekly title that already knew the difference. Shinuchi is listed. Enten will later be surrendered on purpose so it can scout the Storehouse. The weapon in this header is the one the state already owns.</p>
  <p>File: <a href="../characters/hiyuki.html">Hiyuki</a>, <a href="../factions/kamunabi.html">Kamunabi</a>, <a href="../characters/tafuku.html">Tafuku</a>.</p>
""",
    (19, "Knight of Darkness"),
    (23, "Storehouse"),
    [("../analysis/flame-bone.html", "Flame Bone"), ("../factions/kamunabi.html", "Kamunabi")],
)

chapter(
    32,
    "Wall",
    "壁",
    "Volume 4 · Rakuzaichi",
    "The auction speaking in architecture. Hakuri is already the person the Storehouse might answer.",
    f"""
  <p>Read it official: {VIZ}. Chapter 32 sits in Volume 4, <em>Equal</em>, between “Mr. Inazuma” and chapter 37’s title. The English word is Wall. The Japanese is 壁. The auction house has been architecture since chapter 23 titled the Storehouse.</p>
  <h2>What this site already printed</h2>
  <p>Hakuri awakens Isou and Storehouse in this volume. The discarded son was scattering his own spirit energy; when he chooses Chihiro, the architecture answers. A wall in a Sazanami building is never only masonry. It is inventory, bloodline, and a subspace that thinks people are stock. This room does not invent a unique panel. It files the title next to the Storehouse and the equal relationship the clan refused to grant.</p>
  <p>File: <a href="../world/storehouse.html">Storehouse</a>, <a href="../characters/hakuri.html">Hakuri</a>, <a href="chapter-23.html">chapter 23</a>, <a href="chapter-37.html">Equal</a>.</p>
""",
    (27, "Mr. Inazuma"),
    (37, "Equal"),
    [("../world/storehouse.html", "Storehouse"), ("../characters/hakuri.html", "Hakuri")],
)

chapter(
    41,
    "Fervent",
    "熱狂",
    "Volume 5 · Rakuzaichi",
    "The title of Volume 5 is also chapter 41. The crowd. Shinuchi heat. The two-hundred-year market ending.",
    f"""
  <p>Read it official: {VIZ}. Volume 5 takes this title through chapter 46. The jacket is crowded: Chihiro, Kyora, Hakuri, Hiyuki. The title <em>Fervent</em> is the crowd. Kyora is already dying into a masterpiece he listed but did not understand.</p>
  <h2>Storehouse war as a header</h2>
  <p>Chihiro spends the last of Cloud Gouger to take Enten back in this volume. Kyora touches Magatsumi. The Sword Master looks through an auctioneer’s eyes. Hiyuki and Chihiro keep the building from becoming a second island. Chapter 44, “The Curtain Falls,” is the stamp. This issue is the heat the stamp is for.</p>
  <p>File: <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>, <a href="../characters/kyora.html">Kyora</a>, <a href="chapter-44.html">The Curtain Falls</a>.</p>
""",
    (37, "Equal"),
    (44, "The Curtain Falls"),
    [("../characters/kyora.html", "Kyora"), ("../arcs/rakuzaichi.html", "Rakuzaichi")],
)

chapter(
    45,
    "What Comes Next",
    "これからの話",
    "Volume 5 closer corridor",
    "After the curtain. Before Uruha. The auction has to become a next sentence.",
    f"""
  <p>Read it official: {VIZ}. Chapter 44 titled the fall of the 208th. Chapter 45 asks what comes next. Chapter 46 is “Unruly Punk.” Chapter 47 opens the long book on Uruha. This issue is the hinge the chapter index already described: the auction speaking in family, then the Sword Bearer Assassination naming people.</p>
  <h2>The bargain already on the table</h2>
  <p>Chihiro gives the Kamunabi Magatsumi and keeps Enten by joining them. Hiyuki is the reason that bargain has a moral floor. Hakuri’s Storehouse leaves the building as a person. The next movement is Sanso boxes and a train. This room is the title that admits the market is over and the hunt is not.</p>
  <p>File: <a href="chapter-44.html">The Curtain Falls</a>, <a href="chapter-47.html">Uruha</a>, <a href="../arcs/sword-bearer.html">Sword Bearer</a>.</p>
""",
    (44, "The Curtain Falls"),
    (47, "Uruha"),
    [("../arcs/rakuzaichi.html", "Rakuzaichi"), ("../arcs/sword-bearer.html", "Sword Bearer")],
)

chapter(
    48,
    "The Kokugoku Steam Squad",
    "国獄 湯煙スクワッド",
    "Volume 6 · Kokugoku",
    "Named in a title. Buried in the same week. The first wave was not the problem.",
    f"""
  <p>Read it official: {VIZ}. Chapter 48 is titled for the Kamunabi guard on Uruha’s hot-spring Sanso. Fushimi is the named specialist: Smoke Axe, cuts with smoke between the hands, bandana. They beat Hishaku-hired Datenseki troops. Hiruhiko is the second wave. The squad dies.</p>
  <h2>How the bureau spends specialists</h2>
  <p>Anti-Cloud Gouger was six people for one sword in the first book. The Steam Squad is the second book’s matching piece for one box. Recaps that say “Hiruhiko attacked a fortress” without the squad skip the people who already won once that week. Uruha is already being moved when the box’s purpose ends.</p>
  <p>File: <a href="../factions/steam-squad.html">Steam Squad</a>, <a href="../world/kokugoku.html">Kokugoku</a>, <a href="../characters/fushimi.html">Fushimi</a>.</p>
""",
    (47, "Uruha"),
    (50, "Interception"),
    [("../factions/steam-squad.html", "Steam Squad"), ("../world/kokugoku.html", "Kokugoku")],
)

chapter(
    56,
    "Daybreak",
    "夜更け",
    "Volume 6 closer",
    "The title of Volume 6 is also chapter 56. 夜更け is late night. The English sold a dawn. Collapse is next.",
    f"""
  <p>Read it official: {VIZ}. Volume 6 is <em>Daybreak</em>, printed 夜更け / 黎明. Chapter 56 is the weekly title that matches the spine. Senkutsuji is already the temple. Hakuri has already been moving Tobimune. Samura clears hirelings. What he does with Uruha is chapter 57’s “Collapse.”</p>
  <h2>Late night as a jacket</h2>
  <p>The Japanese 夜更け is the hour after midnight, not a sunrise. The English volume title still says Daybreak. This site’s volume guide keeps both. Suzaku: kill the contract, keep the man. Owl goes up after. This issue is the last page of the temple volume before the cut gets its own header.</p>
  <p>File: <a href="chapter-51.html">Samura</a>, <a href="chapter-57.html">Collapse</a>, <a href="../world/senkutsuji.html">Senkutsuji</a>.</p>
""",
    (51, "Samura"),
    (57, "Collapse"),
    [("../world/senkutsuji.html", "Senkutsuji"), ("../blades/tobimune.html", "Tobimune")],
)

chapter(
    59,
    "Blackout",
    "暗転",
    "Volume 7 · Night Battle",
    "A stage direction in the week between Collapse and Resurrection. The lights go out on purpose.",
    f"""
  <p>Read it official: {VIZ}. Chapter 59 sits in Volume 7, <em>Night Battle</em>, between “Collapse” and “Resurrection.” The English is Blackout. The Japanese is 暗転: a theatre blackout, the lights cut between scenes.</p>
  <h2>What the long book is doing</h2>
  <p>Samura has already cut Uruha. The Hishaku think they have a partner. Suzaku is contract surgery, not a grave the ten get to keep. Owl is about to make Japan a room. This title is the dark between those facts. We do not invent a unique panel for the blackout. We file the word next to the false deaths and the night the hotel is being chosen.</p>
  <p>File: <a href="chapter-57.html">Collapse</a>, <a href="chapter-60.html">Resurrection</a>, <a href="../analysis/owl.html">Owl</a>.</p>
""",
    (57, "Collapse"),
    (60, "Resurrection"),
    [("../analysis/owl.html", "Owl"), ("../world/senkutsuji.html", "Senkutsuji")],
)

chapter(
    66,
    "Truth",
    "真実",
    "Volume 8 opener",
    "Iori’s past is already the week. The seal is love that was erased. The hotel is the next title.",
    f"""
  <p>Read it official: {VIZ}. Volume 8 is <em>Dawn</em>. Chapter 66 is “Truth.” Chapter 62 already named Iori. Chapter 67 will name the Kyoto Bloodshed Hotel. The Masumi job is Operation Easy Does It: move the daughter because a father who can see the country can also be used as a lever.</p>
  <h2>What truth costs in this book</h2>
  <p>The seal frays because she still loved him and breaks when she shields a classmate. Malediction gets spoken aloud in this volume. Hiruhiko wrecks the hotel with Play. This issue is the word before the building. Samura erased himself from Iori for a reason that was almost love. Truth is the thing the erasure was trying to postpone.</p>
  <p>File: <a href="chapter-62.html">Iori</a>, <a href="../world/easy-does-it.html">Easy Does It</a>, <a href="chapter-67.html">Hotel</a>.</p>
""",
    (62, "Iori"),
    (67, "Kyoto Bloodshed Hotel"),
    [("../characters/iori.html", "Iori"), ("../world/hotel.html", "Hotel")],
)

chapter(
    75,
    "Illusion",
    "幻想",
    "Volume 9 opener · Kumeyuri",
    "Before Banquet has a name on the weekly title. Hallucination as the hallway into the hotel fight.",
    f"""
  <p>Read it official: {VIZ}. Volume 9 is <em>Enten</em>. It opens on chapter 75, “Illusion.” Chapter 76 will title Banquet (宴), Kumeyuri’s intoxicating hallucination. Play is already tearing the hotel. This issue is the word the technique will occupy.</p>
  <h2>Banquet’s door</h2>
  <p>Hiruhiko holds Kumeyuri in Uruha’s vacancy. Reinforced ears mitigate. A fatal wound can snap it. Fluency in Play scales with respect for objects; Hiruhiko does not respect objects. The upper hotel comes apart. Chapter 75 names the category. Chapter 76 names the art.</p>
  <p>File: <a href="chapter-76.html">Banquet</a>, <a href="../analysis/play.html">Play</a>, <a href="../blades/kumeyuri.html">Kumeyuri</a>.</p>
""",
    (70, "Iai White Purity Style"),
    (76, "Banquet"),
    [("../blades/kumeyuri.html", "Kumeyuri"), ("../analysis/play.html", "Play")],
)

chapter(
    80,
    "Secret Room",
    "密室",
    "Volume 9 · hotel",
    "A closed room after Play starts taking the building. Core is the next title in the index.",
    f"""
  <p>Read it official: {VIZ}. Chapter 80 is “Secret Room.” Chapter 79 is “Threat!!” Chapter 81 is “Core.” The hotel fight is already Banquet and Play. Samura is already an Owl problem because two Enchanted Blades occupy one city.</p>
  <h2>A room that was supposed to hold</h2>
  <p>This site’s hotel page and the Play essay already treat the Kyoto Bloodshed Hotel as a building that comes apart when the wielder does not respect furniture. A secret room in that week is still architecture under a banquet sword. We do not invent who is behind which door. We file the title next to the hotel and the Enten-versus-Tobimune duel that Volume 9 is walking toward.</p>
  <p>File: <a href="../world/hotel.html">hotel</a>, <a href="chapter-76.html">Banquet</a>, <a href="chapter-82.html">Enten vs Tobimune</a>.</p>
""",
    (76, "Banquet"),
    (82, "Enten vs Tobimune"),
    [("../world/hotel.html", "Hotel"), ("../blades/enten.html", "Enten")],
)

chapter(
    92,
    "The Swordsmen",
    "剣士たち",
    "Volume 10 · HQ",
    "The title of Volume 10 is also chapter 92. Blades before factions. Natsuki is the issue next door.",
    f"""
  <p>Read it official: {VIZ}. Volume 10 is <em>The Swordsmen</em>. Chapter 91 named Natsuki. Chapter 92 takes the spine word. The jacket is a four-man war ensemble: Natsuki, Hokuto, Uruha, Yura. Kasen’s leak is on the table. HQ infiltration. Uruha walks again.</p>
  <h2>Blades before factions</h2>
  <p>The titles essay says this chapter wants swordsmen before organizations. Yura starts spending Shinuchi at range. Yukisada will sit in the barrier. The wartime kit is no longer a rumor in a cellar. This room is the header. The people stay on their own files.</p>
  <p>File: <a href="chapter-91.html">Natsuki</a>, <a href="../characters/natsuki.html">Natsuki</a>, <a href="../world/hq.html">headquarters</a>.</p>
""",
    (91, "Natsuki"),
    (97, "Vessel"),
    [("../characters/natsuki.html", "Natsuki"), ("../world/hq.html", "HQ")],
)

chapter(
    97,
    "Vessel",
    "受け皿",
    "Volume 11 · HQ barrier",
    "Yukisada as a wall from the inside. Seventeen. Regeneration past decapitation. The title is the job.",
    f"""
  <p>Read it official: {VIZ}. Chapter 97 is “Vessel.” Yukisada sits in the Kamunabi headquarters barrier so he can split it from inside. Yura calls him the strongest fighter among the ten. You do not stab a wall that is also a person. Hakuri’s answer is Storehouse: remove the Kamunabi vessel from the split.</p>
  <h2>The lock is a teenager</h2>
  <p>Chapter 98 will title Ikuto Hagiwara as a worthless commander. Chapter 99 will put quotation marks on “Strongest.” This issue is the noun those insults are standing on. Regeneration past decapitation is the innate art. Vessel is the assignment. The auction trick, spent on a government building.</p>
  <p>File: <a href="../characters/yukisada.html">Yukisada</a>, <a href="../world/barriers.html">barriers</a>, <a href="../world/vessel.html">Vessel as an art</a>.</p>
""",
    (92, "The Swordsmen"),
    (98, "Hagiwara"),
    [("../characters/yukisada.html", "Yukisada"), ("../world/barriers.html", "Barriers")],
)

chapter(
    99,
    "“Strongest”",
    "一番強い",
    "Volume 11 · quotation marks",
    "The press’s word, dragged into a headquarters fight. Sword Master is the next caption.",
    f"""
  <p>Read it official: {VIZ}. The long book has started putting quotation marks on the press’s words. Chapter 99 is “Strongest.” Chapter 100 is “Sword Master.” Chapter 104 is “Heroes.” Yura already used strongest for Yukisada among the ten. The Sword Master standing up in Yura is a different claim.</p>
  <h2>Captions as politics</h2>
  <p>The titles essay says you do not need the Malediction page to feel this. You need to read the table of contents like a person. A leftover commander got a cruel full name in chapter 98. The next week puts the superlative in quotes. This room files the punctuation.</p>
  <p>File: <a href="chapter-98.html">Hagiwara</a>, <a href="chapter-100.html">Sword Master</a>, <a href="../analysis/titles.html">titles</a>.</p>
""",
    (98, "Hagiwara"),
    (100, "Sword Master"),
    [("../analysis/titles.html", "Titles"), ("../characters/yura.html", "Yura")],
)

chapter(
    105,
    "Transformation",
    "変身",
    "Volume 11 closer",
    "The last weekly title in Heroes. The Sword Master is already wearing another man’s body.",
    f"""
  <p>Read it official: {VIZ}. Volume 11, <em>Heroes</em>, holds chapters 96–105. Chapter 105 is “Transformation.” The jacket is snow, Aka and Kuro, Enten raised. The chapter index already put quotation marks on Heroes. This issue is the last word on that spine.</p>
  <h2>What is already transforming</h2>
  <p>Yura offers a body. Akemura overwrites; he does not sign a new Lifelong Contract. The insect kit is the war. The possession path is the unique clause. Volume 12 is expected to open on “Karma” and close Part 1 on “Swordsmith.” This room is the hinge the solicited book is waiting on.</p>
  <p>File: <a href="chapter-104.html">Heroes</a>, <a href="chapter-106.html">Karma</a>, <a href="../blades/magatsumi.html">Magatsumi</a>.</p>
""",
    (104, "Heroes"),
    (106, "Karma"),
    [("../blades/magatsumi.html", "Magatsumi"), ("../manga/volumes.html", "Volumes")],
)

chapter(
    106,
    "Karma",
    "宿縁",
    "Volume 12 corridor · Part 1 close",
    "The first title the solicited twelfth is expected to collect. Enten versus Magatsumi is two issues away.",
    f"""
  <p>Read it official: {VIZ}. The Sword Bearer page already lists the last present-tense corridor: Karma, Enten vs. Magatsumi, Tobimune vs. Magatsumi, As a Swordsman, Rock, Kunishige Rokuhira, Swordsmith. Chapter 106 is the first of those words. Volume 12 (4 September 2026, ISBN 978-4-08-885177-8) is expected to hold 106–115 and then open the war book.</p>
  <h2>宿縁 as a header</h2>
  <p>Akemura is loose in the Kamunabi. Chihiro has seen the Sword Master wear another man’s body. Samura will spend his life. This title is the debt the workshop and the war already stacked. We do not invent a unique beat for the issue. We file the word the corridor starts on.</p>
  <p>File: <a href="chapter-108.html">Enten vs Magatsumi</a>, <a href="volume-12.html">Volume 12</a>, <a href="../arcs/sword-bearer.html">Sword Bearer</a>.</p>
""",
    (105, "Transformation"),
    (108, "Enten vs Magatsumi"),
    [("../arcs/sword-bearer.html", "Sword Bearer"), ("volume-12.html", "Volume 12")],
)

chapter(
    110,
    "As a Swordsman",
    "剣士として",
    "Volume 12 corridor",
    "After two Enchanted Blade titles. Before Rock. The job, not the press word.",
    f"""
  <p>Read it official: {VIZ}. Chapter 108 titled Enten versus Magatsumi. Chapter 109 titled Tobimune versus Magatsumi. Chapter 110 is “As a Swordsman.” The quotation marks on Strongest and Heroes were the press. This header is the vocation.</p>
  <h2>Who the title can sit on</h2>
  <p>Samura’s support brief, Chihiro’s retraction, Iori inheriting a blade the father spent: the long book has been asking what a swordsman is for since Iai White Purity. <span class="spoiler">Samura spends his life. Black Suzaku stalls Magatsumi’s drain. Iori holds Tobimune.</span> This room files the weekly word. The deaths stay on the character pages.</p>
  <p>File: <a href="chapter-109.html">Tobimune vs Magatsumi</a>, <a href="../characters/samura.html">Samura</a>, <a href="chapter-113.html">Rock</a>.</p>
""",
    (109, "Tobimune vs Magatsumi"),
    (113, "Rock"),
    [("../characters/samura.html", "Samura"), ("../blades/tobimune.html", "Tobimune")],
)

chapter(
    113,
    "Rock",
    "石",
    "Volume 12 corridor · Irishima",
    "The island that starts the clock. English Twitter called the splash Japan’s Atlantis. The first blade is still unnamed.",
    f"""
  <p>Read it official: {VIZ}. Chapter 113 is “Rock.” This site’s world page uses the splash as the island picture. English Twitter called it Japan’s Atlantis. Shokoku rises from the sea. Irishima already showed a Datenseki vein. The Seitei War is a mineral argument that Part 2 will make into talks and a kiln.</p>
  <h2>Stone, not a named sword</h2>
  <p>Chapter 114 will title Kunishige Rokuhira. Chapter 115 will title Swordsmith. Through chapter 130 the first wartime plate of tamahagane comes out of a furnace and no Enchanted Blade has yet been named on the page. This issue is the rock that makes the smith necessary. We do not name the first blade here.</p>
  <p>File: <a href="../world/irishima.html">Irishima</a>, <a href="../world/shokoku.html">Shokoku</a>, <a href="../analysis/irishima.html">the vein essay</a>.</p>
""",
    (110, "As a Swordsman"),
    (114, "Kunishige Rokuhira"),
    [("../world/irishima.html", "Irishima"), ("../world/shokoku.html", "Shokoku")],
)

chapter(
    114,
    "Kunishige Rokuhira",
    "六平国重",
    "Volume 12 corridor",
    "A name-title before Swordsmith. The father is the commute the present tense has left.",
    f"""
  <p>Read it official: {VIZ}. Chapter 114 is the smith’s full name. Chapter 115 is “Swordsmith.” Part 1 ends by handing the book to the man who made the blades and the princess the war will spend. Volume 12 is expected to collect this corridor and open Irishima on paper.</p>
  <h2>The household as a header</h2>
  <p>Kunishige is dead at thirty-seven in the present tense. He is still a picky dealer in Part 2, eyes not yet on the ore. Birthday June 5. Seven blades. Enten never registered. This weekly title is the person, not the job. The job is the next issue.</p>
  <p>File: <a href="../characters/kunishige.html">Kunishige</a>, <a href="chapter-115.html">Swordsmith</a>, <a href="../world/workshop.html">workshop</a>.</p>
""",
    (113, "Rock"),
    (115, "Swordsmith"),
    [("../characters/kunishige.html", "Kunishige"), ("chapter-115.html", "Swordsmith")],
)


# --- 17 technique rooms ---

add(
    "world/kuro.html",
    "Kuro",
    "Kuro, Enten’s black goldfish: the flying slash sized to the fish Chihiro calls, and Kuro: Shred as many small cuts.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Kuro',
    "Enten · 涅",
    "Kuro",
    "涅",
    "Black goldfish paints arm and edge. The household’s first fighting word.",
    """
  <p>Kuro (涅) is Enten’s first named technique. A black goldfish paints arm and edge. The flying slash is sized to the fish called. <strong>Kuro: Shred</strong> (涅千) is many small black fish, many small cuts, more spirit, less strain on the body. The fish can be moved as scouts and tools.</p>
  <h2>Not a transformation</h2>
  <p>True Realm is later and means Magatsumi’s death. Kuro is the daily language: the bowl made into a cut. Chihiro spends it empty-handed once spirit has left the body as a shape. Volume 11’s snow jacket still shows Aka and Kuro because the kit is the face of the seventh blade. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../blades/enten.html">Enten</a>, <a href="aka.html">Aka</a>, <a href="nishiki.html">Nishiki</a>, <a href="techniques.html">catalog</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="aka.html">Aka</a><a href="nishiki.html">Nishiki</a><a href="../blades/enten.html">Enten</a><a href="techniques.html">Catalog</a><a href="technique-index.html">Index</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/aka.html",
    "Aka",
    "Aka, Enten’s red goldfish: drink an attack, then speak Aka plus the absorbed name to spend it back.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Aka',
    "Enten · 猩",
    "Aka",
    "猩",
    "Red goldfish drinks a hit. The name you speak is the one you just swallowed.",
    """
  <p>Aka (猩) is Enten’s red goldfish. It drinks an attack. Speaking Aka plus the absorbed name spends that attack back for a short window. It is not a general shield. It is a mouth with a timer.</p>
  <h2>Red next to black</h2>
  <p>Kuro cuts. Aka returns. Nishiki clothes. Hokazono wanted white, black, and red because the hero’s coat is already stained. The Volume 11 jacket still pairs Aka and Kuro on snow. This page is the drink, not the cloak. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="kuro.html">Kuro</a>, <a href="nishiki.html">Nishiki</a>, <a href="../fun/bowl.html">the bowl</a>, <a href="../blades/enten.html">Enten</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="kuro.html">Kuro</a><a href="nishiki.html">Nishiki</a><a href="../blades/enten.html">Enten</a><a href="techniques.html">Catalog</a><a href="../fun/goldfish.html">Goldfish</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/nishiki.html",
    "Nishiki",
    "Nishiki, Enten’s tricolor cloak: speed, power, and resistance to other Enchanted Blade ailments. Support is the wounded form.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Nishiki',
    "Enten · 錦",
    "Nishiki",
    "錦",
    "The design brief, not a fashion layer. Tricolor spirit as a coat.",
    """
  <p>Nishiki (錦) is Enten’s tricolor cloak of dense spirit. Speed, power, and resistance to other Enchanted Blade ailments, including Spider and vitality-drain. The catalog calls it the design brief, not a fashion layer. <strong>Nishiki: Support</strong> is an unofficial name for the wounded form: supports movement instead of amplifying it. Less strain, still faster than an empty coat.</p>
  <h2>Why a cloak is a counter</h2>
  <p>Enten was forged to end the other six, especially Magatsumi. A coat that resists Magatsumi’s diet is the household answering a national crime. True Realm is still Magatsumi’s death, not this layer. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="kuro.html">Kuro</a>, <a href="aka.html">Aka</a>, <a href="../analysis/enten-purpose.html">what Enten was for</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="kuro.html">Kuro</a><a href="aka.html">Aka</a><a href="../blades/enten.html">Enten</a><a href="techniques.html">Catalog</a><a href="../world/dark-power.html">Dark power</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/mei.html",
    "Mei",
    "Mei, Cloud Gouger’s lightning: a bolt that can charge, a cloak Sojo finds first, and Mei: Shred as black dark power.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Mei',
    "Cloud Gouger · 鳴",
    "Mei",
    "鳴",
    "Lightning. Wear it or throw it. When the blade is dying the color goes black.",
    """
  <p>Mei (鳴) is Cloud Gouger’s lightning bolt. It can charge. A heavy charge disables Mei for about 10–20 seconds until the bearer understands the sword better. <strong>Cloaked Mei</strong> is unofficial: wear the lightning instead of throwing it. Sojo finds this first. Speed like a bolt. <strong>Mei: Shred</strong> (鳴千) is Chihiro, blade dying, black lightning. Dark power. Faster and meaner than white cloak.</p>
  <h2>Weather as a customer’s religion</h2>
  <p>Sojo’s True Realm is slaughter. Chihiro’s last Cloud Gouger is a partner he wants to die well. Same steel. Different lock. Cloaked Mei is how Sojo leaves the bathhouse fight and comes home to Kaburato. The ACG die in that return. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="yui.html">Yui</a>, <a href="kou.html">Kou</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>, <a href="dark-power.html">dark power</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="yui.html">Yui</a><a href="kou.html">Kou</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a><a href="../characters/sojo.html">Sojo</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/yui.html",
    "Yui",
    "Yui, Cloud Gouger’s ice: instant cages and constructs, amount variable with the point of the blade.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Yui',
    "Cloud Gouger · 結",
    "Yui",
    "結",
    "Ice as a cage. Kou exists so this freeze can be larger.",
    """
  <p>Yui (結) is Cloud Gouger’s ice: instant cages and constructs. The amount varies with the point of the blade. Kou’s water or mist exists to make Mei a wire and Yui a larger freeze. The three-count is weather as a kit, not three personalities.</p>
  <h2>Ice next to slaughter</h2>
  <p>Sojo is a fan who spends specialists. Yui is how a street becomes a box. Chihiro inherits residual charges later and spends them at the Rakuzaichi, then the sword is gone. This page is the ice, not the last roar. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="mei.html">Mei</a>, <a href="kou.html">Kou</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="mei.html">Mei</a><a href="kou.html">Kou</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a><a href="techniques.html">Catalog</a><a href="../arcs/vs-sojo.html">Vs. Sojo</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/kou.html",
    "Kou",
    "Kou, Cloud Gouger’s water or mist: the setup art that makes Mei a wire and Yui a larger freeze.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Kou',
    "Cloud Gouger · 降",
    "Kou",
    "降",
    "Water or mist. The unglamorous third that makes the other two meaner.",
    """
  <p>Kou (降) is Cloud Gouger’s water or mist. The catalog is blunt: it exists to make Mei a wire and Yui a larger freeze. Readers who only clip lightning miss the humidity the bolt is using.</p>
  <h2>Setup as a named technique</h2>
  <p>Most blades have three named techniques. Kou is the one that looks like weather instead of a finish. Sojo still spends it as a customer. Chihiro still spends residual charges as a partner. Same third word. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="mei.html">Mei</a>, <a href="yui.html">Yui</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="mei.html">Mei</a><a href="yui.html">Yui</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a><a href="techniques.html">Catalog</a><a href="../world/spirit-energy.html">Spirit energy</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/banquet-art.html",
    "Banquet",
    "Banquet, Kumeyuri’s hallucination technique: intoxicating visions. Reinforced ears mitigate. A fatal wound can snap it.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Banquet',
    "Kumeyuri · 宴",
    "Banquet",
    "宴",
    "Hallucination as a room. Chapter 76 put the word on the weekly title. This page is the art.",
    """
  <p>Banquet (宴) is Kumeyuri’s intoxicating hallucination. Reinforced ears mitigate. A fatal wound can snap it. Chapter 76 is the issue titled for it. Chapter 75 titled Illusion. Play (遊) is the other named technique: move nearby objects; fluency scales with respect.</p>
  <h2>Not Crimson Recital</h2>
  <p>Uruha’s Koen is not a blade technique. It is the innate art that comes back when Samura cuts the contract and keeps the man. The banquet sword is the job. The recital is the person. Hiruhiko holds Kumeyuri in Uruha’s vacancy; Ro recovers the blade after the Hishaku extract Hiruhiko. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../manga/chapter-76.html">chapter 76</a>, <a href="../analysis/play.html">Play</a>, <a href="../blades/kumeyuri.html">Kumeyuri</a>, <a href="crimson-recital.html">Crimson Recital</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/chapter-76.html">Ch. 76</a><a href="../analysis/play.html">Play</a><a href="../blades/kumeyuri.html">Kumeyuri</a><a href="crimson-recital.html">Koen</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/crow.html",
    "Crow",
    "Crow, Tobimune’s swap: trade places with a feather after a faint spirit trace lands on the chosen plume.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Crow',
    "Tobimune · 鴉",
    "Crow",
    "鴉",
    "A support blade’s first door. Swap with a feather. External Crow moves other people.",
    """
  <p>Crow (鴉) is Tobimune’s printed swap: trade places with a feather. A faint spirit trace lands on the chosen feather first. <strong>External Crow</strong> is unofficial: move entities other than Samura and the blade. Chihiro notes Tobimune was forged for support. Crow is the support move that is also an entrance.</p>
  <h2>Feathers before Owl</h2>
  <p>Owl makes Japan a room. Suzaku heals, then kills contracts while keeping the man. Crow is how a blind swordsman is already in the hallway. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="suzaku.html">Suzaku</a>, <a href="../analysis/owl.html">Owl essay</a>, <a href="../blades/tobimune.html">Tobimune</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="suzaku.html">Suzaku</a><a href="../analysis/owl.html">Owl</a><a href="../blades/tobimune.html">Tobimune</a><a href="../characters/samura.html">Samura</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/suzaku.html",
    "Suzaku",
    "Suzaku, Tobimune’s flames: heal the bearer, burn others, later kill a Lifelong Contract and keep the person. Black flames are dark power.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Suzaku',
    "Tobimune · 雀",
    "Suzaku",
    "雀",
    "Flames that heal the bearer. After the war, slash, contract dies, the person walks.",
    """
  <p>Suzaku (雀) is Tobimune’s flames. They heal the bearer, burn others, and can coat the blade. After the war Samura advanced this into resurrection: slash with Suzaku, the contract dies, the person walks. <strong>External Suzaku</strong> is unofficial: heal others and restore ruined objects, including Tobimune itself. <strong>Suzaku: Black Flames</strong> is unofficial dark power. Samura spends his life. Black fire nullifies Magatsumi’s wide drain long enough for Chihiro to leave. Then Samura dies.</p>
  <h2>Mercy as a support brief</h2>
  <p>Uruha “dies” at Senkutsuji because this art looks like a grave. The Hishaku think they have a partner. They have a surgeon. The essay on the death math lives at <a href="../analysis/suzaku.html">Suzaku, the cut that keeps</a>. This page is the kit row. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="crow.html">Crow</a>, <a href="../world/contracts.html">contracts</a>, <a href="../blades/tobimune.html">Tobimune</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../analysis/suzaku.html">Suzaku essay</a><a href="crow.html">Crow</a><a href="../blades/tobimune.html">Tobimune</a><a href="../characters/uruha.html">Uruha</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/isou.html",
    "Isou",
    "Isou, Sazanami burial-force: the innate art Hakuri inherits next to the Storehouse. Dual inheritance, historically almost unique.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Isou',
    "Sazanami · burial-force",
    "Isou",
    "Isou",
    "Burial-force. The clan art that is not the warehouse. Hakuri gets both.",
    """
  <p>Isou is the Sazanami burial-force. The Storehouse is the subspace. Hakuri inherits both. Dual inheritance is historically almost unique in the clan. He was scattering his own spirit energy; when he chooses Chihiro, the architecture answers. Volume 4 is <em>Equal</em> because of that choice, not because the house granted it.</p>
  <h2>Force next to a room</h2>
  <p>Kyora used the Storehouse as civilization. Hakuri’s version leaves the building. Isou is the shove that is not a pocket. Kudo later spends Warrior’s Path so Hakuri can keep walking. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="storehouse.html">Storehouse</a>, <a href="../characters/hakuri.html">Hakuri</a>, <a href="../analysis/hakuri.html">Hakuri essay</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="storehouse.html">Storehouse</a><a href="../characters/hakuri.html">Hakuri</a><a href="../analysis/hakuri.html">Essay</a><a href="../factions/sazanami.html">Sazanami</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/coin.html",
    "Coin",
    "Azami’s Coin (Koin): a clinic stimulant rewritten as an executioner’s projectile. The Shigyu brothers are one of the executions.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Coin',
    "Azami · Koin",
    "Coin",
    "Koin",
    "Clinic chemistry as a thrown sentence. Eleven Kamunabi dead, then both brothers.",
    """
  <p>Azami’s Coin (Koin) is a clinic stimulant rewritten as an executioner’s projectile. The catalog keeps it in one line because the person is the file. The Shigyu brothers are hired chaos: eleven Kamunabi dead. Azami kills both. Coin is the clinic art at that range.</p>
  <h2>A head who stayed inside</h2>
  <p>Azami trained under Ichiki with Shiba. He helps hide Kunishige. He stays in the bureau Shiba walked away from. Headquarters is a building that has already been entered by the time this art is cleanup. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/azami.html">Azami</a>, <a href="../characters/shigyu.html">Shigyu</a>, <a href="hq.html">HQ</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/azami.html">Azami</a><a href="../characters/shigyu.html">Shigyu</a><a href="hq.html">HQ</a><a href="techniques.html">Catalog</a><a href="../factions/kamunabi.html">Kamunabi</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/kurotsuchi.html",
    "Kurotsuchi",
    "Hiroto Soga’s Kurotsuchi: directional gravity. Killed on Irishima by Ariu Mikaboshi.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Kurotsuchi',
    "Hiroto · gravity",
    "Kurotsuchi",
    "Kurotsuchi",
    "Directional gravity. A Soga art that dies on the island the talks are about.",
    """
  <p>Kurotsuchi is Hiroto Soga’s directional gravity. The fight log files Irishima as Soga versus Mikaboshi / Ariu: Kurotsuchi, Sumika, Datenseki bodies. Hiroto and Yoshinojo die later on the island, not in the talks plates. Ariu’s Sumika is insect constructs and poisoned air.</p>
  <h2>Talks first</h2>
  <p>Chapters 117–121 are the conference. The deaths are later work. This page is the gravity, not a spoiler map of which panel. Giyu is Hiroto’s ambitious younger brother, the kind of heir who might accept Mikaboshi demands that include handing Chiaki over. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/hiroto.html">Hiroto</a>, <a href="sumika.html">Sumika</a>, <a href="../world/irishima.html">Irishima</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/hiroto.html">Hiroto</a><a href="sumika.html">Sumika</a><a href="../characters/ariu.html">Ariu</a><a href="fight-log.html">Fight log</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/sumika.html",
    "Sumika",
    "Ariu Mikaboshi’s Sumika: insect constructs, poisoned air, a Datenseki-hardened body. The camp that Magatsumi copies him is still a camp.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Sumika',
    "Ariu · 栖",
    "Sumika",
    "栖",
    "Insects and bad air. A body that can live with the ore. The chapters have not confirmed the copy thesis.",
    """
  <p>Sumika is Ariu Mikaboshi’s insect constructs, poisoned air, and a Datenseki-hardened body. Ariu is crown prince at the Irishima talks. After chapter 119, explainers argue Magatsumi copies his insect sorcery. The chapters have not confirmed that. This encyclopedia marks that camp as a camp.</p>
  <h2>Kings who already live with the stone</h2>
  <p>The Mikaboshi were sorcerer kings the Soga drove into the sea. Their undersea habitat is Datenseki as architecture. Mainland users pop. They do not. Mashiro dies later to Ariu; Part 2 still has him alive in the talks. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/ariu.html">Ariu</a>, <a href="undersea.html">undersea habitat</a>, <a href="../fun/theories.html">marked theories</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/ariu.html">Ariu</a><a href="kurotsuchi.html">Kurotsuchi</a><a href="../blades/magatsumi.html">Magatsumi</a><a href="undersea.html">Undersea</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/akuu.html",
    "Akuu",
    "Mashiro Akuu: air pressure and hands-free weapons. Dies later to Ariu. Part 2 still has him alive in the talks.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Akuu',
    "Mashiro · 空亜",
    "Akuu",
    "空亜",
    "Air pressure. Weapons that do not need a hilt. A living objection in the talks.",
    """
  <p>Akuu is Mashiro’s air pressure, hands-free weapons. He dies later to Ariu. Part 2 still has him alive in the talks, objecting to stolen ore. Shiba’s certainty does not yet have a blade to point at. Mashiro is the voice that does not need Enten to say the mineral is already a crime.</p>
  <h2>Alive in the conference</h2>
  <p>The Irishima plates are not the later deaths. This page keeps the art and the sequence the fight log already printed. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/mashiro.html">Mashiro</a>, <a href="../manga/chapter-124.html">Powerless</a>, <a href="sumika.html">Sumika</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/mashiro.html">Mashiro</a><a href="../characters/shiba.html">Shiba</a><a href="sumika.html">Sumika</a><a href="techniques.html">Catalog</a><a href="../manga/part-2.html">Part 2</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/warriors-path.html",
    "Warrior’s Path",
    "Kudo’s Warrior’s Path (Shitō): send a body through architecture. He spends it on Hakuri.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Warrior’s Path',
    "Kudo · 死闘",
    "Warrior’s Path",
    "死闘",
    "Send a body through a building. The spend is Hakuri, not a flourish.",
    """
  <p>Warrior’s Path (Shitō) is Kudo’s art: send a body through architecture. He spends it on Hakuri. The Volume 11 synopsis already says Kudo dies for Hakuri. Headquarters is the building. The Storehouse is the other way through a wall. Kudo’s way is a person thrown as a key.</p>
  <h2>A death the plot still spends</h2>
  <p>The deaths page keeps him on the list of named fates. This room is the technique so the sacrifice has a verb. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/kudo.html">Kudo</a>, <a href="../characters/hakuri.html">Hakuri</a>, <a href="hq.html">HQ</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/kudo.html">Kudo</a><a href="../characters/hakuri.html">Hakuri</a><a href="isou.html">Isou</a><a href="deaths.html">Deaths</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/jikai.html",
    "Jikai",
    "Hagiwara’s Jikai: magnetism. Legs gone. Still in the Yukisada math. Chapter 98 titles him worthless commander.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Jikai',
    "Hagiwara · 磁戒",
    "Jikai",
    "磁戒",
    "Magnetism. The ACG plan was restrain, magnetize, launch Sojo. Cloaked Mei comes home.",
    """
  <p>Jikai is Ikuto Hagiwara’s magnetism. The Anti-Cloud Gouger plan at the bathhouse is restrain, magnetize, launch Sojo off the island, take Cloud Gouger. Sojo remotely spends a cloaked Mei and returns. Hagiwara loses both legs. Four of six die. He is still in the HQ math around Yukisada. Chapter 98 titles him Ikuto Hagiwara, Worthless Commander.</p>
  <h2>An art that outlives the legs</h2>
  <p>Kugara’s iron body is the childhood friend the leftover commander hallucinates. Kazane’s Kaichi stays unused. Jikai is the verb the cruel caption is still using. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/hagiwara.html">Hagiwara</a>, <a href="acg.html">ACG</a>, <a href="../manga/chapter-98.html">chapter 98</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/hagiwara.html">Hagiwara</a><a href="iron-body.html">Iron body</a><a href="acg.html">ACG</a><a href="../manga/chapter-98.html">Ch. 98</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/vessel.html",
    "Vessel",
    "Yukisada as Vessel: regeneration past decapitation, sat inside the Kamunabi HQ barrier so it can be split from within.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Vessel',
    "Yukisada · 受け皿",
    "Vessel",
    "受け皿",
    "A seventeen-year-old who became a wall from the inside. Chapter 97 titled the job.",
    """
  <p>Vessel is Yukisada’s assignment, not a second innate name. He regenerates past decapitation. He sits in the headquarters barrier so he can split it from inside. Yura calls him the strongest fighter among the ten. Hakuri’s Storehouse is the tool that works: remove the Kamunabi vessel from the split. Chapter 97 is titled Vessel.</p>
  <h2>You do not stab a wall that is also a person</h2>
  <p>The barriers page already wrote that sentence. This room is the technique index row with a door. After the massacre, Azami cannot call Shiba into the building until Yukisada’s stolen barrier is a field again. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../manga/chapter-97.html">chapter 97</a>, <a href="../characters/yukisada.html">Yukisada</a>, <a href="barriers.html">barriers</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/chapter-97.html">Ch. 97</a><a href="../characters/yukisada.html">Yukisada</a><a href="barriers.html">Barriers</a><a href="storehouse.html">Storehouse</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)


# --- 16 world / analysis / fun / volume ---

add(
    "world/tamahagane.html",
    "Tamahagane",
    "Tamahagane in Kagurabachi: Datenseki allowed to be steel. Chapter 130 pulls it from a collapsed furnace after sixty-one hours of blast.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Tamahagane',
    "Chapter 130 · 玉鋼",
    "Tamahagane",
    "玉鋼",
    "Ore that has been allowed to be steel. The first blade is still unnamed on the floor.",
    """
  <p>Tamahagane is Datenseki that has been allowed to be steel. Chapter 129, “Ironworks,” puts Kunishige at the edge of the process. Chapter 130 pulls the plate from a collapsed furnace. The shop clock is March 29. By 18:30, after sixty-one hours of blast, the steel comes up. Subaru Urita says it will make a terrifying sword. Hasumi’s lab is surprised.</p>
  <h2>Not a named Enchanted Blade</h2>
  <p>Through chapter 130 no wartime blade has been named on the page. The first Enchanted Blade stays unnamed. Smelting.html is the kiln. Veins.html is Subaru’s thesis on the board. This page is the word that came out of the furnace. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="smelting.html">smelting</a>, <a href="../manga/chapter-130.html">I'm Fine!</a>, <a href="first-blade.html">first blade</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="smelting.html">Smelting</a><a href="veins.html">Veins</a><a href="../manga/chapter-130.html">Ch. 130</a><a href="datenseki.html">Datenseki</a><a href="first-blade.html">First blade</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/briefcase.html",
    "Sojo’s briefcase",
    "The Datenseki briefcase returned to Kaburato Castle: semi-stabilized ore the Korogumi bring back, then Sojo spends it.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Briefcase',
    "Kaburato · Datenseki",
    "Sojo’s briefcase",
    "Datenseki",
    "Yakuza errand. Semi-stable stone. The house goes with him.",
    """
  <p>Sojo comes home to Kaburato Castle with a briefcase of semi-stabilized Datenseki the yakuza returned. The Korogumi are the neighborhood that can walk that errand. He finds Chihiro in the courtyard. Enten bisects Cloud Gouger. Sojo spends the ore. The house goes with him.</p>
  <h2>Not Kunishige’s eyes</h2>
  <p>Stones that hold for a few minutes. About 250 kilograms of the mineral known in that stretch. One pair of eyes ever made it safe. Sojo chooses Datenseki over a quiet death. The ACG die at the bathhouse so Chihiro can be in this courtyard. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="kaburato.html">Kaburato</a>, <a href="../factions/korogumi.html">Korogumi</a>, <a href="datenseki.html">Datenseki</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="kaburato.html">Kaburato</a><a href="../characters/sojo.html">Sojo</a><a href="../factions/korogumi.html">Korogumi</a><a href="datenseki.html">Datenseki</a><a href="../manga/chapter-18.html">Roar</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/handover.html",
    "The handover letter",
    "Chapter 130’s April 1 noon letter: Irishima’s beach, Chiaki as cargo, three days from the March 29 shop clock.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Handover',
    "Chapter 130 · April 1",
    "The handover letter",
    "April 1",
    "A dated letter, not a rumor. The beach is the office printed as cargo.",
    """
  <p>The dated timeline already has the row. March 29, shop clock: tamahagane. <span class="spoiler">April 1, noon: a letter sets Irishima’s beach for the Chiaki handover. Three days. Japan has accepted the Mikaboshi demand. The clan’s kindness is a forbidden anesthesia, so she will not have to remember what the beach is for. Akemura is in chains for trying to stop it. Kunishige and Shiba interrupt anyway.</span></p>
  <h2>A clock, not a theory</h2>
  <p>We do not invent a Wednesday the book has not given. Part 2 printed March 29 and April 1. The princess page writes the office. This page writes the stationery. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../manga/chapter-130.html">I'm Fine!</a>, <a href="princess.html">Princess Soga</a>, <a href="anesthesia.html">anesthesia</a>, <a href="timeline.html">timeline</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/chapter-130.html">Ch. 130</a><a href="princess.html">Princess</a><a href="anesthesia.html">Anesthesia</a><a href="timeline.html">Timeline</a><a href="../characters/chiaki.html">Chiaki</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/pine-sorcery.html",
    "Pine sorcery",
    "Pine-sorcery hirelings at Senkutsuji and a pine-sorcery barrier at Naginojoen: bought weather, not Hishaku tattoos.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Pine sorcery',
    "Hired weather",
    "Pine sorcery",
    "Pine",
    "A barrier in a Sazanami hallway. Hirelings on a temple lawn. The ten buy weather.",
    """
  <p>Pine sorcery shows up in two printed jobs on this site. The Tou hold a pine-sorcery barrier in a hallway at Naginojoen. Pine-sorcery hirelings hit Senkutsuji while the Masumi suppress sound and scent. Samura clears the grounds once Tobimune is in his hand. The Shigyu page already said the sentence: the ten buy weather. Pine crews at the temple, Datenseki troops at Kokugoku, the brothers at HQ.</p>
  <h2>Not a flame tattoo</h2>
  <p>They are not Hishaku. They are payroll, like Madoka, like the Korogumi briefcase. Recaps that fold the temple attack into “the Hishaku arrive” lose the hired art. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="senkutsuji.html">Senkutsuji</a>, <a href="../factions/tou.html">Tou</a>, <a href="../characters/shigyu.html">Shigyu</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="senkutsuji.html">Senkutsuji</a><a href="../factions/tou.html">Tou</a><a href="../world/naginojoen.html">Naginojoen</a><a href="../factions/hishaku.html">Hishaku</a><a href="fight-log.html">Fight log</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/counter-sorcery-army.html",
    "Counter-Sorcery Army",
    "The Counter-Sorcery Army: the wartime body the Kamunabi are rebuilt from when Shokoku rises and Datenseki becomes a front.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Counter-Sorcery Army',
    "Before the rename",
    "Counter-Sorcery Army",
    "Sorcery Bureau",
    "The bureau’s wartime name. The Kamunabi are what you call it after the island.",
    """
  <p>The Kamunabi form from the Counter-Sorcery Army. The world timeline and the glossary already print that rebuild. Shokoku appears. Irishima’s vein is harvested. The Mikaboshi return with bodies that can live with Datenseki. For two years research goes nowhere. Shiba believes Kunishige’s eyes are the only way to make the mineral usable. He is right. Six Enchanted Blades enter at one year and five months and reverse the front.</p>
  <h2>A rename is still a government</h2>
  <p>The Sorcery Bureau page is the office before the wartime rename. White Robes sit at the leadership table later. Hiyuki is the pointed end of the organization Shiba left. This room is the army the present-day bureau is admitting it used to be. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../factions/bureau.html">Sorcery Bureau</a>, <a href="../factions/kamunabi.html">Kamunabi</a>, <a href="../arcs/seitei-war.html">Seitei War</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../factions/bureau.html">Bureau</a><a href="../factions/kamunabi.html">Kamunabi</a><a href="index.html">World</a><a href="../world/shokoku.html">Shokoku</a><a href="../factions/soga.html">Soga</a><a href="glossary.html">Glossary</a></nav>
""",
)

add(
    "world/anesthesia.html",
    "Anesthesia",
    "The Soga clan’s forbidden anesthesia in chapter 130: kindness so Chiaki will not remember the beach the letter has dated.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Anesthesia',
    "Chapter 130 · forbidden art",
    "Anesthesia",
    "Anesthesia",
    "A kindness that is also a wipe. The title of the issue is I'm Fine!",
    """
  <p><span class="spoiler">Chapter 130 prints the clan’s answer to the handover as a forbidden art the page calls anesthesia: so Chiaki will not have to remember what Irishima’s beach is for. Kunishige and Shiba come in anyway. Two years since he last touched her. The anesthesia is broken by the entrance. The title is what a princess is supposed to say when a nation has decided she is cargo. The page then lets her say she has always wanted to see him.</span></p>
  <h2>Not a technique catalog row</h2>
  <p>This is not Isou. It is not foresight. It is a clan kindness aimed at a dated letter. Akemura is in chains for trying to stop the beach. The younger brother is not yet Magatsumi. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="handover.html">handover</a>, <a href="princess.html">Princess Soga</a>, <a href="../manga/chapter-130.html">I'm Fine!</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="handover.html">Handover</a><a href="princess.html">Princess</a><a href="../characters/chiaki.html">Chiaki</a><a href="../manga/chapter-130.html">Ch. 130</a><a href="../factions/soga.html">Soga</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/teleport.html",
    "Shiba’s teleport",
    "Togo Shiba’s teleportation: extraction, infiltration, civilian evacuation. Famous as a teenager. He will not sign a blade.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Teleport',
    "Shiba · teleportation",
    "Teleport",
    "Teleport",
    "The practical magic of the series. He leaves the space. He does not own it.",
    """
  <p>Shiba’s teleportation is extraction, infiltration, civilian evacuation. Famous as a teenager. Not a bearer. A Lifelong Contract would shut those nerves off; he has never signed one. He dumps a fight onto the street when the Kamunabi basement is the wrong terrain. Cafe Haru Haru is the civilian door. Age 39. Birthday October 15.</p>
  <h2>Space versus exit</h2>
  <p>Tafuku’s domain and Hakuri’s Kura are other ways to control space. Shiba does not control the space. He leaves it. He trained under Ichiki with Azami. He guarded the Soga before the war. He walked away when Kunishige hid. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/shiba.html">Shiba</a>, <a href="duel-domain.html">duel domain</a>, <a href="innate.html">innate</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/shiba.html">Shiba</a><a href="duel-domain.html">Duel domain</a><a href="../world/cafe.html">Cafe</a><a href="innate.html">Innate</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/duel-domain.html",
    "Duel domain",
    "Tafuku Mihara’s duel domain: two people, one match, then the street returns. The matching room next to Flame Bone.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Duel domain',
    "Tafuku · domain",
    "Duel domain",
    "Domain",
    "A match that puts the city on pause. Then the sidewalk is a sidewalk again.",
    """
  <p>Tafuku’s duel domain is two people, one match, then the street returns. He is Hiyuki’s matching room: sumo silhouette, calm. Flame Bone is the pointed end. The domain is the rule that keeps the pointed end from becoming a crowd problem. Chapter 20 titled the Kamunabi’s weapon; this art is how that weapon is allowed to work in a city.</p>
  <h2>Not Storehouse</h2>
  <p>Hakuri’s Kura moves inventory. Shiba leaves a room. Tafuku borrows a street and gives it back. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/tafuku.html">Tafuku</a>, <a href="../characters/hiyuki.html">Hiyuki</a>, <a href="../manga/chapter-20.html">chapter 20</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/tafuku.html">Tafuku</a><a href="../analysis/flame-bone.html">Flame Bone</a><a href="teleport.html">Teleport</a><a href="../manga/chapter-20.html">Ch. 20</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/gansui.html",
    "Gansui",
    "Harima’s Gansui: lift and shape stone so the Anti-Cloud Gouger fight can happen over water instead of a city.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Gansui',
    "Harima · 岩垂",
    "Gansui",
    "岩垂",
    "Stone as a battlefield. Kazane unused beside her. A head wound drops the islands.",
    """
  <p>Gansui (岩垂) is Shiyumi Harima’s art: she lifts and shapes stone. At the bathhouse she pulls the ground into the air so the squad can fight Sojo over the ocean instead of a city. Kazane stays beside her as the unused secret weapon. The other four press Sojo. She holds the floor. Sojo cloaks Mei, comes back, and cuts a large section of her head and shoulder. The platforms fall. She is confirmed dead after the battle.</p>
  <h2>Logistics as a grave</h2>
  <p>Civilian streets stay intact because the fight is a set of floating platforms. Recaps that say “the Kamunabi fought Sojo” without the woman holding the islands skip the reason those civilians live. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/harima.html">Harima</a>, <a href="bathhouse.html">bathhouse</a>, <a href="acg.html">ACG</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/harima.html">Harima</a><a href="iron-body.html">Iron body</a><a href="bathhouse.html">Bathhouse</a><a href="acg.html">ACG</a><a href="techniques.html">Catalog</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/iron-body.html",
    "Iron body",
    "Kugara’s iron body: the ACG art meant for lightning and rain. Sojo kills him. Hagiwara keeps the face as a wound.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Iron body',
    "Kugara · iron",
    "Iron body",
    "Iron",
    "A matching piece against weather. Weather does not check the roster for childhood friends.",
    """
  <p>Hajime Kugara’s art is an iron body. Mask. Friends with Hagiwara since they were five. An iron body is the matching piece a bureau would staff against lightning and rain. Sojo is not weather. Sojo is a fan who spends specialists. Kugara is named among the dead at the compound. Hagiwara later hallucinates this face.</p>
  <h2>No True Realm for iron</h2>
  <p>True Realm arrives in the same fight on Chihiro’s side. Kugara’s iron does not get a brief, meant. It gets a grave. The ACG page is the roster. The character page is the friend. This room is the metal. Official chapters: VIZ / MANGA Plus.</p>
  <p>File: <a href="../characters/kugara.html">Kugara</a>, <a href="jikai.html">Jikai</a>, <a href="acg.html">ACG</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/kugara.html">Kugara</a><a href="../characters/hagiwara.html">Hagiwara</a><a href="jikai.html">Jikai</a><a href="gansui.html">Gansui</a><a href="acg.html">ACG</a><a href="index.html">World</a></nav>
""",
)

add(
    "analysis/hakuri.html",
    "Hakuri and the architecture",
    "Essay: Hakuri Sazanami inherits Isou and the Storehouse. Dual inheritance. The discarded son becomes the walking Kura.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Hakuri',
    "Essay · Storehouse",
    "Hakuri and the architecture",
    "蔵",
    "The clan called him defective stock. The building answered when he chose a smith’s son.",
    """
  <p>Hakuri is the error that ends the firm. Isou is burial-force. The Storehouse is two centuries of auction compressed into a subspace, then into him when he stops scattering his own spirit energy. Dual inheritance is historically almost unique in the Sazanami. Volume 4 titles the relationship <em>Equal</em>. The house never granted it. Chihiro did.</p>
  <p>Kyora used the Kura as civilization and inventory. Hakuri’s version leaves the building: blades across the country, a Vessel lifted out of a government wall, Tobimune returned through a marker mandala. Registration is still a person and their charged objects. The owner changed. Chapter 32 titled Wall in the same volume as that waking. The architecture was always the plot.</p>
  <h2>Brothers, not a fifth Tou</h2>
  <p>Soya, Tamaki, Enji, Tenri are the household military. Hakuri is not a fifth. Tenri dies on a half-stable Datenseki stone trying to impress Kyora. Soya’s extra wants memories gone. Samura erased himself from Iori for a reason that was almost love. Two erasures in one book. Only one of them is trying to keep a daughter out of a ledger. Hakuri’s inheritance is the other motion: keep the room and walk it out of the clan.</p>
  <p>Kudo spends Warrior’s Path so that walk continues. Official chapters: VIZ / MANGA Plus. Related: <a href="../characters/hakuri.html">Hakuri</a>, <a href="../world/storehouse.html">Storehouse</a>, <a href="../world/isou.html">Isou</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/hakuri.html">Hakuri</a><a href="../world/storehouse.html">Storehouse</a><a href="../world/isou.html">Isou</a><a href="revenge.html">Revenge</a><a href="index.html">All essays</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a></nav>
""",
)

add(
    "analysis/suzaku.html",
    "Suzaku, the cut that keeps",
    "Essay: Suzaku looks like a killing. It is contract surgery. Black flames are the later math Samura spends his life on.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Suzaku',
    "Essay · Tobimune",
    "Suzaku, the cut that keeps",
    "雀",
    "Slash. The contract dies. The person walks. The Hishaku file it as a grave and are wrong.",
    """
  <p>Owl is surveillance. Crow is a door. Suzaku is the support brief spent as mercy, then as a life. After the war Samura advanced the flames into resurrection: slash with Suzaku, the Lifelong Contract dies, the person walks. Uruha falls at Senkutsuji looking like the Hishaku pact. It is surgery. Collapse is the title. Resurrection is two issues later. The ten think they have a partner who will eliminate bearers. He is lying about the dying.</p>
  <p><span class="spoiler">Black flames are dark power. Samura spends his life. The fire nullifies Magatsumi’s wide drain long enough for Chihiro to leave. Then Samura dies. Iori holds Tobimune. External Suzaku, unofficial, already showed the art can restore ruined objects, including the blade itself. The daughter inherits the support sword. Whether she puts eyes over Japan is a later chapter.</span></p>
  <h2>Death math is not a power ranking</h2>
  <p>This essay will not rank flames against goldfish. It will say the book’s cruelty is precise: the technique that keeps a man is the technique that spends the surgeon. Owl over Japan is the other support cost. Official chapters: VIZ / MANGA Plus. Kit: <a href="../world/suzaku.html">Suzaku</a>. Owl: <a href="owl.html">the country as a room</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/suzaku.html">Suzaku kit</a><a href="owl.html">Owl</a><a href="../characters/samura.html">Samura</a><a href="../world/contracts.html">Contracts</a><a href="index.html">All essays</a><a href="../blades/tobimune.html">Tobimune</a></nav>
""",
)

add(
    "analysis/foresight.html",
    "Foresight as an office",
    "Essay: Chiaki’s foresight is inherited proof of Izanami. Prophecy made the Soga aristocracy. Part 2 makes it cargo.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Foresight',
    "Essay · Princess Soga",
    "Foresight as an office",
    "姫",
    "A national warrant that looks like a person. The beach letter is what a government does with a warrant.",
    """
  <p>Chiaki Soga’s foresight is Princess Soga’s job and inherited proof of Izanami. The prophecy page already said the useful sentence: prophecy made them aristocracy and made them useful. Giyu can treat the office as something you hand to Mikaboshi. Kunishige’s later household, a bowl instead of a forecast, is a refusal of that room.</p>
  <p>Part 2 opens on the rank. Chapter 116 is “Princess.” Chapter 123 is “Chiaki.” The talks want the vein and a foothold. <span class="spoiler">Chapter 130 dates the handover. Anesthesia is the clan’s kindness so she will not remember the beach. Foresight did not save her from being stationery. It made her valuable enough to mail.</span></p>
  <h2>We do not invent unseen prophecies</h2>
  <p>This essay will not print visions the magazine has not shown. It will say the office is the plot. Akemura is her younger brother, still the friend a smith can trust in the war book, already Magatsumi in the present tense. Official chapters: VIZ / MANGA Plus. Related: <a href="../world/prophecy.html">prophecy</a>, <a href="../world/princess.html">Princess Soga</a>, <a href="../characters/chiaki.html">Chiaki</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/chiaki.html">Chiaki</a><a href="../world/prophecy.html">Prophecy</a><a href="../world/izanami.html">Izanami</a><a href="irishima.html">Irishima</a><a href="index.html">All essays</a><a href="../factions/soga.html">Soga</a></nav>
""",
)

add(
    "fun/enten-oneshot.html",
    "The Enten one-shot",
    "Hokazono’s Tezuka Award one-shot Enten (炎天): Jump Giga Spring 2021. Different kanji, different story, same hunger for a named sword.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Enten one-shot',
    "100th Tezuka Award",
    "The Enten one-shot",
    "炎天",
    "Not 淵天. Not the seventh blade. The short that already wanted a named sword in Jump.",
    """
  <p>Before the weekly, Hokazono placed <em>Enten</em> (炎天) at the 100th Tezuka Awards. It ran in <em>Jump Giga</em> Spring 2021. Different story. Different kanji. The serial’s seventh blade is 淵天. The author page already said this: same hunger for a named sword in a magazine that still sells named swords. Then Giga and Jump shorts: <em>Farewell! Cherry Boy!</em>, <em>Chain</em>, <em>Madogiwa de Amu</em>, <em>Roku no Meiyaku</em>.</p>
  <h2>The serial waits</h2>
  <p>The titles essay notes the patience: the one-shot was already named Enten, and the weekly waits until Volume 9 to put that word on a spine alone. Chapter 83 says the brief cleanly. Volume extras (bathhouse, Soya) are a different pile: the serial already in motion. This page is the pre-serial test. We do not host the one-shot.</p>
  <p>File: <a href="hokazono.html">Hokazono</a>, <a href="oneshots.html">bathhouse extras</a>, <a href="../blades/enten.html">淵天</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="hokazono.html">Hokazono</a><a href="oneshots.html">Volume extras</a><a href="../analysis/titles.html">Titles</a><a href="../blades/enten.html">Enten</a><a href="index.html">Fun</a><a href="../manga/publication.html">Publication</a></nav>
""",
)

add(
    "fun/circulation.html",
    "Circulation",
    "Kagurabachi circulation: Shueisha’s restated numbers from 350,000 in July 2024 to over 4 million by April 2026.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Circulation',
    "4 million · April 2026",
    "Circulation",
    "部数",
    "The meme predicted the opposite. The restated numbers are the joke dying of sales.",
    """
  <p>Shueisha’s restated numbers, because the meme predicted the opposite:</p>
  <ul>
    <li>July 2024: over 350,000 copies (including digital)</li>
    <li>August 2024: over 600,000</li>
    <li>October 2024: over 1 million</li>
    <li>December 2024: over 1.3 million</li>
    <li>May 2025: over 2.2 million</li>
    <li>October 2025: over 3 million sold</li>
    <li>April 2026: over 4 million in circulation</li>
  </ul>
  <p>Chapter 1 was the most-viewed new title on MANGA Plus in its first week. By April 2024 the app had logged over 99 million page views. Next Manga Award, print, 2024. North America: Circana BookScan monthly top 20 adult graphic novels since November 2024. New York Times Graphic Books and Manga bestseller monthly list since December 2024. Eleven Japanese volumes by May 2026. Volume 12 listed for 4 September.</p>
  <p>This page is the count. The publication record is the awards and the anime. We do not list scans. Buy the tankōbon. Official chapters: VIZ / MANGA Plus.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/publication.html">Publication</a><a href="meme.html">Meme</a><a href="../manga/volume-12.html">Volume 12</a><a href="../manga/volumes.html">Volumes</a><a href="index.html">Fun</a><a href="../collectibles/index.html">Collectibles</a></nav>
""",
)

add(
    "manga/volume-12.html",
    "Kagurabachi Volume 12",
    "Kagurabachi Volume 12: solicited 4 September 2026, ISBN 978-4-08-885177-8. Expected to collect Karma through Swordsmith and open the war book.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Volume 12',
    "Solicited · 4 Sep 2026",
    "Volume 12",
    "第12巻",
    "Part 1’s last corridor on paper, then Irishima. The jacket has not been announced.",
    """
  <p>Volume 12 is listed for 4 September 2026, ISBN 978-4-08-885177-8. English TBD. The volume guide expects chapters 106–115, Karma through Swordsmith, then the war book. The jacket has not been announced. Eleven spines are already on the shelf. This one is the solicited close.</p>
  <h2>What the corridor already named</h2>
  <p>Karma. Enten vs. Magatsumi. Tobimune vs. Magatsumi. As a Swordsman. Rock. Kunishige Rokuhira. Swordsmith. <span class="spoiler">Part 1 ends with Enten bisected, Samura spent, Iori holding Tobimune, Chihiro writing notes toward a new Enten, Akemura loose in a body that used to be Yura.</span> Chapter 116 is Princess. The uncollected run through I'm Fine! (130) still lives on the Part 2 page. Chapter 131 is due 6 September 2026. We do not invent its title.</p>
  <p>Circulation by April 2026: 4 million. Buy the tankōbon when it exists. Official chapters: VIZ / MANGA Plus. ISBN table: <a href="volumes.html">volume guide</a>. Sentences: <a href="synopses.html#volume-12">synopses</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="volumes.html">Volume guide</a><a href="synopses.html">Synopses</a><a href="chapter-106.html">Karma</a><a href="chapter-115.html">Swordsmith</a><a href="part-2.html">Part 2</a><a href="publication.html">Publication</a></nav>
""",
)


if __name__ == "__main__":
    print("pages", len(PAGES))
