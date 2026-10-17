#!/usr/bin/env python3
"""Second 17 Oct printed-fact wave: English trades, leftover pairs, title-source essays."""
from oct_lib import page

# --- English trades 2-7 (1, 8, 9, 10 already exist) ---
EN = [
    (
        2,
        "Enten vs. Cloud Gouger",
        "4 February 2025",
        "978-1-9747-5271-3",
        "The first English weather duel. Chihiro versus Sojo, True Realm, a wartime blade that dies.",
        "Ch. 9–18. Japanese volume 2 was 2 May 2024. The English trade is the volume 1 BookScan object’s sequel, not a new meme.",
        "../manga/volume-2.html",
        "../arcs/vs-sojo.html",
    ),
    (
        3,
        "Knight of Darkness",
        "6 May 2025",
        "978-1-9747-5478-6",
        "Hiyuki arrives in English cloth. The 208th Rakuzaichi starts being built on a VIZ spine.",
        "Ch. 19–27. Japanese volume 3 was 4 July 2024. Flame Bone is a permission slip, not a seventh blade.",
        "../manga/volume-3.html",
        "../arcs/rakuzaichi.html",
    ),
    (
        4,
        "Equal",
        "5 August 2025",
        "978-1-9747-5607-0",
        "Hakuri’s English debut as a jacket argument. Equal is a word about brothers, not a power level.",
        "Ch. 28–36. Japanese volume 4 was 4 October 2024. The Storehouse is already the architecture.",
        "../manga/volume-4.html",
        "../analysis/equal-jacket.html",
    ),
    (
        5,
        "Fervent",
        "4 November 2025",
        "978-1-9747-5891-3",
        "The auction crowd in English. Shinuchi is listed. The building has to live.",
        "Ch. 37–46. Japanese volume 5 was 4 December 2024. Volume 5 closer is The Curtain Falls, then Uruha.",
        "../manga/volume-5.html",
        "../arcs/rakuzaichi.html",
    ),
    (
        6,
        "Daybreak",
        "3 February 2026",
        "978-1-9747-6287-3",
        "Part 1’s second movement in English. Uruha, Samura, Hiruhiko. Two Japanese words on one English jacket.",
        "Ch. 47–56. Japanese volume 6 was 4 March 2025. Night Battle is next. Two Daybreaks sit on the essay desk.",
        "../manga/volume-6.html",
        "../analysis/two-daybreaks.html",
    ),
    (
        7,
        "Night Battle",
        "5 May 2026",
        "978-1-9747-6574-4",
        "Samura, Chihiro, Iori. The hotel is not yet the title. The eyes are already the brief.",
        "Ch. 57–65. Japanese volume 7 was 2 May 2025. English 8, Dawn, is the hotel book.",
        "../manga/volume-7.html",
        "../arcs/sword-bearer.html",
    ),
]

for n, title, date, isbn, lede, body, jp, extra in EN:
    page(
        f"collectibles/english-volume-{n}.html",
        f"Kagurabachi English Volume {n} | {title}",
        f"VIZ Kagurabachi volume {n}, {title}, {date}, ISBN {isbn}. The English trade, not a scan.",
        f"Collect · EN {n}",
        f"English volume {n}",
        f"英語版 第{n}巻",
        lede,
        [
            (
                "What the trade is",
                [
                    f"VIZ dated {date}. ISBN {isbn}. {body}",
                    f"Japanese commute: <a href=\"{jp}\">volume {n}</a>. Sister English objects: <a href=\"english-volume-1.html\">1</a>, <a href=\"english-volume-8.html\">8</a>, <a href=\"english-volume-9.html\">9</a>, <a href=\"english-volume-10.html\">10</a>. Catalog number: <a href=\"isbn-english-{n}.html\">ISBN {isbn}</a>. Lag: <a href=\"../analysis/volume-lag.html\">volume lag</a>. Extra door: <a href=\"{extra}\">{extra.split('/')[-1].replace('.html','').replace('-',' ')}</a>.",
                ],
            )
        ],
        [
            (f"isbn-english-{n}.html", "ISBN"),
            (jp, f"JP {n}"),
            ("english-volume-1.html", "English 1"),
            ("english-volume-8.html", "English 8"),
            ("../manga/volumes.html", "Volume guide"),
            ("index.html", "Collectibles"),
        ],
    )
    page(
        f"collectibles/isbn-english-{n}.html",
        f"ISBN {isbn} | English Volume {n}",
        f"VIZ Kagurabachi English volume {n} carries ISBN {isbn}. A catalog number, not a plot.",
        "Collect · ISBN",
        isbn,
        "ISBN",
        f"The number on English volume {n}.",
        [
            (
                "A catalog, not a chapter",
                [
                    f"{isbn} is the VIZ trade for <a href=\"english-volume-{n}.html\">English volume {n}</a> ({title}). The Japanese ISBN lives on <a href=\"{jp}\">volume {n}</a>. We do not invent barcodes.",
                    "English 1 is <a href=\"isbn-english-1.html\">978-1-9747-4724-5</a>. English 10’s solicitation is <a href=\"isbn-english-10.html\">978-1-9747-6947-6</a>. Shelf map: <a href=\"../manga/volumes.html\">volumes</a>.",
                ],
            )
        ],
        [
            (f"english-volume-{n}.html", f"English {n}"),
            ("isbn-english-1.html", "ISBN EN 1"),
            ("isbn-english-10.html", "ISBN EN 10"),
            ("../manga/volumes.html", "Volume guide"),
            ("index.html", "Collectibles"),
        ],
    )

page(
    "collectibles/isbn-english-8.html",
    "ISBN 978-1-9747-1650-0 | English Volume 8",
    "VIZ Kagurabachi English volume 8, Dawn, carries ISBN 978-1-9747-1650-0. 4 August 2026.",
    "Collect · ISBN",
    "978-1-9747-1650-0",
    "ISBN",
    "The hotel book’s catalog number.",
    [
        (
            "A catalog, not a chapter",
            [
                "978-1-9747-1650-0 is the VIZ trade for <a href=\"english-volume-8.html\">English volume 8</a> (Dawn, 4 August 2026). Japanese volume 8 was 4 July 2025.",
                "The 1650 block looks unlike the 4xxx/5xxx/6xxx neighbors on this shelf. The volume guide still prints it. We file the number, we do not rewrite VIZ’s barcode.",
            ],
        )
    ],
    [
        ("english-volume-8.html", "English 8"),
        ("isbn-english-1.html", "ISBN EN 1"),
        ("isbn-english-7.html", "ISBN EN 7"),
        ("../manga/volumes.html", "Volume guide"),
        ("index.html", "Collectibles"),
    ],
)

page(
    "collectibles/isbn-english-9.html",
    "ISBN 978-1-9747-6845-5 | English Volume 9",
    "VIZ Kagurabachi English volume 9, Enten, is listed 3 November 2026, ISBN 978-1-9747-6845-5.",
    "Collect · ISBN",
    "978-1-9747-6845-5",
    "ISBN",
    "The November 2026 English Enten spine.",
    [
        (
            "A catalog, not a chapter",
            [
                "978-1-9747-6845-5 is the listed VIZ trade for <a href=\"english-volume-9.html\">English volume 9</a> (Enten, 3 November 2026). Japanese volume 9 was 3 October 2025.",
                "November 2026 is also a magazine month. The English Enten jacket is a trade date, not a weekly title. Month door: <a href=\"../fun/november-2026.html\">November 2026</a>.",
            ],
        )
    ],
    [
        ("english-volume-9.html", "English 9"),
        ("isbn-english-8.html", "ISBN EN 8"),
        ("isbn-english-10.html", "ISBN EN 10"),
        ("../fun/november-2026.html", "November 2026"),
        ("index.html", "Collectibles"),
    ],
)

# --- leftover pairs ---
page(
    "characters/hakuri-and-hiyuki.html",
    "Hakuri and Hiyuki | Storehouse and Flame Bone",
    "Hakuri inherits the Storehouse. Hiyuki is the Kamunabi’s pointed end. They share Chihiro’s working circle, not a clan.",
    "Pair · 蔵",
    "Hakuri and Hiyuki",
    "伯理と緋雪",
    "A walking warehouse. A permission slip of bone.",
    [
        (
            "Two tools, one boy",
            [
                "Hakuri’s Isou and Storehouse are Sazanami burial-force. Hiyuki’s Flame Bone is inherited Kamunabi permission. Chihiro keeps both people in the present-tense hunt. The pair is not a marriage and not a squad name.",
                "See <a href=\"hakuri.html\">Hakuri</a>, <a href=\"hiyuki.html\">Hiyuki</a>, <a href=\"chihiro-and-hakuri.html\">Chihiro and Hakuri</a>, <a href=\"chihiro-and-hiyuki.html\">Chihiro and Hiyuki</a>, <a href=\"../world/circle.html\">the circle</a>.",
            ],
        )
    ],
    [
        ("hakuri.html", "Hakuri"),
        ("hiyuki.html", "Hiyuki"),
        ("hiyuki-and-tafuku.html", "Tafuku"),
        ("../world/storehouse.html", "Storehouse"),
        ("../analysis/flame-bone.html", "Flame Bone"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/hakuri-and-shiba.html",
    "Hakuri and Shiba | Two Ways Out of a Room",
    "Shiba teleports. Hakuri moves the room. Chihiro needs both exits after the raid’s three-year sit-down ends.",
    "Pair · 出口",
    "Hakuri and Shiba",
    "伯理と柴",
    "Extraction without a contract. A warehouse that walks.",
    [
        (
            "Teleport versus Storehouse",
            [
                "Shiba’s innate art is teleport, extraction without signing steel. Hakuri’s Storehouse moves people and charged objects across the country once the subspace answers him. Cafe Haru Haru was Shiba’s sit-down. The auction is Hakuri’s.",
                "See <a href=\"hakuri.html\">Hakuri</a>, <a href=\"shiba.html\">Shiba</a>, <a href=\"chihiro-and-shiba.html\">Chihiro and Shiba</a>, <a href=\"../world/teleport.html\">teleport</a>, <a href=\"../world/storehouse.html\">Storehouse</a>.",
            ],
        )
    ],
    [
        ("hakuri.html", "Hakuri"),
        ("shiba.html", "Shiba"),
        ("hinao-and-shiba.html", "Hinao and Shiba"),
        ("../world/cafe.html", "Cafe"),
        ("../world/teleport.html", "Teleport"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/kuguri-and-hiruhiko.html",
    "Kuguri and Hiruhiko | Two Hishaku at the Hotel",
    "Kuguri teaches Iai with a closed eye. Hiruhiko wrecks the building with Play. Same ten. Different brief.",
    "Pair · ホテル",
    "Kuguri and Hiruhiko",
    "久々李と昼彦",
    "A classroom. A demolition.",
    [
        (
            "The hotel as two jobs",
            [
                "Yura sent both. Kuguri’s closed-eye Iai is the style Chihiro copies in the Kyoto Bloodshed Hotel. Hiruhiko’s Play is the art that takes the floors. Chapter 70 puts the school name on a title. The pair is not a friendship page.",
                "See <a href=\"kuguri.html\">Kuguri</a>, <a href=\"hiruhiko.html\">Hiruhiko</a>, <a href=\"kuguri-and-yura.html\">Kuguri and Yura</a>, <a href=\"yura-and-hiruhiko.html\">Yura and Hiruhiko</a>, <a href=\"../analysis/play.html\">Play</a>.",
            ],
        )
    ],
    [
        ("kuguri.html", "Kuguri"),
        ("hiruhiko.html", "Hiruhiko"),
        ("chihiro-and-kuguri.html", "Chihiro and Kuguri"),
        ("chihiro-and-hiruhiko.html", "Chihiro and Hiruhiko"),
        ("../world/hotel-floors.html", "Hotel floors"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/hiruhiko-and-iori.html",
    "Hiruhiko and Iori | Play versus the Daughter",
    "Iori is Samura’s daughter, memory-sealed then unsealed at the hotel. Hiruhiko is the Hishaku who treats the building as a toy.",
    "Pair · 娘",
    "Hiruhiko and Iori",
    "昼彦とイヲリ",
    "A demolitionist. The cargo the hotel was built around.",
    [
        (
            "The daughter is not a stage prop",
            [
                "Iori copies the house style because it is the house. Hiruhiko’s Play is why the hotel stops being a building. Samura’s brief is the daughter, not the Hishaku roster. Essay: <a href=\"../analysis/daughter-cargo.html\">daughter as cargo</a>.",
                "See <a href=\"hiruhiko.html\">Hiruhiko</a>, <a href=\"iori.html\">Iori</a>, <a href=\"samura-and-iori.html\">Samura and Iori</a>, <a href=\"chihiro-and-iori.html\">Chihiro and Iori</a>.",
            ],
        )
    ],
    [
        ("hiruhiko.html", "Hiruhiko"),
        ("iori.html", "Iori"),
        ("samura-and-iori.html", "Samura and Iori"),
        ("../analysis/daughter-cargo.html", "Daughter cargo"),
        ("../analysis/play.html", "Play"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/iori-and-kiri.html",
    "Iori and Kiri | Two Women of the Iai House",
    "Iori copies Shirakai because it is her house. Kiri Shirakai wants to behead the founder for saying women cannot.",
    "Pair · 居合",
    "Iori and Kiri",
    "イヲリと斬",
    "A daughter who inherited the school. A student who wants the founder’s head.",
    [
        (
            "The argument the family is still having",
            [
                "Itsuo Shirakai’s speed school closes the eyes. Samura took that further. Iori is Samura’s daughter; the style is household. Kiri is the founder’s problem: the school said women cannot, and she is still in the room. Hakuri meets that argument too.",
                "See <a href=\"iori.html\">Iori</a>, <a href=\"kiri.html\">Kiri</a>, <a href=\"kiri-and-itsuo.html\">Kiri and Itsuo</a>, <a href=\"hakuri-and-kiri.html\">Hakuri and Kiri</a>, <a href=\"../world/iai.html\">Iai</a>.",
            ],
        )
    ],
    [
        ("iori.html", "Iori"),
        ("kiri.html", "Kiri"),
        ("kiri-and-itsuo.html", "Itsuo"),
        ("kiri-and-samura.html", "Kiri and Samura"),
        ("../world/iai.html", "Iai"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/sojo-and-hagiwara.html",
    "Sojo and Hagiwara | Customer versus Captain",
    "Ikuto Hagiwara led the Anti-Cloud Gouger Special Forces. Sojo is Cloud Gouger’s customer, not Hishaku. Six went. Two walked out.",
    "Pair · 対",
    "Sojo and Hagiwara",
    "双城と萩原",
    "A weather kit sold as a product. A squad that was not enough.",
    [
        (
            "The government against a customer",
            [
                "Yura sold Cloud Gouger to Sojo. Hagiwara’s Jikai is magnetism. The Anti-Cloud Gouger Special Forces die in Tokyo trying to fake Kunishige’s eyes with Datenseki and a secret weapon. Hagiwara loses both legs. Sojo still dies in the Datenseki backlash, not to the squad.",
                "See <a href=\"sojo.html\">Sojo</a>, <a href=\"hagiwara.html\">Hagiwara</a>, <a href=\"kazane-and-hagiwara.html\">the two survivors</a>, <a href=\"../analysis/sojo-customer.html\">customer</a>, <a href=\"../analysis/acg-cavalry.html\">ACG</a>.",
            ],
        )
    ],
    [
        ("sojo.html", "Sojo"),
        ("hagiwara.html", "Hagiwara"),
        ("hagiwara-and-kugara.html", "Kugara"),
        ("../blades/cloud-gouger.html", "Cloud Gouger"),
        ("../analysis/acg-cavalry.html", "ACG"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/kazane-and-kugara.html",
    "Kazane and Kugara | Newest Member, Iron Body",
    "Kazane Machi was the newest Anti-Cloud Gouger member. Kugara’s Iron Body did not walk out. Kazane lost the arm that was supposed to fire Kaichi.",
    "Pair · 新",
    "Kazane and Kugara",
    "カザネと具柄",
    "A secret weapon without an arm. An iron body that still died.",
    [
        (
            "Two ACG files, one survivor",
            [
                "Six went. Kugara is among the dead. Hagiwara still hears him. Kazane survived with the right arm gone, Kaichi unfired. The team’s secret weapon never became a True Realm scene. HQ later uses the leftover.",
                "See <a href=\"kazane.html\">Kazane</a>, <a href=\"kugara.html\">Kugara</a>, <a href=\"hagiwara-and-kugara.html\">Hagiwara and Kugara</a>, <a href=\"../world/iron-body.html\">Iron Body</a>, <a href=\"../world/kaichi.html\">Kaichi</a>.",
            ],
        )
    ],
    [
        ("kazane.html", "Kazane"),
        ("kugara.html", "Kugara"),
        ("kazane-and-hagiwara.html", "Two survivors"),
        ("../world/iron-body.html", "Iron Body"),
        ("../world/kaichi.html", "Kaichi"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/yura-and-bingo.html",
    "Yura and Bingo | The Mind and the Tree",
    "Yura decides which blade goes to which monster. Bingo is one of the ten: Mako, lion-dancer heads, HQ muscle.",
    "Pair · 十",
    "Yura and Bingo",
    "幽と瓶伍",
    "A planner. Festival heads in a government hallway.",
    [
        (
            "Roster, not a duet",
            [
                "The Hishaku are ten criminal sorcerers, flame tattoos, a shared fire-gate. Yura is the mind. Bingo’s printed kit is Mako (魔咬), Demon Bite: lion-dancer charms, stacked weight, corpse fuel, then sleep. Headquarters infiltration, not the hotel. We do not invent Bingo as Yura’s second.",
                "See <a href=\"yura.html\">Yura</a>, <a href=\"bingo.html\">Bingo</a>, <a href=\"bingo-and-yukisada.html\">Bingo and Yukisada</a>, <a href=\"../factions/hishaku.html\">Hishaku</a>.",
            ],
        )
    ],
    [
        ("yura.html", "Yura"),
        ("bingo.html", "Bingo"),
        ("bingo-and-yukisada.html", "Yukisada"),
        ("yura-and-hiruhiko.html", "Hiruhiko"),
        ("../factions/hishaku.html", "Hishaku"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/yura-and-toto.html",
    "Yura and Toto | The Mind and Another of the Ten",
    "Toto is printed among the Hishaku ten. Yura still assigns the jobs. Sharing a tattoo is not sharing a brief.",
    "Pair · 十",
    "Yura and Toto",
    "幽と斗斗",
    "A planner. A named face that is not the hotel.",
    [
        (
            "Named is not explained",
            [
                "This archive names Toto because the book did. The rest of the ten still includes unnamed members. Yura’s pair pages with Hiruhiko, Kuguri, Hokuto, Kasen, and Akemura are the jobs the plot actually spent. Toto’s job is thinner. We file the roster, we do not pad it.",
                "See <a href=\"yura.html\">Yura</a>, <a href=\"toto.html\">Toto</a>, <a href=\"toto-and-sengoku.html\">Toto and Sengoku</a>, <a href=\"../factions/hishaku.html\">Hishaku</a>.",
            ],
        )
    ],
    [
        ("yura.html", "Yura"),
        ("toto.html", "Toto"),
        ("toto-and-sengoku.html", "Sengoku"),
        ("../factions/hishaku.html", "Hishaku"),
        ("../characters/index.html", "The rest of the ten"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/mashiro-and-ariu.html",
    "Mashiro and Ariu | Two Island Arts, Two Sides",
    "Mashiro’s Akuu is air pressure. Ariu Mikaboshi is the printed name on Hiroto’s and Yoshinojo’s Irishima deaths.",
    "Pair · 島",
    "Mashiro and Ariu",
    "真城と亜利雨",
    "A Soga-side pressure. A Mikaboshi name on two graves.",
    [
        (
            "Do not collapse the island",
            [
                "Irishima is a vein, a talk, a war. Mashiro stands with the Soga household arts. Ariu is a Mikaboshi individual, not the whole undersea clan. Pairing them is a reminder that the island has two printed kits, not a secret alliance.",
                "See <a href=\"mashiro.html\">Mashiro</a>, <a href=\"ariu.html\">Ariu</a>, <a href=\"mashiro-and-shiba.html\">Mashiro and Shiba</a>, <a href=\"ariu-and-mikaboshi.html\">Ariu and the clan</a>, <a href=\"../world/akuu.html\">Akuu</a>.",
            ],
        )
    ],
    [
        ("mashiro.html", "Mashiro"),
        ("ariu.html", "Ariu"),
        ("../world/akuu.html", "Akuu"),
        ("../factions/mikaboshi.html", "Mikaboshi"),
        ("../world/irishima.html", "Irishima"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/giyu-and-kunishige.html",
    "Giyu and Kunishige | Two Smiths, One Ore",
    "Kunishige’s eyes are the known way Datenseki becomes a blade. Giyu is the other printed smith the war book puts on Irishima.",
    "Pair · 鍛",
    "Giyu and Kunishige",
    "義勇と国重",
    "A household smith. A second name on the kiln.",
    [
        (
            "The ore is not a monopoly until it is",
            [
                "Kunishige forges all seven Enchanted Blades. Enten is the seventh, after the treaty, as a retraction. Giyu is the other smith name the island chapters put on the page. Chihiro’s later notes for a new Enten are still a Rokuhira job.",
                "See <a href=\"giyu.html\">Giyu</a>, <a href=\"kunishige.html\">Kunishige</a>, <a href=\"chihiro-and-giyu.html\">Chihiro and Giyu</a>, <a href=\"chiaki-and-giyu.html\">Chiaki and Giyu</a>, <a href=\"../world/smelting.html\">smelting</a>.",
            ],
        )
    ],
    [
        ("giyu.html", "Giyu"),
        ("kunishige.html", "Kunishige"),
        ("chihiro-and-kunishige.html", "Father and son"),
        ("../world/smelting.html", "Smelting"),
        ("../blades/enten.html", "Enten"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/chihiro-and-kiri.html",
    "Chihiro and Kiri | Copied Iai, Unfinished Grudge",
    "Chihiro copies Iai White Purity Style with his eyes shut. Kiri Shirakai wants the founder’s head for locking women out.",
    "Pair · 流",
    "Chihiro and Kiri",
    "千鉱と斬",
    "A boy who stole a curriculum. A student who wants the school on trial.",
    [
        (
            "The school as two hungers",
            [
                "Chihiro copies Kuguri and the house at the Kyoto hotel. The style is a tool for a seventh-blade brief. Kiri’s hunger is the founder. Hakuri stands closer to Kiri’s argument than Chihiro does. We do not file Chihiro as a Shirakai heir.",
                "See <a href=\"chihiro.html\">Chihiro</a>, <a href=\"kiri.html\">Kiri</a>, <a href=\"chihiro-and-kuguri.html\">Chihiro and Kuguri</a>, <a href=\"hakuri-and-kiri.html\">Hakuri and Kiri</a>, <a href=\"../world/iai.html\">Iai</a>.",
            ],
        )
    ],
    [
        ("chihiro.html", "Chihiro"),
        ("kiri.html", "Kiri"),
        ("iori-and-kiri.html", "Iori and Kiri"),
        ("chihiro-and-iori.html", "Chihiro and Iori"),
        ("../world/iai.html", "Iai"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/fushimi-and-samura.html",
    "Fushimi and Samura | Masumi Eyes, Closed Eyes",
    "Fushimi is Masumi, perception work around Uruha. Samura closed his eyes on purpose and then spent the life.",
    "Pair · 目",
    "Fushimi and Samura",
    "伏見と座村",
    "A watcher assigned to a bearer. A bearer who refused to watch.",
    [
        (
            "Two ways to use an eye",
            [
                "The Masumi are Kamunabi perception. Fushimi’s printed job sits on Uruha’s Sanso side of the map. Samura’s Iai is eyes closed, then the eyes themselves gone, then Suzaku-black. The pair is a contrast, not a team-up.",
                "See <a href=\"fushimi.html\">Fushimi</a>, <a href=\"samura.html\">Samura</a>, <a href=\"fushimi-and-uruha.html\">Fushimi and Uruha</a>, <a href=\"../analysis/closed-eye.html\">closed eye</a>, <a href=\"../analysis/suzaku.html\">Suzaku</a>.",
            ],
        )
    ],
    [
        ("fushimi.html", "Fushimi"),
        ("samura.html", "Samura"),
        ("fushimi-and-uruha.html", "Uruha"),
        ("../analysis/closed-eye.html", "Closed eye"),
        ("../factions/masumi.html", "Masumi"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/hiyuki-and-yura.html",
    "Hiyuki and Yura | Permission Slip versus Plan",
    "Hiyuki is the Kamunabi’s pointed end. Yura is the Hishaku mind. Flame Bone against a fire-gate is not a titled duel on this desk.",
    "Pair · 火",
    "Hiyuki and Yura",
    "緋雪と幽",
    "A national skeleton. A shared tattoo.",
    [
        (
            "Two fires, two employers",
            [
                "Flame Bone is inherited, Kamunabi-permissioned, pointed at Enchanted Blade problems. The Hishaku flame is a tattoo and a gate. Yura sold Cloud Gouger to Sojo and later needed a leak inside the Kamunabi. Hiyuki is not that leak. Kasen is.",
                "See <a href=\"hiyuki.html\">Hiyuki</a>, <a href=\"yura.html\">Yura</a>, <a href=\"yura-and-kasen.html\">Yura and Kasen</a>, <a href=\"../analysis/flame-bone.html\">Flame Bone</a>, <a href=\"../analysis/leak.html\">the leak</a>.",
            ],
        )
    ],
    [
        ("hiyuki.html", "Hiyuki"),
        ("yura.html", "Yura"),
        ("chihiro-and-yura.html", "Chihiro and Yura"),
        ("../factions/hishaku.html", "Hishaku"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/hokuto-and-samura.html",
    "Hokuto and Samura | Two Wartime Styles",
    "Hokuto is a Sword Bearer on the Hishaku side of the present. Samura was a wartime bearer who spent the last of his life on Magatsumi.",
    "Pair · 戦",
    "Hokuto and Samura",
    "北兜と座村",
    "A present-tense bearer. A closed-eye spend.",
    [
        (
            "Bearers are not a union",
            [
                "Volume 10’s jacket word is 剣士たち, the swordsmen as an ensemble. Hokuto sits on that spine with Natsuki, Uruha, Yura. Samura’s Tobimune is the owl, Suzaku, Crow. The pair is two contracts, not one school. Uruha stands between them on other pages.",
                "See <a href=\"hokuto.html\">Hokuto</a>, <a href=\"samura.html\">Samura</a>, <a href=\"uruha-and-hokuto.html\">Uruha and Hokuto</a>, <a href=\"ibuki-and-hokuto.html\">Ibuki and Hokuto</a>, <a href=\"../world/bearers.html\">bearers</a>.",
            ],
        )
    ],
    [
        ("hokuto.html", "Hokuto"),
        ("samura.html", "Samura"),
        ("uruha-and-samura.html", "Uruha and Samura"),
        ("../blades/tobimune.html", "Tobimune"),
        ("../manga/volume-10.html", "Vol. 10"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/ichiki-and-yatsuru.html",
    "Ichiki and Yatsuru | Two Seats at the Leadership Table",
    "Ichiki and Yatsuru sit among the Kamunabi heads. The table is not Hiyuki, and it is not Kasen’s leak.",
    "Pair · 席",
    "Ichiki and Yatsuru",
    "壱鬼と夜弦",
    "A leadership table. Not the pointed end.",
    [
        (
            "Heads are not a squad name",
            [
                "The Kamunabi rebuilt from the Counter-Sorcery Army. Ichiki, Yatsuru, Izaru, and the rest of the heads are why Hiyuki has a permission slip and why Chihiro can be hired without becoming the state. Kasen is the leak at that table, not these two.",
                "See <a href=\"ichiki.html\">Ichiki</a>, <a href=\"yatsuru.html\">Yatsuru</a>, <a href=\"ichiki-and-azami.html\">Ichiki and Azami</a>, <a href=\"izaru-and-ichiki.html\">izaru</a>, <a href=\"../factions/kamunabi.html\">Kamunabi</a>.",
            ],
        )
    ],
    [
        ("ichiki.html", "Ichiki"),
        ("yatsuru.html", "Yatsuru"),
        ("ichiki-and-azami.html", "Azami"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("index.html", "Characters"),
        ("bonds.html", "Bonds"),
    ],
)

page(
    "characters/izaru-and-ichiki.html",
    "izaru and Ichiki | Two Heads, One Table",
    "izaru sits with Ichiki among the Kamunabi leadership. Naming both keeps the table from collapsing into Azami.",
    "Pair · 席",
    "izaru and Ichiki",
    "亥猿と壱鬼",
    "Two seats. One leak elsewhere.",
    [
        (
            "Do not file every head as Azami",
            [
                "Azami is the face Chihiro meets first. Ichiki and Izaru are why the leadership table has more than one surname. Yatsuru is the other named seat on this wave. Kasen is the leak. Hiyuki is the pointed end. Keep the nouns.",
                "See <a href=\"izaru.html\">izaru</a>, <a href=\"ichiki.html\">Ichiki</a>, <a href=\"ichiki-and-yatsuru.html\">Ichiki and Yatsuru</a>, <a href=\"azami.html\">Azami</a>.",
            ],
        )
    ],
    [
        ("izaru.html", "izaru"),
        ("ichiki.html", "Ichiki"),
        ("ichiki-and-yatsuru.html", "Yatsuru"),
        ("ichiki-and-azami.html", "Azami"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("bonds.html", "Bonds"),
    ],
)

# --- essays / world / fun / guide ---
page(
    "analysis/wikipedia-titles.html",
    "Wikipedia as a Title Source | Kagurabachi Archive",
    "This desk files weekly English and Japanese chapter titles from the Wikipedia chapter list when VIZ’s listing is still untitled. Not a plot source.",
    "Essay · 出典",
    "Wikipedia titles",
    "題名の出典",
    "A chapter list. Not a recap wiki.",
    [
        (
            "What we take, what we refuse",
            [
                "VIZ’s Kagurabachi chapter index often ships the number without a subtitle in the first week. MANGA Plus title URLs 404. The Wikipedia chapter list is the printed-English door this archive already used for chapter 132, Misaka (巳坂), then 133, Misaka Version II (巳坂二号), then 134, Masters of the Sword (剣豪).",
                "We do not take Fandom plot recaps. We do not invent chapter 135. We do not file Irishima 118–120 as separate rooms. Method leftover: <a href=\"live-untitled.html\">live untitled</a>. Catch-up week: <a href=\"wikipedia-caught-up.html\">Wikipedia caught up</a>. Policy: <a href=\"../guide/official-only.html\">official-only</a>.",
            ],
        )
    ],
    [
        ("wikipedia-caught-up.html", "Caught up"),
        ("live-untitled.html", "Live untitled"),
        ("../manga/chapter-133.html", "Ch. 133"),
        ("../manga/chapter-134.html", "Ch. 134"),
        ("../guide/official-only.html", "Official-only"),
        ("index.html", "Essays"),
    ],
)

page(
    "analysis/kengo.html",
    "剣豪 | Masters of the Sword as a Weekly Word",
    "Chapter 134’s Japanese title is 剣豪. English: Masters of the Sword. A rank word, not Volume 10’s jacket, not the press’s Sword Master.",
    "Essay · 剣豪",
    "剣豪",
    "剣豪",
    "A weekly rank. Three Japanese nouns still in collision.",
    [
        (
            "What the week said",
            [
                "Jump 2026 issue 46, VIZ 11 October 2026. Wikipedia prints Masters of the Sword / 剣豪. Volume 10’s jacket is 剣士たち, The Swordsmen. Quoted press for Akemura is 剣聖, Sword Master. Collision desks: <a href=\"kengo-versus-kenshi.html\">versus 剣士たち</a>, <a href=\"kengo-versus-kensei.html\">versus 剣聖</a>.",
                "We do not recap the panels. We do not file 剣豪 as a new Enchanted Blade. Neighbor titles: <a href=\"../manga/chapter-133.html\">Misaka Version II</a>, then <a href=\"../manga/chapter-135.html\">135’s door</a>.",
            ],
        )
    ],
    [
        ("kengo-versus-kenshi.html", "vs 剣士"),
        ("kengo-versus-kensei.html", "vs 剣聖"),
        ("sword-master-press.html", "Sword Master"),
        ("../manga/chapter-134.html", "Ch. 134"),
        ("../manga/volume-10.html", "Vol. 10"),
        ("index.html", "Essays"),
    ],
)

page(
    "analysis/five-dates-only.html",
    "Five Dates Only | Printed Birthdays versus Merch Calendars",
    "This archive prints five birthdays: Chihiro 11 August, Kunishige 5 June, Shiba 15 October, Sojo 6 June, Char 21 December. Merch calendars stay unmarked.",
    "Essay · 五",
    "Five dates only",
    "五つの日付",
    "A profile badge is a source. A shop calendar is not.",
    [
        (
            "Why the list stays short",
            [
                "Hakuri, Hiyuki, Samura, Iori, Yura, and Chiaki do not have published dates on this desk. Ages that are printed (Chihiro 18, Shiba 39, Sojo 30 at death, Kunishige 37 at death) are not extra birthdays. Char’s age is still blank.",
                "Hub: <a href=\"../world/birthdays.html\">five dates</a>. Adjacent June: <a href=\"adjacent-june.html\">5 and 6 June</a>. Shiba’s month: <a href=\"shiba-october.html\">October</a>. Profiles: <a href=\"../world/profiles.html\">profiles</a>.",
            ],
        )
    ],
    [
        ("../world/birthdays.html", "Five dates"),
        ("adjacent-june.html", "Adjacent June"),
        ("shiba-october.html", "Shiba October"),
        ("../world/profiles.html", "Profiles"),
        ("../world/chihiro-birthday.html", "11 August"),
        ("index.html", "Essays"),
    ],
)

page(
    "analysis/english-shelf.html",
    "The English Shelf | VIZ Trades 1 through 10",
    "VIZ Kagurabachi trades from English 1 (5 November 2024) through the volume 10 solicitation (2 February 2027). About nine months behind Japan.",
    "Essay · 英語棚",
    "English shelf",
    "英語の棚",
    "Nine spines dated. A tenth solicited. Japan is already on 12.",
    [
        (
            "What the cloth actually is",
            [
                "English 1, Mission, 5 November 2024, ISBN 978-1-9747-4724-5, is the object Circana BookScan put at #1. English 2–7 now have rooms. English 8 is Dawn, 4 August 2026. English 9, Enten, 3 November 2026. English 10, 2 February 2027, ISBN 978-1-9747-6947-6.",
                "Japanese volume 12 solicited 4 September 2026. The English shelf does not catch the war book this year. Lag: <a href=\"volume-lag.html\">volume lag</a>. Guide: <a href=\"../manga/volumes.html\">volumes</a>.",
            ],
        )
    ],
    [
        ("../collectibles/english-volume-1.html", "English 1"),
        ("../collectibles/english-volume-8.html", "English 8"),
        ("../collectibles/english-volume-10.html", "English 10"),
        ("volume-lag.html", "Volume lag"),
        ("../manga/volumes.html", "Volume guide"),
        ("index.html", "Essays"),
    ],
)

page(
    "fun/november-2026.html",
    "November 2026 | English Enten, Still a Weekly Book",
    "3 November 2026 is VIZ English volume 9, Enten. The magazine does not pause for the trade. Chapter 135 is already a mid-October door.",
    "Fun · 十一月",
    "November 2026",
    "二〇二六年十一月",
    "A listed English spine. A weekly book that does not wait.",
    [
        (
            "Trade date versus magazine date",
            [
                "English volume 9 is listed 3 November 2026, ISBN 978-1-9747-6845-5. October 2026 already held Misaka Version II and Masters of the Sword. Chapter 135 is Jump 2026 issue 47, on sale 19 October 2026, before the English Enten cloth.",
                "Sister months: <a href=\"october-2026.html\">October</a>, <a href=\"year-2026.html\">2026</a>. English object: <a href=\"../collectibles/english-volume-9.html\">English 9</a>. We do not invent November’s weekly titles.",
            ],
        )
    ],
    [
        ("october-2026.html", "October 2026"),
        ("year-2026.html", "2026"),
        ("../collectibles/english-volume-9.html", "English 9"),
        ("../manga/chapter-135.html", "Ch. 135 door"),
        ("index.html", "Fun"),
        ("sunday.html", "Sunday"),
    ],
)

page(
    "fun/five-printed-dates.html",
    "Five Printed Dates | The Birthday Desk as a Fun Door",
    "Chihiro 11 August, Kunishige 5 June, Shiba 15 October, Sojo 6 June, Char 21 December. A fun door onto the world hub, not extra cake chapters.",
    "Fun · 誕生日",
    "Five printed dates",
    "五つの日付",
    "The same five. No merch extras.",
    [
        (
            "A calendar you can actually cite",
            [
                "Shiba’s 15 October sat inside the same month as Misaka Version II and Masters of the Sword. Kunishige and Sojo sit a day apart in June. Chihiro is August. Char is December. The book does not throw parties. The profile pages just say the dates.",
                "World hub: <a href=\"../world/birthdays.html\">birthdays</a>. Essay: <a href=\"../analysis/five-dates-only.html\">five dates only</a>. Shiba’s month: <a href=\"shiba-october.html\">Shiba’s October</a>.",
            ],
        )
    ],
    [
        ("../world/birthdays.html", "Birthdays"),
        ("shiba-october.html", "Shiba October"),
        ("../analysis/five-dates-only.html", "Five dates only"),
        ("../analysis/adjacent-june.html", "Adjacent June"),
        ("index.html", "Fun"),
        ("community.html", "Sunday board"),
    ],
)

page(
    "guide/spoiler-134.html",
    "Chapter 134 Spoilers | Title Only",
    "Chapter 134 is titled Masters of the Sword (剣豪). This archive still does not recap the panels. Official reading is VIZ and MANGA Plus.",
    "Guide · ネタバレ",
    "134 without a recap",
    "134の無ネタバレ",
    "A ranked week. A closed mouth on the panels.",
    [
        (
            "What we will say",
            [
                "Wikipedia printed the weekly word. We file 剣豪 and Masters of the Sword. We still do not recap the issue. If you want the chapter, read it official. Same rule on <a href=\"spoiler-133.html\">133</a>. Next door: <a href=\"../manga/chapter-135.html\">135</a>, still untitled here.",
                "Collision desks if you only needed the noun: <a href=\"../analysis/kengo.html\">剣豪</a>. Policy: <a href=\"official-only.html\">official-only</a>.",
            ],
        )
    ],
    [
        ("../manga/chapter-134.html", "Ch. 134"),
        ("spoiler-133.html", "133 without a recap"),
        ("official-only.html", "Official-only"),
        ("spoiler-ladder.html", "Spoiler ladder"),
        ("../analysis/kengo.html", "剣豪"),
        ("index.html", "Guide"),
    ],
)

page(
    "guide/brand-new-doors.html",
    "Brand-New Doors | 17 October Wave",
    "What this archive added on 17 October 2026: titled 133 and 134, a 135 door, leftover pairs, English trades 2–7, birthday rooms, title-source essays.",
    "Guide · 新",
    "Brand-new doors",
    "新しい扉",
    "Printed leftover rooms, not stub spam.",
    [
        (
            "Where to start",
            [
                "Magazine: <a href=\"current-week.html\">current week</a>, <a href=\"../manga/chapter-133.html\">Misaka Version II</a>, <a href=\"../manga/chapter-134.html\">Masters of the Sword</a>, <a href=\"../manga/chapter-135.html\">135’s door</a>. Title method: <a href=\"../analysis/wikipedia-titles.html\">Wikipedia titles</a>.",
                "Pairs: <a href=\"../characters/bonds.html\">bonds</a>. Dates: <a href=\"../world/birthdays.html\">five birthdays</a>. English cloth: <a href=\"../analysis/english-shelf.html\">the English shelf</a>. Mid-month desk: <a href=\"mid-october-update.html\">mid-October update</a>.",
            ],
        )
    ],
    [
        ("mid-october-update.html", "Mid-October"),
        ("ultra-doors.html", "October 7 wave"),
        ("current-week.html", "Current week"),
        ("../characters/bonds.html", "Bonds"),
        ("../analysis/english-shelf.html", "English shelf"),
        ("index.html", "Guide"),
    ],
)

page(
    "world/october-fifteen.html",
    "October 15 | Shiba’s Date Inside a Titled Month",
    "Togo Shiba’s printed birthday is 15 October. In 2026 that date sat between Misaka Version II and Masters of the Sword.",
    "World · 10/15",
    "October 15",
    "10月15日",
    "A profile badge. A magazine month. Not a cake chapter.",
    [
        (
            "The date and the week",
            [
                "Shiba is 15 October, age 39. Chapter 133 is dated 4 October 2026. Chapter 134 is dated 11 October 2026. The birthday is not a Jump color-page claim on this desk. It is a profile fact that happened to land in the same month as two new weekly words.",
                "Room: <a href=\"shiba-birthday.html\">Shiba’s birthday</a>. Essay: <a href=\"../analysis/shiba-october.html\">Shiba’s October</a>. Fun door: <a href=\"../fun/shiba-october.html\">Shiba’s October</a>. Five dates: <a href=\"birthdays.html\">birthdays</a>.",
            ],
        )
    ],
    [
        ("shiba-birthday.html", "Shiba’s birthday"),
        ("birthdays.html", "Five dates"),
        ("../analysis/shiba-october.html", "Essay"),
        ("../fun/october-2026.html", "October 2026"),
        ("../characters/shiba.html", "Shiba"),
        ("index.html", "World"),
    ],
)

page(
    "manga/titles-through-masters.html",
    "Titles through Masters of the Sword | Chapter Index Door",
    "The spoken weekly list now ends on chapter 134, Masters of the Sword (剣豪). Chapter 135 stays a date. Irishima 118–120 stay table-only.",
    "Manga · 題名",
    "Through Masters of the Sword",
    "剣豪まで",
    "132 Misaka. 133 Version II. 134 剣豪. 135 a door.",
    [
        (
            "The spoken end of the list",
            [
                "Chapter 132 is Misaka. Chapter 133 is Misaka Version II. Chapter 134 is Masters of the Sword. The first Enchanted Blade is still unnamed. Enten is the seventh. Sojo is a Cloud Gouger customer, not Hishaku. We do not invent 135.",
                "Index: <a href=\"chapters.html\">chapters</a>. After Misaka: <a href=\"titles-after-misaka.html\">after Misaka</a>. Essay catalog: <a href=\"../analysis/titles-through-134.html\">titles through 134</a>. Source: <a href=\"../analysis/wikipedia-titles.html\">Wikipedia titles</a>.",
            ],
        )
    ],
    [
        ("chapters.html", "Chapter index"),
        ("chapter-134.html", "Ch. 134"),
        ("chapter-135.html", "Ch. 135 door"),
        ("../analysis/titles-through-134.html", "Essay"),
        ("part-2.html", "Part 2"),
        ("index.html", "Manga"),
    ],
)

print("mid_wave2 done")
