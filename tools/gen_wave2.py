#!/usr/bin/env python3
"""Second-wave character files. Facts from the archive's own scrape. No em-dashes."""
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
    "toto",
    "Toto",
    "斗斗",
    "Hishaku · blood trail",
    "The Hishaku’s extraction specialist: she reads blood, she holds the fire-gate, and she is the reason a kidnapping still has a schedule when Kuguri forgets it.",
    "p-toto",
    "../assets/portraits/hiruhiko.webp",
    "Hishaku company. Toto hunts with Kuguri; the fire-gate is her habit.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Sorcery", "Blood tracking and extraction"),
        ("Role", "Finder, sample-reader, fire-gate rescue"),
        ("Partners", '<a href="kuguri.html">Kuguri</a> on the Iori job; Hiruhiko on earlier retrievals'),
        ("Known samples", "Samura’s blood at Senkutsuji; Sengoku’s head at the hotel"),
        ("Arc", '<a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a>'),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Toto is one of the eight named <a href="../factions/hishaku.html">Hishaku</a>. She is not the mind of the set. <a href="yura.html">Yura</a> decides which blade goes to which monster. She is not the swordsman who wants a historic duel. That is <a href="hokuto.html">Hokuto</a>. She is not the eighteen-year-old who treats friendship as a weapon. That is <a href="hiruhiko.html">Hiruhiko</a>. Toto is logistics with a body. Blood is a signature. A severed head is a page. The shared fire-gate is a door she prefers to a cut.</p>
    <p>The Iori job is her longest printed room. After Senkutsuji, she has a sample taken off <a href="samura.html">Seiichi Samura</a>. That is enough to find <a href="iori.html">Iori</a>. <a href="kuguri.html">Kuguri</a> is sent to close. Toto is sent to keep the close from becoming a funeral for the wrong Hishaku. At the Kyoto Bloodshed Hotel she reads <a href="../world/hotel.html">Yojiro Sengoku</a>’s severed head the same way she reads a living trail. The building has a style. She has a schedule. Kuguri drops the schedule when Chihiro’s fake Iai gets serious. Toto does not. That split is the ten in miniature: one member falls in love with the fight, one member still remembers they came for a girl.</p>
    <p>Eight of the ten are named on this site. Toto is one of the named. This archive will not invent the remaining two. It will also not invent a childhood, a recruitment scene, or a textbook title for the blood art. The chapters through 129 have given her work, not a biography. The work is enough to file.</p>
    <h2>Personality</h2>
    <p>She prefers the fire-gate to the cut. That is not cowardice in this book. It is a professional opinion about which object is worth standing next to. Hokuto wants a deadly battle. Kuguri wants a sword that will finally sign him. Hiruhiko wants a peer. Toto wants the people she was sent with to leave the room alive enough to be sent again. Extraction is a personality. The ten can afford one member who thinks getting out is a technique.</p>
    <p>She is not comic relief and she is not a silent extra. When Kuguri abandons the kidnapping, someone in the pairing still has to be the adult. The pages give that job to the woman who can find a person from a stain. She is ruthless in the way a tracker is ruthless: the target is a problem of information, not a speech. Iori is a lever against Samura. Sengoku is a sample. Chihiro is an obstacle who happens to be learning a school in the same corridor. Toto files all three under the same heading: work.</p>
    <p>Readers who want her to be “the nice Hishaku” will be disappointed. Fire-gate rescue is not kindness. It is inventory control. Yura did not staff the ten with a medic. He staffed it with a person who can pull comrades out of fatal rooms so the method can continue tomorrow. Toto is why Hiruhiko and Kuguri are still in the book after Kyoto. That is not a favor. That is the clan’s only manners: use.</p>
    <h2>Abilities</h2>
    <p>Blood tracking and extraction. A sample taken off Samura at Senkutsuji is enough to locate Iori. A severed head at the hotel is enough to keep reading. The archive will not invent a named kata or a range in kilometers. What the panels show is a specialist who treats spilled life as a map. Anyone who has bled in front of her has given her a door. Anyone who thinks a safehouse is safe because the lights are off has not met the woman who does not need lights.</p>
    <p>The shared fire-gate is available to all ten. Toto uses it as a habit. The tattoos are the uniform; the gate is the logistics. When the Kyoto scene turns fatal (Play taking the upper floors apart, Samura arriving because two Enchanted Blades in one hotel is a beacon Owl can see) she is the reason Kuguri is extracted rather than finished. Hokuto would rather close distance with steel. Toto would rather the steel leave through a door that is not a window.</p>
    <p>She is not Yukisada. Regeneration is a different desk. She is not Bingo. Lion-dancer heads are a different kind of body. She is the member you send when the problem is “where” rather than “how hard.” That is why the Iori job is Toto-and-Kuguri rather than Toto-and-Hokuto. Find, then close. The close got distracted. The find did not fail.</p>
    <h2>Story role</h2>
    <p>After a Sanso falls and Senkutsuji becomes a surgery, Samura’s Owl goes up nationwide. The Hishaku want Iori as a lever so the fastest bearer will flinch. Toto has the blood. Sumi of the Masumi puts Iori on a motorcycle. Kuguri gives chase. The Kyoto Bloodshed Hotel, Reigen One-Sword Style, Yojiro Sengoku, is the Masumi’s chosen veil. Chihiro is there to tell Iori the truth rather than re-seal it. Toto is there to make sure the veil is not actually dark.</p>
    <p>Sengoku dies. Toto reads the head. That sentence is the hotel’s ethics in one cut: a swordsman who taught a staff a style becomes a page in a tracker’s book. Ikura, Iori’s classmate, trails Toto and is part of why the memory seal finally breaks; Iori shields him. The kidnapping fails because a girl chose a person, not because Toto lost the trail. Hiruhiko wrecks the upper floors with Play. Samura walks into the duel. Toto pulls who she can through the gate. The building remains a ruin. The ten remain a method.</p>
    <p>She is not the face of the later HQ infiltration. That photograph is Yura, Hokuto, Yukisada in the barrier, Bingo’s lucky charms. Toto’s chapter of the book is the hotel and the jobs that look like retrieval: find Chihiro after a death, find Iori after a temple, get the loud ones out before the father arrives. Without her, Kuguri’s classroom has no extraction. Without her, the Iori plan is a swordsman wandering Kyoto hoping to smell a girl. The long book needs a tracker because Enchanted Blades are not the only things that leave a signature. People do.</p>
    <h2>Notes</h2>
    <p>Toto is she. Recaps that default the ten to a list of men will misfile the extraction specialist and then wonder why the hotel has a schedule. Kuguri is the partner who falls in love with Chihiro’s imitation. Hiruhiko is the other Kyoto Hishaku, already beaten once on the train, already contracted to Kumeyuri. Sengoku is the sample. Ikura is the civilian who walked into a tracker’s job and became the reason a seal broke. Chapter 67 through 74 are the hotel rooms. “Imitate” and “Iai White Purity Style” are Kuguri’s classroom titles. Toto is the woman still holding the clock in those same chapters.</p>
    <p>Two of the ten stay unlabeled. This archive will not invent them, and it will not invent Toto’s age, master, or a childhood in a village the magazine has not drawn. For the clan, see <a href="../factions/hishaku.html">Hishaku</a>. For the building, see <a href="../world/hotel.html">the Kyoto Bloodshed Hotel</a>. For the unwilling instructor, see <a href="kuguri.html">Kuguri</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Kuguri", "kuguri.html"),
        ("Iori", "iori.html"),
        ("Kyoto Bloodshed Hotel", "../world/hotel.html"),
        ("Hiruhiko", "hiruhiko.html"),
    ],
)

character(
    "yukisada",
    "Yukisada",
    "幸禎",
    "Hishaku · the Vessel",
    "Seventeen. Yura calls him the strongest fighter among the ten. He regenerates past decapitation, then becomes the boy you ask to hold a government building.",
    "p-yukisada",
    "../assets/covers/jp-vol11.webp",
    "Volume 11, Heroes. Yukisada is the lock on the cell even when the jacket shows Chihiro.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Age", "17"),
        ("Sorcery", "Regeneration past decapitation; HQ barrier Vessel"),
        ("Rank in the ten", "Strongest fighter, per Yura"),
        ("Jacket", "Volume 11, <em>Heroes</em>, as the lock behind the snow"),
        ("Arc", "Kamunabi headquarters; late Sword Bearer Assassination"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Yukisada is the youngest named <a href="../factions/hishaku.html">Hishaku</a> and the one Yura is willing to call the strongest fighter in the set. That sentence should sit next to his age. Seventeen. Regeneration that survives the head coming off. Later, a Vessel so he can manipulate Kamunabi headquarters’ barrier from the inside, splitting control with the state’s own vessel and shutting the building against relief. A boy who cannot stay dead is a boy you can ask to hold a building. The manga does not sentimentalize the hiring.</p>
    <p>He is not the mind. Yura walks to the cell. He is not the historic duel. Hokuto wants Uruha. He is not the hotel tracker. Toto wants a sample. Yukisada is the reason Azami cannot simply call <a href="shiba.html">Shiba</a> until the field is restored. Hakuri, <a href="kiri.html">Kiri</a>, and <a href="hagiwara.html">Hagiwara</a> cannot kill him cleanly. The solution that works is Storehouse: remove the Kamunabi vessel from the split rather than win a regeneration duel. The auction house’s discarded son is how you unmake a boy who is also architecture.</p>
    <p>Volume 11 is titled <em>Heroes</em>. The chapter index puts quotation marks on the word because the press already used it. Yukisada is the lock on the cell in that book even when the jacket shows Chihiro, goldfish, snow. Part 1’s last political fact is that the state which covered up Malediction has been possessed by Malediction’s author. Yukisada is how the ten held the door while that fact finished happening.</p>
    <h2>Personality</h2>
    <p>The pages do not give him a monologue about justice. They give him a job and a body that will not quit. Seventeen is young for that job. The manga does not write him as a child who wandered into a cult. It writes him as a member. The age is a fact. The work is the work. Readers who want a tragic recruitment chapter will have to wait; chapter 129 has not printed one.</p>
    <p>Yura’s praise (strongest fighter) is not a nickname Chihiro invented. It is the leader of the ten telling the room which monster to budget for. That matters because the Hishaku labor split is easy to misread as “Yura thinks, Hokuto cuts, Hiruhiko plays.” Yukisada is the other end of the spectrum: a combatant so expensive that the correct answer is not to fight him. Hakuri’s Storehouse is the correct answer. The book has been teaching that lesson since the Rakuzaichi. The headquarters chapters spend it on a teenager.</p>
    <p>He is not Hiruhiko. Hiruhiko is loud and wants a friend-shaped rival. Yukisada’s printed self is quieter and worse: a regenerative wall with a barrier contract. If there is an interiority waiting (why he said yes, whether the regeneration predates the tattoos, whether he wanted the Vessel job), the magazine has not opened it. This file will not invent a diary.</p>
    <h2>Abilities</h2>
    <p>Regeneration past decapitation. Most sorcerers die when the neck is cut. Yukisada continues. The technique is not given a textbook name this archive will treat as official. The effect is. Heads come off. The boy stands up. That is enough to make him a deterrent in rooms where other Hishaku would rather not spend a senior, and enough to make Kiri’s vow-shaped odachi the wrong tool. You cannot decapitate your way out of a person who treats decapitation as a pause.</p>
    <p>The Vessel job is the second art, or the first art spent as architecture. Barriers in this manga have people inside them. Yukisada becomes the Hishaku’s half of Kamunabi headquarters’ barrier, splitting control with the Kamunabi’s own vessel. The building shuts against relief. Azami’s teleporting friend cannot be invited in until the field is a field again. Hagiwara, already a commander with no legs, is still in the building and still not enough. The fight is not a duel. It is a property dispute inside a contract.</p>
    <p>Hakuri’s answer is the clan trick the Sazanami spent two centuries on: register, remove, do not siege. Take the Kamunabi vessel out of the split. Do not try to out-heal the boy. Storehouse-as-Kamui is the lazy comparison. The interesting version is inheritance used against a teenager who is currently a government building. See <a href="../world/storehouse.html">the Storehouse desk</a>.</p>
    <h2>Story role</h2>
    <p>He arrives in the present tense when the Hishaku stop being a rumor in a cellar and become a problem inside the state’s own address. Kasen’s leak is already on the table. Yura starts spending Magatsumi at range without drawing it. Hokuto wants the swordsmen in the corridor. Yukisada sits in the barrier. Volume 10 is <em>The Swordsmen</em>. Volume 11 is the lock. You cannot have a cell conversation if the building still belongs to the people who sealed the cell.</p>
    <p>Kudo dies for Hakuri in the same campaign. Uruha, contract cut, Crimson Recital limping back, walks into the raid to keep the walking Storehouse alive. Those two facts belong next to Yukisada. The ten need Hakuri dead or held because Hakuri is how you unmake Yukisada without winning a regeneration argument. The Kamunabi need Hakuri alive for the same reason. The discarded son is the only key that fits a boy-shaped door.</p>
    <p>Yura offers the body. <span class="spoiler">Akemura stands up in the leader. Part 1 ends with the Sword Master loose and the auction house already gone. Yukisada’s job in that last movement is not to become the new mind. It is to have held the room long enough for the mind to change species.</span> After that, this page will not invent a new org chart. Possession is not a merger. The ten do not automatically become Akemura’s squad because a barrier sat still.</p>
    <h2>Notes</h2>
    <p>Eight named. Two unlabeled. Yukisada is the named boy. Read him next to chapter titles that put quotation marks on “Heroes,” “Strongest,” “Sword Master.” The press used those words after the war. The long book uses them as captions on a headquarters fight. For the commander who cannot kill him, see <a href="hagiwara.html">Ikuto Hagiwara</a>. For the granddaughter with the odachi, see <a href="kiri.html">Kiri Shirakai</a>. For the architecture, see <a href="hakuri.html">Hakuri</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Hakuri", "hakuri.html"),
        ("The Storehouse", "../world/storehouse.html"),
        ("Hagiwara", "hagiwara.html"),
        ("Yura", "yura.html"),
    ],
)

character(
    "bingo",
    "Bingo",
    "瓶伍",
    "Hishaku · Demon Bite",
    "Lion-dancer heads that punish you for breaking them, a man who eats corpses to keep the charms fed, and a nap in the middle of a government building.",
    "p-bingo",
    "../assets/covers/jp-vol10.webp",
    "Hishaku muscle on the HQ floor. The lucky charms are not a festival joke.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Sorcery", "Mako (魔咬, Demon Bite): lion-dancer heads / lucky charms"),
        ("Side effect", "Eats corpses to fuel the art; then gets sleepy"),
        ("Punish mechanic", "Destroying a charm stacks invisible weight on the destroyer"),
        ("Role", "Headquarters infiltration muscle"),
        ("First printed room", "Late Sword Bearer Assassination / HQ"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Bingo is one of the eight named <a href="../factions/hishaku.html">Hishaku</a>. He looks like a festival until the heads start moving. <strong>Mako</strong> (魔咬), Demon Bite: lion-dancer constructs the text also calls lucky charms, mouths that hit hard. Destroying them stacks an invisible weight on whoever did the destroying. He can turn his own head into a charm. He eats corpses to fuel the art. Then he gets sleepy. The archive keeps all of that on the same page because the manga does.</p>
    <p>He is headquarters muscle, not the hotel tracker and not the barrier boy. Toto finds. Yukisada holds the building. Bingo fills the corridors with bodies that are not quite people so the ten can lose a head without losing a sorcerer. The Shigyu brothers are hired chaos in the same campaign; Azami kills both. Bingo is staff. Hirelings die. Charms get heavier.</p>
    <p>This file will not promote him into a weekly final boss. The pages have not given him a domestic scene, a flashback, or a jacket of his own. They have given him a kit that makes cleanup expensive and a sleep that makes him look like a joke until you remember he just ate someone. That is enough for a desk.</p>
    <h2>Personality</h2>
    <p>The nap is characterized as rhythm, not as a gag the author forgot to cut. Tired monsters are still monsters. A sleeping Hishaku is still a Hishaku. Chihiro does not get to treat Bingo as comic relief because the lion-dancer silhouette is funny in a festival parade. In a Kamunabi hallway the silhouette is a mouth.</p>
    <p>Corpse-eating is not metaphor and it is not cuisine writing. Bingo consumes the dead. The implication is logistical before it is aesthetic. A man who eats corpses leaves fewer bodies for the Kamunabi to read. Toto reads blood; Bingo removes the rest. The ten’s manners are use. Bingo is useful in the ugliest register the book has printed for them.</p>
    <p>He is not Hiruhiko. There is no printed speech about friendship. He is not Kuguri. There is no unrequited blade. He is the member you send when you need extra bodies in a building you do not own yet. If a later chapter gives him a wish, this page will add it. Until then the wish is implied: keep the charms fed, then sleep.</p>
    <h2>Abilities</h2>
    <p>Mako’s lion-dancer heads are festival objects in the world outside the panel. Inside the panel they are weapons, decoys, and traps. You can send a head into a room where you would not send Uran. You can lose a construct and not lose a sorcerer. The stacked weight is the mean clause. The correct play is not “break all the heads.” The correct play is “do not play the game the charms want.” The book does not always give Chihiro’s side that luxury.</p>
    <p>Turning his own head into a charm is the kit folding back onto the user. Regeneration is Yukisada’s miracle. Bingo’s version is ruder: the body becomes another lucky object. Eating corpses fuels the art. Sleep follows. The cycle is a design brief. Fuel, swarm, crash. Headquarters is a long enough fight for the crash to matter. A sleepy infiltrator is still an infiltrator who already spent the dead.</p>
    <p>He shares a building with Yukisada’s barrier and Yura’s remote Magatsumi. Those are the expensive arts. Mako is the cheap-looking one that turns out to have a tax. Weight is a tax. Sleep is a tax. Corpses are a tax the ten are willing to pay because the building is full of them.</p>
    <h2>Story role</h2>
    <p>Bingo’s printed room is the HQ infiltration, when the Hishaku stop raiding Sanso fortresses and walk into the address that holds Magatsumi. Kasen’s leak has already done its work as policy. Yura spends Shinuchi at range. Yukisada splits the barrier. Hokuto looks for a swordsman. Bingo looks like a parade and functions as area denial. The lucky charms keep relief expensive. The sleep keeps him from being a perpetual-motion machine. The book is cruel about both.</p>
    <p>He is not required for the cell conversation. Yura would walk to Akemura with or without lion-dancers. He is required for the sentence “the ten can occupy a government building.” Occupation is not a duel. Occupation is furniture that bites. Mako is furniture that bites.</p>
    <p>After Yura’s body is no longer Yura’s, this page will not invent Bingo’s new loyalty. The ten are a method, not a hive mind. Flame tattoos and a fire-gate do not become Akemura’s uniform because the leader offered a spine. What is printed: charms, weight, corpses, sleep, a headquarters. The catalog places Mako next to Twilight Wave and Blood Crane. The org page places Bingo next to Uran as a name that finally has a room.</p>
    <h2>Notes</h2>
    <p>Eight named. Two unlabeled. Bingo is the named lion-dancer. Uran, ice, still has her own file as of this pass; she is the raid’s breath, not the HQ’s parade. For the building he occupies, see <a href="../factions/kamunabi.html">Kamunabi</a>. For the boy holding the barrier, see <a href="yukisada.html">Yukisada</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Yukisada", "yukisada.html"),
        ("Yura", "yura.html"),
        ("Technique catalog", "../world/techniques.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
    ],
)

character(
    "uran",
    "Uran",
    "右嵐",
    "Hishaku · ice",
    "Ice on the breath. One of the three who stood in the Rokuhira house the night the smith died.",
    "p-uran",
    "../assets/portraits/yura.webp",
    "Named with the raid. The pages have given her ice and a night, not a jacket.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Sorcery", "Ice; breath that freezes and restrains"),
        ("Known for", "Present at Kunishige’s murder with Hokuto and the third raider"),
        ("Status in the ten", "Named; raid veteran"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Uran is one of the eight named <a href="../factions/hishaku.html">Hishaku</a>. Ice. A breath that freezes and restrains. She stood in the Rokuhira house with <a href="hokuto.html">Hokuto</a> and the third raider the night <a href="kunishige.html">Kunishige</a> died. The six wartime blades left in their hands. Enten stayed with the son. That is the whole of her first printed fact, and it is already enough to put her on the site’s worst list. Recaps that talk as if only Yura walked into the workshop are doing Hokuto and Uran a courtesy they have not earned.</p>
    <p>She is not the mind. She is not the hotel. She is not the Vessel. She is the raid’s weather. Three sorcerers were enough to kill a hermit smith and steal a cellar. The book has spent three years of story showing what that night cost everyone else. Uran is one of the three bodies who made the cost.</p>
    <p>The pages have not yet given her a room of her own in the present-tense HQ fight. This file exists anyway. A named raider does not get to live only as a caption on Yura’s page. Eight names. Two unlabeled. She is a name.</p>
    <h2>Personality</h2>
    <p>The magazine has not printed a monologue. What can be said without invention: she is staffed for restraint. Ice that holds is a different brief from Hokuto’s sword that wants a historic death. The workshop needed someone to keep a household from becoming a running fight long enough for the theft to finish. Breath that freezes is how you pause a room. The third raider is still unlabeled. This archive will not invent that person, and it will not invent Uran’s feelings about the goldfish bowl.</p>
    <p>Readers looking for a “sympathetic Hishaku” will not find a childhood here. The raid is the character. Everything after is unprinted. The honest page is short where the text is short and long where the implication is long. The implication is: Chihiro’s father died in a room that included this woman’s weather.</p>
    <h2>Abilities</h2>
    <p>Ice. Breath that freezes and restrains. The catalog will not invent a three-count or a True Realm. Innate arts in this book do not owe the reader a numbered list. What the panels support is control: hold a body, hold a doorway, hold the seconds a swordsman needs to finish a civilian. Cloud Gouger’s Yui is ice as an Enchanted Blade technique. Uran’s ice is hers. She did not need a stolen weather sword to make a workshop cold.</p>
    <p>She shares the fire-gate and the tattoos with the rest of the ten. Toto is the one who uses the gate as a habit. Uran’s printed use is the night, not the extraction. If a later chapter shows her freezing a headquarters corridor, this page will add the corridor. Until then the workshop is the room.</p>
    <h2>Story role</h2>
    <p>Three years before page one, three Hishaku hit the house. Hokuto is named. Uran is named. The third stays unlabeled, and this archive will not fill the blank. Kunishige dies in front of Chihiro. The six wartime swords leave. Shortly after, Hokuto murders Ibuki so Cloud Gouger’s contract opens. Uran’s name is not on Ibuki’s kill. It is on the smith’s. That is the worse line if you are Chihiro. The first wartime sword’s death is a method. The father’s death is the plot.</p>
    <p>Yura ordered the raid. Kasen leaked the address. Uran walked into the address. The leak as policy lives on <a href="../analysis/leak.html">the leak essay</a> and on <a href="kasen.html">Kasen</a>’s file. The walk lives here. Without the three, there is no underworld Chihiro, no Cafe Haru Haru as a sit-down, no Enten carried into Tokyo as a job. The present tense is a three-year commute away from Uran’s breath.</p>
    <p>She remains in the ten. Present-tense spotlight has gone to Yura, Hokuto, Hiruhiko, Kuguri, Toto, Yukisada, Bingo. Uran is the reminder that the raid was not two famous men and a fog. It was a crew. Ice is a crew skill.</p>
    <h2>Notes</h2>
    <p>Eight named. Two unlabeled. The third raider is not automatically one of the two unlabeled present-tense members; the book has not done that math in a caption. This page will not either. For the swordsman on the same night, see <a href="hokuto.html">Hokuto</a>. For the house, see <a href="kunishige.html">Kunishige</a> and <a href="chihiro.html">Chihiro</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Hokuto", "hokuto.html"),
        ("Kunishige", "kunishige.html"),
        ("Kasen", "kasen.html"),
        ("The leak", "../analysis/leak.html"),
    ],
)

print("wave2 a: toto yukisada bingo uran")
