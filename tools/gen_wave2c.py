#!/usr/bin/env python3
"""Remaining second-wave character files. No em-dashes."""
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
    "tamaki",
    "Tamaki Sazanami",
    "漣 珠紀",
    "Sazanami · the Tou",
    "Older sister. One of the three who meet Chihiro and Shiba at the estate. She lies to Kyora about Soya. Tenri tells the truth.",
    "p-tamaki",
    "../assets/portraits/kyora.webp",
    "Tou. The sister who tried to edit a brother’s condition for the father.",
    [
        ("Clan", '<a href="../factions/sazanami.html">Sazanami</a> · Tou'),
        ("Father", '<a href="kyora.html">Kyora Sazanami</a>'),
        ("Siblings", "Soya, Tenri, Enji, Hakuri"),
        ("Printed move", "Lies to Kyora that Soya is unwell; Tenri corrects her"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Tamaki Sazanami is the older sister among the Tou, the household military that protects the Rakuzaichi. She is one of the three who confront <a href="chihiro.html">Chihiro</a> and <a href="shiba.html">Shiba</a> at the estate. She lies to <a href="kyora.html">Kyora</a> that <a href="soya.html">Soya</a> is unwell. <a href="tenri.html">Tenri</a> corrects her. That pair of sentences is most of her printed interiority, and it is already a file. A clan that treats children as stock still has a daughter who will edit a brother’s condition before the father hears it. The edit fails. The father is the calendar. The truth is a younger brother’s loyalty test.</p>
    <p>She is not Hakuri. She is not the heir. She is not the boy who ate the stone. She is Tou: good enough to be one of the four, not rare enough to hold Storehouse. After the 208th the clan goes into hiding. This page will not invent her postwar job. It will keep the lie, the correction, and the estate fight on the record.</p>
    <h2>Personality</h2>
    <p>The lie is the character. Whether it is mercy for Soya or management of Kyora, the magazine has not given a speech. What can be said: she is willing to put a sentence between the eleventh head and a son. In a house that sacrifices children to keep an auction on the calendar, a lie about wellness is a small heresy. Tenri’s correction is the orthodox move. Tamaki is the heresy that did not take.</p>
    <p>Readers who want a secret ally in the Tou will have to wait for a chapter that prints one. Confronting Chihiro and Shiba at the estate is not alliance. It is the firm defending the address. The archive will not recast a door guard as a mole because she once lied about a brother.</p>
    <h2>Story role</h2>
    <p>The Rakuzaichi arc needs a household, not only a father and a discarded son. Tamaki is part of how the estate feels like a family military instead of a boss and minions. Volume 3 puts Kyora on a jacket with Chihiro and Hiyuki. The children are the green-black interior. When Hakuri awakens and the Storehouse becomes a war, the Tou are the people who still think the building is theirs. Tamaki is one of those people.</p>
    <p>Enji begs Shiba for death after Tenri and is told to live and raise what is left so another child does not eat a stone. Tamaki is part of what is left. Soya crawls out with amnesia. Hakuri walks. The sister who lied is still a Sazanami in the ways that matter to victims: she knows the name, the art, the calendar. If she walks into a later chapter, this file will add the walk.</p>
    <h2>Notes</h2>
    <p>Tamaki (漣 珠紀). Tou. The lie. For the firm, see <a href="../factions/sazanami.html">Sazanami</a>. For the brother who corrected her, see <a href="tenri.html">Tenri</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Sazanami", "../factions/sazanami.html"),
        ("Soya", "soya.html"),
        ("Tenri", "tenri.html"),
        ("Hakuri", "hakuri.html"),
        ("Kyora", "kyora.html"),
    ],
)

character(
    "enji",
    "Enji Sazanami",
    "漣 円慈",
    "Sazanami · the Tou",
    "Older brother. After Tenri pops, he begs Shiba for death. Shiba tells him to live and raise what is left of the clan.",
    "p-enji",
    "../assets/portraits/shiba.webp",
    "Tou. The refusal is Shiba’s ethics in one sentence.",
    [
        ("Clan", '<a href="../factions/sazanami.html">Sazanami</a> · Tou'),
        ("Father", '<a href="kyora.html">Kyora Sazanami</a>'),
        ("Siblings", "Soya, Tamaki, Tenri, Hakuri"),
        ("Printed turn", "Begs Shiba for death; is told to live"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The refusal</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Enji Sazanami is an older brother among the Tou. His printed turn comes after <a href="tenri.html">Tenri</a> dies on a half-stable Datenseki stone. Enji begs <a href="shiba.html">Togo Shiba</a> for death. Shiba tells him to live and raise what is left of the clan so another child does not eat a stone. That is Shiba’s ethics in one refusal. The goldfish household’s manners, applied to an auction son who just watched the mineral do what the mineral does.</p>
    <p>He is not the heir and not the discarded warehouse. He is the Tou who asked to be taken off the calendar and was put back on a different one: raise, do not pop. This page exists so that refusal has a door. Recaps that skip from Kyora’s death to Hakuri’s deal miss the brother who wanted to follow Tenri into the crater.</p>
    <h2>The refusal</h2>
    <p>Shiba left the Kamunabi when the smith hid. He extracts. He teleports. He jokes. He also says no to a suicide that would look like responsibility. Enji’s request is the firm’s logic completed: if the auction is civilization and the civilization just ate a child, the remaining soldier should be deleted. Shiba’s no is the workshop’s logic: a household raises what is left. Another Datenseki snack is not honor.</p>
    <p>Part 2 will later spend chapters on smelting so the reader understands the pop in industrial time. Enji’s chapter is the pop in domestic time. The same mineral. A smaller room. A teleporting uncle who will not be a weapon for a boy’s guilt.</p>
    <h2>Story role</h2>
    <p>The 208th ends the firm. Soya crawls out with amnesia. Tamaki has already lied. Hakuri is the building that walks. Enji is told to be a person who raises people. Whether he does is a later sentence. The printed one is the order. Chihiro’s circle keeps collecting people the institutions wanted to spend. Enji is the rare collection who was on the enemy roster five minutes earlier.</p>
    <p>This archive will not invent a redemption montage. It will keep Shiba’s sentence on the page. For the father who built the calendar, see Kyora. For the son who became the warehouse, see Hakuri. For the mineral, see <a href="../world/datenseki.html">Datenseki</a>.</p>
    <h2>Notes</h2>
    <p>Enji (漣 円慈). Tou. The beg. The refusal. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Shiba", "shiba.html"),
        ("Tenri", "tenri.html"),
        ("Sazanami", "../factions/sazanami.html"),
        ("Datenseki", "../world/datenseki.html"),
        ("Hakuri", "hakuri.html"),
    ],
)

character(
    "madoka",
    "Norisaku Madoka",
    "円 法炸",
    "Sojo’s employee · Daruma",
    "Chapter 8 is his name and a promise. He decides to go straight. Sojo kills him for talking.",
    "p-madoka",
    "../assets/portraits/sojo.webp",
    "The customer’s staff. A Daruma, a confession, a grave.",
    [
        ("Affiliation", "Employee of <a href='sojo.html'>Genichi Sojo</a>"),
        ("Sorcery", "Exploding Daruma"),
        ("Chapter", "8, “Norisaku Madoka: I Will Change”"),
        ("Status", "Killed by Sojo for talking"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The promise</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Norisaku Madoka is a Daruma sorcerer on <a href="sojo.html">Sojo</a>’s payroll. Exploding Daruma. He decides to go straight. Sojo kills him for talking. Chapter 8 is titled with his name and a promise: “Norisaku Madoka: I Will Change.” The archive keeps a page because the first book’s ethics lesson is not only Cloud Gouger versus Enten. It is also what a customer does with staff who grow a conscience.</p>
    <p>He is not Hishaku. Recaps that blur Sojo’s gang with Yura’s ten cannot explain a sale. Madoka worked for the buyer. The Daruma are the buyer’s furniture. Chihiro and Shiba’s underworld commute runs through people like him: hirelings who can still choose a different sentence and then die of the choice.</p>
    <h2>The promise</h2>
    <p>I will change. The title is sincere enough that the book spends a chapter on it. Madoka is not a fake-out gag. He is a man who looks at the work (Enchanted Blade trafficking, a hunted girl, a boss who loves a dead smith’s steel and will spend civilians for it) and tries to step off. Talking is the step. Sojo treats talking as a leak. The kill is the customer’s quality control.</p>
    <p>Char is the last Kyonagi. Sojo wants a stabilizer for Datenseki because he cannot borrow Kunishige’s eyes. Madoka’s change happens in that weather. A hireling deciding to be a person is not smaller than a True Realm. It is the civilian version. Hinao’s cafe is the other civilian version: remain, broker, do not explode. Madoka explodes because that is his art and then because that is his boss.</p>
    <h2>Story role</h2>
    <p>Early chapters need confirmation that an Enchanted Blade is in the city. Madoka is part of that confirmation, then part of the body count that teaches Chihiro what Sojo’s love of the work actually spends. Azami wants the boy out of the underworld. Chapter 8 is why. The underworld kills the people who try to leave it with information still in their mouths.</p>
    <p>He is a door into Sojo’s file, not a rival. The bathhouse extra will later let the worst fan rate tubs. Madoka does not get an extra. He gets a title that is also an epitaph. Read him next to <a href="../analysis/sojo-fan.html">Sojo, worst fan</a>. The fan loved the steel. The staff died of a sentence.</p>
    <h2>Notes</h2>
    <p>Norisaku Madoka (円 法炸). Daruma. Chapter 8. For the customer, see <a href="sojo.html">Sojo</a>. For the girl he failed to keep safe by talking, see <a href="char.html">Char</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Sojo", "sojo.html"),
        ("Char", "char.html"),
        ("Sojo, worst fan", "../analysis/sojo-fan.html"),
        ("Chihiro", "chihiro.html"),
        ("Chapter index", "../manga/chapters.html"),
    ],
)

character(
    "kazane",
    "Kazane Machi",
    "真智 カザネ",
    "Anti-Cloud Gouger · Kaichi",
    "The newest of the six. Demon Monster, the unused secret weapon. Sojo takes the right arm first.",
    "p-kazane",
    "../assets/portraits/sojo.webp",
    "ACG. The secret weapon that did not get to be a weapon.",
    [
        ("Affiliation", '<a href="../world/acg.html">Anti-Cloud Gouger Special Forces</a>'),
        ("Sorcery", "Demon Monster (怪魑, Kaichi)"),
        ("Role", "Newest member; unused secret weapon against Cloud Gouger"),
        ("Injury", "Sojo takes the right arm first"),
        ("Commander", '<a href="hagiwara.html">Ikuto Hagiwara</a>'),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Kaichi</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Kazane Machi is the newest member of the <a href="../world/acg.html">Anti-Cloud Gouger Special Forces</a>. Six people. One stolen sword. Her sorcery is <strong>Demon Monster</strong> (怪魑, Kaichi), filed in the register as the unused secret weapon. <a href="sojo.html">Sojo</a> takes the right arm first. The book’s joke is institutional: a government builds a specialist whose art is meant for a weather blade, then the weather blade user removes the specialist’s arm before the art is the scene.</p>
    <p>She is not the commander. Hagiwara loses both legs and keeps a chapter title. She is not Kugara, childhood friend, iron body, the hallucination’s face. She is the newest, which in a six-person unit is a kind of cruelty all by itself. You barely learned the hallway. The hallway already has lightning in it.</p>
    <h2>Kaichi</h2>
    <p>Demon Monster. The archive will not invent a textbook. Unused is the important adjective. A secret weapon that is not used is still a fact about the people who staffed the unit: they believed Cloud Gouger needed a monster in reserve. Sojo did not wait for the reserve. Mei does not care about your org chart.</p>
    <p>Chihiro finds a True Realm in the same fight and loses an arm of his own. Parallel mutilation is not cute symmetry. It is the first book teaching that Enchanted Blades spend limbs whether you are the protagonist or the cavalry. Kazane’s arm is the state’s. Chihiro’s arm is the household’s. Sojo wants Datenseki more than he wants either of them whole.</p>
    <h2>Story role</h2>
    <p>Vs. Sojo is the only printed room so far that is hers. Hospital, specialists, compound, four graves, two survivors. This page will not invent which side of the grave/survivor line she finally occupies beyond the register’s injuries: arm first, unit shattered. The ACG desk holds the roster. Hagiwara’s file holds the leftover command. Kazane’s file holds the unused weapon, so the catalog does not have to pretend Kaichi was a rumor.</p>
    <p>When headquarters later fills with leftovers, the ACG survivors are still in the building. If Kazane is one of the two who walk, she walks as a one-armed secret. If she is one of the four graves, the secret died unused. The register’s “two survivors” is the authority until a chapter captions her pulse. This page will not flip a coin.</p>
    <h2>Notes</h2>
    <p>Kazane Machi (真智 カザネ). Kaichi. Right arm. For the commander, see <a href="hagiwara.html">Hagiwara</a>. For the weather sword, see <a href="../blades/cloud-gouger.html">Cloud Gouger</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Anti-Cloud Gouger", "../world/acg.html"),
        ("Hagiwara", "hagiwara.html"),
        ("Sojo", "sojo.html"),
        ("Cloud Gouger", "../blades/cloud-gouger.html"),
        ("Vs. Sojo", "../arcs/vs-sojo.html"),
    ],
)

character(
    "hasumi",
    "Shinsaku Hasumi",
    "蓮水 晋作",
    "Sorcery Bureau · the lab",
    "Lab chief in the war book. He comes to trust Kunishige, lets Shiba steal ore, then resigns when the bureau accepts Mikaboshi ceasefire terms.",
    "p-hasumi",
    "../assets/covers/hokazono-commemorative.jpg",
    "The kiln’s government half. Hasumi is the man who learns the eyes are real and still loses the politics.",
    [
        ("Affiliation", "Sorcery Bureau, Datenseki lab"),
        ("Role", "Lab chief in Part 2"),
        ("Turn", "Comes to trust Kunishige; later resigns"),
        ("Crisis", "Lets Shiba steal ore; disillusioned by ceasefire terms"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The lab</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Shinsaku Hasumi is the Sorcery Bureau’s Datenseki lab chief in Part 2. The lab fails. Shiba already knows whose eyes to hire. Hasumi comes to trust <a href="kunishige.html">Kunishige</a>, later lets <a href="shiba.html">Shiba</a> steal ore, and resigns after the bureau accepts Mikaboshi ceasefire terms. He is the government half of the kiln: a man who learns the mineral is real work and then watches his institution decide a princess is a bargaining chip.</p>
    <p>He is not Mashiro. Mashiro opposes taking stolen rock to a civilian smith and dies later to Ariu. Hasumi is the one who has to run the tests that fail until the civilian looks. He is not Joji. Joji is annoyed and ranked above the partners. Hasumi is the lab. When the lab becomes a political object, he leaves it.</p>
    <h2>The lab</h2>
    <p>About 250 kilograms of Datenseki are known. One pair of eyes ever made it safe. Hasumi’s job is the sentence before “one pair.” Fail, fail, fail, then a picky weapons dealer who will not sell to people he cannot stand. Trusting Kunishige is a scientific conclusion and a moral risk. Letting Shiba steal ore is the risk spent. Resignation is the receipt.</p>
    <p>Chapters 125 through 129 refuse montage. Smelting, Fire, Smelting, Smelting, Ironworks. Hokazono talked to a real swordsmith. Hasumi is the bureau person who has to stand near that refusal. The mineral wants to pop the user. Kunishige nearly dies in chapter 129. Chiaki pulls him back. A lab chief who has already seen failure knows what the fire is. He cannot sign the ceasefire with a clean face. Giyu might trade Chiaki. The bureau might accept. Hasumi resigns.</p>
    <h2>Story role</h2>
    <p>The Irishima talks are a battlefield titled as meetings. Hasumi is the meeting’s technical officer. Without him the book would skip from “vein showed” to “smith looks” with no government embarrassment. The embarrassment is the point. Japan harvests Irishima. The Mikaboshi come back. The lab does not produce a usable weapon on schedule. Enchanted Blades enter at plus one year and five months because a civilian was hired after the schedule failed.</p>
    <p>His resignation is the Bureau becoming an army becoming the Kamunabi, seen from the man who liked the work and hated the terms. Present-tense Kasen will later leak a smith’s address because he thinks blades are a path to order. Hasumi is the older version of a government scientist: he saw the ore, trusted the eyes, and left when the table offered a girl. The leak essay is Kasen’s disease. This page is the man who quit before that disease was the director’s job.</p>
    <h2>Notes</h2>
    <p>Shinsaku Hasumi (蓮水 晋作). Lab chief. Resigns. For the talks, see <a href="../manga/part-2.html">Part 2</a>. For the vein, see <a href="../analysis/irishima.html">Irishima’s vein</a>. For the partner who said no to the theft, see <a href="mashiro.html">Mashiro</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Part 2", "../manga/part-2.html"),
        ("Kunishige", "kunishige.html"),
        ("Shiba", "shiba.html"),
        ("Mashiro", "mashiro.html"),
        ("Irishima’s vein", "../analysis/irishima.html"),
    ],
)

print("wave2c: tamaki enji madoka kazane hasumi")
