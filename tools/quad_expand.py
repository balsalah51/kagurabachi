#!/usr/bin/env python3
"""Deepen existing rooms with unique printed-fact addenda. Idempotent via marker."""
from pathlib import Path
import re

ROOT = Path("/workspace")
MARK = "<!-- quad-wave -->"

CHAPTERS = [
    (1, "Mission", "すべきこと", "Volume 1 opens the job as a household leftover."),
    (2, "Heaps", "累累", "Bodies and jobs still stacked from the raid night."),
    (3, "Witness", "目撃者", "Char’s eyes make the hunt a pair."),
    (4, "Sorcery and the Enchanted Blade", "妖術と妖刀", "The words land before the first versus title."),
    (5, "A Good Meal", "ごちそう", "The plate is already method."),
    (6, "Peace", "平穏", "A quiet title in a revenge book."),
    (7, "Smoke Signal", "狼煙", "The city starts answering."),
    (8, "Norisaku Madoka: I Will Change", "円 法炸 〜俺は変わるんだ〜", "A staff name as a promise."),
    (9, "Enten vs. Cloud Gouger", "淵天vs刳雲", "Volume 2’s jacket, two swords on one street."),
    (10, "Swift", "サクッっと", "Magazine speed. Weather already in the city."),
    (11, "Awaken", "目覚め", "Someone wakes into the job."),
    (12, "Preparations", "支度", "The ACG list is being built."),
    (13, "Elite", "精鋭", "Specialists named so weather has opponents."),
    (14, "True Realm", "本領", "Slaughter as a brief Sojo can mean."),
    (15, "Food", "飯", "Char still has to eat. Sojo’s people eat too."),
    (16, "Silence", "沈黙", "Talking treated as a leak."),
    (17, "Tea", "茶", "The third table title before Roar."),
    (18, "Roar", "轟く", "Enten bisects. Datenseki pops the customer."),
    (19, "Knight of Darkness", "闇の騎士", "Volume 3. The auction’s first coat."),
    (20, "The Kamunabi's Weapon", "神奈備の武器", "Hiyuki as a permission slip with a skeleton."),
    (21, "Lukewarm", "微温い", "The auction is not hot yet."),
    (22, "Deadlock", "拮抗", "First Deadlock. Japanese is not 均衡."),
    (23, "Storehouse", "蔵", "The real building gets a weekly name."),
    (24, "Hunters", "狩人", "Hakuri is not in this vocabulary yet."),
    (25, "Deal", "取引", "Rakuzaichi as a market sentence."),
    (26, "Confidence", "自信", "Someone else’s word. Hakuri’s comes later."),
    (27, "Mr. Inazuma", "Mr.イナズマ", "A person. A sister inside."),
    (28, "Breach", "突破口", "Volume 4 opener. A hole in the wall."),
    (29, "Selection", "取捨", "What the Kura keeps. What it throws away."),
    (30, "Intruders", "乱入者", "People not invited into the Kura."),
    (31, "Greeting", "挨拶", "The house starts answering Hakuri."),
    (32, "Wall", "壁", "The auction house as architecture."),
    (33, "Defend to the Death", "死守", "Tou vocabulary. Stone in the corridor."),
    (34, "Duty", "役目", "A Sazanami job title."),
    (35, "Cage", "檻", "Storehouse as a cage, not a religion, for one week."),
    (36, "Geniuses", "天才達", "Volume 4 closer before Fervent."),
    (37, "Equal", "対等", "The jacket word as a weekly title."),
    (38, "Race", "競合", "The Storehouse war is a clock."),
    (39, "Surpass!", "超えろ!!", "The magazine shouts at the pair."),
    (40, "The Tip", "一端", "One end of the auction. Kyora is still the head."),
    (41, "Fervent", "熱狂", "Volume 5’s spine weather."),
    (42, "Everything", "全部", "The building is being spent."),
    (43, "Fulfill", "全う", "Duty before the curtain. Tenri’s stone."),
    (44, "The Curtain Falls", "閉幕", "Prisoners leave. The firm ends."),
    (45, "What Comes Next", "これからの話", "Already a title. Uruha is next."),
    (46, "Unruly Punk", "勝手な野郎", "Volume 5 closer. Auction over."),
    (47, "Uruha", "漆羽", "The long book opens on a name."),
    (48, "The Kokugoku Steam Squad", "国獄 湯煙スクワッド", "A box advertises a bearer."),
    (49, "Deadlock", "均衡", "Second Deadlock. Steam Squad just got a grave."),
    (50, "Interception", "迎撃", "Transit has already started."),
    (51, "Samura", "座村", "The fastest bearer as a weekly pointing finger."),
    (52, "Just the Two of Us", "2人きり", "Iai house as ethics."),
    (53, "Darkness", "暗がり", "Not chapter 59’s Blackout."),
    (54, "Friendship", "友情", "Uruha and Samura before the cut."),
    (55, "Fight Alongside", "共闘", "Last title before 夜更け."),
    (56, "Daybreak", "夜更け", "Volume 6 spine. Small hours."),
    (57, "Collapse", "崩壊", "A train that does not hold."),
    (58, "Reunion", "再会", "Not chapter 130’s reunion."),
    (59, "Blackout", "暗転", "A stage word. Different from Darkness."),
    (60, "Resurrection", "黄泉がえり", "The long book’s return word."),
    (61, "Night Battle", "夜戦", "Volume 7’s spine as a weekly title."),
    (62, "Iori", "イヲリ", "Cargo becomes a name."),
    (63, "Car Chase", "車追跡", "Masumi job as a vehicle."),
    (64, "Become the Samurai", "ビカム侍", "English as a loan. Copy starts."),
    (65, "Imitate", "見真似", "Volume 7 closer. The method named."),
    (66, "Truth", "真実", "Volume 8 opener."),
    (67, "Kyoto Bloodshed Hotel", "ザ殺戮ホテル", "The building gets its title."),
    (68, "Metamorphosis", "変幻", "Play is about to wreck a floor."),
    (69, "The Guy with the Scar", "傷ノ男", "Kuguri as a face title."),
    (70, "Iai White Purity Style", "居合白禊流", "The school named in full."),
    (71, "Contest", "勝負", "A match title in a support-blade corridor."),
    (72, "Future", "未来", "First of two Futures."),
    (73, "Daybreak", "黎明", "Second Daybreak. Not 夜更け."),
    (74, "Dawn", "夜明け", "Volume 8 spine on the last weekly page."),
    (75, "Illusion", "幻想", "Volume 9 weather."),
    (76, "Banquet", "宴", "Respect or contempt, objects move or fall."),
    (77, "No Longer Relevant", "蚊帳の外", "Someone is outside the net."),
    (78, "Switch", "交代", "Contracts move. False death as door."),
    (79, "Threat!!", "曲者!!", "The magazine shouts again."),
    (80, "Secret Room", "密室", "A closed room in a long book."),
    (81, "Core", "主力", "Before Enten vs Tobimune."),
    (82, "Enten Vs. Tobimune", "淵天VS飛宗", "Lids already down on purpose."),
    (83, "The Enten", "淵天", "The retraction as a the."),
    (84, "The Wounded", "傷の者たち", "Scar and spend sharing a week."),
    (85, "Open", "開く", "A door title after the match."),
    (86, "Quickening", "胎動", "Volume 9 closer weather."),
    (87, "Phantoms", "亡霊", "Volume 10 opener."),
    (88, "The First Step", "皮切り", "A start word in a swordsmen book."),
    (89, "Battle Chaos", "乱戦", "The long book’s mess title."),
    (90, "Kiri", "斬ちゃん", "Odachi. The school’s no, ignored."),
    (91, "Natsuki", "奈ツ基", "Lightning Menace. Not Mei."),
    (92, "The Swordsmen", "剣士たち", "Jacket word as a weekly title."),
    (93, "Finishing Touches", "仕上げ", "A craft word in an assassination book."),
    (94, "The Second Arrow", "二の矢", "Something already flew."),
    (95, "Flood", "横溢", "Volume 10 closer weather."),
    (96, "Urgency", "切迫", "Volume 11 opener."),
    (97, "Vessel", "受け皿", "Yukisada as a building."),
    (98, "Ikuto Hagiwara, Worthless Commander", "無能隊長 萩原幾兎", "ACG cruelty reused as a title."),
    (99, '"Strongest"', "一番強い", "Press word, quoted."),
    (100, '"Sword Master"', "剣聖", "Press name, quoted."),
    (101, "Safe Zone", "安全地帯", "A box word after quotes."),
    (102, "What You Need to See", "視るべきモノ", "A looking title in a basement week."),
    (103, "Healing", "再生", "Not the Kyonagi word, a weekly one."),
    (104, '"Heroes"', "英雄", "Jacket word, quoted first."),
    (105, "Transformation", "変身", "Volume 11 closer."),
    (106, "Karma", "宿縁", "Volume 12 solicitation starts here."),
    (107, "This Moment", "この一瞬", "Before the Magatsumi meetings."),
    (108, "Enten vs. Magatsumi", "淵天 VS勾罪", "Retraction meets the war sword."),
    (109, "Tobimune vs. Magatsumi", "飛宗 VS勾罪", "Support blade against diet."),
    (110, "As a Swordsman", "剣士として", "A job title after two versus weeks."),
    (111, "Apex", "頂", "The peak word before the second Future."),
    (112, "Future", "未来", "Second Future. War-book door."),
    (113, "Rock", "石", "The island’s mineral as a title."),
    (114, "Kunishige Rokuhira", "六平国重", "Present tense on a buried man."),
    (115, "Swordsmith", "刀匠", "Part 1’s close word."),
    (116, "Princess", "姫", "Part 2 opens on an office."),
    (117, "The Irishima Talks", "杁島会談", "Property first. 118–120 stay table-only."),
    (121, "The Irishima Talks END", "杁島会談 終", "The table closes. Start is next."),
    (122, "Start", "始動", "The kiln commute begins."),
    (123, "Chiaki", "千晃", "The mother as a weekly pointing finger."),
    (124, "Powerless", "無力", "Before smelting names labor."),
    (125, "Smelting", "製鉄", "Datenseki into work."),
    (126, "Fire", "火", "A rest will sit after this labor."),
    (127, "Smelting, Part 2", "製鉄 弐", "The Japanese keeps counting."),
    (128, "Smelting, Part 3", "製鉄 参", "Still labor. Still no first-blade name."),
    (129, "Ironworks", "製鉄 肆", "Chiaki in the fire. Eyes open."),
    (130, "I'm Fine!", "大丈夫!", "Reunion on the clock."),
    (131, "Tipping Point", "転換点", "Bureau choice. 132 stays a door."),
]

VOL_OF = {}
for a, b, num, *_ in [
    (1, 8, 1), (9, 18, 2), (19, 27, 3), (28, 36, 4), (37, 46, 5),
    (47, 56, 6), (57, 65, 7), (66, 74, 8), (75, 86, 9), (87, 95, 10),
    (96, 105, 11), (106, 115, 12),
]:
    for i in range(a, b + 1):
        VOL_OF[i] = num

ARC_OF = {}
for a, b, name in [(1, 18, "Vs. Sojo"), (19, 46, "Rakuzaichi"), (47, 115, "Sword Bearer Assassination"), (116, 131, "Seitei War / Part 2")]:
    for i in range(a, b + 1):
        ARC_OF[i] = name


def insert(path: Path, html: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARK in text:
        return False
    needle = "</article>"
    if needle not in text:
        print("no article", path)
        return False
    text = text.replace(needle, html + "\n    </article>", 1)
    path.write_text(text, encoding="utf-8")
    return True


def chapter_block(n, en, jp, note):
    prev_n = n - 1 if n != 118 else 117
    next_n = n + 1 if n != 117 else 121
    if n == 121:
        next_n = 122
    vol = VOL_OF.get(n)
    vol_bit = f"Volume {vol} on this desk" if vol and vol <= 11 else ("Volume 12 solicitation" if vol == 12 else "Uncollected Part 2")
    arc = ARC_OF.get(n, "the weekly list")
    prev_link = f'<a href="chapter-{prev_n}.html">chapter {prev_n}</a>' if prev_n >= 1 and prev_n not in {118, 119, 120} else "the talks table"
    next_link = f'<a href="chapter-{next_n}.html">chapter {next_n}</a>' if next_n <= 131 and next_n not in {118, 119, 120} else ("the talks table" if n == 117 else '<a href="chapter-132.html">the chapter 132 door</a>')
    room = f"chapter-{n}.html"
    return f"""
    {MARK}
    <h2>This week on the register</h2>
    <p>{en} ({jp}) is chapter {n}. {note} {vol_bit}. Arc commute: {arc}. Neighbor titles: {prev_link}, then {next_link}. Official pages stay on VIZ and MANGA Plus. This room does not host the issue.</p>
    <p>Title collisions, if any, live on <a href="../world/title-collisions.html">title collisions</a> and the essays for <a href="../analysis/two-deadlocks.html">two Deadlocks</a>, <a href="../analysis/two-futures.html">two Futures</a>, and <a href="../analysis/two-daybreaks.html">two Daybreaks</a>. Named-person weeks are listed on <a href="../analysis/named-person-titles.html">chapters named for people</a>. The full table is <a href="chapters.html">the chapter index</a>.</p>
    <p>New desks this wave that touch this corridor: <a href="../characters/bonds.html">printed bonds</a>, <a href="../world/battle-index.html">fight desks</a>, <a href="../guide/quad-doors.html">quadruple wave</a>. Chapter 132 remains a publication door without a printed title here. Irishima 118–120 remain table-only.</p>
"""


CHAR_ADD = {
    "chihiro.html": (
        "This wave’s Chihiro pairs",
        "The son now has dedicated rooms with <a href=\"chihiro-and-kunishige.html\">Kunishige</a>, <a href=\"chihiro-and-hakuri.html\">Hakuri</a>, <a href=\"chihiro-and-hiyuki.html\">Hiyuki</a>, <a href=\"chihiro-and-shiba.html\">Shiba</a>, <a href=\"chihiro-and-char.html\">Char</a>, <a href=\"chihiro-and-sojo.html\">Sojo</a>, <a href=\"chihiro-and-samura.html\">Samura</a>, <a href=\"chihiro-and-uruha.html\">Uruha</a>, <a href=\"chihiro-and-hiruhiko.html\">Hiruhiko</a>, <a href=\"chihiro-and-iori.html\">Iori</a>, <a href=\"chihiro-and-kuguri.html\">Kuguri</a>, and <a href=\"chihiro-and-azami.html\">Azami</a>. Fight desks: <a href=\"../world/battle-chihiro-sojo.html\">vs Sojo</a>, <a href=\"../world/battle-enten-tobimune.html\">vs Tobimune</a>, <a href=\"../world/battle-enten-magatsumi.html\">vs Magatsumi</a>.",
    ),
    "kunishige.html": (
        "Kiln pairs",
        "See <a href=\"chihiro-and-kunishige.html\">the household</a>, <a href=\"shiba-and-kunishige.html\">Shiba</a>, <a href=\"azami-and-kunishige.html\">Azami</a>, <a href=\"subaru-and-kunishige.html\">Subaru</a>, and <a href=\"chiaki-and-kunishige.html\">Chiaki</a>. Chapter 114 titles him in the present. Ironworks is 129. The first blade stays unnamed.",
    ),
    "hakuri.html": (
        "Auction pairs",
        "<a href=\"chihiro-and-hakuri.html\">Chihiro</a>, <a href=\"hakuri-and-kyora.html\">Kyora</a>, <a href=\"hakuri-and-soya.html\">Soya</a>, <a href=\"hakuri-and-tenri.html\">Tenri</a>, <a href=\"hakuri-and-kudo.html\">Kudo</a>. Fights: <a href=\"../world/battle-hakuri-soya.html\">vs Soya</a>, <a href=\"../world/battle-rakuzaichi.html\">208th</a>.",
    ),
    "sojo.html": (
        "Customer pairs",
        "<a href=\"chihiro-and-sojo.html\">Chihiro</a>, <a href=\"sojo-and-char.html\">Char</a>, <a href=\"sojo-and-ibuki.html\">Ibuki</a>. He is not Hishaku. Bathhouse extras stay in the tankōbon: <a href=\"../fun/bathhouse-quest.html\">#1</a>, <a href=\"../fun/bathhouse-quest-2.html\">#2</a>.",
    ),
    "samura.html": (
        "Iai pairs",
        "<a href=\"chihiro-and-samura.html\">Chihiro</a>, <a href=\"uruha-and-samura.html\">Uruha</a>, <a href=\"samura-and-iori.html\">Iori</a>, <a href=\"ibuki-and-samura.html\">Ibuki</a>. Fights: <a href=\"../world/battle-senkutsuji.html\">Senkutsuji</a>, <a href=\"../world/battle-enten-tobimune.html\">Enten vs Tobimune</a>, <a href=\"../world/battle-tobimune-magatsumi.html\">Tobimune vs Magatsumi</a>.",
    ),
    "yura.html": (
        "Mind pairs",
        "<a href=\"yura-and-hiruhiko.html\">Hiruhiko</a>, <a href=\"yura-and-kasen.html\">Kasen</a>, <a href=\"yura-and-akemura.html\">Akemura</a>. Jobs list: <a href=\"../factions/hishaku-jobs.html\">Hishaku jobs</a>.",
    ),
    "ibuki.html": (
        "Original bearer pairs",
        "<a href=\"sojo-and-ibuki.html\">Sojo</a>, <a href=\"ibuki-and-natsuki.html\">Natsuki</a>, <a href=\"ibuki-and-hokuto.html\">Hokuto</a>, <a href=\"ibuki-and-samura.html\">Samura</a>. Chapter 132 is still a door, not a plot file.",
    ),
    "hiyuki.html": (
        "Permission pairs",
        "<a href=\"chihiro-and-hiyuki.html\">Chihiro</a>, <a href=\"hiyuki-and-tafuku.html\">Tafuku</a>. Auction clash: <a href=\"../world/battle-chihiro-hiyuki.html\">the auction desk</a>.",
    ),
    "chiaki.html": (
        "Princess pairs",
        "<a href=\"chiaki-and-kunishige.html\">Kunishige</a>, <a href=\"chiaki-and-giyu.html\">Giyu</a>, <a href=\"chiaki-and-shiba.html\">Shiba</a>. Office essay: <a href=\"../analysis/princess-office.html\">princess as office</a>.",
    ),
    "shiba.html": (
        "Guardian pairs",
        "<a href=\"chihiro-and-shiba.html\">Chihiro</a>, <a href=\"shiba-and-kunishige.html\">Kunishige</a>, <a href=\"hinao-and-shiba.html\">Hinao</a>, <a href=\"chiaki-and-shiba.html\">Chiaki</a>, <a href=\"mashiro-and-shiba.html\">Mashiro</a>.",
    ),
}


def main():
    n = 0
    for num, en, jp, note in CHAPTERS:
        path = ROOT / f"manga/chapter-{num}.html"
        if not path.exists():
            print("missing chapter", num)
            continue
        if insert(path, chapter_block(num, en, jp, note)):
            n += 1
            print("expanded chapter", num)

    c = 0
    for rel, (h2, p) in CHAR_ADD.items():
        path = ROOT / "characters" / rel
        html = f"\n    {MARK}\n    <h2>{h2}</h2>\n    <p>{p}</p>\n"
        if insert(path, html):
            c += 1
            print("expanded", rel)

    extras = {
        "world/battles.html": f'\n    {MARK}\n    <h2>Fight desks this wave</h2>\n    <p>Individual clash rooms now live on <a href="battle-index.html">fight desks</a>: raid, vs Sojo, ACG, Rakuzaichi, Hakuri vs Soya, Tenri’s stone, Sanso, Senkutsuji, hotel Iai, hotel Play, Enten vs Tobimune, HQ week, Enten vs Magatsumi, Tobimune vs Magatsumi, Chihiro and Hiyuki at auction.</p>\n',
        "world/locations.html": f'\n    {MARK}\n    <h2>Place satellites</h2>\n    <p>New rooms: <a href="workshop-cellar.html">cellar</a>, <a href="cafe-interior.html">cafe interior</a>, <a href="auction-floor.html">auction floor</a>, <a href="hotel-floors.html">hotel floors</a>, <a href="hq-basement.html">HQ basement</a>, <a href="sanso-kokugoku.html">Kokugoku</a>, <a href="senkutsuji-grounds.html">Senkutsuji grounds</a>, <a href="soga-house.html">Soga house</a>, <a href="irishima-table.html">talks table</a>, <a href="undersea-rooms.html">undersea rooms</a>.</p>\n',
        "world/techniques.html": f'\n    {MARK}\n    <h2>This wave’s kit essays</h2>\n    <p><a href="../analysis/three-count.html">The three-count</a> keeps Magatsumi’s exception honest. <a href="../analysis/color-dark.html">When color goes black</a> splits Mei Shred, Black Suzaku, and Magatsumi’s pantry. <a href="../guide/who-holds.html">Who holds what</a> is the beginner door onto the bearer register.</p>\n',
        "manga/volumes.html": f'\n    {MARK}\n    <h2>Reading rooms</h2>\n    <p>Each collected book now has a commute page: <a href="volume-1-read.html">1</a> <a href="volume-2-read.html">2</a> <a href="volume-3-read.html">3</a> <a href="volume-4-read.html">4</a> <a href="volume-5-read.html">5</a> <a href="volume-6-read.html">6</a> <a href="volume-7-read.html">7</a> <a href="volume-8-read.html">8</a> <a href="volume-9-read.html">9</a> <a href="volume-10-read.html">10</a> <a href="volume-11-read.html">11</a> <a href="volume-12-read.html">12 (solicited)</a>.</p>\n',
        "manga/chapters.html": f'\n    {MARK}\n    <h2>Arc maps</h2>\n    <p><a href="../arcs/vs-sojo-map.html">Vs. Sojo 1–18</a>. <a href="../arcs/rakuzaichi-map.html">Rakuzaichi 19–46</a>. <a href="../arcs/sword-bearer-map.html">Sword Bearer 47–115</a>. <a href="../arcs/seitei-war-map.html">Seitei War 116–131</a>. 118–120 stay unlinked. 132 stays a door.</p>\n',
        "analysis/index.html": "",  # wired separately
    }
    e = 0
    for rel, html in extras.items():
        if not html:
            continue
        if insert(ROOT / rel, html):
            e += 1
            print("expanded", rel)

    print("expand chapters", n, "chars", c, "extras", e)


if __name__ == "__main__":
    main()
