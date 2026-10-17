#!/usr/bin/env python3
"""Birthday, voice, and leftover world rooms."""
from oct_lib import page

# Five printed birthdays as their own rooms
page(
    "world/chihiro-birthday.html",
    "Chihiro’s Birthday | 11 August",
    "Chihiro Rokuhira’s printed birthday is 11 August. Present-tense age on this desk: 18. One of five dates Jump put on a profile.",
    "World · 8/11",
    "11 August",
    "8月11日",
    "The son’s date. Not a merch calendar.",
    [
        (
            "What is printed",
            [
                "The birthdays hub keeps five dates because five profiles carry them. Chihiro is 11 August, age 18 in the present-tense book. Kunishige dies in front of him at 37. The raid is not a birthday chapter.",
                "Hub: <a href=\"birthdays.html\">five dates</a>. Character: <a href=\"../characters/chihiro.html\">Chihiro</a>. Other August objects are not filed as his. Merch calendars stay on <a href=\"profiles.html\">profiles</a>.",
            ],
        )
    ],
    [
        ("birthdays.html", "Five dates"),
        ("../characters/chihiro.html", "Chihiro"),
        ("kunishige-birthday.html", "5 June"),
        ("profiles.html", "Profiles"),
        ("present.html", "Present tense"),
        ("index.html", "World"),
    ],
)

page(
    "world/kunishige-birthday.html",
    "Kunishige’s Birthday | 5 June",
    "Kunishige Rokuhira’s printed birthday is 5 June. He dies at 37. The next morning on the calendar is Sojo’s.",
    "World · 6/5",
    "5 June",
    "6月5日",
    "The smith’s date. Adjacent to his worst reader.",
    [
        (
            "What is printed",
            [
                "5 June is on Kunishige’s profile. Age at death: 37. Sojo’s printed date is 6 June. The pair room is <a href=\"../characters/sojo-and-kunishige.html\">Sojo and Kunishige</a>. The calendar essay is <a href=\"../analysis/adjacent-june.html\">adjacent June</a>.",
                "Hub: <a href=\"birthdays.html\">five dates</a>. Character: <a href=\"../characters/kunishige.html\">Kunishige</a>. We do not invent a cake chapter.",
            ],
        )
    ],
    [
        ("birthdays.html", "Five dates"),
        ("../characters/kunishige.html", "Kunishige"),
        ("sojo-birthday.html", "6 June"),
        ("../analysis/adjacent-june.html", "Adjacent June"),
        ("workshop.html", "Workshop"),
        ("index.html", "World"),
    ],
)

page(
    "world/sojo-birthday.html",
    "Sojo’s Birthday | 6 June",
    "Genichi Sojo’s printed birthday is 6 June. Present-tense age at death: 30. The day after the smith.",
    "World · 6/6",
    "6 June",
    "6月6日",
    "The customer’s date. Not a Hishaku tattoo.",
    [
        (
            "What is printed",
            [
                "6 June is on Sojo’s profile. He is 30 at death. He is a Cloud Gouger customer, not Hishaku. Kunishige’s date is 5 June. The fan never sat the smith. The calendar almost did.",
                "Hub: <a href=\"birthdays.html\">five dates</a>. Character: <a href=\"../characters/sojo.html\">Sojo</a>. Customer essay: <a href=\"../analysis/sojo-customer.html\">customer</a>.",
            ],
        )
    ],
    [
        ("birthdays.html", "Five dates"),
        ("../characters/sojo.html", "Sojo"),
        ("kunishige-birthday.html", "5 June"),
        ("../analysis/adjacent-june.html", "Adjacent June"),
        ("../blades/cloud-gouger.html", "Cloud Gouger"),
        ("index.html", "World"),
    ],
)

page(
    "world/shiba-birthday.html",
    "Shiba’s Birthday | 15 October",
    "Togo Shiba’s printed birthday is 15 October. Present-tense age: 39. In 2026 the date sat inside the 剣豪 fortnight.",
    "World · 10/15",
    "15 October",
    "10月15日",
    "The cafe uncle’s date. One of five.",
    [
        (
            "What is printed",
            [
                "15 October is on Shiba’s profile. Age 39 in the present-tense book. October 2026 also held Misaka Version II and Masters of the Sword. We do not invent a birthday chapter. The month essay is <a href=\"../analysis/shiba-october.html\">Shiba’s October</a>.",
                "Hub: <a href=\"birthdays.html\">five dates</a>. Character: <a href=\"../characters/shiba.html\">Shiba</a>. Voices: <a href=\"../media/two-shibas.html\">two Shibas</a>.",
            ],
        )
    ],
    [
        ("birthdays.html", "Five dates"),
        ("../characters/shiba.html", "Shiba"),
        ("../analysis/shiba-october.html", "Shiba’s October"),
        ("../fun/october-2026.html", "October 2026"),
        ("cafe.html", "Cafe"),
        ("index.html", "World"),
    ],
)

page(
    "world/char-birthday.html",
    "Char’s Birthday | 21 December",
    "Char Kyonagi’s printed birthday is 21 December, from the chapter 2 color page. Her age is not on this desk. Merch calendars that move the date to Hinao are marked wrong here.",
    "World · 12/21",
    "21 December",
    "12月21日",
    "A color-page date. Not a badge we have held.",
    [
        (
            "What is printed",
            [
                "Char’s 21 December comes from the chapter 2 color page, not a can badge. The profiles page already notes that at least one merch calendar puts 21 December on Hinao instead. This archive will not follow that swap.",
                "Hub: <a href=\"birthdays.html\">five dates</a>. Character: <a href=\"../characters/char.html\">Char</a>. Color pages: <a href=\"../manga/color-pages.html\">color pages</a>. Voice: <a href=\"../media/nemoto.html\">Nemoto</a>.",
            ],
        )
    ],
    [
        ("birthdays.html", "Five dates"),
        ("../characters/char.html", "Char"),
        ("../manga/color-pages.html", "Color pages"),
        ("profiles.html", "Profiles"),
        ("../factions/kyonagi.html", "Kyonagi"),
        ("index.html", "World"),
    ],
)

page(
    "world/sushi-subaru.html",
    "Sushi Subaru | Chef First, Smith Second",
    "Subaru Urita’s restaurant is Sushi Subaru. Wikipedia’s bearer file lists chef as primary occupation and passion. The Enchanted Blades are the other job.",
    "World · 鮨",
    "Sushi Subaru",
    "すしすば琉",
    "A restaurant. A hachimaki. Bentos for a hidden workshop.",
    [
        (
            "What the file prints",
            [
                "Subaru wears a hachimaki, a mustache, a scar over the right eye. Before the Seitei War he was one of Japan’s most prolific swordsmiths. His primary occupation and passion is sushi. Sand-Bone One-Sword Style. Duplication sorcery. Kunishige took a liking to him immediately.",
                "The workshop ate those plates. Meals in the title list are not a gag about this kitchen only, but this kitchen is why the gag lands. See <a href=\"../characters/subaru.html\">Subaru</a>, <a href=\"sand-bone.html\">Sand-Bone</a>, <a href=\"../analysis/meals.html\">meals</a>.",
            ],
        )
    ],
    [
        ("../characters/subaru.html", "Subaru"),
        ("sand-bone.html", "Sand-Bone"),
        ("food.html", "Food"),
        ("../characters/subaru-and-kunishige.html", "Mentor"),
        ("../characters/subaru-and-chihiro.html", "Bentos"),
        ("index.html", "World"),
    ],
)

page(
    "world/shokoku-datenseki.html",
    "Shokoku | The Island That Wielded Datenseki",
    "Wikipedia’s bearer file: Japan’s victory in the Seitei War was against the island nation skilled in wielding Datenseki, Shokoku. A place name, not a blade name.",
    "World · 諸国",
    "Shokoku",
    "諸国",
    "The other side of the war. Datenseki as their craft.",
    [
        (
            "Name versus nickname",
            [
                "Seitei is the war. Irishima is the talks table. Shokoku is the island nation the bearer file names as Datenseki-skilled. English tapes have said Japan’s Atlantis. That nickname is not this room. This room is the Wikipedia place-word.",
                "Datenseki: <a href=\"datenseki.html\">Datenseki</a>. War: <a href=\"../arcs/seitei-war.html\">Seitei War</a>. Island essay: <a href=\"seitei-island.html\">Seitei</a>. Mikaboshi: <a href=\"../factions/mikaboshi.html\">Mikaboshi</a>.",
            ],
        )
    ],
    [
        ("datenseki.html", "Datenseki"),
        ("seitei-island.html", "Seitei"),
        ("irishima.html", "Irishima"),
        ("../arcs/seitei-war.html", "Seitei War"),
        ("../factions/mikaboshi.html", "Mikaboshi"),
        ("index.html", "World"),
    ],
)

page(
    "fun/shiba-october.html",
    "Shiba’s October | Fun Desk",
    "15 October is Togo Shiba’s printed birthday. In 2026 it sat between Masters of the Sword and chapter 135’s door.",
    "Fun · 10/15",
    "Shiba’s October",
    "柴の十月",
    "A date on a profile. Not a Jump cover story.",
    [
        (
            "How to celebrate without inventing a chapter",
            [
                "Buy the book. Read the cafe pages. Konishi is the anime Shiba. Fukushima is the voiced-comic Shiba. The birthday is 15 October. The weekly title that week was already 剣豪.",
                "World room: <a href=\"../world/shiba-birthday.html\">15 October</a>. Essay: <a href=\"../analysis/shiba-october.html\">Shiba’s October</a>. Character: <a href=\"../characters/shiba.html\">Shiba</a>.",
            ],
        )
    ],
    [
        ("../world/shiba-birthday.html", "15 October"),
        ("../analysis/shiba-october.html", "Essay"),
        ("../characters/shiba.html", "Shiba"),
        ("october-2026.html", "October 2026"),
        ("../media/two-shibas.html", "Two Shibas"),
        ("index.html", "Fun"),
    ],
)

page(
    "media/fukushima.html",
    "Jun Fukushima | Voiced-Comic Shiba",
    "Jun Fukushima is Togo Shiba in the official voiced comic. Katsuyuki Konishi is Shiba in the Cypic series. Both credits are official.",
    "Media · 福島",
    "Jun Fukushima",
    "福島潤",
    "A promo Shiba. Not the April 2027 Shiba.",
    [
        (
            "Two Shibas",
            [
                "The voiced comic assigns Jun Fukushima to Shiba. The television series assigns Katsuyuki Konishi. This page is the comic credit so a search does not land only on Konishi. Split: <a href=\"two-shibas.html\">two Shibas</a>. Character: <a href=\"../characters/shiba.html\">Shiba</a>.",
                "Ishige is comic Chihiro. Fujimaki is comic Kunishige. Tadano is comic Hinao. Staff: <a href=\"staff.html\">staff</a>.",
            ],
        )
    ],
    [
        ("two-shibas.html", "Two Shibas"),
        ("konishi.html", "Konishi"),
        ("voiced-comic.html", "Voiced comic"),
        ("staff.html", "Staff"),
        ("../characters/shiba.html", "Shiba"),
        ("index.html", "Media"),
    ],
)

page(
    "media/two-chihiros.html",
    "Two Chihiros | Ishige and Kimura",
    "Shoya Ishige reads Chihiro in the voiced comic. Taihi Kimura reads Chihiro for Cypic. Same boy. Two official voices.",
    "Media · 二千",
    "Two Chihiros",
    "二人のチヒロ",
    "A Jump promo. An April 2027 series.",
    [
        (
            "Do not collapse the credits",
            [
                "Search will mash them. This room keeps both. Ishige: <a href=\"ishige.html\">Ishige</a>. Kimura: <a href=\"kimura.html\">Kimura</a>. The teaser still sells Aka, Kuro, and Nishiki behind Enten. Cour length is unprinted.",
                "Cast essay: <a href=\"../analysis/two-casts.html\">two official casts</a>. Character: <a href=\"../characters/chihiro.html\">Chihiro</a>.",
            ],
        )
    ],
    [
        ("ishige.html", "Ishige"),
        ("kimura.html", "Kimura"),
        ("../analysis/two-casts.html", "Two casts"),
        ("voiced-comic.html", "Voiced comic"),
        ("anime.html", "Anime"),
        ("index.html", "Media"),
    ],
)

page(
    "media/two-kunishiges.html",
    "Two Kunishiges | Fujimaki and Seki",
    "Kenta Fujimaki reads Kunishige in the voiced comic. Tomokazu Seki reads Kunishige for Cypic. Same smith. Two official voices.",
    "Media · 二匠",
    "Two Kunishiges",
    "二人の国重",
    "A promo smith. A television smith.",
    [
        (
            "Do not collapse the credits",
            [
                "Fujimaki: <a href=\"fujimaki.html\">Fujimaki</a>. Seki: <a href=\"seki.html\">Seki</a>. The man both of them read dies on page one and returns as labor in Part 2. Neither credit is a chapter host.",
                "Cast essay: <a href=\"../analysis/two-casts.html\">two official casts</a>. Character: <a href=\"../characters/kunishige.html\">Kunishige</a>.",
            ],
        )
    ],
    [
        ("fujimaki.html", "Fujimaki"),
        ("seki.html", "Seki"),
        ("../analysis/two-casts.html", "Two casts"),
        ("voiced-comic.html", "Voiced comic"),
        ("anime.html", "Anime"),
        ("index.html", "Media"),
    ],
)

page(
    "media/two-shibas.html",
    "Two Shibas | Fukushima and Konishi",
    "Jun Fukushima reads Shiba in the voiced comic. Katsuyuki Konishi reads Shiba for Cypic. Same uncle. Two official voices.",
    "Media · 二柴",
    "Two Shibas",
    "二人の柴",
    "A promo teleport. A television teleport.",
    [
        (
            "Do not collapse the credits",
            [
                "Fukushima: <a href=\"fukushima.html\">Fukushima</a>. Konishi: <a href=\"konishi.html\">Konishi</a>. 15 October is the printed birthday, not a voice date. Cafe: <a href=\"../world/cafe.html\">the cafe</a>.",
                "Cast essay: <a href=\"../analysis/two-casts.html\">two official casts</a>. Character: <a href=\"../characters/shiba.html\">Shiba</a>.",
            ],
        )
    ],
    [
        ("fukushima.html", "Fukushima"),
        ("konishi.html", "Konishi"),
        ("../analysis/two-casts.html", "Two casts"),
        ("../world/shiba-birthday.html", "15 October"),
        ("voiced-comic.html", "Voiced comic"),
        ("index.html", "Media"),
    ],
)

page(
    "media/two-hinaos.html",
    "Two Hinaos | Tadano and Itō",
    "Akari Tadano reads Hinao in the voiced comic. Miku Itō reads Hinao for Cypic. Same counter. Two official voices.",
    "Media · 二雛",
    "Two Hinaos",
    "二人の雛緒",
    "A promo cafe. A television cafe.",
    [
        (
            "Do not collapse the credits",
            [
                "Tadano: <a href=\"tadano.html\">Tadano</a>. Itō: <a href=\"ito-miku.html\">Itō</a>. Merch calendars that steal Char’s 21 December for Hinao are wrong on this desk. Char’s voice is Nemoto, with no voiced-comic twin filed here.",
                "Cast essay: <a href=\"../analysis/two-casts.html\">two official casts</a>. Character: <a href=\"../characters/hinao.html\">Hinao</a>.",
            ],
        )
    ],
    [
        ("tadano.html", "Tadano"),
        ("ito-miku.html", "Itō"),
        ("nemoto.html", "Nemoto"),
        ("../analysis/two-casts.html", "Two casts"),
        ("../world/cafe.html", "Cafe"),
        ("index.html", "Media"),
    ],
)

print("mid_rooms done")
