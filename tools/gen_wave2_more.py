#!/usr/bin/env python3
"""More second-wave rooms: Kudo, Hiroto, Giyu, fire-gate, chapter titles. No em-dashes."""
from page_lib import page, crumb, hero, infobox


def character(slug, name, jp, kicker, lede, portrait, img, caption, rows, article, related):
    rels = "".join(f'<a href="{u}">{t}</a>' for t, u in related)
    body = (
        crumb(("Characters", "index.html"), name)
        + hero(kicker, name, jp, lede)
        + f"""<div class="layout">
      <article class="article">{article}
        <p class="related">{rels}</p>
      </article>
      {infobox(name, jp, portrait, img, caption, rows)}
    </div>"""
    )
    page(f"characters/{slug}.html", name, lede, body)


character(
    "kudo",
    "Kudo",
    "区堂",
    "Kamunabi · Warrior’s Path",
    "Gas-mask apparatus, one eye closed. He sends a body through walls. He dies protecting Hakuri, which is the bureau’s best argument that not everyone in the building was Kasen.",
    "p-azami",
    "../assets/portraits/azami.webp",
    "Kamunabi leadership table. Kudo is the head who spends himself on the walking Storehouse.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a> leadership'),
        ("Sorcery", "Warrior’s Path (死闘, Shitō)"),
        ("Look", "Gas-mask apparatus; one eye closed"),
        ("Death", "Protecting Hakuri during the HQ assault"),
        ("Politics", "Supporter of Kunishige; not the leak"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Kudo sits on the Kamunabi leadership table with Kasen, Ichiki, Yatsuru, Azami, and Izaru. Gas-mask apparatus. One eye closed. <strong>Warrior’s Path</strong> (死闘, Shitō): send a body in a direction, through walls and floors. He supported hiding Kunishige. He dies protecting <a href="hakuri.html">Hakuri</a> during the headquarters assault. That death is the bureau’s best printed argument that the building was not only a leak. Azami can kill the Shigyu brothers in a hallway and still be alive. Kudo spends the hallway on the walking Storehouse and does not walk out.</p>
    <p>He is not the director. Kasen sealed Shinuchi and then mailed an address. He is not the prosecutor. Izaru talks as if the smith stole national property. Kudo is the head who treats Hakuri as a person worth a wall. The Hishaku hunt the discarded son because the auction was architecture. The Kamunabi keep Chihiro because Chihiro comes with Hakuri. Kudo dies on that sentence.</p>
    <h2>Personality</h2>
    <p>A gas mask and a closed eye are not a personality. The pages give him the manners of a supporter: Kunishige should have been hidden, the boy’s partner should not be left in a corridor, a body can be a door. Leadership tables in this book are arguments. Kudo’s side of the argument is the one that still believes a household was worth protecting after the war. He did not leak the address. He dies in the building the leak made inevitable.</p>
    <p>Readers looking for a comic-relief commander will not find one. Warrior’s Path is a grim name even before the death. Shitō is a struggle to the death as a technique title. The book is not subtle. A man named for dying on a path dies on a path.</p>
    <h2>Abilities</h2>
    <p>Shitō sends a body in a direction, through walls and floors. The archive will not invent a range chart. What the panels support is a leader who can put himself (or a body) on the other side of architecture. Headquarters is a building full of architecture. Yukisada has stolen the barrier. Bingo has filled corridors with mouths. Kudo’s art is how you still move when the building has become someone else’s property.</p>
    <p>It is not Storehouse. Hakuri registers and removes. Kudo transits. It is not Shiba’s teleport, which is a family friend’s habit and a Soga guardian’s old job. It is a Kamunabi head’s combat rewrite of “I will be in that room.” The rewrite costs him the last room.</p>
    <h2>Story role</h2>
    <p>Volume 11’s headquarters stretch needs a death that is not Chihiro’s and not Samura’s. Kudo is that death. Uruha walks into the same raid to keep Hakuri alive, contract already cut, Crimson Recital limping. Two different institutions (a bearer and a bureaucrat) spend themselves on the same boy. The ten need the walking Storehouse stopped because Yukisada is a boy-shaped door and Hakuri is the key. Kudo understands the key well enough to die on it.</p>
    <p>Afterward the table is lighter by one supporter. Kasen’s leak is still the original memo. Azami is still the strongest head. Yatsuru’s barriers are still the work being stolen. Izaru is still distrust. Ichiki is still small and old and the man who trained Shiba. Kudo is the empty chair that proves the leak did not purchase every spine in the room. See <a href="../analysis/leak.html">the leak as policy</a>.</p>
    <h2>Notes</h2>
    <p>Kudo (区堂). Warrior’s Path. Dies for Hakuri. For the building, see <a href="../factions/kamunabi.html">Kamunabi</a>. For the boy, see <a href="hakuri.html">Hakuri</a> and <a href="../world/storehouse.html">the Storehouse</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Hakuri", "hakuri.html"),
        ("The leak", "../analysis/leak.html"),
        ("Yukisada", "yukisada.html"),
        ("Azami", "azami.html"),
    ],
)

character(
    "hiroto",
    "Hiroto Soga",
    "曽我 昼音",
    "Soga · clan head",
    "Stoic head of the mainland prophecy house. Kurotsuchi: crush or levitate. Among the strongest alive before a Datenseki prince walks onto Irishima and kills him.",
    "p-akemura",
    "../assets/panels/ch113.png",
    "Irishima. Hiroto is the mainland’s strongest sentence before the island answers.",
    [
        ("Clan", '<a href="../factions/soga.html">Soga</a> head'),
        ("Sorcery", "Kurotsuchi: directional gravity, crush or levitate"),
        ("Kin", "Chiaki (princess); Akemura (younger); Yoshinojo; Giyu (ambitious brother)"),
        ("Death", "Killed on Irishima by Ariu Mikaboshi"),
        ("Tense", "Part 2 past; not a present-tense file"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Kurotsuchi</li><li>The table</li><li>Death</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Hiroto Soga is clan head when Part 2’s clock is still a conference. The Soga were mainland prophecy aristocracy for centuries. A woman in each generation can see; that foresight is treated as inherited proof of Izanami. Chiaki holds the Princess Soga title. Akemura is her younger brother, not yet Sword Master, still the friend a smith trusts. Hiroto is the stoic who has to sit across from a vein, a risen nation, and a bureau that wants the rock without admitting it needs a picky civilian. He is among the strongest alive before Datenseki royalty walks onto Irishima. He dies to <a href="ariu.html">Ariu Mikaboshi</a> on that island, with Yoshinojo.</p>
    <p>He is not the present-tense uncle in a basement. He is the reason the present-tense uncle had a house to inherit a war from. Shiba guarded the clan. Kunishige sold swords to people he could stand, which included this house. The blades do not exist yet. Hiroto’s job in the encyclopedia is to keep the Soga from being only Chiaki’s eyes and Akemura’s flowers.</p>
    <h2>Kurotsuchi</h2>
    <p>Directional gravity. Levitate or crush. The archive will not invent a three-count. What the panels and the register support is a clan head who can end a man without an Enchanted Blade, which is the point of putting him on the same island as a prince whose body is already mineral. Adaptation versus aristocracy. Hiroto can crush. Ariu grew up inside Datenseki. The crush loses.</p>
    <p>Readers who want Kurotsuchi to be a secret sixth blade technique are doing the camp’s work early. It is an innate art. Lifelong Contracts have not been invented as a plot object yet because the steel has not been smelted. Gravity is a person.</p>
    <h2>The table</h2>
    <p>Chapters 117–121 are titled as talks. Hiroto is the mainland’s strongest sentence at that table. Giyu, ambitious younger brother, next in line, is willing to accept Mikaboshi demands that include handing Chiaki over. Yoshinojo grins and does not relent. Hasumi’s lab fails. Mashiro does not want stolen ore walked into a shop. Joji is annoyed. Shiba already knows whose eyes to hire. A princess with foresight is a strategic weapon and a hostage tag. Hiroto can be the strongest man in the room and still lose the room to a ceasefire he has not signed yet.</p>
    <p>Ukizane Soga, historical, nearly destroyed the Mikaboshi before they hid under the sea. Hiroto is not Ukizane. The exiles came back with adapted bodies. A thousand years of winning the mainland is not a warranty on a vein.</p>
    <h2>Death</h2>
    <p>Ariu kills Hiroto and Yoshinojo on Irishima. Sumika, poisoned air, hardened flesh. The talks have not always spent the splash; the register is willing to state the later. This file will not storyboard a panel the uncollected run has not made cheap to source as a weekly caption. It will say: the head dies to the prince. The grinning veteran dies with him. Giyu’s ambition becomes a succession problem. Chiaki’s title becomes more expensive. Akemura’s later policy (flowers, 200,000 civilians) is what a younger brother does with grief and a masterpiece the country has not yet asked Kunishige to make.</p>
    <p>Part 1 taught you to hate the Sword Master. Part 2 is making you watch the country build him, and watch the house he came from lose its head to the mineral’s royal family. See <a href="../factions/soga.html">Soga and Mikaboshi</a> and <a href="../analysis/irishima.html">the vein</a>.</p>
    <h2>Notes</h2>
    <p>Hiroto Soga (曽我 昼音). Kurotsuchi. Dead to Ariu. For the princess, see <a href="chiaki.html">Chiaki</a>. For the ambitious brother, see <a href="giyu.html">Giyu</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Soga and Mikaboshi", "../factions/soga.html"),
        ("Ariu", "ariu.html"),
        ("Chiaki", "chiaki.html"),
        ("Giyu", "giyu.html"),
        ("Part 2", "../manga/part-2.html"),
    ],
)

character(
    "giyu",
    "Giyu Soga",
    "曽我 義勇",
    "Soga · the ambitious brother",
    "Hiroto’s younger brother, next in line, willing to accept Mikaboshi terms that include handing Chiaki over. A title is also a hostage tag.",
    "p-akemura",
    "../assets/portraits/akemura.webp",
    "Succession as a threat. Giyu is the Soga who might trade the princess.",
    [
        ("Clan", '<a href="../factions/soga.html">Soga</a>'),
        ("Kin", "Hiroto (head); Chiaki (princess); Akemura; Yoshinojo"),
        ("Printed stance", "Willing to accept ceasefire terms that include handing Chiaki over"),
        ("Tense", "Part 2 talks"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The trade</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Giyu Soga is Hiroto’s ambitious younger brother, next in line when Part 2 is still a conference. The Soga’s warrant is Chiaki’s eyes. The Soga’s risk is everyone who wants those eyes in a different building. Giyu is the risk wearing the family name. He is willing to accept Mikaboshi ceasefire terms that include handing the princess over. That sentence is why a title is also a hostage tag, and why Shiba tells Kunishige not to lose hope when the princess rank puts distance between them.</p>
    <p>He is not Akemura. Akemura is the brother a princess loves, the friend a smith trusts, the man who will later void a peace with flowers. Giyu is the succession problem in the present tense of the talks. If Hiroto dies to Ariu (and he does), ambition becomes a vacancy. This page will not invent Giyu’s later crown. It will keep the trade on the record.</p>
    <h2>The trade</h2>
    <p>Handing Chiaki over is not a metaphor. Foresight is a strategic weapon. The Mikaboshi came back for a vein. A people who can kill the clan head and the grinning veteran can demand the woman who sees. Giyu’s willingness is the mainland aristocracy doing what aristocracies do when the war is a mineral: spend the symbol to keep the furniture. Hasumi resigns when the bureau accepts terms. Mashiro dies later to the same prince. Giyu’s printed sin is earlier and colder: he would have signed.</p>
    <p>The clan is not a single will. Hiroto is stoic. Yoshinojo is unrelenting. Chiaki is hope in the fire. Akemura is not yet policy. Giyu is the will that treats a sister-rank as inventory. Hakuri’s auction house is the present-tense version of inventory. Part 2 puts the habit in a prophecy house so you cannot pretend only criminals warehouse people.</p>
    <h2>Story role</h2>
    <p>The Irishima talks need someone at the table who is not a hero and not a prince. Giyu is that someone. Without him the Soga look like a united tragic house. With him they look like a government. Kunishige has not looked at the stone. Enten does not exist. The ambitious brother is already doing the math the Hishaku will later do with blades: open the knot, spend the person, change the country.</p>
    <p>When Hiroto and Yoshinojo die on the island, this file becomes heavier. Next in line is not a trivia line. It is a threat to Chiaki that outlives the talks. Akemura’s Malediction is a different answer to the same war (erase the island’s logic with flowers). Giyu’s answer was a trade. The country filed the flowers as heroes. It would have filed the trade as peace. See <a href="../analysis/malediction.html">Malediction</a>.</p>
    <h2>Notes</h2>
    <p>Giyu Soga (曽我 義勇). The trade. For the head, see <a href="hiroto.html">Hiroto</a>. For the princess, see <a href="chiaki.html">Chiaki</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hiroto", "hiroto.html"),
        ("Chiaki", "chiaki.html"),
        ("Soga and Mikaboshi", "../factions/soga.html"),
        ("Malediction", "../analysis/malediction.html"),
        ("Part 2", "../manga/part-2.html"),
    ],
)

page(
    "world/fire-gate.html",
    "The fire-gate",
    "The Hishaku’s shared door: flame tattoos as a uniform, extraction as a habit, Toto as the specialist who prefers a gate to a cut.",
    crumb(("World", "index.html"), "The fire-gate")
    + hero("毘灼 · logistics", "The fire-gate", "火門", "Ten people, one door. The tattoos are the uniform. The gate is why a hotel fight can end in extraction instead of a grave.")
    + """
    <article class="article">
      <p>The Hishaku share a fire-gate. Flame-emblem tattoos. A door that is not a window and not a Storehouse. Toto uses it as a habit, pulling comrades out of fatal rooms. Hokuto would rather close distance with steel. Kuguri would rather a sword finally sign him. Hiruhiko would rather a peer. Yukisada becomes a building. The gate is the ten’s only manners that look like care and are actually inventory control. Yura did not staff a medic. He staffed a method that can leave.</p>
      <p>The Kyoto Bloodshed Hotel is the printed exam. Play takes the upper floors apart. Samura arrives because two Enchanted Blades ping Owl. Toto extracts Kuguri rather than letting the unwilling instructor finish as a corpse. Without the gate, chapter 70’s classroom is a tomb. With it, the ten remain a method tomorrow. See <a href="hotel.html">the hotel</a> and <a href="../characters/toto.html">Toto</a>.</p>

      <h2>What it is not</h2>
      <p>It is not Hakuri’s Kura. Storehouse registers people and charged objects and moves blades across the country. The fire-gate moves Hishaku. Confusing the two is how recaps turn every teleport into the same trick. Shiba’s teleport is a third trick: a family friend, a Soga guardian, a man who left the bureau. Azami cannot call him into headquarters until Yukisada’s stolen barrier is a field again. None of those sentences are the fire-gate.</p>
      <p>It is not Suzaku. Samura’s flames heal, burn, and later kill contracts while keeping the man. The gate does not heal. It relocates the tattooed. It is not Magatsumi’s overwrite. Yura spending Shinuchi at range is a masterpiece leaking through spirit left in the steel. The gate is cheaper and older in the ten’s life: they formed about four years before the main story with one plan for Shinuchi. Logistics predates the cell conversation.</p>

      <h2>Who uses it</h2>
      <p>All ten can, in principle. Toto prefers it to the cut. That preference is a personality. The raid on the Rokuhira house did not need a gate to be a massacre; three sorcerers in a workshop is enough. The hotel needed a gate because the father arrived. Headquarters is a different problem (Yukisada holds the door from inside). The fire-gate is for the jobs that go wrong in someone else’s building.</p>
      <p>This archive will not invent a maximum range, a cooldown, or a chapter that lectures the geometry. Flame tattoos are the visible contract. The gate is the clause. Two of the ten stay unlabeled; they still get the door. Official chapters: VIZ / MANGA Plus.</p>
      <p class="related"><a href="../factions/hishaku.html">Hishaku</a><a href="../characters/toto.html">Toto</a><a href="hotel.html">Hotel</a><a href="storehouse.html">Storehouse</a><a href="../world/techniques.html">Catalog</a></p>
    </article>
    """,
)

page(
    "analysis/titles.html",
    "What the titles are doing",
    "From meals to quotation marks: how Kagurabachi’s chapter names teach the method before the essays do.",
    crumb(("Essays", "index.html"), "What the titles are doing")
    + hero("Essay · the index", "What the titles are doing", "題", "Early chapters are objects and meals. Then the swords get their names. Then the press’s words get quotation marks. Part 2 opens on a rank and a kiln.")
    + """
    <article class="article">
      <p>The <a href="../manga/chapters.html">chapter index</a> is not a filing cabinet. It is the book’s method in miniature. Early titles are objects and meals: “Heaps,” “A Good Meal,” “Peace,” “Food,” “Tea.” A revenge manga that starts on food is already telling you the household comes first. Then the swords get their names on the page: “Enten vs. Cloud Gouger,” “True Realm,” “Roar.” The auction speaks in architecture and family: “Storehouse,” “Deal,” “Equal,” “Fervent,” “The Curtain Falls.” The long book names people, “Uruha,” “Samura,” “Iori,” “Natsuki”, and then puts quotation marks on the words the press already used: “Strongest,” “Sword Master,” “Heroes.” Part 2 opens on a rank and a place. “Princess.” “The Irishima Talks,” four times, then “END.” “Chiaki.” “Smelting.” “Fire.” “Ironworks.”</p>
      <p>This essay is for readers who skip the index and then wonder when the book got political. It was political when it titled a chapter after a Daruma sorcerer’s promise. “Norisaku Madoka: I Will Change” is an epitaph that looks like hope. Chapter 98, “Ikuto Hagiwara, Worthless Commander,” is a government talking to a leftover. The quotation marks on “Heroes” are the war’s press release dragged into a headquarters fight. You do not need the Malediction essay to feel that. You need to read the table of contents like a person.</p>

      <h2>Meals, then steel</h2>
      <p>Chihiro works a cafe. Char needs a good meal. Sojo’s people eat and die. The first movement’s titles insist that bodies have to be fed before they can hold weather. True Realm arrives as a title only after the hospital and the specialists. The brief, meant, is a late word for something the goldfish already knew. Volume 1 is <em>Mission</em>. Volume 2 names the duel. The jump from should-do to blade-versus-blade is the first book’s whole commute.</p>
      <p>Hokazono’s one-shot was already named <em>Enten</em>. The serial waits until Volume 9 to put that word on a spine alone. Chapter 83 is the brief said cleanly. The title desk is patient. It will feed you for eight chapters before it lets a sword fight be the header.</p>

      <h2>People as headers</h2>
      <p>Once the long book starts, chapters are named like files in this archive: Uruha, Samura, Iori, Natsuki, Ikuto Hagiwara. A supporting commander getting a cruel full-name title is the manga deciding institutions have protagonists too. “Imitate” and “Iai White Purity Style” are Kuguri’s classroom without printing Kuguri. “The Swordsmen” is a jacket and a chapter that wants blades before factions. This site’s character pages are downstream of that habit. When we file Toto or Yukisada, we are agreeing with the index: people are the unit, not “Hishaku guy #6.”</p>

      <h2>Talks, then heat</h2>
      <p>Part 2’s “The Irishima Talks” repeated is a joke that is also a thesis. A war over a vein is a meeting until it is a kiln. “END” on a talks chapter is the book telling you the conference was the battlefield. Then Chiaki, then Smelting, then Fire, then Ironworks. Montage is refused. Hokazono talked to a real swordsmith. The titles become process words because the ethics are in the process. If you came for another hotel and got “Smelting” four ways, you got the point.</p>
      <p>When 130 prints, this essay will add the word. Until then the index through 129 is the argument. Official chapters: VIZ / MANGA Plus. Related: <a href="../guide/part-1.html">Part 1 long cut</a>, <a href="../manga/synopses.html">synopses</a>, <a href="irishima.html">the vein</a>.</p>
      <p class="related"><a href="../manga/chapters.html">Chapter index</a><a href="../guide/part-1.html">Part 1</a><a href="malediction.html">Malediction</a><a href="../manga/part-2.html">Part 2</a></p>
    </article>
    """,
)

print("more rooms written")
