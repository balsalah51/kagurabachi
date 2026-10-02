#!/usr/bin/env python3
"""Printed-fact essays for the quadruple wave."""
from quad_lib import page

ROOMS = []


def add(*a):
    ROOMS.append(a)


add(
    "analysis/two-deadlocks.html",
    "Two Deadlocks | 拮抗 and 均衡 | Kagurabachi",
    "Chapter 22 is Deadlock as 拮抗. Chapter 49 is Deadlock as 均衡. Same English, different Japanese, different rooms.",
    "Titles · 拮抗",
    "Two Deadlocks",
    "二つの膠着",
    "The magazine reuses English when the Japanese wants a second room.",
    [
        ("拮抗, the auction", [
            "Chapter 22, Deadlock, Japanese 拮抗, sits in the Rakuzaichi before Storehouse. Hiyuki is already in the building. The auction is not hot yet. Lukewarm was 21. The first Deadlock is temperature and a market that has not yet spent a son on a stone.",
            "Chihiro is inside a two-century firm. Hakuri is not yet the Kura. The English word is a stalemate. The Japanese is opposition, a balance of forces that can still move.",
        ]),
        ("均衡, the box", [
            "Chapter 49, Deadlock, Japanese 均衡, sits after The Kokugoku Steam Squad. Steam Squad just got a grave. The Sanso has been hit. Equilibrium here is the ugly kind: a box and a clan of ten, a train about to fail. Same English title. Different mineral.",
            "This desk files both on <a href=\"../world/title-collisions.html\">title collisions</a>. Recaps that merge them are doing the magazine’s Japanese a disservice. See <a href=\"titles.html\">what the titles are doing</a>.",
        ]),
    ],
    [("titles.html", "Titles"), ("../world/title-collisions.html", "Collisions"), ("../manga/chapter-22.html", "Ch. 22"), ("../manga/chapter-49.html", "Ch. 49"), ("../fun/chapter-titles.html", "Title list"), ("../arcs/rakuzaichi.html", "Rakuzaichi")],
)

add(
    "analysis/two-futures.html",
    "Two Futures | Chapter 72 and 112 | Kagurabachi",
    "The English Future is used twice. First in the hotel corridor. Again after Apex, before Rock.",
    "Titles · 未来",
    "Two Futures",
    "二つの未来",
    "Same English. Different week. Different hope.",
    [
        ("Hotel Future", [
            "Chapter 72, Future (未来), sits after Contest and before the second Daybreak. Chihiro is still in the Iai classroom’s weather. Iori is in the building. Hiruhiko has not yet finished dropping the set. The first Future is a hotel word: someone might still leave.",
        ]),
        ("After Apex", [
            "Chapter 112, Future (未来), sits after Apex and before Rock. Enten and Tobimune have already met Magatsumi. Volume 12 is about to carry Kunishige Rokuhira and Swordsmith as present-tense titles. The second Future is a war-book door: the island, the vein, the kiln.",
            "Do not flatten them. The magazine knew the English would collide. The chapters do not. See <a href=\"../world/title-collisions.html\">collisions</a>.",
        ]),
    ],
    [("titles.html", "Titles"), ("../manga/chapter-72.html", "Ch. 72"), ("../manga/chapter-112.html", "Ch. 112"), ("../world/title-collisions.html", "Collisions"), ("part-two-clock.html", "Part 2 clock"), ("../manga/part-2.html", "Part 2")],
)

add(
    "analysis/two-daybreaks.html",
    "Two Daybreaks | 夜更け and 黎明 | Kagurabachi",
    "Chapter 56 is Daybreak as 夜更け, Volume 6’s spine weather. Chapter 73 is Daybreak as 黎明, after the hotel Future.",
    "Titles · 夜明け前",
    "Two Daybreaks",
    "二つの夜明け",
    "Night-ending, then a different dawn word.",
    [
        ("夜更け", [
            "Chapter 56, Daybreak (夜更け), closes Volume 6’s argument after Fight Alongside. Senkutsuji’s ethics are already surgical. The Japanese is the small hours, night wearing out. Volume 6’s English spine is Daybreak. The weekly title and the jacket share a weather.",
        ]),
        ("黎明", [
            "Chapter 73, Daybreak (黎明), is the second English Daybreak. Japanese is dawn as a beginning, not the small hours. Chapter 74 is Dawn (夜明け), Volume 8’s spine word on the last weekly page of that book. The magazine stacks three morning words so nobody can pretend the hotel week was one sunrise.",
            "See <a href=\"../manga/volume-6.html\">Volume 6</a> and <a href=\"../manga/volume-8.html\">Volume 8</a>.",
        ]),
    ],
    [("titles.html", "Titles"), ("../manga/chapter-56.html", "Ch. 56"), ("../manga/chapter-73.html", "Ch. 73"), ("../manga/chapter-74.html", "Dawn"), ("../world/title-collisions.html", "Collisions"), ("../fun/volume-spines.html", "Spines")],
)

add(
    "analysis/smelting-sequence.html",
    "The Smelting Sequence | 125–129 | Kagurabachi",
    "Smelting, Fire, Smelting Parts 2 and 3, Ironworks. Datenseki into tamahagane. Chiaki in the fire.",
    "Part 2 · 製鉄",
    "The smelting sequence",
    "製鉄の連",
    "Hokazono talked to a real swordsmith so this would not be cosplay.",
    [
        ("The titles", [
            "Chapter 125 is Smelting (製鉄). Chapter 126 is Fire (火). Chapter 127 is Smelting, Part 2. Chapter 128 is Smelting, Part 3. Chapter 129 is Ironworks (製鉄 肆). The Japanese keeps the smelting word and counts. English gives the fourth a factory noun. Both are labor.",
            "Kunishige has not yet looked at the ore in the talks. The sequence is the looking. Subaru is the colleague who took a liking. Shiba will not let him quit. Chiaki is why the eyes stay open. Mashiro is still opposed to stealing ore for a civilian. Hasumi’s lab already failed.",
        ]),
        ("After Ironworks", [
            "Chapter 130 is I’m Fine! Chapter 131 is Tipping Point. The bureau’s choice, yield or stand the smith up, sits on the same clock as a reunion. The first Enchanted Blade’s name is still not printed on this desk. The sequence is work, not a reveal cheat.",
            "See <a href=\"../world/smelting.html\">smelting</a>, <a href=\"irishima.html\">the vein</a>, and <a href=\"../manga/chapter-129.html\">Ironworks</a>.",
        ]),
    ],
    [("../world/smelting.html", "Smelting"), ("../manga/chapter-125.html", "Ch. 125"), ("../manga/chapter-129.html", "Ironworks"), ("irishima.html", "Vein"), ("../world/tamahagane.html", "Tamahagane"), ("part-two-clock.html", "Clock")],
)

add(
    "analysis/boxes-fail.html",
    "Boxes That Do Not Hold | Sanso, Cell, Storehouse | Kagurabachi",
    "The Kamunabi put bearers in boxes. The Hishaku treat boxes as listings. Hakuri’s Kura is the box that walks.",
    "Theme · 箱",
    "Boxes that do not hold",
    "持たない箱",
    "Safety, in this book, is a room someone else can mail.",
    [
        ("Sanso", [
            "After the raid, surviving wartime bearers are locked in Sanso. Uruha is moved. Hiruhiko hits the box. Steam Squad dies on the way to a train that does not hold. Subaru is relocated when the pattern is obvious. Samura is at a temple, which is only a prettier box until Suzaku spends it as surgery.",
        ]),
        ("The basement", [
            "Magatsumi in the HQ basement is the state’s masterpiece box. Yukisada is a person seated so a barrier can be steered. Yura offers a body. The Sword Master leaves. Kasen’s leak already proved the workshop was a box with a mailing address.",
        ]),
        ("The walking exception", [
            "The Storehouse is a subspace that held loot and people. Hakuri inherits it and walks. The only box that works in the long book is the one that refuses to stay architecture. See <a href=\"../world/sanso.html\">Sanso</a>, <a href=\"../world/hq.html\">HQ</a>, and <a href=\"../world/storehouse.html\">Storehouse</a>.",
        ]),
    ],
    [("../world/sanso.html", "Sanso"), ("../world/hq.html", "HQ"), ("../world/storehouse.html", "Storehouse"), ("../world/barriers.html", "Barriers"), ("leak.html", "Leak"), ("suzaku.html", "Suzaku")],
)

add(
    "analysis/closed-eye.html",
    "Closed Eyes | Iai as Ethics | Kagurabachi",
    "Iai White Purity Style shuts the lids. Chihiro copies that on purpose. The hotel is where the ethic becomes a draw.",
    "Essay · 閉眼",
    "Closed eyes",
    "閉じた目",
    "Speed is the syllabus. The lids are the argument.",
    [
        ("The school", [
            "Itsuo Shirakai’s Iai White Purity Style is printed as eyes closed. Samura and Uruha are the famous students. Kiri brings an odachi anyway. Chihiro copies off Kuguri and the house style, eyes open, then shut. Chapter 64, Become the Samurai. Chapter 65, Imitate. Chapter 70 names the school.",
            "Closed eyes are not a power-up glow. They are a decision about what you will not look at while you cut. Samura erased a daughter so he would not have to look at a handle. Chihiro shuts his eyes so he can stand in that school’s argument without being enrolled.",
        ]),
        ("Against weather", [
            "Sojo’s weather is spectacle. Cloaked Mei, True Realm as slaughter. Chihiro’s later closed-eye draw is the opposite method: less looking, more brief. See <a href=\"copy.html\">copy</a> and <a href=\"../world/iai.html\">Iai</a>.",
        ]),
    ],
    [("copy.html", "Copy"), ("../world/iai.html", "Iai"), ("../characters/samura.html", "Samura"), ("../world/battle-hotel-iai.html", "Classroom"), ("../characters/itsuo.html", "Itsuo"), ("../manga/chapter-70.html", "Ch. 70")],
)

add(
    "analysis/storehouse-religion.html",
    "Storehouse as Religion | Firm, Cage, Walk | Kagurabachi",
    "The Sazanami treat the Kura as a house god. Chapter 35 titles Cage. Hakuri treats it as a building that can leave.",
    "Essay · 蔵",
    "Storehouse as religion",
    "蔵の信仰",
    "Two centuries of auction need a theology. The leftover becomes logistics.",
    [
        ("The theology", [
            "The Storehouse holds loot and people. That is a firm. The Sazanami talk about it as if it were a religion: selection, duty, defend to the death, fulfill. Chapter 35, Cage (檻), is the week the book says the quiet part. A subspace that warehouses humans is a cage even when the family calls it heritage.",
            "Kyora is the eleventh head, the priest of that firm. Hakuri is the error. Isou plus Storehouse in one living Sazanami is not a miracle the clan wanted. It is why Magatsumi can move when a government barrier splits.",
        ]),
        ("After the firm", [
            "When the Rakuzaichi ends, the theology ends. The walking Kura remains. Hakuri does not preach. He moves people and charged objects. See <a href=\"hakuri.html\">Hakuri’s essay</a> and <a href=\"../world/storehouse.html\">the Kura</a>.",
        ]),
    ],
    [("hakuri.html", "Hakuri essay"), ("../world/storehouse.html", "Storehouse"), ("../factions/sazanami.html", "Sazanami"), ("../manga/chapter-23.html", "Ch. 23"), ("../manga/chapter-35.html", "Cage"), ("../characters/kyora.html", "Kyora")],
)

add(
    "analysis/customer-vs-bearer.html",
    "Customer versus Bearer | Register Correction | Kagurabachi",
    "A Lifelong Contract is a nervous system. A sale is a receipt. Sojo paid. Ibuki held. Recaps that swap them fail the register.",
    "Essay · 顧客",
    "Customer versus bearer",
    "顧客と所持",
    "The sword already had a brief before the fan bought the leftover weather.",
    [
        ("The register", [
            "Ibuki Misaka, wartime bearer, retired, murdered, contract opened. Sojo, arms dealer, customer, cloaked Mei, True Realm as slaughter, Datenseki suicide. Chihiro, dying contract, residual charges, notes toward forging again. Natsuki never held Cloud Gouger. Lightning Menace is the rhyme without the mineral.",
            "Hishaku method: kill the bearer, open the contract, sell or assign. Yura sold. Hokuto opened. Kasen mailed the workshop. The customer is Volume 2. The original is a grave under the residual charges.",
        ]),
        ("Sister corrections", [
            "Enten is the seventh, not a sixth-plus. Magatsumi is Shinuchi at auction and a war crime in a field. Sword Master is a press name. This desk keeps a register so fandom labels do not overwrite receipts. See <a href=\"sojo-customer.html\">Sojo, customer</a> and <a href=\"../world/bearers.html\">bearers</a>.",
        ]),
    ],
    [("sojo-customer.html", "Customer"), ("sojo-fan.html", "Worst fan"), ("../world/bearers.html", "Bearers"), ("../world/contracts.html", "Contracts"), ("../characters/ibuki.html", "Ibuki"), ("../world/misaka-brothers.html", "Brothers")],
)

add(
    "analysis/seventh-apology.html",
    "The Seventh as Apology | Retraction in Steel | Kagurabachi",
    "Six wartime blades enter at +1 year 5 months. Enten is forged later because they cannot be smashed. A bowl, not a trophy.",
    "Essay · 七振目",
    "The seventh as apology",
    "謝罪の七振",
    "The goldfish are furniture first. The True Realm is a death.",
    [
        ("Why a seventh exists", [
            "Every attempt to destroy the wartime six fails. Kunishige and Chihiro forge Enten about fifteen years after the war. Kuro, Aka, Nishiki. True Realm: Magatsumi’s death. Dark power is not Enten’s usual color. The household stays a household even when the coat is black.",
            "The press can count seven miracles. The workshop counted one retraction. Chapter 83, The Enten, is the magazine agreeing. Volume 9’s spine is Enten. The jacket and the weekly title are the same argument.",
        ]),
        ("Part 2’s kiln", [
            "The war book shows the labor that will make the first wartime swords. The seventh is still years away and already the kind of answer Chiaki in the fire is practicing. The first blade’s name stays unprinted here. See <a href=\"enten-purpose.html\">purpose</a> and <a href=\"seventh-never.html\">never a trophy</a>.",
        ]),
    ],
    [("enten-purpose.html", "Purpose"), ("seventh-never.html", "Never a trophy"), ("../world/seventh.html", "The seventh"), ("../blades/enten.html", "Enten"), ("../fun/goldfish.html", "Goldfish"), ("../fun/bowl.html", "Bowl")],
)

add(
    "analysis/three-count.html",
    "The Three-Count | Most Blades, Not Magatsumi | Kagurabachi",
    "Most Enchanted Blades have three named techniques. Magatsumi does not keep the count. The insect kit is the exception filed as diet.",
    "Essay · 三つ",
    "The three-count",
    "三つの型",
    "A catalog rule, then the war sword that refuses it.",
    [
        ("The rule", [
            "Enten: Kuro, Aka, Nishiki, then shred and support extensions. Cloud Gouger: Mei, Yui, Kou, then cloaked Mei and Mei Shred. Tobimune: Owl, Crow, Suzaku. Kumeyuri: Play, Banquet, and the respect argument. The catalog teaches three as a household size.",
            "Magatsumi: Dragonfly, Centipede, Butterfly, Bee, Spider, Malediction. Cobweb, rings, cuts through buildings, flowers, about 200,000 civilians. Dark power is ordinary diet. The three-count is how you know the other swords were trying to be tools. This one is a climate.",
        ]),
        ("Why the count matters", [
            "Fandom kits that invent a third name for a blade that has not printed one fail the catalog. Two wartime swords stay unnamed, kit blank. This desk will not fill them. See <a href=\"../world/three-count.html\">the count file</a> and <a href=\"../world/techniques.html\">the catalog</a>.",
        ]),
    ],
    [("../world/three-count.html", "Count file"), ("../world/techniques.html", "Catalog"), ("../world/insect-kit.html", "Insect kit"), ("insect-camp.html", "Insect camp"), ("../blades/magatsumi.html", "Magatsumi"), ("true-realm.html", "True Realm")],
)

add(
    "analysis/quoted-press.html",
    "Quoted Press | Strongest, Sword Master, Heroes | Kagurabachi",
    "Chapters 99, 100, and 104 put quotation marks on the press. The basement is failing while the headlines stay clean.",
    "Essay · 「」",
    "Quoted press",
    "鉤括弧",
    "The magazine tells you the words are someone else’s.",
    [
        ("The three", [
            "Chapter 99 is “Strongest” (一番強い). Chapter 100 is “Sword Master” (剣聖). Chapter 104 is “Heroes” (英雄). Volume 11’s spine is Heroes. The weekly title puts the jacket word in quotes first. The press named Akemura. The press named a war. The book puts marks around the naming.",
        ]),
        ("While the building fails", [
            "HQ week spends Kudo, sits Yukisada in a barrier, and loses the Sword Master to a body offer. The headlines do not update in time. Quotation marks are the desk’s favorite politics. See <a href=\"quotation-marks.html\">quotes on the press</a> and <a href=\"../world/quoted-headlines.html\">headlines</a>.",
        ]),
    ],
    [("quotation-marks.html", "Quotes"), ("../world/quoted-headlines.html", "Headlines"), ("../manga/chapter-99.html", "Ch. 99"), ("../manga/chapter-100.html", "Ch. 100"), ("../manga/chapter-104.html", "Ch. 104"), ("../manga/volume-11.html", "Volume 11")],
)

add(
    "analysis/meal-method.html",
    "Meals as Method | Plate before True Realm | Kagurabachi",
    "A Good Meal, Peace, Food, Tea. The first book feeds people before it names slaughter as a realm.",
    "Essay · 膳",
    "Meals as method",
    "膳が先",
    "The plate is how you know who will not be spent.",
    [
        ("The titles", [
            "Chapter 5, A Good Meal (ごちそう). Chapter 6, Peace (平穏). Chapter 15, Food (飯). Chapter 17, Tea (茶). Cafe Haru Haru is the civilian door. Char still has to eat. Sojo’s people eat too. Moku later makes Chihiro eat on a Masumi road.",
            "True Realm is chapter 14, between Food’s neighbors. The book puts slaughter in the vocabulary only after it has already taught a table. Kunishige was a picky eater. Subaru is a sushi chef. The kiln still has to feed a man who barely ate.",
        ]),
        ("Sister desks", [
            "See <a href=\"meals.html\">the plate essay</a>, <a href=\"meals-to-quotes.html\">meals to quotes</a>, and <a href=\"workshop-kitchen.html\">the kitchen</a>. This page is the method sentence: if a recap skips the meals, it has already skipped who the hunt refuses to spend.",
        ]),
    ],
    [("meals.html", "Plate"), ("meals-to-quotes.html", "Meals to quotes"), ("workshop-kitchen.html", "Kitchen"), ("../world/food.html", "Food"), ("../world/cafe.html", "Cafe"), ("titles.html", "Titles")],
)

add(
    "analysis/false-death.html",
    "False Death as Surgery | Suzaku, Switch | Kagurabachi",
    "Samura cuts Uruha down at Senkutsuji. The look is a Hishaku pact. The art is contract surgery. Switch is the weekly receipt.",
    "Essay · 偽死",
    "False death as surgery",
    "偽りの死",
    "Keep the man. Kill the contract. Let the press be wrong.",
    [
        ("The look", [
            "Friendship and Fight Alongside already titled the Iai house. Senkutsuji spends those titles as a cut. Uruha looks dead. Kumeyuri’s Lifelong Contract is what died. Ro recovers the steel. Chapter 78, Switch (交代), is contracts moving. The assassination arc walks through a trick the state will not thank anyone for.",
        ]),
        ("The later spend", [
            "Black Suzaku is the version that does not fake. Samura spends his life, stalls Magatsumi’s drain, sends Tobimune to Iori, dies. One classmate gets a false grave. The other gets a real one. The school’s ethics are not gentle. They are specific. See <a href=\"suzaku.html\">Suzaku</a> and <a href=\"../world/battle-senkutsuji.html\">the temple desk</a>.",
        ]),
    ],
    [("suzaku.html", "Suzaku"), ("../world/battle-senkutsuji.html", "Temple desk"), ("../world/senkutsuji.html", "Senkutsuji"), ("../characters/uruha.html", "Uruha"), ("../manga/chapter-78.html", "Switch"), ("contract-hinge.html", "Contract hinge")],
)

add(
    "analysis/daughter-cargo.html",
    "Daughter as Cargo | Iori, Seal, Choice | Kagurabachi",
    "The Masumi move Iori as cargo so she cannot be a handle. Ikura breaks the seal by being someone she chooses to protect.",
    "Essay · 荷",
    "Daughter as cargo",
    "荷としての娘",
    "Chapter 62 names her. Chapter 63 is a car chase. The hotel ends the logistics.",
    [
        ("The brief", [
            "Samura erases Iori’s memories. Ro, Moku, Sumi keep her moving. The job is ugly and printed: a daughter treated as a handle to be unhooked. Chihiro is in the hotel copying a draw, not teaching her. Hiruhiko is there to drop the building. The cargo brief cannot survive a classmate who is a shield.",
        ]),
        ("The last send", [
            "Black Suzaku sends Tobimune to Iori. The father who unhooked her from steel makes her a bearer in the last accounting. Cargo becomes inheritance. This desk will not call that kindness without also calling it a Lifelong Contract. See <a href=\"../characters/samura-and-iori.html\">the pair</a>.",
        ]),
    ],
    [("../characters/iori.html", "Iori"), ("../characters/samura-and-iori.html", "Pair"), ("../factions/masumi.html", "Masumi"), ("../characters/ikura.html", "Ikura"), ("../world/hotel.html", "Hotel"), ("../world/black-suzaku.html", "Black Suzaku")],
)

add(
    "analysis/volume-jackets.html",
    "Jackets as Arguments | Eleven Spines | Kagurabachi",
    "Mission through Heroes, plus a solicited twelfth. The cloth is politics, not decoration.",
    "Essay · 表紙",
    "Jackets as arguments",
    "表紙は主張",
    "Equal is a word. The Swordsmen is a cruelty. Heroes arrives in quotes first.",
    [
        ("A few jackets", [
            "Volume 1, Mission: the household job. Volume 2: the weather fight. Volume 5 ends the auction on Unruly Punk’s week. Volume 6, Daybreak: the temple’s small hours. Volume 8, Dawn. Volume 9, Enten. Volume 10, The Swordsmen: Natsuki next to Hokuto. Volume 11, Heroes: the press word the weekly already quoted.",
            "Volume 12 is solicited for 4 September 2026, ISBN 978-4-08-885177-8, expected to carry Kunishige Rokuhira and Swordsmith. This desk files the solicitation, not a jacket it has not held.",
        ]),
        ("Sister rooms", [
            "See <a href=\"equal-jacket.html\">Equal</a>, <a href=\"../manga/covers.html\">cover studies</a>, and <a href=\"../fun/volume-spines.html\">spines</a>.",
        ]),
    ],
    [("equal-jacket.html", "Equal"), ("../manga/covers.html", "Covers"), ("../fun/volume-spines.html", "Spines"), ("../manga/volumes.html", "Volumes"), ("../guide/volume-map.html", "Volume map"), ("../manga/volume-10.html", "Vol. 10")],
)

add(
    "analysis/rest-weeks.html",
    "Rest Weeks as Print | Fire, September, Doors | Kagurabachi",
    "The 2026 rest after Fire, the September door for issue 44, and the rule that a rest is not a title.",
    "Essay · 休載",
    "Rest weeks as print",
    "休載も記録",
    "A missing magazine is a fact. It is not a chapter.",
    [
        ("After Fire", [
            "Chapter 126 is Fire. The 2026 rest sits after that labor before Ironworks resumes the kiln. This desk already files <a href=\"../fun/hiatus.html\">the 2026 rest</a>. Hokazono’s illness later moves chapter 132 to Jump 2026 issue 44, on sale 28 September 2026. That issue is a door. The title is not printed on this desk.",
        ]),
        ("What we will not do", [
            "We do not invent unpublished titles, first-blade names, or Fandom-only labels to fill a rest. See <a href=\"../fun/september-2026-rest.html\">September 2026</a> and <a href=\"../fun/jump-2026-44.html\">issue 44</a>. Official pages remain VIZ and MANGA Plus.",
        ]),
    ],
    [("../fun/hiatus.html", "2026 rest"), ("../fun/september-2026-rest.html", "September"), ("../fun/jump-2026-44.html", "Issue 44"), ("../manga/chapter-132.html", "Ch. 132 door"), ("../media/jump-return.html", "Return"), ("../manga/publication.html", "Publication")],
)

add(
    "analysis/color-dark.html",
    "When Color Goes Black | Dark Power | Kagurabachi",
    "Dark power is True Realm at the brink, or a dying blade. Mei Shred. Black Suzaku. Magatsumi’s ordinary diet.",
    "Essay · 黒",
    "When color goes black",
    "色が落ちる",
    "Output jumps. The household goldfish are the exception that proves the diet.",
    [
        ("The printed uses", [
            "Dark power (Kuroi chikara) is printed as True Realm at the brink of death, or a dying blade. Color goes black. Chihiro’s leftover Cloud Gouger charges go black because the blade is dying: Mei Shred. Samura’s Black Suzaku is the life spend. Magatsumi does not need a special week. Black is its pantry.",
            "Enten’s goldfish stay goldfish. The coat is already black because the house was painted that way. Recaps that treat every black panel as the same transformation flatten three different spends.",
        ]),
        ("Sister files", [
            "See <a href=\"../world/dark-power.html\">dark power</a>, <a href=\"../world/mei-shred.html\">Mei Shred</a>, and <a href=\"../world/black-suzaku.html\">Black Suzaku</a>.",
        ]),
    ],
    [("../world/dark-power.html", "Dark power"), ("true-realm.html", "True Realm"), ("../world/mei-shred.html", "Mei Shred"), ("../world/black-suzaku.html", "Black Suzaku"), ("../blades/magatsumi.html", "Magatsumi"), ("../fun/goldfish.html", "Goldfish")],
)

add(
    "analysis/bowl-hope.html",
    "Bowl as Hope | Goldfish, not Prophecy | Kagurabachi",
    "Chiaki in the fire is the hope that becomes a bowl. The goldfish are furniture before they are kit.",
    "Essay · 鉢",
    "Bowl as hope",
    "鉢という希望",
    "Hokazono almost drew carp. The fins and the bowl won.",
    [
        ("Furniture first", [
            "The workshop bowl is how you know the seventh blade is a household. Kuro, Aka, Nishiki are not a prophecy diagram. They are fish a picky smith and a quiet son kept on a table. The interview is on <a href=\"../fun/goldfish.html\">goldfish, not koi</a>. The fun room is <a href=\"../fun/bowl.html\">the bowl</a>.",
            "Ironworks puts Chiaki in the fire so Kunishige keeps his eyes open. That hope is years before Enten and already shaped like a bowl instead of a nation of flowers. Malediction is the other answer: a field the size of a country, filed as victory.",
        ]),
        ("Revenge to ledger", [
            "Chihiro’s first engine is revenge. The notes toward new Enten and even new Cloud Gouger are a smith’s ledger. The bowl taught the ledger. See <a href=\"revenge.html\">revenge</a> and <a href=\"enten-purpose.html\">purpose</a>.",
        ]),
    ],
    [("../fun/bowl.html", "Bowl"), ("../fun/goldfish.html", "Goldfish"), ("revenge.html", "Revenge"), ("enten-purpose.html", "Purpose"), ("../manga/chapter-129.html", "Ironworks"), ("malediction.html", "Malediction")],
)

add(
    "analysis/princess-office.html",
    "Princess as Office | Warrant, then Cargo | Kagurabachi",
    "Princess Soga is inherited foresight, proof of Izanami. Chiaki holds the title. Giyu would trade it.",
    "Essay · 姫",
    "Princess as office",
    "職としての姫",
    "Chapter 116 opens Part 2 on a job title, not a mood.",
    [
        ("The warrant", [
            "The Soga were prophecy aristocracy. They drove the Mikaboshi off the mainland. Chiaki’s foresight is inherited proof of Izanami. Princess is the office. Chapter 116, Princess (姫), is the war book’s first weekly word. The talks follow. Shiba is guardian. Kunishige has not looked at the ore.",
            "Giyu would trade the princess. Hiroto and Yoshinojo die to Ariu’s insects. The clan is not a chorus. Foresight as an office is already an essay on this shelf. This page is the reminder that 姫 is a job the bureau and the clan will both try to spend.",
        ]),
        ("The kiln", [
            "Chiaki in the fire is the office choosing a smith over a trade. See <a href=\"foresight.html\">foresight</a> and <a href=\"../characters/chiaki-and-giyu.html\">Chiaki and Giyu</a>.",
        ]),
    ],
    [("foresight.html", "Foresight"), ("../world/princess.html", "Princess"), ("../characters/chiaki.html", "Chiaki"), ("../manga/chapter-116.html", "Ch. 116"), ("../factions/soga.html", "Soga"), ("../characters/chiaki-and-giyu.html", "Pair")],
)

add(
    "analysis/sword-master-press.html",
    "Sword Master as Press Name | 剣聖 | Kagurabachi",
    "Akemura Soga is a man in a cell. Sword Master is what the press needed after a field of flowers.",
    "Essay · 剣聖",
    "Sword Master as press name",
    "新聞の剣聖",
    "Chapter 100 puts the name in quotes. The basement still has to hold the man.",
    [
        ("The naming", [
            "Malediction, 蠱, about 200,000 civilians, is covered as victory. Heroes, Strongest, Sword Master: the vocabulary that lets a nation keep six war crimes in a cellar instead of a court. Akemura is Magatsumi’s Lifelong Contract, the master key. If he dies, five other bearers die. The press name and the knot are why the Kamunabi keep him.",
        ]),
        ("The offer", [
            "Yura spends Shinuchi without drawing it and offers a body. The press name walks out of the basement. Quoted chapter 100 does not get a correction issue. See <a href=\"quotation-marks.html\">quotes</a> and <a href=\"../world/sword-master.html\">the name file</a>.",
        ]),
    ],
    [("quotation-marks.html", "Quotes"), ("../world/sword-master.html", "Name file"), ("../characters/akemura.html", "Akemura"), ("malediction.html", "Malediction"), ("../manga/chapter-100.html", "Ch. 100"), ("../characters/yura-and-akemura.html", "Offer")],
)

add(
    "analysis/named-person-titles.html",
    "Chapters Named for People | Uruha, Samura, Iori, Kiri | Kagurabachi",
    "The magazine sometimes stops describing a week and just names a person. That is a politics.",
    "Essay · 人名",
    "Chapters named for people",
    "人名の話",
    "A title that is only a name is a pointing finger.",
    [
        ("The list", [
            "Chapter 8 is Norisaku Madoka: I Will Change. Chapter 27 is Mr. Inazuma. Chapter 47 is Uruha. Chapter 51 is Samura. Chapter 62 is Iori. Chapter 90 is Kiri. Chapter 91 is Natsuki. Chapter 98 is Ikuto Hagiwara, Worthless Commander. Chapter 114 is Kunishige Rokuhira. Chapter 123 is Chiaki.",
            "Each name-week is a door. Uruha opens the long book. Samura opens the temple. Iori opens the cargo brief. Kiri and Natsuki open Volume 10’s jacket argument. Kunishige and Chiaki are present-tense on people the first page already complicated.",
        ]),
        ("What we skip", [
            "Chapters 118–120 stay table-only on this site, combined through <a href=\"../world/irishima-talks.html\">the talks room</a>. We do not invent a 132 name. See <a href=\"../fun/chapter-titles.html\">the title list</a>.",
        ]),
    ],
    [("titles.html", "Titles"), ("../fun/chapter-titles.html", "Title list"), ("../world/register.html", "Register"), ("named-graves.html", "Named graves"), ("../guide/chapter-map.html", "Chapter map"), ("../manga/chapters.html", "Index")],
)

add(
    "analysis/war-as-kiln.html",
    "War as Kiln | Part 2’s Labor | Kagurabachi",
    "The Seitei War book is not a highlight reel of named techniques. It is ore, talks, fire, and a choice.",
    "Essay · 炉",
    "War as kiln",
    "戦争は炉",
    "Irishima’s vein was always the war. The kiln is now on the page.",
    [
        ("The clock", [
            "Shokoku rises. Irishima already showed a vein. Japan harvests. Mikaboshi return. Talks, chapters 117–121, with 118–120 table-only here. Start, Chiaki, Powerless, then the smelting sequence. March 29 and April 1 sit on the handover clock. Tipping Point is the bureau’s choice week.",
            "This is not Chihiro’s coat for a while. It is the labor that will make the coat necessary. The first blade stays unnamed. Datenseki into tamahagane is the sentence. Flowers come later, as a crime, not as a technique list.",
        ]),
        ("Sister essays", [
            "See <a href=\"irishima.html\">the vein</a>, <a href=\"part-two-clock.html\">the clock</a>, and <a href=\"smelting-sequence.html\">the sequence</a>.",
        ]),
    ],
    [("irishima.html", "Vein"), ("part-two-clock.html", "Clock"), ("smelting-sequence.html", "Sequence"), ("../manga/part-2.html", "Part 2"), ("../arcs/seitei-war.html", "Seitei War"), ("../world/tamahagane.html", "Tamahagane")],
)


def main():
    n = 0
    for args in ROOMS:
        if page(*args):
            n += 1
    print("essays wrote", n, "of", len(ROOMS))


if __name__ == "__main__":
    main()
