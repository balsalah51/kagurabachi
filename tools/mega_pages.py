#!/usr/bin/env python3
"""Mega content wave: leftover chapter titles, volume rooms, printed world topics.

Does not invent chapter 118-120 rooms, first-blade identity, or chapter 132 plot.
Chapter 131 title is the Wikipedia / VIZ listing: Tipping Point (転換点).
"""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <script>!function(){try{var m=document.cookie.match(/(?:^|; )kb-theme=(dark|light)/);if(m)document.documentElement.setAttribute("data-theme",m[1])}catch(e){}}()</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
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

PAGES: list[str] = []

VOLS = [
    (1, 8, 1, "Mission", "すべきこと", "Vs. Sojo"),
    (9, 18, 2, "Enten vs. Cloud Gouger", "淵天 VS 刳雲", "Vs. Sojo"),
    (19, 27, 3, "Knight of Darkness", "闇の騎士", "Rakuzaichi"),
    (28, 36, 4, "Equal", "対等", "Rakuzaichi"),
    (37, 46, 5, "Fervent", "熱狂", "Rakuzaichi"),
    (47, 56, 6, "Daybreak", "夜更け / 黎明", "Sword Bearer"),
    (57, 65, 7, "Night Battle", "夜戦", "Sword Bearer"),
    (66, 74, 8, "Dawn", "夜明け", "Sword Bearer"),
    (75, 86, 9, "Enten", "淵天", "Sword Bearer"),
    (87, 95, 10, "The Swordsmen", "剣士たち", "Sword Bearer"),
    (96, 105, 11, "Heroes", "英雄", "Sword Bearer"),
    (106, 115, 12, "Volume 12 (solicited)", "第12巻", "Part 1 close"),
]


def vol_meta(n: int):
    for a, b, num, title, jp, arc in VOLS:
        if a <= n <= b:
            return num, title, jp, arc
    return None, "Uncollected", "", "Seitei War / Part 2"


def write(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    html = (
        HEAD.replace("{title}", title).replace("{desc}", desc)
        + f'<p class="crumb">{crumb}</p>\n'
        + '<header class="page-hero"><div>\n'
        + f'  <p class="kicker">{kicker}</p>\n'
        + f'  <h1>{h1}<span class="jp">{jp}</span></h1>\n'
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + f'<article class="article brief">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    if path.exists():
        raise SystemExit(f"refusing to overwrite {rel}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    PAGES.append(rel)
    print("wrote", rel)


def related(links):
    bits = "".join(f'<a href="{h}">{t}</a>' for h, t in links[:8])
    return f'<nav class="related" aria-label="Related pages">{bits}</nav>'


# Existing rooms for neighbor math (plus new leftovers + 131).
EXISTING = {
    1, 4, 5, 7, 8, 9, 14, 18, 19, 20, 23, 27, 32, 37, 41, 44, 45, 47, 48, 50,
    51, 56, 57, 59, 60, 62, 66, 67, 70, 75, 76, 80, 82, 83, 90, 91, 92, 97, 98,
    99, 100, 104, 105, 106, 108, 109, 110, 113, 114, 115, 116, 117, 121, 122,
    123, 124, 125, 126, 127, 128, 129, 130,
}
SKIP_SOLO = {118, 119, 120}

LEFTOVER = [
    (2, "Heaps", "累累", "Volume 1 still stacking the raid’s leftovers. Bodies, jobs, the street."),
    (3, "Witness", "目撃者", "Char has seen an Enchanted Blade. The hunt gets a pair of eyes."),
    (6, "Peace", "平穏", "A quiet title in a revenge book. The workshop was this before the raid."),
    (10, "Swift", "サクッっと", "The magazine’s joke speed. Volume 2 is already a weather fight."),
    (11, "Awaken", "目覚め", "Someone wakes into the job. Cloud Gouger is already in the city."),
    (12, "Preparations", "支度", "The ACG squad is being built. Chihiro is already late to their brief."),
    (13, "Elite", "精鋭", "Specialists named so the weather sword has an opponent list."),
    (15, "Food", "飯", "The second meal title. Char still has to eat. Sojo’s people eat too."),
    (16, "Silence", "沈黙", "Sojo treats talking as a leak. The title agrees."),
    (17, "Tea", "茶", "The third table title. Before Roar, the book still pours."),
    (21, "Lukewarm", "微温い", "Hiyuki is already in the building. The auction is not hot yet."),
    (22, "Deadlock", "拮抗", "The first of two Deadlocks. Japanese here is 拮抗, later 均衡."),
    (24, "Hunters", "狩人", "The auction house has a hunting vocabulary. Hakuri is not in it yet."),
    (25, "Deal", "取引", "Rakuzaichi as a market sentence. Shinuchi is already listed."),
    (26, "Confidence", "自信", "Hakuri’s word, later. Here it is still someone else’s."),
    (28, "Breach", "突破口", "Volume 4 opener. Equal is the spine. This issue is the hole in the wall."),
    (29, "Selection", "取捨", "What the Storehouse keeps. What the clan throws away."),
    (30, "Intruders", "乱入者", "People who were not invited into the Kura."),
    (31, "Greeting", "挨拶", "The auction house starts answering Hakuri. Chapter 32 will title Wall."),
    (33, "Defend to the Death", "死守", "The Tou and the building. Tenri will spend a stone later."),
    (34, "Duty", "役目", "A Sazanami job title. Hakuri’s version walks out."),
    (35, "Cage", "檻", "Storehouse as a cage, not a religion, for one week."),
    (36, "Geniuses", "天才達", "Volume 4 closer before Fervent. Equal is still the jacket word."),
    (38, "Race", "競合", "After Equal. The Storehouse war is a clock."),
    (39, "Surpass!", "超えろ!!", "The magazine shouts. Chihiro and Hakuri are the pair the jacket already chose."),
    (40, "The Tip", "一端", "One end of the auction. Kyora is still the head."),
    (42, "Everything", "全部", "After Fervent. The building is being spent."),
    (43, "Fulfill", "全う", "A duty title before the curtain. Tenri’s stone is in this corridor."),
    (46, "Unruly Punk", "勝手な野郎", "Volume 5 closer. The auction is over. The next book is Uruha."),
    (49, "Deadlock", "均衡", "The second Deadlock. Japanese is 均衡 this time. Steam Squad just got a grave."),
    (52, "Just the Two of Us", "2人きり", "Samura’s week. Iori is already the reason the house is quiet."),
    (53, "Darkness", "暗がり", "Not chapter 59’s Blackout. A smaller dark."),
    (54, "Friendship", "友情", "Uruha and Samura. The Iai house as ethics, not a tournament."),
    (55, "Fight Alongside", "共闘", "The last title before Daybreak (夜更け). Volume 6 is about to close."),
    (58, "Reunion", "再会", "After Collapse. Not chapter 130’s reunion. This one is still the hotel road."),
    (61, "Night Battle", "夜戦", "Volume 7’s spine word, used as a weekly title."),
    (63, "Car Chase", "車追跡", "The Masumi job is already a vehicle. Iori is the cargo."),
    (64, "Become the Samurai", "ビカム侍", "The English is a loan. Chihiro is copying a closed-eye draw."),
    (65, "Imitate", "見真似", "Volume 7 closer. The Iai lesson is watching, then spending."),
    (68, "Metamorphosis", "変幻", "Hotel week. Hiruhiko’s Play is about to wreck a floor."),
    (69, "The Guy with the Scar", "傷ノ男", "A hotel face title. Kuguri is the classroom."),
    (71, "Contest", "勝負", "After Iai White Purity Style. A match title in a support-blade fight."),
    (72, "Future", "未来", "The first of two Futures. Chapter 112 will reuse the English."),
    (73, "Daybreak", "黎明", "The second Daybreak. Japanese is 黎明, not 夜更け. Volume 8 is Dawn."),
    (74, "Dawn", "夜明け", "Volume 8’s spine word on the last weekly page of the book."),
    (77, "No Longer Relevant", "蚊帳の外", "After Banquet. Someone is outside the net."),
    (78, "Switch", "交代", "Contracts move. Uruha’s false death is already the door."),
    (79, "Threat!!", "曲者!!", "The magazine shouts again. The hotel still has floors."),
    (81, "Core", "主力", "Before Enten vs Tobimune. Volume 9 is already named Enten."),
    (84, "The Wounded", "傷の者たち", "After The Enten. The hotel is a hospital and a morgue."),
    (85, "Open", "開く", "A door title. Owl is already national."),
    (86, "Quickening", "胎動", "Volume 9 closer. Something in the basement is already moving."),
    (87, "Phantoms", "亡霊", "Volume 10 opener. The war’s leftovers have names."),
    (88, "The First Step", "皮切り", "The start of a different cut. Not the first Enchanted Blade."),
    (89, "Battle Chaos", "乱戦", "Headquarters is becoming a street."),
    (93, "Finishing Touches", "仕上げ", "After The Swordsmen. A craft title in a war book."),
    (94, "The Second Arrow", "二の矢", "Volume 10’s late shot. Hokuto is already in the building."),
    (95, "Flood", "横溢", "Volume 10 closer. Magatsumi’s field is a weather of its own."),
    (96, "Urgency", "切迫", "Volume 11 opener. Vessel is the next named job."),
    (101, "Safe Zone", "安全地帯", "After Sword Master. Headquarters still pretends it has one."),
    (102, "What You Need to See", "視るべきモノ", "A seeing title. Samura’s eyes and Chiaki’s office are different tools."),
    (103, "Healing", "再生", "Suzaku’s week in the index. Not Yukisada’s regeneration."),
    (107, "This Moment", "この一瞬", "After Karma. Enten vs Magatsumi is the next title."),
    (111, "Apex", "頂", "After As a Swordsman. The top of a fight that is already lost."),
    (112, "Future", "未来", "The second Future. Japanese matches chapter 72. Part 1 is two issues from Swordsmith."),
]


def ch_note(n, en, jp):
    vnum, vtitle, _vjp, arc = vol_meta(n)
    vol = f"Volume {vnum}, <em>{vtitle}</em>" if vnum and vnum < 12 else "the uncollected run"
    if n <= 18:
        extra = "Early titles are objects and meals: Heaps, Peace, Food, Tea. The swords get their names on the page later."
        links = [("../arcs/vs-sojo.html", "Vs. Sojo"), ("../world/food.html", "Meals")]
    elif n <= 46:
        extra = "The auction speaks in architecture and family: Storehouse, Deal, Equal, Fervent, The Curtain Falls."
        links = [("../arcs/rakuzaichi.html", "Rakuzaichi"), ("../world/storehouse.html", "Storehouse")]
    elif n <= 115:
        extra = "The long book names people, then puts quotation marks on the press’s words."
        links = [("../arcs/sword-bearer.html", "Sword Bearer"), ("../world/hotel.html", "Hotel")]
    else:
        extra = "Part 2 opens on a rank and a place. Princess. Talks. Smelting. Fire."
        links = [("../arcs/seitei-war.html", "Seitei War"), ("part-2.html", "Part 2")]
    if n in (22, 49):
        extra += " Two weekly titles share the English word Deadlock; the Japanese column differs."
        links.append(("../analysis/titles.html", "Titles"))
    if n in (56, 73):
        extra += " Two weekly titles share Daybreak; 夜更け and 黎明 are not the same word."
        links.append(("../analysis/titles.html", "Titles"))
    if n in (72, 112):
        extra += " Two weekly titles share Future. The Japanese is 未来 both times."
        links.append(("../analysis/titles.html", "Titles"))
    if n in (15, 17, 6):
        links = [("../world/food.html", "Meals"), ("../characters/char.html", "Char"), ("../arcs/vs-sojo.html", "Vs. Sojo")]
    if n in (61, 74):
        extra += " The spine later borrows this weekly word."
    return extra, links, vol, arc


def neighbors(n, titles):
    rooms = sorted(EXISTING | set(titles) | {131})
    rooms = [x for x in rooms if x not in SKIP_SOLO]
    if n not in rooms:
        return None, None
    i = rooms.index(n)
    prev = rooms[i - 1] if i else None
    nxt = rooms[i + 1] if i < len(rooms) - 1 else None
    return prev, nxt


def chapter_room(n, en, jp, lede, extra_body=None):
    extra, links, vol, arc = ch_note(n, en, jp)
    titles = {x[0]: x[1] for x in LEFTOVER}
    titles[131] = "Tipping Point"
    prev, nxt = neighbors(n, titles)
    nav = []
    if prev:
        nav.append((f"chapter-{prev}.html", f"Ch. {prev}"))
    nav.append(("chapters.html", "Chapter index"))
    if nxt:
        nav.append((f"chapter-{nxt}.html", f"Ch. {nxt}"))
    nav.extend(links)
    body = extra_body or f"""
  <p>Read it official: {VIZ}. This page is a room for the weekly title, not a substitute. Chapter {n} is “{en}” ({jp}). It sits in {vol}, {arc}.</p>
  <h2>What the title is doing</h2>
  <p>{extra} The <a href="chapters.html">chapter index</a> is the authority for wording. When English and Japanese disagree, the Japanese column is the magazine’s word.</p>
  <p>Official chapters only. We do not host them. File the commute on the <a href="../arcs/index.html">arc map</a> and the <a href="synopses.html">volume synopses</a>.</p>
    {related(nav)}
"""
    write(
        f"manga/chapter-{n}.html",
        f"Kagurabachi Chapter {n} “{en}”",
        f"Kagurabachi chapter {n}, {en} ({jp}): a room for the weekly title. Official reading on VIZ and MANGA Plus.",
        f'<a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter {n}',
        f"{vol} · {arc}",
        f"Chapter {n} - “{en}”",
        jp,
        lede,
        body,
    )


def main():
    for row in LEFTOVER:
        chapter_room(*row)

    chapter_room(
        131,
        "Tipping Point",
        "転換点",
        "Jump 2026 #41. VIZ dated 6 September 2026. The war book’s next weekly word.",
        extra_body=f"""
  <p>Read it official: {VIZ}. Chapter 131 is titled “Tipping Point” (転換点). VIZ’s listing is 6 September 2026. Weekly Shōnen Jump 2026 issue 41. This page is a publication door, not a substitute and not a leak desk.</p>
  <h2>What we print</h2>
  <p>Chapter 130, “I'm Fine!,” put tamahagane on the floor and Chiaki in the room. Chapter 131 is the next magazine word. We file the title from the public chapter list (Wikipedia’s English rendering matches the VIZ chapter number). We do not invent the panels. The <a href="part-2.html">Part 2 page</a> will take new sentences when this desk has read the official chapter.</p>
  <p>Chapter 132 was scheduled for the 42/43 combined issue (14 September 2026) and was announced on hiatus for the author’s sudden illness. The official account said he had already recovered. Continuation: Jump 2026 issue 44, on sale 28 September 2026. File: <a href="../fun/september-2026-rest.html">the September rest</a>.</p>
    {related([
        ("chapter-130.html", "Ch. 130"),
        ("chapters.html", "Chapter index"),
        ("part-2.html", "Part 2"),
        ("../fun/september-2026-rest.html", "September rest"),
        ("../world/smelting.html", "Smelting"),
        ("../world/princess.html", "Princess"),
    ])}
""",
    )

    volumes()
    world()
    fun_analysis()
    print("total", len(PAGES))


def volumes():
    data = [
        (1, "Mission", "すべきこと", "2024-02-02", "978-4-08-883819-9", "2024-11-05", "978-1-9747-4724-5", "1–8",
         "Chihiro Rokuhira", "jp-vol1.webp",
         "Chihiro takes Enten into Tokyo after a sighting. Three years after the raid, he and Shiba work the underworld. Char says she has seen an Enchanted Blade. Madoka, Azami, and Sojo’s first shadow. The bowl is already on the table.",
         "Rusty ruby / asphalt red, white title, Kuro overhead. The law of the series in one jacket."),
        (2, "Enten vs. Cloud Gouger", "淵天 VS 刳雲", "2024-05-02", "978-4-08-883880-9", "2025-02-04", "978-1-9747-5271-3", "9–18",
         "Chihiro, Sojo", "jp-vol2.webp",
         "The weather sword and the household blade share a street. True Realm, Roar, Cloud Gouger bisected. Sojo is a customer, not Hishaku. The ACG squad is spent around him.",
         "Cyan invited onto the triad because Cloud Gouger is on stage."),
        (3, "Knight of Darkness", "闇の騎士", "2024-07-04", "978-4-08-884116-8", "2025-05-06", "978-1-9747-5478-6", "19–27",
         "Chihiro, Hiyuki, Kyora", "jp-vol3.webp",
         "Hiyuki arrives. The 208th Rakuzaichi is being built. Mr. Inazuma sits in this book. Volume 3 wears chapter 19’s title.",
         "Flame-orange against auction green-black."),
        (4, "Equal", "対等", "2024-10-04", "978-4-08-884209-7", "2025-08-05", "978-1-9747-5607-0", "28–36",
         "Chihiro, Hakuri", "jp-vol4.webp",
         "Hakuri and the Storehouse. Two figures at storehouse dusk. The clan called him defective stock. Chihiro does not pick him up as a tool.",
         "The jacket is the brief: they meet in the middle."),
        (5, "Fervent", "熱狂", "2024-12-04", "978-4-08-884348-3", "2025-11-04", "978-1-9747-5891-3", "37–46",
         "Chihiro, Kyora, Hakuri, Hiyuki", "jp-vol5.webp",
         "The Storehouse war. The Curtain Falls. Unruly Punk closes the auction book. Kyora dies as himself long enough to admit the son.",
         "A group jacket: the cast the building spent."),
        (6, "Daybreak", "夜更け / 黎明", "2025-03-04", "978-4-08-884399-5", "2026-02-03", "978-1-9747-6287-3", "47–56",
         "Uruha, Samura, Chihiro, Hiruhiko", "jp-vol6.webp",
         "Uruha. The Kokugoku Steam Squad. Interception. Samura. The spine holds two Japanese mornings: 夜更け and 黎明.",
         "The long book begins as a name and a grave."),
        (7, "Night Battle", "夜戦", "2025-05-02", "978-4-08-884413-8", "2026-05-05", "978-1-9747-6574-4", "57–65",
         "Samura, Chihiro, Iori", "jp-vol7.webp",
         "Collapse, Blackout, Resurrection, Iori. The Masumi job. Become the Samurai. Imitate. Volume 7 wears a weekly title as a spine.",
         "Night as a curriculum, not a mood."),
        (8, "Dawn", "夜明け", "2025-07-04", "978-4-08-884566-1", "2026-08-04", "978-1-9747-1650-0", "66–74",
         "Chihiro, Iori, Hiruhiko", "jp-vol8.webp",
         "Truth. Kyoto Bloodshed Hotel. Iai White Purity Style. Daybreak as 黎明, then Dawn. Owl will hang over the silhouette.",
         "A hotel under a national bird."),
        (9, "Enten", "淵天", "2025-10-03", "978-4-08-884653-8", "2026-11-03", "978-1-9747-6845-5", "75–86",
         "Chihiro", "jp-vol9.webp",
         "Illusion, Banquet, Enten vs Tobimune, The Enten. Volume 9 is the seventh blade as a jacket word. Quickening closes the book.",
         "A single-figure icon. The household made large."),
        (10, "The Swordsmen", "剣士たち", "2026-01-05", "978-4-08-884740-5", "TBD", "", "87–95",
         "Natsuki, Hokuto, Uruha, Yura", "jp-vol10.webp",
         "Phantoms, Kiri, Natsuki, The Swordsmen, Flood. Blades before factions. Lightning Menace on a four-man war photograph.",
         "A group jacket: the state’s swordsman in the war photo."),
        (11, "Heroes", "英雄", "2026-05-01", "978-4-08-885102-0", "TBD", "", "96–105",
         "Chihiro, goldfish, snow", "jp-vol11.webp",
         "Urgency, Vessel, Hagiwara, Strongest, Sword Master, Heroes, Transformation. Quotes on the press’s words. Snow, Aka and Kuro.",
         "Snow invited onto the triad. The goldfish stay."),
    ]
    for num, title, jp, jpdate, isbn_jp, endate, isbn_en, chs, faces, cover, synopsis, palette in data:
        en_line = f"English {endate}, ISBN {isbn_en}." if isbn_en else "English TBD."
        nxt = num + 1
        prev = num - 1
        nav = [("volumes.html", "Volume guide"), ("synopses.html", "Synopses"), ("covers.html", "Covers")]
        if prev >= 1:
            nav.insert(0, (f"volume-{prev}.html", f"Vol. {prev}"))
        if nxt <= 11:
            nav.append((f"volume-{nxt}.html", f"Vol. {nxt}"))
        elif nxt == 12:
            nav.append(("volume-12.html", "Vol. 12"))
        write(
            f"manga/volume-{num}.html",
            f"Kagurabachi Volume {num} {title} | Jump Comics",
            f"Kagurabachi Volume {num}, {title}: chapters {chs}. Japan {jpdate}, ISBN {isbn_jp}. {en_line}",
            f'<a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Volume {num}',
            f"Jump Comics · Ch. {chs}",
            f"Volume {num}: {title}",
            jp,
            synopsis,
            f"""
  <figure class="shot">
      <img src="../assets/covers/{cover}" alt="Kagurabachi Volume {num} Japanese jacket">
      <figcaption>{palette} Buy the tankōbon. Official chapters: VIZ / MANGA Plus.</figcaption>
    </figure>
  <p>Japan {jpdate}, ISBN {isbn_jp}. {en_line} Jacket faces: {faces}. Chapters {chs}. Longer sentences: <a href="synopses.html#volume-{num}">synopsis</a>. The ISBN table: <a href="volumes.html">volume guide</a>.</p>
  <h2>What the spine is holding</h2>
  <p>{synopsis} Palette note: {palette} Extras the magazine does not carry live on <a href="omake.html">volume extras</a>.</p>
  <p>Chapter rooms for this book are linked from the <a href="chapters.html">index</a>. We do not host chapters.</p>
    {related(nav)}
""",
        )


def world():
    rooms = [
        ("world/owl.html", "Owl (梟) | Tobimune Technique | Kagurabachi",
         "Owl, Tobimune’s national reconnaissance: giant eyes, range versus resolution.",
         "Tobimune · 梟", "Owl", "梟",
         "Hang it high and you hear Enchanted Blade noise across the country.",
         f"""
  <p>Owl (梟) is Tobimune’s reconnaissance. Giant eyes. Range versus resolution: hang it high and you hear Enchanted Blade noise across Japan; pull it closer and the picture sharpens. After Senkutsuji, Samura hangs Owl over the country. Volume 8’s jacket is a hotel silhouette under that bird.</p>
  <h2>Support, not a weather report</h2>
  <p>Chihiro says Tobimune was forged for support. Crow is a swap. Suzaku is fire that can keep a person. Owl is how the long book knows where the steel is. Essay: <a href="../analysis/owl.html">Owl over Japan</a>. Kit: <a href="crow.html">Crow</a>, <a href="suzaku.html">Suzaku</a>, <a href="../blades/tobimune.html">Tobimune</a>.</p>
    {related([("crow.html", "Crow"), ("suzaku.html", "Suzaku"), ("../analysis/owl.html", "Essay"), ("../blades/tobimune.html", "Tobimune")])}
"""),
        ("world/play.html", "Play (遊) | Kumeyuri Technique | Kagurabachi",
         "Play, Kumeyuri’s telekinesis: fluency scales with respect. Destructive Play is contempt as demolition.",
         "Kumeyuri · 遊", "Play", "遊",
         "Move the set. Respect makes it smoother. Contempt wrecks the hotel.",
         f"""
  <p>Play (遊) is Kumeyuri’s second named technique. Move objects. Fluency scales with respect for the room. Hiruhiko’s reading is the inverse: Destructive Play, the same art spent as demolition. The Kyoto Bloodshed Hotel loses upper floors to it. Banquet takes the senses; Play takes the furniture.</p>
  <h2>Two briefs, one steel</h2>
  <p>Uruha is the war bearer. Hiruhiko signs after Samura’s false death of Uruha. Essay: <a href="../analysis/play.html">Play</a>. Hallucination room: <a href="banquet-art.html">Banquet</a>. Blade: <a href="../blades/kumeyuri.html">Kumeyuri</a>. Official chapters: VIZ / MANGA Plus.</p>
    {related([("banquet-art.html", "Banquet"), ("destructive-play.html", "Destructive Play"), ("../analysis/play.html", "Essay"), ("../blades/kumeyuri.html", "Kumeyuri")])}
"""),
        ("world/flame-bone.html", "Flame Bone of the Starving | Hiyuki | Kagurabachi",
         "Hiyuki Kagari’s hereditary flaming skeleton, licensed by the Kamunabi, stood next to Enchanted Blades in the text.",
         "Hiyuki · Gasha no Enkotsu", "Flame Bone", "Gasha no Enkotsu",
         "A permission slip you can see through the body.",
         f"""
  <p>Flame Bone of the Starving (Gasha no Enkotsu) is Hiyuki Kagari’s hereditary art: pieces of a giant flaming skeleton. Authorization up to a line, ribs, torso, as if the Kamunabi issued a license for how much she can wear to work. The text will stand it next to an Enchanted Blade. Chapter 19 titles her arrival. Chapter 20 titles the Kamunabi’s weapon.</p>
  <h2>Not a seventh sword</h2>
  <p>Tafuku’s duel domain is how that weapon is allowed to work in a city. Essay: <a href="../analysis/flame-bone.html">Flame Bone</a>. Person: <a href="../characters/hiyuki.html">Hiyuki</a>. Room: <a href="duel-domain.html">duel domain</a>.</p>
    {related([("../analysis/flame-bone.html", "Essay"), ("../characters/hiyuki.html", "Hiyuki"), ("../manga/chapter-19.html", "Ch. 19"), ("duel-domain.html", "Domain")])}
"""),
        ("world/lightning-menace.html", "Lightning Menace (Raiku) | Natsuki | Kagurabachi",
         "Natsuki Misaka’s Lightning Menace: voltage in the body, not Mei. Volume 10 jacket.",
         "Natsuki · 雷躯", "Lightning Menace", "雷躯",
         "The family rhyme without Datenseki.",
         f"""
  <p>Lightning Menace (Raiku, 雷躯) is Natsuki Misaka’s innate art: voltage in the body, not Cloud Gouger’s Mei. He is Ibuki’s brother, a Kamunabi squadron leader, a Kumeyuri candidate who was not chosen. Volume 10’s jacket puts him with Hokuto, Uruha, and Yura.</p>
  <h2>Not the weather sword</h2>
  <p>Mei is a bolt with a charge delay. Raiku is a person. Chapter 91 titles his name. File: <a href="../characters/natsuki.html">Natsuki</a>, <a href="../characters/ibuki.html">Ibuki</a>, <a href="mei.html">Mei</a>.</p>
    {related([("../characters/natsuki.html", "Natsuki"), ("../manga/chapter-91.html", "Ch. 91"), ("mei.html", "Mei"), ("../manga/volume-10.html", "Volume 10")])}
"""),
        ("world/twilight-wave.html", "Twilight Wave (Hagure) | Kuguri | Kagurabachi",
         "Kuguri’s Twilight Wave: bank motion and heat, spend later. Printed as 破暮.",
         "Kuguri · 破暮", "Twilight Wave", "破暮",
         "Bank the motion. Spend it when the hotel needs a classroom.",
         f"""
  <p>Twilight Wave (Hagure, 破暮) is Kuguri’s innate art: bank kinetic energy and heat, spend later. He is Hishaku. Chihiro copies Iai by watching him and the house style at the Kyoto Bloodshed Hotel. The guy with the scar is a weekly title in that corridor.</p>
  <p>File: <a href="../characters/kuguri.html">Kuguri</a>, <a href="iai.html">Iai</a>, <a href="../manga/chapter-70.html">chapter 70</a>. Official chapters: VIZ / MANGA Plus.</p>
    {related([("../characters/kuguri.html", "Kuguri"), ("iai.html", "Iai"), ("../manga/chapter-69.html", "Ch. 69"), ("hotel.html", "Hotel")])}
"""),
        ("world/blood-crane.html", "Blood Crane (Chizuru) | Hiruhiko | Kagurabachi",
         "Hiruhiko’s Blood Crane: origami that cuts and lifts. Goes quiet when Kumeyuri is signed.",
         "Hiruhiko · 血鶴", "Blood Crane", "血鶴",
         "The train art. Then the banquet steel is louder.",
         f"""
  <p>Blood Crane (Chizuru, 血鶴) is Hiruhiko’s innate origami: it cuts and lifts. The train to Kokugoku, the kabuki house. Then he picks up Kumeyuri and the crane is no longer the loudest thing in the room. The Steam Squad dies in that commute.</p>
  <p>File: <a href="../characters/hiruhiko.html">Hiruhiko</a>, <a href="train.html">the train</a>, <a href="play.html">Play</a>, <a href="../factions/steam-squad.html">Steam Squad</a>.</p>
    {related([("../characters/hiruhiko.html", "Hiruhiko"), ("train.html", "Train"), ("play.html", "Play"), ("../manga/chapter-50.html", "Ch. 50")])}
"""),
        ("world/smoke-axe.html", "Smoke Axe | Fushimi | Kagurabachi",
         "Fushimi’s Smoke Axe: cut with smoke between hands. Named with the Steam Squad, buried the same week.",
         "Kokugoku · 煙斧", "Smoke Axe", "煙斧",
         "Named. Competent. Insufficient.",
         f"""
  <p>Smoke Axe (煙斧) is Fushimi’s art: cut with smoke between the hands. He is Kokugoku Steam Squad. They beat Hishaku-hired Datenseki troops. Then Hiruhiko arrives. Chapter 48 titles the squad. They get a name and a grave in the same week.</p>
  <p>File: <a href="../characters/fushimi.html">Fushimi</a>, <a href="../factions/steam-squad.html">Steam Squad</a>, <a href="../manga/chapter-48.html">chapter 48</a>, <a href="kokugoku.html">Kokugoku</a>.</p>
    {related([("../characters/fushimi.html", "Fushimi"), ("../factions/steam-squad.html", "Steam Squad"), ("../manga/chapter-48.html", "Ch. 48"), ("blood-crane.html", "Blood Crane")])}
"""),
        ("world/kuro-shred.html", "Kuro: Shred (涅千) | Enten | Kagurabachi",
         "Kuro: Shred, many small black fish, many small cuts, more spirit, less strain on the body.",
         "Enten · 涅千", "Kuro: Shred", "涅千",
         "The workhorse spent as a flock.",
         f"""
  <p>Kuro: Shred (涅千) is the extension of <a href="kuro.html">Kuro</a>: many small black fish, many small cuts, more spirit, less strain on the body. The daily language of Enten, subdivided. Not True Realm. Not a transformation.</p>
  <p>Parent kit: <a href="../blades/enten.html">Enten</a>. Sisters: <a href="aka.html">Aka</a>, <a href="nishiki.html">Nishiki</a>. Official chapters: VIZ / MANGA Plus.</p>
    {related([("kuro.html", "Kuro"), ("../blades/enten.html", "Enten"), ("aka.html", "Aka"), ("techniques.html", "Catalog")])}
"""),
        ("world/mei-shred.html", "Mei: Shred | Cloud Gouger | Kagurabachi",
         "Mei: Shred, Chihiro’s last use of a dying Cloud Gouger, black because the steel is dying.",
         "Cloud Gouger · dark power", "Mei: Shred", "Mei",
         "Black because the blade is dying.",
         f"""
  <p>Mei: Shred is Chihiro’s last spend of a dying Cloud Gouger. Black because the steel is dying: the same dark-power rule that later paints Samura’s flames. Sojo found cloaked Mei first. Chihiro found the last inch.</p>
  <p>Parent: <a href="mei.html">Mei</a>. Dying contract: <a href="../blades/cloud-gouger.html">Cloud Gouger</a>. Rule: <a href="dark-power.html">dark power</a>.</p>
    {related([("mei.html", "Mei"), ("cloaked-mei.html", "Cloaked Mei"), ("dark-power.html", "Dark power"), ("../blades/cloud-gouger.html", "Cloud Gouger")])}
"""),
        ("world/cloaked-mei.html", "Cloaked Mei | Cloud Gouger | Kagurabachi",
         "Cloaked Mei: wear the lightning instead of throwing it. Sojo finds that reading first.",
         "Cloud Gouger · 鳴", "Cloaked Mei", "Mei",
         "Wear the bolt. The pause is still the tell.",
         f"""
  <p>Cloaked Mei is the extension of <a href="mei.html">Mei</a>: wear the lightning instead of throwing it. Sojo finds that reading first. The charge delay is still the opening. Not an unofficial name invented here; the catalog already calls it cloaked Mei.</p>
  <p>Customer: <a href="../characters/sojo.html">Sojo</a>. Blade: <a href="../blades/cloud-gouger.html">Cloud Gouger</a>. Last spend: <a href="mei-shred.html">Mei: Shred</a>.</p>
    {related([("mei.html", "Mei"), ("mei-shred.html", "Mei: Shred"), ("../characters/sojo.html", "Sojo"), ("yui.html", "Yui")])}
"""),
        ("world/nishiki-support.html", "Nishiki: Support | Enten | Kagurabachi",
         "Nishiki: Support, the catalog’s last Enten line: the cloak spent as help, not fashion.",
         "Enten · 錦", "Nishiki: Support", "錦",
         "The purpose showing through the support kit.",
         f"""
  <p>The technique catalog lists Kuro, Kuro: Shred, Aka, Nishiki, Nishiki: Support. True Realm: Magatsumi’s death. Nishiki: Support is the cloak spent as help. Enten’s brief is fewer blades, not a louder coat.</p>
  <p>Parent: <a href="nishiki.html">Nishiki</a>. Purpose: <a href="../analysis/enten-purpose.html">what Enten was forged for</a>. Blade: <a href="../blades/enten.html">Enten</a>.</p>
    {related([("nishiki.html", "Nishiki"), ("../analysis/enten-purpose.html", "Purpose"), ("kuro.html", "Kuro"), ("../blades/enten.html", "Enten")])}
"""),
        ("world/destructive-play.html", "Destructive Play | Kumeyuri | Kagurabachi",
         "Destructive Play: Hiruhiko’s contempt as demolition. Same technique as Play, spent as a wrecking ball.",
         "Kumeyuri · 遊", "Destructive Play", "遊",
         "Not a new named art. The same Play, inverted.",
         f"""
  <p>Destructive Play is not a second named technique. It is <a href="play.html">Play</a> spent as demolition because Hiruhiko does not respect objects. The Kyoto Bloodshed Hotel loses upper floors. Uruha never needed that reading. Samura later takes the steel back.</p>
  <p>Blade: <a href="../blades/kumeyuri.html">Kumeyuri</a>. Person: <a href="../characters/hiruhiko.html">Hiruhiko</a>. Place: <a href="hotel.html">hotel</a>.</p>
    {related([("play.html", "Play"), ("banquet-art.html", "Banquet"), ("../characters/hiruhiko.html", "Hiruhiko"), ("hotel.html", "Hotel")])}
"""),
        ("world/black-suzaku.html", "Black Suzaku | Tobimune | Kagurabachi",
         "Black Suzaku: the life-for-power rule with the lights off. Strong enough to argue with Malediction.",
         "Tobimune · dark power", "Black Suzaku", "雀",
         "The same flames at the brink.",
         f"""
  <p>Black Suzaku is Suzaku at the brink: the dark-power rule that painted Mei: Shred when Cloud Gouger was dying. <span class="spoiler">When Magatsumi breaks Enten, Samura’s flames go black. They pause the disintegration. He buys Chihiro a corridor and dies holding Magatsumi back.</span></p>
  <p>Parent: <a href="suzaku.html">Suzaku</a>. Essay: <a href="../analysis/suzaku.html">the cut that keeps</a>. Rule: <a href="dark-power.html">dark power</a>.</p>
    {related([("suzaku.html", "Suzaku"), ("../analysis/suzaku.html", "Essay"), ("dark-power.html", "Dark power"), ("../characters/samura.html", "Samura")])}
"""),
        ("world/external-crow.html", "External Crow | Tobimune | Kagurabachi",
         "External Crow: move other people the way Crow swaps the wielder with a feather.",
         "Tobimune · 鴉", "External Crow", "鴉",
         "The feathers have to exist first.",
         f"""
  <p>External Crow is Crow spent on other people: trade their place with a feather already laid. It looks like teleportation until you notice the plumes have to exist first. Samura fights by sound. The feathers are how a blind man is already standing where you meant to cut.</p>
  <p>Parent: <a href="crow.html">Crow</a>. Blade: <a href="../blades/tobimune.html">Tobimune</a>. Not Shiba’s <a href="teleport.html">teleport</a>.</p>
    {related([("crow.html", "Crow"), ("owl.html", "Owl"), ("../blades/tobimune.html", "Tobimune"), ("teleport.html", "Teleport")])}
"""),
        ("world/external-suzaku.html", "External Suzaku | Tobimune | Kagurabachi",
         "External Suzaku: the support brief spent on the world. Kill the contract, keep the person.",
         "Tobimune · 雀", "External Suzaku", "雀",
         "Heal the world instead of the self.",
         f"""
  <p>External Suzaku is Suzaku spent outward. After the war Samura taught the flames to raise the dead so a Lifelong Contract can die and the person can walk. Uruha wakes in a morgue with Crimson Recital limping back. That is the support blade doing support.</p>
  <p>Parent: <a href="suzaku.html">Suzaku</a>. Contracts: <a href="contracts.html">Lifelong Contracts</a>. Uruha: <a href="../characters/uruha.html">Uruha</a>.</p>
    {related([("suzaku.html", "Suzaku"), ("black-suzaku.html", "Black Suzaku"), ("contracts.html", "Contracts"), ("../analysis/suzaku.html", "Essay")])}
"""),
        ("world/dragonfly.html", "Dragonfly (蜻) | Magatsumi | Kagurabachi",
         "Dragonfly, Magatsumi’s wing shapes and directional blast. Hiyuki can mitigate with Flame Bone.",
         "Magatsumi · 蜻", "Dragonfly", "蜻",
         "Wings as a blast. Blades can block.",
         f"""
  <p>Dragonfly (蜻) is printed on the technique catalog as Magatsumi kit: wing shapes, directional blast. Hiyuki can mitigate with Flame Bone; Enchanted Blades can block. This page does not invent further Magatsumi names.</p>
  <p>Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Shinuchi as a job title: <a href="shinuchi.html">Shinuchi</a>. Flower field: <a href="symbols.html">symbols</a>.</p>
    {related([("../blades/magatsumi.html", "Magatsumi"), ("shinuchi.html", "Shinuchi"), ("flame-bone.html", "Flame Bone"), ("techniques.html", "Catalog")])}
"""),
        ("world/honryo.html", "True Realm (Honryō) | Kagurabachi",
         "True Realm, Honryō: when the wielder’s intent locks with the steel. Not a Super Saiyan form.",
         "Sorcery · 本領", "True Realm", "本領",
         "The brief, said with the whole nervous system.",
         f"""
  <p>True Realm (Honryō, 本領) is when the wielder’s intent locks with the Enchanted Blade. Chapter 14 titles it. Enten’s True Realm is Magatsumi’s death. Chihiro reaches it first against Sojo, not because he is louder, because he means the cut. Sojo wanted Cloud Gouger to gain slaughter.</p>
  <p>Essay: <a href="../analysis/true-realm.html">True Realm</a>. Chapter: <a href="../manga/chapter-14.html">14</a>. Sorcery: <a href="sorcery.html">sorcery</a>.</p>
    {related([("../analysis/true-realm.html", "Essay"), ("../manga/chapter-14.html", "Ch. 14"), ("../blades/enten.html", "Enten"), ("sorcery.html", "Sorcery")])}
"""),
        ("world/mako.html", "Mako (魔咬) | Bingo | Kagurabachi",
         "Bingo’s Mako: lion-dancer lucky charms, stacked weight on destroyers, eats corpses, gets sleepy.",
         "Hishaku · 魔咬", "Mako", "魔咬",
         "A charm that eats. Then he sleeps.",
         f"""
  <p>Mako (魔咬) is Bingo’s printed art: lion-dancer lucky charms, stacked weight on destroyers. He eats corpses and gets sleepy. He is one of eight named Hishaku. Two remain unnamed. Sojo is not in this list.</p>
  <p>Person: <a href="../characters/bingo.html">Bingo</a>. Org: <a href="../factions/hishaku.html">Hishaku</a>. Register: <a href="register.html">name register</a>.</p>
    {related([("../characters/bingo.html", "Bingo"), ("../factions/hishaku.html", "Hishaku"), ("register.html", "Register"), ("techniques.html", "Catalog")])}
"""),
        ("world/title-collisions.html", "Repeated Kagurabachi Titles | Daybreak, Deadlock, Future",
         "Two Daybreaks, two Deadlocks, two Futures: the Japanese column is the magazine’s word.",
         "Index · collisions", "Title collisions", "重題",
         "The English search word is not always the magazine’s word.",
         f"""
  <p>The chapter index already warns: “Daybreak” lands on 夜更け and 黎明. Two different “Deadlock”s (拮抗, 均衡). Two different “Future”s (未来 both times). This room is the collision list so a search does not merge them.</p>
  <ul>
    <li>Daybreak: <a href="../manga/chapter-56.html">56 夜更け</a> and <a href="../manga/chapter-73.html">73 黎明</a></li>
    <li>Deadlock: <a href="../manga/chapter-22.html">22 拮抗</a> and <a href="../manga/chapter-49.html">49 均衡</a></li>
    <li>Future: <a href="../manga/chapter-72.html">72</a> and <a href="../manga/chapter-112.html">112</a></li>
  </ul>
  <p>Essay: <a href="../analysis/titles.html">titles</a>. Authority: <a href="../manga/chapters.html">chapter index</a>.</p>
    {related([("../analysis/titles.html", "Titles"), ("../manga/chapters.html", "Index"), ("../manga/chapter-56.html", "Ch. 56"), ("../fun/chapter-titles.html", "Title desk")])}
"""),
        ("world/irishima-talks.html", "The Irishima Talks | Chapters 117–121 | Kagurabachi",
         "The Irishima Talks: four numbered pieces and END. 118–120 stay in the table, not as solo rooms.",
         "Part 2 · 杁島会談", "The Irishima Talks", "杁島会談",
         "117 is the door. 121 is END. The middle three stay in the index.",
         f"""
  <p>Chapters 117–121 are one negotiation with five weekly titles: The Irishima Talks, Parts 2–4, then END. Japan wants the vein. The Mikaboshi want Irishima and a foothold. This site gives 117 and 121 their own rooms. 118, 119, and 120 stay linked only as table rows so the middle of a talk is not three stub essays.</p>
  <p>Door: <a href="../manga/chapter-117.html">117</a>. End: <a href="../manga/chapter-121.html">121</a>. Island: <a href="irishima.html">Irishima</a>. Essay: <a href="../analysis/irishima.html">the talks</a>. Part 2: <a href="../manga/part-2.html">the forge</a>.</p>
    {related([("../manga/chapter-117.html", "Ch. 117"), ("../manga/chapter-121.html", "Ch. 121"), ("irishima.html", "Irishima"), ("../analysis/irishima.html", "Essay")])}
"""),
        ("world/malediction.html", "The Malediction | Magatsumi | Kagurabachi",
         "The Malediction: Magatsumi’s national sin. Enten’s True Realm is this sword’s death.",
         "Seitei War · Magatsumi", "The Malediction", "呪禍",
         "The reason Enten exists.",
         f"""
  <p>The Malediction is Magatsumi’s wartime crime, the thing Samura tried to kill by killing the men who won. Enten’s True Realm is Magatsumi’s death. Essay: <a href="../analysis/malediction.html">Malediction</a>. Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. War: <a href="../arcs/seitei-war.html">Seitei War</a>.</p>
  <p>This page does not invent a first-blade name. The first Enchanted Blade is still unnamed after chapter 131’s listing. File: <a href="first-blade.html">the first blade</a>.</p>
    {related([("../analysis/malediction.html", "Essay"), ("../blades/magatsumi.html", "Magatsumi"), ("honryo.html", "True Realm"), ("first-blade.html", "First blade")])}
"""),
    ]
    # Fix the blood-crane typo if I left a broken href - I see I have a syntax error in blood-crane
    # I'll fix in the list: `"<p>File: <a href="../characters/hiruhiko.html">Hiruhiko</a>, <a href="train.html", "Train"),` 
    # That's broken. Need to fix after write... I'll fix the string now by rewriting that room after.
    for rel, title, desc, kicker, h1, jp, lede, body in rooms:
        crumb_label = "World"
        write(
            rel, title, desc,
            f'<a href="../index.html">Archive</a> / <a href="index.html">{crumb_label}</a> / {h1}',
            kicker, h1, jp, lede, body,
        )


def fun_analysis():
    write(
        "fun/september-2026-rest.html",
        "Kagurabachi September 2026 Rest | Chapter 132 Delay",
        "Official hiatus: Jump 2026 combined 42/43 skipped after Hokazono’s illness. Chapter 132 due issue 44, 28 September 2026.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / September rest',
        "Jump 42/43 · recovered",
        "The September rest",
        "休載",
        "A sudden illness. An official recovery note. Issue 44, 28 September.",
        f"""
  <p>The official Kagurabachi account announced that serialization scheduled for Weekly Shōnen Jump 2026 issue 42/43 combined (on sale 14 September) would rest because of the author’s sudden illness. The same notice said Takeru Hokazono had already recovered. Continuation: issue 44, on sale 28 September 2026. That is chapter 132’s door. We do not invent its title.</p>
  <h2>Two rests in one year</h2>
  <p>The first 2026 rest followed chapter 126, “Fire”: a announced month so the kiln could stay honest. Ironworks returned 23 August. This September skip is a health notice with a printed return date. File the summer month on <a href="hiatus.html">the 2026 rest</a>. Chapter 131, “Tipping Point,” already printed 6 September. Official reading: {VIZ}.</p>
    {related([("hiatus.html", "Summer rest"), ("../manga/chapter-131.html", "Ch. 131"), ("../manga/publication.html", "Publication"), ("hokazono.html", "Hokazono")])}
""",
    )
    write(
        "fun/chapter-titles.html",
        "Kagurabachi Chapter Titles | Meals, Names, Quotes",
        "How Kagurabachi titles work: objects and meals, then names, then quotation marks on the press.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Titles',
        "Index voice",
        "Chapter titles",
        "題",
        "The title language is the book’s method in miniature.",
        f"""
  <p>Early chapters are objects and meals: Heaps, A Good Meal, Peace, Food, Tea. Then the swords get names: Enten vs. Cloud Gouger, True Realm, Roar. The auction speaks in architecture: Storehouse, Deal, Equal. The long book names people, then puts quotation marks on Strongest, Sword Master, Heroes. Part 2 opens on a rank and a place.</p>
  <p>Collisions sit on <a href="../world/title-collisions.html">title collisions</a>. The table: <a href="../manga/chapters.html">chapter index</a>. Essay: <a href="../analysis/titles.html">titles</a>.</p>
    {related([("../manga/chapters.html", "Index"), ("../world/title-collisions.html", "Collisions"), ("../analysis/titles.html", "Essay"), ("../world/food.html", "Meals")])}
""",
    )
    write(
        "analysis/meals.html",
        "Meals in the Title List | Kagurabachi Essay",
        "A revenge manga that titles food before True Realm: A Good Meal, Food, Tea, Peace.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Meals',
        "Essay · table",
        "The plate before the cut",
        "食事",
        "Char has to eat. The workshop was a kitchen.",
        f"""
  <p>Chapter 5 is “A Good Meal.” Chapter 15 is “Food.” Chapter 17 is “Tea.” Chapter 6 is “Peace.” True Realm is chapter 14, in the middle of that table, because the book will not let the hunt outrun a plate. The <a href="../world/food.html">meals page</a> files the objects. This essay files the method.</p>
  <p>Sojo’s people eat and die later in the same volume. The bowl on the Rokuhira table and a plate in a cafe are the same grammar. Official chapters: VIZ / MANGA Plus.</p>
    {related([("../world/food.html", "Meals"), ("../manga/chapter-5.html", "Ch. 5"), ("../manga/chapter-15.html", "Ch. 15"), ("titles.html", "Titles")])}
""",
    )
    write(
        "analysis/quotation-marks.html",
        "Quotation Marks on the Press | Kagurabachi Essay",
        "Strongest, Sword Master, Heroes: the long book puts quotes on words the Kamunabi already used.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Quotes',
        "Essay · Volume 11",
        "Quotes on the press",
        "「」",
        "The index keeps the quotation marks for a reason.",
        f"""
  <p>Chapter 99 is “Strongest.” Chapter 100 is “Sword Master.” Chapter 104 is “Heroes.” Volume 11 wears Heroes as a jacket. The weekly pages put quotes around words the Kamunabi and the press already spent on the Sword Bearers after Malediction. The book is arguing with a headline.</p>
  <p>Rooms: <a href="../manga/chapter-99.html">99</a>, <a href="../manga/chapter-100.html">100</a>, <a href="../manga/chapter-104.html">104</a>. Spine: <a href="../manga/volume-11.html">Volume 11</a>. Titles: <a href="titles.html">essay</a>.</p>
    {related([("../manga/chapter-104.html", "Heroes"), ("../manga/volume-11.html", "Volume 11"), ("titles.html", "Titles"), ("malediction.html", "Malediction")])}
""",
    )
    write(
        "analysis/named-graves.html",
        "Named Then Buried | Kagurabachi Essay",
        "Steam Squad, ACG leftovers, Tenri: the book names specialists in the week it spends them.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Essays</a> / Graves',
        "Essay · specialists",
        "Named, then buried",
        "名と墓",
        "A name and a grave in the same week.",
        f"""
  <p>Chapter 48 titles the Kokugoku Steam Squad. Fushimi’s Smoke Axe is competent. Hiruhiko arrives anyway. The Anti-Cloud Gouger Special Forces were the same sentence in the first book: six people built to solve one sword. Tenri eats a half-stable stone trying to impress Kyora. The encyclopedia’s job is to keep the names after the week moves on.</p>
  <p>Files: <a href="../factions/steam-squad.html">Steam Squad</a>, <a href="../world/acg.html">ACG</a>, <a href="../world/deaths.html">deaths</a>.</p>
    {related([("../manga/chapter-48.html", "Ch. 48"), ("../factions/steam-squad.html", "Steam Squad"), ("../world/deaths.html", "Deaths"), ("../world/smoke-axe.html", "Smoke Axe")])}
""",
    )
    write(
        "guide/chapter-map.html",
        "Kagurabachi Chapter Map | Every Weekly Title, Linked When We Have a Room",
        "A beginner door to the chapter index: Part 1, four arcs, leftover titles now have rooms. 118–120 stay in the table.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Guide</a> / Chapter map',
        "Guide · 1–131",
        "Chapter map",
        "話一覧",
        "The table is the authority. The rooms are doors.",
        f"""
  <p>Every weekly English and Japanese title lives on the <a href="../manga/chapters.html">chapter index</a>. This page is the beginner sentence: Part 1 is 1–115. Vs. Sojo 1–18. Rakuzaichi 19–46. Sword Bearer Assassination 47–115. Part 2 starts at 116. Chapter 131 is “Tipping Point.” Chapters 118–120 stay unlinked as solo rooms; use <a href="../world/irishima-talks.html">the talks room</a>.</p>
  <p>How to read: <a href="reading-order.html">reading order</a>. Official chapters: {VIZ}.</p>
    {related([("../manga/chapters.html", "Index"), ("reading-order.html", "Reading order"), ("../manga/part-2.html", "Part 2"), ("../world/irishima-talks.html", "Talks")])}
""",
    )
    write(
        "fun/volume-spines.html",
        "Kagurabachi Volume Spines | Eleven Jackets, One Solicited Close",
        "Mission through Heroes, then Volume 12 solicited 4 September 2026. Each spine now has a room.",
        '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Spines',
        "Jump Comics",
        "Eleven spines",
        "背表紙",
        "The commute by jacket instead of by Sunday.",
        f"""
  <p>Volume 1 Mission through Volume 11 Heroes each have a room on this wave. Volume 12 is still the solicited close: 4 September 2026, ISBN 978-4-08-885177-8, jacket unannounced. English trails Japan by about nine months. Volumes 10 and 11 English were TBD when the ISBN table was filed.</p>
  <p>Start: <a href="../manga/volume-1.html">Volume 1</a>. Table: <a href="../manga/volumes.html">volume guide</a>. Sentences: <a href="../manga/synopses.html">synopses</a>.</p>
    {related([("../manga/volume-1.html", "Vol. 1"), ("../manga/volume-11.html", "Vol. 11"), ("../manga/volume-12.html", "Vol. 12"), ("../manga/covers.html", "Covers")])}
""",
    )


if __name__ == "__main__":
    main()
