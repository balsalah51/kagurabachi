#!/usr/bin/env python3
"""October 2026 archive refresh.

Files chapter 132 as Misaka (巳坂) from the Wikipedia chapter list.
Chapter 133 stays a publication door (Jump 2026 #45, 4/5 October 2026).
No unpublished plot. No first-blade name. No 118-120 solo rooms.
No U+2014 em-dashes.
"""
from oct_lib import page, write_long, crumb_for, related, VIZ, PAGES


def chapter_132():
    body = f"""
  <p>Read it official: {VIZ}. Chapter 132 is titled “Misaka” (巳坂). VIZ’s listing is 27 September 2026. Weekly Shōnen Jump 2026 issue 44, on sale 28 September 2026, after the official 42/43 health skip. This page files the printed weekly word. It is not a substitute and not a leak desk.</p>
  <h2>What we print</h2>
  <p>The Wikipedia chapter list now prints the English title Misaka and the Japanese 巳坂. That is the family name already on this archive for <a href="../characters/ibuki.html">Ibuki Misaka</a> and <a href="../characters/natsuki.html">Natsuki Misaka</a>. Chapter 131 is <a href="chapter-131.html">Tipping Point</a> (転換点). The health notice that moved this issue from the 42/43 combined magazine sits on <a href="../fun/september-2026-rest.html">the September rest</a>.</p>
  <p>We do not recap the panels here. Official reading stays on VIZ and MANGA Plus. Neighbor titles: <a href="chapter-131.html">chapter 131</a>, then <a href="chapter-133.html">the chapter 133 door</a>. House rooms: <a href="../world/misaka-brothers.html">the brothers</a>, <a href="../world/kitakyushu.html">Kitakyushu</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
  <h2>This week on the register</h2>
  <p>Misaka is a name-week. The earlier name-weeks are on <a href="../analysis/named-person-titles.html">chapters named for people</a>. A title that is only a house is filed on <a href="../analysis/misaka-title.html">Misaka as a title</a>. The first Enchanted Blade is still unnamed on this desk. Irishima 118–120 remain table-only.</p>
    {related([("chapter-131.html", "Ch. 131"), ("chapter-133.html", "Ch. 133 door"), ("../characters/ibuki.html", "Ibuki"), ("../world/misaka-brothers.html", "Brothers"), ("../fun/jump-2026-44.html", "Issue 44"), ("../fun/september-2026-rest.html", "September rest"), ("chapters.html", "Index"), ("publication.html", "Publication")])}
"""
    write_long(
        "manga/chapter-132.html",
        "Kagurabachi Chapter 132 “Misaka”",
        "Kagurabachi chapter 132, Misaka (巳坂): Jump 2026 issue 44, VIZ 27 September 2026. Official reading on VIZ and MANGA Plus.",
        crumb_for("manga/chapter-132.html", "Chapter 132"),
        "the uncollected run · Seitei War / Part 2",
        "Chapter 132 - “Misaka”",
        "巳坂",
        "Jump 2026 #44. VIZ dated 27 September 2026. The weekly word is the house.",
        body,
        overwrite=True,
    )


def chapter_133():
    body = f"""
  <p>Read it official when it lands: {VIZ}. Chapter 133 is due Weekly Shōnen Jump 2026 issue 45, on sale 5 October 2026 in Japan, with the usual Sunday VIZ / MANGA Plus window on 4 October 2026. This page is a publication door. We do not invent the title or the panels.</p>
  <p>Chapter 132 is <a href="chapter-132.html">Misaka</a> (巳坂). The prior rest: <a href="../fun/september-2026-rest.html">September rest</a>. Issue room: <a href="../fun/jump-2026-45.html">issue 45</a>.</p>
    {related([("chapter-132.html", "Ch. 132 Misaka"), ("../fun/jump-2026-45.html", "Issue 45"), ("../fun/october-2026.html", "October 2026"), ("publication.html", "Publication"), ("index.html", "Manga guide"), ("chapters.html", "Chapters"), ("synopses.html", "Synopses"), ("part-2.html", "Part 2")])}
"""
    write_long(
        "manga/chapter-133.html",
        "Kagurabachi Chapter 133 | Jump 2026 Issue 45",
        "Chapter 133’s magazine door: Weekly Shōnen Jump 2026 issue 45, on sale 5 October 2026. Title not printed on this desk.",
        crumb_for("manga/chapter-133.html", "Chapter 133’s door"),
        "Jump 45 · door",
        "Chapter 133’s door",
        "第133話",
        "A return date. Not a weekly title. We will not invent one.",
        body,
        overwrite=True,
    )


def rooms():
    page(
        "fun/jump-2026-45.html",
        "Jump 2026 Issue 45 | Chapter 133’s Date",
        "Weekly Shōnen Jump 2026 #45, on sale 5 October 2026, is chapter 133’s magazine date. Title not printed here.",
        "Fun · #45",
        "Jump 2026 issue 45",
        "2026年45号",
        "5 October 2026. A date, not a title.",
        [
            (
                "The next magazine",
                [
                    "Issue 44 held <a href=\"../manga/chapter-132.html\">Misaka</a> after the 42/43 health skip. Issue 45 is the next weekly door: chapter 133, on sale 5 October 2026. The usual Sunday window for VIZ and MANGA Plus is 4 October. We do not invent the weekly title.",
                    "Prior printed word: <a href=\"../manga/chapter-132.html\">Misaka</a>. Prior issue: <a href=\"jump-2026-44.html\">issue 44</a>. Month desk: <a href=\"october-2026.html\">October 2026</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133 door"),
            ("../manga/chapter-132.html", "Misaka"),
            ("jump-2026-44.html", "Issue 44"),
            ("october-2026.html", "October"),
            ("september-2026-rest.html", "September rest"),
            ("hiatus.html", "Rests"),
        ],
    )
    page(
        "fun/october-2026.html",
        "October 2026 | After Misaka | Kagurabachi",
        "October 2026 on the Kagurabachi desk: chapter 132 Misaka is printed, chapter 133 is a date, English volume 9 is still ahead.",
        "Fun · 10月",
        "October 2026",
        "2026年10月",
        "A titled house, then a date, then an English spine still in the mail.",
        [
            (
                "What is already printed",
                [
                    "Chapter 132, <a href=\"../manga/chapter-132.html\">Misaka</a> (巳坂), landed in Jump 2026 #44. Chapter 131 remains <a href=\"../manga/chapter-131.html\">Tipping Point</a>. Volume 12 is on Japanese shelves as of 4 September 2026. The first Enchanted Blade is still unnamed here.",
                    "Chapter 133 is <a href=\"../manga/chapter-133.html\">a door</a> for Jump 2026 #45 (5 October). English volume 9 is listed for 3 November 2026. Cypic’s April 2027 series is unchanged. This month desk files those clocks. It does not invent next week’s title.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/chapter-133.html", "Ch. 133 door"),
            ("jump-2026-45.html", "Issue 45"),
            ("../collectibles/english-volume-9.html", "EN vol. 9"),
            ("../guide/october-update.html", "October update"),
            ("year-2026.html", "2026"),
        ],
    )
    page(
        "guide/october-update.html",
        "October 2026 Update | Kagurabachi Archive",
        "What this archive refreshed in October 2026: Misaka as a titled room, a 133 door, voice rooms, English volume doors, and stale volume counts.",
        "Guide · 更新",
        "October update",
        "十月の更新",
        "The door became a title. The next issue is a door again.",
        [
            (
                "What changed",
                [
                    "Wikipedia’s chapter list now prints chapter 132 as Misaka (巳坂). This desk files that word, the Jump 2026 #44 date, and the VIZ 27 September listing. Chapter 133 stays untitled here. Irishima 118–120 stay table-only. The first blade stays unnamed.",
                    "Stale solicitation language for Japanese volume 12 is corrected: the book is out. English volume 8 is the last printed VIZ trade on this pass; volume 9 is 3 November 2026. Anime voices now include Miku Itō as Hinao and Miyari Nemoto as Char, beside Kimura, Seki, and Konishi.",
                    "New doors this wave start at <a href=\"current-week.html\">the current week</a>, <a href=\"../analysis/misaka-title.html\">Misaka as a title</a>, and <a href=\"../fun/october-2026.html\">October 2026</a>. Official reading stays on VIZ and MANGA Plus.",
                ],
            )
        ],
        [
            ("current-week.html", "Current week"),
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/chapter-133.html", "133 door"),
            ("quad-doors.html", "Quadruple wave"),
            ("mega-doors.html", "Mega doors"),
            ("official-only.html", "Official-only"),
        ],
    )
    page(
        "guide/current-week.html",
        "Current Week | Kagurabachi Archive",
        "What is current on this desk: chapter 132 Misaka is the latest titled room. Chapter 133 is due Jump 2026 #45.",
        "Guide · 今週",
        "Current week",
        "今週",
        "Misaka is printed. The next magazine is not.",
        [
            (
                "As of 3 October 2026",
                [
                    "Latest titled room: <a href=\"../manga/chapter-132.html\">chapter 132, Misaka</a> (巳坂), Jump 2026 #44, VIZ 27 September 2026. Latest titled prior: <a href=\"../manga/chapter-131.html\">Tipping Point</a>. Next magazine: <a href=\"../manga/chapter-133.html\">chapter 133’s door</a>, Jump 2026 #45.",
                    "VIZ’s public list was still showing chapters 130–132 as the free window on this pass. That window moves. Read official. Do not use this page as a leak desk. Part 2 still runs from <a href=\"../manga/part-2.html\">Princess</a>. Volume 12 is a Japanese object, not an English one yet.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/chapter-133.html", "133 door"),
            ("../manga/viz-free-now.html", "VIZ free window"),
            ("october-update.html", "October update"),
            ("reading-order.html", "How to read"),
            ("../manga/chapters.html", "Index"),
        ],
    )
    page(
        "manga/viz-free-now.html",
        "VIZ Free Window | Kagurabachi",
        "VIZ’s public Kagurabachi list on this October 2026 pass showed chapters 130–132 free. The window moves. Read official.",
        "Manga · FREE",
        "VIZ free window",
        "無料公開",
        "A listing, not a promise. The magazine still owns the week.",
        [
            (
                "What the public list showed",
                [
                    "On 3 October 2026 the VIZ Shonen Jump chapter list showed Ch. 130, Ch. 131, and Ch. 132 as FREE, with “New chapter coming in 2 days.” That countdown is chapter 133’s Sunday window. Older issues sat behind the join wall.",
                    "This desk does not host those pages. It files that the latest titled room is <a href=\"chapter-132.html\">Misaka</a> and that <a href=\"chapter-133.html\">133</a> is still a date. When the free window slides, this paragraph is a snapshot, not a store.",
                ],
            )
        ],
        [
            ("chapter-130.html", "I'm Fine!"),
            ("chapter-131.html", "Tipping Point"),
            ("chapter-132.html", "Misaka"),
            ("chapter-133.html", "133 door"),
            ("../guide/current-week.html", "Current week"),
            ("publication.html", "Publication"),
        ],
    )
    page(
        "manga/uncollected-after-12.html",
        "Uncollected After Volume 12 | Kagurabachi",
        "Chapters 114–132 sit after Volume 12’s printed map on this desk. Misaka is the latest titled weekly. 118–120 stay table-only.",
        "Manga · 未収録",
        "Uncollected after 12",
        "12巻以後",
        "The tankōbon stopped. The magazine did not.",
        [
            (
                "What is still weekly-only",
                [
                    "Volume 12 (4 September 2026, ISBN 978-4-08-885177-8) is the last Japanese spine on this desk. Wikipedia’s volume map prints Karma through Rock on that book, then lists 114–132 as not yet in tankōbon format. This room is that leftover list, not a pirate shelf.",
                    "114 Kunishige Rokuhira. 115 Swordsmith. 116 Princess. 117 The Irishima Talks. 118–120 stay table-only here. 121 END. 122 Start. 123 Chiaki. 124 Powerless. 125–129 the smelting run. 130 I'm Fine!. 131 Tipping Point. 132 Misaka. 133 is a door.",
                    "Read them official. File titles on <a href=\"chapters.html\">the chapter index</a>. The war book’s long cut is <a href=\"part-2.html\">Part 2</a>.",
                ],
            )
        ],
        [
            ("chapter-132.html", "Misaka"),
            ("volume-12.html", "Volume 12"),
            ("part-2.html", "Part 2"),
            ("chapters.html", "Index"),
            ("../world/irishima-talks.html", "Talks"),
            ("../guide/current-week.html", "Current week"),
        ],
    )
    page(
        "analysis/misaka-title.html",
        "Misaka as a Title | Kagurabachi Essay",
        "Chapter 132 is titled Misaka (巳坂): a house name as a weekly word, after Tipping Point and a health skip.",
        "Essay · 巳坂",
        "Misaka as a title",
        "タイトルの巳坂",
        "A pointing finger at a family already on the register.",
        [
            (
                "Name-weeks",
                [
                    "The book has already titled weeks Uruha, Samura, Iori, Kiri, Natsuki, Kunishige Rokuhira, and Chiaki. Chapter 132’s Misaka is the house, not a given name. Ibuki and Natsuki already share 巳坂 on this archive. Natsuki had his own week at 91.",
                    "We file the word. We do not recap the issue. The brothers room, Cloud Gouger, Kitakyushu, and the Sorcery Bureau pages already hold the printed jobs around that name. See <a href=\"named-person-titles.html\">chapters named for people</a> and <a href=\"../fun/house-name-weeks.html\">house-name weeks</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Ch. 132"),
            ("named-person-titles.html", "Named weeks"),
            ("../fun/house-name-weeks.html", "House names"),
            ("../characters/ibuki.html", "Ibuki"),
            ("../characters/natsuki.html", "Natsuki"),
            ("../world/misaka-brothers.html", "Brothers"),
        ],
    )
    page(
        "analysis/after-the-skip.html",
        "After the September Skip | Kagurabachi",
        "Hokazono’s illness moved chapter 132 from Jump 2026 42/43 to issue 44. The titled return is Misaka.",
        "Essay · 休載の後",
        "After the skip",
        "休載のあと",
        "A recovered author. A house name. Not a leak.",
        [
            (
                "The printed sequence",
                [
                    "The official account said serialization scheduled for Weekly Shōnen Jump 2026 issue 42/43 combined (on sale 14 September) would rest because of the author’s sudden illness, and that Takeru Hokazono had already recovered. Continuation: issue 44, 28 September. That issue’s weekly word is now printed as Misaka.",
                    "File the notice on <a href=\"../fun/september-2026-rest.html\">the September rest</a>. File the title on <a href=\"../manga/chapter-132.html\">chapter 132</a>. File the next date on <a href=\"../manga/chapter-133.html\">chapter 133</a>. Rest weeks are print facts. They are not fake chapters. See <a href=\"rest-weeks.html\">rest weeks as print</a>.",
                ],
            )
        ],
        [
            ("../fun/september-2026-rest.html", "September rest"),
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/chapter-133.html", "133 door"),
            ("rest-weeks.html", "Rest weeks"),
            ("../fun/hiatus.html", "2026 rest"),
            ("../manga/publication.html", "Publication"),
        ],
    )
    page(
        "analysis/titles-through-132.html",
        "Titles Through Misaka | Kagurabachi",
        "Part 2’s printed weekly words from Princess through Misaka. Tipping Point, then a house name.",
        "Essay · 話数",
        "Titles through Misaka",
        "姫から巳坂",
        "Rank, talks, kiln, reunion, a bureau word, then a family.",
        [
            (
                "The run",
                [
                    "116 Princess. 117 The Irishima Talks. 118–120 table-only here. 121 END. 122 Start. 123 Chiaki. 124 Powerless. 125 Smelting. 126 Fire. 127–129 the numbered kiln. 130 I'm Fine!. 131 Tipping Point. 132 Misaka.",
                    "The meals and quoted press of Part 1 taught the method. Part 2 spends that method on a rank, a table, a kiln, and then a house. We still do not name the first blade. The next magazine is still a door. Index: <a href=\"../manga/chapters.html\">chapters</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/part-2.html", "Part 2"),
            ("named-person-titles.html", "Named weeks"),
            ("../fun/chapter-titles.html", "Title list"),
            ("../arcs/seitei-war-map.html", "War map"),
            ("../manga/uncollected-after-12.html", "Uncollected"),
        ],
    )
    page(
        "fun/house-name-weeks.html",
        "House-Name Weeks | Kagurabachi Titles",
        "Weekly titles that are family names: Misaka, and the earlier given-name weeks that already pointed at houses.",
        "Fun · 家名",
        "House-name weeks",
        "家の話",
        "Sometimes the title is the clan, not the given name.",
        [
            (
                "What is printed",
                [
                    "Chapter 132 is Misaka. That is 巳坂, the house Ibuki and Natsuki already share. Chapter 91 was Natsuki, the younger brother’s given name. Chapter 47 Uruha, 51 Samura, 62 Iori, 90 Kiri, 114 Kunishige Rokuhira, 123 Chiaki are people. Chapter 8 spends a full sentence on Norisaku Madoka.",
                    "A house-only title is rarer. This desk files it as a pointing finger, not as a recap. See <a href=\"../analysis/misaka-title.html\">Misaka as a title</a> and <a href=\"chapter-titles.html\">how titles work</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Misaka"),
            ("../analysis/misaka-title.html", "Essay"),
            ("chapter-titles.html", "Titles"),
            ("../world/misaka-house.html", "The house"),
            ("../characters/ibuki.html", "Ibuki"),
            ("../analysis/named-person-titles.html", "Named people"),
        ],
    )
    page(
        "characters/shiba-and-ibuki.html",
        "Shiba and Ibuki | Kagurabachi",
        "Togo Shiba of the Sorcery Bureau and Ibuki Misaka of Kitakyushu: printed jobs that share a war, a house title, and no invented 132 recap.",
        "Characters · 対",
        "Shiba and Ibuki",
        "柴と巳坂",
        "A bureau friend. A Kitakyushu swordsman. The weekly word is the house.",
        [
            (
                "Printed jobs",
                [
                    "Shiba grew up alongside Kunishige, guarded the Soga, joined the Kamunabi in the war, and left after the smith hid. Before that war he is already a Sorcery Bureau man who will steal Datenseki for a picky dealer. Ibuki is Cloud Gouger’s original bearer, Samura’s equal, Kitakyushu-born, at odds with that same bureau, later retired, later killed by Hokuto.",
                    "Chapter 132’s title is Misaka. This pair room does not recap those panels. It files the two résumés the title now sits between. See <a href=\"shiba.html\">Shiba</a>, <a href=\"ibuki.html\">Ibuki</a>, and <a href=\"../factions/sorcery-bureau-and-misaka.html\">the bureau and the house</a>.",
                ],
            )
        ],
        [
            ("shiba.html", "Shiba"),
            ("ibuki.html", "Ibuki"),
            ("../manga/chapter-132.html", "Misaka"),
            ("../world/kitakyushu.html", "Kitakyushu"),
            ("../factions/sorcery-bureau-and-misaka.html", "Bureau"),
            ("bonds.html", "Bonds"),
        ],
    )
    page(
        "characters/ibuki-and-kunishige.html",
        "Ibuki and Kunishige | Kagurabachi",
        "Kunishige Rokuhira chose Ibuki Misaka for Cloud Gouger. The smith, the weather sword, and a house the magazine later uses as a title.",
        "Characters · 対",
        "Ibuki and Kunishige",
        "伊武基と国重",
        "A selective smith. One brother got the contract.",
        [
            (
                "The choice",
                [
                    "Kunishige sold few swords before the war because he would not sell to people he could not stand. The Enchanted Blade bearers are that ethic written in Datenseki. Ibuki received Cloud Gouger. Natsuki, nearly invincible beside him, did not. Uruha received Kumeyuri when Natsuki wanted it.",
                    "After the war Kunishige hid the six blades and made a seventh with his son. Ibuki put the sword down and was murdered so the contract would open. Chapter 132’s title is the house the smith once signed. This page does not recap the issue. See <a href=\"ibuki.html\">Ibuki</a> and <a href=\"kunishige.html\">Kunishige</a>.",
                ],
            )
        ],
        [
            ("ibuki.html", "Ibuki"),
            ("kunishige.html", "Kunishige"),
            ("../blades/cloud-gouger.html", "Cloud Gouger"),
            ("../manga/chapter-132.html", "Misaka"),
            ("natsuki.html", "Natsuki"),
            ("bonds.html", "Bonds"),
        ],
    )
    page(
        "world/kitakyushu.html",
        "Kitakyushu | Kagurabachi",
        "Kitakyushu is the printed hometown where Ibuki Misaka fought alongside Natsuki before Cloud Gouger’s contract.",
        "World · 北九州",
        "Kitakyushu",
        "北九州",
        "A hometown on the register. Not a tourist page.",
        [
            (
                "What is printed",
                [
                    "Ibuki was ferocious in his younger years and often fought in his hometown of Kitakyushu alongside his younger brother Natsuki. That sentence is why this desk has a place room. The brothers’ combined skill is the wartime rumor. Lightning Menace stays Natsuki’s innate art. Cloud Gouger is the contract only one of them received.",
                    "Ibuki’s actions put him at odds with the Sorcery Bureau. After the war he abandoned swordsmanship. Hokuto killed the retired man. Chapter 132’s title is the house that city already knew. We do not invent a street map. See <a href=\"misaka-brothers.html\">the brothers</a> and <a href=\"misaka-house.html\">the house</a>.",
                ],
            )
        ],
        [
            ("../characters/ibuki.html", "Ibuki"),
            ("../characters/natsuki.html", "Natsuki"),
            ("misaka-brothers.html", "Brothers"),
            ("misaka-house.html", "House"),
            ("../manga/chapter-132.html", "Misaka"),
            ("index.html", "World"),
        ],
    )
    page(
        "world/misaka-house.html",
        "The Misaka House | 巳坂 | Kagurabachi",
        "巳坂 is the printed family name of Ibuki and Natsuki, and the weekly title of chapter 132.",
        "World · 巳坂",
        "The Misaka house",
        "巳坂家",
        "Two brothers. One contract. One magazine word.",
        [
            (
                "The name",
                [
                    "Ibuki Misaka (巳坂 伊武基) is Cloud Gouger’s original bearer. Natsuki Misaka (巳坂奈ツ基) is the Kamunabi squadron leader with Lightning Menace who wanted Kumeyuri and now wants Hokuto. Chapter 91 already spent a week on the younger brother’s given name. Chapter 132 spends a week on the house.",
                    "This is not a clan page in the Soga or Sazanami sense. No printed Misaka technique list beyond Natsuki’s Raiku and the weather sword Ibuki signed. The useful doors are <a href=\"misaka-brothers.html\">the brothers</a>, <a href=\"kitakyushu.html\">Kitakyushu</a>, and <a href=\"../manga/chapter-132.html\">the titled week</a>.",
                ],
            )
        ],
        [
            ("../characters/ibuki.html", "Ibuki"),
            ("../characters/natsuki.html", "Natsuki"),
            ("misaka-brothers.html", "Brothers"),
            ("../analysis/misaka-title.html", "Title essay"),
            ("../manga/chapter-132.html", "Ch. 132"),
            ("../world/lightning-menace.html", "Raiku"),
        ],
    )
    page(
        "factions/sorcery-bureau-and-misaka.html",
        "Sorcery Bureau and the Misaka House | Kagurabachi",
        "Ibuki Misaka’s actions put him at odds with the Sorcery Bureau, the pre-war office that later becomes the Kamunabi.",
        "Factions · 魔術局",
        "Bureau and Misaka",
        "局と巳坂",
        "The office that becomes the Kamunabi already had a problem with one swordsman.",
        [
            (
                "Printed tension",
                [
                    "The Sorcery Bureau (魔術局) is the government sorcery office before the Seitei War. It is restructured through the Counter-Sorcery Army into the Kamunabi. Shiba and Mashiro work there. Hasumi runs a secret Datenseki lab. Ibuki, ferocious in Kitakyushu, is printed as at odds with that office.",
                    "Chapter 132’s title is the house. This page does not recap the issue. It files the résumé collision: a bureau that wants control of dangerous swordsmen, and a bearer Kunishige will later trust with weather. See <a href=\"../characters/shiba-and-ibuki.html\">Shiba and Ibuki</a> and <a href=\"kamunabi.html\">Kamunabi</a>.",
                ],
            )
        ],
        [
            ("kamunabi.html", "Kamunabi"),
            ("../characters/ibuki.html", "Ibuki"),
            ("../characters/shiba.html", "Shiba"),
            ("../characters/shiba-and-ibuki.html", "The pair"),
            ("../world/kitakyushu.html", "Kitakyushu"),
            ("../manga/chapter-132.html", "Misaka"),
        ],
    )
    page(
        "collectibles/english-volume-8.html",
        "Kagurabachi English Volume 8 | VIZ",
        "VIZ Kagurabachi Volume 8, 4 August 2026, ISBN 978-1-9747-1650-0. The hotel book in English cloth.",
        "Collectibles · EN 8",
        "English volume 8",
        "英語版 8",
        "4 August 2026. The hotel on a VIZ spine.",
        [
            (
                "The object",
                [
                    "VIZ Volume 8, 4 August 2026, ISBN 978-1-9747-1650-0. The Japanese book (4 July 2025, ISBN 978-4-08-884566-1) is the Kyoto Bloodshed Hotel corridor: Truth through Dawn. English trails the Japanese jacket by about a year. Shop stays off character pages.",
                    "Next English spine: <a href=\"english-volume-9.html\">volume 9</a>, listed 3 November 2026. Japanese volume 12 is already out. Parallel cloth: <a href=\"../fun/english-volumes.html\">English volumes</a>.",
                ],
            )
        ],
        [
            ("../manga/volume-8.html", "JP vol. 8"),
            ("english-volume-9.html", "EN vol. 9"),
            ("../fun/english-volumes.html", "English desk"),
            ("../manga/volume-8-read.html", "Read vol. 8"),
            ("shop.html", "Shop"),
            ("index.html", "Collectibles"),
        ],
    )
    page(
        "collectibles/english-volume-9.html",
        "Kagurabachi English Volume 9 | VIZ",
        "VIZ Kagurabachi Volume 9 is listed for 3 November 2026, ISBN 978-1-9747-6845-5. A date, not a recap.",
        "Collectibles · EN 9",
        "English volume 9",
        "英語版 9",
        "3 November 2026. Still ahead of this desk.",
        [
            (
                "The solicitation",
                [
                    "VIZ Volume 9 is listed for 3 November 2026, ISBN 978-1-9747-6845-5. The Japanese book (3 October 2025, ISBN 978-4-08-884653-8) is the hotel’s aftermath into the headquarters assault: Illusion through Open. This page is a date. We do not invent a VIZ jacket essay before the object is in hand.",
                    "Prior English: <a href=\"english-volume-8.html\">volume 8</a>, 4 August 2026. Japanese volume 12 is already on shelves. See <a href=\"../fun/english-volumes.html\">the English desk</a>.",
                ],
            )
        ],
        [
            ("../manga/volume-9.html", "JP vol. 9"),
            ("english-volume-8.html", "EN vol. 8"),
            ("../fun/english-volumes.html", "English desk"),
            ("../manga/volume-9-read.html", "Read vol. 9"),
            ("../fun/october-2026.html", "October"),
            ("shop.html", "Shop"),
        ],
    )
    page(
        "media/kimura.html",
        "Taihi Kimura as Chihiro | Kagurabachi Anime",
        "Taihi Kimura is the announced Cypic series voice of Chihiro Rokuhira for the April 2027 Kagurabachi anime.",
        "Media · CV",
        "Taihi Kimura",
        "木村太飛",
        "The 2027 Chihiro. A different throat from the voiced comic.",
        [
            (
                "The credit",
                [
                    "Taihi Kimura is Chihiro Rokuhira in Cypic’s television series, scheduled for April 2027. The voiced comic already assigned Shoya Ishige to the same role. Keep the two lists separate. Official site: <a href=\"https://anime.kagurabachi.jp/\">anime.kagurabachi.jp</a>.",
                    "The rest of the announced Cypic cast on this pass: Tomokazu Seki as Kunishige, Katsuyuki Konishi as Shiba, Miku Itō as Hinao, Miyari Nemoto as Char. Full roll: <a href=\"../fun/voices.html\">voices</a>.",
                ],
            )
        ],
        [
            ("../characters/chihiro.html", "Chihiro"),
            ("../fun/voices.html", "Voices"),
            ("ishige.html", "Ishige, comic"),
            ("anime.html", "Anime"),
            ("staff.html", "Staff"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/konishi.html",
        "Katsuyuki Konishi as Shiba | Kagurabachi Anime",
        "Katsuyuki Konishi is the announced Cypic series voice of Togo Shiba for the April 2027 Kagurabachi anime.",
        "Media · CV",
        "Katsuyuki Konishi",
        "小西克幸",
        "The 2027 Shiba. Teleport, mouth, extraction.",
        [
            (
                "The credit",
                [
                    "Katsuyuki Konishi is Togo Shiba in the Cypic series. The voiced comic assigned Jun Fukushima to the same role. Two objects. One uncle in the booth.",
                    "Shiba’s printed job is teleportation, Soga-guardian youth, bureau war, and the friend who still extracts Chihiro. See <a href=\"../characters/shiba.html\">Shiba</a> and <a href=\"../fun/voices.html\">voices</a>.",
                ],
            )
        ],
        [
            ("../characters/shiba.html", "Shiba"),
            ("../fun/voices.html", "Voices"),
            ("kimura.html", "Kimura"),
            ("seki.html", "Seki"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/seki.html",
        "Tomokazu Seki as Kunishige | Kagurabachi Anime",
        "Tomokazu Seki is the announced Cypic series voice of Kunishige Rokuhira for the April 2027 Kagurabachi anime.",
        "Media · CV",
        "Tomokazu Seki",
        "関智一",
        "The 2027 smith. Impossible eyes.",
        [
            (
                "The credit",
                [
                    "Tomokazu Seki is Kunishige Rokuhira in the Cypic series. The voiced comic assigned Kenta Fujimaki to the same role. The war book will ask the 2027 voice to be a picky dealer who barely eats before it asks him to be a ghost in a cellar.",
                    "See <a href=\"../characters/kunishige.html\">Kunishige</a> and <a href=\"../fun/voices.html\">voices</a>.",
                ],
            )
        ],
        [
            ("../characters/kunishige.html", "Kunishige"),
            ("../fun/voices.html", "Voices"),
            ("kimura.html", "Kimura"),
            ("fujimaki.html", "Fujimaki, comic"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/ito-miku.html",
        "Miku Ito as Hinao | Kagurabachi Anime",
        "Miku Itō is the announced Cypic series voice of Hinao for the April 2027 Kagurabachi anime.",
        "Media · CV",
        "Miku Ito",
        "伊藤美来",
        "The 2027 cafe. A different throat from the voiced comic.",
        [
            (
                "The credit",
                [
                    "Miku Itō is Hinao in the Cypic series (announced 28 August 2026). The voiced comic already assigned Akari Tadano to the same role. Cafe Haru Haru is the printed room: coffee, introductions, yakuza and corporations who need sorcerers.",
                    "Keep the comic quartet and the 2027 roll on separate lists. See <a href=\"../characters/hinao.html\">Hinao</a> and <a href=\"../fun/voices.html\">voices</a>.",
                ],
            )
        ],
        [
            ("../characters/hinao.html", "Hinao"),
            ("../fun/voices.html", "Voices"),
            ("tadano.html", "Tadano, comic"),
            ("nemoto.html", "Nemoto"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/nemoto.html",
        "Miyari Nemoto as Char | Kagurabachi Anime",
        "Miyari Nemoto is the announced Cypic series voice of Char Kyonagi for the April 2027 Kagurabachi anime.",
        "Media · CV",
        "Miyari Nemoto",
        "根本京里",
        "The 2027 last Kyonagi. Announced with Hinao.",
        [
            (
                "The credit",
                [
                    "Miyari Nemoto is Char Kyonagi in the Cypic series (announced 28 August 2026, same notice as Miku Itō’s Hinao). The voiced comic has not been filed here as a Char credit. The printed job is the last Kyonagi, regeneration, Sojo’s experiment, and the girl Chihiro will not spend.",
                    "See <a href=\"../characters/char.html\">Char</a> and <a href=\"../fun/voices.html\">voices</a>. Birthday on this desk: 21 December.",
                ],
            )
        ],
        [
            ("../characters/char.html", "Char"),
            ("../fun/voices.html", "Voices"),
            ("ito-miku.html", "Itō"),
            ("kimura.html", "Kimura"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/ishige.html",
        "Shoya Ishige as Chihiro | Voiced Comic",
        "Shoya Ishige is Chihiro Rokuhira in the 2024 Kagurabachi voiced comic, a different object from the 2027 Cypic series.",
        "Media · ボイスコミック",
        "Shoya Ishige",
        "石毛翔弥",
        "The comic Chihiro. January 2024, not April 2027.",
        [
            (
                "The credit",
                [
                    "Shogakukan-Shueisha Productions released a voiced comic for the new Jump titles in January 2024. Shoya Ishige is Chihiro there. Taihi Kimura is Chihiro in Cypic’s series. Two throats. One goldfish bowl.",
                    "Comic roll on this desk: Ishige (Chihiro), Kenta Fujimaki (Kunishige), Jun Fukushima (Shiba), Akari Tadano (Hinao). Series roll: Kimura, Seki, Konishi, Itō, Nemoto.",
                ],
            )
        ],
        [
            ("kimura.html", "Kimura, series"),
            ("../media/voiced-comic.html", "Voiced comic"),
            ("../fun/voices.html", "Voices"),
            ("../characters/chihiro.html", "Chihiro"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/fujimaki.html",
        "Kenta Fujimaki as Kunishige | Voiced Comic",
        "Kenta Fujimaki is Kunishige Rokuhira in the 2024 Kagurabachi voiced comic.",
        "Media · ボイスコミック",
        "Kenta Fujimaki",
        "藤巻健太",
        "The comic smith. Seki is the 2027 smith.",
        [
            (
                "The credit",
                [
                    "Kenta Fujimaki announced the Kunishige credit for the YouTube voiced comic in February 2024. Tomokazu Seki is the Cypic series credit. Keep them on separate lists.",
                    "See <a href=\"seki.html\">Seki</a> and <a href=\"../characters/kunishige.html\">Kunishige</a>.",
                ],
            )
        ],
        [
            ("seki.html", "Seki, series"),
            ("ishige.html", "Ishige"),
            ("../fun/voices.html", "Voices"),
            ("../characters/kunishige.html", "Kunishige"),
            ("voiced-comic.html", "Voiced comic"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/tadano.html",
        "Akari Tadano as Hinao | Voiced Comic",
        "Akari Tadano is Hinao in the 2024 Kagurabachi voiced comic. Miku Itō is the 2027 series credit.",
        "Media · ボイスコミック",
        "Akari Tadano",
        "只野あきら",
        "The comic cafe. Itō is the 2027 cafe.",
        [
            (
                "The credit",
                [
                    "Akari Tadano is Hinao in the voiced comic. Miku Itō is Hinao in the Cypic series. Cafe Haru Haru had a voice before the 2027 roll captioned her again.",
                    "See <a href=\"ito-miku.html\">Itō</a> and <a href=\"../characters/hinao.html\">Hinao</a>.",
                ],
            )
        ],
        [
            ("ito-miku.html", "Itō, series"),
            ("../characters/hinao.html", "Hinao"),
            ("../fun/voices.html", "Voices"),
            ("voiced-comic.html", "Voiced comic"),
            ("anime.html", "Anime"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/crunchyroll.html",
        "Crunchyroll | Kagurabachi Anime License",
        "Crunchyroll will stream the Kagurabachi anime worldwide except Japan, mainland China, North Korea, and South Korea.",
        "Media · 配信",
        "Crunchyroll",
        "クランチロール",
        "The listed worldwide door, with the listed exceptions.",
        [
            (
                "The license",
                [
                    "Crunchyroll’s June 2026 announcement is the English-language streaming door this desk files: worldwide except Japan, mainland China, North Korea, and South Korea. Muse Communication holds South and Southeast Asia. Broadcast remains April 2027. Cypic, Takeuchi, Sasaki.",
                    "How to watch without inventing a cour: <a href=\"../guide/watch.html\">the watch page</a>. Official hub: <a href=\"https://anime.kagurabachi.jp/\">anime.kagurabachi.jp</a>.",
                ],
            )
        ],
        [
            ("anime.html", "Anime"),
            ("muse-asia.html", "Muse"),
            ("../guide/watch.html", "How to watch"),
            ("staff.html", "Staff"),
            ("../fun/world-tour.html", "World tour"),
            ("index.html", "Media"),
        ],
    )
    page(
        "media/muse-asia.html",
        "Muse Communication | Kagurabachi Anime",
        "Muse Communication licensed the Kagurabachi anime for South and Southeast Asia.",
        "Media · 配信",
        "Muse Communication",
        "ミューズ",
        "The SEA door. Crunchyroll is the other map.",
        [
            (
                "The license",
                [
                    "Muse Communication’s April 2026 license covers South and Southeast Asia. Crunchyroll’s later notice covers the rest of the listed world, minus Japan, mainland China, North Korea, and South Korea. Two doors. One April 2027 broadcast.",
                    "See <a href=\"crunchyroll.html\">Crunchyroll</a> and <a href=\"../guide/watch.html\">how to watch</a>.",
                ],
            )
        ],
        [
            ("crunchyroll.html", "Crunchyroll"),
            ("anime.html", "Anime"),
            ("../guide/watch.html", "How to watch"),
            ("staff.html", "Staff"),
            ("../fun/world-tour.html", "World tour"),
            ("index.html", "Media"),
        ],
    )


def main():
    chapter_132()
    chapter_133()
    rooms()
    print("pages this run", len(PAGES))


if __name__ == "__main__":
    main()
