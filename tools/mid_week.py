#!/usr/bin/env python3
"""17 Oct 2026 week: file Wikipedia titles for 133 and 134; 135 stays a door."""
from oct_lib import page, write_long, crumb_for, related, VIZ


def chapter_133():
    body = f"""
  <p>Read it official: {VIZ}. Chapter 133 is titled “Misaka Version II” (巳坂二号). VIZ’s listing is 4 October 2026. Weekly Shōnen Jump 2026 issue 45, on sale 5 October 2026. This page files the printed weekly word from the Wikipedia chapter list. It is not a substitute and not a leak desk.</p>
  <h2>What we print</h2>
  <p>The Wikipedia chapter list now prints the English title Misaka Version II and the Japanese 巳坂二号. Chapter 132 is <a href="chapter-132.html">Misaka</a> (巳坂). The 二号 is a numbering, like Irishima’s 弐, not a new house. Neighbor titles: then <a href="chapter-134.html">Masters of the Sword</a>. House rooms: <a href="../characters/ibuki.html">Ibuki</a>, <a href="../characters/natsuki.html">Natsuki</a>, <a href="../world/misaka-brothers.html">the brothers</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
  <p>We do not recap the panels here. Official reading stays on VIZ and MANGA Plus. A title that is a house plus a number sits on <a href="../analysis/version-two.html">Version II as a title</a>. Two Misaka weeks sit on <a href="../analysis/two-misaka-weeks.html">two Misaka weeks</a>.</p>
  <h2>This week on the register</h2>
  <p>The first Enchanted Blade is still unnamed. Irishima 118–120 remain table-only. Enten is the seventh blade. Sojo is a Cloud Gouger customer, not Hishaku. Chapter 135 is <a href="chapter-135.html">a date</a>.</p>
    {related([("chapter-132.html", "Ch. 132 Misaka"), ("chapter-134.html", "Ch. 134"), ("chapter-135.html", "Ch. 135 door"), ("../analysis/version-two.html", "Version II"), ("../fun/jump-2026-45.html", "Issue 45"), ("../world/misaka-brothers.html", "Brothers"), ("chapters.html", "Index"), ("publication.html", "Publication")])}
"""
    write_long(
        "manga/chapter-133.html",
        "Kagurabachi Chapter 133 “Misaka Version II”",
        "Kagurabachi chapter 133, Misaka Version II (巳坂二号): Jump 2026 issue 45, VIZ 4 October 2026. Official reading on VIZ and MANGA Plus.",
        crumb_for("manga/chapter-133.html", "Chapter 133"),
        "the uncollected run · Seitei War / Part 2",
        "Chapter 133 - “Misaka Version II”",
        "巳坂二号",
        "Jump 2026 #45. VIZ dated 4 October 2026. The weekly word is the house, numbered.",
        body,
        overwrite=True,
    )


def chapter_134():
    body = f"""
  <p>Read it official: {VIZ}. Chapter 134 is titled “Masters of the Sword” (剣豪). VIZ’s listing is 11 October 2026. Weekly Shōnen Jump 2026 issue 46, on sale 12 October 2026. This page files the printed weekly word from the Wikipedia chapter list. It is not a substitute and not a leak desk.</p>
  <h2>What we print</h2>
  <p>The Wikipedia chapter list now prints the English title Masters of the Sword and the Japanese 剣豪. That is not Volume 10’s jacket word 剣士たち, and it is not the quoted press name 剣聖. Collision rooms: <a href="../analysis/kengo-versus-kenshi.html">剣豪 versus 剣士たち</a>, <a href="../analysis/kengo-versus-kensei.html">剣豪 versus 剣聖</a>.</p>
  <p>Neighbor titles: <a href="chapter-133.html">Misaka Version II</a>, then <a href="chapter-135.html">chapter 135’s door</a>. We do not recap the panels. Official reading stays on VIZ and MANGA Plus.</p>
  <h2>This week on the register</h2>
  <p>The first Enchanted Blade is still unnamed. Irishima 118–120 remain table-only. Enten is the seventh. Issue room: <a href="../fun/jump-2026-46.html">issue 46</a>. Month: <a href="../fun/october-2026.html">October 2026</a>.</p>
    {related([("chapter-133.html", "Ch. 133"), ("chapter-135.html", "Ch. 135 door"), ("../analysis/kengo-versus-kenshi.html", "剣豪 vs 剣士"), ("../fun/jump-2026-46.html", "Issue 46"), ("../analysis/sword-master-press.html", "Sword Master"), ("../manga/volume-10.html", "Vol. 10"), ("chapters.html", "Index"), ("publication.html", "Publication")])}
"""
    write_long(
        "manga/chapter-134.html",
        "Kagurabachi Chapter 134 “Masters of the Sword”",
        "Kagurabachi chapter 134, Masters of the Sword (剣豪): Jump 2026 issue 46, VIZ 11 October 2026. Official reading on VIZ and MANGA Plus.",
        crumb_for("manga/chapter-134.html", "Chapter 134"),
        "the uncollected run · Seitei War / Part 2",
        "Chapter 134 - “Masters of the Sword”",
        "剣豪",
        "Jump 2026 #46. VIZ dated 11 October 2026. The weekly word is a swordsman rank, not a jacket.",
        body,
        overwrite=True,
    )


def chapter_135():
    body = f"""
  <p>Read it official when it lands: {VIZ}. Chapter 135 is due Weekly Shōnen Jump 2026 issue 47, on sale 19 October 2026 in Japan, with the usual Sunday VIZ / MANGA Plus window on 18 October 2026. VIZ’s series page, checked 17 October, still said a new chapter was coming in one day. This page is a publication door. We do not invent the title or the panels.</p>
  <p>Chapter 134 is <a href="chapter-134.html">Masters of the Sword</a> (剣豪). Chapter 133 is <a href="chapter-133.html">Misaka Version II</a> (巳坂二号). Issue room: <a href="../fun/jump-2026-47.html">issue 47</a>.</p>
    {related([("chapter-134.html", "Ch. 134"), ("chapter-133.html", "Ch. 133"), ("../fun/jump-2026-47.html", "Issue 47"), ("../fun/october-2026.html", "October 2026"), ("publication.html", "Publication"), ("index.html", "Manga guide"), ("chapters.html", "Chapters"), ("part-2.html", "Part 2")])}
"""
    write_long(
        "manga/chapter-135.html",
        "Kagurabachi Chapter 135 | Jump 2026 Issue 47",
        "Chapter 135’s magazine door: Weekly Shōnen Jump 2026 issue 47, on sale 19 October 2026. Title not printed on this desk.",
        crumb_for("manga/chapter-135.html", "Chapter 135’s door"),
        "Jump 47 · door",
        "Chapter 135’s door",
        "第135話",
        "A return date. Not a weekly title. We will not invent one.",
        body,
        overwrite=True,
    )


def rooms():
    page(
        "fun/jump-2026-45.html",
        "Jump 2026 Issue 45 | Misaka Version II",
        "Weekly Shōnen Jump 2026 #45 held chapter 133, Misaka Version II (巳坂二号), on 5 October 2026.",
        "Fun · #45",
        "Jump 2026 issue 45",
        "2026年45号",
        "The magazine ran the numbered house.",
        [
            (
                "What the issue held",
                [
                    "Issue 44 held <a href=\"../manga/chapter-132.html\">Misaka</a>. Issue 45 held <a href=\"../manga/chapter-133.html\">Misaka Version II</a>. VIZ dated 4 October 2026. Wikipedia’s chapter list now prints 巳坂二号. We still do not recap the panels.",
                    "Next titled week: <a href=\"jump-2026-46.html\">issue 46</a>, Masters of the Sword. Month: <a href=\"october-2026.html\">October 2026</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133"),
            ("../manga/chapter-132.html", "Misaka"),
            ("jump-2026-44.html", "Issue 44"),
            ("jump-2026-46.html", "Issue 46"),
            ("october-2026.html", "October"),
            ("../analysis/version-two.html", "Version II"),
        ],
        overwrite=True,
    )
    page(
        "fun/jump-2026-46.html",
        "Jump 2026 Issue 46 | Masters of the Sword",
        "Weekly Shōnen Jump 2026 #46 held chapter 134, Masters of the Sword (剣豪), on 12 October 2026.",
        "Fun · #46",
        "Jump 2026 issue 46",
        "2026年46号",
        "The magazine ran 剣豪. Not 剣士たち. Not 剣聖.",
        [
            (
                "What the issue held",
                [
                    "Issue 45 held Misaka Version II. Issue 46 held <a href=\"../manga/chapter-134.html\">Masters of the Sword</a>. VIZ dated 11 October 2026. Wikipedia’s chapter list now prints 剣豪.",
                    "Next magazine: <a href=\"jump-2026-47.html\">issue 47</a>, chapter 135’s date. Collision essay: <a href=\"../analysis/kengo-versus-kenshi.html\">剣豪 versus 剣士たち</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-134.html", "Ch. 134"),
            ("../manga/chapter-133.html", "Ch. 133"),
            ("jump-2026-45.html", "Issue 45"),
            ("jump-2026-47.html", "Issue 47"),
            ("october-2026.html", "October"),
            ("../analysis/kengo-versus-kensei.html", "剣豪 vs 剣聖"),
        ],
        overwrite=True,
    )
    page(
        "fun/jump-2026-47.html",
        "Jump 2026 Issue 47 | Chapter 135’s Date",
        "Weekly Shōnen Jump 2026 #47, on sale 19 October 2026, is chapter 135’s magazine date. Title not printed here.",
        "Fun · #47",
        "Jump 2026 issue 47",
        "2026年47号",
        "19 October 2026. A date, not a title.",
        [
            (
                "The next magazine",
                [
                    "Issue 46 held Masters of the Sword. Issue 47 is the next weekly door: chapter 135, on sale 19 October 2026. The usual Sunday window is 18 October. VIZ’s series page, checked 17 October, still counted one day. We do not invent the weekly title.",
                    "Prior titled word: <a href=\"../manga/chapter-134.html\">Masters of the Sword</a>. Month: <a href=\"october-2026.html\">October 2026</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-135.html", "Ch. 135 door"),
            ("../manga/chapter-134.html", "Ch. 134"),
            ("jump-2026-46.html", "Issue 46"),
            ("october-2026.html", "October"),
            ("hiatus.html", "Rests"),
            ("jump-issue-doors.html", "Issue doors"),
        ],
    )
    page(
        "fun/october-2026.html",
        "October 2026 | Two Misaka Weeks, Then 剣豪",
        "October 2026 on the Kagurabachi desk: 132 Misaka, 133 Misaka Version II, 134 Masters of the Sword, 135 a date.",
        "Fun · 10月",
        "October 2026",
        "2026年10月",
        "A house, a numbered house, a swordsman rank, then a date.",
        [
            (
                "What is already printed",
                [
                    "Chapter 132, <a href=\"../manga/chapter-132.html\">Misaka</a>. Chapter 133, <a href=\"../manga/chapter-133.html\">Misaka Version II</a>. Chapter 134, <a href=\"../manga/chapter-134.html\">Masters of the Sword</a>. Volume 12 is on Japanese shelves. English volume 9 is still 3 November. English volume 10 is still 2 February 2027.",
                    "Chapter 135 is <a href=\"../manga/chapter-135.html\">a door</a> for Jump 2026 #47. Shiba’s printed birthday, 15 October, sat inside this month: <a href=\"shiba-october.html\">Shiba’s October</a>. The first Enchanted Blade is still unnamed here.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133"),
            ("../manga/chapter-134.html", "Ch. 134"),
            ("../manga/chapter-135.html", "Ch. 135 door"),
            ("shiba-october.html", "Shiba’s October"),
            ("../guide/current-week.html", "Current week"),
            ("year-2026.html", "2026"),
        ],
        overwrite=True,
    )
    page(
        "guide/current-week.html",
        "Current Week | Kagurabachi Desk",
        "As of 17 October 2026: 133 is Misaka Version II, 134 is Masters of the Sword, 135 is Jump 2026 #47.",
        "Guide · 今週",
        "Current week",
        "今週",
        "Two titled Misaka weeks. Then 剣豪. Then a date.",
        [
            (
                "As of 17 October 2026",
                [
                    "Latest titled rooms: <a href=\"../manga/chapter-134.html\">chapter 134, Masters of the Sword</a> (剣豪), Jump 2026 #46, VIZ 11 October 2026, and <a href=\"../manga/chapter-133.html\">chapter 133, Misaka Version II</a> (巳坂二号). Next magazine: <a href=\"../manga/chapter-135.html\">chapter 135’s door</a>, Jump 2026 #47.",
                    "VIZ’s public list is showing 132–134 in the free window on this pass. That window moves. Wikipedia caught up on both weekly words after the 7 October live-untitled filing. Read official. Do not use this page as a leak desk.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "133"),
            ("../manga/chapter-134.html", "134"),
            ("../manga/chapter-135.html", "135 door"),
            ("../manga/viz-free-now.html", "VIZ free window"),
            ("mid-october-update.html", "Mid-October update"),
            ("reading-order.html", "How to read"),
        ],
        overwrite=True,
    )
    page(
        "guide/mid-october-update.html",
        "Mid-October 2026 Update | Kagurabachi Archive",
        "What this archive refreshed on 17 October 2026: Misaka Version II, Masters of the Sword, a 135 door, leftover pairs, birthday rooms, two-cast voice desks.",
        "Guide · 中旬",
        "Mid-October update",
        "十月中旬",
        "Wikipedia printed two weekly words. The desk grew around them.",
        [
            (
                "What this wave added",
                [
                    "Chapter 133 is no longer live-untitled. Chapter 134 is no longer a date. Chapter 135 is the new door. Leftover printed pairs, the five birthday rooms, sushi Subaru, two official casts, and title-collision essays sit beside them.",
                    "Start at <a href=\"current-week.html\">current week</a> if you want the magazine. Start at <a href=\"../characters/bonds.html\">bonds</a> if you want the leftover pairs. Start at <a href=\"../world/birthdays.html\">birthdays</a> if you want the five dates.",
                ],
            )
        ],
        [
            ("current-week.html", "Current week"),
            ("ultra-doors.html", "October 7 wave"),
            ("october-update.html", "October 3 update"),
            ("../analysis/version-two.html", "Version II"),
            ("../analysis/kengo-versus-kenshi.html", "剣豪"),
            ("index.html", "Guide"),
        ],
    )
    page(
        "manga/titles-after-misaka.html",
        "Titles After Misaka | Version II, Then 剣豪",
        "After chapter 132’s house name: 133 is Misaka Version II, 134 is Masters of the Sword, 135 is a date.",
        "Manga · 題",
        "After Misaka",
        "巳坂のあと",
        "A numbered house, then a rank, then silence we will not fill.",
        [
            (
                "The spoken list",
                [
                    "Mission through Masters of the Sword is the titled run. <a href=\"../analysis/titles-through-134.html\">Titles through 134</a> is the catalog. Chapter 135 stays a door. Recap blogs are not the Wikipedia chapter list.",
                    "Version II essay: <a href=\"../analysis/version-two.html\">二号</a>. 剣豪 collisions: <a href=\"../analysis/kengo-versus-kenshi.html\">versus 剣士たち</a>.",
                ],
            )
        ],
        [
            ("chapter-132.html", "Misaka"),
            ("chapter-133.html", "Version II"),
            ("chapter-134.html", "剣豪"),
            ("chapter-135.html", "135 door"),
            ("../analysis/titles-through-134.html", "Through 134"),
            ("chapters.html", "Index"),
        ],
        overwrite=True,
    )
    page(
        "guide/spoiler-133.html",
        "Chapter 133 Spoilers | Title Only",
        "Chapter 133 is titled Misaka Version II. This archive still does not recap the panels. Official reading is VIZ and MANGA Plus.",
        "Guide · ネタバレ",
        "133 without a recap",
        "133の無ネタバレ",
        "A titled week. A closed mouth on the panels.",
        [
            (
                "What changed on 17 October",
                [
                    "Wikipedia printed the weekly word. The live-untitled rule lifted for the title only. We still do not recap the issue. If you want the chapter, read it official. Policy: <a href=\"official-only.html\">official-only</a>.",
                    "Same rule on <a href=\"../manga/chapter-134.html\">chapter 134</a>. Next door: <a href=\"../manga/chapter-135.html\">135</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133"),
            ("official-only.html", "Official-only"),
            ("spoiler-ladder.html", "Spoiler ladder"),
            ("current-week.html", "Current week"),
            ("../analysis/version-two.html", "Version II"),
            ("index.html", "Guide"),
        ],
        overwrite=True,
    )


if __name__ == "__main__":
    chapter_133()
    chapter_134()
    chapter_135()
    rooms()
    print("mid_week done")
