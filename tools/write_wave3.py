#!/usr/bin/env python3
"""Write the Sep 2026 encyclopedia wave: chapter close readings and Part 2 rooms."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
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
    "manga/chapter-18.html",
    "Kagurabachi Chapter 18 “Roar” | Close Reading",
    "Close reading of Kagurabachi chapter 18, Roar: Enten cuts Cloud Gouger, Sojo spends the ore, and the first wartime blade dies.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter 18</p>
    <header class="page-hero"><div>
      <p class="kicker">Volume 2 closer</p>
      <h1>Chapter 18 - “Roar”<span class="jp">轟く</span></h1>
      <p class="lede">A wartime sword learns it can die. A customer chooses the crater. The boy who would not spend Char keeps the pieces.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch018.png" alt="Chapter 18: Roar">
      <figcaption>The first Enchanted Blade the present tense is allowed to bury. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>Read it official: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> or <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. This page is a close reading, not a substitute. Volume 2 takes its English title from the duel this issue finishes: <em>Enten vs. Cloud Gouger</em>. The <a href="../arcs/vs-sojo.html">Vs. Sojo arc</a> is the longer commute. Chapter 18 is the stamp at the end of the ticket.</p>

      <h2>The cut</h2>
      <p>Chihiro has already lost an arm. The Anti-Cloud Gouger Special Forces have already spent four of six. True Realm entered the vocabulary in chapter 14. What “Roar” files is the correction the war jackets never printed: <a href="../blades/enten.html">Enten</a> can cut <a href="../blades/cloud-gouger.html">Cloud Gouger</a> in half. Kunishige’s wartime steel was sold as immortal. The seventh blade, never on the Kamunabi’s books, is the first one to prove the other six are objects.</p>
      <p>Sojo wanted Cloud Gouger to “gain slaughter.” It did. That is what True Realm is when the wielder finally means it. Enten’s meaning in the same room is smaller and harder: a household object asked to unmake a weapon. Goldfish in the cut. The weather stops being weather.</p>

      <h2>The crater</h2>
      <p>Sojo will not walk out a quiet failure. He fuses with unstable Datenseki rather than admit Kyonagi cells were never Kunishige’s eyes. The compound goes with him. The book has already taught you the mineral pops the user. Chapter 18 is the customer choosing that sentence as a last technique.</p>
      <p>He is not Hishaku. He is a sale. <a href="../characters/yura.html">Yura</a> needed a monster who would love the work and never meet the house. <a href="../analysis/sojo-fan.html">The worst-fan essay</a> is the longer version. “Roar” is the version that fits in a last issue of Volume 2: enough crater to make the rule legible, not enough to make the ten a cast list.</p>

      <h2>What leaves the building</h2>
      <ul>
        <li><strong>Cloud Gouger’s pieces</strong> - still charged enough to spend later. Chihiro keeps them. The Rakuzaichi will ask him to.</li>
        <li><strong>Char</strong> - alive, which is the whole difference between this protagonist and every adult who touched a blade in the war. File: <a href="../characters/char.html">Char</a>.</li>
        <li><strong>The state’s receipt</strong> - six specialists, four graves, a commander without legs, a specialist without an arm. Elite is a job title. <a href="../world/acg.html">Anti-Cloud Gouger</a>.</li>
        <li><strong>The public count, already wrong</strong> - six wartime blades. One is now a pair of fragments in a boy’s bag. The seventh still does not exist on paper.</li>
      </ul>

      <h2>Where the roar sends you</h2>
      <p>Chapter 19 is “Knight of Darkness.” Hiyuki arrives as the Kamunabi’s pointed end. The auction is already being built. Reading order: <a href="../guide/reading-order.html">how to read</a>. The first issue’s furniture: <a href="chapter-1.html">chapter 1</a>.</p>
    </article>
""",
)

write(
    "manga/chapter-115.html",
    "Kagurabachi Chapter 115 “Swordsmith” | Close Reading",
    "Close reading of Kagurabachi chapter 115, Swordsmith: Enten in pieces, Samura spent, Iori with Tobimune, and Part 1’s last present-tense page.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter 115</p>
    <header class="page-hero"><div>
      <p class="kicker">Part 1 closer</p>
      <h1>Chapter 115 - “Swordsmith”<span class="jp">刀匠</span></h1>
      <p class="lede">The present tense ends on a job title. The boy who hunted blades has to think like the man who made them.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/enten.webp" alt="Enten">
      <figcaption>The seventh blade, already asked to do the work it was forged for. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>Read it official: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> or <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. This page is a close reading, not a substitute. Part 1 runs chapters 1 through 115. “Swordsmith” is the last present-tense issue. Volume 12 (4 September 2026, ISBN 978-4-08-885177-8) is expected to collect the Karma-through-Swordsmith corridor and then open the war book. The <a href="../guide/part-1.html">Part 1 long cut</a> is the commute. This page is the stamp.</p>

      <h2>What the title is doing</h2>
      <p>The long book spent chapters putting quotation marks on the press’s words: “Strongest,” “Sword Master,” “Heroes.” Chapter 115 drops the quotes. 刀匠 is a civilian job. Kunishige’s job. The son who spent a hundred issues retrieving steel is being handed the only work that ever made the steel mean something other than a raid.</p>
      <p>Enten was forged as a retraction, not a seventh trophy. Its True Realm is Magatsumi’s death. <span class="spoiler">The issue leaves Enten bisected. The counter-blade has already spent itself on the thing it was for. Chihiro is writing notes toward a new Enten. The workshop ethics from chapter 1 are back on the table as homework, not furniture.</span></p>

      <h2>The people the present tense leaves standing</h2>
      <p><span class="spoiler">Samura is spent. Iori is holding Tobimune. Owl over Japan is now a girl with her father’s support blade and a country that still needs a room. Akemura is loose in the Kamunabi, in a body that used to be Yura. The Sword Master does not need the auction house anymore. He has a building.</span></p>
      <p>The <a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a> arc is the long book that made those sentences possible: Uruha, Samura, Iori, Kasen’s leak, Yura offering Akemura a body. “Swordsmith” does not recap them. It files them as the reason the next page cannot stay in October.</p>

      <h2>The page turn</h2>
      <p>Chapter 116 is “Princess.” Chihiro has not been born yet on that page. Enten does not exist. The kiln is still a proposal. Part 2 is not a clip show of the war jackets. It is the room where the sins are still being smelted. Guide: <a href="../guide/part-2.html">Part 2, the forge door</a>. Magazine run: <a href="part-2.html">Part 2 page</a>.</p>
      <p>The present-tense aftermath is paused, not cancelled. When Jump cuts back, the catalog will say so. Until then the son is a smith in the only sense the first issue respected: a person who has to decide what a blade is for before he swings it.</p>
    </article>
""",
)

write(
    "manga/chapter-129.html",
    "Kagurabachi Chapter 129 “Ironworks” | Close Reading",
    "Close reading of Kagurabachi chapter 129, Ironworks: Kunishige in the fire, Chiaki as the reason the eyes stay open, and the first blade still unfinished.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter 129</p>
    <header class="page-hero"><div>
      <p class="kicker">23 August 2026</p>
      <h1>Chapter 129 - “Ironworks”<span class="jp">製鉄 肆</span></h1>
      <p class="lede">The kiln is not a montage. It is a man at the edge of a process, and a princess who arrives as the reason to keep looking.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="Chapter 113: the island that makes the kiln national">
      <figcaption>The island that started the clock. Chapter 129 is the clock counted in workshop hours. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>Read it official: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> or <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. This page is a close reading, not a substitute. Jump printed “Ironworks” on 23 August 2026 after an announced rest. 125 “Smelting,” 126 “Fire,” 127 and 128 as 製鉄 弐 and 参: the archive’s smithing manual. 129 is 製鉄 肆, the fourth plate. The <a href="part-2.html">Part 2 page</a> writes the uncollected run in sentences. <a href="../world/smelting.html">Smelting</a> is the mineral argument in one room.</p>

      <h2>The fire first</h2>
      <p>Kunishige is at the edge of the process. Unstable Datenseki pops the user. His eyes are the only printed way to make the mineral into a blade instead of a crater. Hokazono talked to a real swordsmith so these pages would not be cosplay. “Ironworks” is that homework on fire: labor, failure, heat, a shop that might go with the ore.</p>
      <p>Flashback inside the flashback. Chiaki has become Princess Soga. Distance opens. Shiba tells him not to lose hope. The worst days arrive in the flames first, because that is what a kiln does with memory: it brings the unlivable hours up before the usable steel.</p>

      <h2>Then the reason</h2>
      <p>Chiaki arrives as the reason to keep the eyes open. Not as a prophecy. As a person a picky weapons dealer can still stand. He pushes further. The chapter ends with the fire beginning to settle. The first Enchanted Blade is not confirmed finished. The process has not yet been allowed to become a montage.</p>
      <p>Shiba’s willingness to risk himself for the smith is already the friendship that will later walk out of the Kamunabi when the smith hides. The princess is already the hope Part 1’s son will inherit as a bowl of fish instead of a warrant. Enten’s household language is being assembled here as a relationship. File: <a href="../characters/chiaki.html">Chiaki</a>, <a href="../world/princess.html">Princess Soga</a>.</p>

      <h2>What 129 plants for 130</h2>
      <p>The next issue stays on the iron. Subaru Urita, prolific smith and sushi chef, is the colleague this project will need. Hasumi’s lab is still learning the eyes are real. The Mikaboshi want a princess. Giyu is the kind of heir who might hand her over. “Ironworks” does not resolve those rooms. It puts Kunishige far enough into the fire that the next page has to decide whether the steel, or the woman, comes out first.</p>
      <p>Close reading of that decision: <a href="chapter-130.html">chapter 130, “I'm Fine!”</a>.</p>
    </article>
""",
)

write(
    "manga/chapter-130.html",
    "Kagurabachi Chapter 130 “I'm Fine!” | Close Reading",
    "Close reading of Kagurabachi chapter 130, I'm Fine!: Datenseki becomes tamahagane, Chiaki and Kunishige reunite, and the handover clock starts.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">Manga</a> / Chapter 130</p>
    <header class="page-hero"><div>
      <p class="kicker">Jump 2026 issue 40 · 30 August 2026</p>
      <h1>Chapter 130 - “I'm Fine!”<span class="jp">“大丈夫！”</span></h1>
      <p class="lede">The steel comes out of the furnace. The title is a lie a princess tells until she is allowed to say she wanted to see him.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="The island the handover is scheduled on">
      <figcaption>Irishima is already the beach on the letter. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>Read it official: <a href="https://www.viz.com/shonenjump/kagurabachi-chapter-130/chapter/51144">VIZ, chapter 130</a> or <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. This page is a close reading, not a substitute. We do not host chapters. Jump 2026 issue 40. English readers search “I'm Fine!” The magazine’s word is 「“大丈夫！”」, quotes on the page, the way the long book put quotes on “Heroes.”</p>

      <h2>The clock in the shop</h2>
      <p>The ironworks is still on March 29. By 18:30, after sixty-one hours of blast, Subaru watches tamahagane come up from a collapsed furnace: Datenseki that has finally been allowed to be steel. He says the quiet craftsman sentence: this will make a terrifying sword. The Bureau hears it from Hasumi’s report and is surprised, which is the lab admitting Shiba was right about the eyes.</p>
      <p>The first Enchanted Blade is still not a finished object in this issue. 125 through 129 were smelting. 130 is the plate of steel on the floor. Forging is the next verb. <a href="../world/smelting.html">Smelting</a> keeps the mineral argument in one room.</p>

      <h2>The letter</h2>
      <p><span class="spoiler">Japan has accepted the Mikaboshi demand to hand Chiaki over. The letter sets Irishima’s beach for April 1, noon. Three days. The clan’s answer to what will be done to her is a forbidden art the page calls anesthesia: so she will not have to remember it. Akemura tried to stop the handover and is in chains for it. The younger brother is not yet Magatsumi. He is still the friend a smith can trust, and the sibling who would rather be locked than let the beach happen.</span></p>
      <p>Princess Soga is a title the government listens to because the clan has been a warning system for a thousand years. Chapter 130 is the title used as a shipping label. File: <a href="../world/princess.html">the office</a>, <a href="../factions/soga.html">Soga and Mikaboshi</a>.</p>

      <h2>The interruption</h2>
      <p><span class="spoiler">Kunishige and Shiba come in anyway. Two years since he last touched her. The anesthesia is broken by the entrance. The title of the chapter is what a princess is supposed to say when a nation has decided she is cargo: I'm fine. The page then lets her say the sentence the title was covering: she has always wanted to see him.</span></p>
      <p>Chapter 129 put her in the fire as memory, the reason the eyes stayed open. Chapter 130 puts her in the room. The kiln and the woman come out of the same hour. That is the household Enten will later speak in goldfish. Chihiro has not been born. The bowl is not on the table. The relationship is already the brief.</p>

      <h2>What 130 does not finish</h2>
      <p>The beach is still in three days. The tamahagane is still steel, not a named blade. Subaru is in the shop. Joji is the annoyed senior the lab already gave us. Giyu is still the heir who might prefer a treaty to a sister. Chapter 131 is due 6 September 2026. This entry moves when it prints. Official doors stay VIZ and MANGA Plus.</p>
      <p>The chapter before: <a href="chapter-129.html">Ironworks</a>. The war’s political frame: <a href="../arcs/seitei-war.html">Seitei War</a>. The person, not only the title: <a href="../characters/chiaki.html">Chiaki Soga</a>.</p>
    </article>
""",
)

write(
    "guide/part-2.html",
    "Kagurabachi Part 2 Guide | Princess, Talks, Ironworks",
    "Beginner guide to Kagurabachi Part 2: why the present tense ends, who Chiaki is, and how to read the Seitei War chapters without skipping the kiln.",
    """    <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">Guide</a> / Part 2</p>
    <header class="page-hero"><div>
      <p class="kicker">The forge door</p>
      <h1>Part 2, for people who just turned the page<span class="jp">第二部案内</span></h1>
      <p class="lede">You finished Swordsmith. The next issue is a princess. This is how to stand in that room without asking the kiln to be a clip show.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="The island Part 2 finally counts in hours">
      <figcaption>Chapter 113 already showed the clock. Part 2 is the clock, running. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>The homepage row is one line. The <a href="../manga/part-2.html">manga Part 2 page</a> is the titled run in sentences. This page is the door for someone who liked Chihiro’s hunt and has just been sent eighteen years backward. Official chapters: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. We do not host them.</p>

      <h2>What ended</h2>
      <p>Part 1 is chapters 1–115. Revenge was the engine. “Swordsmith” is the last present-tense job title: Enten spent, the son thinking like a smith again, the Sword Master loose in a government building. Close reading: <a href="../manga/chapter-115.html">chapter 115</a>. The long cut: <a href="part-1.html">Part 1</a>.</p>
      <p>You are not owed a press conference. The book goes to Irishima. Chihiro has not been born. Enten does not exist. Shiba is still a Soga guardian. Mashiro is still alive. Kunishige is still a picky weapons dealer who barely eats because he will not sell to people he cannot stand.</p>

      <h2>Who to learn fast</h2>
      <p><a href="../characters/chiaki.html">Chiaki Soga</a> is Chihiro’s mother, Princess Soga, foresight as the clan’s warrant. <a href="../characters/akemura.html">Akemura</a> is her younger brother, not yet the man the present tense calls Sword Master. <a href="../characters/ariu.html">Ariu</a> is the Mikaboshi prince; Sumika is printed. <a href="../characters/hasumi.html">Hasumi</a> runs the Datenseki lab. <a href="../characters/giyu.html">Giyu</a> is the heir who might trade a princess for a treaty. The clan page: <a href="../factions/soga.html">Soga and Mikaboshi</a>.</p>

      <h2>How the chapters are grouped</h2>
      <p><strong>116–122.</strong> Princess, then the Irishima Talks in five pieces, then “Start.” The war before the blades: what a state will prefer to a living island.</p>
      <p><strong>123–126.</strong> Chiaki as a person. Powerless. Smelting. Fire. The serial then took a month because fire in a smith’s shop is not a metaphor.</p>
      <p><strong>127–130.</strong> The rest of the smelting, Ironworks (23 August 2026), then “I'm Fine!” (30 August 2026): tamahagane on the floor, a reunion the title tries to keep small. Close readings: <a href="../manga/chapter-129.html">129</a>, <a href="../manga/chapter-130.html">130</a>. Chapter 131 is due 6 September 2026.</p>

      <h2>What not to do</h2>
      <p>Do not skip to Magatsumi. The flowers are later. Do not treat paternity rumors after 118 and 122 as fact; face, eye, and the absence of insect sorcery still point at the smith. When a video outruns the magazine, it belongs on the <a href="../media/index.html">theories page</a>. Give the war its chapters. Twenty to forty of ground is the useful caution. The printed run through 130 is still the talks, the kiln, and one beach that has not happened yet.</p>
      <p>Reading order for the whole serial: <a href="reading-order.html">how to read</a>. The mineral essay: <a href="../analysis/irishima.html">Irishima’s vein</a>. The kiln as a room: <a href="../world/smelting.html">smelting</a>.</p>
    </article>
""",
)

write(
    "world/smelting.html",
    "Kagurabachi Smelting | Datenseki, Tamahagane, the Kiln",
    "How Kagurabachi turns Datenseki into steel: Kunishige’s eyes, the ironworks chapters, tamahagane in chapter 130, and why the first blade is still work.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Smelting</p>
    <header class="page-hero"><div>
      <p class="kicker">The kiln</p>
      <h1>Smelting<span class="jp">製鉄</span></h1>
      <p class="lede">A quarter-ton of rock, a pair of eyes, sixty-one hours of blast, and a plate of steel that is not yet a national sin.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="The island whose vein feeds the kiln">
      <figcaption>The vein is the political object. The kiln is the homework. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>About 250 kilograms of Datenseki are known in the present tense. Unstable, the mineral pops the user. Enchanted Blades are the rare version that overflow as weather instead of craters. Every attempt to get there without Kunishige’s eyes produces a bomb with a few minutes on the clock. Sojo died on that sentence. Tenri died on that sentence. Part 2 puts you in the shop where the sentence was first successfully refused.</p>

      <h2>The chapters that are the manual</h2>
      <p>125 “Smelting.” 126 “Fire.” Then a month off, because Hokazono talked to a real swordsmith and the magazine was willing to wait on heat. 127 and 128 continue 製鉄. 129 “Ironworks” (製鉄 肆, 23 August 2026) puts Kunishige at the edge of the process with Chiaki as the reason the eyes stay open. 130 pulls tamahagane, Datenseki that has been allowed to be steel, out of a collapsed furnace. Subaru Urita is there to say it will make a terrifying sword. Hasumi’s lab is surprised, which is the Bureau admitting a friend’s stubbornness was national policy waiting to happen.</p>
      <p>The first Enchanted Blade is not confirmed finished in 130. Smelting and forging are different verbs. The wartime six, later, are what a state does with plates like that one. Enten, fifteen years after the war, is what a father does when he cannot smash the cellar. File: <a href="../world/datenseki.html">Datenseki</a>, <a href="../world/seventh.html">the seventh</a>, <a href="../blades/index.html">the blades</a>.</p>

      <h2>Who is in the room</h2>
      <p>Kunishige is the eyes. Shiba is already sure, and already willing to walk into someone else’s disaster. Subaru is the colleague: prolific smith, sushi chef, the man who can watch a furnace fail and still read the steel. Joji is the annoyed senior at the lab. Hasumi is the chief who will learn the eyes are real and later resign when the terms include a girl. Mashiro is still alive in these chapters and still opposed to taking stolen ore to a picky smith.</p>
      <p>Chiaki is not a fuel. She is the reason. 129 puts her in the fire as memory. 130 puts her in the shop as a person two years late. The household that will become Enten’s goldfish is being assembled as work and as love in the same hour. Close readings: <a href="../manga/chapter-129.html">Ironworks</a>, <a href="../manga/chapter-130.html">I'm Fine!</a>.</p>
    </article>
""",
)

write(
    "world/princess.html",
    "Kagurabachi Princess Soga | Chiaki’s Office and the Handover",
    "Princess Soga in Kagurabachi: foresight as clan warrant, Chiaki’s title as hostage tag, and the chapter 130 handover clock.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / Princess Soga</p>
    <header class="page-hero"><div>
      <p class="kicker">Office</p>
      <h1>Princess Soga<span class="jp">姫</span></h1>
      <p class="lede">A warning system the mainland has used for a thousand years, and a shipping label a treaty can write a princess’s name on.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/ch113.png" alt="The island that makes the title national">
      <figcaption>The talks are what you do when a princess can see a war and a bureau still wants a beach. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>Chiaki Soga holds the Princess Soga title. Foresight is talked about as inherited proof of Izanami, the clan’s warrant, the reason a government listens. She and her younger brother Akemura were elevated from a lower branch when the main-line prophetess died without children. The office is older than either of them. Part 2 opens on the rank before it opens on the person. Chapter 116 is “Princess.” Chapter 123 is “Chiaki.”</p>

      <h2>Warrant and hostage tag</h2>
      <p>The Soga pushed the Mikaboshi off the mainland something like a thousand years ago. Foresight made them aristocracy. It also made them useful. A princess who can see a war is a diplomatic object. Giyu, Hiroto’s ambitious younger brother, is the kind of heir who might accept Mikaboshi demands that include handing her over. Shiba guarded the Soga door before Cafe Haru Haru existed. He tells Kunishige not to lose hope when the title puts distance between a smith and a woman.</p>
      <p>The person under the office is Kunishige’s partner and Chihiro’s mother. The present-tense book spends a long time pretending the workshop was a father, a son, and a bowl of fish. It was. It was also this door. File: <a href="../characters/chiaki.html">Chiaki</a>, <a href="../factions/soga.html">Soga and Mikaboshi</a>.</p>

      <h2>The beach on the letter</h2>
      <p><span class="spoiler">Chapter 130 prints the office as cargo. Japan has accepted the handover. Irishima’s beach, April 1, noon, three days from the ironworks’ March 29 clock. The clan’s kindness is a forbidden anesthesia, so she will not have to remember what the beach is for. Akemura is in chains for trying to stop it. Kunishige and Shiba interrupt anyway. Two years. The title of the issue is “I'm Fine!” The page then lets her say she has always wanted to see him.</span></p>
      <p>A title that can be a warning system can also be a lie you tell until the right person is in the room. Enten’s later language, a bowl of goldfish instead of a prophecy, starts here: the hope Shiba told Kunishige not to lose, inherited by a son who will never be asked to see the future, only to decide what a blade is for. Close reading: <a href="../manga/chapter-130.html">chapter 130</a>. The kiln in the same hour: <a href="smelting.html">smelting</a>.</p>
    </article>
""",
)

write(
    "world/seventh.html",
    "Kagurabachi’s Seventh Blade | Why Enten Was Never on the Books",
    "The public count in Kagurabachi is six wartime Enchanted Blades. Enten is the seventh: unregistered, forged as a retraction, True Realm aimed at Magatsumi.",
    """    <p class="crumb"><a href="../index.html">Archive</a> / <a href="index.html">World</a> / The seventh</p>
    <header class="page-hero"><div>
      <p class="kicker">The unregistered count</p>
      <h1>The seventh<span class="jp">七本目</span></h1>
      <p class="lede">Six swords on every government list. A seventh in a cellar the lists could not smash. The whole series is people counting wrong.</p>
    </div></header>
    <figure class="shot">
      <img src="../assets/panels/enten.webp" alt="Enten">
      <figcaption>Black steel, goldfish, never a national treasure on paper. Full chapter: VIZ / MANGA Plus.</figcaption>
    </figure>
    <article class="article">
      <p>The Kamunabi count six Enchanted Blades. So does the auction house when it lists Shinuchi. So does Sojo, who wanted to mass-produce a seventh by faking the eyes and instead produced craters. Chapter 1 already told you the public number is a lie: Enten stays with the son when the six wartime swords leave the house. The Hishaku stole what was on the books. The book they could not steal is the one Kunishige made afterward.</p>

      <h2>When the seventh is forged</h2>
      <p>Every attempt to destroy the wartime blades fails. About fifteen years after the Seitei War, Kunishige and Chihiro forge Enten in the workshop. It is the first blade built as a counter rather than a weapon of state. Its True Realm is Magatsumi’s death. The goldfish are the household made into a fighting language: Kuro, Aka, Nishiki, a bowl on the table before they are a kit. The <a href="../analysis/enten-purpose.html">purpose essay</a> is the longer version. The steel’s file: <a href="../blades/enten.html">Enten</a>.</p>
      <p>Part 2 is the kiln before any of that language exists. Through chapter 130 the first wartime plate of tamahagane has come out of the furnace and no Enchanted Blade has yet been named on the page. The seventh is still decades and a cover-up away. That is why the count matters now: you are watching the six get made, and you already know a father will later refuse to stop at six.</p>

      <h2>Bearers the list cannot hold</h2>
      <p>Chihiro is Enten’s contract. The Lifelong Contract shuts the bearer’s innate sorcery off; he copies other people’s instead. After “Swordsmith,” <span class="spoiler">Enten is in pieces and the son is taking notes toward a new one</span>, which is the seventh being asked to be a seventh twice. Iori ends Part 1 holding Tobimune, a wartime blade changing hands without the government getting a vote. The <a href="bearers.html">Sword Bearers</a> page is every printed contract. This page is the one contract the raid could not inventory.</p>
      <p>Cloud Gouger dies in chapter 18 and still spends a few charges of Mei as fragments. Magatsumi’s contract is the master key: if Akemura dies, the other five wartime bearers die with him. Enten was aimed at that knot. The unregistered sword is the only one whose brief was to unmake the registered set. Close reading of the first night that fact is already true: <a href="../manga/chapter-1.html">chapter 1</a>. Close reading of the last present-tense night: <a href="../manga/chapter-115.html">chapter 115</a>.</p>
    </article>
""",
)
