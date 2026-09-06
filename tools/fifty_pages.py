#!/usr/bin/env python3
"""Write 50 encyclopedia pages on subjects this site never gave a room."""
from pathlib import Path

ROOT = Path("/workspace")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
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
        + f"  <h1>{h1}<span class=\"jp\">{jp}</span></h1>\n"
        + f'  <p class="lede">{lede}</p>\n</div></header>\n'
        + f'<article class="article">\n{body}\n</article>\n'
        + FOOT
    )
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


PAGES = []


def add(rel, title, desc, crumb, kicker, h1, jp, lede, body):
    PAGES.append((rel, title, desc))
    write(rel, title, desc, crumb, kicker, h1, jp, lede, body)


# --- Characters who only had a register line ---

add(
    "characters/harima.html",
    "Shiyumi Harima",
    "Shiyumi Harima of the Anti-Cloud Gouger Special Forces: Gansui stone, the airborne field, and a grave the ACG page used to leave as a roster line.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Harima',
    "ACG · Gansui",
    "Shiyumi Harima",
    "張間 梓弓",
    "Stone as a battlefield. Kazane as a reserve. A head wound that drops the islands into the sea.",
    """
  <p>Shiyumi Harima (張間 梓弓) is one of the six Anti-Cloud Gouger Special Forces. Her art is Gansui (岩垂): she lifts and shapes stone. At the bathhouse fight she pulls the ground into the air so the squad can fight Sojo over the ocean instead of a city. Kazane stays beside her as the unused secret weapon. The other four press Sojo. She holds the floor.</p>
  <h2>What the stone is for</h2>
  <p>The ACG page on this site used to name her in a line and move on. The fandom wiki and the Vs. Sojo recaps treat Gansui as logistics: civilian streets stay intact because the fight is a set of floating platforms. When Sojo cloaks Mei and comes back for the reserve, he cuts a large section of her head and shoulder. The platforms fall. She is confirmed dead after the battle. Four graves among six. Chihiro is in Kaburato Castle while this happens. Official chapters: VIZ / MANGA Plus.</p>
  <p>She is not Hiyuki. Flame Bone is a national pointed end. Gansui is a specialist’s kit for one sword. Recaps that say “the Kamunabi fought Sojo” without the woman holding the islands are skipping the reason the civilians in that stretch live. Unit: <a href="../world/acg.html">Anti-Cloud Gouger</a>. Commander: <a href="hagiwara.html">Hagiwara</a>. The fight: <a href="../arcs/vs-sojo.html">Vs. Sojo</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="uzuki.html">Uzuki</a><a href="kasahara.html">Kasahara</a><a href="../world/acg.html">ACG</a><a href="kazane.html">Kazane</a><a href="../world/bathhouse.html">Bathhouse</a><a href="index.html">Characters</a></nav>
""",
)

add(
    "characters/uzuki.html",
    "Kiyohiko Uzuki",
    "Kiyohiko Uzuki of the Anti-Cloud Gouger Special Forces: binding spells, the poles next to Sojo, and a grave the roster used to skip.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Uzuki',
    "ACG · binding",
    "Kiyohiko Uzuki",
    "卯月 清彦",
    "Restrict the weather. Then the weather comes back wearing lightning.",
    """
  <p>Kiyohiko Uzuki (卯月 清彦) is Anti-Cloud Gouger. Binding spells: restrict a target’s movement. At the hospital he is the one who notices Chihiro’s fight produced zero civilian injuries. At the bathhouse he throws short poles that land beside Sojo so the bind can sit on a point, then goes in with Kasahara, Kugara, and Hagiwara while Harima holds the stone aloft.</p>
  <h2>The bind that does not hold</h2>
  <p>The plan is restrain, magnetize, launch Sojo off the island, take Cloud Gouger. Sojo remotely spends a cloaked Mei and returns. Uzuki dies in that return. Binding is a learned art, not an Enchanted Blade. It is enough for hired weather. It is not enough for a fan who has found True Realm as slaughter. This page exists because the register and the ACG file used to leave him as three words. File the unit: <a href="../world/acg.html">ACG</a>. File the sword: <a href="../blades/cloud-gouger.html">Cloud Gouger</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="harima.html">Harima</a><a href="kasahara.html">Kasahara</a><a href="../world/acg.html">ACG</a><a href="sojo.html">Sojo</a><a href="../world/bathhouse.html">Bathhouse</a><a href="index.html">Characters</a></nav>
""",
)

add(
    "characters/kasahara.html",
    "Makoto Kasahara",
    "Makoto Kasahara of the Anti-Cloud Gouger Special Forces: enlarged hands, the search for Sojo’s base, and the smash that does not land.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Kasahara',
    "ACG · hands",
    "Makoto Kasahara",
    "笠原 誠",
    "The sixth member. Busy hunting a castle. Then a smash from above that Sojo walks around.",
    """
  <p>Makoto Kasahara (笠原 誠) is the ACG member Chihiro asks about in the hospital. Harima says he is busy searching for Sojo’s base. His art enlarges his hands. At the bathhouse he is the smash from above: a giant arm coming down while Uzuki binds and Hagiwara magnetizes. Sojo dodges. The plan still almost works. Then cloaked Mei comes home.</p>
  <h2>Why the sixth matters</h2>
  <p>Six people, one sword. The roster is incomplete if you only keep the commander, the childhood friend, and the unused secret. Kasahara is the searcher and the weight. He dies of the injuries Sojo leaves. Kaburato Castle is the house Chihiro walks into while this squad dies over the water. Pages: <a href="../world/kaburato.html">Kaburato</a>, <a href="../world/acg.html">ACG</a>, <a href="harima.html">Harima</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="harima.html">Harima</a><a href="uzuki.html">Uzuki</a><a href="../world/acg.html">ACG</a><a href="../world/kaburato.html">Kaburato</a><a href="hagiwara.html">Hagiwara</a><a href="index.html">Characters</a></nav>
""",
)

add(
    "characters/inazuma.html",
    "Yuu Inazuma",
    "Yuu Inazuma, Mr. Inazuma: the child who tries to break into the Rakuzaichi to free his sister, and the chapter that titles itself after him.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Inazuma',
    "Chapter 27",
    "Yuu Inazuma",
    "稲妻 裕",
    "A child who calls himself Mr. Inazuma. A sister inside the auction. Chihiro as the door that actually opens.",
    """
  <p>Yuu Inazuma (稲妻 裕) introduces himself as Mr. Inazuma. He is a child trying to break into the 208th Rakuzaichi to get his older sister out. Chapter 27 is titled for him. Chihiro meets the attempt, not a mascot. The auction is a building that warehouses people. Yuu is the civilian sentence of that fact: someone outside the clan still treats a listing as a person.</p>
  <h2>After the building falls</h2>
  <p>Chihiro gets the sister and the other hostages out of the Storehouse before Kyora and Magatsumi finish the firm. Yuu is reunited. The register used to give him one clause. The fandom wiki and the volume 3 synopsis keep him because the auction’s victims are the reason Hakuri’s inheritance is logistics instead of a trophy. See <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>, <a href="../world/storehouse.html">Storehouse</a>, <a href="hakuri.html">Hakuri</a>. Official chapters: VIZ / MANGA Plus.</p>
    <nav class="related" aria-label="Related pages"><a href="hakuri.html">Hakuri</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a><a href="../world/storehouse.html">Storehouse</a><a href="chihiro.html">Chihiro</a><a href="../world/register.html">Register</a><a href="index.html">Characters</a></nav>
""",
)

add(
    "characters/ukizane.html",
    "Ukizane Soga",
    "Ukizane Soga: the historical Soga who nearly destroyed the Mikaboshi and forced the undersea habitat, a name this encyclopedia never gave a page.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Ukizane',
    "Soga history",
    "Ukizane Soga",
    "曽我",
    "A mainland prophet house that almost finished the old kings. The sea is what was left.",
    """
  <p>Ukizane Soga is a historical name, not a present-tense fighter. The printed chapters say he nearly destroyed the Mikaboshi before they hid under the sea. The Mikaboshi king answered by building an enormous branched sphere in the deep, Datenseki as architecture, so the clan could live with the ore instead of dying to it. Irishima’s later earthquake and Shokoku’s rise are those kings coming back for a vein the Soga once tried to end.</p>
  <h2>Why the name is not Chiaki</h2>
  <p>Chiaki is Princess Soga in the talks. Hiroto, Yoshinojo, and Giyu are the war-generation house. Ukizane is the reason the undersea page exists: a Soga success so complete it created a nation that could wait a thousand years. We do not invent his face, art, or century beyond what the chapters and the public wiki summary already print. Habitat: <a href="../world/undersea.html">undersea Mikaboshi</a>. Clan: <a href="../factions/soga.html">Soga and Mikaboshi</a>. Island: <a href="../world/irishima.html">Irishima</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/undersea.html">Undersea habitat</a><a href="../factions/soga.html">Soga</a><a href="../world/shokoku.html">Shokoku</a><a href="chiaki.html">Chiaki</a><a href="ariu.html">Ariu</a><a href="index.html">Characters</a></nav>
""",
)

add(
    "characters/shigyu.html",
    "The Shigyu Brothers",
    "The Shigyu brothers: Hishaku-hired chaos at Kamunabi headquarters, eleven dead, Azami’s two-cut answer.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Characters</a> / Shigyu',
    "HQ hirelings",
    "The Shigyu Brothers",
    "死柳兄弟",
    "Ordinary origins. Eleven Kamunabi dead. Azami does not keep them as a plot.",
    """
  <p>The Shigyu brothers (死柳兄弟) are two sorcerers the Hishaku hire to hit Kamunabi headquarters. They join to wreck, not to hold a blade. Despite ordinary origins they kill eleven Kamunabi personnel, then reach Level 1’s underground core with a Hishaku member. Azami meets them there and kills both.</p>
  <h2>Hirelings are not the ten</h2>
  <p>Pine-sorcery crews at Senkutsuji, Datenseki troops at Kokugoku, the Shigyu at HQ: the ten buy weather. The brothers are the HQ version of that sentence. Recaps that fold them into “the Hishaku attack” lose the fact that Yura’s method includes people who are not flame tattoos. Azami’s Coin is the clinic art rewritten as execution; this is one of the executions. Place: <a href="../world/hq.html">headquarters</a>. Head: <a href="azami.html">Azami</a>. Org: <a href="../factions/hishaku.html">Hishaku</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/hq.html">Headquarters</a><a href="azami.html">Azami</a><a href="../factions/hishaku.html">Hishaku</a><a href="../world/core-station.html">Core Station</a><a href="../world/register.html">Register</a><a href="index.html">Characters</a></nav>
""",
)

# --- Locations ---

add(
    "world/naginojoen.html",
    "Naginojoen",
    "Naginojoen, the Sazanami ancestral graveyard under the Rakuzaichi: the ceremony room, the emergency door, and the seal Shiba cannot teleport through.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Naginojoen',
    "Sazanami cemetery",
    "Naginojoen",
    "凪浄苑",
    "A graveyard that is also a door. Leadership of the clan is a ceremony in a sealed room.",
    """
  <p>Naginojoen (凪浄苑) is the Sazanami ancestral graveyard on the bottom floor of the auction house. Clan leadership, and therefore ownership of the Storehouse, passes here. The Emergency Access Door’s real-world counterpart sits in a sealed room inside it. Shiba cannot teleport into the Naginojoen. The Tou guard the hallway. That is why the 208th infiltration is a walk, not an extraction.</p>
  <h2>Cemetery as architecture</h2>
  <p>Chihiro finds a door in the Storehouse and reads it as a twin. The twin is here. Hakuri lures Soya away. Shiba beats the remaining Tou and tells them to go home and raise the younger members. The trio enter to find the emergency door already destroyed. Kyora has already spent the insurance. The Storehouse page is the subspace. This page is the grave that holds the spare key. See <a href="storehouse.html">Storehouse</a>, <a href="emergency-door.html">emergency door</a>, <a href="../factions/tou.html">the Tou</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="storehouse.html">Storehouse</a><a href="emergency-door.html">Emergency door</a><a href="../factions/tou.html">The Tou</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a><a href="registration.html">Registration</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/senkutsuji.html",
    "Senkutsuji Temple",
    "Senkutsuji Temple: Samura’s Sanso, the Masumi, Tobimune’s return, and the surgery that looks like a Hishaku pact.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Senkutsuji',
    "Temple · Sanso",
    "Senkutsuji",
    "仙屈寺",
    "A Buddhist room used as a vault, then as a surgery. Owl launches from here later.",
    """
  <p>Senkutsuji is the temple where the Kamunabi put Seiichi Samura after the raid. The Masumi (Ro, Moku, Sumi) serve him there. Hakuri and Uruha arrive by Sumi’s marker mandala from a train station. Pine-sorcery hirelings hit the grounds. Hakuri puts Tobimune back in Samura’s hand. Samura clears the temple. Then he cuts Uruha down. It looks like the Hishaku pact. It is Suzaku: kill the contract, keep the man.</p>
  <h2>Vault, then launch site</h2>
  <p>Locations.html gave this temple a paragraph. The fandom wiki and the Sword Bearer recaps treat it as the week the boxes fail in public. Samura later spends Owl nationwide from the same story-week. Chihiro dies here and is pulled back. The Masumi are freed. Iori becomes the next problem because a temple that was a vault is now a rumor the ten can use. Fortress type: <a href="sanso.html">Sanso</a>. Style: <a href="iai.html">Iai</a>. Arc: <a href="../arcs/sword-bearer.html">Sword Bearer Assassination</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/samura.html">Samura</a><a href="../factions/masumi.html">Masumi</a><a href="sanso.html">Sanso</a><a href="../blades/tobimune.html">Tobimune</a><a href="../arcs/sword-bearer.html">Sword Bearer</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/kokugoku.html",
    "Kokugoku Hot Spring Sanso",
    "Kokugoku Hot Spring Sanso: Uruha’s box, the Steam Squad, Datenseki troops, and the week Hiruhiko makes a scene.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Kokugoku',
    "Hot spring · Sanso",
    "Kokugoku",
    "国獄",
    "A fortress that is also a bath. Chapter 48 titles the squad. The squad dies the same week.",
    """
  <p>Kokugoku Hot Spring Sanso is the Kamunabi box around Yoji Uruha after the raid. The Kokugoku Steam Squad guards it. Hishaku-hired Datenseki troops hit first. The squad beats them. Then Hiruhiko arrives. Blood Crane, mercenaries, a train, a kabuki house. The Steam Squad dies. Chapter 48 is titled for them. Uruha is already being moved when the box’s purpose ends.</p>
  <h2>Why a hot spring</h2>
  <p>Sanso are boxes. This one is a spring because the state still pretends a bearer can live somewhere that looks like rest. Fushimi’s Smoke Axe is the named art that proves the first wave was real. Hiruhiko is the member Yura sends when money is not enough. Chihiro fights him so Hakuri can put Uruha on a train toward Senkutsuji. Pages: <a href="../factions/steam-squad.html">Steam Squad</a>, <a href="../characters/fushimi.html">Fushimi</a>, <a href="sanso.html">Sanso</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../factions/steam-squad.html">Steam Squad</a><a href="../characters/uruha.html">Uruha</a><a href="../characters/hiruhiko.html">Hiruhiko</a><a href="sanso.html">Sanso</a><a href="senkutsuji.html">Senkutsuji</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/hq.html",
    "Kamunabi Headquarters",
    "Kamunabi headquarters in Tokyo: Magatsumi in the basement, Yukisada in the barrier, Kudo’s death, and the building that loses the Sword Master.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Headquarters',
    "Tokyo · Level 1",
    "Kamunabi Headquarters",
    "神奈備本部",
    "The building that hid a war crime as a basement, then offered the body that walked him out.",
    """
  <p>Kamunabi headquarters is in Tokyo. Magatsumi sits sealed in the basement after the 208th. Kasen’s leak is policy in the same building. When the Hishaku come, Yukisada splits the barrier as Vessel. The Shigyu kill eleven on the way to the core. Kudo spends Warrior’s Path so Hakuri can reach Shinuchi, then dies. Hakuri parks the Kamunabi vessel in his Storehouse so communications can return. Shiba dumps Yura onto the street.</p>
  <h2>The cell is the setting</h2>
  <p><span class="spoiler">Yura offers a body. Akemura leaves the cell. The building that hid the Sword Master is the building that loses him. Samura and Chihiro meet that fact on the street, not in the basement.</span> Locations.html gave HQ a paragraph. This page is the architecture: barrier, core, cell, street. See <a href="barriers.html">barriers</a>, <a href="core-station.html">Core Station</a>, <a href="../factions/white-robes.html">White Robes</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="barriers.html">Barriers</a><a href="../characters/yukisada.html">Yukisada</a><a href="../characters/kudo.html">Kudo</a><a href="../factions/kamunabi.html">Kamunabi</a><a href="core-station.html">Core Station</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/kaburato.html",
    "Kaburato Castle",
    "Kaburato Castle, Sojo’s stronghold: Char in the courtyard, the Datenseki briefcase, and the last Enten versus Cloud Gouger.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Kaburato',
    "Sojo’s house",
    "Kaburato Castle",
    "かぶらと",
    "The compound the ACG die to keep Chihiro inside of. A courtyard, a briefcase, a roar.",
    """
  <p>Kaburato Castle is Sojo’s stronghold in the Vs. Sojo week. The fandom wiki and the chapter recaps use the castle name; this site used to say “compound.” Chihiro infiltrates to pull Char while the Anti-Cloud Gouger Special Forces meet Sojo at a bathhouse. Sojo comes home with a briefcase of semi-stabilized Datenseki the yakuza returned. He finds Chihiro in the courtyard. The last duel is here. Enten bisects Cloud Gouger. Sojo spends the ore. The house goes with him.</p>
  <h2>Castle, not myth</h2>
  <p>It is a crime boss’s house with a research hunger, not a wartime Sanso. Korogumi muscle and Madoka’s employment sit on the same street. Char’s regeneration is the stabilizer hunt that made the castle a lab. After Roar, residual Cloud Gouger charges wait for the Rakuzaichi. The castle does not. See <a href="../arcs/vs-sojo.html">Vs. Sojo</a>, <a href="../characters/sojo.html">Sojo</a>, <a href="../factions/korogumi.html">Korogumi</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/sojo.html">Sojo</a><a href="../characters/char.html">Char</a><a href="../world/acg.html">ACG</a><a href="../arcs/vs-sojo.html">Vs. Sojo</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/shokoku.html",
    "Shokoku",
    "Shokoku, the island nation that rises from the sea: Mikaboshi return, Irishima’s vein, overthrow, treaty, then Malediction.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Shokoku',
    "The risen nation",
    "Shokoku",
    "渚国",
    "An island that should have stayed under the sea. English rooms called the splash Japan’s Atlantis.",
    """
  <p>Shokoku is the island nation that appears about twenty-two years before the present tense. The Mikaboshi come back with Datenseki-adapted bodies. Irishima already showed a vein; Japan harvests it. The Sorcery Bureau becomes an army. Talks fail. The Seitei War is the name of that failure. Enchanted Blades enter at one year and five months and reverse the front. Shokoku overthrows its royals and signs a peace. Akemura voids the peace with flowers: Malediction, about 200,000 civilians.</p>
  <h2>Island, nation, crime</h2>
  <p>Irishima is the vein and the talks. Shokoku is the political body that rose, fought, surrendered, and then was slaughtered after the treaty. YouTube rooms nicknamed chapter 113 “Japan’s Atlantis.” This page keeps the nation name so the island page can stay a mineral. See <a href="irishima.html">Irishima</a>, <a href="../arcs/seitei-war.html">Seitei War</a>, <a href="../analysis/malediction.html">Malediction</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="irishima.html">Irishima</a><a href="undersea.html">Undersea habitat</a><a href="../factions/soga.html">Soga and Mikaboshi</a><a href="../arcs/seitei-war.html">Seitei War</a><a href="../analysis/irishima.html">Vein essay</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/undersea.html",
    "Mikaboshi Undersea Habitat",
    "The Mikaboshi undersea habitat: a branched sphere built from Datenseki after Ukizane nearly ended the old kings.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Undersea habitat',
    "Below the sea",
    "Undersea habitat",
    "海底",
    "A nation that learned to live inside the ore because the mainland almost finished them.",
    """
  <p>After Ukizane Soga nearly destroyed the Mikaboshi, their king used Datenseki to build an enormous spherical habitat deep under the ocean, crafted from immense branches. The clan and the people who went with them adapted their bodies to the unstable mineral. That is why raw Datenseki does not pop them the way it pops a mainland user. Shokoku rising is that habitat deciding the wait is over.</p>
  <h2>Not a second Irishima</h2>
  <p>Irishima is the vein Japan already found. The habitat is the thousand-year answer to a Soga purge. Hasumi’s later lab notes that vitality alone should not let a body survive the ore’s crush; the printed research still treats the adaptation as the mystery. Ariu’s Datenseki-hardened flesh is the prince version of the same homework. See <a href="../characters/ukizane.html">Ukizane</a>, <a href="shokoku.html">Shokoku</a>, <a href="../characters/ariu.html">Ariu</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/ukizane.html">Ukizane</a><a href="shokoku.html">Shokoku</a><a href="irishima.html">Irishima</a><a href="datenseki.html">Datenseki</a><a href="../factions/soga.html">Soga</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/bathhouse.html",
    "The Bathhouse Fight",
    "The bathhouse fight against Sojo: airborne stone, binding poles, cloaked Mei, and the ACG graves the castle duel is timed against.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Bathhouse fight',
    "Vs. Sojo · place",
    "The bathhouse fight",
    "銭湯",
    "Sojo leaves a tub. Six specialists are waiting. Four of them do not come back.",
    """
  <p>The Anti-Cloud Gouger Special Forces meet Sojo as he exits a bathhouse, more than forty-nine hours after the hospital stretch. Harima lifts the ground into the air and walks the platforms toward the ocean so civilians stay out of the weather. Uzuki binds. Kasahara smashes. Hagiwara magnetizes. Kugara is iron. Kazane is told to wait as the secret weapon. The plan almost puts Cloud Gouger in their hands.</p>
  <h2>Why this is not Kaburato</h2>
  <p>Chihiro is in the castle pulling Char. The bathhouse is the state’s matching piece, timed to empty the house. Cloaked Mei lets Sojo spend lightning without holding the hilt. He comes back, takes Kazane’s arm, wrecks Harima’s head, and finishes the rest. Two survivors. The last duel is a courtyard; this page is the water the courtyard is bought with. See <a href="acg.html">ACG</a>, <a href="kaburato.html">Kaburato</a>, <a href="../fun/oneshots.html">bathhouse extras</a> (a different tub, later, as a gag).</p>
    <nav class="related" aria-label="Related pages"><a href="acg.html">ACG</a><a href="../characters/harima.html">Harima</a><a href="kaburato.html">Kaburato</a><a href="../arcs/vs-sojo.html">Vs. Sojo</a><a href="../characters/sojo.html">Sojo</a><a href="index.html">World</a></nav>
""",
)

# --- Factions ---

add(
    "factions/tou.html",
    "The Tou",
    "The Tou, Sazanami Special Defense Corps: Soya, Tenri, Tamaki, Enji, the household military of the 208th Rakuzaichi.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / The Tou',
    "Household military",
    "The Tou",
    "濤",
    "Four best fighters. A father’s commands. An auction that treats children as stock and calls that a defense.",
    """
  <p>The Tou (濤), also printed as the Special Defense Corps, are the four best fighters in the Sazanami clan: Soya, Tenri, Tamaki, and Enji. They follow the head and protect the Rakuzaichi. Three of them meet Chihiro and Shiba in the estate. Tamaki lies about Soya’s whereabouts. Tenri later spends unstable Datenseki to impress Kyora and dies. Enji asks Shiba for death and is told to raise what is left. Soya loses to Hakuri’s dual inheritance, then crawls out of the rubble with amnesia and the same hunger.</p>
  <h2>Not the Storehouse</h2>
  <p>The Sazanami page already had the household. This page is the military job: a hallway at Naginojoen, a pine-sorcery barrier, short blades, a brother’s obsession. Hakuri is the error that ends the firm, not a fifth Tou. See <a href="sazanami.html">Sazanami</a>, <a href="../world/naginojoen.html">Naginojoen</a>, <a href="../characters/tenri.html">Tenri</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="sazanami.html">Sazanami</a><a href="../characters/soya.html">Soya</a><a href="../characters/tenri.html">Tenri</a><a href="../world/naginojoen.html">Naginojoen</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a><a href="index.html">Factions</a></nav>
""",
)

add(
    "factions/korogumi.html",
    "The Korogumi",
    "The Korogumi yakuza: Hishaku-allied muscle on the Tokyo street, Datenseki errands, and the neighborhood the ten can walk through.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / Korogumi',
    "Underworld firm",
    "The Korogumi",
    "転組",
    "Ordinary crime next to flame tattoos. The briefcase that comes back to Kaburato is their kind of job.",
    """
  <p>The Korogumi are yakuza allied with the Hishaku. This encyclopedia’s underworld page named them in a sentence and moved on to Cafe Haru Haru. The fandom wiki lists them as an organization beside Kamunabi, Hishaku, and Sazanami. They are not the ten. They are the neighborhood the ten can walk through: errands, muscle, a Datenseki briefcase returned to Sojo’s courtyard.</p>
  <h2>Scale</h2>
  <p>Civilian sorcerers take small jobs. Hinao brokers yakuza and corporations at the cafe. The Korogumi are the named firm on that street. Enchanted Blades sit next to ordinary sorcery the way flame-gate sits next to a gang office. Recaps that say “Sojo’s men” without a firm lose the city’s actual map. See <a href="../world/underworld.html">underworld</a>, <a href="../world/civilian.html">civilian sorcerers</a>, <a href="hishaku.html">Hishaku</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="hishaku.html">Hishaku</a><a href="../world/underworld.html">Underworld</a><a href="../world/kaburato.html">Kaburato</a><a href="../world/cafe.html">Cafe Haru Haru</a><a href="../characters/sojo.html">Sojo</a><a href="index.html">Factions</a></nav>
""",
)

add(
    "factions/steam-squad.html",
    "Kokugoku Steam Squad",
    "The Kokugoku Steam Squad: Uruha’s Sanso guard, Smoke Axe, a win against Datenseki troops, then Hiruhiko.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / Steam Squad',
    "Chapter 48",
    "Kokugoku Steam Squad",
    "国獄湯煙スクワッド",
    "Named in a title. Buried in the same week. The first wave was not the problem.",
    """
  <p>The Kokugoku Steam Squad is the Kamunabi guard on Uruha’s hot-spring Sanso. Fushimi is the named specialist: Smoke Axe, cuts with smoke between the hands, bandana. They beat Hishaku-hired Datenseki troops. Hiruhiko is the second wave. The squad dies. Chapter 48 is titled for them. That is how the bureau spends specialists: a name, a win, a grave.</p>
  <h2>Not the ACG</h2>
  <p>Anti-Cloud Gouger was six people for one sword in the first book. The Steam Squad is the second book’s matching piece for one box. Recaps that say “Hiruhiko attacked a fortress” without the squad skip the people who already won once that week. Place: <a href="../world/kokugoku.html">Kokugoku</a>. Face: <a href="../characters/fushimi.html">Fushimi</a>. Other specialist graves: <a href="../world/acg.html">ACG</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/kokugoku.html">Kokugoku</a><a href="../characters/fushimi.html">Fushimi</a><a href="../characters/hiruhiko.html">Hiruhiko</a><a href="../world/acg.html">ACG</a><a href="kamunabi.html">Kamunabi</a><a href="index.html">Factions</a></nav>
""",
)

add(
    "factions/bureau.html",
    "The Sorcery Bureau",
    "The Sorcery Bureau before it is the Kamunabi: Hasumi’s lab, Shiba and Mashiro, stolen Datenseki, and a ceasefire that resigns a chief.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / Sorcery Bureau',
    "Before the rename",
    "Sorcery Bureau",
    "魔術局",
    "A government desk that becomes an army. Part 2 is before the rename has finished meaning anything.",
    """
  <p>The Sorcery Bureau (魔術局) is the government sorcery desk that exists before the Seitei War. It is restructured into the Counter-Sorcery Army, then into the Kamunabi. Shinsaku Hasumi runs a secret Datenseki laboratory. Shiba and Mashiro work under that roof. Joji is ranked above them and annoyed. Shiba believes Kunishige’s eyes are the only way to make the mineral usable. He is right. Hasumi comes to trust the smith, then resigns after letting Shiba steal ore, disillusioned when the bureau accepts Mikaboshi ceasefire terms that include a princess on a beach.</p>
  <h2>Why this is not the Kamunabi page</h2>
  <p>The Kamunabi page is the present-tense state. This page is the desk that still thinks Datenseki is a research problem and Chiaki is a diplomatic object. Mashiro dies later to Ariu; in the talks he is still alive and opposed to taking stolen ore to a friend. See <a href="../characters/hasumi.html">Hasumi</a>, <a href="../characters/mashiro.html">Mashiro</a>, <a href="kamunabi.html">Kamunabi</a>, <a href="../world/princess.html">Princess Soga</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="kamunabi.html">Kamunabi</a><a href="../characters/hasumi.html">Hasumi</a><a href="../characters/mashiro.html">Mashiro</a><a href="../characters/joji.html">Joji</a><a href="../world/smelting.html">Smelting</a><a href="index.html">Factions</a></nav>
""",
)

add(
    "factions/white-robes.html",
    "The White Robes",
    "The Kamunabi White Robes: Kasen, Ichiki, and Yatsuru, the seal on Shinuchi and the leadership table’s learned arts.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / White Robes',
    "Three seals",
    "White Robes",
    "白衣",
    "Director, teacher, barrier. The three who locked Magatsumi and then sat on the same leak.",
    """
  <p>White Robes, on this site’s register, are Kasen, Ichiki, and Yatsuru: the leadership trio who sealed Shinuchi after the war. Kasen is director, barriers, later the leak. Ichiki is elderly, small, trained Shiba and Azami, helped hide Kunishige. Yatsuru is the sole woman among named heads, barriers and sealing, the stolen field. They are learned arts as an office, not a clan.</p>
  <h2>A robe is not a conscience</h2>
  <p>Azami, Izaru, and Kudo sit at the same table and are not called White Robes in the register. The robe names the seal job. The leak is the same job rotting. Ichiki’s training of Shiba is why teleportation still has a teacher in the building. Yatsuru’s barriers are why Yukisada’s Vessel is a theft of a room they built. See <a href="../characters/kasen.html">Kasen</a>, <a href="../characters/ichiki.html">Ichiki</a>, <a href="../characters/yatsuru.html">Yatsuru</a>, <a href="../analysis/leak.html">the leak essay</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/kasen.html">Kasen</a><a href="../characters/ichiki.html">Ichiki</a><a href="../characters/yatsuru.html">Yatsuru</a><a href="kamunabi.html">Kamunabi</a><a href="../world/hq.html">Headquarters</a><a href="index.html">Factions</a></nav>
""",
)

add(
    "factions/kyonagi.html",
    "The Kyonagi Clan",
    "The Kyonagi clan: regenerative blood, Char as the last, her hunted mother, and Sojo’s stabilizer thesis.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Factions</a> / Kyonagi',
    "Last of the line",
    "Kyonagi",
    "鏡凪",
    "A clan hunted for a body that closes wounds. Sojo wanted a battery. Chihiro wanted a meal and a door.",
    """
  <p>The Kyonagi (鏡凪) are a regenerative clan. Char is the last. She can close her own wounds and other people’s. Sojo kidnaps her and her mother to test whether that healing can stabilize Datenseki. The mother is hunted with her and is not given a separate file on this site; the chapters do not hand us a standalone biography. Char ends up at Cafe Haru Haru, then in Kaburato, then out.</p>
  <h2>Not a blade contract</h2>
  <p>Kyonagi regeneration is innate, not a Lifelong Contract. That is why Sojo treats Char as ore homework instead of a bearer. Lineage.html mentioned the house. This page is the hunt: a clan as a stabilizer thesis, a child as the last sample, a cafe as the civilian door that keeps her. See <a href="../characters/char.html">Char</a>, <a href="../world/datenseki.html">Datenseki</a>, <a href="../characters/sojo.html">Sojo</a>. Birthday on file: 21 December. We do not invent her age.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/char.html">Char</a><a href="../world/lineage.html">Lineage</a><a href="../characters/sojo.html">Sojo</a><a href="../world/cafe.html">Cafe Haru Haru</a><a href="../world/kaburato.html">Kaburato</a><a href="index.html">Factions</a></nav>
""",
)

# --- Systems ---

add(
    "world/spirit-energy.html",
    "Spirit Energy",
    "Spirit energy (Genryoku) in Kagurabachi: the life-force every person has, the training that steers it, and why Enchanted Blades overfill it.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Spirit energy',
    "Genryoku",
    "Spirit energy",
    "玄力",
    "The YouTube power-system videos start here. The book starts with a bowl. Both are talking about the same overflow.",
    """
  <p>Spirit energy (玄力, Genryoku) sits in every person. The fandom wiki and the “power system explained” tapes treat it as the resource: train the nerves, raise capacity, reinforce the body, then spend a sorcery. Enchanted Blades are the overflow case. They amplify spirit until it cannot stay inside the skin and has to become a shape: goldfish, clouds, flowers, feathers. Sorcery.html on this site is the practice. This page is the fuel those videos kept asking for.</p>
  <h2>Limits the chapters actually print</h2>
  <p>Damage to the neural pathways that govern spirit energy can shut the art down. Sealed rope can stop reinforcement and spells. Some rooms, Naginojoen among them, are warded against a type of sorcery; Shiba’s teleport stops at the cemetery door. Hakuri scattered his own spirit into a private Storehouse without knowing, which is why Isou misfired until he took the energy back. Datenseki without Kunishige’s eyes returns the amplified current as a crater. See <a href="sorcery.html">sorcery</a>, <a href="veins.html">veins in steel</a>, <a href="../analysis/true-realm.html">True Realm</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="sorcery.html">Sorcery</a><a href="innate.html">Innate arts</a><a href="datenseki.html">Datenseki</a><a href="../fun/youtube.html">YouTube room</a><a href="techniques.html">Techniques</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/dark-power.html",
    "Dark Power",
    "Dark power (Kuroi chikara) in Kagurabachi: black output at the edge of death, Mei Shred, Suzaku’s black flames, Magatsumi’s diet.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Dark power',
    "Kuroi chikara",
    "Dark power",
    "黒い力",
    "The color goes black. The output jumps. The catalog named it in a paragraph. The Sunday threads kept asking for a page.",
    """
  <p>Dark power (Kuroi chikara) is what the technique catalog calls the lock at the edge of death, or when the blade itself is dying. The color goes black. The output jumps. Chihiro’s Mei: Shred is black lightning on a dying Cloud Gouger. Samura’s Suzaku turns black when he spends his life; those flames stall Magatsumi’s wide drain long enough for Chihiro to leave. Magatsumi’s ordinary darkness is vitality as a diet, not a special mode.</p>
  <h2>Not a transformation gauge</h2>
  <p>True Realm is intent locking with steel. Dark power is that lock spent when the body or the sword is already ending. Reddit and YouTube recaps collapse the two. The chapters keep them next to each other: Honryō is the brief, black is the cost. We do not invent a third wartime blade’s black form. See <a href="../analysis/true-realm.html">True Realm</a>, <a href="techniques.html">catalog</a>, <a href="../blades/tobimune.html">Tobimune</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../analysis/true-realm.html">True Realm</a><a href="techniques.html">Techniques</a><a href="../blades/cloud-gouger.html">Cloud Gouger</a><a href="../blades/tobimune.html">Tobimune</a><a href="../analysis/malediction.html">Malediction</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/sand-bone.html",
    "Sand-Bone One-Sword Style",
    "Sand-Bone One-Sword Style: Subaru Urita’s school, sushi chef as cover, duplication as the assassination nightmare.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Sand-Bone',
    "Urita school",
    "Sand-Bone One-Sword Style",
    "砂骨一刀流",
    "A surviving bearer who would rather talk rice. The style is why relocating him is national policy.",
    """
  <p>Subaru Urita practices Sand-Bone One-Sword Style. He is a prolific pre-war smith, a sushi chef who owns Sushi Subaru, and a surviving Enchanted Blade bearer whose wartime sword is still unnamed in print. Duplication: several Subarus. A contract-opening assassination’s nightmare. After Sanso attacks begin, the Kamunabi relocate him.</p>
  <h2>School, not blade kit</h2>
  <p>Iai White Purity is the famous speed religion. Reigen is a hotel curriculum. Sand-Bone is the third named school this site had never filed. Subaru’s other homework is the vein thesis that lets Kunishige start Enchanted Blades at all. See <a href="../characters/subaru.html">Subaru</a>, <a href="veins.html">veins</a>, <a href="iai.html">Iai</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/subaru.html">Subaru</a><a href="veins.html">Veins</a><a href="iai.html">Iai</a><a href="reigen.html">Reigen</a><a href="bearers.html">Sword Bearers</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/reigen.html",
    "Reigen One-Sword Style",
    "Reigen One-Sword Style: Yojiro Sengoku’s school, taught to the Kyoto Bloodshed Hotel staff, read by Toto through a severed head.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Reigen',
    "Hotel school",
    "Reigen One-Sword Style",
    "霊厳一刀流",
    "A manager’s curriculum. Every employee is a student. Toto does not care about the syllabus.",
    """
  <p>Yojiro Sengoku, general manager of the Kyoto Bloodshed Hotel, is a master of Reigen One-Sword Style. He taught it to the hotel staff. The house is a respite under a veil, then a classroom where Chihiro copies Iai off Kuguri, then a demolition when Hiruhiko spends Play. Toto takes Sengoku’s head as a blood sample to confirm who is in the building.</p>
  <h2>Why a hotel has a style</h2>
  <p>Reigen is not Iai and not Sand-Bone. It is the reason the staff are not civilians in the useful sense. The hotel page is the building. This page is the syllabus the ten treat as furniture. See <a href="hotel.html">Kyoto Bloodshed Hotel</a>, <a href="../characters/sengoku.html">Sengoku</a>, <a href="../characters/toto.html">Toto</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="hotel.html">Kyoto hotel</a><a href="../characters/sengoku.html">Sengoku</a><a href="iai.html">Iai</a><a href="../characters/toto.html">Toto</a><a href="../arcs/sword-bearer.html">Sword Bearer</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/crimson-recital.html",
    "Crimson Recital",
    "Crimson Recital (Koen): Uruha’s innate art, dark while Kumeyuri is signed, back when Samura cuts the contract and keeps the man.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Crimson Recital',
    "Koen",
    "Crimson Recital",
    "紅演",
    "The banquet sword is the job. The recital is the person. Suzaku is the surgery that returns it.",
    """
  <p>Crimson Recital (紅演, Koen) is Yoji Uruha’s innate sorcery. A Lifelong Contract shuts it off while he holds Kumeyuri. When Samura cuts Uruha down at Senkutsuji, the scene reads as murder and a Hishaku pact. It is Suzaku used as surgery: the contract dies, the man walks, the old art limps back. Physical boost. He later spends it protecting Hakuri from Hishaku assassins.</p>
  <h2>Not Banquet</h2>
  <p>Banquet and Play are Kumeyuri. Koen is Uruha. The technique catalog mentioned the distinction in a clause. Reddit threads still mix them. This page keeps the person under the oiran sword. See <a href="../characters/uruha.html">Uruha</a>, <a href="../blades/kumeyuri.html">Kumeyuri</a>, <a href="contracts.html">contracts</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/uruha.html">Uruha</a><a href="../blades/kumeyuri.html">Kumeyuri</a><a href="contracts.html">Contracts</a><a href="../characters/samura.html">Samura</a><a href="senkutsuji.html">Senkutsuji</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/easy-does-it.html",
    "Operation Easy Does It",
    "Operation: Easy Does It: the Masumi job to keep Iori out of Hishaku hands after Senkutsuji, motorcycle included.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Easy Does It',
    "Masumi job",
    "Operation: Easy Does It",
    "作戦",
    "A name the chapters print like a briefing. Protect the daughter. Do not make a scene. The hotel makes a scene anyway.",
    """
  <p>Operation: Easy Does It is the Masumi assignment after Samura frees them: protect Iori Samura from the Hishaku plan to use her against her father. They pull her from school to the Kyoto Bloodshed Hotel. Sumi leaves on a motorcycle with Iori while Kuguri gives chase. Chihiro copies Iai in the house. Ikura trails Toto. The seal breaks when Iori protects a classmate’s fact in her own body.</p>
  <h2>A quiet name for a loud week</h2>
  <p>The Masumi page is the clan. The hotel page is the building. This page is the job title the English room kept quoting. Easy does not hold. Hiruhiko wrecks the upper floors with Play. Samura arrives. See <a href="../factions/masumi.html">Masumi</a>, <a href="../characters/iori.html">Iori</a>, <a href="hotel.html">hotel</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../factions/masumi.html">Masumi</a><a href="../characters/iori.html">Iori</a><a href="hotel.html">Kyoto hotel</a><a href="../characters/sumi.html">Sumi</a><a href="../arcs/sword-bearer.html">Sword Bearer</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/shinuchi.html",
    "Shinuchi",
    "Shinuchi as a title: the auction-house and Kamunabi name for Magatsumi, masterpiece as a listing, not a second sword.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Shinuchi',
    "真打",
    "Shinuchi",
    "真打",
    "A word that means the top of the bill. Readers kept asking if it was a seventh wartime blade. It is Magatsumi’s job title.",
    """
  <p>Shinuchi (真打) is the auction-house and Kamunabi name for Magatsumi. The glossary already used the word. Reddit and YouTube still treat it as a possibly separate sword. It is not. Shinuchi means masterpiece, the headliner, the listing at the 208th Rakuzaichi. Kyora sells a title. Yura spends a title. The steel is Magatsumi.</p>
  <h2>Why the double name stays</h2>
  <p>VIZ keeps both. English readers meet Shinuchi first as an auction rumor, Magatsumi later as a person. The leak, the seal, the basement, the possession path: all of that is one blade with a billing. See <a href="../blades/magatsumi.html">Magatsumi</a>, <a href="../fun/names.html">names in English</a>, <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../blades/magatsumi.html">Magatsumi</a><a href="../fun/names.html">Names</a><a href="../characters/akemura.html">Akemura</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a><a href="glossary.html">Glossary</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/veins.html",
    "Spirit Veins in Steel",
    "Subaru Urita’s vein thesis: tiny pathways in a katana that let spirit energy flow, the homework Kunishige uses on Datenseki.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Veins',
    "Urita thesis",
    "Veins in steel",
    "気脈",
    "Carbon, heat, humidity. A sushi chef’s book on how a sword conducts a soul.",
    """
  <p>Before Enchanted Blades exist, Subaru Urita’s work <em>Japanese Katana and the Flow of Spiritual Energy</em> argues that material is the key. Tiny disturbances from carbon, construction, and heat create pathways he calls veins. Spirit energy follows them the way current follows a wire. A blade designed around veins cuts clean. Hasumi’s lab had been looking for a storage battery for Datenseki overflow. Subaru’s veins are a conductor, not a battery. Kunishige’s eyes are what let the conductor survive 1,000 degrees of ore that wants to explode.</p>
  <h2>Why YouTube kept pausing chapter 125</h2>
  <p>Anime Explained and the spoiler tapes treat this blackboard as the power-system reveal. Smelting.html is the kiln. This page is the thesis on the board: veins, magnetite, tatara observation, Noro as expelled impurity. The first Enchanted Blade is still unnamed when tamahagane comes out of the collapsed furnace. See <a href="smelting.html">smelting</a>, <a href="../characters/subaru.html">Subaru</a>, <a href="first-blade.html">first blade talk</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="smelting.html">Smelting</a><a href="../characters/subaru.html">Subaru</a><a href="datenseki.html">Datenseki</a><a href="spirit-energy.html">Spirit energy</a><a href="first-blade.html">First blade</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/prophecy.html",
    "Soga Prophecy",
    "Soga prophecy as a national office: foresight used as government advice for millennia, not only Chiaki’s personal sight.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Prophecy',
    "Institution",
    "Soga prophecy",
    "予言",
    "A clan that tells the mainland what is coming, and a government that listens until a beach is cheaper.",
    """
  <p>For centuries before the Seitei War the Soga are the most influential sorcerer clan in Japan because a woman in each generation can see. They advise on national threats. That is an office, not a personality. Chiaki inherits it from a main-line prophetess who died without children. The princess page is her title as hostage tag. This page is the institution Reddit kept calling “the Soga CIA.”</p>
  <h2>Advice, then cargo</h2>
  <p>Prophecy made them aristocracy and made them useful. Giyu can treat the office as something you hand to Mikaboshi. Kunishige’s later household, a bowl instead of a forecast, is a refusal of this room. We do not invent unseen prophecies. See <a href="princess.html">Princess Soga</a>, <a href="izanami.html">Izanami</a>, <a href="../characters/chiaki.html">Chiaki</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="princess.html">Princess Soga</a><a href="izanami.html">Izanami</a><a href="../factions/soga.html">Soga</a><a href="../characters/chiaki.html">Chiaki</a><a href="../characters/giyu.html">Giyu</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/registration.html",
    "Sazanami Registration",
    "Sazanami birth registration: every clan member entered in the Storehouse as an object the subspace already knows.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Registration',
    "Clan ceremony",
    "Sazanami registration",
    "登録",
    "Born into a warehouse. Sorcerers can feel the tag. Hakuri’s later Storehouse is the same grammar used on purpose.",
    """
  <p>Sazanami children are registered in a ceremony at birth. The Storehouse treats them as known objects. Sorcerers can detect the registration. Auction goods are encased; clan members are not, because the building already has their names. Weapons can be summoned. People can be stored. The first head built a subspace that is also a census.</p>
  <h2>Hakuri’s version</h2>
  <p>Hakuri can register individuals and their spiritually charged possessions in his own Storehouse. That is why a walking Kura can un-arm and re-arm bearers. The clan used registration as ownership. He uses it as logistics. See <a href="storehouse.html">Storehouse</a>, <a href="naginojoen.html">Naginojoen</a>, <a href="../characters/hakuri.html">Hakuri</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="storehouse.html">Storehouse</a><a href="../characters/hakuri.html">Hakuri</a><a href="naginojoen.html">Naginojoen</a><a href="../factions/sazanami.html">Sazanami</a><a href="emergency-door.html">Emergency door</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/emergency-door.html",
    "The Emergency Access Door",
    "The Storehouse Emergency Access Door: a floating spare key in subspace whose twin sits in Naginojoen, already broken when Chihiro arrives.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Emergency door',
    "Spare key",
    "Emergency Access Door",
    "非常扉",
    "Insurance if the head dies before the ceremony. Kyora spends the insurance first.",
    """
  <p>The Emergency Access Door is the Sazanami fail-safe: if the Storehouse owner dies before ownership can pass at Naginojoen, the subspace can still be entered. Inside the Kura it is a floating door. In the world it sits in a sealed cemetery room. Chihiro scouts the Storehouse through Enten’s residual charge and notices the door that is never opened. When he, Shiba, and Hakuri reach Naginojoen, the twin is already destroyed.</p>
  <h2>A door that is a plot</h2>
  <p>The Storehouse page is the island. This page is the lock the infiltration was aimed at. Kyora does not leave a spare key for a discarded son. Hakuri becomes a second Storehouse instead. See <a href="storehouse.html">Storehouse</a>, <a href="naginojoen.html">Naginojoen</a>, <a href="../arcs/rakuzaichi.html">Rakuzaichi</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="storehouse.html">Storehouse</a><a href="naginojoen.html">Naginojoen</a><a href="../characters/kyora.html">Kyora</a><a href="../characters/hakuri.html">Hakuri</a><a href="../arcs/rakuzaichi.html">Rakuzaichi</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/food.html",
    "Meals in Kagurabachi",
    "Meals as plot in Kagurabachi: A Good Meal, Food, Tea, Moku shutting Chihiro up with a plate, Subaru’s sushi cover.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Meals',
    "Chapter titles",
    "Meals",
    "飯",
    "The first book titles food before it titles True Realm. The household is a table that keeps getting reset.",
    """
  <p>Chapter 5 is “A Good Meal.” Chapter 15 is “Food.” Chapter 17 is “Tea.” Before Enten versus Cloud Gouger, the book keeps seating people. Char needs to eat. Chihiro needs to remember the workshop was a kitchen. Moku later forces food on Chihiro when the boy starts eating himself after Senkutsuji. Subaru’s public life is a sushi restaurant. Hinao’s door is a cafe.</p>
  <h2>Why Sunday threads joke about the menu</h2>
  <p>Reddit and the first-read notes already clocked the meal titles. This page files them as setting, not a gag compilation. A hunt that will not spend innocents still has to feed them. The bowl on the workshop table is the same grammar as a plate on a train. See <a href="../fun/bowl.html">the bowl</a>, <a href="../world/cafe.html">Cafe Haru Haru</a>, <a href="../characters/moku.html">Moku</a>, <a href="../manga/chapter-1.html">chapter 1</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../fun/bowl.html">The bowl</a><a href="cafe.html">Cafe Haru Haru</a><a href="../characters/moku.html">Moku</a><a href="../characters/subaru.html">Subaru</a><a href="../fun/first-read.html">First-read</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/civilian.html",
    "Civilian Sorcerers",
    "Civilian sorcerers in Kagurabachi: small jobs, Hinao’s brokerage, yakuza and corporations, the street the Kamunabi exist above.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Civilian sorcerers',
    "Small jobs",
    "Civilian sorcerers",
    "民間",
    "Not the bureau. Not the ten. The people Hinao calls when a company wants a quiet spell.",
    """
  <p>Sorcery is public after the war, but most of it is not national. Civilian sorcerers handle small jobs. Hinao’s Cafe Haru Haru connects them to yakuza and corporations who need work done. Chihiro and Shiba take that work for three years after the raid. Madoka is a civilian employee who tries to go straight. The Korogumi are the firm on the same map.</p>
  <h2>Why the Kamunabi exist</h2>
  <p>Some jobs are national. Enchanted Blades, Sanso, Irishima: those are not cafe tickets. The underworld page is the city. This page is the labor category YouTube glossaries skip when they jump from spirit energy to yōtō. See <a href="../characters/hinao.html">Hinao</a>, <a href="underworld.html">underworld</a>, <a href="../factions/korogumi.html">Korogumi</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../characters/hinao.html">Hinao</a><a href="cafe.html">Cafe Haru Haru</a><a href="underworld.html">Underworld</a><a href="../factions/kamunabi.html">Kamunabi</a><a href="sorcery.html">Sorcery</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/train.html",
    "The Train Interception",
    "The train interception: Chihiro, Hakuri, and Uruha leave Kokugoku, Hiruhiko boards, and the fight spills into a kabuki house.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Train',
    "Sword Bearer start",
    "The train",
    "列車",
    "A box fails. The next scene is a carriage. Friendship, for Hiruhiko, starts by losing arms.",
    """
  <p>After Kokugoku, Chihiro and Hakuri put Uruha on a train bound for Senkutsuji. Hiruhiko boards with sorcerers. Chihiro tackles him off. The fight lands in a kabuki theater. Chihiro severs Hiruhiko’s arms, pulls Hishaku intelligence, and earns a warped kind of recognition: two eighteen-year-olds who grew up inside violence. Hakuri and Uruha reach the temple with Moku and Sumi.</p>
  <h2>Not a fortress fight</h2>
  <p>Battles.html folds this into Sanso and Senkutsuji. The English room still talks about “the train chapter” as its own week. This page keeps the carriage and the theater so the Steam Squad’s grave and Samura’s surgery stay separate rooms. See <a href="kokugoku.html">Kokugoku</a>, <a href="../characters/hiruhiko.html">Hiruhiko</a>, <a href="../arcs/sword-bearer.html">Sword Bearer</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="kokugoku.html">Kokugoku</a><a href="senkutsuji.html">Senkutsuji</a><a href="../characters/hiruhiko.html">Hiruhiko</a><a href="../characters/uruha.html">Uruha</a><a href="battles.html">Battles</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/first-blade.html",
    "The First Enchanted Blade",
    "The first Enchanted Blade in Kagurabachi: still unnamed after Ironworks and I'm Fine!. Fan camps, no invented title.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / First blade',
    "Unnamed in print",
    "The first blade",
    "最初の刀",
    "Chapter 130 pulls tamahagane. Subaru says it will make a terrifying sword. Jump has not printed the name.",
    """
  <p>Kunishige’s wartime six are forged after two years of failed Datenseki research. The chapters through 130 show the kiln, the eyes, Chiaki as the reason the work stays open, and tamahagane coming out of a collapsed furnace. They do not name the first finished Enchanted Blade. This page is a warning label, not a leak.</p>
  <h2>What the rooms are doing</h2>
  <p>MangaDex, Reddit, and the Mystiqora-style tapes argue Magatsumi, Tobimune, Kumeyuri, or Subaru’s still-unnamed sword. Some want a new bearer. The chapters have not confirmed any of that. We will not. When Jump prints a title it belongs on the <a href="techniques.html">catalog</a> and the <a href="../blades/index.html">blade index</a>. Until then the first blade is work. See <a href="smelting.html">smelting</a>, <a href="../manga/chapter-130.html">chapter 130</a>, <a href="../fun/theories.html">marked theories</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="smelting.html">Smelting</a><a href="../manga/chapter-130.html">Chapter 130</a><a href="../fun/theories.html">Theories</a><a href="../blades/index.html">Blades</a><a href="../characters/subaru.html">Subaru</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/core-station.html",
    "Core Station",
    "Core Station and the Kamunabi HQ underground: Level 1, named operators the register left as furniture, the room the Shigyu reach.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Core Station',
    "HQ underground",
    "Core Station",
    "中枢",
    "Chapter 95 is titled Core. The building has a downstairs the ten paid hirelings to see.",
    """
  <p>Kamunabi headquarters has levels. Chapter 95 is “Core.” The Shigyu brothers reach Level 1’s underground core with a Hishaku member before Azami ends them. The name register lists Core Station Surveyor and operators, West Entrance Commander, Ishihira, Kashima, as HQ furniture tropes lists named. This site still does not invent biographies for furniture.</p>
  <h2>A room, not a cast</h2>
  <p>Yukisada’s Vessel work, Hagiwara’s later magnetism, Hakuri parking the Kamunabi vessel in the Storehouse: those are the core as a system. The titled chapter is the week the downstairs stops being theoretical. See <a href="hq.html">headquarters</a>, <a href="../characters/shigyu.html">Shigyu</a>, <a href="barriers.html">barriers</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="hq.html">Headquarters</a><a href="../characters/shigyu.html">Shigyu</a><a href="../characters/azami.html">Azami</a><a href="barriers.html">Barriers</a><a href="register.html">Register</a><a href="index.html">World</a></nav>
""",
)

add(
    "world/izanami.html",
    "Izanami and the Soga Warrant",
    "Izanami in Kagurabachi: the printed claim that Soga foresight proves descent from the goddess, warrant rather than theology class.",
    '<a href="../index.html">Archive</a> / <a href="index.html">World</a> / Izanami',
    "Warrant",
    "Izanami",
    "伊邪那美",
    "The chapters say the sight proves the blood. They do not reprint the Kojiki.",
    """
  <p>Soga foresight is described as inherited proof that the prophetess descends from Izanami. That sentence is a warrant: why a government listens, why Princess Soga is an office, why a lower-branch girl can be elevated when the main line fails. This encyclopedia had used the name inside Chiaki’s file and the princess page. Reddit kept searching for a myth explainer. This is the explainer: we do not add kami genealogy the manga did not print.</p>
  <h2>Goddess as paperwork</h2>
  <p>Izanami in the old stories is creation and death. In this book she is the stamp on a clan’s letterhead. Chiaki’s sight is the living version. Akemura’s later choices are not her instruction sheet. See <a href="prophecy.html">prophecy</a>, <a href="princess.html">Princess Soga</a>, <a href="../characters/chiaki.html">Chiaki</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="prophecy.html">Prophecy</a><a href="princess.html">Princess Soga</a><a href="../factions/soga.html">Soga</a><a href="../characters/chiaki.html">Chiaki</a><a href="../fun/names.html">Names</a><a href="index.html">World</a></nav>
""",
)

# --- Fun / media / manga / collectibles ---

add(
    "fun/etymology.html",
    "What Kagurabachi Means",
    "Kagurabachi’s title: kagura as sacred dance, bachi as strike or punishment, and what Hokazono has and has not said.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Title',
    "カグラバチ",
    "What the title means",
    "語源",
    "English rooms ask this every week. The kanji are not printed on the spine the way Enten is printed on a fish.",
    """
  <p>The series title is カグラバチ, Kagurabachi, written in katakana. Readers split it as kagura (神楽), the Shinto sacred dance, and bachi (罰 or 撥): punishment, divine retribution, or the stick that strikes a drum. The English fandom and Japanese comment sections have run that reading since 2023. Hokazono’s interviews talk Hollywood Japan, goldfish, and swords. They do not hand us a classroom etymology we can treat as a chapter fact.</p>
  <h2>How this archive uses the word</h2>
  <p>We keep the katakana. We do not pretend the title is a technique name. Enchanted Blades have kanji the book prints. The magazine title is a sound. If a later comment from the author pins one kanji, it belongs here. Until then the dance-and-strike reading is how the rooms talk, marked as talk. See <a href="names.html">names in English</a>, <a href="hokazono.html">Hokazono</a>, <a href="../guide/series.html">the series</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="names.html">Names</a><a href="hokazono.html">Hokazono</a><a href="pronounce.html">Pronunciation</a><a href="../guide/series.html">The series</a><a href="meme.html">Meme</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/pacing.html",
    "Hokazono on Pacing",
    "Takeru Hokazono on Kagurabachi’s pace: the Da Vinci interview citing Jujutsu Kaisen and Chainsaw Man, and what that is not.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Pacing',
    "Da Vinci",
    "Pacing",
    "速度",
    "He said the recent sense of speed is the brief. He also said he wanted a story about people fighting each other.",
    """
  <p>In a <em>Da Vinci</em> interview Hokazono said that while drawing he thought it might be early, then read <em>Jujutsu Kaisen</em> and <em>Chainsaw Man</em> and felt the current magazine’s sense of speed. He tries to keep readers engaged by moving. In the same stretch he said he did not want to make the book too entertaining; he wanted a story about people fighting each other. Animehunch and the English room circulated the quotes in 2025–2026.</p>
  <h2>Not a clone brief</h2>
  <p>The author page already has Winter Soldier, Tarantino, goldfish. This page is the magazine-speed comment YouTube used as a thumbnail. Influence is not theft. Part 2’s kiln chapters are the other half of the brief: he will stop the week to talk to a swordsmith. See <a href="hokazono.html">Hokazono</a>, <a href="hiatus.html">the 2026 rest</a>, <a href="../manga/publication.html">publication</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="hokazono.html">Hokazono</a><a href="hiatus.html">Hiatus</a><a href="../manga/publication.html">Publication</a><a href="youtube.html">YouTube</a><a href="../guide/series.html">The series</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/world-tour.html",
    "Kagurabachi Anime World Tour",
    "Kagurabachi Anime World Tour: first twenty minutes from July 2026 at Anime Expo, Japan Expo, AnimagiC, and Anime NYC.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / World tour',
    "July 2026",
    "Anime World Tour",
    "世界ツアー",
    "A ticket and a memory unless a booklet ships. The broadcast is still April 2027.",
    """
  <p>Before the Cypic series airs, the first twenty minutes of episode 1 toured from July 2026: Anime Expo in Los Angeles, Japan Expo in Paris, AnimagiC in Mannheim, Anime NYC in New York. Some stops added panels with Taihi Kimura and producers. The full first episode is slated for a Japan screening in Q2 2027. Crunchyroll has the television license outside the listed exceptions.</p>
  <h2>What this page is not</h2>
  <p>The anime page is the countdown and the teaser. Collectibles will log an SKU if a tour booklet exists. This page is the event the English room treated as a pilgrimage. Cour length and adaptation stopping point are still unconfirmed. The elevator-ending camp is still a camp. See <a href="../media/anime.html">anime</a>, <a href="../guide/watch.html">how to watch</a>, <a href="../media/staff.html">staff</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../media/anime.html">Anime</a><a href="../guide/watch.html">How to watch</a><a href="../media/staff.html">Staff</a><a href="../collectibles/index.html">Collectibles</a><a href="voices.html">Voices</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/hiatus.html",
    "The 2026 Rest",
    "Kagurabachi’s 2026 rest after chapter 126: an announced month so Hokazono could keep the kiln honest, return in August, Ironworks on 23 August.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / 2026 rest',
    "After Fire",
    "The 2026 rest",
    "休載",
    "One person, a war flashback, and a mineral that needed a real smith’s vocabulary.",
    """
  <p>After chapter 126, “Fire,” the official account announced a rest. Serialization paused from Weekly Shōnen Jump 2026 issue 31 (29 June) and returned in August. Chapter 129, “Ironworks,” is 23 August 2026. Chapter 130, “I'm Fine!,” is 30 August. The reason given was quality: Hokazono had talked to a real swordsmith, and the magazine was willing to wait on heat.</p>
  <h2>Not a cancellation rumor</h2>
  <p>Sunday threads treated the month as a health decision and a craft decision. Both can be true. This page files the dates so the smelting chapters are not a blur. We do not invent chapter 131’s title or plot. Official reading stays VIZ / MANGA Plus. See <a href="../world/smelting.html">smelting</a>, <a href="hokazono.html">Hokazono</a>, <a href="../manga/publication.html">publication</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/smelting.html">Smelting</a><a href="hokazono.html">Hokazono</a><a href="../manga/chapter-129.html">Ironworks</a><a href="../manga/chapter-130.html">Chapter 130</a><a href="pacing.html">Pacing</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/theories.html",
    "Marked Fan Theories",
    "Kagurabachi theories the rooms actually run: first blade identity, Magatsumi and Ariu’s insects, cour 1’s elevator. Marked as talk, never as print.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Theories',
    "Not print",
    "Marked theories",
    "考察",
    "The media page already hosts videos. This page is the list of claims we refuse to file as fact.",
    """
  <p>After chapter 119, explainers argue Magatsumi copies Ariu Mikaboshi’s insect sorcery. The chapters have not confirmed that. After 130, Reddit and MangaDex argue the first Enchanted Blade is Magatsumi, Tobimune, Kumeyuri, or Subaru’s unnamed sword. Jump has not printed a name. YouTube still bets cour 1 ends at chapter 60’s elevator. Cypic has not said so.</p>
  <h2>How this archive treats a camp</h2>
  <p>A theory can live here if it is labeled. It cannot migrate onto a character page as biography. The first-blade page is the kiln warning. The anime page keeps the elevator as a camp. If you want the printed insect kit, read <a href="../blades/magatsumi.html">Magatsumi</a> and <a href="../characters/ariu.html">Ariu</a> as two files. See <a href="youtube.html">YouTube room</a>, <a href="reddit.html">Reddit room</a>, <a href="../world/first-blade.html">first blade</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../world/first-blade.html">First blade</a><a href="youtube.html">YouTube</a><a href="reddit.html">Reddit</a><a href="../media/index.html">Videos</a><a href="../media/anime.html">Anime</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/pronounce.html",
    "How to Say the Names",
    "How to pronounce Kagurabachi names in English rooms: Kagurabachi, Chihiro, Kunishige, Enten, Magatsumi, Kamunabi, Hishaku.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Pronunciation',
    "Sound",
    "How to say it",
    "発音",
    "Sunday voice chats keep asking. This is a speaking list, not a new translation.",
    """
  <p>Kagurabachi is roughly kah-goo-rah-bah-chee. Chihiro Rokuhira: chee-hee-roh roh-koo-hee-rah. Kunishige: koo-nee-shee-geh. Enten: en-ten. Magatsumi: mah-gah-tsoo-mee. Shinuchi: sheen-oo-chee. Kamunabi: kah-moo-nah-bee. Hishaku: hee-shah-koo. Datenseki: dah-ten-seh-kee. Irishima: ee-ree-shee-mah.</p>
  <h2>What we will not do</h2>
  <p>We will not respell VIZ’s official English. Cloud Gouger stays Cloud Gouger. Enchanted Blade stays the site’s word for yōtō. The names page is the translation argument. This page is the sound the English Discord asks for before a watch party. See <a href="names.html">names in English</a>, <a href="etymology.html">title</a>, <a href="voices.html">voices</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="names.html">Names</a><a href="etymology.html">Title</a><a href="voices.html">Voices</a><a href="../guide/cast.html">Who is who</a><a href="fandom.html">Fandom</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/youtube.html",
    "YouTube Recap Culture",
    "Kagurabachi on YouTube: spoiler channels, power-system explainers, Anime Explained, and why this archive still sends you to VIZ.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / YouTube',
    "Spoiler tapes",
    "YouTube recaps",
    "動画",
    "The media index already lists official trailers. This page is the recap economy the Sunday room actually watches.",
    """
  <p>English YouTube around Kagurabachi is mostly three jobs: official teasers, long retrospectives for people who fell behind Part 1, and weekly spoiler tapes that race the magazine. Anime Explained and similar channels pause on the 125 blackboard, the Rokuhira eyes, and the first-blade question. Weekend Weebs is useful on True Realm. The media index already hosts those links as arguments. This page is the culture: thumbnails that invent a finished sword, runtimes that outpace Jump, comments that treat a camp as a leak.</p>
  <h2>The rule on this site</h2>
  <p>Watch the tape. Read the chapter on VIZ or MANGA Plus. If a video names the first Enchanted Blade, it is guessing. If it ends cour 1 on an elevator, it is guessing. Official trailers first: <a href="../media/index.html">theories and videos</a>. Printed kiln: <a href="../world/smelting.html">smelting</a>. Marked camps: <a href="theories.html">theories</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../media/index.html">Videos</a><a href="theories.html">Theories</a><a href="reddit.html">Reddit</a><a href="../media/anime.html">Anime</a><a href="sunday.html">Sunday</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "fun/reddit.html",
    "r/Kagurabachi",
    "r/Kagurabachi and the English Reddit room: weekly threads, first-blade arguments, power-system posts, and what this encyclopedia will not scrape.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Fun</a> / Reddit',
    "Sunday thread",
    "r/Kagurabachi",
    "reddit",
    "The board already hosts stills. This page is the conversation those stills sit under.",
    """
  <p>The English subreddit is the weekly thread, the first-blade poll, the “is Magatsumi just Ariu’s kit” post, and the power-system essay that starts from spirit energy instead of a goldfish. MangaDex chapter threads run the same arguments with more heat. This site’s Sunday board already shows credited pictures. The fandom page already maps the hashtag. This page is the forum as a habit.</p>
  <h2>What we do not do</h2>
  <p>We do not scrape usernames into the encyclopedia. We do not file a poll as print. We do not host leaks. If you want the printed answer, open the chapter on VIZ or MANGA Plus. If you want the camp, open <a href="theories.html">marked theories</a>. Pictures: <a href="community.html">Sunday board</a>. Habit: <a href="sunday.html">Sunday ritual</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="community.html">Sunday board</a><a href="sunday.html">Sunday ritual</a><a href="theories.html">Theories</a><a href="fandom.html">English fandom</a><a href="youtube.html">YouTube</a><a href="index.html">Fun</a></nav>
""",
)

add(
    "media/recommendations.html",
    "Who Recommended Kagurabachi",
    "Public recommendations for Kagurabachi: Kōhei Horikoshi, Masashi Kishimoto, Vaundy, and the polls that followed the meme.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Theories</a> / Recommendations',
    "Plaques",
    "Who recommended it",
    "推薦",
    "The publication record listed the names in a paragraph. The English room kept asking for the plaque page.",
    """
  <p>Kōhei Horikoshi and Masashi Kishimoto have recommended Kagurabachi. Vaundy has too. Those are public comments, not ghostwriters. The series ranked seventh on AnimeJapan’s 2024 Most Wanted Anime Adaptation poll, won the 2024 Next Manga Award in print, placed on Da Vinci’s Book of the Year (22nd in 2024, 13th in 2025), and sixth on <em>Kono Manga ga Sugoi!</em> 2025 for male readers. 2026: Daruma for Best Action Manga at Japan Expo.</p>
  <h2>A plaque is not the chapter</h2>
  <p>The meme page is why people opened chapter 1. This page is why a certain kind of reader stayed after the joke: other makers pointed. Circulation and ISBNs stay on the publication record. See <a href="../manga/publication.html">publication</a>, <a href="../fun/meme.html">meme to flagship</a>, <a href="../fun/hokazono.html">Hokazono</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/publication.html">Publication</a><a href="../fun/meme.html">Meme</a><a href="../fun/hokazono.html">Hokazono</a><a href="anime.html">Anime</a><a href="staff.html">Staff</a><a href="index.html">Theories</a></nav>
""",
)

add(
    "media/editions.html",
    "Kagurabachi Abroad",
    "Kagurabachi outside Japan: VIZ and MANGA Plus simulpub, English tankōbon trailing about nine months, Kana in France.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Theories</a> / Editions',
    "Licenses",
    "Editions abroad",
    "海外",
    "Same week on the apps. A different object on the shelf. French type on a Volume 11 promo.",
    """
  <p>VIZ Media and MANGA Plus publish the English chapter the same week as <em>Weekly Shōnen Jump</em>. That is the legal Sunday. VIZ’s print Volume 1 arrived 5 November 2024. English editions trail Japanese tankōbon by about nine months. Volume 9 English is listed for 3 November 2026. Volumes 10 and 11 English were still TBD when this page was filed. A French edition via Kana is noted on Volume 11 promo. Other territories follow local Jump licenses.</p>
  <h2>Why this is not the volume guide</h2>
  <p>ISBNs and jackets live on the manga pages. This page is the license map Reddit asks for when someone wants to buy in Paris or wait for a hard copy. We do not list scans. Crunchyroll and Muse Communication are the anime licenses, not the book. See <a href="../manga/volumes.html">volumes</a>, <a href="../manga/publication.html">publication</a>, <a href="../collectibles/shop.html">where to buy</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../manga/volumes.html">Volumes</a><a href="../manga/publication.html">Publication</a><a href="../collectibles/shop.html">Shop</a><a href="anime.html">Anime</a><a href="../fun/sunday.html">Sunday</a><a href="index.html">Theories</a></nav>
""",
)

add(
    "manga/omake.html",
    "Volume Extras",
    "Kagurabachi Jump Comics extras: Genichi Sojo’s Bathhouse Quest, Soya Sazanami’s Memories, Begone!, and why the magazine chapter is not the book.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Manga Guide</a> / Volume extras',
    "Jump Comics",
    "Volume extras",
    "おまけ",
    "The oneshots page is the gags. This page is the reason you buy the tankōbon.",
    """
  <p>Japanese Jump Comics volumes carry extras the weekly magazine does not. Printed so far on this site’s radar: <em>Genichi Sojo’s Bathhouse Quest</em> in two parts, and <em>Soya Sazanami’s Memories, Begone!</em> The oneshots page already walks those jokes. This page is the category: jackets, extras, and the red-to-black spine bar are why the tankōbon is a different object from Sunday’s chapter.</p>
  <h2>Buy the book</h2>
  <p>We do not host extras. Color leads in the magazine do not always reprint. If a later volume adds a new omake, it belongs here and on the volume guide. See <a href="../fun/oneshots.html">bathhouse and extras</a>, <a href="volumes.html">volume guide</a>, <a href="../collectibles/index.html">collectibles</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../fun/oneshots.html">Oneshots</a><a href="volumes.html">Volumes</a><a href="covers.html">Covers</a><a href="author-comments.html">Author comments</a><a href="../collectibles/index.html">Collectibles</a><a href="index.html">Manga guide</a></nav>
""",
)

add(
    "manga/author-comments.html",
    "Author Comments",
    "Hokazono’s magazine comments and public notes: the announced 2026 rest, the swordsmith visit, and what this archive will not invent.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Manga Guide</a> / Author comments',
    "WSJ margin",
    "Author comments",
    "作者コメント",
    "Weekly Jump still prints a box. We file the ones that changed the schedule, not a fake quote dump.",
    """
  <p>Weekly Shōnen Jump author comments are short. The ones that matter on this site are public and dated: the 2026 rest after “Fire,” the note that Hokazono spoke with a real swordsmith so the kiln would not be cosplay, the interviews already cited on the author page (Asahi goldfish, Anime NYC 2025, <em>Da Vinci</em> pace). We do not invent weekly boxes we have not read.</p>
  <h2>Where the longer talk lives</h2>
  <p>Hokazono’s file holds Hollywood Japan, Winter Soldier, goldfish not koi. The pacing page holds Jujutsu Kaisen and Chainsaw Man. The rest page holds the month off. This page is the index of those comments so a search for “author comment” has a door. See <a href="../fun/hokazono.html">Hokazono</a>, <a href="../fun/hiatus.html">2026 rest</a>, <a href="../fun/pacing.html">pacing</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="../fun/hokazono.html">Hokazono</a><a href="../fun/hiatus.html">2026 rest</a><a href="../fun/pacing.html">Pacing</a><a href="publication.html">Publication</a><a href="omake.html">Volume extras</a><a href="index.html">Manga guide</a></nav>
""",
)

add(
    "collectibles/figures.html",
    "Figures and Other Merch",
    "Kagurabachi merch beyond volumes and UNION ARENA: what this archive will log, and what we will not invent as a SKU.",
    '<a href="../index.html">Archive</a> / <a href="index.html">Collectibles</a> / Figures',
    "No fake SKUs",
    "Figures and other merch",
    "フィギュア",
    "The shop page is where to buy books. The card page is UE16BT. This page is everything else that actually exists.",
    """
  <p>This encyclopedia already files tankōbon, English trades, and the UNION ARENA set. Official apparel, posters, and figures appear as Jump and anime licenses land. We do not invent a Banpresto number or a prize figure that has not been solicited. A world-tour booklet, if one ships, belongs on collectibles with an SKU. Until then the tour is a ticket.</p>
  <h2>What to buy first</h2>
  <p>The object is still the volume. Cards are a separate hobby with a partner door on the UNION ARENA page. Replica swords sold by random shops are not official just because they use a name. When a licensed figure is announced, this page will take the line. See <a href="index.html">collectibles</a>, <a href="shop.html">where to buy</a>, <a href="union-arena.html">UNION ARENA</a>.</p>
    <nav class="related" aria-label="Related pages"><a href="index.html">Collectibles</a><a href="shop.html">Shop</a><a href="union-arena.html">UNION ARENA</a><a href="../fun/world-tour.html">World tour</a><a href="../manga/volumes.html">Volumes</a><a href="../manga/omake.html">Volume extras</a></nav>
""",
)

if __name__ == "__main__":
    print("pages", len(PAGES))
    for rel, title, desc in PAGES:
        print(rel)
