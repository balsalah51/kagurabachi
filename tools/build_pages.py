#!/usr/bin/env python3
"""Generate Kagurabachi Archive inner pages from templates."""
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
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
"""

FOOT = """
  </main>
  <div id="site-footer"></div>
  <script src="{js}"></script>
</body>
</html>
"""


def page(rel, title, desc, body, depth=1):
    prefix = "../" * depth
    html = (
        HEAD.format(title=title, desc=desc, css=f"{prefix}css/site.css")
        + body
        + FOOT.format(js=f"{prefix}js/site.js")
    )
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def crumb(*parts):
    bits = ['<a href="../index.html">Archive</a>']
    for label, href in parts[:-1]:
        bits.append(f'<a href="{href}">{label}</a>')
    bits.append(parts[-1] if isinstance(parts[-1], str) else parts[-1][0])
    return f'<p class="crumb">{" / ".join(bits)}</p>'


def hero(kicker, title, jp, lede):
    return f"""<header class="page-hero"><div>
      <p class="kicker">{kicker}</p>
      <h1>{title}<span class="jp">{jp}</span></h1>
      <p class="lede">{lede}</p>
    </div></header>
"""


def infobox(name, jp, portrait_class, caption, rows):
    dls = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return f"""<aside class="infobox">
      <div class="infobox-head"><h2>{name}</h2><span class="jp">{jp}</span></div>
      <div class="portrait {portrait_class}"><svg viewBox="0 0 160 90" fill="none" aria-hidden="true"><path d="M22 48c18-22 40-24 58-10 6-16 28-24 48-8-22 20-40 18-54 6-10 18-32 28-52 12z" fill="#e8c547"/></svg>
        <div class="portrait-caption">{caption}</div>
      </div>
      <dl>{dls}</dl>
    </aside>"""


# ——— Characters index ———
page(
    "characters/index.html",
    "Characters",
    "Kagurabachi character encyclopedia: Chihiro, the blade bearers, Kamunabi, Hishaku, and the Sazanami clan.",
    crumb("Characters")
    + hero("Encyclopedia", "Characters", "登場人物", "The people who hold the blades, the people who sold them, and the people still paying for the war.")
    + """
    <h2>Chihiro’s circle</h2>
    <div class="grid">
      <a class="card" href="chihiro.html"><div class="card-art p-chihiro"></div><div class="card-body"><span class="tag">Enten</span><h3>Chihiro Rokuhira</h3><p>Protagonist. Swordsmith’s son. Age 18.</p></div></a>
      <a class="card" href="kunishige.html"><div class="card-art p-kunishige"></div><div class="card-body"><span class="tag">Smith</span><h3>Kunishige Rokuhira</h3><p>Forged all seven Enchanted Blades.</p></div></a>
      <a class="card" href="shiba.html"><div class="card-art p-shiba"></div><div class="card-body"><span class="tag">Sorcerer</span><h3>Togo Shiba</h3><p>Family friend. Teleportation.</p></div></a>
      <a class="card" href="hakuri.html"><div class="card-art p-hakuri"></div><div class="card-body"><span class="tag">Storehouse</span><h3>Hakuri Sazanami</h3><p>Disowned Sazanami. Dual inheritance.</p></div></a>
      <a class="card" href="char.html"><div class="card-art p-char"></div><div class="card-body"><span class="tag">Kyonagi</span><h3>Char Kyonagi</h3><p>Last of a regenerative clan.</p></div></a>
      <a class="card" href="iori.html"><div class="card-art p-iori"></div><div class="card-body"><span class="tag">Iai</span><h3>Iori Samura</h3><p>Samura’s daughter. Memory-sealed.</p></div></a>
    </div>
    <h2>Blade bearers &amp; the war</h2>
    <div class="grid">
      <a class="card" href="samura.html"><div class="card-art p-samura"></div><div class="card-body"><span class="tag">Tobimune</span><h3>Seiichi Samura</h3><p>Fastest bearer. Iai White Purity.</p></div></a>
      <a class="card" href="uruha.html"><div class="card-art p-uruha"></div><div class="card-body"><span class="tag">Kumeyuri</span><h3>Yoji Uruha</h3><p>Prodigy loyal to the Rokuhira name.</p></div></a>
      <a class="card" href="akemura.html"><div class="card-art p-akemura"></div><div class="card-body"><span class="tag">Magatsumi</span><h3>Akemura Soga</h3><p>The Sword Master.</p></div></a>
    </div>
    <h2>Kamunabi, Hishaku, auction house</h2>
    <div class="grid">
      <a class="card" href="hiyuki.html"><div class="card-art p-hiyuki"></div><div class="card-body"><span class="tag">Kamunabi</span><h3>Hiyuki Kagari</h3><p>Flame Bone of the Starving.</p></div></a>
      <a class="card" href="sojo.html"><div class="card-art p-sojo"></div><div class="card-body"><span class="tag">Cloud Gouger</span><h3>Genichi Sojo</h3><p>Arms dealer. First major rival.</p></div></a>
      <a class="card" href="yura.html"><div class="card-art p-yura"></div><div class="card-body"><span class="tag">Hishaku</span><h3>Yura</h3><p>The man who ordered the raid.</p></div></a>
      <a class="card" href="kyora.html"><div class="card-art p-kyora"></div><div class="card-body"><span class="tag">Sazanami</span><h3>Kyora Sazanami</h3><p>Eleventh head. Rakuzaichi auctioneer.</p></div></a>
    </div>
    """,
)

# Character article factory
def character(slug, name, jp, kicker, lede, portrait, caption, rows, article, related):
    rels = "".join(f'<a href="{u}">{t}</a>' for t, u in related)
    body = (
        crumb(("Characters", "index.html"), name)
        + hero(kicker, name, jp, lede)
        + f"""<div class="layout">
      <article class="article">{article}
        <p class="related">{rels}</p>
      </article>
      {infobox(name, jp, portrait, caption, rows)}
    </div>"""
    )
    page(f"characters/{slug}.html", name, lede, body)


character(
    "chihiro",
    "Chihiro Rokuhira",
    "六平 千鉱",
    "Enchanted Blade bearer · Enten",
    "The swordsmith’s son who inherited the seventh blade — and, later, the reason it was made.",
    "p-chihiro",
    "Decorative mark — goldfish of Enten. Not official art.",
    [
        ("Age", "18"),
        ("Birthday", "August 11"),
        ("Occupation", "Sword-bearer; later Kamunabi-aligned"),
        ("Enchanted Blade", '<a href="../blades/enten.html">Enten</a>'),
        ("Style", "Self-taught Iai White Purity Style (by imitation)"),
        ("Family", '<a href="kunishige.html">Kunishige Rokuhira</a> (father); <a href="akemura.html">Akemura Soga</a> (maternal uncle)'),
        ("Allies", "Shiba, Hakuri, Char, Iori, Masumi"),
        ("Voiced by", "Shoya Ishige (voiced comic); Taihi Kimura (anime)"),
    ],
    """
    <nav class="toc"><strong>On this page</strong>
      <ol><li>Overview</li><li>Personality</li><li>Abilities</li><li>Story role</li><li>Notes</li></ol>
    </nav>
    <h2>Overview</h2>
    <p>Chihiro grew up in isolation at his father’s workshop, training as a smith and as a swordsman in the quiet years after the Seitei War. Three years before the main story, the Hishaku murdered Kunishige and stole the six wartime Enchanted Blades. Chihiro survived, took Enten — the seventh blade, forged with him as a teenager — and went into the underworld with Togo Shiba to recover the swords and kill the men who ordered the raid.</p>
    <p>He is typically stoic and economical with words, but he will not spend innocent lives for the hunt. That line is the difference between him and almost every adult who touched the blades during the war.</p>
    <h2>Personality</h2>
    <p>Revenge is the engine, not the whole machine. Chihiro observes before he draws. He copies swordsmanship by watching — Uruha, Samura, Iori — and treats Enten as a partner rather than a trophy. After he learns what the Seitei War actually cost, the mission shifts: Enten was never only a weapon of succession. Kunishige made it to <em>end</em> the other blades.</p>
    <h2>Abilities</h2>
    <p>Enten manifests spirit energy as water and three goldfish. <strong>Kuro</strong> is the black fish: flying slashes, later extended as Kuro: Shred. <strong>Aka</strong> is the red fish: absorb an attack, then spend it. <strong>Nishiki</strong> is the tricolor cloak: speed, density, and a built-in resistance to other Enchanted Blade ailments — Enten’s purpose showing through the technique list.</p>
    <p>He briefly contracted the dying Cloud Gouger after Sojo’s death and spent its last charges at the Rakuzaichi. He is a keen enough student to fake Iai White Purity after watching its practitioners.</p>
    <h2>Story role</h2>
    <p>Chihiro is the viewpoint through Vs. Sojo, the Rakuzaichi, and the Sword Bearer Assassination arc. He hands Magatsumi to the Kamunabi in exchange for keeping Enten and working inside the system. By the end of Part 1 he has seen the Sword Master wear another man’s body, watched Samura spend his life, and started thinking like a smith again: <span class="spoiler">notes for a new Enten, and even a new Cloud Gouger, from the pieces he still holds.</span></p>
    <h2>Notes</h2>
    <p>Hokazono has said goldfish beat koi because the fin-to-body ratio read better on the page and because the bowl of fish was a better symbol of Chihiro and Kunishige’s daily life than a carp would have been. The fighting language is a household object first.</p>
    """,
    [
        ("Enten", "../blades/enten.html"),
        ("Kunishige", "kunishige.html"),
        ("Vs. Sojo Arc", "../arcs/vs-sojo.html"),
        ("What Enten was for", "../analysis/enten-purpose.html"),
    ],
)

character(
    "kunishige",
    "Kunishige Rokuhira",
    "六平 国重",
    "Swordsmith · Enchanted Blades",
    "The only smith who ever stabilized Datenseki. He ended a war and then spent the rest of his life trying to unmake the ending.",
    "p-kunishige",
    "Decorative mark. Not official art.",
    [
        ("Birthday", "June 5"),
        ("Age at death", "37"),
        ("Occupation", "Weapons dealer, then hermit smith"),
        ("Works", "Six wartime Enchanted Blades; Enten"),
        ("Partner", "Chiaki Soga"),
        ("Voiced by", "Kenta Fujimaki (voiced comic); Tomokazu Seki (anime)"),
    ],
    """
    <h2>Overview</h2>
    <p>Before the Seitei War, Kunishige sold swords to people he could stand, which meant he barely ate. The Kamunabi’s Datenseki research went nowhere for two years. Shiba believed Kunishige’s eyes — his ability to see what the ore was doing — were the only way to make the mineral usable. He was right. The Enchanted Blades turned the war. They also made possible the Malediction.</p>
    <p>After Akemura used Magatsumi to kill the remaining island population, Kunishige confiscated all six blades, hid with help from Azami and Shiba, and raised Chihiro in a workshop over a cellar full of swords he could not break. Every attempt to destroy them failed. Enten, forged with his son nearly fifteen years after the war, was the first blade built as a counter rather than a weapon of state.</p>
    <h2>The goldfish</h2>
    <p>The three goldfish in the house — later Kuro, Aka, and Nishiki — are the emotional core of Enten. Hokazono has said he almost used koi, then realized goldfish better recorded the small contest of who the fish liked more. That domestic joke becomes Chihiro’s entire fighting style.</p>
    <h2>Death</h2>
    <p>Three Hishaku sorcerers raided the house, killed Kunishige in front of Chihiro, and took the six wartime blades. Enten stayed with the son. The Kamunabi later learned a director had leaked the address. The smith’s last work is still trying to finish the job he could not do with a hammer.</p>
    """,
    [("Chihiro", "chihiro.html"), ("Datenseki", "../world/datenseki.html"), ("Enten", "../blades/enten.html")],
)

character(
    "shiba",
    "Togo Shiba",
    "柴 登吾",
    "Sorcerer · teleportation",
    "Kunishige’s oldest friend, Chihiro’s ride into town, and the man who left the Kamunabi when the smith went into hiding.",
    "p-shiba",
    "Decorative mark. Not official art.",
    [
        ("Age", "39"),
        ("Birthday", "October 15"),
        ("Sorcery", "Teleportation"),
        ("Former post", "Kamunabi; earlier Soga clan guardian"),
        ("Voiced by", "Jun Fukushima (voiced comic); Katsuyuki Konishi (anime)"),
    ],
    """
    <h2>Overview</h2>
    <p>Shiba is loud, childish on purpose, and one of the most dangerous sorcerers in the book. He grew up with Kunishige, guarded the Soga clan before the war, joined the Kamunabi when the island rose, and walked away after the smith disappeared. In the present he is Chihiro’s adult — the one who takes him to Cafe Haru Haru, the one who pulls him out of rooms he should not die in.</p>
    <p>His teleportation is the practical magic of the series: infiltration, extraction, civilian evacuation. Before the war he was already famous as a teenager. He trained under Ichiki with Azami. He is not a blade bearer. He does not need to be.</p>
    """,
    [("Chihiro", "chihiro.html"), ("Kamunabi", "../factions/index.html")],
)

character(
    "hakuri",
    "Hakuri Sazanami",
    "漣 伯理",
    "Sazanami clan · Storehouse",
    "The son the auction house threw away — and the only living Sazanami to hold both Isou and the Storehouse.",
    "p-hakuri",
    "Decorative mark. Not official art.",
    [
        ("Clan", "Sazanami (disowned)"),
        ("Sorcery", "Isou; Storehouse (Kura)"),
        ("Family", "Kyora (father); Soya, Tamaki, Enji, Tenri (siblings)"),
        ("Role", "Registers people and spiritually charged objects; transports blades"),
    ],
    """
    <h2>Overview</h2>
    <p>Hakuri was beaten into believing he had no talent. The clan’s Isou — a burial-force technique — would not answer him because he was scattering his own spirit energy. When he chose Chihiro over the Rakuzaichi, the seal on that self-doubt broke. He is one of two people in clan history to wield both Isou and the Storehouse, the subspace the family head uses to warehouse loot and human beings.</p>
    <h2>Storehouse</h2>
    <p>Hakuri can register a person and their charged possessions, then move blades across the country. That single trick is why the Kamunabi bother to keep Chihiro: the bearers can be un-armed and re-armed without a siege. It is also why the Hishaku hunt him. The auction was a building. Hakuri is the building that walks.</p>
    """,
    [("Kyora", "kyora.html"), ("Rakuzaichi Arc", "../arcs/rakuzaichi.html")],
)

character(
    "char",
    "Char Kyonagi",
    "鏡凪 シャル",
    "Kyonagi clan",
    "The last child of a clan hunted for the way their flesh heals — Sojo’s experiment, Chihiro’s first rescue that was not a sword.",
    "p-char",
    "Decorative mark. Not official art.",
    [
        ("Birthday", "December 21"),
        ("Clan", "Kyonagi (last)"),
        ("Ability", "Regeneration; can heal others"),
        ("Held by", "Sojo (formerly); Chihiro’s group"),
    ],
    """
    <h2>Overview</h2>
    <p>Sojo wanted Datenseki that did not explode. He thought Kyonagi cells were the stabilizer Kunishige’s eyes had been. Char and her mother were inventory. Chihiro’s decision to keep her — against Azami’s advice to avoid Sojo — is the first time the revenge plot has to share the page with a living person who is not a combatant.</p>
    <p>She can close her own wounds and other people’s. That is why everyone wants her and why the archive lists her with the fighters.</p>
    """,
    [("Sojo", "sojo.html"), ("Vs. Sojo Arc", "../arcs/vs-sojo.html")],
)

character(
    "iori",
    "Iori Samura",
    "座村 イヲリ",
    "Iai White Purity Style",
    "A student who was told her father was a story. The seal failed the moment she chose to protect someone.",
    "p-iori",
    "Decorative mark. Not official art.",
    [
        ("Father", '<a href="samura.html">Seiichi Samura</a>'),
        ("Style", "Iai White Purity Style (eyes closed in combat)"),
        ("Present blade", '<span class="spoiler">Tobimune, after Samura’s death</span>'),
    ],
    """
    <h2>Overview</h2>
    <p>After Iori’s mother died, Samura tried to be a parent and a war criminal in the same house. When Yura came to the door with the truth of the Malediction, Samura had the Masumi erase him from her memory and sent her away. The spell frayed because she still loved him. It broke when she moved to shield a classmate — Iai, eyes shut, the way the style is supposed to be used.</p>
    <p>The Kyoto Bloodshed Hotel is where she decides she wants the memories. Everything after that is a daughter walking toward a man who already spent himself trying to keep her out of the ledger.</p>
    """,
    [("Samura", "samura.html"), ("Sword Bearer Arc", "../arcs/sword-bearer.html")],
)

character(
    "hiyuki",
    "Hiyuki Kagari",
    "香刈 緋雪",
    "Kamunabi elite",
    "The organization’s sharpest fighter without an Enchanted Blade — Flame Bone of the Starving, short temper, actual principles.",
    "p-hiyuki",
    "Decorative mark. Not official art.",
    [
        ("Organization", "Kamunabi"),
        ("Sorcery", "Flame Bone of the Starving (Gasha no Enkotsu)"),
        ("Partner", "Tafuku Mihara (domain sorcery)"),
        ("Note", "Said to rival an Enchanted Blade"),
    ],
    """
    <h2>Overview</h2>
    <p>Hiyuki is assigned to problems the Kamunabi cannot file. Flame Bone is a learned, monstrous sorcery that lets her stand in front of Shinuchi without becoming a footnote. She starts as Chihiro’s obstacle — the state with a personality — and becomes the reason the Rakuzaichi actually ends: she will burn the auction if the alternative is leaving people in the Storehouse.</p>
    <p>Tafuku’s calm is the other half of the act. Together they are the Kamunabi as it wishes it looked.</p>
    """,
    [("Factions", "../factions/index.html"), ("Rakuzaichi Arc", "../arcs/rakuzaichi.html")],
)

character(
    "sojo",
    "Genichi Sojo",
    "双城 厳一",
    "Enchanted Blade bearer · Cloud Gouger",
    "Underworld arms dealer who loved Kunishige’s work the way a thief loves a lock. The first rival who understood the blades as craft.",
    "p-sojo",
    "Decorative mark. Not official art.",
    [
        ("Age", "30"),
        ("Birthday", "June 6"),
        ("Blade", '<a href="../blades/cloud-gouger.html">Cloud Gouger (Kuregumo)</a>'),
        ("Techniques used", "Mei, cloaked Mei, Yui, Kou"),
        ("Fate", "Killed in the Datenseki backlash after Enten bisected Cloud Gouger"),
    ],
    """
    <h2>Overview</h2>
    <p>Sojo is not Hishaku. He is a customer. They handed him Cloud Gouger in early October; he used it to chase Char and to chase the idea that he could mass-produce Kunishige. He is cruel, curious, and sincere about the smith in a way Chihiro recognizes with disgust.</p>
    <h2>Fight</h2>
    <p>The Anti-Cloud Gouger Special Forces die around him. Chihiro loses an arm and still reaches the True Realm first. Enten cuts Cloud Gouger in half — the first time one of Kunishige’s wartime swords is shown to be mortal. Sojo fuses with unstable Datenseki rather than admit the experiment failed. The compound goes with him.</p>
    <p>Chihiro keeps the pieces. Even a dead blade can still spend a few charges of Mei.</p>
    """,
    [("Cloud Gouger", "../blades/cloud-gouger.html"), ("Vs. Sojo Arc", "../arcs/vs-sojo.html")],
)

character(
    "yura",
    "Yura",
    "幽",
    "Hishaku · leader",
    "The man who planned Kunishige’s murder so he could one day hold Magatsumi. Chihiro’s named target.",
    "p-yura",
    "Decorative mark. Not official art.",
    [
        ("Organization", "Hishaku (leader of ten)"),
        ("Marks", "Flame-emblem tattoo; fire-gate teleportation"),
        ("Goal", "Wield the Shinuchi; later, an alliance with its true bearer"),
        ("Fate", '<span class="spoiler">Allows Akemura to possess him after Chihiro wounds him</span>'),
    ],
    """
    <h2>Overview</h2>
    <p>Yura is calm enough to bet his life on a coin, convinced the result is already blessed. He raided the Rokuhira house, sold Cloud Gouger to Sojo, put Magatsumi on the Rakuzaichi block after cracking its seal, and signed a private contract with Samura. He wanted the Sword Master dead so the Lifelong Contract would open. Then he spoke to Akemura and changed the math.</p>
    <p>He is the Hishaku as a mind: not the loudest killer in the set of ten, the one who decides which blade goes to which monster.</p>
    """,
    [("Hishaku", "../factions/index.html"), ("Magatsumi", "../blades/magatsumi.html")],
)

character(
    "samura",
    "Seiichi Samura",
    "座村 清市",
    "Enchanted Blade bearer · Tobimune",
    "Blind swordsman, fastest of the six, a Buddhist who tried to kill the war by killing the men who won it.",
    "p-samura",
    "Decorative mark. Not official art.",
    [
        ("Blade", '<a href="../blades/tobimune.html">Tobimune</a>'),
        ("Style", "Iai White Purity Style"),
        ("Family", '<a href="iori.html">Iori Samura</a> (daughter)'),
        ("Fate", '<span class="spoiler">Dies holding Magatsumi back so Chihiro can leave; Tobimune passes to Iori</span>'),
    ],
    """
    <h2>Overview</h2>
    <p>Samura took his own eyes to sharpen everything else. He fights by sound, sheathed, at a speed the rest of the bearers treat as weather. Tobimune was built as a support sword: feathers, an owl over the country, flames that heal the wielder and burn everyone else. After the war he taught those flames to raise the dead.</p>
    <h2>The pact</h2>
    <p>Guilt over the Malediction puts him in a room with Yura. The deal looks like traitor-work: kill the other bearers, return the blades, kill the Sword Master, then die with the Hishaku. What he actually does to Uruha is a contract-breaking mercy. He erases himself from Iori because he knows what “hero” meant on the island.</p>
    <p>Chihiro beats him with purpose, not pace. Samura heals his eyes, sees his daughter, and spends the last of his life on Magatsumi. That is the Iai style as ethics: one cut, no extra motion.</p>
    """,
    [("Tobimune", "../blades/tobimune.html"), ("Iori", "iori.html"), ("Analysis", "../analysis/malediction.html")],
)

character(
    "uruha",
    "Yoji Uruha",
    "漆羽 洋児",
    "Enchanted Blade bearer · Kumeyuri",
    "War prodigy who treated Kunishige like a vocation. He loses the will to live, then finds the son, then finds out death was a technique.",
    "p-uruha",
    "Decorative mark. Not official art.",
    [
        ("Blade", '<a href="../blades/kumeyuri.html">Kumeyuri</a> (Seitei War)'),
        ("Style", "Iai White Purity Style (mastered by 16)"),
        ("Innate sorcery", "Crimson Recital (returns when the contract breaks)"),
        ("Sanso", "Kokugoku Hot Spring"),
    ],
    """
    <h2>Overview</h2>
    <p>Uruha was chosen young and never recovered from being chosen. Kunishige’s death empties him; Chihiro’s existence refills the oath. The Hishaku send Hiruhiko and Datenseki infantry at the train. Samura “kills” him at Senkutsuji — Suzaku, not betrayal — so the Lifelong Contract dies and Kumeyuri can be pulled off the board. Uruha wakes in a morgue with his old sorcery coming back and walks into the Kamunabi raid to keep Hakuri alive.</p>
    """,
    [("Kumeyuri", "../blades/kumeyuri.html"), ("Samura", "samura.html")],
)

character(
    "akemura",
    "Akemura Soga",
    "曽我 明無良",
    "Sword Master · Magatsumi",
    "Kunishige’s most trusted friend, Chihiro’s uncle, and the author of the atrocity the Kamunabi filed as victory.",
    "p-akemura",
    "Decorative mark. Not official art.",
    [
        ("Title", "Sword Master (Kensei)"),
        ("Blade", '<a href="../blades/magatsumi.html">Magatsumi / Shinuchi</a>'),
        ("Clan", "Soga (Chiaki’s younger brother)"),
        ("War crime", "Malediction — ~200,000 civilians after the treaty"),
    ],
    """
    <h2>Overview</h2>
    <p>Akemura is not a berserker who lost the plot. He is a patriot who decided the island should not exist. Magatsumi is the only Enchanted Blade without a tidy three-technique kit and the only one that can overwrite another body. After the flowers finished their work he handed himself in. The other bearers could not stop him. The Kamunabi built a myth instead of a trial.</p>
    <p>His life is tied to the other five wartime contracts: if he dies, they die. That knot is why nobody simply executes the monster in the basement. When Yura finally reaches the cell, Akemura is still lucid. He takes the offered body and goes back to work.</p>
    """,
    [("Magatsumi", "../blades/magatsumi.html"), ("The Malediction", "../analysis/malediction.html")],
)

character(
    "kyora",
    "Kyora Sazanami",
    "漣 京羅",
    "Sazanami clan head",
    "Eleventh auctioneer of the Rakuzaichi. He will spend children to keep a two-hundred-year market open.",
    "p-kyora",
    "Decorative mark. Not official art.",
    [
        ("Title", "11th head of the Sazanami"),
        ("Sorcery", "Storehouse (environmental control inside the Kura)"),
        ("Children", "Soya, Tamaki, Enji, Hakuri, Tenri"),
        ("Fate", "Dies resisting Magatsumi’s possession after spending Shinuchi"),
    ],
    """
    <h2>Overview</h2>
    <p>Kyora is the Rakuzaichi in a person: polite, absolute, certain that the auction is civilization. Hakuri is a failed product until the boy becomes a rival Storehouse. Tenri dies on Datenseki trying to be useful. When Chihiro corners him in the collapsing subspace, Kyora unsheathes Magatsumi and almost becomes someone else. He dies as himself, which is the only kindness the book gives him — and he uses it to admit, too late, what he did to Hakuri.</p>
    """,
    [("Hakuri", "hakuri.html"), ("Rakuzaichi Arc", "../arcs/rakuzaichi.html")],
)

# ——— Blades ———
page(
    "blades/index.html",
    "Enchanted Blades",
    "The seven Enchanted Blades of Kagurabachi: Enten, Cloud Gouger, Magatsumi, Kumeyuri, Tobimune, and the two still unnamed in publication.",
    crumb("Enchanted Blades")
    + hero("Yōtō 妖刀", "Enchanted Blades", "妖刀", "Seven katana Kunishige cut from Datenseki. Six won a war. The seventh was made to finish them.")
    + """
    <article class="article">
      <p>An Enchanted Blade does not “cast” so much as overfill. Spirit energy becomes too large for the body and leaves as a shape — goldfish, clouds, flowers, feathers, oiran — that can be steered, seen through, and charged into the steel so the bearer can spend techniques while empty-handed. Most blades have three named techniques and a True Realm when the wielder’s intent locks with the sword. Magatsumi refuses the three-count.</p>
      <p><strong>Lifelong Contracts</strong> (Meimetsu Keiyaku) bind a blade to one nervous system. The bearer’s innate sorcery goes dark until the contract is cut. Magatsumi’s contract is the master key: if Akemura dies, the other five wartime bearers die with him. Destroy Magatsumi and the knot comes apart.</p>
    </article>
    <div class="grid">
      <a class="card" href="enten.html"><div class="card-art blade-enten"></div><div class="card-body"><span class="tag">Seventh</span><h3>Enten 淵天</h3><p>Chihiro. Made to destroy the others.</p></div></a>
      <a class="card" href="cloud-gouger.html"><div class="card-art blade-kuregumo"></div><div class="card-body"><span class="tag">Kuregumo</span><h3>Cloud Gouger 刳雲</h3><p>Ibuki → Sojo → Chihiro. Bisected.</p></div></a>
      <a class="card" href="magatsumi.html"><div class="card-art blade-magatsumi"></div><div class="card-body"><span class="tag">Shinuchi</span><h3>Magatsumi 勾罪</h3><p>Akemura. The strongest, and the leak.</p></div></a>
      <a class="card" href="kumeyuri.html"><div class="card-art blade-kumeyuri"></div><div class="card-body"><span class="tag">Fifth forged</span><h3>Kumeyuri 酌揺</h3><p>Uruha → Hiruhiko. Hallucination and play.</p></div></a>
      <a class="card" href="tobimune.html"><div class="card-art blade-tobimune"></div><div class="card-body"><span class="tag">Support blade</span><h3>Tobimune 飛宗</h3><p>Samura → Iori. Feathers and black fire.</p></div></a>
    </div>
    <p class="note">Two wartime blades remain unnamed in the chapters collected so far. Subaru Urita is a surviving bearer; one portrait in the war ensemble is still unlabeled. This archive will not invent names.</p>
    """,
)


def blade_page(slug, name, jp, lede, bclass, rows, article):
    body = (
        crumb(("Blades", "index.html"), name)
        + hero("Enchanted Blade", name, jp, lede)
        + f"""<div class="layout">
      <article class="article">{article}</article>
      {infobox(name, jp, bclass, "Color field for this blade — not official steel.", rows)}
    </div>"""
    )
    page(f"blades/{slug}.html", name, lede, body)


blade_page(
    "enten",
    "Enten",
    "淵天",
    "The seventh blade. Forged after the war, with Chihiro, to confront the other six — especially Magatsumi.",
    "blade-enten",
    [
        ("Bearer", "Chihiro Rokuhira"),
        ("Manifestation", "Water droplets; three goldfish"),
        ("Kuro 涅", "Black fish. Flying slash; Kuro: Shred"),
        ("Aka 猩", "Red fish. Absorb, then return an attack"),
        ("Nishiki 錦", "Tricolor cloak. Speed, power, ailment resist"),
        ("Status", '<span class="spoiler">Bisected by Magatsumi; pieces held, Suzaku-black stalled the rot</span>'),
    ],
    """
    <h2>Purpose</h2>
    <p>Kunishige could not smash the wartime blades. Enten is the tool he built instead: a sword whose True Realm is the death of Magatsumi. Nishiki’s cloak shrugging off Spider and vitality-drain is not a random buff. It is the design brief.</p>
    <h2>The fish</h2>
    <p>Kuro, Aka, and Nishiki are named for the three goldfish in the Rokuhira house. Kuro paints arm and edge in black water and throws a cut the size of the fish you called. Shred spends more spirit to throw many small ones. Aka drinks a technique and lets you speak it back for a short window. Nishiki is the household made into armor.</p>
    <blockquote class="cite">“In a revenge tale where the protagonist’s clothes are stained black with blood, the colors white, black, and red match well.”<footer>Takeru Hokazono, on why the fish — and the palette — are not koi</footer></blockquote>
    """,
)

blade_page(
    "cloud-gouger",
    "Cloud Gouger",
    "刳雲 · Kuregumo",
    "Lightning, ice, and weather in one katana. First of the stolen six to appear; first to die.",
    "blade-kuregumo",
    [
        ("War bearer", "Ibuki Misaka (killed by Hokuto)"),
        ("Later bearers", "Genichi Sojo; Chihiro (dying contract)"),
        ("Mei 鳴", "Lightning bolt; charge delay; cloaked Mei; Mei: Shred"),
        ("Yui 結", "Ice, instant cages and constructs"),
        ("Kou 降", "Water or mist; conducts Mei, feeds Yui"),
        ("Status", "Bisected by Enten; residual energy spent; fragments retained"),
    ],
    """
    <h2>Overview</h2>
    <p>Cloud Gouger leaves the body as clouds and cloud-dragons. Sojo’s cloaked Mei is the first time the series shows an extension: instead of throwing the lightning, wear it. Chihiro’s last use, Mei: Shred, turns the lightning black because the blade is dying — the same “dark power” rule that later paints Suzaku.</p>
    <p>Kou exists to make the other two worse. Water is a wire. Ice is a larger Yui. It is a craftsman’s weather kit, which is why Sojo loved it and why Chihiro refused to let the last inch of it vanish unused.</p>
    """,
)

blade_page(
    "magatsumi",
    "Magatsumi",
    "勾罪 · Shinuchi 真打",
    "The masterpiece. Flowers, insects, and a technique that emptied an island after the war was already over.",
    "blade-magatsumi",
    [
        ("Bearer", "Akemura Soga"),
        ("Proxies", "Kyora Sazanami; Yura (possession path)"),
        ("Manifestation", "Black drip, flower fields, butterflies"),
        ("Named arts", "Spider, Dragonfly, Centipede, Butterfly, Bee"),
        ("Extension", "Malediction (Kodoku)"),
        ("Unique", "No three-technique limit; can bypass its own contract"),
    ],
    """
    <h2>Overview</h2>
    <p>Once Magatsumi entered the field, Japan could walk onto the island. That is the official sentence. The unofficial one is Malediction: Akemura’s bloodlust aimed the blade’s life-drain at an entire civilian population and grew flowers out of 200,000 people after a treaty existed.</p>
    <p>The steel weeps black, darkens ground, and blooms. Touch the field and branches find your mouth. The wielder eats what the field takes. Spider pins. Dragonfly and Bee are directional disasters. Centipede is omnidirectional. Butterfly cuts a building and keeps going. Anyone who holds the sheathed blade starts becoming Akemura.</p>
    """,
)

blade_page(
    "kumeyuri",
    "Kumeyuri",
    "酌揺",
    "A blade that throws a banquet and then plays with the room. Spirit energy as faceless oiran.",
    "blade-kumeyuri",
    [
        ("War bearer", "Yoji Uruha"),
        ("Later", "Hiruhiko (after Uruha’s false death)"),
        ("Banquet 宴", "Sense-killing hallucination; ears can be reinforced"),
        ("Play 遊", "Move objects; respect makes the telekinesis smoother"),
        ("Extension", "Destructive Play — Hiruhiko’s contempt as a demolition tool"),
    ],
    """
    <h2>Overview</h2>
    <p>Kumeyuri is theater. Banquet takes the senses; Play takes the set. Hiruhiko, who does not love objects, discovers the extension: if Play is respect, then contempt is a wrecking ball. The Kyoto Bloodshed Hotel loses its upper floors to that reading. Samura takes the blade off him. Ro of the Masumi recovers it.</p>
    """,
)

blade_page(
    "tobimune",
    "Tobimune",
    "飛宗",
    "Feathers, a national owl, and flames that cannot decide if they are a hospital or a crematorium.",
    "blade-tobimune",
    [
        ("War bearer", "Seiichi Samura"),
        ("Present", '<span class="spoiler">Iori Samura</span>'),
        ("Crow 鴉", "Swap with a feather; External Crow moves other people"),
        ("Owl 梟", "Giant eyes; range versus resolution trade-off"),
        ("Suzaku 雀", "Heal self, burn others; External Suzaku heals the world; black flames at the brink"),
    ],
    """
    <h2>Overview</h2>
    <p>Chihiro says Tobimune was forged for support. Crow is a reposition. Owl is reconnaissance at the scale of a country — Samura hangs it in the sky and listens for Enchanted Blade noise. Suzaku began as selfish fire and became resurrection: Uruha, Chihiro, a hotel Hiruhiko had already started to unmake. Black Suzaku is the life-for-power rule with the lights off. It is strong enough to argue with Malediction.</p>
    """,
)

print("core encyclopedia done")
