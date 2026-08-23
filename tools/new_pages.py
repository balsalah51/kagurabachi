#!/usr/bin/env python3
"""Write additional lore and fandom pages."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Kagurabachi Archive</title>
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


def write(rel, title, desc, body):
    path = ROOT / rel
    path.write_text(HEAD.format(title=title, desc=desc) + body + FOOT, encoding="utf-8")
    print("wrote", rel)


write(
    "world/glossary.html",
    "Glossary",
    "Kagurabachi terms: Enchanted Blades, Lifelong Contracts, True Realm, Datenseki, Sanso, Malediction.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Glossary</p>
<header class="page-hero"><div>
  <p class="kicker">Reference</p>
  <h1>Glossary<span class="jp">用語</span></h1>
  <p class="lede">The words the book uses, and the English ones the fandom settled on.</p>
</div></header>
<article class="article">
  <p>VIZ and the wiki do not always pick the same rendering. This list follows the names already used on this site. Japanese is given where it helps. Full writeups live on the linked pages.</p>
  <h2>Steel and ore</h2>
  <p><strong><a href="../blades/index.html">Enchanted Blade</a></strong> (妖刀, yōtō) — a katana Kunishige cut from Datenseki. Spirit energy leaves the body as a shape: goldfish, clouds, flowers, feathers. Most have three named techniques. Magatsumi does not keep the three-count.</p>
  <p><strong><a href="datenseki.html">Datenseki</a></strong> — the mineral. Unstable, it pops the user. Kunishige’s eyes were the only known way to make it into a blade instead of a crater. Sojo and Tenri both die trying to fake that.</p>
  <p><strong><a href="contracts.html">Lifelong Contract</a></strong> (Meimetsu Keiyaku) — binds a blade to one nervous system and shuts the bearer’s innate sorcery off. Magatsumi’s contract is the master key: if Akemura dies, the other five wartime bearers die with him.</p>
  <p><strong><a href="../analysis/true-realm.html">True Realm</a></strong> (本領, Honryō) — the blade when the wielder’s intent locks with the steel. Not a transformation. Sojo’s Cloud Gouger “gains slaughter.” Enten’s True Realm is Magatsumi’s death.</p>
  <p><strong>Shinuchi</strong> (真打) — the auction-house and Kamunabi name for <a href="../blades/magatsumi.html">Magatsumi</a>. “Masterpiece.” The listing at the 208th Rakuzaichi.</p>
  <h2>Places and offices</h2>
  <p><strong>Kamunabi</strong> (神奈備) — state sorcerers, rebuilt from the Counter-Sorcery Army. They want the blades under seal. Hiyuki is the pointed end. Kasen, later, is the leak.</p>
  <p><strong>Hishaku</strong> (毘灼) — ten criminal sorcerers. Flame tattoos. Shared fire-gate. They killed Kunishige and stole six blades.</p>
  <p><strong>Sanso</strong> — Kamunabi fortresses where surviving wartime bearers were locked after the raid. The next book starts when one is attacked.</p>
  <p><strong>Storehouse</strong> (蔵, Kura) — the Sazanami subspace. Kyora’s warehouse. Hakuri inherits it and can move people and charged objects across the country.</p>
  <p><strong>Rakuzaichi</strong> (落罪市) — two centuries of auction. The 208th lists Shinuchi. See <a href="../arcs/rakuzaichi.html">the arc</a> and <a href="locations.html">locations</a>.</p>
  <p><strong>Seitei War</strong> — the war over Irishima’s Datenseki. Blades enter at +1 year 5 months. After the treaty, Malediction. See the <a href="index.html">timeline</a>.</p>
  <h2>Arts and crimes</h2>
  <p><strong><a href="iai.html">Iai White Purity Style</a></strong> (居合白禊流) — Itsuo Shirakai’s speed school. Eyes closed. Samura and Uruha are the famous students. Chihiro copies it.</p>
  <p><strong><a href="../analysis/malediction.html">Malediction</a></strong> (Kodoku) — Akemura’s Magatsumi extension after the treaty. About 200,000 civilians. Flowers.</p>
  <p><strong>Flame Bone of the Starving</strong> — Hiyuki’s inherited skeleton. Kamunabi permission slip. See the <a href="../analysis/flame-bone.html">essay</a>.</p>
  <p><strong>Isou</strong> — Sazanami burial-force. Hakuri could not use it until he stopped scattering his own spirit energy.</p>
  <p class="related"><a href="sorcery.html">Sorcery</a><a href="locations.html">Locations</a><a href="../fun/names.html">Names in English</a></p>
</article>
""",
)

write(
    "world/locations.html",
    "Locations",
    "Kagurabachi places: the Rokuhira workshop, Tokyo underworld, Rakuzaichi, Sanso, Senkutsuji, the Kyoto hotel, Irishima.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Locations</p>
<header class="page-hero"><div>
  <p class="kicker">Geography</p>
  <h1>Locations<span class="jp">舞台</span></h1>
  <p class="lede">A modern Japan, an island that should have stayed under the sea, and a few buildings that hold a sword.</p>
</div></header>
<figure class="shot">
  <img src="../assets/panels/ch113.png" alt="Chapter 113 — Irishima / Shokoku">
  <figcaption>Chapter 113 — the island that starts the clock. Full chapter: VIZ / MANGA Plus.</figcaption>
</figure>
<article class="article">
  <h2>The Rokuhira workshop</h2>
  <p>Isolation after the war. A house, a forge, a cellar of swords Kunishige could not smash, a bowl of goldfish. Chihiro grew up here. The Hishaku raid happens here. Enten is forged here, about fifteen years after the Seitei War. The workshop is the book’s moral unit: a household, not a barracks. Every later room is measured against it.</p>
  <h2>Tokyo underworld</h2>
  <p>Where Chihiro and Shiba work for three years after the raid. Cafe Haru Haru is the sit-down between jobs. Char’s sighting, Madoka’s confirmation, Sojo’s compound — the city is the first map. The Anti-Cloud Gouger Special Forces die in it. The Kamunabi want Chihiro out of it. He stays.</p>
  <h2>The Rakuzaichi</h2>
  <p>The Sazanami auction house. Two hundred years. The Tou as household military. The Storehouse as the actual building: a subspace that holds loot and people. The 208th lists Shinuchi. Chihiro lets them take Enten so the blade can scout the Kura on its own charge. On auction day he walks back in with Cloud Gouger’s stump. When the Rakuzaichi ends, the firm ends. See <a href="../arcs/rakuzaichi.html">the arc</a>.</p>
  <h2>Sanso fortresses</h2>
  <p>After the raid, surviving wartime bearers are locked in Kamunabi Sanso. The state’s idea of safety is a box. Uruha is moved; Samura is at Senkutsuji. When a Sanso is attacked, the Sword Bearer Assassination arc starts on a train. The boxes were never going to hold.</p>
  <h2>Senkutsuji</h2>
  <p>The temple where Hakuri returns Tobimune to Samura. Samura clears it, then cuts Uruha down. It looks like a Hishaku pact. It is Suzaku: kill the contract, keep the man. A Buddhist room used as a surgery.</p>
  <h2>Kyoto Bloodshed Hotel</h2>
  <p>The Masumi take Iori here. Chihiro learns Iai by copying Kuguri and the house style. Iori’s seal breaks. Hiruhiko wrecks the hotel with Play. Samura arrives. Feathers, banquet, goldfish. The hotel is where the daughter and the father occupy the same city again.</p>
  <h2>Kamunabi headquarters</h2>
  <p>Tokyo. Magatsumi in the basement. Kasen’s leak on the table. Kudo dies for Hakuri. Yura spends Shinuchi without drawing it. Shiba dumps the fight onto the street. <span class="spoiler">Akemura leaves the cell in Yura’s offered body. The building that hid the Sword Master is the building that loses him.</span></p>
  <h2>Irishima and Shokoku</h2>
  <p>Shokoku rises from the sea. Irishima already showed a Datenseki vein. Japan harvests it. The Mikaboshi come back. The Irishima talks are Part 2’s opening property: Chiaki, Shiba as Soga guardian, Kunishige still a picky dealer who has not looked at the ore. English Twitter called the chapter 113 splash “Japan’s Atlantis.” The <a href="index.html">timeline</a> holds the dates.</p>
  <p class="related"><a href="glossary.html">Glossary</a><a href="../arcs/seitei-war.html">Seitei War</a><a href="../factions/index.html">Factions</a></p>
</article>
""",
)

write(
    "world/contracts.html",
    "Lifelong Contracts",
    "How Kagurabachi Lifelong Contracts bind Enchanted Blades, shut innate sorcery, and why Magatsumi is the master key.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Contracts</p>
<header class="page-hero"><div>
  <p class="kicker">System</p>
  <h1>Lifelong Contracts<span class="jp">盟滅契約</span></h1>
  <p class="lede">A blade on one nervous system. The old art goes dark until someone cuts the knot.</p>
</div></header>
<article class="article">
  <p>A Lifelong Contract (Meimetsu Keiyaku) is how an Enchanted Blade stops being a tool you put down. It binds the steel to one body. The bearer’s innate sorcery — teleport, Flame Bone, Isou, whatever they were — shuts off for the duration. The sword is now the only language those nerves speak.</p>
  <p>That is why Shiba never signs one. Teleportation is the practical magic of the series; a contract would take the exit away. Hiyuki’s Flame Bone is inherited, not a blade contract, which is why she can stand next to Enchanted Blades without becoming their employee. Hakuri’s Storehouse is clan sorcery. The people who pick up Kunishige’s wartime six give those arts away.</p>
  <h2>How a contract opens</h2>
  <p>Kill the bearer. The Hishaku spent three years on that plan. Hokuto murders Ibuki Misaka so Cloud Gouger can go to a customer. After Sojo dies, Chihiro briefly contracts the dying sword and spends its last Mei at the Rakuzaichi. A dead blade can still hold a few charges. It is not a new life. It is a leftover.</p>
  <p>Samura’s specialty is the other door: cut the contract without cutting the person. What he does to Uruha looks like murder. It is Suzaku used as surgery — kill the knot, keep the man. That is why the Hishaku pact was never the whole file. See <a href="../characters/samura.html">Samura</a> and <a href="../blades/tobimune.html">Tobimune</a>.</p>
  <h2>The Magatsumi knot</h2>
  <p>Magatsumi’s contract is the master key. If <a href="../characters/akemura.html">Akemura</a> dies, the other five wartime bearers die with him. Destroy Magatsumi and the knot comes apart. That is why nobody simply executes the Sword Master in the basement, and why Enten’s True Realm is not “beat the uncle.” It is the death of the blade that holds the others hostage.</p>
  <p>Anyone who holds sheathed Magatsumi starts becoming Akemura. Kyora, dying, looks through the auctioneer’s eyes and sees the Master. Yura spends Shinuchi at range, then offers a body. The contract does not care about your job title. See <a href="../blades/magatsumi.html">Magatsumi</a>.</p>
  <h2>Enten</h2>
  <p>Enten is still a Lifelong Contract. Chihiro’s innate art, such as it is, is the household: watching, copying, the goldfish. The contract does not shut a famous sorcery off because he never had one on the books. Nishiki’s resistance to other-blade ailments is the brief made visible — a contract written as a counter, not as a national weapon. <span class="spoiler">When Magatsumi bisects Enten, the pieces stay with Chihiro. Suzaku-black stalls the rot. He starts notes for a new Enten like a smith again.</span></p>
  <p class="related"><a href="sorcery.html">Sorcery</a><a href="../analysis/true-realm.html">True Realm</a><a href="../blades/index.html">Blades</a></p>
</article>
""",
)

write(
    "world/iai.html",
    "Iai White Purity Style",
    "Iai White Purity Style in Kagurabachi: Shirakai’s school, Samura, Uruha, Iori, and Chihiro copying it.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Iai White Purity</p>
<header class="page-hero"><div>
  <p class="kicker">School</p>
  <h1>Iai White Purity Style<span class="jp">居合白禊流</span></h1>
  <p class="lede">Eyes closed. One cut. No extra motion. Mocked until it killed the mockers.</p>
</div></header>
<article class="article">
  <p>Itsuo Shirakai’s speed school. The curriculum is not theater. You close your eyes so the rest of the body has to get honest. Samura took that further and took the eyes themselves. Uruha is the other famous student — prodigy, loyal to the Rokuhira name, Kumeyuri in his hand. Kiri Shirakai wants to behead the founder for saying women cannot. The school is an argument the family is still having.</p>
  <h2>Who uses it</h2>
  <p><a href="../characters/samura.html">Seiichi Samura</a> is the weather the other bearers treat as given. Sheathed, by sound, faster than the plot wants to draw. Iai as ethics: one cut, no extra motion. What he does to Uruha is that ethic used as mercy. What he does at the end of Part 1 is the same sentence spent on Magatsumi.</p>
  <p><a href="../characters/uruha.html">Yoji Uruha</a> learned the school and kept a different loyalty — to Kunishige’s name, not to the Kamunabi box. <a href="../characters/iori.html">Iori</a> is Samura’s daughter. Memory-sealed, then unsealed at the Kyoto hotel. She copies the house style because it is the house. <span class="spoiler">Tobimune passes to her.</span></p>
  <p><a href="../characters/chihiro.html">Chihiro</a> is not a student. He is a watcher. He fakes Iai after seeing Uruha, Samura, Iori, Kuguri. The book’s joke is that a smith’s son can steal a closed-eye school by looking. That is also the theme: Enten was never only inherited. It was learned in a workshop, then again in other people’s rooms.</p>
  <h2>On the page</h2>
  <p>Chapter 70 puts the name on a title. The Kyoto Bloodshed Hotel is the classroom: Chihiro copies Kuguri and the house while Hiruhiko wrecks the building with Play. Samura versus Chihiro in chapter 83 is Iai against goldfish — pace against purpose. Chihiro wins the argument, not the clock.</p>
  <p>The fandom likes to call it “the iaijutsu school” and stop. The useful part is the eyes. A blind man built a style that does not need them. A sighted boy copies it anyway. A daughter has the seal broken and finds the curriculum was her father’s apology. See <a href="sorcery.html">sorcery</a> for how a Lifelong Contract sits next to a school that is not Datenseki.</p>
  <p class="related"><a href="../characters/samura.html">Samura</a><a href="../characters/iori.html">Iori</a><a href="../arcs/sword-bearer.html">Sword Bearer</a></p>
</article>
""",
)

write(
    "analysis/true-realm.html",
    "True Realm",
    "True Realm (Honryō) in Kagurabachi: not a transformation. The blade when the wielder finally means it.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Analysis</a> / True Realm</p>
<header class="page-hero"><div>
  <p class="kicker">Essay</p>
  <h1>True Realm<span class="jp">本領</span></h1>
  <p class="lede">Not a Super Saiyan form. The brief, said with the whole nervous system.</p>
</div></header>
<figure class="shot">
  <img src="../assets/panels/ch014.png" alt="Chapter 14 — True Realm">
  <figcaption>Chapter 14 — Honryō enters the vocabulary. Full chapter: VIZ / MANGA Plus.</figcaption>
</figure>
<article class="article">
  <p>Chapter 14 puts the word on the page. English readers still treat True Realm as a gauge: when do we get the glow? Weekend Weebs on chapter 83 is the useful correction. Honryō is not a transformation. It is what happens when the wielder’s intent locks with the Datenseki. The sword becomes the autobiography.</p>
  <p>Sojo wants Cloud Gouger to “gain slaughter” and is delighted when it does. That is True Realm as a customer review. The weather kit was always able to kill. The lock is him admitting that killing is the product. Enten’s True Realm is Magatsumi’s death. Chihiro reaches it first in the compound — not because he is louder, because he means the cut. A wartime blade sold as immortal is shown to be mortal. Volume 2 is titled for that argument.</p>
  <p>Akemura invents Malediction after the treaty because the desire finished crystallizing. The war was over. The island still existed. Magatsumi had no three-technique limit to hide behind. Kodoku is True Realm as policy: a field the size of a nation, filed as victory. See <a href="malediction.html">The Malediction</a>.</p>
  <p>Samura’s Suzaku is the other end of the same idea. A support blade taught to raise the dead, then taught to go black. <span class="spoiler">When he spends the last of his life on Magatsumi, the fire is no longer a heal. It is the brief: keep the boy in the corridor.</span> Extensions — cloaked Mei, Kuro: Shred, Mei: Shred, Suzaku-black — are True Realm leaking into the technique list. “Dark power” in this book is a dying or desperate blade telling the truth louder.</p>
  <p>The YouTube camp that treats Honryō as a power-up will keep being wrong in the same way the koi essays are wrong. The page already told you. Intent. Mortality. Datenseki. Agree. The <a href="../media/index.html">theory desk</a> files the useful chapter-83 writeup next to the goldfish-as-language video. This essay is the site’s version: True Realm is the household or the factory, depending on who is holding the steel.</p>
  <p class="related"><a href="enten-purpose.html">Enten’s purpose</a><a href="../world/contracts.html">Contracts</a><a href="../world/sorcery.html">Sorcery</a></p>
</article>
""",
)

write(
    "fun/names.html",
    "Names in English",
    "How Kagurabachi names land in English: Enten, Cloud Gouger, Magatsumi, Shinuchi, Kamunabi, Hishaku.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Names</p>
<header class="page-hero"><div>
  <p class="kicker">Translation</p>
  <h1>Names in English<span class="jp">英訳の名前</span></h1>
  <p class="lede">VIZ, the wiki, and the comments section do not always pick the same sword.</p>
</div></header>
<article class="article">
  <p>This site follows the English renderings already in the articles. Japanese sits next to them when the kanji is doing work. We are not a localization desk. We are a concordance so “Kuregumo” and “Cloud Gouger” do not become two characters.</p>
  <h2>The blades</h2>
  <p><strong>Enten</strong> (淵天) — VIZ keeps Enten. The kanji is abyss / heaven; the joke is a bowl of fish, not a cosmic title. Fandom sometimes writes En-Ten. We do not.</p>
  <p><strong>Cloud Gouger</strong> (刳雲, Kuregumo) — VIZ’s English is the one on the volume 2 jacket. Japanese readers and a lot of English comments still say Kuregumo. Both appear on this site, Cloud Gouger first.</p>
  <p><strong>Magatsumi</strong> (勾罪) — the blade’s name. <strong>Shinuchi</strong> (真打) is the masterpiece title, the auction listing, the word the Kamunabi use when they mean the thing in the basement. Using only Shinuchi hides that it has a name the Sword Master gave it.</p>
  <p><strong>Kumeyuri</strong> (酌揺) and <strong>Tobimune</strong> (飛宗) — VIZ keeps the Japanese. Two wartime blades remain unnamed in the printed chapters. This archive will not invent them.</p>
  <h2>People and offices</h2>
  <p><strong>Chihiro Rokuhira</strong> (六平 千鉱) — family name first in Japanese. We write given name first, Japanese in the heading. Same for Kunishige, Hakuri Sazanami, Seiichi Samura, Yoji Uruha, Hiyuki Kagari, Akemura Soga, Togo Shiba, Genichi Sojo.</p>
  <p><strong>Kamunabi</strong> (神奈備) and <strong>Hishaku</strong> (毘灼) — left in Japanese. Early fan translations tried “Shrine Force” and worse. The official English kept the names. <strong>Rakuzaichi</strong> (落罪市) is the auction; “fallen-sin market” is a gloss, not a title.</p>
  <p><strong>True Realm</strong> (本領, Honryō) — VIZ’s phrase. We use it, and Honryō once so the chapter-14 page is findable. <strong>Malediction</strong> (Kodoku) — the English for Akemura’s extension; Kodoku stays in parentheses because the Japanese is the technique’s actual file name on this site.</p>
  <p><strong>Iai White Purity Style</strong> (居合白禊流) — VIZ’s long English. The fandom shortens it to “Iai.” Both are fine; the page title is the long one.</p>
  <h2>What we do not do</h2>
  <p>We do not “correct” VIZ mid-sentence. We do not pretend a scan group’s first-week guess is canon. If a later official volume changes a chapter title, the <a href="../manga/chapters.html">chapter index</a> is the authority. Name essays that exist only to fight about “Mr. Savage” energy — see Kanzenshuu’s Dragon Ball files — are someone else’s Sunday. Ours is: goldfish, not koi, and Cloud Gouger when the jacket says Cloud Gouger.</p>
  <p class="related"><a href="../world/glossary.html">Glossary</a><a href="goldfish.html">Goldfish</a><a href="../manga/chapters.html">Chapters</a></p>
</article>
""",
)

write(
    "fun/fandom.html",
    "The English fandom",
    "Kagurabachi fandom after the 2023 meme: Sunday Jump, theories, #BachiAnime, and what people actually argue about.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Fandom</p>
<header class="page-hero"><div>
  <p class="kicker">Readers</p>
  <h1>The English fandom<span class="jp">英語圏の読者</span></h1>
  <p class="lede">A hashtag that had to become a reading group. Then an anime tag.</p>
</div></header>
<article class="article">
  <figure class="shot">
    <img src="../assets/covers/teaser-og.jpg" alt="Official teaser visual">
    <figcaption>The teaser that English Twitter hired as a career. © Project Kagurabachi.</figcaption>
  </figure>
  <p>The <a href="meme.html">meme page</a> is the 2023 origin: ironic Big Three posts, then 99 million Manga Plus views. This page is what the room does now. Sunday still lives under one tag. The legal way to be there is VIZ or MANGA Plus the day Jump drops. The <a href="sunday.html">Sunday ritual</a> is the how. Leaks are not a desk we keep.</p>
  <h2>What people argue</h2>
  <p>Craft versus prediction. Goldfish-as-language (correct about Kuro / Aka / Nishiki, wrong about carp). True Realm as the wielder, not a gauge. Sojo as Kunishige’s worst reader. Enten as a retraction. Those hold up against the printed pages and have essays here.</p>
  <p>Camps: Cour 1 ends at the elevator (chapter 60’s doors — not confirmed). Reforge Enten versus a new named blade. The Seitei War flashback has to be long enough — do not Skypeia it. Ariu as Magatsumi’s original. Those live on the <a href="../media/index.html">theory desk</a> as arguments, not answers.</p>
  <h2>Desks worth keeping</h2>
  <p>ANN on Anime NYC — Hokazono in a stuffed room that was not billed as a main event. Asahi on the fins and the Hollywood-Japan crush. Weekend Weebs on chapter 83. ComicBook picking up the goldfish translation from <a href="https://x.com/brkagurabachi">@brkagurabachi</a>. The useful split is: interview and chapter, or leak thumbnail. Only the first kind gets a card.</p>
  <p>Official tags now include <a href="https://x.com/hashtag/BachiAnime">#BachiAnime</a>. <a href="https://x.com/kb_anime_jp">@kb_anime_jp</a> and <a href="https://x.com/kb_anime_en">@kb_anime_en</a> are the studio’s voices. The 2023 posts did not plan an April 2027 Cypic show. The pages did. See <a href="../media/anime.html">the anime page</a>.</p>
  <h2>How this archive sits in it</h2>
  <p>Wiki-depth articles, a Kanzenshuu-style manga guide, cover studies, long essays. We do not host chapters. We do not rank “correct” theories. We do not invent names for the two unnamed wartime blades. If you are sending the book to someone who only knows the hashtag, send <a href="first-read.html">first-read notes</a> and chapter 1 on MANGA Plus, not a “generational” compilation.</p>
  <p>Circulation passed 4 million by April 2026. Next Manga Award 2024 (print). The fandom’s job now is the same as Chihiro’s: stop treating the work as a trophy. Read it.</p>
  <p class="related"><a href="meme.html">Meme to flagship</a><a href="sunday.html">Sunday</a><a href="../media/index.html">Theories</a></p>
</article>
""",
)

write(
    "media/anime.html",
    "The anime",
    "Kagurabachi anime: Cypic, Tetsuya Takeuchi, Keigo Sasaki, April 2027, Crunchyroll, and the announced cast.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Theories</a> / Anime</p>
<header class="page-hero"><div>
  <p class="kicker">April 2027</p>
  <h1>The anime<span class="jp">アニメ</span></h1>
  <p class="lede">Cypic. Tetsuya Takeuchi. Three goldfish still on the teaser.</p>
</div></header>
<article class="article">
  <div class="video"><iframe src="https://www.youtube.com/embed/Ppmbg4IoL3g" title="Kagurabachi teaser PV" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
  <p class="credit">Official teaser. © Project Kagurabachi.</p>
  <p>Television series from Cypic, directed by Tetsuya Takeuchi, character designs by Keigo Sasaki. Scheduled for April 2027. Crunchyroll outside Japan, with the usual listed exceptions. Official site: <a href="https://anime.kagurabachi.jp/">anime.kagurabachi.jp</a>. Accounts: <a href="https://x.com/kb_anime_jp">@kb_anime_jp</a>, <a href="https://x.com/kb_anime_en">@kb_anime_en</a>. The tag is <a href="https://x.com/hashtag/BachiAnime">#BachiAnime</a>.</p>
  <h2>What is confirmed</h2>
  <p>The first twenty minutes toured from July 2026 — Anime Expo, Japan Expo, AnimagiC, Anime NYC — before the broadcast. A ticket and a memory unless a booklet ships; the <a href="../collectibles/index.html">collectibles</a> page will log an SKU if one appears. Cour length and adaptation stopping point are not confirmed. The YouTube camp that ends season 1 on chapter 60’s elevator is a camp. Takeuchi / Sasaki / Cypic are facts.</p>
  <h2>Voices announced so far</h2>
  <ul>
    <li><a href="../characters/chihiro.html">Chihiro Rokuhira</a> — Taihi Kimura (anime); Shoya Ishige (voiced comic)</li>
    <li><a href="../characters/kunishige.html">Kunishige Rokuhira</a> — Tomokazu Seki (anime); Kenta Fujimaki (voiced comic)</li>
    <li><a href="../characters/shiba.html">Togo Shiba</a> — Katsuyuki Konishi (anime); Jun Fukushima (voiced comic)</li>
  </ul>
  <p>Character trailers sit on the <a href="index.html">theory desk</a> next to the teaser. More cast will land closer to 2027. This page will not invent them.</p>
  <h2>What the teaser sells</h2>
  <p>Black coat. White type. Three fish. Hokazono’s palette from volume 1 — white, black, blood red, Enten gold — is the one the studio inherited. The fandom that showed up for a 2023 meme is now a room that has to sit through a Sunday-night slot. The book already taught the difference between a trophy and a household. The anime’s job is the same cut.</p>
  <p class="related"><a href="index.html">Theories &amp; video</a><a href="../fun/fandom.html">English fandom</a><a href="../collectibles/index.html">Collectibles</a></p>
</article>
""",
)

write(
    "characters/chiaki.html",
    "Chiaki Soga",
    "Chiaki Soga: Chihiro’s mother, Princess Soga, foresight as inherited proof of Izanami.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Chiaki Soga</p>
<header class="page-hero"><div>
  <p class="kicker">Soga clan · Chihiro’s mother</p>
  <h1>Chiaki Soga<span class="jp">曽我 千晃</span></h1>
  <p class="lede">Princess Soga. Foresight as the clan’s warrant. The woman Part 2 puts back on Irishima before the ore had a smith.</p>
</div></header>
<div class="layout">
  <article class="article">
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="Chapter 113 — the island">
      <figcaption>Chapter 113 — the war that made her household national. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <h2>Overview</h2>
    <p>Chiaki is Kunishige’s partner and Chihiro’s mother. She is Chiaki Soga — younger sister of the man the present tense calls the Sword Master only after you learn the uncle’s name. The Soga were mainland prophecy aristocracy. Her foresight is the clan’s warrant, talked about as inherited proof of Izanami. Part 2 opens on her, on the Irishima talks, on a household that is not yet a cover-up.</p>
    <p>The present-day book spends a long time pretending the workshop was a father and a son and a bowl of fish. It was. It was also a Soga door. Shiba guarded that door before the war. Akemura is her younger brother. When he empties the island, the hiding that follows is her family’s crime as much as Kunishige’s steel.</p>
    <h2>Story role</h2>
    <p>In Part 1 she is absence and inheritance: the maternal line that makes Akemura Chihiro’s uncle, the reason Enten’s target is not a stranger. Chapter 123 is titled Chiaki. The Irishima talks (116–121) are the room she occupies while Kunishige is still a picky weapons dealer who has not looked at the ore. Mashiro is still alive. Shiba is still a Soga guardian.</p>
    <p>This page will grow as Jump prints the smelting chapters. Until then the <a href="../arcs/seitei-war.html">Seitei War arc</a> and the <a href="../world/index.html">timeline</a> hold what the present already told us. We will not invent a personality the flashback has not given her yet.</p>
    <h2>Relationships</h2>
    <p><a href="kunishige.html">Kunishige</a> is the partner. <a href="chihiro.html">Chihiro</a> is the son who inherits a seventh blade and, later, an uncle. <a href="akemura.html">Akemura</a> is her younger brother — patriot, Magatsumi, Malediction. <a href="shiba.html">Shiba</a> stood in the Soga doorway before Cafe Haru Haru existed.</p>
    <p class="related"><a href="../arcs/seitei-war.html">Seitei War</a><a href="../factions/index.html">Soga</a><a href="akemura.html">Akemura</a></p>
  </article>
  <aside class="infobox">
    <div class="infobox-head"><h2>Chiaki Soga</h2><span class="jp">曽我 千晃</span></div>
    <div class="portrait p-akemura"><img src="../assets/panels/ch113.png" alt="The island that makes the Soga national.">
      <div class="portrait-caption">The island that makes the Soga national.</div>
    </div>
    <dl><dt>Clan</dt><dd>Soga (Princess Soga)</dd><dt>Art</dt><dd>Foresight (clan warrant)</dd><dt>Family</dt><dd><a href="kunishige.html">Kunishige</a> (partner); <a href="chihiro.html">Chihiro</a> (son); <a href="akemura.html">Akemura</a> (younger brother)</dd><dt>Appears</dt><dd>Part 2 · Irishima talks; ch. 123</dd></dl>
  </aside>
</div>
""",
)

write(
    "characters/azami.html",
    "Azami",
    "Azami of the Kamunabi: trained with Shiba, hid Kunishige, warned Chihiro off Sojo.",
    """<p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Azami</p>
<header class="page-hero"><div>
  <p class="kicker">Kamunabi</p>
  <h1>Azami<span class="jp">アザミ</span></h1>
  <p class="lede">The friend who stayed inside the building. Coin. A warning Chihiro did not take.</p>
</div></header>
<div class="layout">
  <article class="article">
    <h2>Overview</h2>
    <p>Azami trained under Ichiki with Togo Shiba. When the island rose they were both in the bureau. When Kunishige disappeared, Azami stayed and helped hide the smith. Shiba walked away. That fork is the whole character: the Kamunabi as a place a decent person can still occupy, and a place that later leaks the address anyway.</p>
    <p>In the present he is one of the first official faces Chihiro meets. He wants the boy away from Sojo. Chihiro stays. Azami’s Coin is the innate art on the <a href="../world/sorcery.html">sorcery</a> list — small, practical, the opposite of a national skeleton. He is not Hiyuki. He is not Kasen. He is the man who still remembers Kunishige as a person and cannot make the son stand down.</p>
    <h2>Story role</h2>
    <p>Vs. Sojo: Char’s sighting has already happened. Azami is the Kamunabi warning. The Anti-Cloud Gouger Special Forces are the state’s other offer — six people, four dead. Azami’s version is “do not go.” Both fail to move Chihiro. Both are the book teaching you the government arrives late.</p>
    <p>He remains in the building through the auction and the long assassination arc. Kasen’s leak makes every loyal officer look, in hindsight, like someone who stayed in a room that was already sold. Azami hid the smith with Shiba. He did not leak the house. The tragedy is that the house was leaked anyway, from a desk above him.</p>
    <h2>Relationships</h2>
    <p><a href="shiba.html">Shiba</a> is the classmate who left. Ichiki is the teacher who sits among the leaders. <a href="kunishige.html">Kunishige</a> is the friend they hid. <a href="chihiro.html">Chihiro</a> is the warning that did not take. <a href="hiyuki.html">Hiyuki</a> is the pointed end of the same letterhead.</p>
    <p class="related"><a href="../factions/index.html">Kamunabi</a><a href="shiba.html">Shiba</a><a href="../arcs/vs-sojo.html">Vs. Sojo</a></p>
  </article>
  <aside class="infobox">
    <div class="infobox-head"><h2>Azami</h2><span class="jp">アザミ</span></div>
    <div class="portrait p-azami"><img src="../assets/portraits/azami.webp" alt="Manga portrait — Azami.">
      <div class="portrait-caption">Manga portrait — Azami.</div>
    </div>
    <dl><dt>Affiliation</dt><dd>Kamunabi</dd><dt>Sorcery</dt><dd>Coin</dd><dt>Trained</dt><dd>Under Ichiki, with Shiba</dd><dt>Role</dt><dd>Hid Kunishige; warned Chihiro off Sojo</dd></dl>
  </aside>
</div>
""",
)

print("character pages ok")


