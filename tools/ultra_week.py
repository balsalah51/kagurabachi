#!/usr/bin/env python3
"""Live week: chapter 133 untitled on official listings, 134 door, English 10."""
from ultra_lib import page, write_long, crumb_for, related, VIZ


def chapter_133():
    body = f"""
  <p>Read it official: {VIZ}. Chapter 133 is live. VIZ’s chapter page is dated 4 October 2026. Weekly Shōnen Jump 2026 issue 45 went on sale 5 October 2026. This desk still does not print a weekly title. VIZ’s listing is “Kagurabachi, Chapter 133” with no subtitle. Wikipedia’s chapter list still ends at 132, “Misaka” (巳坂). We do not invent one from recap blogs.</p>
  <h2>What we print</h2>
  <p>The magazine happened. The Sunday window happened. The titled neighbor is <a href="chapter-132.html">Misaka</a>. The next magazine is <a href="chapter-134.html">chapter 134’s door</a>, Jump 2026 issue 46. House rooms already on the desk: <a href="../characters/ibuki.html">Ibuki Misaka</a>, <a href="../characters/natsuki.html">Natsuki Misaka</a>, <a href="../world/misaka-brothers.html">the brothers</a>, <a href="../world/kitakyushu.html">Kitakyushu</a>, <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
  <p>We do not recap the panels. A live untitled week is still a publication door. Fan titles stay off this page until VIZ, MANGA Plus, Jump official, or the Wikipedia chapter list prints one.</p>
  <h2>This week on the register</h2>
  <p>The first Enchanted Blade is still unnamed. Irishima 118–120 remain table-only. Enten is the seventh blade. Sojo is a Cloud Gouger customer, not Hishaku. Birthdays stay the five printed ones. Issue room: <a href="../fun/jump-2026-45.html">issue 45</a>. Month desk: <a href="../fun/october-2026.html">October 2026</a>.</p>
    {related([("chapter-132.html", "Ch. 132 Misaka"), ("chapter-134.html", "Ch. 134 door"), ("../fun/jump-2026-45.html", "Issue 45"), ("../fun/october-2026.html", "October"), ("../guide/current-week.html", "Current week"), ("../analysis/live-untitled.html", "Live untitled"), ("chapters.html", "Index"), ("publication.html", "Publication")])}
"""
    write_long(
        "manga/chapter-133.html",
        "Kagurabachi Chapter 133 | Live, Untitled Here",
        "Chapter 133 is live on VIZ (4 October 2026) and Jump 2026 #45. No official subtitle on this desk yet.",
        crumb_for("manga/chapter-133.html", "Chapter 133"),
        "Jump 45 · live untitled",
        "Chapter 133",
        "第133話",
        "The magazine is out. The weekly word is not printed on VIZ or Wikipedia yet.",
        body,
        overwrite=True,
    )


def chapter_134():
    body = f"""
  <p>Read it official when it lands: {VIZ}. Chapter 134 is due Weekly Shōnen Jump 2026 issue 46, on sale 12 October 2026 in Japan, with the usual Sunday VIZ / MANGA Plus window on 11 October 2026. This page is a publication door. We do not invent the title or the panels.</p>
  <p>Chapter 133 is <a href="chapter-133.html">live and untitled here</a>. Chapter 132 is <a href="chapter-132.html">Misaka</a>. Prior rest: <a href="../fun/september-2026-rest.html">September rest</a>. Issue room: <a href="../fun/jump-2026-46.html">issue 46</a>.</p>
    {related([("chapter-133.html", "Ch. 133 live"), ("chapter-132.html", "Misaka"), ("../fun/jump-2026-46.html", "Issue 46"), ("../fun/october-2026.html", "October 2026"), ("publication.html", "Publication"), ("index.html", "Manga guide"), ("chapters.html", "Chapters"), ("part-2.html", "Part 2")])}
"""
    write_long(
        "manga/chapter-134.html",
        "Kagurabachi Chapter 134 | Jump 2026 Issue 46",
        "Chapter 134’s magazine door: Weekly Shōnen Jump 2026 issue 46, on sale 12 October 2026. Title not printed on this desk.",
        crumb_for("manga/chapter-134.html", "Chapter 134’s door"),
        "Jump 46 · door",
        "Chapter 134’s door",
        "第134話",
        "A return date. Not a weekly title. We will not invent one.",
        body,
        overwrite=True,
    )


def rooms():
    page(
        "fun/jump-2026-45.html",
        "Jump 2026 Issue 45 | Chapter 133 Live",
        "Weekly Shōnen Jump 2026 #45 held chapter 133 on 5 October 2026. VIZ dated 4 October. Title not printed here.",
        "Fun · #45",
        "Jump 2026 issue 45",
        "2026年45号",
        "The magazine ran. The subtitle did not land on the listings we file.",
        [
            (
                "What the issue is",
                [
                    "Issue 44 held <a href=\"../manga/chapter-132.html\">Misaka</a> after the 42/43 health skip. Issue 45 is the next weekly object: chapter 133, on sale 5 October 2026. VIZ and MANGA Plus opened the usual Sunday window on 4 October. The chapter is live. VIZ’s page title is still only the number.",
                    "Wikipedia’s chapter list, checked 7 October 2026, still ends at 132. This desk waits. Prior issue: <a href=\"jump-2026-44.html\">issue 44</a>. Next door: <a href=\"jump-2026-46.html\">issue 46</a>. Month: <a href=\"october-2026.html\">October 2026</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133 live"),
            ("../manga/chapter-132.html", "Misaka"),
            ("jump-2026-44.html", "Issue 44"),
            ("jump-2026-46.html", "Issue 46"),
            ("october-2026.html", "October"),
            ("september-2026-rest.html", "September rest"),
        ],
        overwrite=True,
    )
    page(
        "fun/jump-2026-46.html",
        "Jump 2026 Issue 46 | Chapter 134’s Date",
        "Weekly Shōnen Jump 2026 #46, on sale 12 October 2026, is chapter 134’s magazine date. Title not printed here.",
        "Fun · #46",
        "Jump 2026 issue 46",
        "2026年46号",
        "12 October 2026. A date, not a title.",
        [
            (
                "The next magazine",
                [
                    "Issue 45 held chapter 133 without a subtitle this desk will file. Issue 46 is the next weekly door: chapter 134, on sale 12 October 2026. The usual Sunday window is 11 October. We do not invent the weekly title.",
                    "Prior live week: <a href=\"../manga/chapter-133.html\">chapter 133</a>. Prior titled word: <a href=\"../manga/chapter-132.html\">Misaka</a>. Month desk: <a href=\"october-2026.html\">October 2026</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-134.html", "Ch. 134 door"),
            ("../manga/chapter-133.html", "Ch. 133 live"),
            ("jump-2026-45.html", "Issue 45"),
            ("october-2026.html", "October"),
            ("hiatus.html", "Rests"),
            ("jump-issue-doors.html", "Issue doors"),
        ],
    )
    page(
        "fun/october-2026.html",
        "October 2026 | After Misaka | Kagurabachi",
        "October 2026 on the Kagurabachi desk: 132 is Misaka, 133 is live untitled, 134 is a date, English volume 10 is solicited.",
        "Fun · 10月",
        "October 2026",
        "2026年10月",
        "A titled house, a live number, a date, and an English spine still in the mail.",
        [
            (
                "What is already printed",
                [
                    "Chapter 132, <a href=\"../manga/chapter-132.html\">Misaka</a> (巳坂), landed in Jump 2026 #44. Chapter 133 is <a href=\"../manga/chapter-133.html\">live on VIZ</a> as of 4 October 2026 with no subtitle this desk will file. Volume 12 is on Japanese shelves as of 4 September 2026. The first Enchanted Blade is still unnamed here.",
                    "Chapter 134 is <a href=\"../manga/chapter-134.html\">a door</a> for Jump 2026 #46 (12 October). English volume 9 is listed for 3 November 2026. English volume 10 is listed for 2 February 2027 (ISBN 978-1-9747-6947-6). Cypic’s April 2027 series is unchanged. This month desk files those clocks.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133 live"),
            ("../manga/chapter-134.html", "Ch. 134 door"),
            ("../manga/chapter-132.html", "Misaka"),
            ("../collectibles/english-volume-10.html", "English 10"),
            ("../guide/current-week.html", "Current week"),
            ("year-2026.html", "2026"),
        ],
        overwrite=True,
    )
    page(
        "guide/current-week.html",
        "Current Week | Kagurabachi Desk",
        "As of 7 October 2026: 132 is Misaka, 133 is live untitled on VIZ, 134 is Jump 2026 #46.",
        "Guide · 今週",
        "Current week",
        "今週",
        "Misaka is printed. 133 is live. The next magazine is not.",
        [
            (
                "As of 7 October 2026",
                [
                    "Latest titled room: <a href=\"../manga/chapter-132.html\">chapter 132, Misaka</a> (巳坂), Jump 2026 #44, VIZ 27 September 2026. Latest live untitled: <a href=\"../manga/chapter-133.html\">chapter 133</a>, VIZ 4 October 2026, Jump 2026 #45. Next magazine: <a href=\"../manga/chapter-134.html\">chapter 134’s door</a>, Jump 2026 #46.",
                    "VIZ’s public list is showing 131–133 in the free window on this pass. That window moves. Read official. Do not use this page as a leak desk. Part 2 still runs from <a href=\"../manga/part-2.html\">Princess</a>. Volume 12 is a Japanese object. English volume 10 is a 2027 object.",
                ],
            )
        ],
        [
            ("../manga/chapter-132.html", "Misaka"),
            ("../manga/chapter-133.html", "133 live"),
            ("../manga/chapter-134.html", "134 door"),
            ("../manga/viz-free-now.html", "VIZ free window"),
            ("october-update.html", "October update"),
            ("reading-order.html", "How to read"),
        ],
        overwrite=True,
    )
    page(
        "collectibles/english-volume-10.html",
        "Kagurabachi English Volume 10 | VIZ 2 February 2027",
        "VIZ Media’s English volume 10 is listed for 2 February 2027, ISBN 978-1-9747-6947-6. A solicitation, not a Japanese spine.",
        "Collect · EN 10",
        "English volume 10",
        "英語版 第10巻",
        "2 February 2027. ISBN 978-1-9747-6947-6. The lag is the object.",
        [
            (
                "What the listing is",
                [
                    "Simon &amp; Schuster’s VIZ publisher page lists Kagurabachi, Vol. 10 for 2 February 2027. ISBN-13 978-1-9747-6947-6. Trade paperback, 208 pages, $11.99. That is the English object. Japanese volume 10, <em>The Swordsmen</em>, is already on shelves. Do not collapse the two.",
                    "English volume 8 is out. English volume 9 is listed for 3 November 2026. This page exists so a search for “volume 10 English” does not land only on the Japanese jacket. Jacket studies stay on <a href=\"../manga/covers.html\">covers</a>. The commute for the Japanese book is <a href=\"../manga/volume-10-read.html\">volume 10 read</a>.",
                ],
            )
        ],
        [
            ("english-volume-9.html", "English 9"),
            ("english-volume-8.html", "English 8"),
            ("../manga/volume-10.html", "JP volume 10"),
            ("../fun/english-volumes.html", "English trail"),
            ("../media/editions.html", "Editions"),
            ("index.html", "Collectibles"),
        ],
    )
    page(
        "manga/volume-13-door.html",
        "Kagurabachi Volume 13 Door | Next Japanese Spine",
        "The official comics page still lists Japanese volume 12 as latest. Volume 13 is a solicitation door until Shueisha prints the date here.",
        "Manga · 13",
        "Volume 13’s door",
        "第13巻",
        "Twelve spines are out. The thirteenth is not on the official comics page yet.",
        [
            (
                "What this desk will not invent",
                [
                    "comic.kagurabachi.jp/en/comics/ still names Jump Comics volume 12, 4 September 2026, as the latest Japanese book. This page is a door for the next spine. Blogs have repeated a January 2027 date from jacket talk. We wait for Shueisha or the official comics page.",
                    "Volume 12’s room: <a href=\"volume-12.html\">volume 12</a>. Uncollected after 12: <a href=\"uncollected-after-12.html\">the war book still weekly</a>. English lag sits on <a href=\"../collectibles/english-volume-10.html\">English 10</a>.",
                ],
            )
        ],
        [
            ("volume-12.html", "Volume 12"),
            ("uncollected-after-12.html", "Uncollected"),
            ("volumes.html", "Volume guide"),
            ("../collectibles/jump-comics.html", "Jump Comics"),
            ("publication.html", "Publication"),
            ("index.html", "Manga"),
        ],
    )
    page(
        "analysis/live-untitled.html",
        "Live Untitled Weeks | When the Magazine Beats the List",
        "Chapter 133 is readable on VIZ and the magazine while Wikipedia and VIZ still print no subtitle. A live week is not a title.",
        "Essay · 無題",
        "Live untitled",
        "出ている無題",
        "A chapter can be out and still untitled on this desk.",
        [
            (
                "The rule",
                [
                    "This archive files a weekly title when VIZ, MANGA Plus, Jump official, or the Wikipedia chapter list prints one. Chapter 132 waited until Wikipedia printed Misaka. Chapter 133 did not get that courtesy by 7 October 2026. The pages exist. The word does not.",
                    "Recap sites already sell a subtitle. That is not a source this desk accepts. The live door is <a href=\"../manga/chapter-133.html\">chapter 133</a>. The titled neighbor is <a href=\"../manga/chapter-132.html\">Misaka</a>. Official-only policy: <a href=\"../guide/official-only.html\">what we will not file</a>.",
                ],
            )
        ],
        [
            ("../manga/chapter-133.html", "Ch. 133"),
            ("misaka-title.html", "Misaka as a title"),
            ("rest-weeks.html", "Rest weeks"),
            ("../guide/official-only.html", "Official-only"),
            ("../guide/current-week.html", "Current week"),
            ("index.html", "Essays"),
        ],
    )
    page(
        "guide/ultra-doors.html",
        "Biggest Update Doors | October 2026 Wave",
        "The October 7 wave: live untitled 133, license rooms, award desks, leftover pairs, world-tour stops, English volume 10.",
        "Guide · 超",
        "Biggest update doors",
        "最大更新",
        "Printed leftover rooms, not stub spam.",
        [
            (
                "What this wave added",
                [
                    "Chapter 133 is now a live untitled door. Chapter 134 is the next date. Official publishers from comic.kagurabachi.jp each have a room. Awards that lived as a paragraph now have desks. Leftover printed pairs, world-tour stops, and the English volume 10 solicitation sit beside them.",
                    "Start at <a href=\"current-week.html\">current week</a> if you want the magazine. Start at <a href=\"../collectibles/licenses.html\">licenses</a> if you want the shelf abroad. Start at <a href=\"../fun/awards.html\">awards</a> if you want the plaques. Start at <a href=\"../characters/bonds.html\">bonds</a> if you want the leftover pairs.",
                ],
            )
        ],
        [
            ("current-week.html", "Current week"),
            ("october-update.html", "October update"),
            ("../collectibles/licenses.html", "Licenses"),
            ("../fun/awards.html", "Awards"),
            ("quad-doors.html", "Quad wave"),
            ("mega-doors.html", "Mega wave"),
        ],
    )


if __name__ == "__main__":
    chapter_133()
    chapter_134()
    rooms()
    print("ultra_week done")
