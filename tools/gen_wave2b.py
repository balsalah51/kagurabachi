#!/usr/bin/env python3
"""More second-wave character files. No em-dashes."""
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
    "hagiwara",
    "Ikuto Hagiwara",
    "萩原 幾兎",
    "Kamunabi · Anti-Cloud Gouger",
    "Commander of six people built to solve one stolen sword. Both legs gone. Chapter 98 calls him a worthless commander and then keeps using him.",
    "p-hagiwara",
    "../assets/portraits/hiyuki.webp",
    "Kamunabi operations. The ACG desk outlives the sword it was named for.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a> · <a href="../world/acg.html">Anti-Cloud Gouger Special Forces</a>'),
        ("Rank", "Commander"),
        ("Sorcery", "Jikai (磁戒), magnetism"),
        ("Injuries", "Loses both legs against Sojo; later hallucinates Kugara"),
        ("Chapter", "98, “Ikuto Hagiwara, Worthless Commander”"),
        ("First appearance", "Vs. Sojo / hospital stretch"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Ikuto Hagiwara commands the <a href="../world/acg.html">Anti-Cloud Gouger Special Forces</a>: six sorcerers assembled because <a href="../blades/cloud-gouger.html">Cloud Gouger</a> in <a href="sojo.html">Sojo</a>’s hands was a national problem. Four of them die in the first book. He loses both legs. He keeps the desk. Chapter 98 is titled with his name and a cruelty, “Ikuto Hagiwara, Worthless Commander,” because the manga decided the leftover of an institution deserves a chapter that is about the leftover, not about the blade the institution failed to hold.</p>
    <p>The other five are named on the ACG desk: Hajime Kugara (iron body, childhood friend since age five, the face of the later hallucination), Kazane Machi (Demon Monster, Kaichi, unused secret weapon, loses the right arm first), Shiyumi Harima (Gansui, stone), Kiyohiko Uzuki (binding), Makoto Kasahara (enlarged hands). Two survivors. That was the cavalry. This page is the commander’s.</p>
    <p>He is still useful in the headquarters chapters. Useful is the Kamunabi’s only compliment. Yukisada cannot be killed cleanly; Hagiwara is one of the people who learns that sentence the hard way. The book will not let a legless commander leave the story just because the weather sword is already broken. Institutions keep their damaged specialists. This one puts the damage in the title.</p>
    <h2>Personality</h2>
    <p>A commander of a six-person sword-killer unit does not get to be casual. The pages give him the manners of a man who knows the assignment is impossible and shows up anyway. After the compound, the manners include a hallucination. Kugara has been his friend since they were five. The iron body dies. The face stays. That is not a power-up. That is what the book does with people the state spends.</p>
    <p>Worthless is the chapter’s word, not this archive’s diagnosis. The title is how a government talks to the survivor of a failed special forces desk. Hagiwara’s answer is to remain in the building. He does not get a redemption arc that grows the legs back. He gets more work: HQ, Yukisada, a barrier that is also a boy. The cruelty is the characterization.</p>
    <p>He is not Azami. Azami is a head who can still kill the Shigyu brothers in a hallway. He is not Hiyuki. Flame Bone is the pointed end the organization assigns to problems it cannot file. Hagiwara is the pointed end it already used and broke. The difference matters. Chihiro meets the ACG as the state’s best offer in the first arc and watches the offer die. He meets Hagiwara again as proof the offer’s commander is still on the payroll.</p>
    <h2>Abilities</h2>
    <p><strong>Jikai</strong> (磁戒) is magnetism. The archive will not invent a textbook of polarities. What the panels show is a commander who can still fight after the body has been reduced. Legs gone. Authority intact. Magnetism is the technique that makes that sentence possible when the room still has metal in it. The exact grammar waits for a chapter that is willing to lecture. Until then Jikai is the name on the register and the reason a legless officer is not only a speech.</p>
    <p>The hallucination of Kugara is listed here as injury, not as a second sorcery. The book is allowed to show a commander seeing his dead friend without turning the vision into a summon. If a later chapter makes the hallucination a technique, the catalog will move it. Today it is grief with a mask.</p>
    <p>Against Yukisada, Jikai is not enough. Regeneration past decapitation does not care about a magnetic field. The correct tool is Hakuri’s Storehouse, removing the Kamunabi vessel from the barrier split. Hagiwara’s presence in that fight is the state’s stubbornness: send the Cloud Gouger commander at the next impossible object. The object is seventeen and will not stay dead.</p>
    <h2>Story role</h2>
    <p>Vs. Sojo is the introduction. Char is in a hospital. The Anti-Cloud Gouger Forces arrive as if a named unit can solve a stolen Enchanted Blade. Sojo treats them as weather treats a forecast. Four graves. An arm. Two legs. Chihiro loses an arm of his own and finds the True Realm. Cloud Gouger breaks. Sojo chooses Datenseki over a quiet death. Hagiwara lives. The unit does not dissolve in the text just because its named target is gone. A special forces desk that loses its sword still has a building, a budget, and a commander who remembers what the target cost.</p>
    <p>The long book brings him back because headquarters is full of leftovers. Kasen’s leak. Yukisada in the barrier. Kudo dying for Hakuri. The ACG survivors are still in those chapters. Chapter 98’s title is the book looking at the first arc’s cavalry and refusing to pretend the surviving horse is a stallion. Worthless is what you call a man when you already spent his friends and still need his magnetism.</p>
    <p>He is not the end of the Kamunabi argument. Hiyuki and Tafuku are the celebrity pair. Natsuki and Kiri are the squadron leaders on the later jackets. Hagiwara is the argument that the first book’s government failure has a name and a continuing pulse. Read him next to the <a href="../arcs/vs-sojo.html">Vs. Sojo arc</a> and the <a href="../world/acg.html">ACG desk</a>. The cavalry was six. The desk is one man who cannot stand up the way he used to and stands up anyway.</p>
    <h2>Notes</h2>
    <p>Ikuto Hagiwara (萩原 幾兎). Jikai. Both legs. Kugara since age five. Chapter 98. Two ACG survivors; this page will not invent which of the named five besides Kugara is the other grave versus the other survivor beyond what the register already holds: four dead, two alive, Kugara dead, Kazane maimed. For Flame Bone, see <a href="hiyuki.html">Hiyuki</a>. For the weather sword, see <a href="../blades/cloud-gouger.html">Cloud Gouger</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Anti-Cloud Gouger", "../world/acg.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Sojo", "sojo.html"),
        ("Yukisada", "yukisada.html"),
        ("Vs. Sojo", "../arcs/vs-sojo.html"),
    ],
)

character(
    "mashiro",
    "Shuji Mashiro",
    "真城 秀治",
    "Sorcery Bureau · Akuu",
    "Shiba’s partner before the bureau finished becoming an army. Air pressure in the hands. Alive at the Irishima talks. Dead later, to Ariu.",
    "p-mashiro",
    "../assets/portraits/shiba.webp",
    "Bureau years. Mashiro is the partner Shiba still has to talk around.",
    [
        ("Affiliation", "Sorcery Bureau (Part 2 past)"),
        ("Partner", '<a href="shiba.html">Togo Shiba</a>'),
        ("Sorcery", "Akuu (空亜), air pressure; hands-free weapons"),
        ("Gift", "A Kunishige sword at 18"),
        ("Status", "Alive in the Irishima talks; dies later to Ariu Mikaboshi"),
        ("Position", "Opposes taking stolen Datenseki to the smith"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Shuji Mashiro is <a href="shiba.html">Togo Shiba</a>’s partner when both of them still wear the Sorcery Bureau. Part 2 is that tense: the bureau has not finished becoming an army, the Enchanted Blades have not been forged, Chihiro has not been born. Mashiro’s sorcery is <strong>Akuu</strong> (空亜), air pressure, weapons that do not need a grip. He is gifted a Kunishige sword at eighteen. He opposes taking stolen Datenseki to a civilian smith. He is alive at the Irishima talks. He dies later, to <a href="ariu.html">Ariu Mikaboshi</a>.</p>
    <p>The archive keeps a page because a dead partner is still a fact Shiba carries into every present-tense room. Cafe Haru Haru, the raid’s aftermath, the headquarters street: Shiba teleports and jokes and extracts. Mashiro is the missing half of an older act. Part 2 finally puts the half on panel. Then the island takes him, on a delay the register is willing to state and the talks themselves have not yet reached.</p>
    <p>He is not Azami. Azami stays inside and becomes a head. He is not Joji. Joji is the annoyed senior with an eyemask. Mashiro is the partner: equal enough to argue about ore, gifted enough to hold a Rokuhira blade before Rokuhira was a national myth.</p>
    <h2>Personality</h2>
    <p>Opposing the stolen Datenseki run is the printed ethic. Mashiro does not want to walk mineral that is not theirs into a picky weapons dealer’s shop and call that patriotism. Shiba already believes Kunishige’s eyes are the only way to make the vein usable. Both of them can be right about different sentences. The ore is stolen. The eyes are real. The war will not wait for a clean chain of custody. Mashiro is the man who still wants the chain.</p>
    <p>A Kunishige sword at eighteen is a character note, not a contract. Lifelong Contracts belong to Enchanted Blades, which do not exist yet. The gift means Kunishige, still a civilian who will not sell to people he cannot stand, could stand Mashiro. That is a high bar in this book. It is also why the later death is an invoice the smith’s household never gets to pay in person. Chihiro will never meet the uncle’s generation of friends except as names Shiba does not always say.</p>
    <p>The pages do not turn him into comic relief beside Shiba’s mouth. The partnership is work. Joji is ranked above them and annoyed. Hasumi runs the lab and will later resign after letting Shiba steal ore. Mashiro is the one who, in the talks, is still breathing and still arguing. Part 2’s job is to make those arguments expensive before the flowers.</p>
    <h2>Abilities</h2>
    <p>Akuu: air pressure, hands-free weapons. The textbook is thinner than Cloud Gouger’s. The effect is a Bureau sorcerer who can fight without looking like a swordsman even when he owns a Kunishige blade. Treat the name as a caption. Do not invent polarities or a three-count. Innate arts in the war book are being introduced as people, not as a game UI.</p>
    <p>The gifted sword is ordinary excellent steel, which in this series is already a miracle. Subaru will later like Kunishige because both of them kept a civilian craft next to a lethal one. Mashiro holding a Rokuhira blade at eighteen is the lethal side of that household arriving early. Enten’s goldfish are years away. The brief is still “a sword a friend can carry.”</p>
    <h2>Story role</h2>
    <p>Chapters 117 through 121 are titled as talks. Mashiro is in that battlefield. A princess with foresight, a lab that fails, a senior who is annoyed, a prince under the sea who will kill Hiroto and Yoshinojo on the island. Mashiro’s printed position (do not take stolen rock to the smith) is one of the conference table’s honest objections. The war happens anyway. Kunishige looks anyway. The blades enter at plus one year and five months anyway.</p>
    <p>Ariu kills him later. That sentence belongs on both pages. The talks have not yet spent it. The register has. This file will not stage the death as a splash the magazine has not drawn in the uncollected run. It will say: alive now, dead later, same prince who poisons air and hardens a body in Datenseki. Shiba’s present-tense extraction habit is what a man looks like after that kind of later.</p>
    <p>When Part 2 conversations return to Mashiro, they are inventory, not nostalgia. Who stood next to Shiba. Who held a smith’s sword. Who said no to a theft. Who died to a crown prince. The YouTube desk will want a paternity theory. This page is for the quieter claim: the Bureau was people before it was the Kamunabi, and one of those people was the partner.</p>
    <h2>Notes</h2>
    <p>Shuji Mashiro (真城 秀治). Akuu. Kunishige sword at 18. Dies later to Ariu. Alive in the talks. For the prince, see <a href="ariu.html">Ariu Mikaboshi</a>. For the lab chief, see <a href="hasumi.html">Hasumi</a>. For the vein, see <a href="../analysis/irishima.html">Irishima’s vein</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Shiba", "shiba.html"),
        ("Ariu Mikaboshi", "ariu.html"),
        ("Part 2", "../manga/part-2.html"),
        ("Irishima’s vein", "../analysis/irishima.html"),
        ("Hasumi", "hasumi.html"),
    ],
)

character(
    "hinao",
    "Hinao",
    "ヒナオ",
    "Cafe Haru Haru",
    "The civilian door. She runs the cafe where the war sits down, and she connects sorcerers to the people who want to hire them.",
    "p-hinao",
    "../assets/portraits/chihiro.webp",
    "Cafe Haru Haru. Hinao is the room; Chihiro is the counter between raids.",
    [
        ("Occupation", "Proprietor, Cafe Haru Haru"),
        ("Role", "Connects sorcerers to yakuza and corporations who need them"),
        ("Voiced comic", "Akari Tadano"),
        ("First appearance", "Chapter 1"),
        ("Regulars", "Chihiro, Shiba, later the people who know the address"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>The room</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Hinao runs Cafe Haru Haru. <a href="chihiro.html">Chihiro</a> works the counter between raids. <a href="shiba.html">Shiba</a> uses the booths. <a href="azami.html">Azami</a> knows the address. The cafe is the closest thing the first chapters have to a home, and Hinao is the person who keeps the lights on while Enchanted Blades lean against the wall. She also connects sorcerers to yakuza and corporations who need them. The civilian door is a job, not a personality type.</p>
    <p>She is not a secret master. She is not a hidden Masumi. She is not waiting to pull an Enchanted Blade out of the espresso machine. The archive will not promote her into a warrior to make the page longer. The page is long enough if it tells the truth: someone has to run the room where the war sits down, and someone has to know which underworld phone still answers.</p>
    <p>Akari Tadano voices her in the voiced comic. The 2027 Cypic series has announced Chihiro, Kunishige, and Shiba. Hinao’s anime casting is not a caption this page will invent. The cafe will be a problem for a studio either way: a warm interior in a book about stolen steel.</p>
    <h2>Personality</h2>
    <p>The book gives her the manners of a proprietor who has accepted a boy with a sword and a teleporting uncle. That acceptance is not naivete. A woman who brokers sorcerers to corporations already knows what the work costs. She lets Chihiro stay anyway. The goldfish household’s ethics leak into the cafe because Chihiro works there, not because Hinao is a monk. She is a civilian with a ledger.</p>
    <p>When Toto can find Chihiro after a death, the cafe stops being safe. Hinao is still behind the counter. The archive will not write a speech she has not been given. It will write the fact of remaining. Most of the cast can leave a building. The proprietor is the building’s habit.</p>
    <h2>The room</h2>
    <p>Cafe Haru Haru is listed on the <a href="../world/locations.html">locations desk</a> as the sit-down between jobs. Char’s sighting, Madoka’s confirmation, Sojo’s first shadow: the city is the first map, and the cafe is the pin. A modern Japan that had to admit sorcery in public still has coffee. The joke is only funny until an Enchanted Blade user walks in and orders like a person.</p>
    <p>The broker work matters because Chihiro and Shiba’s three-year commute is not a montage of random thugs. It is a labor market. Yakuza and corporations need sorcerers. Hinao knows who. That knowledge is why the first chapters can move without a government handler on every page. Azami wants Chihiro out of the underworld. Hinao is how the underworld had a front door that looked like a cafe.</p>
    <h2>Story role</h2>
    <p>Chapter 1 already needs a place that is not the ruined workshop. Hinao is that place. The raid is three years old. Enten is on the boy. The bowl is on the table at home; the cafe is the public version of a table. Mission, heaps, witness: the early titles are objects and meals. Hinao is the meal’s landlord.</p>
    <p>She does not get fight chapters. She gets the harder job: remaining in the frame as the world the blades are supposedly protecting. Vs. Sojo takes the story to a hospital and a compound. The Rakuzaichi takes it to an auction. The long book takes it to a hotel and a headquarters. The cafe remains the civilian measure. If the war cannot be sat down next to a cup, the war has already eaten the premise.</p>
    <p>Part 2 leaves her behind because Part 2 is twenty-two years earlier and Chihiro has not been born. That absence is useful. The talks have no cafe. They have a conference table and a kiln. Hinao is what the present tense built afterward: a room where a smith’s son can be a waiter instead of only a revenge. The 2027 anime will have to decide how much warmth to light. This page will not storyboard it.</p>
    <h2>Notes</h2>
    <p>Hinao (ヒナオ). Cafe Haru Haru. Broker. Akari Tadano in the voiced comic. For the boy at the counter, see <a href="chihiro.html">Chihiro</a>. For the uncle in the booth, see <a href="shiba.html">Shiba</a>. For first-read notes, see <a href="../fun/first-read.html">the twelve things chapters 1–20 will not spell out</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Chihiro", "chihiro.html"),
        ("Shiba", "shiba.html"),
        ("Locations", "../world/locations.html"),
        ("First-read notes", "../fun/first-read.html"),
        ("Voices", "../fun/voices.html"),
    ],
)

character(
    "itsuo",
    "Itsuo Shirakai",
    "白廻 逸夫",
    "Iai White Purity · founder",
    "The man who founded the school. Lives in the mountains. Texts. A bigot. His granddaughter brought an odachi anyway.",
    "p-itsuo",
    "../assets/portraits/iori.webp",
    "The school’s origin is a man Kiri has already vowed to decapitate.",
    [
        ("Role", "Founder of Iai White Purity Style"),
        ("Known for", "Mountain seclusion; messages; misogyny as curriculum"),
        ("Relatives", '<a href="kiri.html">Kiri Shirakai</a> (granddaughter); the school that produced Samura and Iori'),
        ("Kiri’s vow", "To decapitate him"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The school</li><li>The man</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Itsuo Shirakai founded Iai White Purity Style, the school that produced <a href="samura.html">Seiichi Samura</a> and, in a different generation, <a href="iori.html">Iori</a>. He is a misogynist. He lives in the mountains. He still sends messages. <a href="kiri.html">Kiri Shirakai</a>, granddaughter, two-meter odachi, chapter 90, has vowed to decapitate him. The archive will not sand any of that down. A style named purity was founded by a man who did not want women in the work. History is often that sloppy.</p>
    <p>He is not a weekly villain walking into headquarters. He is a source. Chihiro copies Iai with his eyes shut because that is how the curriculum works, and the curriculum came from this mountain. Kuguri is the unwilling live dummy. Itsuo is the reason the dummy’s lesson has a name. The hotel is a school. The founder is not invited. He is still in the texts.</p>
    <h2>The school</h2>
    <p>Iai White Purity Style is a sword school, not a sorcery clan. Draw, cut, lids down. Samura carried it into the Seitei War and out the other side as the fastest bearer. Iori inherited the body of the practice even when the family tried to keep her from the war. Chihiro, who already copies by sight, shuts his eyes in Kyoto and makes the fake real enough that Kuguri drops a kidnapping. Full desk: <a href="../world/iai.html">Iai White Purity</a>.</p>
    <p>Kiri’s five-shaku blade is a different argument in the same bloodline. The founder did not want her. She brought an odachi to a school that told her not to. Squadron leader, Kamunabi, Volume 10’s neighboring generation. The vow to decapitate Itsuo is not a cute family joke. It is a granddaughter answering a curriculum with a longer sword.</p>
    <h2>The man</h2>
    <p>The misogyny is canon, not a fan diagnosis. He did not want women in the work. The manga lets that fact sit next to Iori’s competence and Kiri’s rank. The contradiction is the point. A school founded by a man who hates the idea of a girl with a sword produced girls with swords. Samura’s guilt-religion and Iori’s broken seal are also products of the same house, in a wider sense: purity as a style you can name, then fail to live.</p>
    <p>He withdrew. The texts still arrive. Kiri is the living relative who still has to deal with the founder as a person, not a statue. When the archive says “the old man in the mountains,” it means this man. This page will not invent the content of a text the magazine has not printed, and it will not invent a redemption hike.</p>
    <h2>Story role</h2>
    <p>He is present as origin whenever Iai is on the page. Samura’s speed. Iori’s body knowledge under a memory seal. Chihiro’s hotel education. Kiri’s odachi and vow. The long book needs a founder so the school is not a floating aesthetic. Enchanted Blades have Kunishige. Iai has Itsuo. One of those men was sorry. The other is still texting from a mountain about a purity that did not include his granddaughter.</p>
    <p>Part 2 will not feature him. The war book is Irishima, Chiaki, a kiln. Iai already exists as a civilian school the bearers can carry into a mineral war. Itsuo’s job in the encyclopedia is to keep the school from becoming a caption on Samura alone. For the daughter who chose a classmate over a seal, see Iori. For the granddaughter who chose a longer blade, see Kiri. For the blind man who made the style a religion, see Samura.</p>
    <h2>Notes</h2>
    <p>Itsuo Shirakai (白廻逸夫). Founder. Bigot. Mountains. Texts. Kiri’s vow. For the hotel classroom, see <a href="kuguri.html">Kuguri</a> and <a href="../world/hotel.html">the Kyoto Bloodshed Hotel</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Kiri Shirakai", "kiri.html"),
        ("Iai White Purity", "../world/iai.html"),
        ("Samura", "samura.html"),
        ("Iori", "iori.html"),
        ("Kuguri", "kuguri.html"),
    ],
)

character(
    "ariu",
    "Ariu Mikaboshi",
    "亜利雨 箕加星",
    "Mikaboshi · crown prince",
    "Insect constructs, poisoned air, a Datenseki-hardened body. He kills two Soga on Irishima. Some readers see Magatsumi in him. That is a camp, not a caption.",
    "p-ariu",
    "../assets/panels/ch113.png",
    "The island that starts the clock. Ariu is the royal kit walking onto it.",
    [
        ("People", '<a href="../factions/soga.html">Mikaboshi</a> crown prince'),
        ("Sorcery", "Sumika (栖): insect constructs, poisoned air"),
        ("Body", "Datenseki-adapted / hardened"),
        ("Known kills", "Hiroto Soga; Yoshinojo Soga; Mashiro (later)"),
        ("Fan camp", "Magatsumi as insect copy. Filed as camp."),
        ("Arc", '<a href="../manga/part-2.html">Part 2 / Irishima talks</a>'),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Sumika</li><li>The Soga</li><li>The Magatsumi camp</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Ariu Mikaboshi is crown prince of the old sorcerer kings the Soga pushed off the mainland more than a thousand years ago. The Mikaboshi survived under the sea in a habitat of branches, bodies adapted to Datenseki, and came back when Irishima’s vein showed and Shokoku rose. Ariu is the royal kit on two legs: <strong>Sumika</strong> (栖), insect constructs, poisoned air that dulls senses, flesh the mineral has already rewritten. He kills <strong>Hiroto Soga</strong> and <strong>Yoshinojo Soga</strong> on the island. He kills <a href="mashiro.html">Shuji Mashiro</a> later. Part 2’s talks are the conference before those invoices come due; the register is willing to state the later.</p>
    <p>He is not a Hishaku. He is not a Kamunabi leak. He is the reason the Seitei War has a royal family inside a quarter-ton of rock. Chiaki’s foresight is the mainland’s warning system. Ariu is the warning, arriving. Kunishige has not yet looked at the stone. Enten does not exist. Magatsumi does not exist. The prince does.</p>
    <h2>Sumika</h2>
    <p>Insects on the page. Control, swarm, air you cannot trust. The textbook is thinner than Cloud Gouger’s three-count and meaner than a single named slash. Poisoned air dulls senses. A Datenseki-hardened body means ordinary steel is a conversation the mineral already won. Hiroto can crush a man with directional gravity and still die to this. That is the point of putting Kurotsuchi next to Sumika on the same island: the strongest mainland aristocrats are not adapted. The exiles are.</p>
    <p>The undersea habitat is a spherical branch-work the Mikaboshi king built with Datenseki. Ariu is a generation of that habitat given a name and a war. This page will not invent the king’s modern name. The desk has not been given one.</p>
    <h2>The Soga</h2>
    <p>Hiroto: clan head, Kurotsuchi, levitate or crush, among the strongest alive before Datenseki royalty walks onto Irishima. Yoshinojo: older, mustache and beard, cocky grin, unrelenting. Both die to Ariu on the island. Giyu, Hiroto’s ambitious younger brother, is willing to accept ceasefire terms that include handing Chiaki over. The prince does not need to be in every panel to warp the table. A people who can kill the head and the grinning veteran can demand a princess.</p>
    <p>Mashiro’s later death is the Bureau’s invoice. Shiba’s partner, Akuu, Kunishige sword at eighteen, alive in the talks. The same prince. The same mineral logic: adapted bodies win against unadapted ethics. Full clan page: <a href="../factions/soga.html">Soga and Mikaboshi</a>.</p>
    <h2>The Magatsumi camp</h2>
    <p>After chapter 119, explainers argued that Magatsumi is those insects recast in Kunishige’s steel: wartime blades as six royal sorcerers copied. Useful camp. Not a caption this page will print as fact. What is printed: once Magatsumi entered the field, Japan could walk onto the island. What is printed: Magatsumi has no three-count and overwrites other bodies. What is printed: Malediction, about 200,000 civilians. Visual echo is not lineage. The archive will not write “Magatsumi’s son” or “Magatsumi’s model sheet” until a chapter does.</p>
    <p>The camp lives next to the <a href="../world/techniques.html">insect kit</a> and the <a href="../analysis/irishima.html">vein essay</a>. When Jump makes it cheap to source, the camp becomes a sentence. Until then Ariu is the prince who kills two Soga on Irishima, poisons the air around a war for a vein, and later takes Mashiro off Shiba’s board.</p>
    <h2>Notes</h2>
    <p>Ariu Mikaboshi (亜利雨 箕加星). Sumika. Crown prince. Camp, not caption. For Chiaki, see <a href="chiaki.html">Chiaki Soga</a>. For the Sword Master the country will build, see <a href="akemura.html">Akemura</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Soga and Mikaboshi", "../factions/soga.html"),
        ("Mashiro", "mashiro.html"),
        ("Irishima’s vein", "../analysis/irishima.html"),
        ("Part 2", "../manga/part-2.html"),
        ("Technique catalog", "../world/techniques.html"),
    ],
)

character(
    "tenri",
    "Tenri Sazanami",
    "漣 天理",
    "Sazanami · the Tou",
    "Younger brother. Short blades. A half-stable Datenseki tool to impress Kyora. Jellyfish, then the pop.",
    "p-tenri",
    "../assets/portraits/kyora.webp",
    "The auction house’s son who died of the mineral lesson.",
    [
        ("Clan", '<a href="../factions/sazanami.html">Sazanami</a> · Tou'),
        ("Father", '<a href="kyora.html">Kyora Sazanami</a>'),
        ("Siblings", "Soya, Tamaki, Enji, Hakuri"),
        ("Tools", "Short blades; half-stable Datenseki; jellyfish manifestation"),
        ("Status", "Deceased at the 208th Rakuzaichi"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Tenri Sazanami is Kyora’s younger son, one of the Tou, the four-person Special Defense Corp that protects the Rakuzaichi. He uses short blades. He wants his father to be proud. He uses a half-stable Datenseki tool against <a href="chihiro.html">Chihiro</a>. Jellyfish manifestation, then the pop. He dies of the lesson <a href="../analysis/irishima.html">Part 2 is currently smelting in public</a>: the mineral without Kunishige’s eyes is a crater. Sojo died of the same lesson at industrial scale. Tenri dies of it as a boy trying to be useful.</p>
    <p>He is not Hakuri. Hakuri is the discarded son who becomes the building. He is not Soya. Soya is the heir, obsessive, later amnesiac. Tenri is the son who passed the test long enough to die passing. The archive will not make him a saint. It will not make him a footnote. A Datenseki death in the auction house is a preview of the vein. Volume 4’s stretch holds it.</p>
    <h2>Personality</h2>
    <p>Desperate to make Kyora proud is the printed engine. The eleventh head sacrifices children to keep a calendar. Tenri internalizes the calendar and tries to become a date worth keeping. Envy used to run the other way: Soya envious of Tenri’s superior sorcery, then Soya fixated on the “untalented” brother instead. Tenri’s talent is not enough to survive a stone that wants to pop the user. Talent is not eyes.</p>
    <p>Tamaki lies to Kyora that Soya is unwell. Tenri corrects her. That small cruelty (truth as loyalty to the father) belongs on this page. He is a good Tou in the firm’s sense. The firm’s sense is the crime. Shiba will later tell Enji to live and raise what is left so another child does not eat a stone. Tenri is the child who already ate it.</p>
    <h2>Abilities</h2>
    <p>Short blades. Isou as family art, spent the way a son of the Tou spends it. The Datenseki tool is the chapter’s weapon and the chapter’s moral. Jellyfish manifestation is the image the register holds: a sea-shape, then instability, then the pop. This page will not invent a named kata list. The panels are the textbook. The pop is the last page of the textbook.</p>
    <p>Cloud Gouger’s residual charges and Kyora’s Magatsumi proxy are louder arts in the same arc. Tenri’s stone is quieter and ruder. It says: you do not need to be Sojo to die of Datenseki. You can be a son in an auction house with something to prove.</p>
    <h2>Story role</h2>
    <p>The 208th Rakuzaichi lists Shinuchi. Chihiro meets Hakuri. Hiyuki arrives. Yura walks the floor. Tenri dies trying to be the household military. Hakuri awakens. Kyora dies in the Storehouse touching a masterpiece he listed and did not understand. The firm ends. Soya crawls out with amnesia. Enji begs to die. Tamaki has already lied. Hakuri walks out as the warehouse. Tenri does not walk out.</p>
    <p>Part 2’s smelting chapters (125–129) make this death look like a syllabus. Kunishige nearly dies in the shop in chapter 129. Chiaki pulls him back. The mineral wants to pop the user. Tenri is the present-tense quiz the class already failed. If you love the kiln and skip the auction son, you are reading the work without the household cost. If you love Hakuri and skip the stone, you are reading the inheritance without the invoice the other brother paid.</p>
    <h2>Notes</h2>
    <p>Tenri (漣 天理). Tou. Short blades. Datenseki pop. Jellyfish. For the father, see <a href="kyora.html">Kyora</a>. For the discarded son, see <a href="hakuri.html">Hakuri</a>. For the heir who lived, see <a href="soya.html">Soya</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Sazanami", "../factions/sazanami.html"),
        ("Hakuri", "hakuri.html"),
        ("Kyora", "kyora.html"),
        ("Soya", "soya.html"),
        ("Rakuzaichi", "../arcs/rakuzaichi.html"),
    ],
)

character(
    "soya",
    "Soya Sazanami",
    "漣 宗也",
    "Sazanami · heir",
    "The older brother who treated Hakuri as defective stock, lost to the house when the house finally answered, and crawled out of the rubble with amnesia and the same appetite.",
    "p-soya",
    "../assets/portraits/hakuri.webp",
    "Heir apparent. The volume extra is a gag, not a redemption.",
    [
        ("Clan", '<a href="../factions/sazanami.html">Sazanami</a> · Tou'),
        ("Father", '<a href="kyora.html">Kyora Sazanami</a>'),
        ("Siblings", "Tenri, Tamaki, Enji, Hakuri"),
        ("After the 208th", "Amnesia; deduces he is Sazanami; rediscovers harming the weak"),
        ("Extra", "<em>Soya Sazanami’s Memories, Begone!</em>"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Soya Sazanami is the older brother, heir apparent, Tou. Obsessive about <a href="hakuri.html">Hakuri</a>. Twisted affection as abuse. Once envious of Tenri’s superior sorcery, later fixated on the “untalented” brother. He demands Hakuri’s return, then resolves to kill him, then loses when Hakuri masters the house. After the building falls he crawls out with amnesia, deduces he is Sazanami, and rediscovers a love of harming the weak. The tankōbon extra, <em>Soya Sazanami’s Memories, Begone!</em>, is a gag about memories he would like to misplace. It is not a redemption.</p>
    <p>He walked out of the Rakuzaichi alive. Tenri did not. Kyora did not. Hakuri walked out as the warehouse. Soya walked out as a question the later chapters can still ask: who still answers to the name, who still knows Isou, who still thinks people are inventory.</p>
    <h2>Personality</h2>
    <p>Obsessive is the word the household page already spent, and it is the right one. Soya’s attention is a kind of violence. Hakuri was beaten into believing he had no talent. Soya is one of the people who did the teaching. Envy of Tenri flipped into a project: the defective brother as an object to retrieve, then to erase. Volume 4’s title is <em>Equal</em>. Soya is the relationship the clan refused to grant, standing in the way of it.</p>
    <p>Amnesia after the fall is not a soft reset. He deduces the clan. He rediscovers the appetite. The extra packed with the volume is the clan’s emotional illiteracy as a four-page joke. Buy the book for that. This site does not host it. The joke does not make him safe. It makes him readable as the same man with fewer files.</p>
    <h2>Abilities</h2>
    <p>Isou, the clan’s burial-force technique, spent as an heir spends it. He is Tou: one of the four best fighters in the firm, which is not the same as being one of two people in clan history to hold Storehouse as well. Hakuri becomes the rare dual inheritance. Soya remains the common one: force without the warehouse, status without the architecture. That is why the awakening scene is a humiliation and a birth at once.</p>
    <p>This page will not invent a unique named extension the magazine did not print. The heir’s kit is the house style plus the heir’s cruelty. After amnesia the kit is whatever a body remembers when the name comes back.</p>
    <h2>Story role</h2>
    <p>He is the older brother in the Rakuzaichi arc, the Toughest version of “come home” the discarded son has to refuse. Hakuri chooses Chihiro. Isou answers. Storehouse opens because Hakuri remembered a woman the auction killed, not because Soya lectured him. The 208th ends. The clan goes into hiding. Soya’s survival means the name can still walk into a later chapter and make Hakuri’s past a present-tense problem.</p>
    <p>Tamaki lies to Kyora that Soya is unwell. Tenri corrects her. Enji begs Shiba for death after Tenri and is told to live. The four Tou are a family military that dies or fails of the father’s calendar. Soya’s failure is the one that keeps breathing. That is worse for everyone who has to meet him again.</p>
    <h2>Notes</h2>
    <p>Soya (漣 宗也). Heir. Amnesia. Extra. For the firm, see <a href="../factions/sazanami.html">Sazanami</a>. For the extras desk, see <a href="../fun/oneshots.html">bathhouse and extras</a>. Official chapters: VIZ / MANGA Plus. Buy the volumes for the gag; this site does not host it.</p>
    """,
    [
        ("Hakuri", "hakuri.html"),
        ("Tenri", "tenri.html"),
        ("Sazanami", "../factions/sazanami.html"),
        ("Rakuzaichi", "../arcs/rakuzaichi.html"),
        ("Volume extras", "../fun/oneshots.html"),
    ],
)

print("wave2b a: hagiwara mashiro hinao itsuo ariu tenri soya")
