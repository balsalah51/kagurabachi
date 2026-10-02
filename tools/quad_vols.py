#!/usr/bin/env python3
"""Volume reading rooms: every collected book plus the solicited twelfth."""
from quad_lib import page

VOLS = [
    {
        "n": 1,
        "rel": "manga/volume-1-read.html",
        "title": "Reading Volume 1 Mission | Kagurabachi",
        "desc": "Chapters 1–8. Household, raid leftover, Char as witness, meals, Madoka. Before the weather title.",
        "jp": "すべきこと",
        "spine": "Mission",
        "chs": "1–8",
        "lede": "The job is a household before it is a versus.",
        "secs": [
            ("What the book is", [
                "Volume 1, Mission (すべきこと), collects chapters 1–8. Japanese ISBN 978-4-08-883819-9, 2 February 2024. English VIZ ISBN 978-1-9747-4724-5, 5 November 2024. Chapter 1 is Mission. Chapter 2 Heaps. Chapter 3 Witness. Chapter 4 Sorcery and the Enchanted Blade. Chapter 5 A Good Meal. Chapter 6 Peace. Chapter 7 Smoke Signal. Chapter 8 Norisaku Madoka: I Will Change.",
                "The raid is already leftover on page one. Kunishige is dead. Enten is in the son’s hand. Shiba is the adult who stayed. Cafe Haru Haru is available as a chair. Char has seen a blade. Sojo is in the city and not yet a versus title. The plate titles teach method before True Realm exists as a word.",
            ]),
            ("How to read it", [
                "Do not skip Madoka. Chapter 8 is a staff name and a promise. The ACG squad is not built yet. Cloud Gouger’s original bearer is not this book’s job. Official pages: VIZ and MANGA Plus. This site does not host chapters. Sister room: <a href=\"volume-1.html\">Volume 1</a>.",
            ]),
        ],
        "links": [("volume-1.html", "Volume 1"), ("chapter-1.html", "Ch. 1"), ("chapter-8.html", "Ch. 8"), ("../arcs/vs-sojo.html", "Vs. Sojo"), ("../guide/newcomer-hour.html", "Newcomer"), ("../fun/first-issue.html", "First issue")],
    },
    {
        "n": 2,
        "rel": "manga/volume-2-read.html",
        "title": "Reading Volume 2 | Enten vs Cloud Gouger | Kagurabachi",
        "desc": "Chapters 9–18. The favorite fight. True Realm. ACG graves. Roar. Sojo is a customer.",
        "jp": "淵天 VS 刳雲",
        "spine": "Enten vs. Cloud Gouger",
        "chs": "9–18",
        "lede": "The jacket is the fight. The register still starts the sword on Ibuki.",
        "secs": [
            ("The week list", [
                "Chapter 9 Enten vs. Cloud Gouger. 10 Swift. 11 Awaken. 12 Preparations. 13 Elite. 14 True Realm. 15 Food. 16 Silence. 17 Tea. 18 Roar. Mei, cloaked Mei, Yui, Kou. Sojo’s Cloud Gouger gains slaughter. Enten bisects the steel. Sojo dies on Datenseki.",
                "Preparations and Elite are the ACG squad being built and named so the weather sword has an opponent list. Four of six die. Char still eats. Tea still pours. The meals do not pause for True Realm. They sit beside it.",
            ]),
            ("Register", [
                "Sojo is a customer, not Hishaku. Ibuki held the blade in the war. Hokuto opened the contract. Yura sold it. Recaps that start Volume 2 as the birth of Cloud Gouger fail the cellar. Sister: <a href=\"volume-2.html\">Volume 2</a>, <a href=\"../world/battle-chihiro-sojo.html\">the fight desk</a>.",
            ]),
        ],
        "links": [("volume-2.html", "Volume 2"), ("chapter-9.html", "Ch. 9"), ("chapter-14.html", "True Realm"), ("chapter-18.html", "Roar"), ("../world/battle-chihiro-sojo.html", "Fight"), ("../analysis/sojo-customer.html", "Customer")],
    },
    {
        "n": 3,
        "rel": "manga/volume-3-read.html",
        "title": "Reading Volume 3 | Knight of Darkness | Kagurabachi",
        "desc": "Chapters 19–27. Auction start. Hiyuki as weapon. Storehouse titled. Mr. Inazuma.",
        "jp": "闇の騎士",
        "spine": "Knight of Darkness",
        "chs": "19–27",
        "lede": "The next building is two centuries old and lists a masterpiece.",
        "secs": [
            ("The week list", [
                "19 Knight of Darkness. 20 The Kamunabi’s Weapon. 21 Lukewarm. 22 Deadlock (拮抗). 23 Storehouse. 24 Hunters. 25 Deal. 26 Confidence. 27 Mr. Inazuma. Hiyuki enters. Tafuku is the partner. Hakuri is not yet the Kura. Chihiro lets the house take Enten to scout, then walks back with a stump.",
            ]),
            ("What to notice", [
                "The first Deadlock is 拮抗, not chapter 49’s 均衡. Inazuma is a person with a sister inside, not a weather gag. Shinuchi is already the listing. Sister: <a href=\"volume-3.html\">Volume 3</a>, <a href=\"../arcs/rakuzaichi.html\">Rakuzaichi</a>.",
            ]),
        ],
        "links": [("volume-3.html", "Volume 3"), ("chapter-19.html", "Ch. 19"), ("chapter-23.html", "Storehouse"), ("chapter-27.html", "Inazuma"), ("../arcs/rakuzaichi.html", "Arc"), ("../analysis/two-deadlocks.html", "Deadlocks")],
    },
    {
        "n": 4,
        "rel": "manga/volume-4-read.html",
        "title": "Reading Volume 4 Equal | Breach to Geniuses | Kagurabachi",
        "desc": "Chapters 28–36. Equal is the spine. The leftover son starts answering the house.",
        "jp": "対等",
        "spine": "Equal",
        "chs": "28–36",
        "lede": "A hole in the wall, then a word the jacket already chose.",
        "secs": [
            ("The week list", [
                "28 Breach. 29 Selection. 30 Intruders. 31 Greeting. 32 Wall. 33 Defend to the Death. 34 Duty. 35 Cage. 36 Geniuses. Hakuri is becoming vocabulary. The Storehouse is a cage for one week. Tenri’s corridor is already duty-shaped. Chapter 37, Equal, opens the next book. This volume’s closer is Geniuses before Fervent.",
            ]),
            ("Jacket", [
                "Equal is a politics. Chihiro and Hakuri are the pair the cloth picked. Essay: <a href=\"../analysis/equal-jacket.html\">Equal</a>. File: <a href=\"volume-4.html\">Volume 4</a>.",
            ]),
        ],
        "links": [("volume-4.html", "Volume 4"), ("chapter-32.html", "Wall"), ("chapter-35.html", "Cage"), ("../analysis/equal-jacket.html", "Equal"), ("../characters/hakuri.html", "Hakuri"), ("../world/storehouse.html", "Storehouse")],
    },
    {
        "n": 5,
        "rel": "manga/volume-5-read.html",
        "title": "Reading Volume 5 Fervent | Curtain, Punk | Kagurabachi",
        "desc": "Chapters 37–46. Equal opens. The curtain falls. Unruly Punk closes the firm.",
        "jp": "熱狂",
        "spine": "Fervent",
        "chs": "37–46",
        "lede": "The auction spends a building and a head. The next title is Uruha.",
        "secs": [
            ("The week list", [
                "37 Equal. 38 Race. 39 Surpass!. 40 The Tip. 41 Fervent. 42 Everything. 43 Fulfill. 44 The Curtain Falls. 45 What Comes Next. 46 Unruly Punk. Tenri’s stone sits in Fulfill’s corridor. Kyora looks through Shinuchi. Prisoners leave. Hakuri walks with both inheritances. Chihiro’s deal: masterpiece to the state, Enten in the hand.",
            ]),
            ("Page turn", [
                "What Comes Next is already a title. Unruly Punk is the closer. Chapter 47 will name a wartime bearer. Sister: <a href=\"volume-5.html\">Volume 5</a>, <a href=\"../guide/after-rakuzaichi.html\">after the auction</a>.",
            ]),
        ],
        "links": [("volume-5.html", "Volume 5"), ("chapter-37.html", "Equal"), ("chapter-44.html", "Curtain"), ("chapter-46.html", "Punk"), ("../arcs/rakuzaichi.html", "Arc"), ("../guide/after-rakuzaichi.html", "After")],
    },
    {
        "n": 6,
        "rel": "manga/volume-6-read.html",
        "title": "Reading Volume 6 Daybreak | Uruha to 夜更け | Kagurabachi",
        "desc": "Chapters 47–56. The long book opens on a name. Friendship. Fight Alongside. Daybreak as small hours.",
        "jp": "夜更け",
        "spine": "Daybreak",
        "chs": "47–56",
        "lede": "A box, a squad grave, a temple ethic, a night wearing out.",
        "secs": [
            ("The week list", [
                "47 Uruha. 48 The Kokugoku Steam Squad. 49 Deadlock (均衡). 50 Interception. 51 Samura. 52 Just the Two of Us. 53 Darkness. 54 Friendship. 55 Fight Alongside. 56 Daybreak (夜更け). Hiruhiko hits the box. Fushimi is named then spent. The second Deadlock is not the auction’s. Senkutsuji’s ethics are already in the titles before the cut lands in the next weather.",
            ]),
            ("Spine", [
                "Daybreak as 夜更け is the small hours, not chapter 73’s 黎明. Sister: <a href=\"volume-6.html\">Volume 6</a>, <a href=\"../analysis/two-daybreaks.html\">two Daybreaks</a>.",
            ]),
        ],
        "links": [("volume-6.html", "Volume 6"), ("chapter-47.html", "Uruha"), ("chapter-51.html", "Samura"), ("chapter-56.html", "Daybreak"), ("../arcs/sword-bearer.html", "Long book"), ("../analysis/two-daybreaks.html", "Daybreaks")],
    },
    {
        "n": 7,
        "rel": "manga/volume-7-read.html",
        "title": "Reading Volume 7 Night Battle | Collapse to Imitate | Kagurabachi",
        "desc": "Chapters 57–65. Train, Iori as cargo, Become the Samurai, Imitate. Volume 7’s spine word is also a weekly title.",
        "jp": "夜戦",
        "spine": "Night Battle",
        "chs": "57–65",
        "lede": "Transit fails. The daughter is a car. The son starts copying a closed-eye draw.",
        "secs": [
            ("The week list", [
                "57 Collapse. 58 Reunion (not chapter 130’s). 59 Blackout. 60 Resurrection. 61 Night Battle. 62 Iori. 63 Car Chase. 64 Become the Samurai. 65 Imitate. The Masumi job is a vehicle. Chihiro copies Iai. The hotel is not yet titled. The lids are not yet down on purpose against Samura.",
            ]),
            ("Spine", [
                "Night Battle is Volume 7’s word and chapter 61’s title. Sister: <a href=\"volume-7.html\">Volume 7</a>, <a href=\"../analysis/copy.html\">copy</a>.",
            ]),
        ],
        "links": [("volume-7.html", "Volume 7"), ("chapter-57.html", "Collapse"), ("chapter-62.html", "Iori"), ("chapter-65.html", "Imitate"), ("../world/iai.html", "Iai"), ("../factions/masumi.html", "Masumi")],
    },
    {
        "n": 8,
        "rel": "manga/volume-8-read.html",
        "title": "Reading Volume 8 Dawn | Hotel, Banquet, 夜明け | Kagurabachi",
        "desc": "Chapters 66–74. Truth, the hotel title, scar, Iai named, Future, second Daybreak, Dawn.",
        "jp": "夜明け",
        "spine": "Dawn",
        "chs": "66–74",
        "lede": "A school, a demolition, three morning words stacked so nobody can merge them.",
        "secs": [
            ("The week list", [
                "66 Truth. 67 Kyoto Bloodshed Hotel. 68 Metamorphosis. 69 The Guy with the Scar. 70 Iai White Purity Style. 71 Contest. 72 Future. 73 Daybreak (黎明). 74 Dawn (夜明け). Kuguri is the classroom. Hiruhiko is the set. The first Future lives here. 黎明 is not 夜更け. Dawn is the spine on the last weekly page.",
            ]),
            ("Sister", [
                "<a href=\"volume-8.html\">Volume 8</a>, <a href=\"../world/hotel.html\">hotel</a>, <a href=\"../analysis/two-futures.html\">two Futures</a>.",
            ]),
        ],
        "links": [("volume-8.html", "Volume 8"), ("chapter-67.html", "Hotel"), ("chapter-70.html", "Iai"), ("chapter-74.html", "Dawn"), ("../world/battle-hotel-play.html", "Play desk"), ("../analysis/two-daybreaks.html", "Daybreaks")],
    },
    {
        "n": 9,
        "rel": "manga/volume-9-read.html",
        "title": "Reading Volume 9 Enten | Banquet to Quickening | Kagurabachi",
        "desc": "Chapters 75–86. The Enten. Enten vs Tobimune. Volume 9’s spine is the seventh blade’s name.",
        "jp": "淵天",
        "spine": "Enten",
        "chs": "75–86",
        "lede": "The jacket and chapter 83 agree: the retraction is the book.",
        "secs": [
            ("The week list", [
                "75 Illusion. 76 Banquet. 77 No Longer Relevant. 78 Switch. 79 Threat!!. 80 Secret Room. 81 Core. 82 Enten Vs. Tobimune. 83 The Enten. 84 The Wounded. 85 Open. 86 Quickening. Suzaku’s surgery is already Switch. The closed-eye match is 82. The magazine says The Enten when the spine already did.",
            ]),
            ("Sister", [
                "<a href=\"volume-9.html\">Volume 9</a>, <a href=\"../world/battle-enten-tobimune.html\">the match</a>, <a href=\"../analysis/seventh-apology.html\">the apology</a>.",
            ]),
        ],
        "links": [("volume-9.html", "Volume 9"), ("chapter-76.html", "Banquet"), ("chapter-82.html", "Vs Tobimune"), ("chapter-83.html", "The Enten"), ("../blades/enten.html", "Enten"), ("../analysis/suzaku.html", "Suzaku")],
    },
    {
        "n": 10,
        "rel": "manga/volume-10-read.html",
        "title": "Reading Volume 10 The Swordsmen | Jacket Cruelty | Kagurabachi",
        "desc": "Chapters 87–95. Kiri, Natsuki, The Swordsmen. Hokuto on the same cloth as the younger Misaka.",
        "jp": "剣士たち",
        "spine": "The Swordsmen",
        "chs": "87–95",
        "lede": "A jacket that puts a rhyme next to a grave’s author.",
        "secs": [
            ("The week list", [
                "87 Phantoms. 88 The First Step. 89 Battle Chaos. 90 Kiri. 91 Natsuki. 92 The Swordsmen. 93 Finishing Touches. 94 The Second Arrow. 95 Flood. Volume 10’s cloth is Natsuki, Hokuto, Uruha, Yura. Sojo is already dead. Lightning Menace is voltage, not Mei. Kiri escorts Hakuri toward Shinuchi.",
            ]),
            ("Sister", [
                "<a href=\"volume-10.html\">Volume 10</a>, <a href=\"../characters/hokuto-and-natsuki.html\">Hokuto and Natsuki</a>.",
            ]),
        ],
        "links": [("volume-10.html", "Volume 10"), ("chapter-90.html", "Kiri"), ("chapter-91.html", "Natsuki"), ("chapter-92.html", "Swordsmen"), ("../characters/natsuki.html", "Natsuki"), ("../characters/hokuto.html", "Hokuto")],
    },
    {
        "n": 11,
        "rel": "manga/volume-11-read.html",
        "title": "Reading Volume 11 Heroes | Quotes, then Spine | Kagurabachi",
        "desc": "Chapters 96–105. Vessel. Worthless Commander. Quoted Strongest, Sword Master, Heroes. Transformation.",
        "jp": "英雄",
        "spine": "Heroes",
        "chs": "96–105",
        "lede": "The weekly title quoted the jacket word before the cloth used it clean.",
        "secs": [
            ("The week list", [
                "96 Urgency. 97 Vessel. 98 Ikuto Hagiwara, Worthless Commander. 99 “Strongest”. 100 “Sword Master”. 101 Safe Zone. 102 What You Need to See. 103 Healing. 104 “Heroes”. 105 Transformation. Yukisada sits in a barrier. The ACG commander is titled as cruelty. The press names get marks. Volume 11, 1 May 2026, puts Heroes on the spine after the magazine already doubted the word.",
            ]),
            ("Sister", [
                "<a href=\"volume-11.html\">Volume 11</a>, <a href=\"../analysis/quoted-press.html\">quoted press</a>, <a href=\"../world/battle-hq.html\">HQ week</a>.",
            ]),
        ],
        "links": [("volume-11.html", "Volume 11"), ("chapter-97.html", "Vessel"), ("chapter-100.html", "Sword Master"), ("chapter-104.html", "Heroes"), ("../analysis/quoted-press.html", "Quotes"), ("../world/hq.html", "HQ")],
    },
    {
        "n": 12,
        "rel": "manga/volume-12-read.html",
        "title": "Reading Volume 12 | Solicited Close | Kagurabachi",
        "desc": "Chapters 106–115 solicited for 4 September 2026. Karma through Swordsmith. Jacket not held on this desk.",
        "jp": "第12巻",
        "spine": "Volume 12 (solicited)",
        "chs": "106–115",
        "lede": "A solicitation is a fact. A held jacket is a different object.",
        "secs": [
            ("The week list", [
                "106 Karma. 107 This Moment. 108 Enten vs. Magatsumi. 109 Tobimune vs. Magatsumi. 110 As a Swordsman. 111 Apex. 112 Future (the second). 113 Rock. 114 Kunishige Rokuhira. 115 Swordsmith. ISBN 978-4-08-885177-8, 4 September 2026. Bonus chapter Soya Sazanami’s Memories, Begone! is listed with this close. This desk has not held a finished jacket to describe.",
            ]),
            ("Page turn", [
                "Part 1 closes around Swordsmith. Part 2 opens Princess. Sister: <a href=\"volume-12.html\">Volume 12</a>, <a href=\"../guide/part-2.html\">Part 2 guide</a>. Do not invent the cloth.",
            ]),
        ],
        "links": [("volume-12.html", "Volume 12"), ("chapter-108.html", "Enten vs Magatsumi"), ("chapter-114.html", "Kunishige"), ("chapter-115.html", "Swordsmith"), ("../guide/part-1.html", "Part 1"), ("../fun/soya-memories.html", "Soya extra")],
    },
]


def main():
    n = 0
    for v in VOLS:
        ok = page(
            v["rel"],
            v["title"],
            v["desc"],
            f"Volume {v['n']} · {v['chs']}",
            f"Reading Volume {v['n']}",
            v["jp"],
            v["lede"],
            v["secs"],
            v["links"],
        )
        if ok:
            n += 1
    print("vols wrote", n, "of", len(VOLS))


if __name__ == "__main__":
    main()
