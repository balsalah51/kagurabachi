#!/usr/bin/env python3
"""Insert existing artwork and a brief article class on thin encyclopedia rooms.

Idempotent. Uses only files already in assets/. Does not invent panels or jackets.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path("/workspace")

# (src relative to the page folder, alt, caption)
SHOTS: dict[str, tuple[str, str, str]] = {
    "manga/chapter-4.html": (
        "../assets/panels/ch001.png",
        "Kagurabachi chapter 4: the workshop still in the first week’s ink",
        "Sorcery arrives as household work. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-5.html": (
        "../assets/covers/jp-vol1.webp",
        "Kagurabachi Volume 1 Japanese jacket",
        "Volume 1 still has the meal in it. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-7.html": (
        "../assets/panels/ch002.png",
        "Kagurabachi early chapter art from the first volume",
        "The underworld starts answering. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-19.html": (
        "../assets/panels/ch019.png",
        "Kagurabachi chapter 19, Knight of Darkness",
        "Volume 3’s title arrives with Hiyuki. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-20.html": (
        "../assets/portraits/hiyuki.webp",
        "Hiyuki Kagari",
        "The Kamunabi’s pointed end. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-32.html": (
        "../assets/panels/Wall_of_Trees.png",
        "A wall of trees in Kagurabachi",
        "The auction house starts answering Hakuri. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-41.html": (
        "../assets/portraits/kyora.webp",
        "Kyora Sazanami",
        "The head of the house spends the building. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-45.html": (
        "../assets/portraits/hakuri.webp",
        "Hakuri Sazanami",
        "What comes next is a person, not a vault. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-48.html": (
        "../assets/portraits/uruha.webp",
        "Yoji Uruha",
        "The Steam Squad is named so the graves can be. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-56.html": (
        "../assets/panels/ch056.png",
        "Kagurabachi chapter 56, Daybreak",
        "夜更け, printed as Daybreak. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-59.html": (
        "../assets/portraits/samura.webp",
        "Seiichi Samura",
        "The lights go out on purpose. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-66.html": (
        "../assets/portraits/iori.webp",
        "Iori Samura",
        "A name the house tried to keep off the ledger. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-75.html": (
        "../assets/portraits/hiruhiko.webp",
        "Hiruhiko",
        "Illusion as a Hishaku brief. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-80.html": (
        "../assets/portraits/hiruhiko.webp",
        "Hiruhiko",
        "A room that is not on the hotel map. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-92.html": (
        "../assets/portraits/samura.webp",
        "Seiichi Samura",
        "The swordsmen, named as a class. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-97.html": (
        "../assets/portraits/azami.webp",
        "Azami",
        "Vessel is a job title inside the barrier. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-99.html": (
        "../assets/panels/tobimune.webp",
        "Tobimune",
        "Strongest, in quotes, because the book is arguing. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-105.html": (
        "../assets/portraits/akemura.webp",
        "Akemura",
        "A body that used to have another name. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-106.html": (
        "../assets/portraits/akemura.webp",
        "Akemura",
        "Karma as a corridor, not a slogan. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-110.html": (
        "../assets/portraits/chihiro.webp",
        "Chihiro Rokuhira",
        "As a swordsman, after the other titles. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-113.html": (
        "../assets/panels/ch113.png",
        "Kagurabachi chapter 113, Rock",
        "Rock. The title is the brief. Full chapter: VIZ / MANGA Plus.",
    ),
    "manga/chapter-114.html": (
        "../assets/portraits/kunishige.webp",
        "Kunishige Rokuhira",
        "The smith as a chapter title. Full chapter: VIZ / MANGA Plus.",
    ),
    "world/kuro.html": (
        "../assets/panels/enten.webp",
        "Enten",
        "Kuro is the black fish, the first word. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/aka.html": (
        "../assets/panels/enten.webp",
        "Enten",
        "Aka drinks a technique and lets you speak it back. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/nishiki.html": (
        "../assets/panels/enten.webp",
        "Enten",
        "The tricolor cloak is Enten’s purpose showing through. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/mei.html": (
        "../assets/panels/Sojo_holding_Cloud_Gouger.png",
        "Sojo holding Cloud Gouger",
        "Lightning with a charge delay. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/yui.html": (
        "../assets/panels/Sojo_holding_Cloud_Gouger.png",
        "Sojo holding Cloud Gouger",
        "Ice cages, amount variable with the point. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/kou.html": (
        "../assets/panels/Sojo_holding_Cloud_Gouger.png",
        "Sojo holding Cloud Gouger",
        "Water or mist: the weather that makes Mei and Yui worse. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/banquet-art.html": (
        "../assets/panels/kumeyuri.webp",
        "Kumeyuri",
        "Banquet is hallucination. Reinforced ears mitigate. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/crow.html": (
        "../assets/panels/tobimune.webp",
        "Tobimune",
        "Swap with a feather already placed. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/suzaku.html": (
        "../assets/panels/tobimune.webp",
        "Tobimune",
        "Flames that heal the bearer and, later, keep the person. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/isou.html": (
        "../assets/portraits/hakuri.webp",
        "Hakuri Sazanami",
        "Sazanami burial-force, inherited next to the Storehouse. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/coin.html": (
        "../assets/portraits/azami.webp",
        "Azami",
        "A clinic stimulant spent as an executioner’s art. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/kurotsuchi.html": (
        "../assets/covers/jp-vol11.webp",
        "Kagurabachi Volume 11 Japanese jacket",
        "Hiroto’s directional gravity. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/sumika.html": (
        "../assets/covers/jp-vol11.webp",
        "Kagurabachi Volume 11 Japanese jacket",
        "Ariu’s insect art, printed as 栖. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/akuu.html": (
        "../assets/official/jp-ogp.jpg",
        "Official Kagurabachi key art",
        "Mashiro’s air pressure, printed as 空亜. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/warriors-path.html": (
        "../assets/portraits/azami.webp",
        "Kamunabi officer Azami",
        "Kudo’s 死闘, spent so Hakuri can walk. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/jikai.html": (
        "../assets/panels/Sojo_holding_Cloud_Gouger.png",
        "Sojo holding Cloud Gouger",
        "Hagiwara’s magnetism against the weather sword. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/vessel.html": (
        "../assets/portraits/yura.webp",
        "Yura",
        "Yukisada as 受け皿 inside the HQ barrier. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/tamahagane.html": (
        "../assets/covers/jp-vol1.webp",
        "Kagurabachi Volume 1 Japanese jacket",
        "Datenseki allowed to be steel. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/briefcase.html": (
        "../assets/portraits/sojo.webp",
        "Genichi Sojo",
        "Semi-stable Datenseki in a case, not a myth. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/handover.html": (
        "../assets/official/jp-ogp.jpg",
        "Official Kagurabachi key art",
        "April 1, Irishima’s beach. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/pine-sorcery.html": (
        "../assets/covers/jp-vol3.webp",
        "Kagurabachi Volume 3 Japanese jacket",
        "Hired weather, not Hishaku. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/counter-sorcery-army.html": (
        "../assets/portraits/azami.webp",
        "Azami",
        "The bureau before the Kamunabi rename. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/anesthesia.html": (
        "../assets/covers/jp-vol11.webp",
        "Kagurabachi Volume 11 Japanese jacket",
        "Soga forbidden kindness in chapter 130. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/teleport.html": (
        "../assets/portraits/shiba.webp",
        "Togo Shiba",
        "Extraction without a contract. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/duel-domain.html": (
        "../assets/portraits/samura.webp",
        "Seiichi Samura",
        "Tafuku’s two-person match. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/gansui.html": (
        "../assets/covers/jp-vol2.webp",
        "Kagurabachi Volume 2 Japanese jacket",
        "Harima’s stone battlefield, printed as 岩垂. Official chapters: VIZ / MANGA Plus.",
    ),
    "world/iron-body.html": (
        "../assets/portraits/sojo.webp",
        "Genichi Sojo",
        "Kugara’s ACG art against the weather sword. Official chapters: VIZ / MANGA Plus.",
    ),
    "analysis/hakuri.html": (
        "../assets/portraits/hakuri.webp",
        "Hakuri Sazanami",
        "The architecture walks out of the clan. Official chapters: VIZ / MANGA Plus.",
    ),
    "analysis/suzaku.html": (
        "../assets/panels/tobimune.webp",
        "Tobimune",
        "The cut that keeps the person. Official chapters: VIZ / MANGA Plus.",
    ),
    "analysis/foresight.html": (
        "../assets/official/jp-ogp.jpg",
        "Official Kagurabachi key art",
        "Foresight as a national office. Official chapters: VIZ / MANGA Plus.",
    ),
    "fun/enten-oneshot.html": (
        "../assets/fun/enten.png",
        "Tezuka Award one-shot Enten, not 淵天",
        "炎天 is a different word. The bowl came later.",
    ),
    "fun/circulation.html": (
        "../assets/official/comics1.png",
        "Kagurabachi Jump Comics announcement",
        "350,000 to 4 million. The meme predicted the opposite.",
    ),
    "manga/volume-12.html": (
        "../assets/covers/jp-vol11.webp",
        "Kagurabachi Volume 11 Japanese jacket",
        "Eleven jackets exist. Volume 12’s has not been announced.",
    ),
}

BRIEF_ONLY = set(SHOTS)


def figure_html(src: str, alt: str, caption: str) -> str:
    return (
        f'<figure class="shot">\n'
        f'      <img src="{src}" alt="{alt}">\n'
        f'      <figcaption>{caption}</figcaption>\n'
        f'    </figure>\n'
    )


def mark_brief(html: str) -> str:
    if 'class="article brief"' in html:
        return html
    return html.replace('<article class="article">', '<article class="article brief">', 1)


def insert_shot(html: str, src: str, alt: str, caption: str) -> str:
    if '<figure class="shot">' in html:
        return html
    block = figure_html(src, alt, caption)
    for needle in ("</header>\n<article", "</header>\n\n<article", "</div></header>\n<article"):
        if needle in html:
            return html.replace(needle, needle.replace("<article", block + "<article"), 1)
    return html.replace("<article class=", block + "<article class=", 1)


def main() -> None:
    n_fig = 0
    n_brief = 0
    for rel, (src, alt, caption) in SHOTS.items():
        path = ROOT / rel
        if not path.is_file():
            print("missing", rel)
            continue
        asset = (path.parent / src).resolve()
        if not asset.is_file():
            print("missing asset", rel, src)
            continue
        html = path.read_text(encoding="utf-8")
        before = html
        html = insert_shot(html, src, alt, caption)
        html = mark_brief(html)
        if html != before:
            path.write_text(html, encoding="utf-8")
            if '<figure class="shot">' in html and '<figure class="shot">' not in before:
                n_fig += 1
            if 'class="article brief"' in html and 'class="article brief"' not in before:
                n_brief += 1
            print("polish", rel)
        else:
            print("skip", rel)
    print(f"figures {n_fig} brief {n_brief}")


if __name__ == "__main__":
    main()
