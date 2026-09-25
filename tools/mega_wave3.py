#!/usr/bin/env python3
"""Third mega wave: leftover printed kit, extras, publication doors.

Printed facts only. No chapter 132 title, no first-blade name, no invented kanji.
118-120 stay table-only. Unofficial phrases stay marked.
"""
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("mega_pages", Path("/workspace/tools/mega_pages.py"))
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)

write = mp.write
related = mp.related
VIZ = mp.VIZ
ROOT = mp.ROOT


def safe_write(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    if (ROOT / rel).exists():
        print("skip exists", rel)
        return
    write(rel, title, desc, crumb, kicker, h1, jp, lede, body)


def crumb_for(rel, h1):
    folder = "World"
    if rel.startswith("analysis/"):
        folder = "Essays"
    elif rel.startswith("fun/"):
        folder = "Fun"
    elif rel.startswith("guide/"):
        folder = "Guide"
    elif rel.startswith("factions/"):
        folder = "Factions"
    elif rel.startswith("manga/"):
        folder = "Manga"
    elif rel.startswith("media/"):
        folder = "Media"
    return f'<a href="../index.html">Archive</a> / <a href="index.html">{folder}</a> / {h1}'


def main():
    extras = [
        ("world/spider.html", "Spider (蛛) | Magatsumi Technique | Kagurabachi",
         "Spider, Magatsumi kit: cobweb and eyes. Caught entities cannot move.",
         "Magatsumi · 蛛", "Spider", "蛛",
         "A web. Eyes. The caught stay still.",
         f"""
  <p>Spider (蛛) is printed on the technique catalog as Magatsumi kit: cobweb and eyes. Caught entities cannot move. This is not a fandom label. The three-count does not apply to this sword. Dragonfly, Centipede, Butterfly, Bee, and Malediction sit beside it.</p>
  <p>Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Group: <a href="insect-kit.html">insect kit</a>. Catalog: <a href="techniques.html">techniques</a>. Official: {VIZ}.</p>
    {related([("insect-kit.html", "Insect kit"), ("dragonfly.html", "Dragonfly"), ("../blades/magatsumi.html", "Magatsumi"), ("malediction.html", "Malediction")])}
"""),
        ("world/centipede.html", "Centipede (蜈) | Magatsumi Technique | Kagurabachi",
         "Centipede, Magatsumi kit: omnidirectional blast from circular structures. Weakest behind the wielder.",
         "Magatsumi · 蜈", "Centipede", "蜈",
         "A ring blast. The back is the soft side.",
         f"""
  <p>Centipede (蜈) is printed Magatsumi kit: omnidirectional blast from circular structures. Weakest directly behind the wielder. The catalog already files that opening. This page is the insect so a search does not merge it with Dragonfly.</p>
  <p>Sisters: <a href="spider.html">Spider</a>, <a href="dragonfly.html">Dragonfly</a>, <a href="butterfly.html">Butterfly</a>, <a href="bee.html">Bee</a>.</p>
    {related([("insect-kit.html", "Insect kit"), ("spider.html", "Spider"), ("../blades/magatsumi.html", "Magatsumi"), ("techniques.html", "Catalog")])}
"""),
        ("world/butterfly.html", "Butterfly (蝶) | Magatsumi Technique | Kagurabachi",
         "Butterfly, Magatsumi kit: amplified slash through space. A building, then the buildings behind it.",
         "Magatsumi · 蝶", "Butterfly", "蝶",
         "A cut that keeps going through rooms.",
         f"""
  <p>Butterfly (蝶) is printed Magatsumi kit: amplified slash through space. A building, then the buildings behind it. Not Bee’s rings. Not Centipede’s circle. The war sword spends architecture as a corridor.</p>
  <p>Kit: <a href="insect-kit.html">insect kit</a>. Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. HQ week lives on the <a href="hq.html">headquarters</a> page.</p>
    {related([("insect-kit.html", "Insect kit"), ("bee.html", "Bee"), ("../blades/magatsumi.html", "Magatsumi"), ("hq.html", "HQ")])}
"""),
        ("world/bee.html", "Bee (蜂) | Magatsumi Technique | Kagurabachi",
         "Bee, Magatsumi kit: rings, piercing blast widest at the origin and narrowest at the point.",
         "Magatsumi · 蜂", "Bee", "蜂",
         "A ring that narrows to a point.",
         f"""
  <p>Bee (蜂) is printed Magatsumi kit: rings, piercing blast widest at the origin and narrowest at the point. The catalog already says that. This page keeps Bee from being a synonym for Butterfly.</p>
  <p>Group: <a href="insect-kit.html">insect kit</a>. Crime: <a href="malediction.html">Malediction</a> (蠱). Official: {VIZ}.</p>
    {related([("insect-kit.html", "Insect kit"), ("butterfly.html", "Butterfly"), ("malediction.html", "Malediction"), ("techniques.html", "Catalog")])}
"""),
        ("world/insect-kit.html", "Magatsumi’s Insect Kit | Spider to Bee | Kagurabachi",
         "Printed Magatsumi insects: Spider, Dragonfly, Centipede, Butterfly, Bee, then Malediction. No three-count.",
         "Magatsumi · insects", "The insect kit", "蟲",
         "Five insects, then a national extension.",
         f"""
  <p>Magatsumi refuses the three-count. The catalog prints <a href="spider.html">Spider 蛛</a>, <a href="dragonfly.html">Dragonfly 蜻</a>, <a href="centipede.html">Centipede 蜈</a>, <a href="butterfly.html">Butterfly 蝶</a>, <a href="bee.html">Bee 蜂</a>, then <a href="malediction.html">Malediction 蠱</a> (Kodoku). Flowers, black weep, insects. A camp of explainers treats this kit as Ariu’s Sumika recast in steel. The chapters have not confirmed that.</p>
  <p>Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Camp: <a href="../analysis/insect-camp.html">the insect camp</a>. Ariu: <a href="sumika.html">Sumika</a>.</p>
    {related([("../blades/magatsumi.html", "Magatsumi"), ("spider.html", "Spider"), ("malediction.html", "Malediction"), ("../analysis/insect-camp.html", "Camp")])}
"""),
        ("world/kaichi.html", "Demon Monster (Kaichi) | Kazane | Kagurabachi",
         "Kazane Machi’s Demon Monster, 怪魑, Kaichi: the unused ACG secret weapon. Sojo takes the arm first.",
         "ACG · 怪魑", "Demon Monster", "怪魑",
         "A reserve that does not get to be a reserve.",
         f"""
  <p>Demon Monster (怪魑, Kaichi) is Kazane Machi’s printed art: the unused secret weapon of the Anti-Cloud Gouger Special Forces. Sojo takes the right arm first. Newest member. A reserve spent before it is spent. This is not a blade technique.</p>
  <p>Person: <a href="../characters/kazane.html">Kazane</a>. Unit: <a href="acg.html">ACG</a>. Kit: <a href="acg-kit.html">ACG kit</a>.</p>
    {related([("../characters/kazane.html", "Kazane"), ("acg.html", "ACG"), ("acg-kit.html", "ACG kit"), ("../manga/chapter-13.html", "Elite")])}
"""),
        ("world/uzuki-binding.html", "Uzuki’s Binding | ACG | Kagurabachi",
         "Kiyohiko Uzuki’s binding spells: Anti-Cloud Gouger kit. Named. One of six.",
         "ACG · 卯月", "Binding spells", "縛",
         "A specialist sentence in a six-person unit.",
         f"""
  <p>Kiyohiko Uzuki’s printed art is binding spells. He is Anti-Cloud Gouger. The innate page files him next to Harima’s Gansui and Kasahara’s enlarged hands. Four of the six die in the first book. The chapters name the kit so the graves keep names.</p>
  <p>Person: <a href="../characters/uzuki.html">Uzuki</a>. Unit: <a href="acg.html">ACG</a>. Stone: <a href="gansui.html">Gansui</a>.</p>
    {related([("../characters/uzuki.html", "Uzuki"), ("acg.html", "ACG"), ("gansui.html", "Gansui"), ("kasahara-hands.html", "Hands")])}
"""),
        ("world/kasahara-hands.html", "Kasahara’s Enlarged Hands | ACG | Kagurabachi",
         "Makoto Kasahara’s enlarged hands: Anti-Cloud Gouger kit. Named with the unit.",
         "ACG · 笠原", "Enlarged hands", "手",
         "A body art. Then the compound.",
         f"""
  <p>Makoto Kasahara’s printed art is enlarged hands. Anti-Cloud Gouger. The catalog lists him with Uzuki’s binding and Harima’s Gansui. Named. Competent. The unit still fails the weather sword. This page is the kit, not a recap of every panel.</p>
  <p>Person: <a href="../characters/kasahara.html">Kasahara</a>. Unit: <a href="acg.html">ACG</a>. Iron: <a href="iron-body.html">Kugara</a>.</p>
    {related([("../characters/kasahara.html", "Kasahara"), ("acg.html", "ACG"), ("uzuki-binding.html", "Binding"), ("iron-body.html", "Iron body")])}
"""),
        ("world/acg-kit.html", "Anti-Cloud Gouger Kit | Six Arts, One Sword | Kagurabachi",
         "ACG kit: Jikai, iron body, Kaichi, Gansui, binding, enlarged hands. Four graves among six.",
         "Kamunabi · ACG", "The ACG kit", "対刳雲",
         "Six people built to solve one sword.",
         f"""
  <p>The Anti-Cloud Gouger Special Forces carry six printed arts that are not blades: Hagiwara’s <a href="jikai.html">Jikai</a>, Kugara’s <a href="iron-body.html">iron body</a>, Kazane’s <a href="kaichi.html">Kaichi</a>, Harima’s <a href="gansui.html">Gansui</a>, Uzuki’s <a href="uzuki-binding.html">binding</a>, Kasahara’s <a href="kasahara-hands.html">enlarged hands</a>. Four graves. Two survivors. The unit is the state’s matching piece. Sojo spends it anyway.</p>
  <p>Roster: <a href="acg.html">ACG</a>. Essay: <a href="../analysis/acg-cavalry.html">the cavalry</a>. Arc: <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
    {related([("acg.html", "ACG"), ("jikai.html", "Jikai"), ("kaichi.html", "Kaichi"), ("../analysis/named-graves.html", "Graves")])}
"""),
        ("world/kyonagi-regen.html", "Kyonagi Regeneration | Char | Kagurabachi",
         "Char’s Kyonagi regeneration: close her own wounds and other people’s. Sojo’s stabilizer hunt.",
         "Kyonagi · Char", "Kyonagi regeneration", "再生",
         "A clan art. Then a child in a hunt.",
         f"""
  <p>Kyonagi regeneration is Char’s printed art: close her own wounds and other people’s. Last of the clan. Sojo held her as a Datenseki stabilizer. Chihiro’s group holds her as a child. Birthday December 21, one of five printed dates. This is not Yukisada’s regeneration and not Suzaku.</p>
  <p>Person: <a href="../characters/char.html">Char</a>. Clan: <a href="../factions/kyonagi.html">Kyonagi</a>. Meals: <a href="../manga/chapter-5.html">A Good Meal</a>.</p>
    {related([("../characters/char.html", "Char"), ("../factions/kyonagi.html", "Kyonagi"), ("food.html", "Meals"), ("../world/birthdays.html", "Birthdays")])}
"""),
        ("world/bead-chains.html", "Izaru’s Bead Chains | Kamunabi | Kagurabachi",
         "Izaru’s bead chains: restrict a target. Leadership table’s prosecutor kit.",
         "Kamunabi · 誘", "Bead chains", "鎖",
         "A prosecutor’s restrict, not a blade.",
         f"""
  <p>Izaru’s printed art is bead chains: restrict a target. He sits on the Kamunabi leadership table. Talks as if Kunishige stole national property. The catalog lists the chains so the table is not only surnames. This is not Hakuri’s Isou and not a Storehouse move.</p>
  <p>Person: <a href="../characters/izaru.html">Izaru</a>. Table: <a href="../factions/leadership.html">leadership</a>. Org: <a href="../factions/kamunabi.html">Kamunabi</a>.</p>
    {related([("../characters/izaru.html", "Izaru"), ("../factions/leadership.html", "Leadership"), ("../factions/kamunabi.html", "Kamunabi"), ("innate.html", "Innate")])}
"""),
        ("world/subaru-duplication.html", "Subaru’s Duplication | Wartime Bearer | Kagurabachi",
         "Subaru Urita’s duplication: several Subarus. A contract-opening assassination’s nightmare.",
         "Bearers · 昴", "Duplication", "分身",
         "Kill one body. The contract does not open.",
         f"""
  <p>Subaru Urita’s printed art is duplication: several Subarus. He is a surviving wartime bearer and, in Part 2, a smith and sushi colleague when the steel comes up. A Lifelong Contract opens if the bearer dies. Several bodies make that job a nightmare. This page does not name his Enchanted Blade. The first blade is still unnamed.</p>
  <p>Person: <a href="../characters/subaru.html">Subaru</a>. Door: <a href="first-blade.html">first blade</a>. Kiln: <a href="smelting.html">smelting</a>.</p>
    {related([("../characters/subaru.html", "Subaru"), ("first-blade.html", "First blade"), ("wartime-two.html", "Unnamed two"), ("smelting.html", "Smelting")])}
"""),
        ("world/wartime-two.html", "The Unnamed Wartime Two | Enchanted Blades | Kagurabachi",
         "Two Enchanted Blades still have no printed names. Subaru is a surviving bearer. The first plate is still work.",
         "Catalog · blank", "The unnamed two", "無名",
         "Jump has not printed the titles. We will not invent them.",
         f"""
  <p>Two Enchanted Blades still have no printed names. Subaru is a surviving bearer. One war-ensemble portrait is still unnamed. Ibuki is dead and his sword is Cloud Gouger, which is named. The first Enchanted Blade is still unnamed after chapter 131’s listing. When Jump prints the titles they belong on the catalog.</p>
  <p>Essay: <a href="../analysis/two-unnamed.html">two unnamed</a>. Door: <a href="first-blade.html">first blade</a>. Count: <a href="seventh.html">the seventh</a>.</p>
    {related([("first-blade.html", "First blade"), ("../analysis/two-unnamed.html", "Essay"), ("seventh.html", "Seventh"), ("techniques.html", "Catalog")])}
"""),
        ("world/sword-master.html", "Sword Master (Kensei) | Akemura’s Press Name | Kagurabachi",
         "Sword Master, Kensei: the press and Kamunabi name for Akemura after Malediction. Chapter 100 titles the word.",
         "Press · 剣聖", "Sword Master", "剣聖",
         "A headline. The book puts quotes on it.",
         f"""
  <p>Sword Master (Kensei) is Akemura’s press name. Chapter 100 titles the word. Volume 11 wears Heroes. The chapter index keeps the quotation marks because the Kamunabi printed those words after Malediction. This page is the office title, not a new person.</p>
  <p>Person: <a href="../characters/akemura.html">Akemura</a>. Chapter: <a href="../manga/chapter-100.html">100</a>. Quotes: <a href="../analysis/quotation-marks.html">essay</a>.</p>
    {related([("../characters/akemura.html", "Akemura"), ("../manga/chapter-100.html", "Ch. 100"), ("quoted-headlines.html", "Headlines"), ("malediction.html", "Malediction")])}
"""),
        ("world/master-key.html", "Magatsumi as Master Key | Lifelong Contracts | Kagurabachi",
         "If Akemura dies, the other five wartime bearers die with him. Magatsumi’s contract is the master key.",
         "Contracts · 真打", "The master key", "鍵",
         "One death as a national off-switch.",
         f"""
  <p>A Lifelong Contract binds a blade to one nervous system. Magatsumi’s contract is the master key: if Akemura dies, the other five wartime bearers die with him. Yura wanted that knot open. Then he spoke to Akemura and changed the math. Enten is the seventh and never sat in that knot.</p>
  <p>Contracts: <a href="contracts.html">Lifelong Contracts</a>. Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Shinuchi: <a href="shinuchi.html">Shinuchi</a>.</p>
    {related([("contracts.html", "Contracts"), ("../blades/magatsumi.html", "Magatsumi"), ("shinuchi.html", "Shinuchi"), ("../characters/yura.html", "Yura")])}
"""),
        ("world/tenri-stone.html", "Tenri’s Stone | Half-Stable Datenseki | Kagurabachi",
         "Tenri Sazanami eats a half-stable Datenseki stone trying to impress Kyora. A fake of Kunishige’s eyes.",
         "Rakuzaichi · 天理", "Tenri’s stone", "石",
         "A permission slip that kills the son.",
         f"""
  <p>Tenri Sazanami dies on a half-stable Datenseki stone trying to impress Kyora. Kunishige’s eyes were the only known way to make the mineral into weather instead of a crater. Sojo’s industrial fake and Tenri’s jellyfish tool are the same sentence from two houses. Named. Then buried.</p>
  <p>Person: <a href="../characters/tenri.html">Tenri</a>. Mineral: <a href="datenseki.html">Datenseki</a>. Briefcase: <a href="briefcase.html">Sojo’s case</a>.</p>
    {related([("../characters/tenri.html", "Tenri"), ("datenseki.html", "Datenseki"), ("../factions/tou.html", "The Tou"), ("../analysis/named-graves.html", "Graves")])}
"""),
        ("world/three-count.html", "The Three-Count | Most Enchanted Blades | Kagurabachi",
         "Most Enchanted Blades have three named techniques. Magatsumi refuses the count. Two wartime swords are still blank.",
         "Catalog · 三", "The three-count", "三技",
         "Goldfish, clouds, feathers. Then a sword that will not stop at three.",
         f"""
  <p>Most Enchanted Blades have three named techniques. Enten, Cloud Gouger, Kumeyuri, and Tobimune keep that grammar, then grow extensions. Magatsumi refuses the three-count: five insects plus Malediction. Two wartime swords still have no printed names. This page is the rule the catalog already states.</p>
  <p><a href="techniques.html">Catalog</a>. <a href="insect-kit.html">Insects</a>. <a href="extension-kit.html">Extensions</a>.</p>
    {related([("techniques.html", "Catalog"), ("insect-kit.html", "Insects"), ("extension-kit.html", "Extensions"), ("wartime-two.html", "Unnamed two")])}
"""),
        ("manga/chapter-132.html", "Kagurabachi Chapter 132 | Jump 2026 Issue 44",
         "Chapter 132’s magazine door: Weekly Shōnen Jump 2026 issue 44, on sale 28 September 2026. Title not printed on this desk.",
         "Jump 44 · door", "Chapter 132’s door", "第132話",
         "A return date. Not a weekly title. We will not invent one.",
         f"""
  <p>Read it official when it lands: {VIZ}. Chapter 132 was scheduled for the 42/43 combined issue (14 September 2026) and was announced on hiatus for the author’s sudden illness. The official account said Takeru Hokazono had already recovered. Continuation: Jump 2026 issue 44, on sale 28 September 2026. This page is a publication door. We do not invent the title or the panels.</p>
  <p>Chapter 131 is <a href="chapter-131.html">Tipping Point</a> (転換点). The rest note: <a href="../fun/september-2026-rest.html">September rest</a>. Issue room: <a href="../fun/jump-2026-44.html">issue 44</a>.</p>
    {related([("chapter-131.html", "Ch. 131"), ("../fun/september-2026-rest.html", "September rest"), ("../fun/jump-2026-44.html", "Issue 44"), ("publication.html", "Publication")])}
"""),
        ("fun/jump-2026-41.html", "Jump 2026 Issue 41 | Chapter 131 Tipping Point",
         "Weekly Shōnen Jump 2026 #41 carried Kagurabachi chapter 131, Tipping Point. VIZ dated 6 September 2026.",
         "Fun · magazine", "Issue 41", "2026#41",
         "6 September 2026. Tipping Point. Then a health skip.",
         f"""
  <p>Weekly Shōnen Jump 2026 issue 41 carried chapter 131, “Tipping Point” (転換点). VIZ’s listing is 6 September 2026. The next magazine slot, combined 42/43, rested. This page is the issue that did print. Official chapters: {VIZ}.</p>
  <p>Room: <a href="../manga/chapter-131.html">131</a>. First issue: <a href="first-issue.html">2023 #42</a>. Rest: <a href="september-2026-rest.html">September</a>.</p>
    {related([("../manga/chapter-131.html", "Ch. 131"), ("first-issue.html", "First issue"), ("september-2026-rest.html", "September rest"), ("../manga/publication.html", "Publication")])}
"""),
        ("fun/jump-2026-44.html", "Jump 2026 Issue 44 | Chapter 132’s Return Date",
         "Weekly Shōnen Jump 2026 #44, on sale 28 September 2026, is the announced return for chapter 132. Title not printed here.",
         "Fun · return", "Issue 44", "2026#44",
         "28 September 2026. A date, not a title.",
         f"""
  <p>The official account pointed continuation at Weekly Shōnen Jump 2026 issue 44, on sale 28 September 2026, after the 42/43 combined skip. That is chapter 132’s magazine door. We do not invent the weekly title. File the health notice on <a href="september-2026-rest.html">the September rest</a>.</p>
  <p>Door: <a href="../manga/chapter-132.html">chapter 132</a>. Prior printed word: <a href="../manga/chapter-131.html">Tipping Point</a>.</p>
    {related([("../manga/chapter-132.html", "Ch. 132 door"), ("september-2026-rest.html", "September rest"), ("hiatus.html", "Summer rest"), ("jump-2026-41.html", "Issue 41")])}
"""),
        ("fun/bathhouse-quest.html", "Genichi Sojo’s Bathhouse Quest | Volume Extra",
         "Two-part tankōbon extra: Sōjō Gen’ichi no Ofuro Tanbō. Sojo rates baths. Same curiosity as the scholar.",
         "Fun · extra", "Bathhouse Quest", "お風呂探訪",
         "A serial menace with a hobby. Not a redemption.",
         f"""
  <p>Two parts, packed with the tankōbon: <em>Genichi Sojo’s Bathhouse Quest</em> (<em>Sōjō Gen’ichi no Ofuro Tanbō</em>). Sojo, off the murder clock, rates baths. The oneshots page already holds the long sentence. This room is the extra’s own door so a search does not stop at the crater.</p>
  <p>Index: <a href="oneshots.html">oneshots</a>. Person: <a href="../characters/sojo.html">Sojo</a>. Essay: <a href="../analysis/sojo-fan.html">worst fan</a>.</p>
    {related([("oneshots.html", "Oneshots"), ("../characters/sojo.html", "Sojo"), ("soya-memories.html", "Soya extra"), ("../manga/omake.html", "Omake")])}
"""),
        ("fun/soya-memories.html", "Soya Sazanami’s Memories, Begone! | Volume Extra",
         "Tankōbon extra: Sazanami Sōya no Modoranai de Kioku. The older brother wants memories gone.",
         "Fun · extra", "Memories, Begone!", "戻らないで記憶",
         "Four pages of the clan’s emotional illiteracy as a joke.",
         f"""
  <p><em>Soya Sazanami’s Memories, Begone!</em> is a volume extra. The older brother who treated Hakuri as defective stock gets a gag about memories he would like to misplace. It is not a redemption. The Tou stay the household military. This page is the extra’s door.</p>
  <p>Person: <a href="../characters/soya.html">Soya</a>. House: <a href="../factions/tou.html">the Tou</a>. Index: <a href="oneshots.html">oneshots</a>.</p>
    {related([("../characters/soya.html", "Soya"), ("oneshots.html", "Oneshots"), ("bathhouse-quest.html", "Bathhouse"), ("../factions/sazanami.html", "Sazanami")])}
"""),
        ("fun/pre-serial.html", "Hokazono’s Pre-Serial Shorts | Tezuka to Jump Giga",
         "Before the weekly: Enten (炎天), Farewell! Cherry Boy!, Chain, Madogiwa de Amu, Roku no Meiyaku.",
         "Fun · shorts", "The pre-serial pile", "読切",
         "Tests before Mission. Not Kagurabachi chapters.",
         f"""
  <p>Takeru Hokazono placed <em>Enten</em> (炎天) at the 100th Tezuka Awards, printed in <em>Jump Giga</em> Spring 2021, then a run of Giga and Jump shorts: <em>Farewell! Cherry Boy!</em>, <em>Chain</em>, <em>Madogiwa de Amu</em>, <em>Roku no Meiyaku</em>. People point at <em>Roku no Meiyaku</em> when they say he already knew how to end a short on a debt. These are not weekly Kagurabachi titles. The serial begins 19 September 2023.</p>
  <p>One-shot room: <a href="enten-oneshot.html">炎天</a>. Author: <a href="hokazono.html">Hokazono</a>. First week: <a href="first-issue.html">2023 #42</a>.</p>
    {related([("enten-oneshot.html", "Enten one-shot"), ("hokazono.html", "Hokazono"), ("first-issue.html", "First issue"), ("oneshots.html", "Volume extras")])}
"""),
        ("analysis/insect-camp.html", "The Insect Camp | Magatsumi and Sumika | Kagurabachi Essay",
         "Explainers argue Magatsumi copies Ariu’s insect sorcery. The chapters have not confirmed that. This essay files the camp.",
         "Essay · camp", "The insect camp", "蟲説",
         "A comparison. Not a printed origin.",
         f"""
  <p>After the Irishima talks, explainers treat Magatsumi’s insects as Ariu Mikaboshi’s Sumika recast in steel. The technique catalog already says the chapters have not confirmed that. This essay keeps the camp on a marked page so the catalog does not have to argue. Spider through Bee are printed kit. The copy claim is not.</p>
  <p><a href="../world/insect-kit.html">Insect kit</a>. <a href="../world/sumika.html">Sumika</a>. <a href="../fun/theories.html">Marked theories</a>.</p>
    {related([("../world/insect-kit.html", "Insects"), ("../world/sumika.html", "Sumika"), ("../characters/ariu.html", "Ariu"), ("../fun/theories.html", "Theories")])}
"""),
        ("analysis/two-unnamed.html", "Two Blades Still Blank | Kagurabachi Essay",
         "Two wartime Enchanted Blades have no printed names. The first plate of tamahagane is still work. Do not invent titles.",
         "Essay · catalog", "Two blades still blank", "空白",
         "The encyclopedia’s job is to wait.",
         f"""
  <p>The catalog already admits the hole: two wartime swords unnamed, Subaru a surviving bearer, the first Enchanted Blade still unnamed after chapter 131’s listing. Fan camps argue Magatsumi, Tobimune, Kumeyuri, or Subaru’s steel. This essay does not pick. When Jump prints a title it belongs on the blade index.</p>
  <p><a href="../world/wartime-two.html">Unnamed two</a>. <a href="../world/first-blade.html">First blade</a>. <a href="../fun/theories.html">Camps</a>.</p>
    {related([("../world/wartime-two.html", "Unnamed two"), ("../world/first-blade.html", "First blade"), ("../blades/index.html", "Blades"), ("../world/seventh.html", "Seventh")])}
"""),
        ("analysis/acg-cavalry.html", "The Cavalry Was Six People | Kagurabachi Essay",
         "Anti-Cloud Gouger is the state’s matching piece. Four graves. A commander with a cruel title. Not Hiyuki.",
         "Essay · ACG", "The cavalry was six", "精鋭",
         "A named unit is not the same as a True Realm.",
         f"""
  <p>Chapter 13 titles Elite. The ACG occupy the first book as the government offering a matching piece and watching it fail. Four of six is the thesis Hiyuki later embodies from the other direction: the state has pointed ends, and pointed ends snap. Recaps that say “the Kamunabi fought Sojo” without the six are doing the graves a courtesy.</p>
  <p><a href="../world/acg.html">ACG</a>. <a href="../world/acg-kit.html">Kit</a>. <a href="named-graves.html">Graves</a>.</p>
    {related([("../world/acg.html", "ACG"), ("../world/acg-kit.html", "Kit"), ("../manga/chapter-13.html", "Elite"), ("named-graves.html", "Graves")])}
"""),
        ("analysis/contract-hinge.html", "The Contract as a Hinge | Kagurabachi Essay",
         "Sign a Lifelong Contract and the old art goes dark. Cut the knot and it limps back. Uruha is the clean example.",
         "Essay · contracts", "The contract as a hinge", "契約",
         "Two lists. One signature between them.",
         f"""
  <p>The innate page already says why it sits beside the catalog: a Lifelong Contract is the hinge. Sign, and the old art goes dark. Cut the knot, and it limps back. Uruha’s Crimson Recital waits under Kumeyuri. Shiba will not sign because teleport would go dark. Subaru’s several bodies make a killing-open a nightmare. Magatsumi’s contract is the master key for the other five wartime bearers.</p>
  <p><a href="../world/contracts.html">Contracts</a>. <a href="../world/crimson-recital.html">Koen</a>. <a href="../world/master-key.html">Master key</a>.</p>
    {related([("../world/contracts.html", "Contracts"), ("../world/crimson-recital.html", "Koen"), ("../world/master-key.html", "Master key"), ("../world/innate.html", "Innate")])}
"""),
        ("guide/technique-map.html", "Kagurabachi Technique Map | Blade Kit and Innate Doors",
         "Beginner door to the technique catalog: five printed kits, leftover insects, ACG arts, innate rooms.",
         "Guide · 技", "Technique map", "技図",
         "The catalog is the authority. The rooms are doors.",
         f"""
  <p>Named Enchanted Blade techniques and major innate arts live on the <a href="../world/techniques.html">catalog</a> and the <a href="../world/technique-index.html">index table</a>. This page is the beginner sentence. Enten, Cloud Gouger, Magatsumi, Kumeyuri, Tobimune. Extensions now have rooms. Magatsumi’s insects now have rooms. Two wartime blades stay blank. Unofficial phrases stay marked with an asterisk on the catalog.</p>
  <p>Innate door: <a href="../world/innate.html">innate sorcery</a>. Extensions: <a href="../world/extension-kit.html">extension kit</a>. Insects: <a href="../world/insect-kit.html">insect kit</a>.</p>
    {related([("../world/techniques.html", "Catalog"), ("../world/technique-index.html", "Index"), ("../world/innate.html", "Innate"), ("../guide/blades.html", "Blades guide")])}
"""),
        ("factions/leadership.html", "Kamunabi Leadership Table | Ichiki, Yatsuru, Izaru, Kasen",
         "The Kamunabi heads as a room: Kasen the leak, Ichiki, Yatsuru, Azami, Izaru, Kudo.",
         "Kamunabi · table", "The leadership table", "首脳",
         "A room of surnames. Then a mailed address.",
         f"""
  <p>Leaders include Kasen (director; later the leak), Ichiki, Yatsuru, Azami, Izaru, Kudo. Ichiki trained Shiba and Azami. Azami helps hide Kunishige. Kudo dies for Hakuri. Izaru’s bead chains are the prosecutor kit. Yatsuru sits in the same room. Kasen mailed an address and called it order.</p>
  <p>Org: <a href="kamunabi.html">Kamunabi</a>. Files: <a href="../characters/ichiki.html">Ichiki</a>, <a href="../characters/izaru.html">Izaru</a>, <a href="../characters/yatsuru.html">Yatsuru</a>, <a href="../analysis/leak.html">the leak</a>.</p>
    {related([("kamunabi.html", "Kamunabi"), ("../characters/kasen.html", "Kasen"), ("../world/bead-chains.html", "Bead chains"), ("../analysis/leak.html", "Leak")])}
"""),
        ("world/proxy-overwrite.html", "Magatsumi Proxies | Kyora and Yura | Kagurabachi",
         "Kyora and Yura spend Magatsumi by overwriting, not by Lifelong Contract. The sheathed blade starts becoming Akemura.",
         "Shinuchi · proxy", "Proxies, not bearers", "上書き",
         "Hold the sheathed masterpiece and the body starts to change.",
         f"""
  <p>Akemura is Magatsumi’s bearer. Kyora, then Yura, spend the sword by overwriting, not by contract. Bypass: anyone who holds the sheathed blade starts becoming Akemura. Yura spends at range through spirit left in the blade, then offers the body. This is not Ibuki’s Cloud Gouger sale and not Chihiro’s dying contract.</p>
  <p>Blade: <a href="../blades/magatsumi.html">Magatsumi</a>. Auction: <a href="../characters/kyora.html">Kyora</a>. Leader: <a href="../characters/yura.html">Yura</a>.</p>
    {related([("../blades/magatsumi.html", "Magatsumi"), ("../characters/kyora.html", "Kyora"), ("../characters/yura.html", "Yura"), ("master-key.html", "Master key")])}
"""),
        ("world/charge-delay.html", "Mei’s Charge Delay | Cloud Gouger | Kagurabachi",
         "Mei can charge. A heavy charge disables Mei for about 10–20 seconds until the bearer understands the sword better.",
         "Cloud Gouger · 鳴", "The charge delay", "溜め",
         "The pause is the tell. Cloaked Mei still has it.",
         f"""
  <p>Mei is a lightning bolt. It can charge. A heavy charge disables Mei for about 10–20 seconds until the bearer understands the sword better. Cloaked Mei wears the bolt instead of throwing it; the delay is still the opening. Sojo finds that reading first. Chihiro’s last spend is Mei: Shred, black because the steel is dying.</p>
  <p><a href="mei.html">Mei</a>. <a href="cloaked-mei.html">Cloaked Mei</a>. <a href="mei-shred.html">Mei: Shred</a>.</p>
    {related([("mei.html", "Mei"), ("cloaked-mei.html", "Cloaked Mei"), ("mei-shred.html", "Mei: Shred"), ("../blades/cloud-gouger.html", "Cloud Gouger")])}
"""),
        ("fun/english-trail.html", "English Volumes Trail Japan | About Nine Months",
         "VIZ English tankōbon trail Japanese Jump Comics by about nine months. Volume 9 listed 3 November 2026.",
         "Fun · VIZ", "The English trail", "英巻",
         "A parallel object, not a color-matched set.",
         f"""
  <p>English editions trail Japan by about nine months. VIZ Volume 1 is 5 November 2024. Volume 9 is listed for 3 November 2026. Volumes 10 and 11 English were TBD when the ISBN table was filed. Japanese jackets stay the color study. VIZ trades are a parallel object.</p>
  <p>Table: <a href="../manga/volumes.html">volume guide</a>. Map: <a href="../guide/volume-map.html">volume map</a>. Spines: <a href="volume-spines.html">eleven spines</a>.</p>
    {related([("../manga/volumes.html", "ISBN table"), ("../guide/volume-map.html", "Volume map"), ("../manga/covers.html", "Covers"), ("circulation.html", "Circulation")])}
"""),
        ("analysis/meals-to-quotes.html", "From Meals to Quotation Marks | Kagurabachi Essay",
         "Title language as method: objects and meals, then names, then quotes on the press, then a rank and a place.",
         "Essay · titles", "Meals to quotation marks", "題の旅",
         "The index already told you the present was a prologue.",
         f"""
  <p>Early chapters are objects and meals. Then the swords get names. The auction speaks in architecture. The long book names people, then puts quotation marks on Strongest, Sword Master, Heroes. Part 2 opens on a rank and a place. The titles essay and the collisions room already hold the list. This page is the commute as one sentence.</p>
  <p><a href="titles.html">Titles</a>. <a href="meals.html">Meals</a>. <a href="quotation-marks.html">Quotes</a>. <a href="../world/title-collisions.html">Collisions</a>.</p>
    {related([("titles.html", "Titles"), ("meals.html", "Meals"), ("quotation-marks.html", "Quotes"), ("../fun/chapter-titles.html", "Title desk")])}
"""),
        ("guide/mega-doors.html", "Mega Update Doors | New Rooms on This Wave",
         "A beginner list of the mega update: leftover chapter titles, volume rooms, printed kit, September rest.",
         "Guide · wave", "Mega update doors", "増室",
         "More rooms. Same printed facts. No invented titles.",
         f"""
  <p>This wave adds leftover weekly title rooms through chapter 131, volume rooms for jackets 1–11, printed technique doors (insects, extensions, leftover innate), and the September 2026 rest. Chapters 118–120 stay in the table. Chapter 132 is a date, not a title. The first blade is still unnamed.</p>
  <p>Start: <a href="../manga/chapter-doors.html">chapter rooms</a>, <a href="chapter-map.html">chapter map</a>, <a href="volume-map.html">volume map</a>, <a href="technique-map.html">technique map</a>.</p>
    {related([("../manga/chapter-doors.html", "Chapter rooms"), ("chapter-map.html", "Chapter map"), ("volume-map.html", "Volume map"), ("technique-map.html", "Technique map")])}
"""),
        ("world/level-one.html", "Level 1 | Kamunabi Headquarters | Kagurabachi",
         "The Shigyu brothers punch into Level 1. Azami’s Coin answers. Headquarters as a building with floors.",
         "HQ · Level 1", "Level 1", "一階",
         "A floor number. Then an executioner’s projectile.",
         f"""
  <p>The Shigyu brothers punch into Level 1 of Kamunabi headquarters. Azami’s Coin answers. The building has floors, a barrier, a Vessel. This page files the floor so headquarters is not only a silhouette. Hakuri later Storehouses the Kamunabi vessel out of the split.</p>
  <p>Place: <a href="hq.html">HQ</a>. Coin: <a href="coin.html">Coin</a>. Barrier: <a href="barriers.html">barriers</a>. Brothers: <a href="../characters/shigyu.html">Shigyu</a>.</p>
    {related([("hq.html", "HQ"), ("coin.html", "Coin"), ("../characters/azami.html", "Azami"), ("../characters/shigyu.html", "Shigyu")])}
"""),
        ("media/jump-return.html", "Kagurabachi Magazine Return | 28 September 2026",
         "Official return: Weekly Shōnen Jump 2026 issue 44, on sale 28 September 2026, after the 42/43 health skip.",
         "Media · schedule", "The magazine return", "再開",
         "A printed date from the official account.",
         f"""
  <p>After chapter 131 printed in issue 41, the official account announced the 42/43 combined issue would rest for the author’s sudden illness, with recovery already noted, and pointed continuation at issue 44 (28 September 2026). This is not a leak desk and not a title. Official reading: {VIZ}.</p>
  <p><a href="../fun/september-2026-rest.html">September rest</a>. <a href="../manga/chapter-132.html">Chapter 132 door</a>. <a href="anime.html">Anime</a>.</p>
    {related([("../fun/september-2026-rest.html", "September rest"), ("../manga/chapter-132.html", "Ch. 132 door"), ("../fun/hiatus.html", "Summer rest"), ("../manga/publication.html", "Publication")])}
"""),
        ("world/shoyusha.html", "Sword Bearer (Shoyūsha) | Lifelong Contract Title | Kagurabachi",
         "Sword Bearer, Shoyūsha: anyone on a Lifelong Contract. Volume 10’s jacket word is The Swordsmen.",
         "Contracts · 所有者", "Sword Bearer", "所有者",
         "A job title. The long book is named after killing them.",
         f"""
  <p>Sword Bearer (Shoyūsha) is anyone on a Lifelong Contract. The long book is Sword Bearer Assassination. Volume 10’s jacket is The Swordsmen. The press’s Sword Master is a different word aimed at Akemura. This page keeps the job title next to the press title.</p>
  <p>List: <a href="bearers.html">bearers</a>. Press: <a href="sword-master.html">Sword Master</a>. Contracts: <a href="contracts.html">contracts</a>.</p>
    {related([("bearers.html", "Bearers"), ("sword-master.html", "Sword Master"), ("contracts.html", "Contracts"), ("../arcs/sword-bearer.html", "The long book")])}
"""),
        ("world/bypass-sheath.html", "The Sheathed Bypass | Magatsumi Possession | Kagurabachi",
         "Anyone who holds sheathed Magatsumi starts becoming Akemura. Unique clause. Not a Lifelong Contract.",
         "Magatsumi · sheath", "The sheathed bypass", "鞘",
         "A masterpiece you should not pick up.",
         f"""
  <p>The catalog already states the unique clause: anyone who holds the sheathed blade starts becoming Akemura. Kyora almost becomes someone else at the auction. Yura later offers a body. This is not signing. This is overwrite. Enten’s True Realm is this sword’s death because the household was built as a retraction.</p>
  <p><a href="proxy-overwrite.html">Proxies</a>. <a href="shinuchi.html">Shinuchi</a>. <a href="../analysis/enten-purpose.html">Enten’s purpose</a>.</p>
    {related([("proxy-overwrite.html", "Proxies"), ("shinuchi.html", "Shinuchi"), ("../blades/magatsumi.html", "Magatsumi"), ("../characters/akemura.html", "Akemura")])}
"""),
        ("fun/next-manga.html", "Next Manga Award 2024 | Kagurabachi Print Category",
         "Kagurabachi took the Next Manga Award print category in 2024. Circulation and later nominations sit beside it.",
         "Fun · award", "Next Manga Award", "次にくる",
         "A print-category win in the first long year.",
         f"""
  <p>The publication record already files Next Manga Award, print category, 2024, then later nominations for Shogakukan, Kodansha, and an Eisner international slot. Circulation moved 1 million by October 2024 to 4 million by April 2026. This page is the award door so the count page is not the only search hit.</p>
  <p><a href="../manga/publication.html">Publication</a>. <a href="circulation.html">Circulation</a>. <a href="first-issue.html">First week</a>.</p>
    {related([("../manga/publication.html", "Publication"), ("circulation.html", "Circulation"), ("first-issue.html", "First issue"), ("hokazono.html", "Hokazono")])}
"""),
        ("world/range-resolution.html", "Owl’s Range Versus Resolution | Tobimune | Kagurabachi",
         "Owl trades range for precision: nationwide, only huge spirit sources ping. Pull it closer and the picture sharpens.",
         "Tobimune · 梟", "Range versus resolution", "射程",
         "Hang it high and Japan is a room. Pull it in and it is a picture.",
         f"""
  <p>Owl is two giant owl eyes. Detection range versus precision: hang it high and you hear Enchanted Blade noise across Japan; nationwide, only huge spirit sources ping. Pull it closer and the picture sharpens. After Senkutsuji, Samura hangs Owl over the country. Volume 8’s jacket is a hotel silhouette under that bird.</p>
  <p>Parent: <a href="owl.html">Owl</a>. Essay: <a href="../analysis/owl.html">Owl over Japan</a>. Blade: <a href="../blades/tobimune.html">Tobimune</a>.</p>
    {related([("owl.html", "Owl"), ("../analysis/owl.html", "Essay"), ("crow.html", "Crow"), ("../manga/volume-8.html", "Volume 8")])}
"""),
        ("world/respect-fluency.html", "Play’s Fluency | Respect for the Room | Kagurabachi",
         "Play’s fluency scales with respect for objects. Hiruhiko’s inverse is Destructive Play. Uruha never needed that reading.",
         "Kumeyuri · 遊", "Fluency and respect", "敬意",
         "Move the set. Contempt drops a hotel.",
         f"""
  <p>Play moves nearby objects. Fluency scales with respect for the room. Destructive Play is the same technique spent as demolition because Hiruhiko does not respect objects. Uruha never needed that reading. Samura later takes the steel back. Banquet takes the senses; Play takes the furniture.</p>
  <p><a href="play.html">Play</a>. <a href="destructive-play.html">Destructive Play</a>. Essay: <a href="../analysis/play.html">Play</a>.</p>
    {related([("play.html", "Play"), ("destructive-play.html", "Destructive Play"), ("../analysis/play.html", "Essay"), ("hotel.html", "Hotel")])}
"""),
        ("analysis/seventh-never.html", "Enten Never Registered | Kagurabachi Essay",
         "Six wartime blades on the books. Enten is seventh, post-war, never registered. The count is the argument.",
         "Essay · seventh", "Never registered", "未登録",
         "A retraction, not a trophy, and not in the wartime knot.",
         f"""
  <p>The seventh page already holds the count. Enten is post-war, goldfish and water, made to end the other six, especially Magatsumi. It never sat in Magatsumi’s master-key knot. Kunishige confiscated six and hid. The son’s sword is the apology that was not submitted to a bureau. Part 2 is the kiln before any of that language exists.</p>
  <p><a href="../world/seventh.html">The seventh</a>. <a href="enten-purpose.html">Purpose</a>. <a href="../world/master-key.html">Master key</a>.</p>
    {related([("../world/seventh.html", "Seventh"), ("enten-purpose.html", "Purpose"), ("../blades/enten.html", "Enten"), ("../world/master-key.html", "Master key")])}
"""),
        ("world/hishaku-unnamed.html", "Two Unnamed Hishaku | The Ten | Kagurabachi",
         "Eight Hishaku are named on this site. Two remain unnamed. Sojo is not in the list. He is a customer.",
         "Hishaku · 十", "Two unnamed of the ten", "二欠",
         "The register already says eight. This page is the hole.",
         f"""
  <p>Yura, Hokuto, Hiruhiko, Kuguri, Toto, Yukisada, Uran, Bingo. Eight named. Two still unnamed. Sojo bought Cloud Gouger. Customer, not a member. This page files the hole so a search does not invent the ninth and tenth names. The shared fire-gate is logistics. The ten formed about four years before the present.</p>
  <p>Org: <a href="../factions/hishaku.html">Hishaku</a>. Register: <a href="register.html">names</a>. Essay: <a href="../analysis/sojo-customer.html">customer</a>.</p>
    {related([("../factions/hishaku.html", "Hishaku"), ("register.html", "Register"), ("../analysis/sojo-customer.html", "Customer"), ("fire-gate.html", "Fire-gate")])}
"""),
        ("guide/sunday-legal.html", "Where to Read Kagurabachi Legally | VIZ and MANGA Plus",
         "Same chapter, same week: VIZ Shonen Jump and MANGA Plus. We do not host chapters, raws, or early dumps.",
         "Guide · official", "Read it official", "正規",
         "Chapter 1 is usually free forever on Plus.",
         f"""
  <p>Week-to-week reading is {VIZ}. Same chapter, same week as Weekly Shōnen Jump. Japanese magazine pages live at Shonen Jump’s series page. This encyclopedia does not host chapters, raws, or early Twitter dumps. Chapter 1 is usually free forever on MANGA Plus, which is how the 2023 meme became readers.</p>
  <p>Ritual: <a href="../fun/sunday.html">Sunday</a>. First week: <a href="../fun/first-issue.html">2023 #42</a>. FAQ: <a href="../faq.html#read">where to read</a>.</p>
    {related([("../fun/sunday.html", "Sunday"), ("../faq.html", "FAQ"), ("../manga/publication.html", "Publication"), ("reading-order.html", "Reading order")])}
"""),
    ]

    for rel, title, desc, kicker, h1, jp, lede, body in extras:
        safe_write(rel, title, desc, crumb_for(rel, h1), kicker, h1, jp, lede, body)
    print("wave3 attempted", len(extras))


if __name__ == "__main__":
    main()
