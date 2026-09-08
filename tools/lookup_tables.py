#!/usr/bin/env python3
"""Timeline, merch profiles, fight log, technique index, volume diffs."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <script>!function(){try{var m=document.cookie.match(/(?:^|; )kb-theme=(dark|light)/);if(m)document.documentElement.setAttribute("data-theme",m[1])}catch(e){}}()</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Kagurabachi Archive</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+JP:wght@400;500;600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/site.css">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
"""

FOOT = """
  </main>
  <div id="site-footer"></div>
  <script src="../js/site.js"></script>
</body>
</html>
"""


def write(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    html = (
        HEAD.format(title=title, desc=desc)
        + f'<p class="crumb">{crumb}</p>\n'
        + f'<header class="page-hero"><div>\n  <p class="kicker">{kicker}</p>\n'
        + f'  <h1>{h1}<span class="jp">{jp}</span></h1>\n'
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + f'<article class="article">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


write(
    "world/timeline.html",
    "Kagurabachi Timeline",
    "Dated Kagurabachi timeline of the present-tense year and the printed Part 2 clocks, without inventing a Wednesday the book did not give.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Timeline',
    "Lookup",
    "Timeline",
    "年表",
    "A dated table of the present-tense year, then the Part 2 clocks the magazine actually printed. The long eras stay on the world page.",
    """
  <p>The <a href="index.html">world page</a> is eras: Mikaboshi exile, Shokoku rising, the war, Enten, the Hishaku, the raid. <a href="present.html">Present tense</a> is the essay that says October and November are weeks, not decades. This page is the lookup: a row you can scan. If a date is a month, we print a month. If Part 2 printed March 29 and April 1, those rows exist. We do not invent a Wednesday the book has not given. Official chapters: VIZ / MANGA Plus.</p>

  <h2>Present-tense year (Chihiro is 18)</h2>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>When</th><th>What</th><th>Where to read</th></tr></thead>
    <tbody>
      <tr><td>18 years before present</td><td>Seitei War ends. Malediction after the treaty. About 200,000 civilians. Kunishige confiscates six blades.</td><td><a href="../arcs/seitei-war.html">Seitei War</a></td></tr>
      <tr><td>~15 years after the war</td><td>Kunishige and Chihiro forge Enten. Seventh blade, never registered.</td><td><a href="../blades/enten.html">Enten</a></td></tr>
      <tr><td>4 years before present</td><td>Hishaku form. Flame tattoos. Fire-gate. One plan for Shinuchi.</td><td><a href="../factions/hishaku.html">Hishaku</a></td></tr>
      <tr><td>3 years before present</td><td>Raid on the Rokuhira workshop. Kunishige dies at 37. Six wartime blades stolen. Enten stays. Ibuki murdered in the same campaign.</td><td><a href="raid.html">The raid</a> · <a href="../manga/chapter-1.html">Ch. 1</a></td></tr>
      <tr><td>Those three years</td><td>Chihiro and Shiba work the Tokyo underworld. Cafe Haru Haru between jobs. Sanso boxes go up after Ibuki.</td><td><a href="underworld.html">Underworld</a> · <a href="sanso.html">Sanso</a></td></tr>
      <tr><td>Early October, present</td><td>Yura sells Cloud Gouger to Sojo. Chapter 1 is an October night in Tokyo.</td><td><a href="present.html">Present tense</a> · <a href="../manga/chapter-1.html">Ch. 1</a></td></tr>
      <tr><td>October, present</td><td>Char, Madoka, Kaburato, True Realm (ch. 14), Enten bisects Cloud Gouger (ch. 18). ACG: four graves.</td><td><a href="../arcs/vs-sojo.html">Vs. Sojo</a> · <a href="../manga/chapter-18.html">Ch. 18</a></td></tr>
      <tr><td>November, present</td><td>208th Rakuzaichi. Hakuri wakes Isou and Storehouse. Kyora dies on Shinuchi. Prisoners leave. Chihiro hands Magatsumi to the Kamunabi and keeps Enten by joining them.</td><td><a href="../arcs/rakuzaichi.html">Rakuzaichi</a> · <a href="../manga/chapter-44.html">Ch. 44</a></td></tr>
      <tr><td>Same season, after the auction</td><td>Sword Bearer Assassination. Train, Senkutsuji, Kyoto hotel, HQ. No winter skip on the page. People have not grown new faces.</td><td><a href="../arcs/sword-bearer.html">Sword Bearer</a> · <a href="../manga/chapter-47.html">Ch. 47</a></td></tr>
      <tr><td>Still that present</td><td>Part 1 closes at ch. 115, “Swordsmith.” Enten in pieces. Iori holds Tobimune. Akemura loose in the Kamunabi.</td><td><a href="../manga/chapter-115.html">Ch. 115</a></td></tr>
    </tbody>
  </table></div>
  <p>Fandom and Wikipedia sometimes pin the Kyoto hotel to a mid-November day. This table keeps November as the month the auction is dated and the hotel as the same political season. A day-number belongs here when the magazine prints one.</p>

  <h2>Part 2 clocks (war book, printed)</h2>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>When</th><th>What</th><th>Where to read</th></tr></thead>
    <tbody>
      <tr><td>22 years before present (era)</td><td>Shokoku appears. Irishima’s vein is already showing. The Bureau becomes an army.</td><td><a href="index.html">World</a></td></tr>
      <tr><td>War year, talks</td><td>Ch. 116–121: Princess, Irishima Talks through END. Ariu at the table. Hiroto and Yoshinojo still alive.</td><td><a href="../manga/chapter-116.html">Ch. 116</a> · <a href="../manga/chapter-117.html">Talks</a></td></tr>
      <tr><td>War year, after END</td><td>Ch. 122 Start. Ch. 123 Chiaki. Ch. 124 Powerless. The walk to the kiln.</td><td><a href="../manga/chapter-122.html">Ch. 122</a></td></tr>
      <tr><td>War year, kiln</td><td>Ch. 125–128 smelting and fire. First blade still unnamed.</td><td><a href="../manga/chapter-125.html">Ch. 125</a></td></tr>
      <tr><td>March 29, shop clock</td><td>Ch. 129–130. By 18:30 after sixty-one hours of blast, tamahagane comes up from a collapsed furnace.</td><td><a href="../manga/chapter-129.html">Ch. 129</a> · <a href="../manga/chapter-130.html">Ch. 130</a></td></tr>
      <tr><td>April 1, noon</td><td><span class="spoiler">Letter sets Irishima’s beach for the Chiaki handover. Three days from the March 29 clock.</span></td><td><a href="../manga/chapter-130.html">Ch. 130</a></td></tr>
    </tbody>
  </table></div>
  <p>Chapter 131 is due 6 September 2026 in the magazine. This table moves when it prints. Birthdays are a different calendar: <a href="birthdays.html">printed dates</a> and <a href="profiles.html">profiles</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="present.html">Present tense</a><a href="index.html">World</a><a href="birthdays.html">Birthdays</a><a href="profiles.html">Profiles</a><a href="../manga/chapters.html">Chapters</a><a href="raid.html">The raid</a></nav>
""",
)

write(
    "world/profiles.html",
    "Kagurabachi Profiles",
    "Lookup of printed Kagurabachi profile facts: ages, birthdays, voices, first appearances. Merch-cited dates stay marked until this archive has seen the badge.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Profiles',
    "Extras and merch",
    "Profiles",
    "プロフィール",
    "A data sheet, not an essay. Printed Jump facts first. Can-badge dates only as citations until we have held the badge.",
    """
  <p>Fandom infoboxes and Japanese birthday calendars harvest volume extras and official birthday can badges. This archive will not copy a third-hand calendar as if we saw the tin. The <a href="birthdays.html">birthdays page</a> keeps five dates Jump printed on profiles. This page is the lookup around those facts: age, first appearance, voice, affiliation. Official chapters: VIZ / MANGA Plus.</p>

  <h2>Printed on this site</h2>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>Name</th><th>Age</th><th>Birthday</th><th>First room</th><th>Voice (printed here)</th></tr></thead>
    <tbody>
      <tr><td><a href="../characters/chihiro.html">Chihiro Rokuhira</a></td><td>18 (15 at the raid)</td><td>11 August</td><td><a href="../manga/chapter-1.html">Ch. 1</a></td><td>Taihi Kimura (anime) / Shoya Ishige (voiced comic)</td></tr>
      <tr><td><a href="../characters/kunishige.html">Kunishige Rokuhira</a></td><td>37 at death</td><td>5 June</td><td><a href="../manga/chapter-1.html">Ch. 1</a></td><td>Tomokazu Seki (anime) / Kenta Fujimaki (voiced comic)</td></tr>
      <tr><td><a href="../characters/shiba.html">Togo Shiba</a></td><td>39</td><td>15 October</td><td><a href="../manga/chapter-1.html">Ch. 1</a></td><td>Katsuyuki Konishi (anime) / Jun Fukushima (voiced comic)</td></tr>
      <tr><td><a href="../characters/sojo.html">Genichi Sojo</a></td><td>30 at death</td><td>6 June</td><td>Vs. Sojo stretch</td><td>—</td></tr>
      <tr><td><a href="../characters/char.html">Char Kyonagi</a></td><td>not printed here</td><td>21 December (ch. 2 color page)</td><td>Ch. 2</td><td>—</td></tr>
      <tr><td><a href="../characters/hakuri.html">Hakuri Sazanami</a></td><td>17</td><td>see merch note</td><td>Ch. 19</td><td>—</td></tr>
      <tr><td><a href="../characters/hinao.html">Hinao</a></td><td>—</td><td>—</td><td>Cafe stretch</td><td>Akari Tadano (voiced comic)</td></tr>
      <tr><td><a href="../characters/iori.html">Iori Samura</a></td><td>—</td><td>—</td><td><a href="../manga/chapter-62.html">Ch. 62</a></td><td>—</td></tr>
      <tr><td><a href="../characters/hiyuki.html">Hiyuki Kagari</a></td><td>—</td><td>see merch note</td><td>Ch. 19–20 stretch</td><td>—</td></tr>
    </tbody>
  </table></div>
  <p>Full voice list: <a href="../fun/voices.html">voices</a>. Name-by-name one-liners: <a href="register.html">register</a>. Heights, weights, and blood types are still unpublished even on the Fandom infoboxes.</p>

  <h2>Hakuri’s date, the first merch check</h2>
  <p>The Fandom Hakuri infobox lists 27 March. Japanese merch calendars (days366 and others) cite tankōbon extras and official birthday can badges for that date, and for a longer list: Hiyuki 8 January, Iori, Azami, Samura, Tenri, Ro, Moku, and more. Those calendars also disagree with each other. At least one puts 21 December on Hinao instead of Char. Char’s 21 December on this site comes from the chapter 2 color page, not a badge we have held.</p>
  <p>Until this archive has seen the badge, the extras page, or a Jump profile scan, the extra dates stay a citation, not a row we treat as printed law. Hakuri 27 March is the obvious first check because Fandom already promotes it as biographical. If you have the can or the volume extras page, the next edit is one cell. We will not invent the rest of the tin.</p>
  <p>Volume extras we do file: <em>Genichi Sojo’s Bathhouse Quest</em> (two parts) and <em>Soya Sazanami’s Memories, Begone!</em> Those live on <a href="../manga/omake.html">omake</a> and <a href="../fun/oneshots.html">oneshots</a>. Magazine-versus-volume art changes sit on the <a href="../manga/volumes.html">volume guide</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="birthdays.html">Birthdays</a><a href="register.html">Register</a><a href="../fun/voices.html">Voices</a><a href="../manga/omake.html">Omake</a><a href="../manga/volumes.html">Volumes</a><a href="index.html">World</a></nav>
""",
)

write(
    "world/fight-log.html",
    "Kagurabachi Fight Log",
    "Lookup table of Kagurabachi fights: combatants, chapter rooms, outcome, techniques. The battles essay stays the commute.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Fight log',
    "Lookup",
    "Fight log",
    "戦闘表",
    "One row per clash the book actually spends pages on. The battles page is the essay. This is the table.",
    """
  <p><a href="battles.html">Battles</a> is the commute in sentences. This page is the index Fandom’s fight articles give you by URL: who, which chapters, what steel, what is left standing. Technique names resolve on the <a href="technique-index.html">technique index</a>. Official chapters: VIZ / MANGA Plus.</p>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>Fight</th><th>Chapters</th><th>Combatants</th><th>Steel / art</th><th>Left standing</th></tr></thead>
    <tbody>
      <tr><td>The raid</td><td><a href="../manga/chapter-1.html">1</a> (flashback)</td><td>Hishaku cell vs Kunishige, Chihiro</td><td>Hokuto, Uran on the night; Enten stays</td><td>Kunishige dead. Six wartime blades gone. <a href="raid.html">Raid</a></td></tr>
      <tr><td>Cafe / early jobs</td><td>1–7</td><td>Chihiro, Shiba vs underworld</td><td>Enten</td><td>Demonstration, not a first villain. <a href="underworld.html">Street</a></td></tr>
      <tr><td>Chihiro vs Madoka</td><td><a href="../manga/chapter-8.html">8</a></td><td>Chihiro, Shiba vs Norisaku Madoka</td><td>Enten / exploding Daruma</td><td>Madoka beaten, then killed by Sojo for talking</td></tr>
      <tr><td>Enten vs Cloud Gouger</td><td><a href="../manga/chapter-9.html">9</a>–<a href="../manga/chapter-18.html">18</a></td><td>Chihiro vs Sojo; ACG in the same city</td><td>Enten / Cloud Gouger; True Realm at <a href="../manga/chapter-14.html">14</a></td><td>Cloud Gouger bisected. Sojo dies in Datenseki backlash. Four ACG graves</td></tr>
      <tr><td>ACG vs Sojo</td><td>Vs. Sojo middle</td><td>Hagiwara’s six vs Sojo</td><td>Jikai, Gansui, binding, iron body, Kaichi unused</td><td>Harima, Uzuki, Kasahara, Kugara dead. Hagiwara legless. Kazane one-armed. <a href="bathhouse.html">Bathhouse</a></td></tr>
      <tr><td>Chihiro vs Hiyuki (first)</td><td>Rakuzaichi open</td><td>Chihiro vs Hiyuki</td><td>Enten / Flame Bone</td><td>Truce later, not a finish. <a href="../analysis/flame-bone.html">Flame Bone</a></td></tr>
      <tr><td>Estate / Tou</td><td>Rakuzaichi middle</td><td>Chihiro, Shiba vs Soya, Tamaki, Enji, Tenri</td><td>Isou; Tenri’s Datenseki tool</td><td>Tenri pops. Enten surrendered to scout the Kura</td></tr>
      <tr><td>Hakuri vs Soya</td><td>~32–37</td><td>Hakuri vs Soya</td><td>Isou, then Storehouse</td><td>Hakuri wakes. Soya later amnesiac. <a href="../manga/chapter-37.html">Equal</a></td></tr>
      <tr><td>Storehouse war</td><td>38–<a href="../manga/chapter-44.html">44</a></td><td>Chihiro, Hiyuki vs Kyora / Shinuchi proxy</td><td>Enten, dying Cloud Gouger, Flame Bone, Magatsumi overwrite</td><td>Prisoners out. Kyora dead. Auction over</td></tr>
      <tr><td>Train interception</td><td><a href="../manga/chapter-50.html">50</a>+</td><td>Chihiro vs Hiruhiko and hirelings</td><td>Enten / Blood Crane</td><td>Fight spills to kabuki. <a href="train.html">Train</a></td></tr>
      <tr><td>Kokugoku / Steam Squad</td><td>48–49</td><td>Steam Squad vs Datenseki troops, then Hiruhiko</td><td>Smoke Axe; Datenseki muscle</td><td>Fushimi and squad die. <a href="../factions/steam-squad.html">Steam Squad</a></td></tr>
      <tr><td>Senkutsuji</td><td><a href="../manga/chapter-51.html">51</a>–<a href="../manga/chapter-57.html">57</a></td><td>Samura, Masumi vs pine hirelings; Samura vs Uruha</td><td>Tobimune returned; Suzaku cut</td><td>Temple falls. Uruha “killed.” Owl up. <span class="spoiler">Contract surgery</span></td></tr>
      <tr><td>Chihiro vs Kuguri</td><td>Hotel road / <a href="../manga/chapter-70.html">70</a></td><td>Chihiro vs Kuguri</td><td>Improvised Iai / Twilight Wave</td><td>Kuguri stays for the boy. Iori still the job</td></tr>
      <tr><td>Hotel / Banquet</td><td><a href="../manga/chapter-67.html">67</a>–<a href="../manga/chapter-76.html">76</a></td><td>Chihiro, Iori, Masumi vs Hiruhiko, Kuguri, Toto</td><td>Enten, Iai, Kumeyuri Banquet and Play</td><td>Hotel wrecked. Samura arrives. Kumeyuri later recovered by Ro</td></tr>
      <tr><td>Enten vs Tobimune</td><td><a href="../manga/chapter-82.html">82</a>–<a href="../manga/chapter-83.html">83</a></td><td>Chihiro vs Samura</td><td>Enten / Tobimune</td><td>Brief spoken. Samura opens his eyes</td></tr>
      <tr><td>HQ infiltration</td><td>86–105</td><td>Hishaku vs Kamunabi; Kiri, Natsuki, Azami, Hagiwara, Hakuri</td><td>Shinuchi at range; Yukisada Vessel; Kudo’s Path</td><td>Kudo dead. Kasen’s leak on the table. Cell reached. <a href="hq.html">HQ</a></td></tr>
      <tr><td>Street over HQ</td><td>106–<a href="../manga/chapter-115.html">115</a></td><td>Chihiro, Samura vs Yura, then Akemura</td><td><a href="../manga/chapter-108.html">Enten vs Magatsumi</a>, <a href="../manga/chapter-109.html">Tobimune vs Magatsumi</a></td><td><span class="spoiler">Enten bisected. Samura spent. Iori holds Tobimune. Akemura loose</span></td></tr>
      <tr><td>Irishima (war book)</td><td><a href="../manga/chapter-117.html">117</a>–121, later deaths</td><td>Soga vs Mikaboshi / Ariu</td><td>Kurotsuchi, Sumika, Datenseki bodies</td><td>Talks first. Hiroto and Yoshinojo die later on the island, not in the talks plates</td></tr>
    </tbody>
  </table></div>
  <p>Part 2’s kiln is labor, not a ranked fight. Those weeks live on <a href="../manga/chapter-125.html">Smelting</a> and <a href="smelting.html">the kiln room</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="battles.html">Battles</a><a href="technique-index.html">Technique index</a><a href="../manga/chapters.html">Chapters</a><a href="../arcs/index.html">Arcs</a><a href="index.html">World</a></nav>
""",
)

write(
    "world/technique-index.html",
    "Kagurabachi Technique Index",
    "Lookup table of named Kagurabachi techniques: blade kit, innate arts, schools. The catalog stays the essay.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Technique index',
    "Lookup",
    "Technique index",
    "技索引",
    "Name, owner, what it does, which room. Asterisks are unofficial names the pages did not print.",
    """
  <p>The <a href="techniques.html">technique catalog</a> is the essay with kit in paragraphs. This page is the index: one row, one name. Blade files still hold the longer kit. Schools have their own rooms. Official chapters: VIZ / MANGA Plus.</p>

  <h2>Enchanted Blade techniques</h2>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>Name</th><th>Blade</th><th>Bearer shown</th><th>What it does</th></tr></thead>
    <tbody>
      <tr><td>Kuro 涅</td><td><a href="../blades/enten.html">Enten</a></td><td>Chihiro</td><td>Black goldfish; flying slash sized to the fish</td></tr>
      <tr><td>Kuro: Shred 涅千</td><td>Enten</td><td>Chihiro</td><td>Many small black fish, many small cuts; scouts</td></tr>
      <tr><td>Aka 猩</td><td>Enten</td><td>Chihiro</td><td>Red goldfish drinks an attack; spend the name back</td></tr>
      <tr><td>Nishiki 錦</td><td>Enten</td><td>Chihiro</td><td>Tricolor cloak: speed, power, resistance</td></tr>
      <tr><td>Nishiki: Support*</td><td>Enten</td><td>Chihiro</td><td>Wounded form; less strain</td></tr>
      <tr><td>Mei 鳴</td><td><a href="../blades/cloud-gouger.html">Cloud Gouger</a></td><td>Sojo, Chihiro</td><td>Lightning. Heavy charge can disable Mei briefly</td></tr>
      <tr><td>Cloaked Mei*</td><td>Cloud Gouger</td><td>Sojo first</td><td>Wear the lightning instead of throwing it</td></tr>
      <tr><td>Mei: Shred 鳴千</td><td>Cloud Gouger</td><td>Chihiro, blade dying</td><td>Black lightning. Dark power</td></tr>
      <tr><td>Yui 結</td><td>Cloud Gouger</td><td>Sojo, Chihiro</td><td>Ice cages and constructs</td></tr>
      <tr><td>Kou 降</td><td>Cloud Gouger</td><td>Sojo, Chihiro</td><td>Water or mist; sets up Mei and Yui</td></tr>
      <tr><td>Spider 蛛</td><td><a href="../blades/magatsumi.html">Magatsumi</a></td><td>Akemura, proxies</td><td>Web and eyes; caught entities cannot move</td></tr>
      <tr><td>Dragonfly 蜻</td><td>Magatsumi</td><td>Akemura, proxies</td><td>Wing shapes, directional blast</td></tr>
      <tr><td>Centipede 蜈</td><td>Magatsumi</td><td>Akemura, proxies</td><td>Omnidirectional blast; weakest behind the wielder</td></tr>
      <tr><td>Butterfly 蝶</td><td>Magatsumi</td><td>Akemura</td><td>Amplified slash through space</td></tr>
      <tr><td>Bee 蜂</td><td>Magatsumi</td><td>Akemura</td><td>Rings; piercing blast</td></tr>
      <tr><td>Malediction 蠱</td><td>Magatsumi</td><td>Akemura</td><td>True Realm as policy. ~200,000 after the treaty. <a href="../analysis/malediction.html">Essay</a></td></tr>
      <tr><td>Banquet 宴</td><td><a href="../blades/kumeyuri.html">Kumeyuri</a></td><td>Hiruhiko, Uruha</td><td>Intoxicating hallucinations. <a href="../manga/chapter-76.html">Ch. 76</a></td></tr>
      <tr><td>Play 遊</td><td>Kumeyuri</td><td>Hiruhiko</td><td>Move objects; fluency scales with respect. <a href="../analysis/play.html">Essay</a></td></tr>
      <tr><td>Destructive Play*</td><td>Kumeyuri</td><td>Hiruhiko</td><td>Hotel comes apart because he does not respect objects</td></tr>
      <tr><td>Crow 鴉</td><td><a href="../blades/tobimune.html">Tobimune</a></td><td>Samura</td><td>Swap with a feather</td></tr>
      <tr><td>External Crow*</td><td>Tobimune</td><td>Samura</td><td>Move entities other than bearer and blade</td></tr>
      <tr><td>Owl 梟</td><td>Tobimune</td><td>Samura</td><td>Detection; nationwide only huge spirit sources. <a href="../analysis/owl.html">Essay</a></td></tr>
      <tr><td>Suzaku 雀</td><td>Tobimune</td><td>Samura</td><td>Flames that heal the bearer; later contract-killing revival</td></tr>
      <tr><td>External Suzaku*</td><td>Tobimune</td><td>Samura</td><td>Heal others; restore ruined objects</td></tr>
      <tr><td>Suzaku: Black Flames*</td><td>Tobimune</td><td>Samura</td><td>Dark power. Stalls Magatsumi’s drain. Samura dies in that math</td></tr>
    </tbody>
  </table></div>
  <p>Two wartime blades are still unnamed. Subaru is a surviving bearer. <a href="first-blade.html">The first blade</a> is still unnamed after chapter 130. True Realm: <a href="../manga/chapter-14.html">ch. 14</a> and the <a href="../analysis/true-realm.html">essay</a>. Dark power: <a href="dark-power.html">Kuroi chikara</a>.</p>

  <h2>Innate arts and schools</h2>
  <div class="table-wrap"><table class="lookup">
    <thead><tr><th>Name</th><th>User</th><th>What it does</th><th>Room</th></tr></thead>
    <tbody>
      <tr><td>Teleportation</td><td>Shiba</td><td>Extraction, infiltration, evacuation</td><td><a href="../characters/shiba.html">Shiba</a></td></tr>
      <tr><td>Coin (Koin)</td><td>Azami</td><td>Clinic stimulant rewritten as execution</td><td><a href="../characters/azami.html">Azami</a></td></tr>
      <tr><td>Isou</td><td>Sazanami; Hakuri</td><td>Burial-force</td><td><a href="../characters/hakuri.html">Hakuri</a></td></tr>
      <tr><td>Storehouse (Kura)</td><td>Kyora, then Hakuri</td><td>Subspace for loot and people</td><td><a href="storehouse.html">Storehouse</a></td></tr>
      <tr><td>Flame Bone of the Starving</td><td>Hiyuki</td><td>Hereditary skeleton, licensed</td><td><a href="../analysis/flame-bone.html">Essay</a></td></tr>
      <tr><td>Duel domain</td><td>Tafuku</td><td>Two people, one match</td><td><a href="../characters/tafuku.html">Tafuku</a></td></tr>
      <tr><td>Lightning Menace (Raiku)</td><td>Natsuki</td><td>Voltage in the body, not Mei</td><td><a href="../characters/natsuki.html">Natsuki</a></td></tr>
      <tr><td>Armored puppet</td><td>Hokuto</td><td>Self-resembling armor, piece control</td><td><a href="../characters/hokuto.html">Hokuto</a></td></tr>
      <tr><td>Twilight Wave (Hagure)</td><td>Kuguri</td><td>Bank motion and heat, spend later</td><td><a href="../characters/kuguri.html">Kuguri</a></td></tr>
      <tr><td>Blood Crane (Chizuru)</td><td>Hiruhiko</td><td>Origami that cuts and lifts</td><td><a href="../characters/hiruhiko.html">Hiruhiko</a></td></tr>
      <tr><td>Blood tracking</td><td>Toto</td><td>Locate and read through blood</td><td><a href="../characters/toto.html">Toto</a></td></tr>
      <tr><td>Regeneration (Hishaku)</td><td>Yukisada</td><td>Survives decapitation; Vessel</td><td><a href="../characters/yukisada.html">Yukisada</a></td></tr>
      <tr><td>Mako</td><td>Bingo</td><td>Lion-dancer heads; stacked weight; corpses</td><td><a href="../characters/bingo.html">Bingo</a></td></tr>
      <tr><td>Ice</td><td>Uran</td><td>Freeze, including breath</td><td><a href="../characters/uran.html">Uran</a></td></tr>
      <tr><td>Kyonagi regeneration</td><td>Char</td><td>Close her wounds and other people’s</td><td><a href="../characters/char.html">Char</a></td></tr>
      <tr><td>Foresight</td><td>Chiaki</td><td>Princess Soga, Izanami proof</td><td><a href="../characters/chiaki.html">Chiaki</a></td></tr>
      <tr><td>Kurotsuchi</td><td>Hiroto</td><td>Directional gravity</td><td><a href="../characters/hiroto.html">Hiroto</a></td></tr>
      <tr><td>Sumika</td><td>Ariu</td><td>Insect constructs, poisoned air</td><td><a href="../characters/ariu.html">Ariu</a></td></tr>
      <tr><td>Warrior’s Path (Shitō)</td><td>Kudo</td><td>Send a body through architecture</td><td><a href="../characters/kudo.html">Kudo</a></td></tr>
      <tr><td>Bead chains</td><td>Izaru</td><td>Restrict</td><td><a href="../characters/izaru.html">Izaru</a></td></tr>
      <tr><td>Jikai</td><td>Hagiwara</td><td>Magnetism</td><td><a href="../characters/hagiwara.html">Hagiwara</a></td></tr>
      <tr><td>Duplication</td><td>Subaru</td><td>Several Subarus</td><td><a href="../characters/subaru.html">Subaru</a></td></tr>
      <tr><td>Akuu</td><td>Mashiro</td><td>Air pressure, hands-free weapons</td><td><a href="../characters/mashiro.html">Mashiro</a></td></tr>
      <tr><td>Gansui</td><td>Harima</td><td>Lift and shape stone</td><td><a href="../characters/harima.html">Harima</a></td></tr>
      <tr><td>Binding spells</td><td>Uzuki</td><td>Restrict movement</td><td><a href="../characters/uzuki.html">Uzuki</a></td></tr>
      <tr><td>Enlarged hands</td><td>Kasahara</td><td>Size as a weapon</td><td><a href="../characters/kasahara.html">Kasahara</a></td></tr>
      <tr><td>Smoke Axe</td><td>Fushimi</td><td>Cut with smoke between hands</td><td><a href="../characters/fushimi.html">Fushimi</a></td></tr>
      <tr><td>Crimson Recital (Koen)</td><td>Uruha</td><td>Innate physical boost when the contract dies</td><td><a href="crimson-recital.html">Crimson Recital</a></td></tr>
      <tr><td>Iai White Purity Style</td><td>Samura, Uruha, Chihiro, Iori, Kiri</td><td>School, not innate. Eyes closed. Speed</td><td><a href="iai.html">Iai</a> · <a href="../manga/chapter-70.html">Ch. 70</a></td></tr>
      <tr><td>Reigen One-Sword Style</td><td>Sengoku, hotel staff</td><td>House style at the Kyoto hotel</td><td><a href="reigen.html">Reigen</a></td></tr>
      <tr><td>Sand-Bone One-Sword Style</td><td>Subaru</td><td>Subaru’s school beside the sushi</td><td><a href="sand-bone.html">Sand-Bone</a></td></tr>
    </tbody>
  </table></div>
    <nav class="related" aria-label="Related pages"><a href="techniques.html">Technique catalog</a><a href="fight-log.html">Fight log</a><a href="../blades/index.html">Blades</a><a href="innate.html">Innate</a><a href="sorcery.html">Sorcery</a><a href="index.html">World</a></nav>
""",
)

print("lookup tables done")
