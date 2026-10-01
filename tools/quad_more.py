#!/usr/bin/env python3
"""Location, guide, fun, faction, and publication rooms for the quadruple wave."""
from quad_lib import page

ROOMS = []


def add(*a):
    ROOMS.append(a)


# --- locations ---
add(
    "world/workshop-cellar.html",
    "The Rokuhira Cellar | Six Swords, One Bowl Upstairs | Kagurabachi",
    "The cellar held the wartime six Kunishige could not smash. Enten was forged upstairs. The raid empties the downstairs.",
    "Place · 蔵下",
    "The Rokuhira cellar",
    "工房の地下",
    "A household measured by what it refused to sell and could not destroy.",
    [
        ("Downstairs", [
            "After the treaty and the Malediction, Kunishige confiscates the six wartime Enchanted Blades and hides. Every attempt to destroy them fails. The cellar is that failure made into architecture. Enten is forged later, upstairs, about fifteen years after the war, as a retraction rather than a seventh trophy.",
            "The raid is three Hishaku. The six leave. Enten stays with the son. The cellar becomes an empty argument: the state wanted these sealed, the clan wanted them used, the smith wanted them gone. None of those three got the night they planned.",
        ]),
        ("Upstairs", [
            "House, forge, bowl. Chihiro grows up over the failure. The goldfish are furniture. The present-tense hunt is the cellar’s unfinished inventory. See <a href=\"workshop.html\">the workshop</a> and <a href=\"raid.html\">the raid</a>.",
        ]),
    ],
    [("workshop.html", "Workshop"), ("raid.html", "Raid"), ("../blades/index.html", "Blades"), ("seventh.html", "The seventh"), ("../characters/kunishige.html", "Kunishige"), ("objects.html", "Objects")],
)

add(
    "world/cafe-interior.html",
    "Cafe Haru Haru Interior | Table, Broker, Coat Off | Kagurabachi",
    "Hinao’s shop is the sit-down between jobs. The interior is how the underworld keeps a civilian hour.",
    "Place · 春々",
    "Cafe Haru Haru interior",
    "春々の店内",
    "Teleportation still needs a chair.",
    [
        ("What the room does", [
            "Cafe Haru Haru is Hinao’s. She brokers sorcerers. Shiba uses the door when Chihiro’s coat is too loud. Char can sit. Meals happen. The Tokyo underworld of the first book needs a table that is not Sojo’s compound and not a Kamunabi briefing.",
            "A Good Meal, Food, Tea, Peace: the weekly titles that taught the plate. The interior is those titles as furniture. This is not a menu the magazine printed line by line. It is a civilian door the book keeps using. See <a href=\"cafe.html\">the cafe file</a> and <a href=\"../characters/hinao-and-shiba.html\">Hinao and Shiba</a>.",
        ]),
    ],
    [("cafe.html", "Cafe"), ("food.html", "Food"), ("../characters/hinao.html", "Hinao"), ("../characters/shiba.html", "Shiba"), ("underworld.html", "Underworld"), ("../analysis/meal-method.html", "Meals")],
)

add(
    "world/auction-floor.html",
    "Rakuzaichi Auction Floor | Listing, Crowd, Shinuchi | Kagurabachi",
    "The 208th’s public room. Two centuries of buyers. The listing that ends the firm is a masterpiece name.",
    "Place · 会場",
    "The auction floor",
    "落罪市の座",
    "The Storehouse is the real building. The floor is the theater.",
    [
        ("The theater", [
            "Rakuzaichi is two hundred years of auction. The floor is where a crowd watches a firm pretend the Storehouse is culture. Shinuchi is the listing. Knight of Darkness, Deal, Confidence, Fervent, The Curtain Falls: weekly titles that know a theater when they see one.",
            "Chihiro lets the house take Enten so the blade can scout the Kura. He walks back in with Cloud Gouger’s stump. Hiyuki is lukewarm, then not. Inazuma has a sister inside. Prisoners are inventory until the building has to live long enough to empty.",
        ]),
        ("After the curtain", [
            "Kyora dies having seen the Sword Master through the listing. The firm ends. The floor does not get a 209th on this desk. See <a href=\"../arcs/rakuzaichi.html\">the arc</a> and <a href=\"storehouse.html\">Storehouse</a>.",
        ]),
    ],
    [("../arcs/rakuzaichi.html", "Rakuzaichi"), ("storehouse.html", "Storehouse"), ("naginojoen.html", "Naginojoen"), ("../characters/kyora.html", "Kyora"), ("../world/battle-rakuzaichi.html", "Fight desk"), ("../manga/chapter-41.html", "Fervent")],
)

add(
    "world/hotel-floors.html",
    "Kyoto Hotel Floors | Veil, Classroom, Rubble | Kagurabachi",
    "Sengoku’s Reigen house stacked as jobs: Masumi veil, Kuguri hallway, Play’s demolition, Samura’s arrival.",
    "Place · 階",
    "Kyoto hotel floors",
    "ホテルの階",
    "A building used as school, cargo bay, and set.",
    [
        ("Stacked jobs", [
            "The Kyoto Bloodshed Hotel is titled in chapter 67. Before that title, it is already Iori’s veil, Chihiro’s classroom, Kuguri’s scar, Ikura’s shield. After Play, it is rubble Toto can read a head from. The floors are not a map the magazine numbered for tourists. They are jobs stacked until the set drops.",
            "Reigen is Sengoku’s house art. The Masumi marker and motorcycle are how you reach a floor without advertising a bearer. Hiruhiko does not care about the marker. Banquet spends architecture. Feathers and goldfish share the wreck.",
        ]),
        ("Sister rooms", [
            "See <a href=\"hotel.html\">the hotel</a>, <a href=\"battle-hotel-iai.html\">the classroom</a>, and <a href=\"battle-hotel-play.html\">Play</a>.",
        ]),
    ],
    [("hotel.html", "Hotel"), ("reigen.html", "Reigen"), ("battle-hotel-iai.html", "Classroom"), ("battle-hotel-play.html", "Play"), ("../characters/sengoku.html", "Sengoku"), ("../manga/chapter-67.html", "Ch. 67")],
)

add(
    "world/hq-basement.html",
    "HQ Basement | Masterpiece, Vessel, Offer | Kagurabachi",
    "Magatsumi lives downstairs. Yukisada sits in the barrier. Yura offers a body. The Sword Master leaves.",
    "Place · B",
    "HQ basement",
    "本部地下",
    "The state’s safest room is the one that loses the man.",
    [
        ("Downstairs", [
            "The Kamunabi keep Akemura because Magatsumi is the master key. The basement is that policy as architecture. Yukisada, seventeen, is a Vessel and will not stay dead from decapitation. Hakuri can move charged objects and people. Kudo dies so that mover lives.",
            "Yura spends Shinuchi without drawing it. The offer is a body. Kasen’s leak is already upstairs on the table. Hiyuki’s duel domain is a street tool, not a basement tool. Shiba dumps what remains onto the street.",
        ]),
        ("Sister files", [
            "See <a href=\"hq.html\">headquarters</a>, <a href=\"level-one.html\">Level 1</a>, and <a href=\"battle-hq.html\">HQ week</a>.",
        ]),
    ],
    [("hq.html", "HQ"), ("level-one.html", "Level 1"), ("battle-hq.html", "HQ week"), ("vessel.html", "Vessel"), ("../characters/yukisada.html", "Yukisada"), ("../characters/akemura.html", "Akemura")],
)

add(
    "world/sanso-kokugoku.html",
    "Kokugoku Hot Spring Sanso | Box, Steam, Hit | Kagurabachi",
    "Uruha’s fortress. Steam Squad’s grave. Hiruhiko’s opening of the long book’s transit.",
    "Place · 国獄",
    "Kokugoku Sanso",
    "国獄の山荘",
    "Chapter 48 names the squad. The box is already a listing.",
    [
        ("The hit", [
            "Kokugoku Hot Spring Sanso is the Kamunabi box that holds Uruha long enough to be found. Fushimi’s Smoke Axe is named, then spent. The second Deadlock, 均衡, sits on this week. A train follows. Collapse is 57. The state’s hot spring is a target.",
            "Samura is not in this box. He is at Senkutsuji. Subaru will be relocated when the pattern is obvious. The Sanso system is one idea: advertise a bearer as safe. The Hishaku fire-gate is the other idea.",
        ]),
        ("Sister files", [
            "See <a href=\"sanso.html\">Sanso</a>, <a href=\"battle-sanso.html\">the fight desk</a>, and <a href=\"../factions/steam-squad.html\">Steam Squad</a>.",
        ]),
    ],
    [("sanso.html", "Sanso"), ("battle-sanso.html", "Fight desk"), ("../factions/steam-squad.html", "Steam Squad"), ("../characters/uruha.html", "Uruha"), ("../characters/fushimi.html", "Fushimi"), ("smoke-axe.html", "Smoke Axe")],
)

add(
    "world/senkutsuji-grounds.html",
    "Senkutsuji Grounds | Return, Clear, Surgery | Kagurabachi",
    "The temple grounds are where Hakuri returns Tobimune and Samura spends Friendship as a cut.",
    "Place · 境内",
    "Senkutsuji grounds",
    "仙窟寺の境内",
    "Owl’s later launch site starts as a Buddhist room.",
    [
        ("The grounds", [
            "Hakuri walks a support blade across the country into a temple. Samura clears the grounds, then cuts Uruha down. Suzaku: kill the contract, keep the man. The look is a pact. The grounds are a surgery. Masumi have already been in this logic as silence-keepers. Owl will later treat Japan as a room the way this temple treated a classmate.",
        ]),
        ("Sister files", [
            "See <a href=\"senkutsuji.html\">the temple</a> and <a href=\"battle-senkutsuji.html\">the fight desk</a>.",
        ]),
    ],
    [("senkutsuji.html", "Temple"), ("battle-senkutsuji.html", "Fight desk"), ("../analysis/suzaku.html", "Suzaku"), ("owl.html", "Owl"), ("../characters/samura.html", "Samura"), ("../factions/masumi.html", "Masumi")],
)

add(
    "world/soga-house.html",
    "The Soga House | Prophecy Aristocracy | Kagurabachi",
    "Mainland foresight clan. Princess as office. A house that would trade a daughter and also put her in a fire so a smith keeps his eyes open.",
    "Place · 曽我",
    "The Soga house",
    "曽我家",
    "Not a chorus. An office with factions.",
    [
        ("Who lives in the argument", [
            "Chiaki holds Princess Soga. Hiroto is clan head, Kurotsuchi, dead to Ariu. Yoshinojo dies the same insect way. Giyu would trade the princess. Shiba is a guardian, not a blood Soga, assigned to the office. Akemura is the wartime uncle the press named Sword Master.",
            "The house pushed the Mikaboshi off the mainland a thousand years back on this timeline. Irishima’s talks put the house back on an island the old kings want. Reunion and Tipping Point share a clock with a bureau choice about Kunishige.",
        ]),
        ("Sister files", [
            "See <a href=\"../factions/soga.html\">Soga</a>, <a href=\"../analysis/princess-office.html\">princess as office</a>, and <a href=\"lineage.html\">lineage</a>.",
        ]),
    ],
    [("../factions/soga.html", "Soga"), ("../characters/chiaki.html", "Chiaki"), ("../analysis/princess-office.html", "Office"), ("lineage.html", "Lineage"), ("irishima.html", "Irishima"), ("../characters/giyu.html", "Giyu")],
)

add(
    "world/irishima-table.html",
    "Irishima Talks Table | 117–121 | Kagurabachi",
    "The table the war book opens on. Chapters 118–120 stay table-only on this site. The combined room holds the vein.",
    "Place · 会談",
    "Irishima talks table",
    "杁島の卓",
    "Property first. Romance is not the title list.",
    [
        ("How this desk files the talks", [
            "Chapter 117 is The Irishima Talks. 118–120 are parts 2–4, table-only here, no solo rooms. 121 is The Irishima Talks END. Chiaki, Shiba as guardian, Kunishige still a picky dealer, Mashiro still opposed, Hasumi’s lab still a failure, Ariu’s insects already a camp of explainers. The table is Part 2’s opening property.",
            "We do not invent dialogue for the unlinked weeks. The combined file is <a href=\"irishima-talks.html\">Irishima talks</a>. The island is <a href=\"irishima.html\">Irishima</a>. The risen land is <a href=\"shokoku.html\">Shokoku</a>. The clock is March 29 and April 1.",
        ]),
    ],
    [("irishima-talks.html", "Talks"), ("irishima.html", "Irishima"), ("shokoku.html", "Shokoku"), ("../analysis/irishima.html", "Vein essay"), ("../manga/part-2.html", "Part 2"), ("march-twenty-nine.html", "March 29")],
)

add(
    "world/undersea-rooms.html",
    "Undersea Habitat | Mikaboshi Bodies | Kagurabachi",
    "Old sorcerer kings survived under the sea with bodies that can live with Datenseki. The habitat is that adaptation as a place.",
    "Place · 海底",
    "Undersea habitat rooms",
    "海底の部屋",
    "The vein was never only an island.",
    [
        ("Adapted bodies", [
            "The Soga drove the Mikaboshi off the mainland. The old kings survived under the sea. Datenseki-adapted bodies. Ariu’s Sumika is insect work. A camp treats Magatsumi as that kit recast in steel. This desk marks the camp. The habitat is printed as the place those bodies lived.",
            "Shokoku rises. The return is not a metaphor. Japan harvested a vein Irishima’s earthquake had already shown. The war book’s talks sit on top of a sea that already had rooms.",
        ]),
        ("Sister files", [
            "See <a href=\"undersea.html\">undersea</a>, <a href=\"../factions/mikaboshi.html\">Mikaboshi</a>, and <a href=\"sumika.html\">Sumika</a>.",
        ]),
    ],
    [("undersea.html", "Undersea"), ("../factions/mikaboshi.html", "Mikaboshi"), ("sumika.html", "Sumika"), ("shokoku.html", "Shokoku"), ("../characters/ariu.html", "Ariu"), ("../analysis/insect-camp.html", "Insect camp")],
)

# --- guides ---
add(
    "guide/after-sojo.html",
    "After Sojo | What Volume 3 Starts | Kagurabachi",
    "A spoiler-aware door for readers who just watched Enten bisect Cloud Gouger and want the next map, not a leak.",
    "Guide · その後",
    "After Sojo",
    "双城のあと",
    "The customer is dead. The auction is the next building.",
    [
        ("What just happened", [
            "You have finished Vs. Sojo if chapter 18, Roar, has happened. Enten bisected Cloud Gouger. Sojo died on Datenseki. The Anti-Cloud Gouger Special Forces spent themselves. Char is off the table. Chihiro has a stump and leftover charges. Sojo was a customer, not Hishaku. Ibuki was the original bearer.",
        ]),
        ("What the next book is", [
            "Volume 3 opens Knight of Darkness. The 208th Rakuzaichi lists Shinuchi. Hakuri is not yet the Storehouse. Hiyuki is the Kamunabi’s Weapon, then Lukewarm. Read officially on VIZ or MANGA Plus. This desk’s arc file is <a href=\"../arcs/rakuzaichi.html\">Rakuzaichi</a>. The pair that will matter is <a href=\"../characters/chihiro-and-hakuri.html\">Chihiro and Hakuri</a>.",
        ]),
        ("What not to skip", [
            "Mr. Inazuma is a person with a sister inside. Tenri’s stone is a Datenseki rhyme you already watched kill a customer. Kyora will look through the listing. The firm ends. Then the long book names Uruha.",
        ]),
    ],
    [("../arcs/vs-sojo.html", "Vs. Sojo"), ("../arcs/rakuzaichi.html", "Rakuzaichi"), ("reading-order.html", "Reading order"), ("../characters/chihiro-and-hakuri.html", "Pair"), ("../world/battle-chihiro-sojo.html", "Fight desk"), ("cast.html", "Cast")],
)

add(
    "guide/after-rakuzaichi.html",
    "After Rakuzaichi | The Long Book Door | Kagurabachi",
    "The firm ended. Magatsumi went to the state. Enten stayed. Chapter 47 is Uruha. Boxes start failing.",
    "Guide · 閉幕のあと",
    "After Rakuzaichi",
    "落罪市のあと",
    "Unruly Punk closes the auction. The next title is a wartime bearer.",
    [
        ("What you are holding", [
            "Hakuri walks with Isou and the Storehouse. Kyora is dead. Tenri is a mineral grave. Soya is blank. Chihiro is on the Kamunabi books with Enten in his hand and a masterpiece in a basement that will not stay a basement.",
        ]),
        ("Where the long book goes", [
            "Sanso, train, Senkutsuji, Kyoto Bloodshed Hotel, HQ. Samura, Iori, Hiruhiko, Kuguri, Kasen’s leak, Yura’s offer. Read the <a href=\"../arcs/sword-bearer.html\">Sword Bearer</a> file. If the temple looks like a betrayal, open <a href=\"../analysis/suzaku.html\">Suzaku</a> before you file a pact.",
        ]),
    ],
    [("../arcs/rakuzaichi.html", "Rakuzaichi"), ("../arcs/sword-bearer.html", "Sword Bearer"), ("../world/battle-senkutsuji.html", "Temple"), ("part-1.html", "Part 1"), ("reading-order.html", "Order"), ("../characters/uruha.html", "Uruha")],
)

add(
    "guide/after-hotel.html",
    "After the Hotel | Eyes Shut, Building Down | Kagurabachi",
    "Iai copied. Play spent the set. Samura arrived. The assassination arc still has a basement to lose.",
    "Guide · ホテルのあと",
    "After the hotel",
    "階のあと",
    "Enten vs Tobimune is already titled. HQ is next politics.",
    [
        ("What the hotel taught", [
            "Chihiro can shut his eyes on purpose. Iori chose someone. Hiruhiko dropped a building. Toto read a head. Kumeyuri’s Play has been used as contempt. The support blade and the seventh blade have a weekly versus.",
        ]),
        ("What is still downstairs", [
            "Magatsumi, Kasen, Yukisada, Kudo, Yura’s offer. Quoted press titles. Volume 10’s jacket cruelty. Volume 11’s Heroes. Then Swordsmith and a page turn to Princess. See <a href=\"../world/battle-hq.html\">HQ week</a> and <a href=\"part-2.html\">Part 2</a>.",
        ]),
    ],
    [("../world/hotel.html", "Hotel"), ("../world/battle-enten-tobimune.html", "Enten vs Tobimune"), ("../world/battle-hq.html", "HQ"), ("../arcs/sword-bearer.html", "Long book"), ("part-1.html", "Part 1"), ("reading-order.html", "Order")],
)

add(
    "guide/spoiler-ladder.html",
    "Spoiler Ladder | How Far You Have Read | Kagurabachi",
    "A ladder of rooms that stay useful if you stop at Sojo, at the curtain, at Swordsmith, or at Tipping Point.",
    "Guide · 梯子",
    "Spoiler ladder",
    "ネタバレの梯子",
    "The archive is an encyclopedia. This page is a stop sign you can move.",
    [
        ("Through chapter 18", [
            "Safe-ish doors: <a href=\"premise.html\">premise</a>, <a href=\"../characters/chihiro.html\">Chihiro</a>, <a href=\"../blades/enten.html\">Enten</a>, <a href=\"../arcs/vs-sojo.html\">Vs. Sojo</a>, <a href=\"after-sojo.html\">after Sojo</a>. Skip hotel, HQ, Part 2, and any Magatsumi insect name you have not met.",
        ]),
        ("Through chapter 46", [
            "Add <a href=\"../arcs/rakuzaichi.html\">Rakuzaichi</a>, <a href=\"../characters/hakuri.html\">Hakuri</a>, <a href=\"after-rakuzaichi.html\">after the auction</a>. Skip Senkutsuji’s cut if you want the temple raw.",
        ]),
        ("Through chapter 115", [
            "Part 1 is on the table. <a href=\"part-1.html\">the long cut</a>, <a href=\"../analysis/index.html\">essays</a>, quoted press, Suzaku. Part 2 starts at Princess. <a href=\"part-2.html\">the forge door</a> is labeled.",
        ]),
        ("Through chapter 131", [
            "Tipping Point is the last titled room. Chapter 132 is a publication door without a printed title here. Irishima 118–120 stay table-only. Do not use spoiler blogs to fill this desk.",
        ]),
    ],
    [("reading-order.html", "Order"), ("chapter-map.html", "Chapter map"), ("part-1.html", "Part 1"), ("part-2.html", "Part 2"), ("../fun/first-read.html", "First read"), ("sunday-legal.html", "Legal Sunday")],
)

add(
    "guide/newcomer-hour.html",
    "Newcomer Hour | One Sitting Map | Kagurabachi",
    "If you have one hour before chapter 1: official door, premise, three blades, one warning about Sojo.",
    "Guide · 一時間",
    "Newcomer hour",
    "最初の一時間",
    "Do not start on a theory video. Start on VIZ or MANGA Plus.",
    [
        ("Fifteen minutes", [
            "Read <a href=\"series.html\">the series</a> and <a href=\"premise.html\">the premise</a>. Kagurabachi is Takeru Hokazono in Weekly Shōnen Jump from 2023 #42. Chihiro, Kunishige, a raid, a seventh blade that is a retraction. Official chapters: VIZ and MANGA Plus. We do not host pages.",
        ]),
        ("Fifteen more", [
            "<a href=\"blades.html\">The blades</a>: Enten, Cloud Gouger, Magatsumi, Tobimune, Kumeyuri, two wartime unnamed. Enten is seventh. Sojo is a customer. Malediction’s kanji is 蠱. Birthdays printed: Chihiro 11 Aug, Kunishige 5 June, Shiba 15 Oct, Sojo 6 June, Char 21 Dec.",
        ]),
        ("The rest of the hour", [
            "Open chapter 1, Mission. If you want a handrail after, <a href=\"../fun/first-read.html\">first-read notes</a> and <a href=\"reading-order.html\">reading order</a>. Skip the Sunday board until you have a week you want to talk about.",
        ]),
    ],
    [("series.html", "Series"), ("premise.html", "Premise"), ("blades.html", "Blades"), ("reading-order.html", "Order"), ("../fun/first-read.html", "First read"), ("cast.html", "Cast")],
)

add(
    "guide/official-only.html",
    "Official-Only Desk | What This Archive Will Not File | Kagurabachi",
    "Printed Jump, tankōbon, VIZ, MANGA Plus. No unpublished titles, no first-blade name, no Fandom-only kit.",
    "Guide · 正本",
    "Official-only desk",
    "正本のみ",
    "A rest week is a fact. A leak is not a chapter.",
    [
        ("Will file", [
            "Weekly titles through chapter 131, Tipping Point (転換点). Volume jackets 1–11 and the Volume 12 solicitation. Technique names on the catalog. The five printed birthdays. Cypic, Takeuchi, April 2027. Circulation steps to 4 million by April 2026. Irishima talks 118–120 as a combined room.",
        ]),
        ("Will not file", [
            "Chapter 132’s title or plot until VIZ, MANGA Plus, or the Wikipedia chapter list this desk trusts prints it. The first Enchanted Blade’s name. Invented kanji. U+2014 em-dashes in live HTML. Shop modules on the homepage or character and blade pages. Solo rooms for 118–120.",
        ]),
        ("Where to read", [
            "VIZ Shonen Jump and MANGA Plus. Japanese magazine pages at Shonen Jump. Japanese Jump Comics for extras. See <a href=\"sunday-legal.html\">legal Sunday</a> and <a href=\"../about.html\">about</a>.",
        ]),
    ],
    [("sunday-legal.html", "Legal Sunday"), ("../about.html", "About"), ("../faq.html", "FAQ"), ("reading-order.html", "Order"), ("../manga/chapter-132.html", "132 door"), ("../world/first-blade.html", "First blade")],
)

add(
    "guide/who-dies.html",
    "Who Dies, Printed | Named Fates Door | Kagurabachi",
    "A door onto the deaths file: raid, weather, auction stone, Steam Squad, hotel owner, Kudo, Samura’s life spend.",
    "Guide · 死者",
    "Who dies, printed",
    "死の記録",
    "Spoiler-heavy on purpose. Use the ladder if you are early.",
    [
        ("The list lives elsewhere", [
            "The encyclopedia file is <a href=\"../world/deaths.html\">deaths</a>. This guide door exists so the beginner map can point at a labeled graveyard instead of hiding names in premise paragraphs. Kunishige in the raid. Ibuki off-page for a contract. ACG specialists. Sojo on Datenseki. Tenri on a stone. Fushimi and Steam Squad. Sengoku at the hotel. Kudo at HQ. Black Suzaku as a life spend.",
        ]),
        ("False graves", [
            "Uruha’s temple cut is surgery, not a last page. Soya’s amnesia is not death. Yukisada will not stay dead from decapitation. Read the deaths file before you correct a Sunday thread with a maybe.",
        ]),
    ],
    [("../world/deaths.html", "Deaths"), ("spoiler-ladder.html", "Ladder"), ("../world/named-graves.html", "Named graves"), ("../analysis/named-graves.html", "Graves essay"), ("../world/battle-index.html", "Fights"), ("cast.html", "Cast")],
)

add(
    "guide/who-holds.html",
    "Who Holds What | Bearer Register Door | Kagurabachi",
    "A beginner door onto the bearer list: wartime six, Enten, customers, leftovers, two unnamed.",
    "Guide · 所持",
    "Who holds what",
    "誰が持つか",
    "A Lifelong Contract is a nervous system. A sale is a receipt.",
    [
        ("The short register", [
            "Enten: Chihiro. Cloud Gouger: Ibuki, then Sojo as customer, then Chihiro on dying charges. Magatsumi: Akemura, listed as Shinuchi, spent by Yura without a draw. Tobimune: Samura, last send toward Iori. Kumeyuri: Uruha, recovered by Ro after surgery. Two wartime blades unnamed, kit blank. Natsuki holds Lightning Menace, not Cloud Gouger.",
        ]),
        ("Full files", [
            "<a href=\"../world/bearers.html\">Bearers</a>, <a href=\"../world/contracts.html\">contracts</a>, <a href=\"blades.html\">blades guide</a>, <a href=\"technique-map.html\">technique map</a>. Do not invent the first blade’s holder.",
        ]),
    ],
    [("../world/bearers.html", "Bearers"), ("blades.html", "Blades"), ("technique-map.html", "Techniques"), ("../world/contracts.html", "Contracts"), ("../analysis/customer-vs-bearer.html", "Customer vs bearer"), ("../world/first-blade.html", "First blade")],
)

add(
    "guide/quad-doors.html",
    "Quadruple Wave | New Rooms This Desk | Kagurabachi",
    "Bonds, fight desks, essays, place satellites, guides, volume reading rooms, and deepened old pages. Printed facts only.",
    "Guide · 増築",
    "Quadruple wave",
    "四倍の増築",
    "More rooms. Same register. No invented chapter 132.",
    [
        ("What landed", [
            "Relationship rooms under Characters, starting at <a href=\"../characters/bonds.html\">printed bonds</a>. Fight desks under World, starting at <a href=\"../world/battle-index.html\">fight desks</a>. New essays under Analysis. Place satellites for cellar, cafe interior, auction floor, hotel floors, HQ basement, Kokugoku, Senkutsuji grounds, Soga house, Irishima table, undersea rooms.",
            "Guide doors for after Sojo, after the auction, after the hotel, spoiler ladder, newcomer hour, official-only desk, who dies, who holds. Volume reading rooms on the manga shelf. Fun and faction satellites. Old chapter and character pages deepened with printed addenda.",
        ]),
        ("What did not land", [
            "No solo rooms for Irishima talks 118–120. No first-blade name. No chapter 132 title. No em-dash in live HTML. Official reading stays on VIZ and MANGA Plus. The previous mega doors remain at <a href=\"mega-doors.html\">mega update</a>.",
        ]),
    ],
    [("mega-doors.html", "Mega doors"), ("../characters/bonds.html", "Bonds"), ("../world/battle-index.html", "Fights"), ("../analysis/index.html", "Essays"), ("chapter-map.html", "Chapters"), ("volume-map.html", "Volumes")],
)

# --- fun / publication ---
add(
    "fun/year-2023.html",
    "Kagurabachi in 2023 | First Issue, Meme, Mission | Kagurabachi",
    "Weekly Shōnen Jump 2023 #42, 19 September. Chapter 1 most-viewed new title on MANGA Plus. The meme before the plates.",
    "Year · 2023",
    "2023",
    "二〇二三",
    "Black coat, white type, a fish English Twitter decided was the next Big Three.",
    [
        ("The start", [
            "Takeru Hokazono, born 6 September 2000, Osaka. Enten one-shot at the 100th Tezuka Awards, Jump Giga Spring 2021, then Giga and Jump shorts. The serial begins 19 September 2023, Jump 2023 #42, chapter 1 Mission (すべきこと). Most-viewed new title on MANGA Plus in its first week.",
            "VIZ and MANGA Plus simulpub the same week. Chapter 1 is usually free forever on Plus. That is how a week of jokes became readers. The Japanese tankōbon is still months away (2 February 2024).",
        ]),
        ("Sister rooms", [
            "See <a href=\"first-issue.html\">the first issue</a>, <a href=\"meme.html\">meme to flagship</a>, and <a href=\"../manga/publication.html\">publication</a>.",
        ]),
    ],
    [("first-issue.html", "First issue"), ("meme.html", "Meme"), ("../manga/publication.html", "Publication"), ("hokazono.html", "Hokazono"), ("../manga/chapter-1.html", "Chapter 1"), ("pre-serial.html", "Pre-serial")],
)

add(
    "fun/year-2024.html",
    "Kagurabachi in 2024 | Volumes, Award, Plus Views | Kagurabachi",
    "Volume 1 on 2 February. Next Manga Award, print. 99 million MANGA Plus views by April. One million copies by October.",
    "Year · 2024",
    "2024",
    "二〇二四",
    "The meme year becomes a book year.",
    [
        ("Paper", [
            "Jump Comics Volume 1, Mission, 2 February 2024, ISBN 978-4-08-883819-9. VIZ English Volume 1, 5 November 2024, ISBN 978-1-9747-4724-5. Next Manga Award, print category, 2024. Nominations later for other prizes sit on the publication page.",
            "By April 2024 MANGA Plus had logged over 99 million page views. Circulation: 1 million by October 2024. The first book’s weather fight and the auction’s start are the year’s weekly weather.",
        ]),
        ("Sister rooms", [
            "See <a href=\"next-manga.html\">Next Manga</a> and <a href=\"circulation.html\">circulation</a>.",
        ]),
    ],
    [("next-manga.html", "Next Manga"), ("circulation.html", "Circulation"), ("../manga/volume-1.html", "Volume 1"), ("../manga/publication.html", "Publication"), ("english-trail.html", "English trail"), ("../manga/volumes.html", "Volumes")],
)

add(
    "fun/year-2025.html",
    "Kagurabachi in 2025 | Two Million, then Three | Kagurabachi",
    "Circulation 2.2 million by May 2025, 3 million by October. The long book is the year’s commute.",
    "Year · 2025",
    "2025",
    "二〇二五",
    "Sanso, hotel, quoted press. The flagship year.",
    [
        ("The count", [
            "2.2 million copies by May 2025. 3 million by October 2025. The Sword Bearer Assassination arc is the commute: Uruha, Samura, Iori, hotel, HQ. English volumes continue in parallel, not as a color-matched set.",
        ]),
        ("Sister rooms", [
            "See <a href=\"circulation.html\">circulation</a> and <a href=\"../arcs/sword-bearer.html\">the long book</a>.",
        ]),
    ],
    [("circulation.html", "Circulation"), ("../arcs/sword-bearer.html", "Sword Bearer"), ("../manga/publication.html", "Publication"), ("toc.html", "ToC"), ("../manga/volumes.html", "Volumes"), ("pacing.html", "Pacing")],
)

add(
    "fun/year-2026.html",
    "Kagurabachi in 2026 | Four Million, Volume 12, Tipping Point | Kagurabachi",
    "4 million by April. Volume 11 Heroes on 1 May. Volume 12 solicited 4 September. Chapter 131 on 6 September. Issue 44 is a door.",
    "Year · 2026",
    "2026",
    "二〇二六",
    "Part 2’s kiln year. Daruma. A rest. A door without a title on this desk.",
    [
        ("The shelf", [
            "Circulation crossed 4 million by April 2026. Volume 11, Heroes, 1 May. Japan Expo Daruma for Best Action Manga. Volume 12 solicited 4 September 2026, ISBN 978-4-08-885177-8. Chapter 129 Ironworks 23 August. Chapter 130 I’m Fine!. Chapter 131 Tipping Point, Jump 2026 #41, 6 September.",
            "A rest after Fire. A later rest and illness move chapter 132 to Jump 2026 #44, on sale 28 September 2026. This desk files the door, not a title. Cypic’s first twenty minutes toured from July 2026. Anime remains April 2027.",
        ]),
        ("Sister rooms", [
            "See <a href=\"hiatus.html\">the rest</a>, <a href=\"september-2026-rest.html\">September</a>, and <a href=\"../manga/part-2.html\">Part 2</a>.",
        ]),
    ],
    [("circulation.html", "Circulation"), ("hiatus.html", "Rest"), ("september-2026-rest.html", "September"), ("../manga/part-2.html", "Part 2"), ("../manga/chapter-131.html", "Ch. 131"), ("../media/anime.html", "Anime")],
)

add(
    "fun/jump-issue-doors.html",
    "Jump Issue Doors | Magazine as Object | Kagurabachi",
    "A map of issue rooms this archive already keeps: first issue, 2026 #41, 2026 #44. A rest is not a chapter.",
    "Fun · 号",
    "Jump issue doors",
    "ジャンプの号",
    "The magazine is a date. The title is a different object.",
    [
        ("What we have", [
            "<a href=\"first-issue.html\">2023 #42</a> starts the serial. <a href=\"jump-2026-41.html\">2026 #41</a> holds Tipping Point. <a href=\"jump-2026-44.html\">2026 #44</a> is chapter 132’s door. <a href=\"hiatus.html\">Rests</a> are filed as print facts, not as fake chapters.",
        ]),
        ("What we will not mass-produce", [
            "A stub for every weekly number is a sitemap trick, not an encyclopedia. This desk keeps doors where the magazine date is doing politics: first week, rest weeks, return weeks. See <a href=\"../manga/publication.html\">publication</a>.",
        ]),
    ],
    [("first-issue.html", "First issue"), ("jump-2026-41.html", "2026 #41"), ("jump-2026-44.html", "2026 #44"), ("hiatus.html", "Rests"), ("toc.html", "ToC"), ("../manga/publication.html", "Publication")],
)

add(
    "fun/bathhouse-quest-2.html",
    "Bathhouse Quest #2 | Second Extra | Kagurabachi",
    "Genichi Sojo’s Bathhouse Quest has a second printed part. Buy the book. This desk will not host the extra.",
    "Extra · ♨2",
    "Bathhouse Quest #2",
    "お風呂探訪 2",
    "The customer hunts a tub again. The tankōbon is the door.",
    [
        ("Two parts", [
            "Wikipedia’s bonus list files Genichi Sojo’s Bathhouse Quest and #2 (双城厳一のお風呂探訪♨ and #2). The first extra already has <a href=\"bathhouse-quest.html\">a room</a>. This page exists so a search for the second part does not invent a plot. The joke sits next to a man who died on Datenseki.",
            "Volume extras also include Soya Sazanami’s Memories, Begone!. Official chapters stay on VIZ and MANGA Plus. Extras stay in the Jump Comics object. See <a href=\"../manga/omake.html\">omake</a>.",
        ]),
    ],
    [("bathhouse-quest.html", "Quest #1"), ("soya-memories.html", "Soya extra"), ("../manga/omake.html", "Omake"), ("../characters/sojo.html", "Sojo"), ("../world/bathhouse.html", "Bathhouse"), ("oneshots.html", "Oneshots")],
)

# --- factions ---
add(
    "factions/hishaku-jobs.html",
    "Hishaku Jobs | Who Does What in the Ten | Kagurabachi",
    "Mind, loud, trail, vessel, ice, nap, scar, opened contract. Two seats unlabeled. A job list, not a vibe.",
    "Faction · 役割",
    "Hishaku jobs",
    "毘灼の仕事",
    "Eight printed names. Two still blank. Flame tattoos. Shared fire-gate.",
    [
        ("The printed jobs", [
            "Yura: the mind, raid, sale, listing, Samura contract, body offer. Hiruhiko: Blood Crane, Play, hotel wrecker, Sanso hit. Toto: blood trail, fire-gate, Sengoku’s head. Hokuto: opened Ibuki’s contract, wants a real fight. Kuguri: Twilight Wave, unwilling classroom, unrequited blade. Yukisada: Vessel, seventeen, will not stay dead. Bingo: Mako, lion-dancer charms, then a nap. Uran: ice, the raid.",
            "Two of the ten are still unnamed. This desk will not invent them. The clan is not a vibe. See <a href=\"hishaku.html\">Hishaku</a> and <a href=\"../world/hishaku-unnamed.html\">unnamed</a>.",
        ]),
    ],
    [("hishaku.html", "Hishaku"), ("../world/hishaku-unnamed.html", "Unnamed"), ("../characters/yura.html", "Yura"), ("../analysis/two-unnamed.html", "Two unnamed"), ("../world/fire-gate.html", "Fire-gate"), ("index.html", "Factions")],
)

add(
    "factions/kamunabi-faces.html",
    "Kamunabi Faces | Seal, Leak, Pointed End | Kagurabachi",
    "Azami stayed. Kasen leaked. Hiyuki is the wish. Hagiwara is the first weather. Kudo is the HQ spend.",
    "Faction · 顔",
    "Kamunabi faces",
    "神奈備の顔",
    "The bureau is not one director.",
    [
        ("Several bureaus", [
            "The Kamunabi rebuilt from the Counter-Sorcery Army. They want blades under seal and bearers in Sanso. Hiyuki and Tafuku are the public act. The ACG squad is the first weather spend. Azami is capital spent against a leak. Kasen is the leak. Ichiki trained Shiba and Azami. Yatsuru holds barriers. Izaru is beads at the table. Kudo dies for Hakuri.",
            "Chihiro’s deal assumes the seal bureau. He gets both. See <a href=\"kamunabi.html\">Kamunabi</a>, <a href=\"leadership.html\">leadership</a>, and <a href=\"bureau.html\">the older bureau</a>.",
        ]),
    ],
    [("kamunabi.html", "Kamunabi"), ("leadership.html", "Leadership"), ("bureau.html", "Bureau"), ("../characters/kasen.html", "Kasen"), ("../characters/azami.html", "Azami"), ("../analysis/leak.html", "Leak")],
)

add(
    "factions/tou-jobs.html",
    "Tou Jobs | Household Military | Kagurabachi",
    "Soya heir, Tenri stone, Tamaki lie, Enji raise. The Sazanami military is four jobs and a leftover who leaves.",
    "Faction · 当",
    "Tou jobs",
    "当の仕事",
    "Hakuri was not in the hunting vocabulary. He becomes the building.",
    [
        ("Four plus the error", [
            "Soya: heir, Isou, amnesia, extra. Tenri: short blades, Datenseki pop. Tamaki: the lie about Soya. Enji: asked to die, told to raise. Hakuri: disowned, then Isou and Storehouse. Kyora: eleventh head, looks through Shinuchi, dies.",
            "See <a href=\"tou.html\">Tou</a>, <a href=\"sazanami.html\">Sazanami</a>, and <a href=\"../world/battle-hakuri-soya.html\">Hakuri vs Soya</a>.",
        ]),
    ],
    [("tou.html", "Tou"), ("sazanami.html", "Sazanami"), ("../characters/hakuri.html", "Hakuri"), ("../characters/soya.html", "Soya"), ("../characters/tenri.html", "Tenri"), ("../world/storehouse.html", "Storehouse")],
)


def main():
    n = 0
    for args in ROOMS:
        if page(*args):
            n += 1
    print("more wrote", n, "of", len(ROOMS))


if __name__ == "__main__":
    main()
