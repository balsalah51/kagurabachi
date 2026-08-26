#!/usr/bin/env python3
"""Countdown-era encyclopedia wave: characters, rooms, essays, shop, watch. No em-dashes."""
from page_lib import page, crumb, hero, infobox


def toc(*items):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<nav class="toc"><strong>On this page</strong>\n      <ol>{lis}</ol>\n    </nav>\n'


def related(*pairs):
    return '<p class="related">' + "".join(f'<a href="{h}">{t}</a>' for h, t in pairs) + "</p>"


def clock(note=None):
    live = note or "Counted to 1 April 2027, 00:00 Japan. A first-episode date lands when they print one."
    return f'''<div class="clock-band" data-clock>
  <p class="clock-kicker">Until the first broadcast</p>
  <p class="clock-label">April 2027 · Cypic · Japan time</p>
  <div class="clock" role="timer" aria-label="Countdown to the Kagurabachi anime">
    <div class="clock-unit"><span class="clock-num" data-d>000</span><span class="clock-unit-label">Days</span></div>
    <div class="clock-unit"><span class="clock-num" data-h>00</span><span class="clock-unit-label">Hours</span></div>
    <div class="clock-unit"><span class="clock-num" data-m>00</span><span class="clock-unit-label">Minutes</span></div>
    <div class="clock-unit"><span class="clock-num" data-s>00</span><span class="clock-unit-label">Seconds</span></div>
  </div>
  <p class="clock-note" data-clock-live>{live}</p>
</div>
'''


def char(rel, title, desc, kicker, name, jp, lede, pclass, img, caption, rows, headings, article, rels):
    box = infobox(name, jp, pclass, img, caption, rows)
    body = (
        crumb(("Characters", "index.html"), title)
        + hero(kicker, name, jp, lede)
        + f'<div class="layout">{box}\n      <article class="article">\n    {toc(*headings)}{article}\n        {related(*rels)}\n      </article>\n      </div>'
    )
    page(rel, title, desc, body)


# --- Kamunabi leaders ---

char(
    "characters/ichiki.html",
    "Ichiki",
    "Kamunabi leader. Elderly, small, White Robe. Trained Shiba and Azami. Sealed Shinuchi. Hid Kunishige.",
    "Kamunabi · White Robe",
    "Ichiki",
    "壱鬼",
    "Small enough to miss in a hallway. Old enough to have trained the two men who still argue about the smith. He helped seal Shinuchi and then helped hide the man who made it.",
    "p-ichiki",
    "../assets/portraits/azami.webp",
    "Leadership table. Ichiki trained the two who stayed and the one who left.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Office", "Leader; White Robe"),
        ("Arts", "Learned arts and physical combat"),
        ("Students", '<a href="shiba.html">Togo Shiba</a>, <a href="azami.html">Soshiro Azami</a>'),
        ("War work", "Sealed Shinuchi with Kasen and Yatsuru; hid Kunishige"),
    ],
    ["Overview", "The teacher", "The seal and the hide", "Notes"],
    """
    <h2>Overview</h2>
    <p>Ichiki sits on the Kamunabi leadership table with <a href="kasen.html">Kasen</a>, <a href="yatsuru.html">Yatsuru</a>, <a href="azami.html">Azami</a>, <a href="izaru.html">Izaru</a>, and <a href="kudo.html">Kudo</a>. Elderly. Small. One of the White Robes: the learned core that can keep a masterpiece in a box. After the Seitei War he sealed <a href="../blades/magatsumi.html">Shinuchi</a> with Kasen and Yatsuru. He also helped hide <a href="kunishige.html">Kunishige Rokuhira</a>. Those two sentences are the same man holding two different national jobs: lock the blade, then lock the smith so the blade cannot be a policy again.</p>
    <p>He is not the director. Kasen mailed an address. He is not the prosecutor. Izaru talks as if the smith stole national property. He is the teacher. <a href="shiba.html">Shiba</a> and Azami trained under him during the war. One stayed inside the bureau. One left when the smith hid. Ichiki remains at the table. The students still argue in two buildings. The teacher is the continuity.</p>
    <h2>The teacher</h2>
    <p>Physical combat and learned arts. The book does not give him a flashy innate signature because the job is not a named attack. The job is to make two teenagers into people who can survive an island. Shiba becomes teleportation and extraction. Azami becomes Coin and an executioner’s manners. Both of them later hide Kunishige. That is Ichiki’s curriculum coming due: not a style, a habit of keeping a person alive when the state wants a sword.</p>
    <p>Small and old is not comic relief. In a leadership room of beards, beads, gas-masks, and Coin, the smallest man is the one who remembers when the bureau was still an army and the students were still boys. Recaps that skip him because he has no volume jacket are skipping the reason Shiba and Azami can share a hallway without killing each other.</p>
    <h2>The seal and the hide</h2>
    <p>Shinuchi’s box is White Robe work. Kasen, Ichiki, Yatsuru. Eighteen years later a director’s leak and a Hishaku vessel named <a href="yukisada.html">Yukisada</a> split the headquarters barrier from the inside. The box was never only Kasen’s. Cracking it implicates the three. Ichiki’s other job, hiding the smith, is the one Kasen spent the other way. Several heads (Azami, Kudo, Ichiki) spent political capital keeping Kunishige alive after Malediction. Kasen spent it on an address.</p>
    <p>When Kudo dies for <a href="hakuri.html">Hakuri</a>, the table is lighter by one supporter. Ichiki is still small and old and the man who trained Shiba. The hide did not purchase every spine in the room. It purchased enough of them that a leak had to be a conspiracy instead of a vote. See <a href="../analysis/leak.html">the leak as policy</a>.</p>
    <h2>Notes</h2>
    <p>Ichiki (壱鬼). White Robe. Teacher of Shiba and Azami. Shinuchi seal. Kunishige hide. For the director who mailed the address, see Kasen. For the woman who shares the seal, see Yatsuru. For the org chart, see <a href="../factions/kamunabi.html">Kamunabi</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("kasen.html", "Kasen"), ("yatsuru.html", "Yatsuru"), ("azami.html", "Azami"), ("shiba.html", "Shiba"), ("../factions/kamunabi.html", "Kamunabi")],
)

char(
    "characters/yatsuru.html",
    "Yatsuru",
    "Kamunabi leader. Sole named woman among the heads. Barriers and sealing. Shinuchi seal. Yukisada splits her barrier from inside.",
    "Kamunabi · White Robe",
    "Yatsuru",
    "夜弦",
    "The sole named woman at the leadership table. Barriers and sealing. When Yukisada sits in the headquarters field, the thing being stolen is her life’s work.",
    "p-yatsuru",
    "../assets/portraits/azami.webp",
    "White Robe work. The box and the building are the same art.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Office", "Leader; White Robe"),
        ("Arts", "Barrier and sealing"),
        ("War work", "Sealed Shinuchi with Kasen and Ichiki"),
        ("Present tense", "HQ barrier; Yukisada splits it from inside"),
    ],
    ["Overview", "The art", "The theft", "Notes"],
    """
    <h2>Overview</h2>
    <p>Yatsuru is the sole named woman among the Kamunabi leaders. Barrier and sealing, the same learned work as <a href="kasen.html">Kasen</a> and <a href="ichiki.html">Ichiki</a>. After the war she is instrumental in the Shinuchi seal. Eighteen years later the masterpiece is still in a basement and she is still at the table. The book does not give her a volume jacket. It gives her the building. When <a href="yukisada.html">Yukisada</a> splits the headquarters barrier, her life’s work is the thing being stolen from inside.</p>
    <p>She is not Hiyuki. Hiyuki is a pointed end the state can aim at an auction. Yatsuru is the architecture that makes a god stay in a room. Recaps that flatten the leadership into Kasen-plus-Azami are missing the woman whose art is the field Yukisada inhabits. The Vessel is seventeen. The barrier is older. The theft is that combination.</p>
    <h2>The art</h2>
    <p>White Robes: Kasen, Ichiki, Yatsuru. Learned rather than a flashy innate signature. You keep Magatsumi in a box by being the kind of sorcerer who can tie a knot a nation will trust for eighteen years. You keep a headquarters from being a street by throwing a barrier a Hishaku teenager then sits inside. Both jobs are the same kit. Kasen used the kit and then mailed an address. Yatsuru used the kit and then watched a boy become the kit’s inverse: regeneration as occupancy.</p>
    <p>Shiba cannot come in until the field is restored. That sentence is Yatsuru’s page even when the panel is Shiba waiting. Teleportation is useless against a well-tied building. Yukisada’s job is to make the building a body. Yatsuru’s job was to make the body a building. One of them is seventeen. One of them did the war.</p>
    <h2>The theft</h2>
    <p>Yura spends Shinuchi at range. Yukisada sits in the barrier. Kudo dies for Hakuri. Azami kills the Shigyu brothers in a hallway. The leadership table’s prosecutor still distrusts Chihiro. Yatsuru’s printed room is the stolen field: not a duel, an inversion. The Hishaku did not smash the barrier from the street. They put a Vessel in it. You cannot cut a boy who will not stay dead, and you cannot restore a field while the boy is the field.</p>
    <p>After Kudo’s empty chair, the table still has a woman whose work is being occupied. The leak essay is Kasen. The Vessel page is Yukisada. This page is the stolen object. Official chapters: VIZ / MANGA Plus.</p>
    <h2>Notes</h2>
    <p>Yatsuru (夜弦). White Robe. Barriers. Shinuchi seal. For the director, see Kasen. For the teacher, see Ichiki. For the boy in the field, see Yukisada. Org: <a href="../factions/kamunabi.html">Kamunabi</a>.</p>
    """,
    [("kasen.html", "Kasen"), ("ichiki.html", "Ichiki"), ("yukisada.html", "Yukisada"), ("kudo.html", "Kudo"), ("../factions/kamunabi.html", "Kamunabi")],
)

char(
    "characters/izaru.html",
    "Izaru",
    "Kamunabi leader. Mutton chops, rosary bead chains. Distrusts Chihiro. Talks as if Kunishige stole the Enchanted Blades.",
    "Kamunabi · prosecutor",
    "Izaru",
    "亥猿",
    "Mutton chops. Rosary-like bead chains. The leadership table’s prosecutor: the smith stole national property, and the son is not a colleague.",
    "p-izaru",
    "../assets/portraits/azami.webp",
    "Beads and distrust. The hide was a theft in this chair.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Office", "Leader"),
        ("Arts", "Rosary-like bead chains; restrict a target"),
        ("Position", "Opposed hiding Kunishige; distrusts Chihiro"),
        ("Table", "Prosecutor opposite Azami, Ichiki, Kudo"),
    ],
    ["Overview", "The brief", "Beads", "Notes"],
    """
    <h2>Overview</h2>
    <p>Izaru is the Kamunabi head who talks as if <a href="kunishige.html">Kunishige</a> stole the Enchanted Blades. Mutton chops. Rosary-like bead chains that restrict a target. He criticized colleagues for hiding the smith. He distrusts <a href="chihiro.html">Chihiro</a> after the boy joins with Enten still in his hand. The leadership table is not a monolith. Azami, Kudo, and Ichiki spent capital on a hide. Kasen spent it on a leak. Izaru is the third position: the blades were national property, the hide was a theft, the son is a security problem wearing a seventh sword.</p>
    <p>He is not wrong about the steel being a state object. He is wrong about the household. Kunishige confiscated six swords after Malediction because the state had already filed a war crime as victory. Chihiro keeps Enten because the seventh blade is a retraction, not a trophy. Izaru’s prosecutor voice is useful because the book needs someone in the building to say the quiet part with beads instead of a mailed address. Kasen wanted the blades used. Izaru wants them not in a civilian’s son. Those are not the same hunger, and they share a hallway.</p>
    <h2>The brief</h2>
    <p>After the Rakuzaichi, Chihiro hands Magatsumi to the Kamunabi and keeps Enten by joining them. Hakuri’s Storehouse is why the table listens. Izaru’s distrust is why the listen is not a welcome. A boy who walked the underworld for three years, who let Enten scout an auction on its own charge, who still will not spend innocents, looks to a prosecutor like a leak with a goldfish. The leak was already in the director’s chair. Izaru is aiming at the wrong civilian.</p>
    <p>When headquarters becomes a battlefield, distrust is not a technique. Bead chains are. The page keeps both: the politics and the kit. Recaps that skip Izaru because he is not Hiyuki are skipping the reason Chihiro’s deal was never going to feel like a homecoming.</p>
    <h2>Beads</h2>
    <p>Rosary-like chains to restrict a target. Learned, visible, a restraint aesthetic in a bureau that also employs Flame Bone and Coin. Izaru’s art is the argument made physical: hold the person still until the property question is settled. Chihiro’s art is a household that will not sit still. The mismatch is the table.</p>
    <p>Kudo dies for Hakuri. Azami kills in the hallway. Yatsuru’s barrier is occupied. Izaru is still the prosecutor. The building can lose a spine and keep a brief. See <a href="../factions/kamunabi.html">the org chart</a> and <a href="../analysis/leak.html">the leak</a>.</p>
    <h2>Notes</h2>
    <p>Izaru (亥猿). Bead chains. Distrust. For the hide’s teacher, see Ichiki. For the hide’s strongest head, see Azami. For the son he will not trust, see Chihiro. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("kasen.html", "Kasen"), ("ichiki.html", "Ichiki"), ("azami.html", "Azami"), ("chihiro.html", "Chihiro"), ("../factions/kamunabi.html", "Kamunabi")],
)

char(
    "characters/ikura.html",
    "Ikura",
    "Iori’s classmate. A loner who trails Toto. Iori’s memory seal breaks when she shields him at the Kyoto Bloodshed Hotel.",
    "Kyoto · classmate",
    "Ikura",
    "井倉",
    "Iori was kind to a loner. The loner trails a blood tracker into a hotel. The seal breaks on a shield, not on a lecture.",
    "p-ikura",
    "../assets/portraits/iori.webp",
    "A civilian in a tracker’s job. The reason a daughter remembers.",
    [
        ("Role", "Iori’s classmate"),
        ("Trait", "Loner; Iori was kind to him"),
        ("Action", "Trails <a href=\"toto.html\">Toto</a> toward the hotel"),
        ("Consequence", "Iori’s seal breaks when she shields him"),
        ("Arc", '<a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a>'),
    ],
    ["Overview", "The trail", "The shield", "Notes"],
    """
    <h2>Overview</h2>
    <p>Ikura sits next to <a href="iori.html">Iori Samura</a> at school. He is a loner. She was kind to him. That is the entire printed biography until he walks into a Hishaku job. <a href="toto.html">Toto</a> has Samura’s blood from Senkutsuji and a schedule. Ikura trails her. At the Kyoto Bloodshed Hotel, Iori’s memory seal, already fraying because she still loved her father, breaks when she shields him. Memory returns as protection. Not as a lecture from Chihiro, not as a Masumi confession, as a girl covering a classmate.</p>
    <p>He is not a sorcerer. He is not a Masumi. He is not the reason Toto lost the trail. Toto did not lose the trail. The kidnapping fails because Iori chose a person. Ikura is the person. The book’s ethics at the hotel are that sentence. Sengoku dies so Toto can read a head. Ikura lives so Iori can remember a father. One civilian becomes a sample. One civilian becomes a shield.</p>
    <h2>The trail</h2>
    <p>Operation: Easy Does It takes Iori out of school toward Kyoto. Sumi rides a motorcycle. Kuguri gives chase. Toto holds the clock. A classmate who follows a blood tracker into that weather is either foolish or loyal. The pages allow both. Iori’s kindness is the cause. Toto’s visibility is the opportunity. Chihiro is in the building to tell the truth rather than re-seal it. Ikura is in the building because he would not stay at his desk.</p>
    <p>Reigen One-Sword Style, Yojiro Sengoku’s house, is the veil. A school hotel full of swordsmen is a dark until a tracker has already read a sample. Ikura does not know the org chart. He knows a girl who sat next to him and did not treat a loner as furniture. That is enough to walk into Play’s demolition radius.</p>
    <h2>The shield</h2>
    <p>The seal was Itsuo’s mountain logic applied as mercy: erase the father so the daughter can live through a war-crime backlash. It frays because love is not a knot Kasen can file. It breaks because she covers Ikura. Chapter titles around the hotel include “Imitate” and “Iai White Purity Style.” They are Kuguri’s classroom. The seal-break is Iori’s classroom: the style in her body choosing a person over a myth.</p>
    <p>Hiruhiko wrecks the upper floors. Samura arrives. Feathers, banquet, goldfish. Ikura does not get a jacket. He gets the reason Volume 8 can be titled <em>Dawn</em> without being a lie about a demolished hotel. Dawn is a girl who remembers. The classmate is why. See <a href="../world/hotel.html">the hotel</a> and <a href="iori.html">Iori</a>.</p>
    <h2>Notes</h2>
    <p>Ikura (井倉). Classmate. Loner. Shield. For the tracker he trailed, see Toto. For the hotelier who becomes a sample, see Sengoku. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("iori.html", "Iori"), ("toto.html", "Toto"), ("sengoku.html", "Sengoku"), ("../world/hotel.html", "Kyoto hotel"), ("../factions/masumi.html", "Masumi")],
)

char(
    "characters/sengoku.html",
    "Yojiro Sengoku",
    "Kyoto Bloodshed Hotel. Reigen One-Sword Style. Taught the staff. Dies so Toto can read a head.",
    "京都 · Reigen",
    "Yojiro Sengoku",
    "戦国与次郎",
    "He taught a hotel a sword school. The Masumi pick the dark. Toto reads the head. Bloodshed was the house name before it was the week’s weather.",
    "p-sengoku",
    "../assets/portraits/samura.webp",
    "Reigen house. A style becomes a sample.",
    [
        ("House", "Kyoto Bloodshed Hotel"),
        ("Style", "Reigen One-Sword Style"),
        ("Role", "Taught the staff; veil for Operation: Easy Does It"),
        ("Death", "So <a href=\"toto.html\">Toto</a> can read a head"),
        ("Chapters", "67–74; Volume 8, <em>Dawn</em>"),
    ],
    ["Overview", "The school", "The sample", "Notes"],
    """
    <h2>Overview</h2>
    <p>Yojiro Sengoku runs the Kyoto Bloodshed Hotel. Reigen One-Sword Style. He taught the staff. The Masumi pick the building as a veil when Samura’s Owl is up and the Hishaku want <a href="iori.html">Iori</a>. It is not a gag name the translation invented for flavor. Bloodshed is the house’s business and then the week’s weather. Sengoku dies so <a href="toto.html">Toto</a> can read a head. That sentence is the hotel’s ethics in one cut: a swordsman who taught a style becomes a page in a tracker’s book.</p>
    <p>He is not Itsuo Shirakai. Iai White Purity is lids-down speed from a mountain bigot. Reigen is a house style, not an Enchanted Blade school and not Iai. Chihiro copies both in the same corridors: Kuguri’s contempt, the staff’s curriculum, Iori’s body already knowing a different school under a seal. Sengoku is the landlord of that classroom. He does not survive the lesson.</p>
    <h2>The school</h2>
    <p>A hotel that trains its people is a fortress the Masumi can rent as darkness. Easy Does It, the operation name, is the book being funny about a week that includes a beheading. Sumi’s motorcycle is the road in. Sengoku’s Reigen is the building. Chihiro’s decision to tell Iori the truth rather than re-seal it is why the veil is also a confession. Kuguri stays because the fake Iai is not fake enough to ignore. Toto holds the clock. Hiruhiko does not respect objects. Play takes the upper floors apart.</p>
    <p>Volume 8’s jacket is the silhouette under Owl: Chihiro, Iori, Hiruhiko. Sengoku is not on it. The house is. Recaps that mention “the Kyoto hotel” without the man who taught it are doing the graves the same courtesy they do the Steam Squad: a building, no teacher.</p>
    <h2>The sample</h2>
    <p>Toto reads blood. A severed head is a sample with a style still on it. She is there for Iori. Sengoku is inventory. The kidnapping still fails, because Iori shields Ikura and the seal breaks. Toto did not fail the read. The job failed the girl. Samura arrives because two Enchanted Blades in one hotel is a beacon Owl can see. Feathers, banquet, goldfish. The father occupies the same city as the daughter again. The hotelier is already a page.</p>
    <p>Ro of the Masumi later recovers Kumeyuri. Logistics continues. Sengoku does not. See <a href="../world/hotel.html">the hotel page</a>. Official chapters: VIZ / MANGA Plus.</p>
    <h2>Notes</h2>
    <p>Yojiro Sengoku (戦国与次郎). Reigen. Hotel. Sample. For the classmate who lives, see Ikura. For the tracker, see Toto. For Play, see <a href="../analysis/play.html">the objects essay</a>.</p>
    """,
    [("toto.html", "Toto"), ("ikura.html", "Ikura"), ("kuguri.html", "Kuguri"), ("../world/hotel.html", "Kyoto hotel"), ("hiruhiko.html", "Hiruhiko")],
)

char(
    "characters/fushimi.html",
    "Fushimi",
    "Kokugoku Steam Squad. Smoke Axe. Beats Datenseki troops, then dies to Hiruhiko with the rest of the squad.",
    "Kokugoku · Steam Squad",
    "Fushimi",
    "伏見",
    "Smoke between the hands. A named art. A named grave. Chapter 48 titles the squad; Hiruhiko is why the title is also an epitaph.",
    "p-fushimi",
    "../assets/portraits/hiyuki.webp",
    "Sanso guard. Competent. Insufficient. The first book already taught this sentence.",
    [
        ("Affiliation", "Kokugoku Steam Squad; <a href=\"../factions/kamunabi.html\">Kamunabi</a>"),
        ("Art", "Smoke Axe (煙斧)"),
        ("Post", "Guard, Uruha’s Kokugoku Hot Spring Sanso"),
        ("Death", "Hiruhiko, with the rest of the squad"),
        ("Chapter", "48, titled for the squad"),
    ],
    ["Overview", "Smoke Axe", "The week", "Notes"],
    """
    <h2>Overview</h2>
    <p>Fushimi is named among the Kokugoku Steam Squad, the Kamunabi guard on <a href="uruha.html">Uruha</a>’s Sanso. Smoke Axe (煙斧): cuts with smoke between the hands. Hishaku-hired Datenseki troops hit first. The squad beats them. Then <a href="hiruhiko.html">Hiruhiko</a> arrives. Blood Crane, mercenary sorcerers, a train, a kabuki house. The Steam Squad dies. Chapter 48 is titled for the squad. They get a name and a grave in the same week. That is how the bureau spends specialists: named, competent, insufficient.</p>
    <p>He is not Hagiwara. The Anti-Cloud Gouger Special Forces were the same sentence in the first book, four graves and a commander with a cruel title. Fushimi is the second book’s matching piece: a Sanso has a squad, the squad has an art, the art beats hired stone, the art does not beat a Hishaku who came to make a scene. Recaps that say “Hiruhiko attacked a fortress” without Smoke Axe are skipping the people who already won once that week.</p>
    <h2>Smoke Axe</h2>
    <p>Cuts with smoke between the hands. Not an Enchanted Blade. Not Datenseki. A Kamunabi squad technique that can take down hired troops wearing the mineral as a bomb. The win matters. It proves Kokugoku was not theater. Uruha was actually guarded. The Hishaku had to send a member, not only money. Hiruhiko is the member. Play is later, at a hotel. Here the crane is enough, plus the fact that a scene is useful to Yura.</p>
    <p>Chihiro fights Hiruhiko so Hakuri can move Uruha toward Senkutsuji. The Steam Squad’s grave is the reason that extraction is already late. See <a href="../world/sanso.html">Sanso</a>.</p>
    <h2>The week</h2>
    <p>Sword Bearer Assassination starts when a box fails. Kokugoku fails first. Senkutsuji fails as a surgery that looks like a betrayal. Subaru is relocated. Fushimi does not live to see Owl. He lives long enough to beat Datenseki and then meet the ten’s loud younger blade. Volume 6 puts Hiruhiko on a jacket. The squad gets a chapter number. Both are the record.</p>
    <h2>Notes</h2>
    <p>Fushimi (伏見). Smoke Axe (煙斧). Kokugoku Steam Squad. For the fortress, see Sanso. For the attacker, see Hiruhiko. For the other specialist graves, see <a href="../world/acg.html">Anti-Cloud Gouger</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("hiruhiko.html", "Hiruhiko"), ("uruha.html", "Uruha"), ("../world/sanso.html", "Sanso"), ("../world/acg.html", "ACG"), ("../factions/kamunabi.html", "Kamunabi")],
)

char(
    "characters/yoshinojo.html",
    "Yoshinojo Soga",
    "Soga clansman. Older, mustache and beard, unrelenting grin. Killed on Irishima by Ariu Mikaboshi with Hiroto.",
    "Soga · Irishima",
    "Yoshinojo Soga",
    "曽我 義之丞",
    "Older. Mustache and beard. A cocky grin that does not relent. Ariu kills him on the island with the clan head.",
    "p-yoshinojo",
    "../assets/panels/ch113.png",
    "Part 2’s island. The grin is not a survival strategy.",
    [
        ("Clan", '<a href="../factions/soga.html">Soga</a>'),
        ("Look", "Older; mustache and beard; cocky grin"),
        ("Stance", "Unrelenting at the talks"),
        ("Death", "Killed on Irishima by <a href=\"ariu.html\">Ariu Mikaboshi</a>, with Hiroto"),
        ("Tense", "Part 2 past"),
    ],
    ["Overview", "The talks", "The island", "Notes"],
    """
    <h2>Overview</h2>
    <p>Yoshinojo Soga is older, mustache and beard, a cocky grin that does not relent. He sits in Part 2’s Irishima tense with <a href="hiroto.html">Hiroto</a> as clan head, <a href="chiaki.html">Chiaki</a> as princess, <a href="akemura.html">Akemura</a> still a younger brother, <a href="giyu.html">Giyu</a> willing to trade the princess. He is killed on the island by <a href="ariu.html">Ariu Mikaboshi</a>, with Hiroto. The talks themselves (chapters 117–121) still have him breathing. The register is willing to state the later grave. The conference has not reached it yet.</p>
    <p>He is not the head. Hiroto is the stoic who has to sit across from a vein. He is not the ambitious brother. Giyu will accept Mikaboshi demands that include handing Chiaki over. Yoshinojo grins and does not relent. That is a complete printed brief: the Soga still have a man who will not fold a princess into a ceasefire, and the island will kill him anyway.</p>
    <h2>The talks</h2>
    <p>Hasumi’s lab fails. Mashiro does not want stolen ore walked into a shop. Joji is annoyed. Shiba already knows whose eyes to hire. A princess with foresight is a strategic weapon and a hostage tag. Yoshinojo’s unrelenting grin is one of the table’s honest temperatures. The war happens anyway. Kunishige looks anyway. The blades enter at plus one year and five months anyway. Grinning at a risen nation is not a Datenseki policy. It is a clan refusing to become Giyu in the room.</p>
    <h2>The island</h2>
    <p>Ariu’s Sumika: insect constructs, poisoned air, a Datenseki-hardened body. He kills Hiroto and Yoshinojo on Irishima. Mashiro dies later to the same prince. The Soga’s mainland warrant, a woman who can see, does not prevent two graves on a vein. Part 2’s job is to make those graves expensive before the flowers. Yoshinojo’s page exists so the island is not only Hiroto and a princess. See <a href="../world/irishima.html">Irishima</a> and <a href="../analysis/irishima.html">the vein essay</a>.</p>
    <h2>Notes</h2>
    <p>Yoshinojo Soga (曽我 義之丞). Unrelenting. Dead to Ariu, with Hiroto. For the ambitious brother, see Giyu. For the clan, see <a href="../factions/soga.html">Soga</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("hiroto.html", "Hiroto"), ("giyu.html", "Giyu"), ("ariu.html", "Ariu"), ("../world/irishima.html", "Irishima"), ("../factions/soga.html", "Soga")],
)

char(
    "characters/joji.html",
    "Joji",
    "Sorcery Bureau senior. Eyemask, nose ring, ranked above Shiba and Mashiro, annoyed. Alive in the Irishima talks.",
    "Bureau · senior",
    "Joji",
    "丈治",
    "Eyemask. Nose ring. Ranked above the partners. Annoyed. Part 2 needs a senior who is already tired of the ore argument.",
    "p-joji",
    "../assets/portraits/shiba.webp",
    "Above Shiba and Mashiro. The annoyance is the rank.",
    [
        ("Affiliation", "Sorcery Bureau (Part 2 past)"),
        ("Look", "Eyemask; nose ring"),
        ("Rank", "Above <a href=\"shiba.html\">Shiba</a> and <a href=\"mashiro.html\">Mashiro</a>"),
        ("Temper", "Annoyed"),
        ("Tense", "Alive in the Irishima talks"),
    ],
    ["Overview", "The rank", "The talks", "Notes"],
    """
    <h2>Overview</h2>
    <p>Joji wears an eyemask and a nose ring and is ranked above <a href="shiba.html">Togo Shiba</a> and <a href="mashiro.html">Shuji Mashiro</a>. He is annoyed. That is the printed file. Part 2 puts him in the Irishima tense while the bureau has not finished becoming an army and the Enchanted Blades have not been forged. He is not the lab. <a href="hasumi.html">Hasumi</a> runs the tests that fail until a civilian looks. He is not the partner. Mashiro argues about stolen rock and dies later to Ariu. Joji is the senior: already tired, already above the two, already in the room when a princess and a vein are the agenda.</p>
    <p>The archive keeps the page because a past-tense Shiba without a boss is a sitcom. Shiba is loud on purpose. Mashiro has Akuu and a Kunishige sword at eighteen. Someone has to be annoyed at both of them while the island rises. Joji is that someone. Recaps that skip him are skipping the bureau’s middle: not a director, not a partner, a rank.</p>
    <h2>The rank</h2>
    <p>Above the partners means he can tell them to sit down and they have to hear it. It does not mean he can stop Shiba from believing Kunishige’s eyes are the only way to make Datenseki into a blade. It does not mean he can stop Mashiro from opposing the walk into the shop. Rank in this book is often a person who is correct about procedure and late about history. Joji’s annoyance reads as that lateness in a face covering.</p>
    <h2>The talks</h2>
    <p>Chapters 117–121. Hiroto. Yoshinojo. Giyu. Chiaki. Hasumi’s failed lab. Mashiro’s objection. Shiba already sure whose eyes to hire. Joji is annoyed in that weather. The war happens anyway. The rename to Kamunabi happens anyway. In the present tense he is not on the leadership table with Kasen and Ichiki. The past tense still needs him, or the partners float. See <a href="../manga/part-2.html">Part 2</a>.</p>
    <h2>Notes</h2>
    <p>Joji (丈治). Eyemask. Nose ring. Annoyed senior. For the partner who dies later, see Mashiro. For the lab chief who resigns, see Hasumi. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("shiba.html", "Shiba"), ("mashiro.html", "Mashiro"), ("hasumi.html", "Hasumi"), ("../manga/part-2.html", "Part 2"), ("../world/irishima.html", "Irishima")],
)

char(
    "characters/kugara.html",
    "Hajime Kugara",
    "Anti-Cloud Gouger. Iron body, mask, Hagiwara’s childhood friend since age five. Dies. The hallucination’s face.",
    "Anti-Cloud Gouger · iron",
    "Hajime Kugara",
    "具柄 一",
    "Iron body. Mask. Friends with Hagiwara since they were five. Sojo kills him. The commander keeps the face as a wound.",
    "p-kugara",
    "../assets/portraits/hiyuki.webp",
    "ACG. The friend the leftover commander still sees.",
    [
        ("Affiliation", '<a href="../world/acg.html">Anti-Cloud Gouger Special Forces</a>'),
        ("Art", "Iron body"),
        ("Bond", "Childhood friend of <a href=\"hagiwara.html\">Ikuto Hagiwara</a> since age five"),
        ("Death", "Vs. Sojo, at the compound"),
        ("After", "The face Hagiwara hallucinates"),
    ],
    ["Overview", "Iron", "The leftover face", "Notes"],
    """
    <h2>Overview</h2>
    <p>Hajime Kugara is one of the six. Iron body. Mask. Childhood friend of <a href="hagiwara.html">Ikuto Hagiwara</a> since age five. The Anti-Cloud Gouger Special Forces exist because Cloud Gouger in Sojo’s hands was a national problem. Four of the six die at the compound. Kugara is named among the dead. Hagiwara loses both legs and later hallucinates this face. The book will not let the commander keep his legs or his friend. It lets him keep the face as a wound.</p>
    <p>He is not Kazane. The newest member loses an arm before her secret weapon is the scene. He is not Harima, Uzuki, Kasahara, kit in a line. He is the friend inside the unit, which is a different cruelty than “newest” or “commander.” You practiced weather together from childhood. Weather does not care.</p>
    <h2>Iron</h2>
    <p>An iron body is the matching piece a bureau would staff against lightning and rain. Sojo is not weather. Sojo is a fan who spends specialists the way he spends praise for a dead smith. Mei does not check the roster for childhood friends. True Realm arrives in the same fight on Chihiro’s side. Kugara’s iron does not get a brief, meant. It gets a grave. The ACG page is the roster. This page is the friend so the hallucination later has a file, not a caption.</p>
    <h2>The leftover face</h2>
    <p>Chapter 98 is “Ikuto Hagiwara, Worthless Commander.” The leftover still works headquarters when Yukisada holds the barrier. Magnetism is not regeneration. The hallucination is Kugara. Institutions keep their damaged specialists. They also keep the dead in the specialist’s eye. Vs. Sojo taught that a named unit is not a True Realm. The long book teaches that the unit outlives the sword as a wound. See <a href="../world/acg.html">the six</a>.</p>
    <h2>Notes</h2>
    <p>Hajime Kugara (具柄 一). Iron body. Dead. Hallucination’s face. For the commander, see Hagiwara. For the unused weapon, see Kazane. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("hagiwara.html", "Hagiwara"), ("kazane.html", "Kazane"), ("sojo.html", "Sojo"), ("../world/acg.html", "Anti-Cloud Gouger"), ("../arcs/vs-sojo.html", "Vs. Sojo")],
)

char(
    "characters/ro.html",
    "Ro",
    "Masumi leader. Over twenty-three, looks like a child. Sunglasses and candy cigarettes. Recovers Kumeyuri after the hotel.",
    "Masumi · leader",
    "Ro",
    "ロウ",
    "Looks like a child. Is not one. Takes on a Samura persona at the temple, then does inventory on a banquet sword.",
    "p-ro",
    "../assets/portraits/samura.webp",
    "Loyalty with sunglasses. The master had a death wish. The leader still files the steel.",
    [
        ("Clan", '<a href="../factions/masumi.html">Masumi</a>'),
        ("Office", "Leader; over twenty-three"),
        ("Look", "Child-sized; Chihiro and Iori mistake him for a child"),
        ("Temple", "Sunglasses, candy cigarettes, Samura manners"),
        ("Hotel", "Recovers <a href=\"../blades/kumeyuri.html\">Kumeyuri</a> after Samura disarms Hiruhiko"),
    ],
    ["Overview", "The persona", "The inventory", "Notes"],
    """
    <h2>Overview</h2>
    <p>Ro leads the three Masumi who guard <a href="samura.html">Seiichi Samura</a> at Senkutsuji. Over twenty-three. Looks like a child. Chihiro and Iori mistake him for one. He dislikes being treated as a kid and will still use the appearance to skip work. After Kunishige’s death the clan’s job is a blind Buddhist swordsman. After Samura frees them, the job is <a href="iori.html">Iori</a>, the daughter whose memories they themselves erased. Ro is what loyalty looks like when the master has sunglasses and a death wish.</p>
    <p>He is not comic relief. A ninja clan’s leader doing inventory on a banquet sword is this book’s idea of logistics. He recovers <a href="../blades/kumeyuri.html">Kumeyuri</a> after Samura takes it off Hiruhiko at the Kyoto Bloodshed Hotel. Play wrecked the upper floors. Ro still files the steel. The Masumi do not get a volume jacket. They get the girl out of the myth long enough for her to choose a sword.</p>
    <h2>The persona</h2>
    <p>At Senkutsuji he takes on a Samura impression: sunglasses, candy cigarettes, “get fired up,” blunt manners. The Masumi suppress sound and scent so a blind man can fight by hearing. They are prepared to die so he can leave. He refuses the sacrifice, rescues them, and later releases them from service. After the temple falls Ro visits Chihiro in hospital and says the Masumi will look out for him, per Hakuri’s request. The child-face is a tool. The promise is not.</p>
    <h2>The inventory</h2>
    <p>Operation: Easy Does It. Owl up. Hishaku want Iori. Sumi’s motorcycle. Kuguri’s chase. Sengoku’s hotel. Iori’s seal. Play. Samura. Kumeyuri changes hands twice in a night. Ro is the one who ends with the banquet blade in clan custody. After Samura dies, Tobimune is Iori’s. The clan that erased him is still in the courtyard. That is not irony for its own sake. It is the job, finished as protection instead of erasure. Full clan: <a href="../factions/masumi.html">Masumi</a>.</p>
    <h2>Notes</h2>
    <p>Ro. Leader. Child-look. Kumeyuri recovery. For the gravity, see Moku. For the map, see Sumi. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("moku.html", "Moku"), ("sumi.html", "Sumi"), ("samura.html", "Samura"), ("../factions/masumi.html", "Masumi"), ("../blades/kumeyuri.html", "Kumeyuri")],
)

char(
    "characters/moku.html",
    "Moku",
    "Masumi. Tall. Rallies Senkutsuji’s troops. Feeds Chihiro when the boy starts eating himself.",
    "Masumi · gravity",
    "Moku",
    "モク",
    "Tall. The clan’s gravity. Ro is the face. Sumi is the map. Moku is the reason Chihiro eats.",
    "p-moku",
    "../assets/portraits/shiba.webp",
    "Goldfish manners, applied by a ninja.",
    [
        ("Clan", '<a href="../factions/masumi.html">Masumi</a>'),
        ("Look", "Tall"),
        ("Temple", "Meets Hakuri and Uruha at the station; rallies troops"),
        ("Habit", "Food and mission when Chihiro chews himself"),
        ("Job after", "Protect Iori, Operation: Easy Does It"),
    ],
    ["Overview", "The station", "The meal", "Notes"],
    """
    <h2>Overview</h2>
    <p>Moku is tall. He meets <a href="hakuri.html">Hakuri</a> and <a href="uruha.html">Uruha</a> at the train station with Sumi. He rallies Senkutsuji’s troops when the Hishaku hit. He is deeply empathetic in the way this book allows: when <a href="chihiro.html">Chihiro</a> starts doubting or chewing himself, Moku reminds him of the mission or shuts him up with food. The goldfish household’s manners, applied by a ninja. He is the clan’s gravity.</p>
    <p>Ro looks like a child and files swords. Sumi draws doors with a marker. Moku feeds the protagonist. That is not a lesser job. Enten is a retraction forged over a bowl. A ninja who makes the boy eat is keeping the brief in a body that has started to skip meals for guilt. The Masumi served Samura until he freed them. Then they served the daughter. Moku’s service looks like a packed lunch in a war.</p>
    <h2>The station</h2>
    <p>Hakuri is walking a Storehouse toward a temple. Uruha is a false-death waiting to happen. Sumi’s mandala is the road. Moku is the height at the platform: a visible adult in a clan whose leader is mistaken for a child. When the temple is attacked he rallies troops. The Masumi suppress sound and scent for a blind man. Moku is in that weather as gravity, not as a named attack. The clan page holds the sacrifice they offered and Samura refused.</p>
    <h2>The meal</h2>
    <p>Chihiro copies Iai until the copying becomes self-harm by another name. Moku’s answer is food. Cafe Haru Haru is the civilian version of this sentence. Moku is the field version. Hinao keeps a cafe. Moku keeps a boy. After Owl, Easy Does It, the hotel, Samura’s death, Tobimune in Iori’s hands, the tall one is still the reason someone eats. See <a href="../factions/masumi.html">Masumi</a> and <a href="../world/cafe.html">Cafe Haru Haru</a>.</p>
    <h2>Notes</h2>
    <p>Moku. Tall. Food. Gravity. For the leader, see Ro. For the road, see Sumi. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("ro.html", "Ro"), ("sumi.html", "Sumi"), ("chihiro.html", "Chihiro"), ("../factions/masumi.html", "Masumi"), ("../world/cafe.html", "Cafe Haru Haru")],
)

char(
    "characters/sumi.html",
    "Sumi",
    "Masumi kunoichi. Cross-shaped tattoo. Transportation mandalas. Motorcycle away from Kuguri with Iori.",
    "Masumi · map",
    "Sumi",
    "スミ",
    "A marker that draws a door. A motorcycle that is the door at speed. Blood tracking versus ink.",
    "p-sumi",
    "../assets/portraits/iori.webp",
    "The reason the hotel is even a possible veil.",
    [
        ("Clan", '<a href="../factions/masumi.html">Masumi</a>'),
        ("Look", "Kunoichi; cross-shaped tattoo, right side of the face"),
        ("Art", "Transportation mandalas, drawn with a marker"),
        ("Care", "Tends Hakuri so Storehouse can be used without killing him"),
        ("Hotel road", "Motorcycle; Iori; Kuguri in chase"),
    ],
    ["Overview", "The marker", "The motorcycle", "Notes"],
    """
    <h2>Overview</h2>
    <p>Sumi is the Masumi kunoichi with a cross-shaped tattoo on the right side of the face. Transportation mandalas, drawn with a marker: that is how Hakuri and Uruha reach Senkutsuji from the station. She tends Hakuri’s treatment so Storehouse can be used without killing him. In Operation: Easy Does It she takes <a href="iori.html">Iori</a> on a motorcycle while <a href="kuguri.html">Kuguri</a> gives chase. Blood tracking versus a drawn door. She is the reason the Kyoto Bloodshed Hotel is even a possible veil. Sengoku’s Reigen house is the building. Sumi’s marker is the road.</p>
    <p>Toto has Samura’s blood. The dark was never complete. Sumi still has to ride. The clan that erased Iori’s father is the clan putting Iori on a bike. Both jobs are hers in the sense that the map is hers. Ro files steel. Moku files meals. Sumi files distance.</p>
    <h2>The marker</h2>
    <p>A mandala you can draw is logistics the Storehouse would recognize: a room that is not a room until someone spends ink. Hakuri is the walking Kura. Sumi is the paper door. She keeps him alive enough to open it. Without that care the temple never receives Tobimune on time, Samura never clears the grounds, Suzaku never looks like a Hishaku pact. The marker is upstream of the false death. Recaps that start the long book on a train without Sumi are starting after the map.</p>
    <h2>The motorcycle</h2>
    <p>Owl nationwide. Hishaku want a daughter as a lever. Chihiro goes along to tell the truth rather than re-seal it. Kuguri scorns hobby swordsmanship and then falls in love with a fake Iai. Toto holds the clock. Sumi rides. Ikura trails a tracker because a loner was shown kindness. Iori’s seal breaks on a shield. Play takes the upper floors. Sumi’s job in that demolition is still the road: get the girl to a building, then get her through a myth. After Samura dies, Tobimune is Iori’s. The kunoichi who drew the door is still in the courtyard. Clan: <a href="../factions/masumi.html">Masumi</a>. Hotel: <a href="../world/hotel.html">Kyoto</a>.</p>
    <h2>Notes</h2>
    <p>Sumi. Marker. Motorcycle. Tattoo. For the leader, see Ro. For gravity, see Moku. For the chase, see Kuguri. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [("ro.html", "Ro"), ("moku.html", "Moku"), ("iori.html", "Iori"), ("kuguri.html", "Kuguri"), ("../factions/masumi.html", "Masumi")],
)

# --- World rooms ---

page(
    "world/cafe.html",
    "Cafe Haru Haru",
    "Hinao’s cafe: the sit-down between jobs, Chihiro at the counter, Shiba in the booths, the civilian door on the first map.",
    crumb(("World", "index.html"), "Cafe Haru Haru")
    + hero("Tokyo underworld", "Cafe Haru Haru", "カフェ ハルハル", "The closest thing the first chapters have to a home. A cup, a counter, a boy with a sword, an uncle who teleports into the booth.")
    + """
<article class="article">
  <p>Cafe Haru Haru is <a href="../characters/hinao.html">Hinao</a>’s room. <a href="../characters/chihiro.html">Chihiro</a> works the counter between raids. <a href="../characters/shiba.html">Shiba</a> uses the booths. <a href="../characters/azami.html">Azami</a> knows the address. After the Rokuhira workshop burns and the cellar is empty of six swords, this is where the present tense sits down. Char’s sighting, Madoka’s confirmation, Sojo’s first shadow: the city is the first map, and the cafe is the pin. A modern Japan that had to admit sorcery in public still has coffee. The joke is only funny until an Enchanted Blade user walks in and orders like a person.</p>
  <p>Hinao also connects sorcerers to yakuza and corporations who need them. The civilian door is a job, not a personality type. Chihiro and Shiba’s three-year commute is not a montage of random thugs. It is a labor market. Azami wants Chihiro out of the underworld. Hinao is how the underworld had a front door that looked like a cafe. Akari Tadano voices her in the voiced comic. The 2027 Cypic series has not announced the cafe’s cast. A studio will still have to light a warm interior in a book about stolen steel.</p>
  <h2>What the room holds</h2>
  <p>Chapter 1 already needs a place that is not the ruined workshop. Mission, heaps, witness: the early titles are objects and meals. Hinao is the meal’s landlord. Enten leans. Goldfish ethics leak into the cups because Chihiro works there, not because the espresso machine is a Masumi. When Toto can find Chihiro after a death, the cafe stops being safe. Hinao is still behind the counter. Most of the cast can leave a building. The proprietor is the building’s habit.</p>
  <p>Vs. Sojo takes the story to a hospital and a compound. The Rakuzaichi takes it to an auction. The long book takes it to a hotel and a headquarters. The cafe remains the civilian measure. If the war cannot be sat down next to a cup, the war has already eaten the premise. <a href="../characters/moku.html">Moku</a> later feeds Chihiro in the field. That is this room’s manners, packed for travel.</p>
  <h2>Part 2’s absence</h2>
  <p>Part 2 is twenty-two years earlier. Chihiro has not been born. The talks have a conference table and a kiln. No Haru Haru. The absence is useful. The cafe is what the present tense built afterward: a room where a smith’s son can be a waiter instead of only a revenge. Shiba will remember a partner, a senior, a lab. He will also, later, pick a booth. Locations: <a href="locations.html">the map</a>. Hinao’s file: <a href="../characters/hinao.html">Hinao</a>. Official chapters: VIZ / MANGA Plus.</p>
  """
    + related(("../characters/hinao.html", "Hinao"), ("../characters/chihiro.html", "Chihiro"), ("../characters/shiba.html", "Shiba"), ("locations.html", "Locations"), ("../fun/first-read.html", "First-read notes"))
    + "</article>",
)

page(
    "world/irishima.html",
    "Irishima",
    "The island and the vein: Shokoku’s rise, the Irishima talks, Datenseki, and Part 2’s opening property. Separate from the vein essay.",
    crumb(("World", "index.html"), "Irishima")
    + hero("Shokoku · the vein", "Irishima", "煎島", "An island that should have stayed under the sea. A quarter-ton of rock. Talks that were already a battlefield.")
    + """
<figure class="shot">
  <img src="../assets/panels/ch113.png" alt="Chapter 113: Irishima / Shokoku">
  <figcaption>Chapter 113 splash. English Twitter called it Japan’s Atlantis. Full chapter: VIZ / MANGA Plus.</figcaption>
</figure>
<article class="article">
  <p>Shokoku rose from the sea about twenty-two years before the main story. Irishima’s earthquake had already shown a Datenseki vein. Japan harvested it. About 250 kilograms known, one pair of eyes ever made it safe. The war is, at the mineral level, a fight over a vein on an island. Everything else, clans, contracts, flowers, is what people did with a quarter-ton of rock. This page is the place. The argument about what the rock means lives on <a href="../analysis/irishima.html">Irishima’s vein</a>. The uncollected chapters live on <a href="../manga/part-2.html">Part 2</a>.</p>
  <p>The Mikaboshi were old sorcerer kings the Soga once drove off the mainland. They survived under the sea with Datenseki-adapted bodies and came back for Irishima’s stone. <a href="../characters/ariu.html">Ariu Mikaboshi</a> kills <a href="../characters/hiroto.html">Hiroto</a> and <a href="../characters/yoshinojo.html">Yoshinojo</a> on the island. Mashiro dies later to the same prince. The Sorcery Bureau becomes an army, then the Kamunabi. A year and five months in, Kunishige’s blades reverse the front. Once Magatsumi enters the field, Japan can walk onto the island. That is the official sentence.</p>
  <h2>The talks</h2>
  <p>Part 1 ends on “Swordsmith.” Part 2 opens on “Princess.” Chapters 117 through 121 are the talks in five pieces, ending on “The Irishima Talks, END.” Chiaki Soga, foresight as inherited proof of Izanami. Shiba as Soga guardian. Kunishige still a picky dealer who has not looked at the ore. Hasumi’s lab fails. Mashiro opposes walking stolen rock into a shop. Joji is annoyed. Giyu will trade a princess. Yoshinojo will not relent. Hiroto is the strongest sentence at the table and still loses the room to a ceasefire he has not signed yet.</p>
  <p>English videos argue paternity rumors after chapter 118 and 122. Face, eye, and the absence of insect sorcery still point at the smith. The rumor is not treated as fact here. Chapter 123 is “Chiaki.” 124 “Powerless.” 125 “Smelting.” 126 “Fire.” After a month off, 127 and 128 continue the heat; 129, “Ironworks” (23 August 2026), puts Kunishige inside the fire with Chiaki as the reason he keeps his eyes open. Hokazono talked to a real swordsmith so the workshop pages would not be cosplay.</p>
  <h2>What the place is not</h2>
  <p>It is not Cafe Haru Haru. It is not a Sanso. It is not the Rakuzaichi Storehouse. It is the water the present-day plot has been swimming in since page one, finally printed as ground. Magatsumi-as-Ariu-copy is a reader comparison some people make about insects and flowers. It is not a caption on this page. The island is a vein, a conference, a kiln, and two Soga graves. Timeline: <a href="index.html">world</a>. Clan: <a href="../factions/soga.html">Soga and Mikaboshi</a>. Official chapters: VIZ / MANGA Plus.</p>
  """
    + related(("../analysis/irishima.html", "Vein essay"), ("../manga/part-2.html", "Part 2"), ("../characters/chiaki.html", "Chiaki"), ("../characters/yoshinojo.html", "Yoshinojo"), ("../arcs/seitei-war.html", "Seitei War"))
    + "</article>",
)

# --- Essays ---

page(
    "analysis/play.html",
    "Play, objects, Banquet",
    "Kumeyuri’s two briefs: Banquet takes the senses, Play takes the set. Respect makes telekinesis smoother. Hiruhiko’s contempt drops a hotel.",
    crumb(("Essays", "index.html"), "Play, objects, Banquet")
    + hero("Essay · Kumeyuri", "Play, objects, Banquet", "遊と宴", "A theater sword. Fluency scales with respect. The hotel falls because the later wielder does not love furniture.")
    + """
<article class="article">
  <p><a href="../blades/kumeyuri.html">Kumeyuri</a> is theater. <strong>Banquet</strong> takes the senses, a hallucination that kills hearing and sight unless the ears are reinforced, snapped by a fatal wound. <strong>Play</strong> takes the set: move nearby objects; respect makes the telekinesis smoother. Spirit energy leaves as faceless oiran. Fifth of the wartime six. <a href="../characters/uruha.html">Yoji Uruha</a> was the war bearer, loyal to the Rokuhira name, a prodigy’s vocation. After Samura’s Suzaku “kills” the contract, <a href="../characters/hiruhiko.html">Hiruhiko</a> inherits the blade and discovers the extension: if Play is respect, contempt is a wrecking ball. Destructive Play is that reading, not a new named art. The Kyoto Bloodshed Hotel loses its upper floors to it.</p>
  <p>This essay is for the object, not the org chart. Yura assigns a scene. Kuguri falls in love with a fake Iai. Toto holds the clock. Those are people. Play is a brief about furniture. Hokazono’s whole book has been about whether you love the thing in your hand. Enten is a household. Magatsumi is a field. Cloud Gouger is weather a fan will spend. Kumeyuri asks a smaller, crueler question: do you respect the chair?</p>
  <h2>Uruha’s room</h2>
  <p>Uruha’s oiran are a war prodigy’s vocation. Banquet is not a party. It is a sense-killing stage cue. Natsuki wanted this sword and did not get it; the resentment is printed. Loyalty to the Rokuhira name is why Uruha can carry theater without turning it into a tantrum. When Samura cuts him down, Suzaku: kill the contract, keep the man. The blade can be pulled off the board. Hiruhiko is the later signature. The mismatch is the demolition. Ro of the Masumi recovers the steel after Samura takes it off the Hishaku. A ninja doing inventory on a banquet sword is logistics. It is also the book putting Play back in a hand that might respect objects again.</p>
  <h2>Hiruhiko’s room</h2>
  <p>Hiruhiko does not love objects. Blood Crane on the train, a kabuki house, then Play at the hotel: every fight is a performance he wants someone to stay for. Chihiro will not stay. Eighteen, killed at three, treats Chihiro as a peer-shaped friend. Friendship is a stage. Furniture is not a friend. Destructive Play drops the upper floors because contempt is fluent too. Suzaku later heals a building he had already started to unmake. Volume 8, <em>Dawn</em>, is dust and a silhouette under Owl. Dawn after a night battle is not a repaired hotel. It is a daughter who remembers, and a wreck.</p>
  <p>Sojo loved Kunishige’s work and never met the man. Hiruhiko does not even love the set. That is the whole difference between the first book’s worst fan and the long book’s loud younger blade. See <a href="sojo-fan.html">Sojo, worst fan</a>, <a href="../world/hotel.html">the hotel</a>, <a href="../characters/hiruhiko.html">Hiruhiko</a>. Official chapters: VIZ / MANGA Plus.</p>
  """
    + related(("../blades/kumeyuri.html", "Kumeyuri"), ("../characters/hiruhiko.html", "Hiruhiko"), ("../characters/uruha.html", "Uruha"), ("../world/hotel.html", "Hotel"), ("copy.html", "Copy by sight"))
    + "</article>",
)

page(
    "analysis/copy.html",
    "Chihiro copies by sight",
    "Chapter 65 is Imitate. Iai White Purity requires the lids down. Chihiro learns a mountain school in a hotel corridor off Kuguri’s contempt.",
    crumb(("Essays", "index.html"), "Chihiro copies by sight")
    + hero("Essay · Imitate", "Chihiro copies by sight", "模倣", "A smith’s son shutting his eyes in a hallway. The fake becomes a school. Kuguri drops the errand.")
    + """
<article class="article">
  <p>Chihiro copies by sight. That is the printed method before anyone says True Realm. He watches a cut and spends it. <a href="../world/iai.html">Iai White Purity</a> requires the lids down. The Kyoto Bloodshed Hotel is where those two facts meet a live instructor who did not volunteer. <a href="../characters/kuguri.html">Kuguri</a> scorns hobby swordsmanship. A boy shutting his eyes in a corridor is the opposite of a hobby once the cuts start landing. Chapter 65 is “Imitate.” Chapter 70 is “Iai White Purity Style.” Those titles are this argument even when the table of contents does not print Chihiro’s name on them.</p>
  <p>He is not Itsuo’s student. <a href="../characters/itsuo.html">Itsuo Shirakai</a> founded the school in the mountains and did not want women in it. <a href="../characters/iori.html">Iori</a>’s body already knows the curriculum under a seal. <a href="../characters/kiri.html">Kiri</a> brought a two-meter odachi to a school that told her not to. Chihiro learns Iai in public, off a Hishaku who came to kidnap a daughter. The Lifelong Contract darkens his innate sorcery. Copying is what is left: eyes, then no eyes, then a mountain style in a smith’s wrist. Enten is still the household. The hallway is extra curriculum the seventh blade did not ask for.</p>
  <h2>The unwilling adjunct</h2>
  <p>Kuguri is sent to close. Toto is sent to keep the close from becoming a funeral for the wrong Hishaku. Kuguri drops the schedule when the fake Iai gets serious. Battle frenzy is the text’s word. Unrequited blade: he wanted Enchanted steel and got Twilight Wave and a corridor. Chihiro is a dummy who starts landing. That is not friendship. Hiruhiko wants friendship as a stage. Kuguri wants a fight that deserves his school-hatred. The copy is an insult that becomes a lesson. Toto still holds the clock. The kidnapping still fails, because Iori shields Ikura. Chihiro’s imitation did not save the girl. It kept Kuguri in the building long enough for Samura to see two Enchanted Blades ping Owl.</p>
  <h2>What copying is not</h2>
  <p>It is not Magatsumi. The Sword Master’s kit is not a sight-gag for a hotel. It is not Play. Objects move when Hiruhiko hates them; Chihiro is moving his own arms. It is not True Realm, which is the brief meant, Cloud Gouger’s storm spent as a life. Copying is the first-book habit, named in the long book, aimed at a school that requires you to stop looking. A goldfish household taught him not to spend innocents. A Hishaku swordsman taught him to shut his eyes. Both lessons are in Volume 8’s dust. See <a href="../world/hotel.html">the hotel</a>, <a href="../characters/kuguri.html">Kuguri</a>, <a href="play.html">Play</a>. Official chapters: VIZ / MANGA Plus.</p>
  """
    + related(("../characters/chihiro.html", "Chihiro"), ("../characters/kuguri.html", "Kuguri"), ("../world/iai.html", "Iai"), ("play.html", "Play"), ("../world/hotel.html", "Hotel"))
    + "</article>",
)

# --- Watch + shop ---

page(
    "guide/watch.html",
    "How to watch the anime",
    "Kagurabachi anime, April 2027: Cypic, Crunchyroll, official hub, countdown. Legal doors only.",
    crumb(("Guide", "index.html"), "How to watch")
    + hero("April 2027", "How to watch", "視聴案内", "Cypic. Takeuchi. Crunchyroll outside Japan, with the listed exceptions. A first-episode date lands when they print one.")
    + clock()
    + """
<article class="article">
  <p>The <em>Kagurabachi</em> television series is from Cypic, directed by Tetsuya Takeuchi, character designs by Keigo Sasaki. Broadcast is listed for April 2027. This page counts to 1 April 2027, 00:00 Japan time, until an episode-one clock exists. Official hub: <a href="https://anime.kagurabachi.jp/">anime.kagurabachi.jp</a>. Accounts: <a href="https://x.com/kb_anime_jp">@kb_anime_jp</a>, <a href="https://x.com/kb_anime_en">@kb_anime_en</a>. The tag is <a href="https://x.com/hashtag/BachiAnime">#BachiAnime</a>. Full file: <a href="../media/anime.html">the anime page</a>.</p>
  <h2>Legal doors</h2>
  <ul>
    <li><strong>Japan.</strong> A television slot will be named when it is named. Until then the official site is the door, not a random stream.</li>
    <li><strong>Outside Japan.</strong> Crunchyroll, with the usual listed exceptions from the license announcement. Wait for the title page to go live on the service. Do not use scrape sites. The book already taught the difference between a trophy and a household; stolen video is the trophy version of watching.</li>
    <li><strong>The first twenty minutes.</strong> Toured from July 2026: Anime Expo, Japan Expo, AnimagiC, Anime NYC. A ticket and a memory unless a booklet SKU appears. The <a href="../collectibles/index.html">collectibles</a> page will log one if it exists.</li>
  </ul>
  <h2>Voices so far</h2>
  <p>Taihi Kimura (Chihiro), Tomokazu Seki (Kunishige), Katsuyuki Konishi (Shiba). Voiced comic: Shoya Ishige, Kenta Fujimaki, Jun Fukushima, Akari Tadano (Hinao). More cast will land closer to 2027. Cour length and adaptation stopping point are not confirmed. The YouTube camp that ends season 1 on chapter 60’s elevator is a camp. Read the book legally while you wait: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. Buy the spines on the <a href="../collectibles/shop.html">shop</a> page.</p>
  <p>If you are sending the show to someone who only knows the 2023 meme, send this countdown and chapter 1, not a “generational” compilation. Sunday still lives under one tag. The legal way to be there is shorter than the leak way.</p>
  """
    + related(("../media/anime.html", "Anime"), ("../fun/voices.html", "Voices"), ("../collectibles/shop.html", "Shop"), ("../fun/first-read.html", "First-read"), ("index.html", "Guide"))
    + "</article>",
)

VIZ = [
    ("01", "Mission", "978-1-9747-4724-5", "5 Nov 2024"),
    ("02", "Enten vs. Cloud Gouger", "978-1-9747-5271-3", "4 Feb 2025"),
    ("03", "Knight of Darkness", "978-1-9747-5478-6", "6 May 2025"),
    ("04", "Equal", "978-1-9747-5607-0", "5 Aug 2025"),
    ("05", "Fervent", "978-1-9747-5891-3", "4 Nov 2025"),
    ("06", "Daybreak", "978-1-9747-6287-3", "3 Feb 2026"),
    ("07", "Night Battle", "978-1-9747-6574-4", "5 May 2026"),
    ("08", "Dawn", "978-1-9747-1650-0", "4 Aug 2026"),
    ("09", "Enten", "978-1-9747-6845-5", "3 Nov 2026"),
]
vol_cards = "\n".join(
    f'<a class="shop-card" data-amazon="{isbn}" href="https://www.amazon.com/s?k={isbn}"><span class="shop-tag">VIZ · Vol. {num}</span><strong>{title}</strong><span>ISBN {isbn}. English date {date}. Opens Amazon search. Commission only if an Associates tag is pasted in js/site.js.</span></a>'
    for num, title, isbn, date in VIZ
)

page(
    "collectibles/shop.html",
    "Shop",
    "Where to buy Kagurabachi volumes and official merch, plus how this site can earn Amazon Associates commission without a fake tag.",
    crumb(("Collectibles", "index.html"), "Shop")
    + hero("Official goods", "Shop", "購買", "Buy the book. Buy licensed merch. This page will not list bootlegs, scans, or replica Enchanted Blades from a marketplace without a license line.")
    + f"""
<article class="article">
  <p>The object to buy is the tankōbon. English volumes are VIZ. Japanese volumes are Jump Comics. Licensed hoodies, clocks, and keycaps live on official Jump storefronts. There is no public affiliate program for those Jump shops, so this site cannot take a cut of a Chihiro jacket. Amazon Associates is the honest US path for the VIZ spines. Crunchyroll Store’s old affiliate program ended 31 May 2026; those links are catalog only.</p>
  <div class="note"><strong>Commission, plainly.</strong> Amazon search links on this page pick up a tag if the site owner pastes an Associates ID into <code>js/site.js</code> as <code>KAGURA.amazonTag</code> (example shape: <code>kagurabachi-20</code>). Until that string is filled, the same buttons still open Amazon; nobody earns. Bookshop.org works the same way with <code>KAGURA.bookshopId</code>. Privacy already discloses the Amazon Associates line. This page will not invent a tag to look live.</div>

  <h2>VIZ volumes (Amazon search)</h2>
  <p>ISBNs match the <a href="../manga/volumes.html">volume guide</a>. English Volumes 10 and 11 are still TBD. No live prices; Associates policy and common sense. Click through, confirm the edition, buy if you want the object.</p>
  <div class="shop-grid">
    {vol_cards}
    <a class="shop-card" data-amazon="Kagurabachi VIZ Media" href="https://www.amazon.com/s?k=Kagurabachi+VIZ"><span class="shop-tag">VIZ · search</span><strong>All English volumes</strong><span>Catch-all Amazon search if you want the set or later ISBNs not yet on this table.</span></a>
    <a class="shop-card" data-bookshop="Kagurabachi" href="https://bookshop.org/search?keywords=Kagurabachi"><span class="shop-tag">Bookshop.org</span><strong>Independent bookstores</strong><span>Search Bookshop. If a Bookshop affiliate ID is pasted beside the Amazon tag, this link starts to pay the site. Empty ID still opens the catalog.</span></a>
  </div>

  <h2>Official merch (no affiliate cut)</h2>
  <p>Shueisha and Jump’s stores do not publish a general US affiliate program for this title. Link them because they are the licensed door, not because this archive earns. If that changes, the note above will change.</p>
  <div class="shop-grid">
    <a class="shop-card" href="https://shonenjumpstore.com/collections/kagurabachi" rel="noopener noreferrer" target="_blank"><span class="shop-tag">US · Jump Store</span><strong>Shonen Jump Store</strong><span>Official English-store collection: hoodie, fish-bowl clock, keycaps, Chihiro jacket when in stock. No commission.</span></a>
    <a class="shop-card" href="https://benelic.com/jumpshop/cat_ka/kagurabachi/" rel="noopener noreferrer" target="_blank"><span class="shop-tag">JP · Jump Shop</span><strong>Jump Shop (Benelic)</strong><span>Japanese Jump Shop catalog for カグラバチ. Regional shipping and store rules apply. No commission.</span></a>
    <a class="shop-card" href="https://jumpcs.shueisha.co.jp/" rel="noopener noreferrer" target="_blank"><span class="shop-tag">JP · Characters Store</span><strong>Jump Characters Store</strong><span>Shueisha’s character goods hub. Search Kagurabachi on their shelf. No commission.</span></a>
    <a class="shop-card" href="https://store.crunchyroll.com/search?q=kagurabachi" rel="noopener noreferrer" target="_blank"><span class="shop-tag">Catalog only</span><strong>Crunchyroll Store</strong><span>Search the store. Their affiliate program ended 31 May 2026. This link does not pay the site.</span></a>
    <a class="shop-card" href="https://www.viz.com/kagurabachi" rel="noopener noreferrer" target="_blank"><span class="shop-tag">Publisher</span><strong>VIZ title page</strong><span>Publisher door for English editions. Buy wherever you already buy books if you prefer not to use Amazon.</span></a>
    <a class="shop-card" href="https://www.amazon.co.jp/s?k=%E3%82%AB%E3%82%B0%E3%83%A9%E3%83%90%E3%83%81" rel="noopener noreferrer" target="_blank"><span class="shop-tag">JP Amazon</span><strong>Japanese tankōbon</strong><span>Jump Comics search on Amazon.co.jp. US Associates tags do not apply here. Eleven volumes out; 12 solicited 4 Sep 2026.</span></a>
  </div>

  <h2>What this site will not sell you</h2>
  <p>Unlicensed statues. Bootleg keychains. Scan listings. “Replica Enchanted Blades” from a marketplace that does not have a license line. World-tour tickets for the first twenty minutes are a memory unless a booklet SKU appears. Figures and maker announcements get logged on <a href="index.html">collectibles</a> with a date when they exist.</p>
  <p>Read the serial free and legally while you wait for April 2027: <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ / Shonen Jump</a> and <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. Countdown: <a href="../media/anime.html">anime</a> and <a href="../guide/watch.html">how to watch</a>. Privacy: <a href="../privacy.html">affiliate disclosure</a>.</p>
  """
    + related(("index.html", "Collectibles"), ("../manga/volumes.html", "ISBNs"), ("../guide/watch.html", "How to watch"), ("../privacy.html", "Privacy"), ("../media/anime.html", "Anime"))
    + "</article>",
)

print("wave complete")
