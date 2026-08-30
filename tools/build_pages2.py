#!/usr/bin/env python3
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("bp", "/workspace/tools/build_pages.py")
# Don't re-run build_pages on import, duplicate the helpers instead.

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
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
"""
FOOT = """
  </main>
  <div id="site-footer"></div>
  <script src="{js}"></script>
</body>
</html>
"""


def page(rel, title, desc, body, depth=1):
    prefix = "../" * depth
    html = HEAD.format(title=title, desc=desc, css=f"{prefix}css/site.css") + body + FOOT.format(js=f"{prefix}js/site.js")
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def crumb(section_href, section, leaf):
    return f'<p class="crumb"><a href="../index.html">Archive</a> / <a href="{section_href}">{section}</a> / {leaf}</p>'


def hero(kicker, title, jp, lede):
    return f"""<header class="page-hero"><div>
      <p class="kicker">{kicker}</p>
      <h1>{title}<span class="jp">{jp}</span></h1>
      <p class="lede">{lede}</p>
    </div></header>"""


# Manga guide
page("manga/index.html", "Manga Guide", "Kagurabachi manga guide: volumes, chapters, covers, color pages, and how to read officially.",
     '<p class="crumb"><a href="../index.html">Archive</a> / Manga Guide</p>'
     + hero("Publication database", "Manga Guide", "漫画ガイド", "Kanzenshuu-style notes on how Kagurabachi exists as paper and pixels: Jump, tankōbon, English editions, covers, and color pages.")
     + """
     <article class="article">
       <p>Kagurabachi began in <em>Weekly Shōnen Jump</em> on 19 September 2023. Takeru Hokazono, Osaka-born, 2000, had already placed with the one-shot <em>Enten</em> at the Tezuka Awards. The serial is the first long work. VIZ and MANGA Plus run the English simulpub. Jump Comics volumes started 2 February 2024 in Japan; VIZ’s first English hardcover-style tankōbon arrived 5 November 2024.</p>
       <p>As of May 2026 there are <strong>11</strong> Japanese volumes. Volume 12 is listed for 4 September 2026. Part 1 of the story closes around chapter 115 (“Swordsmith”). Part 2 opens on the Seitei War. Circulation passed 4 million by April 2026. An anime from Cypic, directed by Tetsuya Takeuchi, is scheduled for April 2027 (Crunchyroll outside Japan).</p>
     </article>
     <div class="grid">
       <a class="card" href="volumes.html"><div class="card-art p-chihiro"></div><div class="card-body"><h3>Volume guide</h3><p>Titles, ISBNs, chapter maps, jacket notes.</p></div></a>
       <a class="card" href="chapters.html"><div class="card-art p-kunishige"></div><div class="card-body"><h3>Chapter index</h3><p>Every titled chapter through the uncollected run.</p></div></a>
       <a class="card" href="covers.html"><div class="card-art blade-enten"></div><div class="card-body"><h3>Cover studies</h3><p>Color reconstructions of the eleven jackets.</p></div></a>
       <a class="card" href="color-pages.html"><div class="card-art p-hiyuki"></div><div class="card-body"><h3>Color pages &amp; pulls</h3><p>How Jump color openings work, without hosting scans.</p></div></a>
     </div>
     """)

VOLS = [
    ("01", "Mission", "すべきこと", "2024-02-02", "978-4-08-883819-9", "2024-11-05", "978-1-9747-4724-5", "1–8", "Chihiro Rokuhira", "Rusty ruby / asphalt red, white title, Kuro goldfish", "Chihiro takes Enten into Tokyo after a sighting. Char, Madoka, Azami, and Sojo’s first shadow."),
    ("02", "Enten vs. Cloud Gouger", "淵天 VS 刳雲", "2024-05-02", "978-4-08-883880-9", "2025-02-04", "978-1-9747-5271-3", "9–18", "Chihiro, Sojo", "Night steel vs storm cyan; blood on black", "Hospital, Anti-Cloud Gouger Forces, the duel that breaks Kuregumo."),
    ("03", "Knight of Darkness", "闇の騎士", "2024-07-04", "978-4-08-884116-8", "2025-05-06", "978-1-9747-5478-6", "19–27", "Chihiro, Hiyuki, Kyora", "Flame-orange against auction green-black", "Hiyuki arrives. The Sazanami estate. Enten is surrendered on purpose."),
    ("04", "Equal", "対等", "2024-10-04", "978-4-08-884209-7", "2025-08-05", "978-1-9747-5607-0", "28–36", "Chihiro, Hakuri", "Two figures, storehouse dusk", "Hakuri awakens Isou and Storehouse. Yura at the auction. Tenri and Datenseki."),
    ("05", "Fervent", "熱狂", "2024-12-04", "978-4-08-884348-3", "2025-11-04", "978-1-9747-5891-3", "37–46", "Chihiro, Kyora, Hakuri, Hiyuki", "Crowded jacket, Shinuchi heat", "Storehouse war. Magatsumi twitch. Chihiro joins the Kamunabi on his terms."),
    ("06", "Daybreak", "夜更け / 黎明", "2025-03-04", "978-4-08-884399-5", "2026-02-03", "978-1-9747-6287-3", "47–56", "Uruha, Samura, Chihiro, Hiruhiko", "Yin-yang bearers, blood center", "Train, kabuki, Senkutsuji. Tobimune returns to a blind man."),
    ("07", "Night Battle", "夜戦", "2025-05-02", "978-4-08-884413-8", "2026-05-05", "978-1-9747-6574-4", "57–65", "Samura, Chihiro, Iori", "Night blue, sunglasses, hotel dark", "The false deaths. Owl over Japan. Operation: Easy Does It."),
    ("08", "Dawn", "夜明け", "2025-07-04", "978-4-08-884566-1", "2026-08-04", "978-1-9747-1650-0", "66–74", "Chihiro, Iori, Hiruhiko", "Hotel silhouette under Owl", "Iori’s past. Malediction spoken aloud. Samura walks into the duel."),
    ("09", "Enten", "淵天", "2025-10-03", "978-4-08-884653-8", "2026-11-03", "978-1-9747-6845-5", "75–86", "Chihiro", "Single-figure Enten jacket", "Enten vs Tobimune. Kunishige’s brief, said cleanly. Samura opens his eyes."),
    ("10", "The Swordsmen", "剣士たち", "2026-01-05", "978-4-08-884740-5", "TBD", ": ", "87–95", "Natsuki, Hokuto, Uruha, Yura", "Four-man war ensemble", "Kasen’s leak. HQ infiltration. Yura starts spending Shinuchi at range."),
    ("11", "Heroes", "英雄", "2026-05-01", "978-4-08-885102-0", "TBD", ": ", "96–105", "Chihiro, goldfish, snow", "Snow white, Aka &amp; Kuro, Enten raised", "Yukisada, the vessel, the cell. The Sword Master stands up in Yura."),
]

rows = "".join(
    f"<tr><td>{n}</td><td><em>{title}</em><br><span style='opacity:.7'>{jp}</span></td><td>{jp_d}<br>ISBN {isbn_j}</td><td>{en_d}<br>{isbn_e}</td><td>Ch. {chs}</td><td>{faces}</td></tr>"
    for n, title, jp, jp_d, isbn_j, en_d, isbn_e, chs, faces, _pal, _sum in VOLS
)

page("manga/volumes.html", "Volume Guide", "Kagurabachi tankōbon volume guide with Japanese and English ISBNs, chapter ranges, and jacket notes.",
     crumb("index.html", "Manga Guide", "Volumes")
     + hero("Tankōbon", "Volume Guide", "単行本", "Eleven Jump Comics volumes in Japan; eight English volumes released or solicited through late 2026.")
     + f"""
     <p class="note">Chapter ranges for middle volumes are compiled from public jacket copy and wiki concordances. If a collected edition shifts a chapter, the chapter index is the authority.</p>
     <div class="table-wrap"><table>
       <thead><tr><th>#</th><th>Title</th><th>Japan</th><th>English (VIZ)</th><th>Chapters</th><th>Jacket faces</th></tr></thead>
       <tbody>{rows}</tbody>
     </table></div>
     <h2>Volume summaries</h2>
     """ + "".join(
         f"<h3>Vol. {n}, {title}</h3><p>{summary} <em>Palette:</em> {pal}.</p>"
         for n, title, jp, jp_d, isbn_j, en_d, isbn_e, chs, faces, pal, summary in VOLS
     )
     + "<p>Volume 12 (4 September 2026, ISBN 978-4-08-885177-8) is expected to close Part 1 (chs. 106–115) and open the war book.</p>")

# Cover studies
covers_html = []
palettes = {
    "01": ("#7a1014", "#0c0b0a", "#f6efe6", "カグラバチ"),
    "02": ("#0a1c22", "#8b1218", "#dceef2", "淵天／刳雲"),
    "03": ("#3b1008", "#1a0c0d", "#e8c547", "闇の騎士"),
    "04": ("#3a2a48", "#161018", "#f6efe6", "対等"),
    "05": ("#9b1419", "#1a0a0b", "#e8c547", "熱狂"),
    "06": ("#4a1020", "#0c0b0a", "#c9a227", "夜更け"),
    "07": ("#1e2430", "#0b0d12", "#e8d080", "夜戦"),
    "08": ("#2a3048", "#c41e3a", "#f6efe6", "夜明け"),
    "09": ("#111", "#7a1014", "#c9a227", "淵天"),
    "10": ("#1c3350", "#4a1858", "#f6efe6", "剣士たち"),
    "11": ("#e8eef2", "#9b1419", "#0c0b0a", "英雄"),
}
cards = []
for n, title, jp, *_rest, pal, summary in [(v[0], v[1], v[2], v[9], v[10]) if False else v for v in VOLS]:
    pass

for v in VOLS:
    n, title, jp, *_ , pal, summary = v[0], v[1], v[2], v[9], v[10]
    bg, fg, accent, lock = palettes[n]
    textc = "#0c0b0a" if n == "11" else "#f6efe6"
    cards.append(f"""
    <article class="cover-study">
      <div class="cover-face" style="background:linear-gradient(160deg,{bg},{fg});color:{textc}">
        <span class="vol">{n}</span>
        <span class="title-lockup" style="color:{accent}">{lock}</span>
      </div>
      <div class="cover-meta">
        <h3>Vol. {n} · {title}</h3>
        <p>{summary} Jacket reading: {pal}.</p>
      </div>
    </article>""")

page("manga/covers.html", "Cover Studies", "Original color reconstructions of Kagurabachi volume jackets based on published cover descriptions.",
     crumb("index.html", "Manga Guide", "Cover Studies")
     + hero("Color documentation", "Cover Studies", "表紙研究", "These are not official illustrations. They are archive reconstructions of palette, lockup, and stated cover figures, the Kanzenshuu habit of documenting a jacket when you cannot reprint it.")
     + '<div class="grid">' + "".join(cards) + "</div>"
     + """<h2>How to read a Hokazono jacket</h2>
     <article class="article">
       <p>Volume 1 sets the law: Chihiro centered, Kuro overhead, asphalt-red field, white logotype, black volume numeral. Later jackets keep the high-contrast triad and invite one extra hue when a rival blade is on the stage (cyan for Cloud Gouger, snow for Volume 11). Group jackets (5, 6, 10) are cast photographs in ink. Single-figure jackets (1, 9, 11) are icons.</p>
     </article>""")

# Chapters
CHAPTERS = [
    (1, "Mission", "すべきこと"), (2, "Heaps", "累累"), (3, "Witness", "目撃者"),
    (4, "Sorcery and the Enchanted Blade", "妖術と妖刀"), (5, "A Good Meal", "ごちそう"),
    (6, "Peace", "平穏"), (7, "Smoke Signal", "狼煙"), (8, "Norisaku Madoka: I Will Change", "円 法炸 〜俺は変わるんだ〜"),
    (9, "Enten vs. Cloud Gouger", "淵天vs刳雲"), (10, "Swift", "サクッっと"), (11, "Awaken", "目覚め"),
    (12, "Preparations", "支度"), (13, "Elite", "精鋭"), (14, "True Realm", "本領"),
    (15, "Food", "飯"), (16, "Silence", "沈黙"), (17, "Tea", "茶"), (18, "Roar", "轟く"),
    (19, "Knight of Darkness", "闇の騎士"), (20, "The Kamunabi's Weapon", "神奈備の武器"),
    (21, "Lukewarm", "微温い"), (22, "Deadlock", "拮抗"), (23, "Storehouse", "蔵"),
    (24, "Hunters", "狩人"), (25, "Deal", "取引"), (26, "Confidence", "自信"), (27, "Mr. Inazuma", "Mr.イナズマ"),
    (28, "Breach", "突破口"), (29, "Selection", "取捨"), (30, "Intruders", "乱入者"),
    (31, "Greeting", "挨拶"), (32, "Wall", "壁"), (33, "Defend to the Death", "死守"),
    (34, "Duty", "役目"), (35, "Cage", "檻"), (36, "Geniuses", "天才達"), (37, "Equal", "対等"),
    (38, "Race", "競合"), (39, "Surpass!", "超えろ!!"), (40, "The Tip", "一端"),
    (41, "Fervent", "熱狂"), (42, "Everything", "全部"), (43, "Fulfill", "全う"),
    (44, "The Curtain Falls", "閉幕"), (45, "What Comes Next", "これからの話"), (46, "Unruly Punk", "勝手な野郎"),
    (47, "Uruha", "漆羽"), (48, "The Kokugoku Steam Squad", "国獄 湯煙スクワッド"),
    (49, "Deadlock", "均衡"), (50, "Interception", "迎撃"), (51, "Samura", "座村"),
    (52, "Just the Two of Us", "2人きり"), (53, "Darkness", "暗がり"), (54, "Friendship", "友情"),
    (55, "Fight Alongside", "共闘"), (56, "Daybreak", "夜更け"), (57, "Collapse", "崩壊"),
    (58, "Reunion", "再会"), (59, "Blackout", "暗転"), (60, "Resurrection", "黄泉がえり"),
    (61, "Night Battle", "夜戦"), (62, "Iori", "イヲリ"), (63, "Car Chase", "車追跡"),
    (64, "Become the Samurai", "ビカム侍"), (65, "Imitate", "見真似"), (66, "Truth", "真実"),
    (67, "Kyoto Bloodshed Hotel", "ザ殺戮ホテル"), (68, "Metamorphosis", "変幻"),
    (69, "The Guy with the Scar", "傷ノ男"), (70, "Iai White Purity Style", "居合白禊流"),
    (71, "Contest", "勝負"), (72, "Future", "未来"), (73, "Daybreak", "黎明"), (74, "Dawn", "夜明け"),
    (75, "Illusion", "幻想"), (76, "Banquet", "宴"), (77, "No Longer Relevant", "蚊帳の外"),
    (78, "Switch", "交代"), (79, "Threat!!", "曲者!!"), (80, "Secret Room", "密室"),
    (81, "Core", "主力"), (82, "Enten Vs. Tobimune", "淵天VS飛宗"), (83, "The Enten", "淵天"),
    (84, "The Wounded", "傷の者たち"), (85, "Open", "開く"), (86, "Quickening", "胎動"),
    (87, "Phantoms", "亡霊"), (88, "The First Step", "皮切り"), (89, "Battle Chaos", "乱戦"),
    (90, "Kiri", "斬ちゃん"), (91, "Natsuki", "奈ツ基"), (92, "The Swordsmen", "剣士たち"),
    (93, "Finishing Touches", "仕上げ"), (94, "The Second Arrow", "二の矢"), (95, "Flood", "横溢"),
    (96, "Urgency", "切迫"), (97, "Vessel", "受け皿"), (98, "Ikuto Hagiwara, Worthless Commander", "無能隊長 萩原幾兎"),
    (99, '"Strongest"', "一番強い"), (100, '"Sword Master"', "剣聖"), (101, "Safe Zone", "安全地帯"),
    (102, "What You Need to See", "視るべきモノ"), (103, "Healing", "再生"), (104, '"Heroes"', "英雄"),
    (105, "Transformation", "変身"), (106, "Karma", "宿縁"), (107, "This Moment", "この一瞬"),
    (108, "Enten vs. Magatsumi", "淵天VS勾罪"), (109, "Tobimune vs. Magatsumi", "飛宗VS勾罪"),
    (110, "As a Swordsman", "剣士として"), (111, "Apex", "頂"), (112, "Future", "未来"),
    (113, "Rock", "石"), (114, "Kunishige Rokuhira", "六平国重"), (115, "Swordsmith", "刀匠"),
    (116, "Princess", "姫"), (117, "The Irishima Talks", "杁島会談"),
    (118, "The Irishima Talks, Part 2", "杁島会談 弐"), (119, "The Irishima Talks, Part 3", "杁島会談 参"),
    (120, "The Irishima Talks, Part 4", "杁島会談 肆"), (121, "The Irishima Talks, END", "杁島会談 終"),
    (122, "Start", "始動"), (123, "Chiaki", "千晃"), (124, "Powerless", "無力"),
    (125, "Smelting", "製鉄"), (126, "Fire", "火"),
]
ch_rows = "".join(f"<tr><td>{n}</td><td>{en}</td><td>{jp}</td></tr>" for n, en, jp in CHAPTERS)
page("manga/chapters.html", "Chapter Index", "Complete Kagurabachi chapter title index from Mission through the Seitei War flashback.",
     crumb("index.html", "Manga Guide", "Chapters")
     + hero("Serialization", "Chapter Index", "話一覧", "English titles follow VIZ / common wiki renderings; Japanese titles follow Jump.")
     + f'<div class="table-wrap"><table><thead><tr><th>#</th><th>English</th><th>Japanese</th></tr></thead><tbody>{ch_rows}</tbody></table></div>'
     + "<p>Bonus one-shots published with the volumes include <em>Genichi Sojo’s Bathhouse Quest</em> (two parts) and <em>Soya Sazanami’s Memories, Begone!</em></p>")

page("manga/color-pages.html", "Color Pages & Pulls", "How Kagurabachi uses Jump color openings and volume jackets, documented without hosting official art.",
     crumb("index.html", "Manga Guide", "Color Pages")
     + hero("Illustration archive", "Color Pages &amp; Pulls", "カラーページ", "A pull, in this archive, is a documented color moment, lead color, center color, jacket, anime teaser, not a scan.")
     + """
     <article class="article">
       <h2>What Jump actually prints</h2>
       <p>A typical <em>Weekly Shōnen Jump</em> color opening is a full-bleed illustration plus a typeset logo, used when a series is leading the issue or celebrating a volume. Kagurabachi’s color pages lean on the same triad as the jackets: Chihiro’s black coat, a red field or blood geometry, and a goldfish that is either Kuro-black or Aka-red. Snow and gold show up when Enten is being iconic rather than narrative (Volume 11; the 2026 anime teaser).</p>
       <h2>How we log a pull</h2>
       <div class="table-wrap"><table>
         <thead><tr><th>Type</th><th>What to record</th><th>Example</th></tr></thead>
         <tbody>
           <tr><td>Issue lead color</td><td>Issue date, position, figures, palette, any author comment</td><td>Vol. 1 announcement color: Chihiro, Kuro, ruby ground</td></tr>
           <tr><td>Interior color</td><td>Chapter number, whether it reprints in tankōbon</td><td>Early Sojo clash pages keep cyan lightning against red type</td></tr>
           <tr><td>Tankōbon jacket</td><td>Faces, background, logo color, see <a href="covers.html">Cover Studies</a></td><td>Vol. 6 yin-yang Uruha / Samura</td></tr>
           <tr><td>Promo / anime</td><td>Studio, date, which fish appear</td><td>Cypic teaser: Aka, Kuro, Nishiki behind Chihiro and Enten</td></tr>
         </tbody>
       </table></div>
       <p>If you own the volume, the legal “pull” is the book in your hands. This site will describe the page, not replace it. Buy the Jump Comics / VIZ edition; do not send us scans.</p>
       <h2>Spine &amp; printing notes</h2>
       <p>Japanese Jump Comics spines for the series run a dark field with the カグラバチ logotype. A shelf of the first eleven volumes reads as a red-to-black bar, useful if you are collecting for the same reason Kanzenshuu collects spine art. English VIZ spines follow VIZ’s current Jump trade dress; they are a parallel object, not a color-matched set.</p>
     </article>
     """)

# Arcs
page("arcs/index.html", "Story Arcs", "Kagurabachi story arcs: Vs. Sojo, Rakuzaichi, Sword Bearer Assassination, Seitei War.",
     '<p class="crumb"><a href="../index.html">Archive</a> / Story Arcs</p>'
     + hero("Narrative map", "Story Arcs", "ストーリーアーク", "Four movements. Two parts. One war that refuses to stay in the past.")
     + """
     <div class="grid">
       <a class="card" href="vs-sojo.html"><div class="card-art blade-kuregumo"></div><div class="card-body"><span class="tag">Ch. 1–18 · Vol. 1–2</span><h3>Vs. Sojo</h3><p>Char, Cloud Gouger, True Realm.</p></div></a>
       <a class="card" href="rakuzaichi.html"><div class="card-art p-kyora"></div><div class="card-body"><span class="tag">Ch. 19–46 · Vol. 3–5</span><h3>Rakuzaichi</h3><p>The 208th auction and Shinuchi.</p></div></a>
       <a class="card" href="sword-bearer.html"><div class="card-art p-samura"></div><div class="card-body"><span class="tag">Ch. 47–115 · Vol. 6–12</span><h3>Sword Bearer Assassination</h3><p>Contracts, Iori, the Master.</p></div></a>
       <a class="card" href="seitei-war.html"><div class="card-art p-akemura"></div><div class="card-body"><span class="tag">Ch. 116– · Part 2</span><h3>Seitei War</h3><p>Irishima, Chiaki, the forge.</p></div></a>
     </div>
     """)

page("arcs/vs-sojo.html", "Vs. Sojo Arc", "Summary and analysis of Kagurabachi's Vs. Sojo arc.",
     crumb("index.html", "Arcs", "Vs. Sojo")
     + hero("Chapters 1–18", "Vs. Sojo Arc", "双城編", "The revenge story learns it will have to protect someone who cannot hold a sword.")
     + """<div class="layout"><article class="article">
     <h2>Summary</h2>
     <p>Three years after the raid, Chihiro and Shiba work the Tokyo underworld. Char Kyonagi says she has seen an Enchanted Blade. Norisaku Madoka confirms Sojo has Cloud Gouger. Azami of the Kamunabi wants Chihiro away from that man. Chihiro stays.</p>
     <p>Sojo takes Char. The Anti-Cloud Gouger Special Forces, six people built to solve one sword, stage an ambush while Chihiro hits the compound. Four of the six die. Hagiwara loses his legs. Kazane loses an arm. Chihiro loses an arm and still finds the True Realm. Enten cuts Cloud Gouger. Sojo chooses Datenseki suicide over a quiet death.</p>
     <h2>Why the arc matters</h2>
     <p>This is the series teaching you the rules: Lifelong Contracts, Datenseki as a bomb, government squads that are not enough, and a protagonist who will spend his body without spending Char. Sojo is the dark mirror of Kunishige-love. Everything later, auction, bearers, Magatsumi, is a larger version of this argument.</p>
     <p class="related"><a href="../characters/sojo.html">Sojo</a><a href="../characters/char.html">Char</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a></p>
     </article></div>""")

page("arcs/rakuzaichi.html", "Rakuzaichi Arc", "Summary of the Rakuzaichi auction arc in Kagurabachi.",
     crumb("index.html", "Arcs", "Rakuzaichi")
     + hero("Chapters 19–46", "Rakuzaichi Arc", "落罪市編", "Two hundred years of auction. One Storehouse. A boy the family called empty.")
     + """<div class="layout"><article class="article">
     <h2>Summary</h2>
     <p>Shinuchi is listed at the 208th Rakuzaichi. Chihiro meets Hakuri, the discarded Sazanami, and Hiyuki, the Kamunabi’s flame. He lets the clan take Enten so the blade can scout the Storehouse on its own charge. On auction day he walks in with Cloud Gouger’s stump and a rebuilt arm.</p>
     <p>Hakuri remembers a woman the auction killed and the Storehouse opens in him. Tenri dies on a half-stable stone trying to impress Kyora. Inside the Kura, Chihiro spends the last of Kuregumo to take Enten back. Kyora, dying, touches Magatsumi. The Sword Master looks through the auctioneer’s eyes. Hiyuki and Chihiro keep the building from becoming a second island. Prisoners leave. The Rakuzaichi ends. Chihiro gives the Kamunabi Magatsumi and keeps Enten by joining them. Then a Sanso is attacked, and the next book starts on a train.</p>
     <p class="related"><a href="../characters/hakuri.html">Hakuri</a><a href="../characters/kyora.html">Kyora</a><a href="../characters/hiyuki.html">Hiyuki</a></p>
     </article></div>""")

page("arcs/sword-bearer.html", "Sword Bearer Assassination Arc", "Part 1 climax of Kagurabachi: the hunt for the wartime bearers.",
     crumb("index.html", "Arcs", "Sword Bearer Assassination")
     + hero("Chapters 47–115", "Sword Bearer Assassination", "所有者暗殺編", "Part 1. Longest arc. The contracts come due.")
     + """<div class="layout"><article class="article">
     <p class="note"><strong>Full spoilers</strong> for the end of Part 1.</p>
     <h2>Movement one, Uruha and Samura</h2>
     <p>Chihiro and Hakuri are sent to keep Yoji Uruha alive. Hiruhiko boards the train. The fight falls into a kabuki house. At Senkutsuji, Hakuri returns Tobimune to Samura, who clears the temple and then cuts Uruha down. It looks like a Hishaku pact. It is Suzaku: kill the contract, keep the man.</p>
     <h2>Movement two, Iori</h2>
     <p>Samura hangs Owl over the country. The Masumi take Iori to the Kyoto Bloodshed Hotel. Chihiro learns Iai by copying Kuguri and the house style. Iori’s seal breaks. Hiruhiko wrecks the hotel with Play. Samura arrives. Feathers, banquet, goldfish.</p>
     <h2>Movement three, the basement</h2>
     <p>Chihiro tells Samura the truth Kunishige left in Enten. Samura opens his eyes. In Tokyo, Kasen’s leak is on the table, Kudo dies for Hakuri, Uruha walks again, Yura spends Magatsumi without drawing it, Yukisada sits in the barrier. Shiba dumps the fight onto the street. Chihiro and Samura meet Yura. Yura, losing, gives the body to Akemura.</p>
     <h2>End of Part 1</h2>
     <p>Magatsumi breaks Enten. Samura’s flames go black. He buys Chihiro a corridor and dies. Tobimune goes to Iori. Akemura is loose in the Kamunabi. Chapters 106–115 spend the last of the present tense and hand the book to a swordsmith and a princess on Irishima.</p>
     <p class="related"><a href="../characters/samura.html">Samura</a><a href="../characters/akemura.html">Akemura</a><a href="../analysis/enten-purpose.html">Enten’s purpose</a></p>
     </article></div>""")

page("arcs/seitei-war.html", "Seitei War Arc", "Part 2 of Kagurabachi: the Seitei War, Irishima, and the birth of the Enchanted Blades.",
     crumb("index.html", "Arcs", "Seitei War")
     + hero("Part 2 · Ch. 116–", "Seitei War Arc", "斉廷戦争編", "The war the jackets called heroic. The talks, the ore, the woman who could see.")
     + """<div class="layout"><article class="article">
     <h2>What the present already told us</h2>
     <p>Shokoku rose from the sea. Irishima had Datenseki. Japan took it. The Mikaboshi, old sorcerer kings the Soga once drove off the mainland, came back with bodies that could survive the stone. The Sorcery Bureau became an army, then the Kamunabi. A year and five months in, Kunishige’s blades reversed the front. After the treaty, Akemura used Malediction anyway.</p>
     <h2>Part 2 on the page</h2>
     <p>The uncollected chapters open on Chiaki Soga, Chihiro’s mother, Princess Soga, foresight as inherited proof of Izanami, and on the Irishima talks. Shiba is still a Soga guardian. Mashiro is still alive. Kunishige is still a picky weapons dealer who has not yet looked at the ore. The smelting chapters are the archive’s smithing manual: how a pair of eyes made a mineral into seven national sins.</p>
     <p>This arc is unfinished. Entries will expand as Jump prints them. Until then, the <a href="../world/index.html">timeline</a> holds the dated facts.</p>
     </article></div>""")

# Analysis
page("analysis/index.html", "Story Analysis", "Essays on Kagurabachi: Enten’s purpose, the Malediction, revenge and inheritance.",
     '<p class="crumb"><a href="../index.html">Archive</a> / Analysis</p>'
     + hero("Essays", "Story Analysis", "考察", "Longer pieces in the Kanzenshuu register: argument, citation, no recap padding.")
     + """
     <div class="grid">
       <a class="card" href="enten-purpose.html"><div class="card-art blade-enten"></div><div class="card-body"><h3>What Enten was forged for</h3><p>A counter-blade, not a seventh trophy.</p></div></a>
       <a class="card" href="malediction.html"><div class="card-art blade-magatsumi"></div><div class="card-body"><h3>The Malediction</h3><p>How a war crime became a myth of heroes.</p></div></a>
       <a class="card" href="revenge.html"><div class="card-art p-chihiro"></div><div class="card-body"><h3>Revenge and inheritance</h3><p>Chihiro, Kunishige, and the goldfish bowl.</p></div></a>
     </div>
     """)

page("analysis/enten-purpose.html", "What Enten Was Forged For", "Analysis of Enten’s design purpose in Kagurabachi.",
     crumb("index.html", "Analysis", "Enten’s purpose")
     + hero("Essay", "What Enten was forged for", "淵天の目的", "Kunishige did not give his son a heirloom. He gave him a retraction.")
     + """<article class="article">
     <p>The public knows six Enchanted Blades. The Kamunabi want six Enchanted Blades. Chihiro’s whole early swagger, the seventh sword, the secret cellar, reads as shōnen inheritance. Chapter 83 and the Kyoto duel with Samura retract that reading. Enten exists because the other swords could not be broken on an anvil. Its True Realm is Magatsumi’s death. Nishiki’s resistance kit is the brief made visible.</p>
     <p>That is why the goldfish matter as craft, not mascot. Kuro, Aka, and Nishiki are peacetime objects. A wartime blade manifests weather, flowers, banquet ghosts. Enten manifests the house. Hokazono’s interview line about koi versus goldfish is the same argument in the real world: the long fish looked like a weapon; the bowl fish looked like a life.</p>
     <p>When Magatsumi finally breaks Enten, the book is being literal. A retraction can fail. Samura’s black Suzaku pausing the disintegration is the support blade doing the job Kunishige assigned it eighteen years late. Chihiro’s notes toward a <em>new</em> Enten are the smith’s education catching up to the father’s. Revenge got him to the door. Inheritance is the forge.</p>
     <blockquote class="pull">The seventh blade is the only one whose success condition is fewer blades.</blockquote>
     </article>""")

page("analysis/malediction.html", "The Malediction", "Analysis of Magatsumi’s Malediction and the Seitei War cover-up.",
     crumb("index.html", "Analysis", "The Malediction")
     + hero("Essay", "The Malediction", "蠱毒", "Two hundred thousand people after a peace. The Kamunabi called it a victory anyway.")
     + """<article class="article">
     <p>Malediction is not one of Magatsumi’s insect names. It is an extension, True Realm as policy. Akemura decides the islanders should end, and the blade learns a wider mouth. Flowers are the visual because the sword already ate people as gardens; he simply asked for a field the size of a nation.</p>
     <p>The other bearers fail in the room and then succeed in the press. Kunishige hides. Samura blinds himself twice: once as training, again as fatherhood. Kasen, years later, still thinks the blades are a path to order, which is how you get a director leaking a smith’s address to the Hishaku. The cover-up is not a twist. It is the water the present-day plot has been swimming in since page one.</p>
     <p>Yura’s conversion is the scary political joke. He wanted Akemura dead to open a contract. He meets the man and recognizes a colleague. Chihiro’s generation inherits both the flowers and the lie about who planted them.</p>
     </article>""")

page("analysis/revenge.html", "Revenge and Inheritance", "Essay on Chihiro’s revenge plot and what he inherits from Kunishige.",
     crumb("index.html", "Analysis", "Revenge and inheritance")
     + hero("Essay", "Revenge and inheritance", "復讐と継承", "The coat is black with other people’s blood. The fish are from the kitchen.")
     + """<article class="article">
     <p>Jump has a file for “father dies, son walks.” Kagurabachi keeps the file and then keeps naming the father. Kunishige is not a saint in flashback; he is a man who sold weapons, stabilized a cursed ore, won a war, and tried to raise a child over a cellar of failures. Chihiro’s stoicism is workshop manners. His refusal to kill bystanders is the one moral the smith actually transmitted.</p>
     <p>Every ally is an inheritance test. Shiba is the friend who stayed. Hakuri is the son of a house that treats children as stock. Iori is what happens if you erase the father instead of explaining him. Sojo is what happens if you love the work and not the man. Hiyuki is the state as a person you might, on a good day, stand next to.</p>
     <p>Part 2’s move into Chiaki and the Irishima talks is the series admitting revenge was the prologue. The real estate is a mineral, a marriage, and a government that will always prefer a useful myth to a living island.</p>
     </article>""")

# Factions / world / collectibles
page("factions/index.html", "Factions", "Kamunabi, Hishaku, Sazanami, Soga, Mikaboshi, Masumi.",
     '<p class="crumb"><a href="../index.html">Archive</a> / Factions</p>'
     + hero("Organizations", "Factions", "勢力", "Who holds the blades, who sells them, who leaked the address.")
     + """
     <h2>Kamunabi 神奈備</h2>
     <p>State sorcerers, rebuilt from the Counter-Sorcery Army / Sorcery Bureau during the war. They guard remaining bearers in Sanso fortresses and want the Enchanted Blades under seal. Leaders include Kasen (director; later revealed as the leak), Ichiki, Yatsuru, Azami, Izaru, Kudo. Hiyuki is the pointed end. The Masumi ninja clan (Ro, Moku, Sumi) serve Samura until he frees them.</p>
     <h2>Hishaku 毘灼</h2>
     <p>Ten criminal sorcerers, flame tattoos, shared fire-gate. They killed Kunishige, stole six blades, and spent three years trying to open the contracts by killing bearers. Named: Yura, Hokuto, Uran, Bingo, Yukisada, Hiruhiko, Kuguri, Toto. Allied with Korogumi yakuza and at least one Kamunabi head.</p>
     <h2>Sazanami 漣</h2>
     <p>Two centuries of Rakuzaichi. Kyora’s Storehouse. The Tou (Soya, Tamaki, Enji, Tenri) as household military. Hakuri is the error that ends the firm.</p>
     <h2>Soga and Mikaboshi</h2>
     <p>The Soga were mainland prophecy aristocracy; Chiaki’s foresight is the clan’s warrant. The Mikaboshi, old rulers exiled to Shokoku, came back for Irishima’s Datenseki and started the war. Ariu Mikaboshi killed Hiroto and Yoshinojo Soga on the island. After the blades arrived, Shokoku overthrew its royals and signed a peace Akemura then voided with flowers.</p>
     """)

page("world/index.html", "World & Timeline", "Kagurabachi in-universe timeline from Shokoku’s rise to Part 2.",
     '<p class="crumb"><a href="../index.html">Archive</a> / World</p>'
     + hero("Setting", "World &amp; Timeline", "世界と年表", "A modern Japan that had to admit sorcery in public, then lie about what it did with it.")
     + """
     <p><a href="datenseki.html">Datenseki</a> · <a href="sorcery.html">Sorcery</a></p>
     <div class="timeline">
       <article><time>~1000+ years ago</time><h3>Mikaboshi exile</h3><p>Soga push the old kings off the mainland. The Mikaboshi survive under the sea with Datenseki-adapted bodies.</p></article>
       <article><time>22 years before present</time><h3>Shokoku appears</h3><p>An island rises. Irishima’s earthquake had already shown a Datenseki vein; Japan harvests it.</p></article>
       <article><time>Seitei War (ends 18 years ago)</time><h3>Blades enter at +1 year 5 months</h3><p>Kamunabi forms. Six Enchanted Blades reverse the war. Treaty. Malediction. Cover-up. Kunishige hides with the steel.</p></article>
       <article><time>~15 years after the war</time><h3>Enten</h3><p>Kunishige and Chihiro forge the seventh blade.</p></article>
       <article><time>4 years ago</time><h3>Hishaku form</h3><p>Ten sorcerers, one plan for Shinuchi.</p></article>
       <article><time>3 years ago</time><h3>The raid</h3><p>Kunishige killed. Six blades stolen. Ibuki Misaka murdered. Remaining bearers locked in Sanso.</p></article>
       <article><time>Present (Oct–Nov)</time><h3>Main story</h3><p>Cloud Gouger to Sojo. 208th Rakuzaichi. Sword Bearer Assassination. Part 1 ends. Part 2 returns to Irishima.</p></article>
     </div>
     """)

page("world/datenseki.html", "Datenseki", "The ore that makes Enchanted Blades, and explodes everyone else.",
     crumb("index.html", "World", "Datenseki")
     + hero("Material", "Datenseki", "奪天石", "About 250 kilograms known. One pair of eyes ever made it safe.")
     + """<article class="article">
     <p>Datenseki amplifies spirit energy the way the blades do, without the stabilizing cut. Unprocessed, it pops the user. Kunishige’s sight let him smith it into katana that overflow as shapes instead of craters. Sojo spent Char’s clan trying to fake that sight and produced stones that hold for a few minutes, long enough to kill Tenri, long enough to arm Hishaku infantry.</p>
     <p>The war is, at the mineral level, a fight over a vein on Irishima. Everything else, clans, contracts, flowers, is what people did with a quarter-ton of rock.</p>
     </article>""")

page("world/sorcery.html", "Sorcery", "How spirit energy, innate arts, and Enchanted Blades interact in Kagurabachi.",
     crumb("index.html", "World", "Sorcery")
     + hero("System", "Sorcery", "妖術", "Yōjutsu and yōtō share a kanji. The blades are sorcery that left the body and did not come back.")
     + """<article class="article">
     <p>Civilian sorcerers handle small jobs. The Kamunabi exist because some jobs are national. Innate arts on this site include Shiba’s teleport, Azami’s Coin, Hakuri’s Isou and Storehouse, Hiyuki’s Flame Bone, Tafuku’s duel domain, Char’s regeneration, Hagiwara’s magnetism, Natsuki’s Lightning Menace, Hiruhiko’s Blood Crane, Kuguri’s Twilight Wave, Toto’s blood tracking.</p>
     <p>A Lifelong Contract shuts those nerves off. Cut the contract without cutting the person, Samura’s specialty, and the old art limps back. Enchanted Blade extensions (True Realm, “dark power”) are what happens when intent, mortality, and Datenseki agree.</p>
     <h3>Iai White Purity Style</h3>
     <p>Itsuo Shirakai’s speed school, mocked until it killed the mockers. Samura and Uruha are the famous students. Iori and Chihiro copy it; Kiri Shirakai wants to behead the founder for saying women cannot. Eyes closed is not theater. It is the curriculum.</p>
     </article>""")

page("collectibles/index.html", "Collectibles", "Kagurabachi volumes, ISBNs, circulation, and licensed merch notes.",
     '<p class="crumb"><a href="../index.html">Archive</a> / Collectibles</p>'
     + hero("On the shelf", "Collectibles", "コレクション", "What exists to buy. No bootlegs, no scan listings.")
     + """
     <h2>Print</h2>
     <ul>
       <li><strong>Jump Comics</strong> (Shueisha), Japanese tankōbon, 11 volumes as of 1 May 2026. Start ISBN 978-4-08-883819-9.</li>
       <li><strong>VIZ Media</strong>, English editions from 5 November 2024. Vols. 1–8 have announced dates through August 2026; later volumes TBA.</li>
       <li><strong>Weekly Shōnen Jump</strong>, the serialization object. Color leads are issue-specific.</li>
       <li>French edition via Kana (noted on Volume 11 promo). Other territorial editions follow local Jump licenses.</li>
     </ul>
     <h2>Circulation &amp; awards</h2>
     <p>350k (Jul 2024) → 1M (Oct 2024) → 2.2M (May 2025) → 3M (Oct 2025) → 4M+ (Apr 2026). Next Manga Award 2024 (print). Nominations: Shogakukan, Kodansha, Eisner (Asia). 2026 Daruma for Best Action Manga. BookScan and NYT graphic lists in North America from the first VIZ volume.</p>
     <h2>Anime object</h2>
     <p>Cypic / Takeuchi / Keigo Sasaki designs. World-tour first-20-minutes from July 2026 (Anime Expo, Japan Expo, AnimagiC, Anime NYC) before the April 2027 broadcast. Crunchyroll worldwide (with listed exceptions). Any “collectible” from that tour is a ticket and a memory unless a formal booklet is sold, record the SKU if one appears.</p>
     <h2>Figures &amp; merch</h2>
     <p>Licensed goods track Jump’s usual partners (Jump Shop, volume-launch storefronts, later anime makers). This archive will log official items with release date and manufacturer when they exist. Unlicensed statues and bootleg keychains are not listed.</p>
     <p class="related"><a href="../manga/volumes.html">Volume ISBNs</a><a href="../manga/covers.html">Jacket studies</a></p>
     """)

print("guides done")
