#!/usr/bin/env python3
"""New character encyclopedia pages from the 2026 scrape. No em-dashes."""
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
    "hokuto",
    "Hokuto",
    "北兜",
    "Hishaku · swordsman",
    "The Hishaku swordsman who killed Ibuki Misaka so Cloud Gouger’s contract would open, then spent the rest of the book hunting a fight that would not disappoint him.",
    "p-hokuto",
    "../assets/covers/jp-vol10.webp",
    "Volume 10 jacket company. Hokuto shares the war photograph with Natsuki, Uruha, and Yura.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Role", "Swordsman; raid participant"),
        ("Sorcery", "Armored puppet (self-resembling armor, piece control)"),
        ("Known kills", '<a href="ibuki.html">Ibuki Misaka</a> (Cloud Gouger bearer); present at the Rokuhira raid'),
        ("Sought fights", '<a href="uruha.html">Yoji Uruha</a>, <a href="natsuki.html">Natsuki Misaka</a>'),
        ("Jacket", "Volume 10, <em>The Swordsmen</em>"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Hokuto dresses like a samurai because he wants the job to look like one. He is one of the ten <a href="../factions/hishaku.html">Hishaku</a>, flame-tattooed, fire-gated, and he is not the mind of the set. <a href="yura.html">Yura</a> decides which blade goes to which monster. Hokuto is the man you send when the monster has to die on a sword. He took part in the murder of <a href="kunishige.html">Kunishige Rokuhira</a>. Shortly after that raid he assassinated <a href="ibuki.html">Ibuki Misaka</a>, wartime bearer of <a href="../blades/cloud-gouger.html">Cloud Gouger</a>, so the Lifelong Contract would open and the Hishaku could sell the weather sword to a customer. The customer was <a href="sojo.html">Genichi Sojo</a>.</p>
    <p>He is not Sojo. Recaps that blur Hishaku and customer cannot explain why Cloud Gouger is in a bathhouse extra while Hokuto is still hunting Uruha. Sojo loved the smith’s work. Hokuto loves the fight. The raid was logistics. Ibuki was supposed to be the real meal, and Hokuto left disappointed: the man who had been equal to <a href="samura.html">Samura</a> in the war had already put the sword down. Killing a retired legend is not the same as killing the legend.</p>
    <p>He believes a sword does not exist for survival. It exists for a deadly battle. That sentence is the whole brief. It is also why Volume 10 can put him on a jacket with Natsuki, Uruha, and Yura and call the book <em>The Swordsmen</em>. Three of those four still think the blade is an argument. One of them thinks it is a government.</p>
    <h2>Personality</h2>
    <p>Cunning is the word the pages give him, and it is the right one if you mean he will use a puppet so the body can live long enough to enjoy the cut. Pride is the other word. He is proficient with a sword and wants that fact respected. He scorns a fight that has already ended, which is why Ibuki’s retirement offends him more than Ibuki’s death satisfies him. He seeks out strong fighters the way Sojo sought out Datenseki: as a problem that should answer back.</p>
    <p><a href="uruha.html">Yoji Uruha</a> is the meal he actually wants. Uruha is still a bearer in the present tense, still loyal to the Rokuhira name, still the prodigy who mastered Iai White Purity by sixteen. Hokuto will walk into Kamunabi headquarters for that. Natsuki, standing next to Uruha, is a bonus and an insult: the younger Misaka who kept training after his brother quit, who wanted Kumeyuri and did not get it, who now wants recognition beside the people Hokuto already tried to erase.</p>
    <p>He is not Hiruhiko. Hiruhiko is eighteen and loud and treats friendship as a blade. Hokuto is older in manner even when the pages do not print an age. He wants a duel that looks like history. The armor puppet is a craftsman’s cheat that lets him stay in the room after a body should have left it. He will use the cheat. He will still talk as if the sword is the only honest object.</p>
    <h2>Abilities</h2>
    <p>His sorcery controls an armored puppet that resembles himself. He can manipulate individual pieces of that armor for defense. Through that art he stood in the Rokuhira house when Kunishige died. The puppet is not a replacement for swordsmanship. It is how a man who wants a lethal fight keeps having one. Piece control means a slash that should have ended the scene becomes a discarded plate. The body behind the plate is still looking for someone who will not miss.</p>
    <p>He carries himself as a swordsman first. The Hishaku shared fire-gate is available to all ten; Toto is the one who uses it as a habit. Hokuto would rather close distance with steel. That preference is why Chihiro’s circle treats him as a blade problem, not a fireworks problem. It is also why Natsuki’s Lightning Menace is the matching language: two men who think weather and armor are just ways to keep a sword conversation going.</p>
    <h2>Story role</h2>
    <p>Three years before the main story, three Hishaku hit the Rokuhira workshop. Hokuto is named among the killers. The six wartime blades leave in their hands. Enten stays with the son. In the same campaign he murders Ibuki. Cloud Gouger’s contract opens. Yura later sells the sword to Sojo in early October of the present. Without Hokuto’s kill, there is no Vs. Sojo arc as printed. Char is not hunted as a stabilizer for a stolen weather blade. Chihiro does not lose an arm finding the True Realm. The first wartime sword is not shown to be mortal. Hokuto is the off-page locksmith of Part 1’s first book.</p>
    <p>He returns to the present tense in the Sword Bearer Assassination arc, when the Hishaku stop being a rumor in a cellar and become a four-man jacket. Volume 10 puts him opposite Natsuki, with Uruha and Yura in the same photograph. Inside Kamunabi headquarters, Uruha (contract cut, Crimson Recital limping back) joins Natsuki to confront Yura and Hokuto. Yura is the remote Magatsumi problem. Hokuto is the swordsman problem. Kasen’s leak is already on the table. The state’s best remaining blades and the men who opened the contracts are in the same corridor.</p>
    <p>He is not the end of the Hishaku. Yura still walks to the cell. Yukisada still sits in the barrier. Hiruhiko still exists as the younger loud blade. Hokuto’s job in the long book is to prove that the raid was not a unique night of violence. It was a method. Kill the bearer, open the contract, sell or spend the steel. Ibuki was the method applied to Cloud Gouger. Uruha was supposed to be the method applied to Kumeyuri, until Samura’s false death scrambled the inventory. Hokuto is still looking for a fight that feels like the war. The war, in Part 2, is busy being smelted on Irishima. He is not invited.</p>
    <h2>Notes</h2>
    <p>Eight of the ten Hishaku are named on this site. Hokuto is one of the named. This archive will not invent the remaining two. He shares the Volume 10 jacket with Natsuki, Uruha, and Yura because the book wants you to see swordsmen before you see factions. The palette of that book is a four-man war ensemble, not a villain spotlight. Read it next to chapter 91, “Natsuki,” and chapter 92, “The Swordsmen.”</p>
    <p>Ibuki’s death is the quiet hinge of the Cloud Gouger story. The public remembers Sojo. The contract remembers Hokuto. For the original bearer’s file, see <a href="ibuki.html">Ibuki Misaka</a>. For the brother who kept the sword after the retirement, see <a href="natsuki.html">Natsuki</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Ibuki Misaka", "ibuki.html"),
        ("Natsuki Misaka", "natsuki.html"),
        ("Cloud Gouger", "../blades/cloud-gouger.html"),
        ("Yura", "yura.html"),
    ],
)

character(
    "kuguri",
    "Kuguri",
    "久々李",
    "Hishaku · Twilight Wave",
    "The Hishaku swordsman who called an uncontracted Enchanted Blade unrequited love, then watched Chihiro fake Iai White Purity and forgot the kidnapping.",
    "p-kuguri",
    "../assets/portraits/hiruhiko.webp",
    "Hishaku company. Kuguri hunts with Toto; Hiruhiko is the louder younger blade.",
    [
        ("Affiliation", '<a href="../factions/hishaku.html">Hishaku</a>'),
        ("Sorcery", "Twilight Wave (破暮, Hagure)"),
        ("Enchanted Blade", "Carries one without a Lifelong Contract"),
        ("Partners", "Toto (blood tracking); later Hiruhiko in Kyoto"),
        ("Known for", "Chihiro copies Iai White Purity off him"),
        ("Arc", '<a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a>'),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Kuguri is one of the ten <a href="../factions/hishaku.html">Hishaku</a>. He is a ruthless swordsman who thrives in battle and scorns anyone who treats swordsmanship as a hobby. He carries an Enchanted Blade without a Lifelong Contract. He describes that state as unrequited love: the steel is in the hand, the nerves are not rewritten, the innate art is still his. Most of the book’s bearers lose their original sorcery when they sign. Kuguri kept Twilight Wave and still wants the marriage.</p>
    <p>He is not the leader. Yura is the mind. Hiruhiko is the loud eighteen-year-old who thinks Chihiro is a peer. Kuguri is the professional who was sent to Kyoto to take <a href="iori.html">Iori Samura</a> off the board so Samura would have to flinch. Toto tracks by blood. Kuguri closes. The Kyoto Bloodshed Hotel is where that job meets a smith’s son who learns styles by watching, and where the job ceases to matter because the fight got interesting.</p>
    <h2>Personality</h2>
    <p>He hates frivolous swordsmanship. That is not a metaphor. He will abandon a kidnapping if the person in front of him starts treating a katana as a serious object. Chihiro, copying Iai White Purity in a hotel corridor with his eyes shut because that is how the curriculum works, is the opposite of frivolous. Kuguri goes from unimpressed to consumed. The mission was Iori. The scene becomes Chihiro. Toto is the one who still remembers they had a schedule.</p>
    <p>Unrequited love is a precise phrase in a book that already treats blades as partners. Chihiro talks to Enten as household. Sojo talked to Cloud Gouger as craft. Samura talks to Tobimune as religion. Kuguri talks to a sword that will not sign him back. He is the Hishaku version of a fan who cannot get the author to answer mail. Unlike Sojo, he still has his own art. Unlike Hiruhiko, he does not confuse play with mastery. He wants the contract. He will not pretend a borrowed charge is the same thing.</p>
    <h2>Abilities</h2>
    <p><strong>Twilight Wave</strong> (破暮, Hagure) absorbs and stores kinetic energy and heat from his movements indefinitely, then releases it in explosive bursts proportional to what he has banked. The art wants time. In a short exchange he often relies on the katana alone, because the battery has not filled. In a long one he becomes a delayed explosion with a swordsman’s manners. That is why he can hunt without looking like a fireworks user, and why a hotel fight that lasts is more dangerous than a street ambush that does not.</p>
    <p>The uncontracted Enchanted Blade is a separate problem. He pursues a deeper connection with it while still spending Twilight Wave. The Hishaku spent three years killing bearers to open wartime contracts. Kuguri is walking around with steel that has not accepted him, which means either the blade’s bearer is still alive or the Hishaku have not finished the paperwork. This archive will not invent which wartime sword he is courting. The chapters have not printed the name on his hip as a caption. The attitude is the entry.</p>
    <p>He is skilled enough that Chihiro, who already copied Uruha and Samura and Iori by sight, uses him as a live Iai dummy. The hotel is a school. Kuguri is an unwilling instructor. That is a humiliation only if you think teaching is lesser than killing. Kuguri thinks a real fight is the point. Chihiro giving him one is, in his terms, respect.</p>
    <h2>Story role</h2>
    <p>After Senkutsuji, Samura’s apparent betrayal, and the nationwide Owl, the Hishaku move on Iori. Toto has blood from the temple attack. Sumi of the Masumi puts Iori on a motorcycle. Kuguri gives chase. The Kyoto Bloodshed Hotel, run by Yojiro Sengoku of the Reigen One-Sword Style, is the Masumi’s chosen veil. Chihiro is there to keep Iori alive and to tell her the truth her father erased. Kuguri is there to take her. They occupy the same building. Chihiro starts shutting his eyes.</p>
    <p>The first impression is contempt. A boy faking a school he did not inherit. Then the fake starts working. Iai White Purity is speed with the lids down. Chihiro is a smith’s son, not Itsuo Shirakai’s student, and he is still fast enough that Kuguri drops the errand. Battle frenzy is the text’s word. Hiruhiko later joins the Kyoto wrecking; Play takes the upper floors apart; Samura arrives because two Enchanted Blades in one hotel is a beacon Owl can see. Toto pulls comrades out through the fire-gate when the scene turns fatal. Kuguri is extracted rather than finished. The kidnapping fails. Iori’s seal breaks because she shields a classmate, not because Kuguri succeeded.</p>
    <p>He remains in the ten. He is not the HQ infiltration’s face; that is Yura, Yukisada, Hokuto, Bingo’s lucky charms, the Shigyu brothers. Kuguri’s chapter of the book is the hotel: the place where Chihiro’s imitation becomes a style, where Iori’s memory starts to leak, where a Hishaku swordsman chose a duel over a bag. The long book needs that scene because Enten versus Tobimune only works if Chihiro has already learned to draw without looking.</p>
    <h2>Notes</h2>
    <p>Toto is the partner on the Iori job: blood tracking, fire-gate rescue, a preference for not standing in the cut. Hiruhiko is the other Kyoto Hishaku, already beaten once on the train, already contracted to Kumeyuri, already treating Chihiro as a friend-shaped rival. Kuguri is the one who takes swordsmanship personally. Chapter 65 is “Imitate.” Chapter 70 is “Iai White Purity Style.” Those titles are his classroom, even if the table of contents does not print his name on them.</p>
    <p>For the clan that sent him, see the <a href="../factions/hishaku.html">Hishaku page</a>. For the school he accidentally taught, see <a href="../world/iai.html">Iai White Purity</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hishaku", "../factions/hishaku.html"),
        ("Chihiro", "chihiro.html"),
        ("Iori", "iori.html"),
        ("Hiruhiko", "hiruhiko.html"),
        ("Iai White Purity", "../world/iai.html"),
    ],
)

character(
    "natsuki",
    "Natsuki Misaka",
    "巳坂 奈ツ基",
    "Kamunabi · Lightning Menace",
    "Ibuki Misaka’s younger brother. The Kamunabi swordsman who wanted Kumeyuri, kept training after the war, and still wants to stand next to the bearers the press already named.",
    "p-natsuki",
    "../assets/covers/jp-vol10.webp",
    "Volume 10 jacket: Natsuki, Hokuto, Uruha, Yura. The state’s swordsman in a four-man war photograph.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Rank", "Squadron leader"),
        ("Sorcery", "Lightning Menace (雷躯, Raiku)"),
        ("Family", '<a href="ibuki.html">Ibuki Misaka</a> (older brother; Cloud Gouger bearer)'),
        ("Wanted blade", '<a href="../blades/kumeyuri.html">Kumeyuri</a> (Uruha was chosen)'),
        ("Jacket", "Volume 10, <em>The Swordsmen</em>"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Natsuki Misaka is an elite Kamunabi swordsman and squadron leader. He is the younger brother of <a href="ibuki.html">Ibuki Misaka</a>, wartime bearer of Cloud Gouger. Together they were nearly unstoppable. After the Seitei War, Ibuki put the sword down for reasons the chapters have not fully unpacked. Natsuki did not. He is still in the building. He still wants the kind of recognition the Enchanted Blade bearers got in the newspapers, and he still has to live with the fact that <a href="uruha.html">Yoji Uruha</a> was chosen for <a href="../blades/kumeyuri.html">Kumeyuri</a> when Natsuki was in the room as a candidate.</p>
    <p>Hokuto of the Hishaku murdered Ibuki so Cloud Gouger’s contract would open. Natsuki’s present-tense job is therefore double: serve the Kamunabi against the ten who raided the Rokuhira house, and avenge a brother who had already retired. He is not a bearer. Lightning Menace is an innate art, not a Datenseki overflow. Volume 10 still puts him on the jacket with Uruha, Hokuto, and Yura, because the book is willing to call a non-bearer a swordsman in the same photograph as a Hishaku killer and a wartime prodigy. That is the respect he wanted. It arrives as a war picture, not a parade.</p>
    <h2>Personality</h2>
    <p>Resentment of Uruha is printed, not inferred. It is not only envy of a blade. It is the specific injury of being almost chosen, then watching the chosen man lose the will to live when Kunishige died, then watching that man walk again because Chihiro exists. Natsuki kept training in the years Uruha sat in a Sanso. He wants equal recognition beside his brother and the other bearers. Equal is the word. Not above. Beside. The Misaka pair used to be a closed system. The war opened it and handed the famous sword to someone else.</p>
    <p>He is not Hiyuki. Hiyuki is the pointed end with a hereditary skeleton and a temper that hides a kind line. Natsuki is a swordsman who thinks in duels and ledgers. He will fight next to Uruha when the Hishaku are in the headquarters, because the alternative is letting Hokuto write the end of the Misaka story twice. Working with the man who got Kumeyuri is the adult version of the childhood formation: two Misaka-adjacent blades in one corridor, except one of them is Uruha, and the weather sword is already bisected in Chihiro’s bag.</p>
    <h2>Abilities</h2>
    <p><strong>Lightning Menace</strong> (雷躯, Raiku) imbues his movements and attacks with lightning. It is not Cloud Gouger. Mei is a goldfish-sized weather event that leaves the body as a dragon and a bolt. Raiku is still inside the nervous system: a man moving like a charge, a cut that arrives with voltage. Readers who flatten every lightning user into Sojo are doing the book a disservice. Sojo was a customer with a stolen katana. Natsuki is a government swordsman with a family art that happens to share an element with his brother’s former blade. The rhyme is cruel. It is also useful against Hokuto’s armor, which is built to discard pieces, not to ground a storm.</p>
    <p>He is a squadron leader, which means the Kamunabi trust him with people, not only with a room. Kiri Shirakai is the other named squadron leader in the long book: odachi, dance-like footwork, a granddaughter at war with her grandfather’s curriculum. Natsuki’s kit is narrower and meaner. He wants to stand where Ibuki stood. The art is how he keeps standing there without Datenseki.</p>
    <h2>Story role</h2>
    <p>For most of Part 1 he is a name in the war ensemble, a jacket face, a reason the Misaka story is not only a grave. Chapter 91 is titled “Natsuki.” Chapter 92 is “The Swordsmen.” That pairing is the book announcing him as a person rather than a caption on Ibuki’s file. Inside HQ, after Kasen’s leak is on the table and Yura is spending Magatsumi at range, Uruha (alive, contract severed, Crimson Recital returning) joins Natsuki to confront Yura and Hokuto. Azami arrives when that goes badly. Yura is the remote masterpiece. Hokuto is the man who killed the older Misaka. Natsuki is finally in the room with both problems.</p>
    <p>He does not get a True Realm, because he does not have an Enchanted Blade. He gets a volume title shared with three other men and a fight in a building that is about to host the Sword Master in someone else’s skin. That is the Kamunabi bargain: you can be elite, you can be a jacket, you can lose a brother, and the myth of the war still will not print your name on a katana. Chihiro, who does have a katana, is busy telling Samura that Enten exists to end the others. Natsuki is busy proving you can be a swordsman in this book without being a bearer. The jacket agrees. The cell in the basement does not care.</p>
    <h2>Notes</h2>
    <p>Ibuki was regarded as equal in skill to Samura during the war. Natsuki’s whole life is standing next to that sentence. After the war Ibuki abandoned swordsmanship; Hokuto found a shadow and was disappointed. Natsuki is the remaining sharpness in the family. Lightning Menace is the remaining weather. Cloud Gouger, once bisected, spends its last charges in Chihiro’s rebuilt arm at the Rakuzaichi and then dies. The Misaka blade is gone. The Misaka swordsman is not.</p>
    <p>Volume 10, <em>The Swordsmen</em>, ISBN 978-4-08-884740-5, 5 January 2026. Jacket faces: Natsuki, Hokuto, Uruha, Yura. For the original Cloud Gouger bearer, see <a href="ibuki.html">Ibuki</a>. For the man who killed him, see <a href="hokuto.html">Hokuto</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Ibuki Misaka", "ibuki.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Uruha", "uruha.html"),
        ("Hokuto", "hokuto.html"),
        ("Kumeyuri", "../blades/kumeyuri.html"),
    ],
)

character(
    "kasen",
    "Kasen",
    "嘉仙",
    "Kamunabi director · the leak",
    "The long-bearded director who helped seal Shinuchi, then leaked Kunishige’s address because he still thought Enchanted Blades were a path to order.",
    "p-kasen",
    "../assets/portraits/azami.webp",
    "Kamunabi leadership. Kasen sits at the same table as Azami, Ichiki, and Yatsuru.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Office", "Director"),
        ("Arts", "Barrier and sealing (learned)"),
        ("War work", "Sealed Shinuchi with Ichiki and Yatsuru"),
        ("Crime", "Leaked Kunishige Rokuhira’s location to the Hishaku"),
        ("Motive", "Enchanted Blades as a tool of national order"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Kasen is the director of the <a href="../factions/kamunabi.html">Kamunabi</a>. Long beard, stoic public face, one of the agency’s most skilled sorcerers in the learned arts: barriers, seals, the kind of work that makes a masterpiece stay in a box. After the Seitei War he sealed <a href="../blades/magatsumi.html">Shinuchi</a> with Ichiki and Yatsuru. He also helped build the myth that the bearers were heroes and the island was a victory. Eighteen years later he is still director. He still believes the path to peace is to use the Enchanted Blades to create order. That belief is how you get a government leaking a smith’s address to the men who will murder him.</p>
    <p>He laments that the Kamunabi cannot command respect from the preexisting major sorcery clans. The Soga had foresight. The Sazanami had an auction. The Masumi had a master they would die for. The Kamunabi have a basement and a press release. Kasen’s solution is not reform. It is steel. If the clans will not bow to a bureau, they will bow to Datenseki that overflow as weather. He conspired with the <a href="../factions/hishaku.html">Hishaku</a> and gave them <a href="kunishige.html">Kunishige</a>. Chihiro’s entire revenge plot is, among other things, a director’s policy working as designed.</p>
    <h2>Personality</h2>
    <p>Stoic is the jacket word. Ideological is the accurate one. He is not Yura. Yura bets his life on a coin and talks to God. Kasen bets the country on a cellar of swords and talks like a civil servant. He is not Azami. Azami helped hide Kunishige, hates the Hishaku, and still works inside the building. Kasen helped hide the <em>blade</em>, then decided the smith was an obstacle to using it. The distinction matters. Several Kamunabi heads (Azami, Kudo, Ichiki) spent political capital keeping Kunishige alive after Malediction. Kasen spent it the other way.</p>
    <p>He wants respect. That is a small sentence for a large crime. The Enchanted Blades are, in his reading, the only language left that clans and criminals both understand. Magatsumi in particular is a master key: kill Akemura and the other wartime bearers die; destroy Magatsumi and the knot comes apart; use Magatsumi and you rewrite the map. Kasen would rather the state hold that key than a hermit in a workshop. The Hishaku were a tool for removing the hermit. They were not supposed to become the new holders. Tools have opinions. Yura’s opinion was Shinuchi for himself, then Shinuchi for a conversation with the Sword Master.</p>
    <h2>Abilities</h2>
    <p>Barrier and sealing, learned rather than a flashy innate signature. He sealed Shinuchi with Ichiki and Yatsuru, which means the box Yura later cracks is partly Kasen’s work. Cracking a seal you helped tie is a special kind of institutional failure. He is named as one of the most powerful sorcerers in the leadership, which in this book does not always mean a named attack. It means you can keep a god in a room. Until you cannot. Until a director’s leak and a Hishaku vessel named Yukisada split the headquarters barrier from the inside.</p>
    <p>The White Robes (Kasen, Ichiki, Yatsuru) are the learned core. Azami is brute Coin and an executioner’s manners. Izaru makes rosary chains. Kudo’s Warrior’s Path sends a body through walls, and then Kudo dies for Hakuri. Kasen’s art is the building. When the building fails, the art is implicated.</p>
    <h2>Story role</h2>
    <p>After the war: seal Shinuchi, file Malediction as victory, let Kunishige disappear with six swords. Three years before the present: leak the address. Three Hishaku hit the house. Kunishige dies. Ibuki dies in the same campaign. The remaining bearers go into Sanso fortresses. Chihiro takes Enten underground. Kasen remains director. The Kamunabi spend three years fighting the Hishaku for blades the Hishaku cannot fully use because the contracts are still tied to living nerves. That stalemate is Kasen’s mess. He wanted the state to own the steel. He created a black market instead.</p>
    <p>In the Sword Bearer Assassination arc the leak becomes printable. Volume 10’s summary is the leadership table discovering that their director conspired to use Shinuchi’s power to rule. Yura already has remote access to Magatsumi’s abilities through spirit energy he left in the blade. Kasen’s order fantasy and Yura’s possession path occupy the same object. When Yura reaches Akemura’s cell, the Sword Master is sane. The director’s plan (blades as order) and the Hishaku plan (blades as lever) both collapse into Akemura standing up in another man’s body and taking the Kamunabi as a vehicle. Part 1 ends with the basement winning. Kasen wanted a tool. He midwifed a second Malediction risk in the capital.</p>
    <p>Chihiro’s deal with the Kamunabi (Magatsumi to the state, Enten in his hand, Hakuri as logistics) assumed a state that wanted the blades sealed. Kasen’s faction assumed a state that wanted them used. Those are not the same bureau. Azami is still in the first one. The leak is how you tell them apart. Hiyuki, pointed at Chihiro in the auction arc, is the bureau as it wishes it looked: a weapon on a permission slip, angry, still capable of evacuating prisoners. Kasen is the bureau as it actually budgets: a myth, a box, a leaked map.</p>
    <h2>Notes</h2>
    <p>Ichiki trained Shiba and Azami during the war and later helped hide Kunishige. Yatsuru is the sole woman among the named leaders, master of the same sealing work. Izaru distrusts Chihiro and blamed Kunishige for “stealing” the blades. Kudo dies. Kasen is the one who made the raid possible. The <a href="../factions/kamunabi.html">Kamunabi page</a> is the org chart. This page is the policy.</p>
    <p>The leak is not a twist for its own sake. It is the setting explaining itself. A government that covered up 200,000 civilians will cover up a smith. A director who thinks order lives in Magatsumi will not protect the man who refused to let Magatsumi be used. For the blade he wanted to govern with, see <a href="../blades/magatsumi.html">Magatsumi</a>. For the man whose address he sold, see <a href="kunishige.html">Kunishige</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Kunishige", "kunishige.html"),
        ("Yura", "yura.html"),
        ("Azami", "azami.html"),
        ("Magatsumi", "../blades/magatsumi.html"),
    ],
)

character(
    "subaru",
    "Subaru Urita",
    "瓜田 すば琉",
    "Enchanted Blade bearer · Sushi Subaru",
    "A surviving wartime bearer whose primary occupation is sushi, who helped Kunishige start the Enchanted Blades, and who still will not let this archive invent the name of his sword.",
    "p-subaru",
    "../assets/portraits/kunishige.webp",
    "Fellow smith. Subaru was a prolific swordsmith before the war; the pages still will not caption his Enchanted Blade.",
    [
        ("Occupation", "Sushi chef (Sushi Subaru); swordsmith; blade bearer"),
        ("Style", "Sand-Bone One-Sword Style"),
        ("Sorcery", "Self-duplication"),
        ("War role", "Enchanted Blade bearer; helped Kunishige begin the blades"),
        ("Blade", "Unnamed in publication (one of two still unlabeled)"),
        ("Status", "Relocated by the Kamunabi after the Sanso attacks"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Subaru Urita is an older man, hachimaki, mustache, scar over the right eye, and one of the last surviving Enchanted Blade bearers. Before the Seitei War he was considered one of Japan’s most prolific swordsmiths. His primary occupation and passion is sushi. He owns a restaurant called Sushi Subaru. That sentence is not a gag the book forgot to cut. It is the point. Kunishige was a picky weapons dealer who barely ate. Subaru is a smith who feeds people on purpose. They liked each other immediately. Subaru helped Kunishige start forging the Enchanted Blades. The word yōtō, the Japanese term this site renders as Enchanted Blade, is credited to him in the wiki’s craft notes. A sushi chef named the national sin.</p>
    <p>He is a master of the Sand-Bone One-Sword Style. He is also a sorcerer who can duplicate himself. He is not Samura, not Uruha, not Akemura, not Ibuki. He is the portrait in the war ensemble that still has a name and still does not have a printed sword title. One wartime blade remains unlabeled even as Subaru is known. This archive will not invent the missing name. The chapters have had 129 tries. When Jump captions it, this page moves.</p>
    <h2>Personality</h2>
    <p>He took a liking to Kunishige shortly after they met. In a series about men who love blades past the point of civilization, Subaru’s affection lands as professional and domestic at once: another smith, a younger one with impossible eyes, a project that will become six war crimes and a seventh apology. Helping start the Enchanted Blades is not the same as wielding Magatsumi. It is closer to handing someone a kiln. Subaru is complicit in the way a colleague is complicit. He is not the Sword Master. He is the man who thought the work was interesting and then had to live inside the myth the Kamunabi built around it.</p>
    <p>Sushi as primary passion is a moral tell. Sojo rated bathhouses. Subaru rates fish. Both are craftsmen adjacent to slaughter who insist on a civilian skill. The difference is that Subaru’s civilian skill is how he wants to be known, and Sojo’s was a volume extra packed next to a Datenseki suicide. After the raid on Kunishige and the death of Ibuki, the Kamunabi locked remaining bearers in Sanso fortresses. When the Hishaku started hitting those fortresses, Subaru was relocated. He is alive. He is not on the Vs. Sojo stage. He is not at the Rakuzaichi. He is the reminder that the war’s toolkit still has unnamed steel in a living body the plot has not spent yet.</p>
    <h2>Abilities</h2>
    <p>Sand-Bone One-Sword Style is his school, distinct from Iai White Purity (Itsuo Shirakai, Samura, Uruha, Iori, Chihiro-by-imitation) and from Kiri’s oversized odachi work. This archive will not fake a curriculum the pages have not demonstrated at length. The name is the entry. Duplication sorcery is the innate art: several Subarus, which is a nightmare for anyone trying to assassinate a bearer to open a contract. Kill one. Another is still holding the unnamed blade. The Hishaku’s whole three-year method (kill bearer, open contract, spend steel) is poorly matched to a man who can be plural. That may be why he was relocated rather than used as bait. It may be why he has survived into chapter 129 while Samura has not.</p>
    <p>The Enchanted Blade itself remains unnamed. Five blades have public technique lists (Enten, Cloud Gouger, Magatsumi, Kumeyuri, Tobimune). Two wartime swords do not. Subaru is a surviving bearer. One portrait in the war ensemble is still unlabeled. Do not collapse those two facts into a caption this site cannot source. He helped forge. He bears. The steel’s shape, fish, weather, or otherwise, is still magazine-only in the sense that it has not been given to the encyclopedia as a name.</p>
    <h2>Story role</h2>
    <p>Before the war he is part of the reason the Enchanted Blade project exists: a senior smith who takes Kunishige seriously when the Sorcery Bureau’s Datenseki research is going nowhere. Shiba believes Kunishige’s eyes are the only way to make the mineral usable. Subaru is the other smith in the room who can tell that is not flattery. The blades enter at plus one year and five months. Subaru is among the six. After Malediction he is part of the surviving set the Kamunabi hide and praise. After the Rokuhira raid he is part of the set they lock in Sanso. After Kokugoku and Senkutsuji he is moved.</p>
    <p>Part 2 returns to Irishima and the forge. Kunishige is not yet a hermit. Chiaki is a princess with foresight. The first fire is on the page in chapters 125 through 129. Subaru’s present-tense body is still in whatever safehouse the Kamunabi chose. His past-tense craft is in every bar of steel Kunishige cuts. If Part 2 is the smelting manual, Subaru is a footnote that might become a chapter. This page will not promote him to Magatsumi’s equal. It will not skip him because he sells sushi. The book named the restaurant. That is a tell.</p>
    <h2>Notes</h2>
    <p>Two wartime blades remain unnamed. Subaru Urita is a surviving bearer. Ibuki is dead; Cloud Gouger is named and bisected. Samura is dead; Tobimune went to Iori. Uruha lives with a severed contract; Kumeyuri was recovered by Ro. Akemura lives in a stolen body; Magatsumi is loose. The unlabeled steel and the unlabeled portrait are the remaining inventory. This archive lists Subaru here so the index stops pretending the war had only three famous names.</p>
    <p>For the project he helped start, see <a href="../blades/index.html">Enchanted Blades</a> and <a href="kunishige.html">Kunishige</a>. For the government that relocated him, see <a href="../factions/kamunabi.html">Kamunabi</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Kunishige", "kunishige.html"),
        ("Enchanted Blades", "../blades/index.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Ibuki Misaka", "ibuki.html"),
        ("Seitei War", "../arcs/seitei-war.html"),
    ],
)

character(
    "tafuku",
    "Tafuku Mihara",
    "美原 多福",
    "Kamunabi · duel domain",
    "Hiyuki Kagari’s partner. Looks like a sumo wrestler, fights like a referee, and is the calm half of the Kamunabi’s idea of a perfect act.",
    "p-tafuku",
    "../assets/portraits/hiyuki.webp",
    "Hiyuki’s partner. Tafuku’s domain is the room; her skeleton is the argument.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Partner", '<a href="hiyuki.html">Hiyuki Kagari</a>'),
        ("Sorcery", "Two-person duel domain"),
        ("Manner", "Nonchalant, calm"),
        ("Arc", '<a href="../arcs/rakuzaichi.html">Rakuzaichi</a> onward'),
        ("Notes", "Comes to respect Chihiro after starting as an enemy"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Tafuku Mihara is <a href="hiyuki.html">Hiyuki Kagari</a>’s partner in the Kamunabi. He looks like a sumo wrestler. His sorcery creates a separate domain where a battle between two combatants takes place, and the domain disappears when the battle is considered over. That is a referee’s art in a book about people who hate referees. Hiyuki is the pointed end: Flame Bone of the Starving, short temper, kind line underneath, authorization up to a rib. Tafuku is the room she fights in. Together they are how the state wishes it looked. The Anti-Cloud Gouger Special Forces were how it actually looked in the first arc: six specialists, four dead, a commander without legs.</p>
    <p>They begin as Chihiro’s enemies. The Kamunabi want Enchanted Blades under seal. Chihiro has the seventh and will not hand it over. Hiyuki is assigned. Tafuku arrives with her. He quickly comes to respect Chihiro, which is not the same as changing sides. Respect in this book means you will stop calling someone a thief long enough to evacuate an auction house with them. The Rakuzaichi is where that happens. Shinuchi is listed. Prisoners are in the Storehouse. Kyora is dying into Magatsumi. Hiyuki and Chihiro keep the building from becoming a second island. Tafuku’s domain is the kind of tool that makes a two-person argument possible in a collapsing firm.</p>
    <h2>Personality</h2>
    <p>Nonchalant and calm, in contrast to Hiyuki’s boisterousness. The pairing is vaudeville on purpose. She yells. He does not. She wears a skeleton the Kamunabi licensed. He wears a body that reads as a rikishi and an art that reads as a dohyō. The joke is structural. Flame Bone is one of the few innate arts the text will stand next to an Enchanted Blade. A duel domain is how you keep that art from becoming a city event. Tafuku is the permission slip’s other half: not the authorization to wear more bone, the authorization to put a wall around the wearing.</p>
    <p>He is not comic relief in the Hiruhiko sense. Hiruhiko’s jokes are cruelty. Tafuku’s calm is competence. When he starts respecting Chihiro, it is because Chihiro will spend a body without spending the people inside the building. That is Hiyuki’s secret too. The three of them, in the auction’s last hour, are a temporary government that works. Then the truce ends, Chihiro hands Magatsumi over, and Tafuku goes back to being the state’s furniture. Furniture that can isolate a god is still furniture the director can leak around.</p>
    <h2>Abilities</h2>
    <p>The duel domain isolates two combatants. When the fight is over, the domain goes. It is not Storehouse. Hakuri’s Kura warehouses people and charged objects across geography. Tafuku’s space is a match, not a vault. It is not Magatsumi’s field, which rewrites the ground into flowers. It is a rule. Two people. One argument. Then the street exists again. Against an Enchanted Blade, a rule like that is either salvation or a trap. Against Hiyuki’s own Flame Bone, it is how the Kamunabi practice not burning the prefecture.</p>
    <p>He is elite. The pages put him next to Hiyuki as a pair you send at problems the organization cannot file. He is not a squadron leader in the Natsuki/Kiri sense. He is not a White Robe. He is operations. When the HQ infiltration starts, the named crises are Yukisada in the barrier, Kudo dying, Azami versus the Shigyu brothers, Yura walking toward the cell. Tafuku’s absence from those captions is not a death notice. It is a reminder that the perfect act was for the auction camera. The basement does not use referees.</p>
    <h2>Story role</h2>
    <p>He enters with Hiyuki after Sojo, when Shinuchi is listed at the 208th Rakuzaichi. Chihiro has just learned that government squads die. Now he learns that the Kamunabi also has a celebrity weapon and a calm partner. Hiyuki wants Enten. Chihiro wants the prisoners out and Magatsumi not in Kyora. Tafuku makes their fights containable. Hakuri makes their logistics possible. Shiba makes their exits possible. The auction ends. Chihiro joins the Kamunabi on terms. Tafuku is part of the terms: the state as a set of people you have already bled beside, not only a director who sold your father.</p>
    <p>Later, when Kasen’s leak is printed and Akemura stands up, the perfect act is not enough. Flame Bone does not beat Magatsumi. A duel domain does not hold a possession. Hiyuki’s essay on this site is about a skeleton on a permission slip. Tafuku’s page is about the slip’s margin: the man who believed a fight could have an ending bell. Part 1’s last bell is Samura dying. Part 2’s first bell is a forge on Irishima. Tafuku is still, as of the chapters collected here, the partner you want if the problem is Hiyuki-sized. The problem became uncle-sized.</p>
    <h2>Notes</h2>
    <p>Hiyuki is stated as the Kamunabi’s strongest fighter and one of the few who can oppose an Enchanted Blade. Tafuku is not given that sentence. He is given the domain. Read them as a unit, then read the Anti-Cloud Gouger Special Forces as the unit the state actually spent on Sojo. The difference is the book’s opinion of institutions. For Hiyuki’s full file, see <a href="hiyuki.html">Hiyuki Kagari</a>. For the skeleton, see the <a href="../analysis/flame-bone.html">Flame Bone essay</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Hiyuki Kagari", "hiyuki.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Flame Bone essay", "../analysis/flame-bone.html"),
        ("Rakuzaichi", "../arcs/rakuzaichi.html"),
        ("Chihiro", "chihiro.html"),
    ],
)

character(
    "kiri",
    "Kiri Shirakai",
    "白廻 斬",
    "Kamunabi · Iai’s granddaughter",
    "Itsuo Shirakai’s granddaughter. Two-meter odachi, dance-like footwork, and a vow to decapitate the man who said women cannot master the style.",
    "p-kiri",
    "../assets/portraits/iori.webp",
    "Another Iai household. Kiri rejects the founder; Iori inherited a father instead of a grandfather.",
    [
        ("Affiliation", '<a href="../factions/kamunabi.html">Kamunabi</a>'),
        ("Rank", "Squadron leader"),
        ("Family", "Granddaughter of Itsuo Shirakai (Iai White Purity founder)"),
        ("Weapon", "Oversized odachi (about two meters; five-shaku blade)"),
        ("Raised by", "Uruha and Samura, in part, as Shirakai’s students"),
        ("Chapter", "90, “Kiri” (斬ちゃん)"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Kiri Shirakai is an elite Kamunabi swordswoman and squadron leader. She is the granddaughter of Itsuo Shirakai, founder of <a href="../world/iai.html">Iai White Purity Style</a>, the speed school that asks you to close your eyes. Samura and Uruha are the famous students. Chihiro is the famous copier. Kiri is the family. Raised in part by those students, she rejects her grandfather’s belief that women cannot master swordsmanship. She has sworn to decapitate him to prove the point. He is still alive, in the mountains, communicating with her by text. The founder of the fastest style in the book is a misogynist on a feature phone. Kiri is the correction, carrying a two-meter odachi that the curriculum was not designed for.</p>
    <p>Chapter 90 is titled “Kiri” (斬ちゃん). The cute suffix is the book’s tell: everyone else says Kiri-chan; the page is a squadron leader escorting Hakuri toward Shinuchi while the headquarters is coming apart. She is not Iori. Iori’s Iai comes back when she shields a classmate, eyes closed, memory unsealed. Kiri never had her style erased. She had it denied. Those are different injuries. Both of them close the distance in a family that treats women as a problem for the school.</p>
    <h2>Personality</h2>
    <p>She is not performing humility for the founder. The vow is explicit. Shirakai’s unconventional methodology (speed, closed eyes) drew ridicule until it killed the ridiculers. He remained, in the family’s accounting, a man who thought a granddaughter should not carry a sword. Kiri’s answer is an odachi so large it looks like a joke until she balances it. Dance-like, fluid, precise. The five-shaku blade is compensation as argument: if the school is about economy of motion, she will spend the economy on mass and still be faster than your opinion.</p>
    <p>Uruha and Samura helped raise her. That means the two wartime Iai students are in the grandmother-adjacent slot, and both of them spent Part 1 trying to die or fake-die for reasons of guilt. Kiri is the next generation that did not commit Malediction and still has to live in the building it paid for. She is loyal enough to the Kamunabi to lead a squadron and escort Hakuri. She is not loyal to the founder’s clause. When Uruha walks again after Suzaku, she is one of the people in the HQ who still thinks a Shirakai student is worth standing next to.</p>
    <h2>Abilities</h2>
    <p>The odachi is about two meters overall, five shaku in the blade. She compensates for weight and size through balance and dance-like movement. That is not Iai as Samura does it (sheathed, blind, echolocation, fastest bearer). It is a related language spoken with a longer mouth. Iai White Purity was built for speed of draw. An odachi that long is a different clock. Kiri’s mastery is making the clock look like the same school anyway. The grandfather said she could not. The chapters show her moving through a collapsing headquarters with Hakuri, which is the exam.</p>
    <p>She is a squadron leader, peer in rank to Natsuki. Lightning Menace and a giant odachi are the Kamunabi’s two named sword acts in the long book’s HQ chapters. One is a Misaka. One is a Shirakai. Neither holds an Enchanted Blade. Both are there to keep Hakuri alive long enough to hide Magatsumi in a Storehouse. The bearers get jackets. The squadron leaders get the corridor.</p>
    <h2>Story role</h2>
    <p>She becomes essential when the Hishaku infiltrate Kamunabi headquarters. Kudo dies getting Hakuri toward Shinuchi. Kiri takes the escort onward. Yukisada, seventeen, regenerating, sitting in the barrier as a Vessel, is the lock. Hagiwara, legless, hallucinating his dead friend Kugara, is still useful. Hakuri’s Storehouse becomes the only way to remove the Kamunabi’s own vessel from a split barrier. Kiri is the swordsman in that math: not the regenerator, not the Storehouse, the person who can walk a boy through a building that Yura is eating at range with Magatsumi.</p>
    <p>Samura later dies holding the Sword Master back. Iori inherits Tobimune. Chihiro keeps Enten’s pieces. Kiri inherits nothing so clean. She inherits a grandfather in the mountains and a style she was told not to use. Part 2 will not pause the forge to resolve her vow. The vow is still the character. When the present tense returns, a Shirakai who hates Shirakai is the kind of loose blade the Kamunabi will need, especially if Akemura is wearing the agency like a coat.</p>
    <h2>Notes</h2>
    <p>Itsuo Shirakai developed Iai White Purity in pursuit of unmatched speed. He is a maverick and a bigot. The two facts share a body. Kiri is the proof that the speed does not belong to him. Iori is the proof that the speed can be given to a daughter and then erased. Chihiro is the proof that it can be stolen by watching. The school is larger than the founder. That is the only kind of inheritance this book likes.</p>
    <p>Chapter 90, “Kiri.” See also <a href="../world/iai.html">Iai White Purity</a>, <a href="uruha.html">Uruha</a>, <a href="samura.html">Samura</a>, <a href="iori.html">Iori</a>, and the <a href="../factions/kamunabi.html">Kamunabi</a> org page. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Iai White Purity", "../world/iai.html"),
        ("Kamunabi", "../factions/kamunabi.html"),
        ("Hakuri", "hakuri.html"),
        ("Uruha", "uruha.html"),
        ("Iori", "iori.html"),
    ],
)

character(
    "ibuki",
    "Ibuki Misaka",
    "巳坂 伊武基",
    "Enchanted Blade bearer · Cloud Gouger",
    "The original Cloud Gouger bearer, Samura’s equal in the war, who put the sword down afterward and was murdered by Hokuto for a contract the Hishaku wanted open.",
    "p-sojo",
    "../assets/portraits/sojo.webp",
    "The later customer. Sojo held Cloud Gouger; Ibuki was the wartime bearer Hokuto killed to make that possible.",
    [
        ("Blade", '<a href="../blades/cloud-gouger.html">Cloud Gouger</a> (Kuregumo)'),
        ("Family", '<a href="natsuki.html">Natsuki Misaka</a> (younger brother)'),
        ("War standing", "Peerless; regarded as equal to Seiichi Samura"),
        ("After the war", "Abandoned swordsmanship"),
        ("Death", "Assassinated by <a href=\"hokuto.html\">Hokuto</a> of the Hishaku, shortly after Kunishige’s murder"),
        ("Aftermath", "Contract opens; blade sold to Genichi Sojo; later bisected by Enten"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>The war</li><li>Retirement and death</li><li>What the blade became</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Ibuki Misaka was the original bearer of <a href="../blades/cloud-gouger.html">Cloud Gouger</a>, the weather sword: Mei, Yui, Kou; lightning, ice, water; clouds and cloud-dragons. During the Seitei War he was a peerless swordsman, regarded as equal in skill to <a href="samura.html">Seiichi Samura</a>. Alongside his younger brother <a href="natsuki.html">Natsuki</a>, the pair were nearly invincible. Natsuki never received an Enchanted Blade. Ibuki did. That split is the Misaka story. After the war Ibuki abandoned swordsmanship for reasons the printed chapters have not fully given. He was assassinated by <a href="hokuto.html">Hokuto</a> of the Hishaku shortly after they murdered <a href="kunishige.html">Kunishige</a>. The Lifelong Contract opened. Yura sold the blade to <a href="sojo.html">Sojo</a>. Chihiro bisected it. The public remembers the customer. The war remembers Ibuki.</p>
    <p>He is off-page for almost all of Part 1 and still inside every Cloud Gouger panel. Sojo’s cloaked Mei, Chihiro’s black Mei: Shred, the Anti-Cloud Gouger Special Forces dying around a compound, Tenri later dying on fake Datenseki: all of that is weather that used to have a different owner. Hokuto was disappointed. He wanted the wartime Ibuki and got the retired one. Natsuki wanted to stand beside that wartime Ibuki and got a jacket with Hokuto instead.</p>
    <h2>The war</h2>
    <p>Six Enchanted Blades enter at plus one year and five months. Cloud Gouger is one of them. Magatsumi is the one that lets Japan walk onto the island. Tobimune is support. Kumeyuri is banquet and play. Enten does not exist yet. Ibuki’s equal-to-Samura reputation is the book’s way of saying the weather sword was not a lesser tool. Samura is fastest, blind, Iai. Ibuki is the other ceiling. Natsuki’s Lightning Menace is a family rhyme: voltage without Datenseki, still in the body. Together the brothers were a formation. Kunishige chose one of them for a contract that would shut the innate art off. The bearer loses sorcery. The brother keeps Raiku. After the war that math looks like a curse. During the war it looked like victory.</p>
    <p>Then Malediction. Akemura uses Magatsumi after the treaty. About 200,000 civilians. The other bearers fail to stop him in the room. The Kamunabi file it as heroism. Kunishige confiscates the six swords. Ibuki, like the others who are not in a cell, has to live with a newspaper that will not print the flowers. He puts the sword down. Samura blinds himself further into religion and then into a Hishaku side deal. Uruha loses the will to live when Kunishige dies. Akemura waits in a basement. Subaru makes sushi. Ibuki’s retirement is the version of guilt that looks like a quiet house. Hokuto hates quiet houses.</p>
    <h2>Retirement and death</h2>
    <p>Three Hishaku hit the Rokuhira workshop. Kunishige dies. The six wartime blades are stolen. In the same campaign Hokuto kills Ibuki. The order of operations is the method: steal the steel, kill the bearer if the contract still holds, sell what you cannot yet sign. Cloud Gouger goes to Sojo in early October of the present, a customer who wants to industrialize Kunishige’s eyes using Kyonagi flesh. Ibuki is already a grave. Char is the next stabilizer on the list. Chihiro is the son who still has Enten. The Anti-Cloud Gouger Special Forces are the state’s apology for not protecting the original bearer: six people built to solve the sword after the man was gone. Four die. Hagiwara loses his legs. Kazane loses an arm. Chihiro loses an arm and still reaches True Realm first. Enten cuts Cloud Gouger in half. Sojo fuses with Datenseki. The compound goes. Ibuki’s blade is shown to be mortal in someone else’s hand.</p>
    <p>Natsuki keeps training. He wanted Kumeyuri; Uruha was chosen. He wants recognition beside his brother and the other bearers. He wants Hokuto. Volume 10 puts all of that on one jacket. Ibuki is the missing face. The title is <em>The Swordsmen</em>. The dead swordsman is the reason the title has a body count.</p>
    <h2>What the blade became</h2>
    <p>Sojo finds cloaked Mei, wearing the lightning instead of throwing it. True Realm, for him, is slaughter, because that is his brief. Chihiro later contracts the dying stump and spends Mei: Shred, black because the blade is dying, the same dark-power rule that paints Suzaku. Residual charges at the Rakuzaichi, then disintegration. Chihiro keeps pieces. By the end of Part 1 his notes include a new Cloud Gouger as well as a new Enten. The original bearer’s sword, in the son’s ledger, is something you might forge again rather than something you avenge by finding Hokuto. Natsuki is still in the building for the second half of that sentence.</p>
    <p>Cloud Gouger’s technique list (Mei, Yui, Kou, extensions) lives on the <a href="../blades/cloud-gouger.html">blade page</a>. This page is the person the list used to belong to. Do not credit Sojo with inventing weather. Credit him with being the worst reader of a sword that already had a master, and credit Hokuto with the murder that made the misreading possible.</p>
    <h2>Notes</h2>
    <p>He is not given a long present-tense arc. He is given a brother, a killer, a customer, a bisection, and a reputation equal to Samura. That is enough for a file. When Part 2’s forge chapters show Kunishige cutting the first wartime steel, Ibuki is not yet chosen. The talks are still talks. The princess is still Chiaki. Fire is still a process. The man who will be Cloud Gouger’s first partner is still, in that past, a swordsman with a brother. The book has not printed that day. This archive will not invent it.</p>
    <p>See <a href="natsuki.html">Natsuki</a>, <a href="hokuto.html">Hokuto</a>, <a href="sojo.html">Sojo</a>, and <a href="../blades/cloud-gouger.html">Cloud Gouger</a>. Official chapters: VIZ / MANGA Plus.</p>
    """,
    [
        ("Cloud Gouger", "../blades/cloud-gouger.html"),
        ("Natsuki Misaka", "natsuki.html"),
        ("Hokuto", "hokuto.html"),
        ("Sojo", "sojo.html"),
        ("Samura", "samura.html"),
    ],
)

print("character pages done")
