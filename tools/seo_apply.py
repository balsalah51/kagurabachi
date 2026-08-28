#!/usr/bin/env python3
"""Apply on-page SEO, related links, alt text, robots, and sitemaps.

Idempotent: safe to re-run. Writes robots.txt, sitemap.xml, sitemap-images.xml,
sitemap.html, search.html, the search index, OpenSearch, and the web manifest,
and patches every HTML page with canonical URLs, Open Graph, Twitter cards,
JSON-LD (including SearchAction for Google), related-page nav, and descriptive
image alt text.
"""
from __future__ import annotations

import html as htmlmod
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path("/workspace")
SITE = "https://kagurabachi.org"
DEFAULT_OG = f"{SITE}/assets/covers/teaser-og.jpg"
FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+JP:wght@400;500;600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap"

TITLE_OVERRIDES = {
    "index.html": "Kagurabachi Encyclopedia | Characters, Enchanted Blades &amp; Manga Guide",
    "about.html": "About This Kagurabachi Encyclopedia",
    "privacy.html": "Privacy Policy · Kagurabachi Archive",
    "404.html": "Page not found · Kagurabachi Archive",
    "characters/index.html": "Kagurabachi Characters | Chihiro, Blade Bearers, Hishaku &amp; Kamunabi",
    "blades/index.html": "Enchanted Blades in Kagurabachi | Enten, Cloud Gouger, Magatsumi",
    "manga/index.html": "Kagurabachi Manga Guide | Volumes, Chapters, Covers",
    "manga/synopses.html": "Kagurabachi Volume Synopses | All 11 Jump Comics Spines",
    "manga/chapters.html": "Kagurabachi Chapter Index | Titles from Mission to Ironworks",
    "manga/volumes.html": "Kagurabachi Volume Guide | Japanese &amp; English ISBNs",
    "manga/covers.html": "Kagurabachi Cover Studies | Eleven Japanese Jackets",
    "manga/color-pages.html": "Kagurabachi Color Pages | Jump Openings &amp; Pulls",
    "manga/part-2.html": "Kagurabachi Part 2 | Princess, Irishima Talks, Ironworks",
    "manga/publication.html": "Kagurabachi Publication Record | Circulation, Awards, Anime",
    "arcs/index.html": "Kagurabachi Story Arcs | Vs. Sojo, Rakuzaichi, Seitei War",
    "analysis/index.html": "Kagurabachi Essays | Enten, Malediction, Revenge",
    "guide/index.html": "Kagurabachi Beginner Guide | Series, Premise, Blades, Story",
    "fun/index.html": "Fun of Kagurabachi | Goldfish, Fandom, Sunday Board",
    "world/index.html": "Kagurabachi World &amp; Timeline | Irishima, Datenseki, Sorcery",
    "factions/index.html": "Kagurabachi Factions | Kamunabi, Hishaku, Sazanami, Soga",
    "collectibles/index.html": "Kagurabachi Collectibles | Volumes, ISBNs, Merch Notes",
    "collectibles/shop.html": "Where to Buy Kagurabachi Volumes &amp; Official Merch",
    "collectibles/union-arena.html": "Kagurabachi UNION ARENA Cards | UE16BT Set Gallery",
    "media/index.html": "Kagurabachi Theories &amp; Videos | Official Trailers First",
    "media/anime.html": "Kagurabachi Anime | Cypic, April 2027 Countdown",
    "media/staff.html": "Kagurabachi Staff | Hokazono, Cypic, Takeuchi, Sasaki, Voices",
    "media/adaptations.html": "Kagurabachi Adaptations | Manga, Voiced Comic, Anime, UNION ARENA",
    "world/register.html": "Kagurabachi Name Register | Every Named Figure Through Ch. 129",
    "world/techniques.html": "Kagurabachi Technique Catalog | Enchanted Blade Kit &amp; Innate Arts",
    "world/glossary.html": "Kagurabachi Glossary | Enchanted Blades, Contracts, True Realm",
    "world/battles.html": "Kagurabachi Battles | Chihiro vs Sojo, Rakuzaichi, Hotel",
    "world/objects.html": "Kagurabachi Objects | Bowl, Datenseki, Storehouse, Contracts",
    "world/birthdays.html": "Kagurabachi Birthdays | Chihiro, Kunishige, Shiba, Sojo, Char",
    "world/lineage.html": "Kagurabachi Lineage | Rokuhira, Soga, Sazanami, Kyonagi",
    "world/symbols.html": "Kagurabachi Symbols | Goldfish, Hishaku Flame, Magatsumi Flowers",
    "sitemap.html": "Site map · Kagurabachi Archive",
    "faq.html": "Kagurabachi FAQ | Anime Date, How to Read, Wiki Answers",
    "search.html": "Search the Kagurabachi Encyclopedia | Characters, Blades, Arcs",
}

DESC_OVERRIDES = {
    "about.html": "What Kagurabachi.org is: an independent encyclopedia for Takeru Hokazono’s manga, with characters, Enchanted Blades, volumes, and essays.",
    "404.html": "This address is missing. Browse the Kagurabachi encyclopedia: characters, volumes, Sunday board, and the workshop.",
    "arcs/vs-sojo.html": "Kagurabachi Vs. Sojo arc (chapters 1–18): Char, Cloud Gouger, True Realm, and the first wartime Enchanted Blade to die.",
    "arcs/rakuzaichi.html": "Kagurabachi Rakuzaichi arc (chapters 19–46): the 208th auction, Hakuri’s Storehouse, Shinuchi, and why the building has to live.",
    "arcs/sword-bearer.html": "Kagurabachi Sword Bearer Assassination arc (chapters 47–115): Uruha, Samura, Iori, Kasen’s leak, and the end of Part 1.",
    "arcs/seitei-war.html": "Kagurabachi Seitei War / Part 2 (chapter 116–): Irishima, Chiaki Soga, the talks, Datenseki, and the kiln on the page.",
    "analysis/enten-purpose.html": "Why Kunishige forged Enten after the Seitei War: a seventh blade built as a retraction. Its True Realm is Magatsumi’s death.",
    "factions/index.html": "Kagurabachi organizations: Kamunabi state sorcerers, the Hishaku ten, Sazanami auction house, Soga, Mikaboshi, and the Masumi.",
    "index.html": "Independent Kagurabachi encyclopedia since the first Jump issue: characters, Enchanted Blades, manga guide, volume synopses, and analysis.",
    "faq.html": "Kagurabachi FAQ: what the manga is, when the 2027 anime airs, where to read legally, Enchanted Blades, Chihiro, KB, UNION ARENA cards, and how this encyclopedia works as a wiki.",
    "search.html": "Search Kagurabachi.org: characters, Enchanted Blades, story arcs, volume synopses, and essays. Wiki-depth index for Takeru Hokazono’s manga.",
    "collectibles/union-arena.html": "Kagurabachi UNION ARENA set UE16BT: pictures of Chihiro, Hakuri, Shiba, and other popular cards, with a TCGPlayer partner door.",
    "world/battles.html": "Major Kagurabachi fights in print: Chihiro versus Sojo, the Rakuzaichi, Senkutsuji, the Kyoto hotel, Kamunabi HQ, and the Seitei War.",
    "world/objects.html": "Kagurabachi items in print: the goldfish bowl, Datenseki, Enchanted Blades, the Storehouse, Lifelong Contracts, and the Hishaku fire-gate.",
    "world/birthdays.html": "Known Kagurabachi birthdays: Chihiro August 11, Kunishige June 5, Togo Shiba October 15, Genichi Sojo June 6, Char Kyonagi December 21.",
    "world/lineage.html": "Kagurabachi families: Rokuhira smiths, Soga prophecy aristocracy, Sazanami auction house, Samura and Iori, Kyonagi, Mikaboshi.",
    "world/symbols.html": "Kagurabachi symbols: Enten’s goldfish, the Hishaku flame, Magatsumi flowers, Tobimune’s owl, Cloud Gouger’s storm, white-black-red.",
    "media/staff.html": "Kagurabachi credits: Takeru Hokazono, Cypic, Tetsuya Takeuchi, Keigo Sasaki, and the announced anime and voiced-comic voices.",
    "media/adaptations.html": "Kagurabachi adaptations: Weekly Shōnen Jump manga, the voiced comic, Cypic’s April 2027 anime, and the UNION ARENA card set.",
}

# Extra related chips keyed by repo-relative path. Merged with any existing related nav.
PAGE_RELATED: dict[str, list[tuple[str, str]]] = {
    "characters/chihiro.html": [
        ("../blades/enten.html", "Enten"),
        ("kunishige.html", "Kunishige"),
        ("shiba.html", "Shiba"),
        ("hakuri.html", "Hakuri"),
        ("char.html", "Char"),
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
        ("../analysis/enten-purpose.html", "What Enten was for"),
        ("../manga/part-2.html", "Part 2"),
    ],
    "characters/kunishige.html": [
        ("chihiro.html", "Chihiro"),
        ("chiaki.html", "Chiaki"),
        ("akemura.html", "Akemura"),
        ("../blades/enten.html", "Enten"),
        ("../blades/index.html", "Enchanted Blades"),
        ("../world/workshop.html", "Workshop"),
        ("../world/datenseki.html", "Datenseki"),
    ],
    "characters/shiba.html": [
        ("chihiro.html", "Chihiro"),
        ("kunishige.html", "Kunishige"),
        ("azami.html", "Azami"),
        ("hinao.html", "Hinao"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("../world/cafe.html", "Cafe Haru Haru"),
        ("mashiro.html", "Mashiro"),
    ],
    "characters/hakuri.html": [
        ("chihiro.html", "Chihiro"),
        ("kyora.html", "Kyora"),
        ("soya.html", "Soya"),
        ("../world/storehouse.html", "Storehouse"),
        ("../factions/sazanami.html", "Sazanami"),
        ("../arcs/rakuzaichi.html", "Rakuzaichi"),
        ("yukisada.html", "Yukisada"),
    ],
    "characters/char.html": [
        ("chihiro.html", "Chihiro"),
        ("sojo.html", "Sojo"),
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
        ("hinao.html", "Hinao"),
        ("madoka.html", "Madoka"),
        ("../world/cafe.html", "Cafe Haru Haru"),
    ],
    "characters/iori.html": [
        ("samura.html", "Samura"),
        ("chihiro.html", "Chihiro"),
        ("../blades/tobimune.html", "Tobimune"),
        ("../world/iai.html", "Iai White Purity"),
        ("../world/hotel.html", "Kyoto hotel"),
        ("ro.html", "Ro"),
        ("ikura.html", "Ikura"),
        ("../arcs/sword-bearer.html", "Sword Bearer"),
    ],
    "characters/chiaki.html": [
        ("kunishige.html", "Kunishige"),
        ("chihiro.html", "Chihiro"),
        ("akemura.html", "Akemura"),
        ("../factions/soga.html", "Soga"),
        ("../arcs/seitei-war.html", "Seitei War"),
        ("../manga/part-2.html", "Part 2"),
        ("../world/irishima.html", "Irishima"),
    ],
    "characters/samura.html": [
        ("../blades/tobimune.html", "Tobimune"),
        ("iori.html", "Iori"),
        ("uruha.html", "Uruha"),
        ("../world/iai.html", "Iai"),
        ("../analysis/owl.html", "Owl over Japan"),
        ("../analysis/malediction.html", "Malediction"),
        ("../factions/masumi.html", "Masumi"),
        ("../arcs/sword-bearer.html", "Sword Bearer"),
    ],
    "characters/uruha.html": [
        ("../blades/kumeyuri.html", "Kumeyuri"),
        ("samura.html", "Samura"),
        ("chihiro.html", "Chihiro"),
        ("hiruhiko.html", "Hiruhiko"),
        ("natsuki.html", "Natsuki"),
        ("../arcs/sword-bearer.html", "Sword Bearer"),
        ("../world/sanso.html", "Sanso"),
    ],
    "characters/akemura.html": [
        ("../blades/magatsumi.html", "Magatsumi"),
        ("../analysis/malediction.html", "Malediction"),
        ("chiaki.html", "Chiaki"),
        ("yura.html", "Yura"),
        ("../factions/soga.html", "Soga"),
        ("../arcs/seitei-war.html", "Seitei War"),
        ("kunishige.html", "Kunishige"),
    ],
    "characters/hiyuki.html": [
        ("../factions/kamunabi.html", "Kamunabi"),
        ("../arcs/rakuzaichi.html", "Rakuzaichi"),
        ("tafuku.html", "Tafuku"),
        ("chihiro.html", "Chihiro"),
        ("../analysis/flame-bone.html", "Flame Bone"),
        ("kyora.html", "Kyora"),
        ("hakuri.html", "Hakuri"),
    ],
    "characters/sojo.html": [
        ("../blades/cloud-gouger.html", "Cloud Gouger"),
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
        ("../analysis/sojo-fan.html", "Worst fan"),
        ("char.html", "Char"),
        ("yura.html", "Yura"),
        ("ibuki.html", "Ibuki"),
        ("chihiro.html", "Chihiro"),
        ("madoka.html", "Madoka"),
    ],
    "characters/yura.html": [
        ("../factions/hishaku.html", "Hishaku"),
        ("../blades/magatsumi.html", "Magatsumi"),
        ("hokuto.html", "Hokuto"),
        ("hiruhiko.html", "Hiruhiko"),
        ("toto.html", "Toto"),
        ("yukisada.html", "Yukisada"),
        ("kunishige.html", "Kunishige"),
        ("chihiro.html", "Chihiro"),
    ],
    "characters/kyora.html": [
        ("hakuri.html", "Hakuri"),
        ("../arcs/rakuzaichi.html", "Rakuzaichi"),
        ("../factions/sazanami.html", "Sazanami"),
        ("../blades/magatsumi.html", "Magatsumi"),
        ("../world/storehouse.html", "Storehouse"),
        ("tenri.html", "Tenri"),
        ("soya.html", "Soya"),
    ],
    "characters/hiruhiko.html": [
        ("../factions/hishaku.html", "Hishaku"),
        ("../blades/kumeyuri.html", "Kumeyuri"),
        ("../arcs/sword-bearer.html", "Sword Bearer"),
        ("../analysis/play.html", "Play"),
        ("kuguri.html", "Kuguri"),
        ("uruha.html", "Uruha"),
        ("../world/hotel.html", "Kyoto hotel"),
    ],
    "characters/azami.html": [
        ("../factions/kamunabi.html", "Kamunabi"),
        ("shiba.html", "Shiba"),
        ("ichiki.html", "Ichiki"),
        ("kasen.html", "Kasen"),
        ("chihiro.html", "Chihiro"),
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
    ],
    "blades/enten.html": [
        ("../characters/chihiro.html", "Chihiro"),
        ("../characters/kunishige.html", "Kunishige"),
        ("magatsumi.html", "Magatsumi"),
        ("cloud-gouger.html", "Cloud Gouger"),
        ("../analysis/enten-purpose.html", "Purpose essay"),
        ("../world/techniques.html", "Techniques"),
        ("../fun/goldfish.html", "Goldfish, not koi"),
        ("../fun/bowl.html", "The bowl"),
    ],
    "blades/cloud-gouger.html": [
        ("../characters/sojo.html", "Sojo"),
        ("../characters/ibuki.html", "Ibuki"),
        ("enten.html", "Enten"),
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
        ("../world/acg.html", "Anti-Cloud Gouger"),
        ("../world/techniques.html", "Techniques"),
        ("index.html", "All blades"),
    ],
    "blades/magatsumi.html": [
        ("../characters/akemura.html", "Akemura"),
        ("../characters/yura.html", "Yura"),
        ("enten.html", "Enten"),
        ("../analysis/malediction.html", "Malediction"),
        ("../world/contracts.html", "Contracts"),
        ("../arcs/seitei-war.html", "Seitei War"),
        ("index.html", "All blades"),
    ],
    "blades/kumeyuri.html": [
        ("../characters/uruha.html", "Uruha"),
        ("../characters/hiruhiko.html", "Hiruhiko"),
        ("../characters/natsuki.html", "Natsuki"),
        ("../analysis/play.html", "Play"),
        ("tobimune.html", "Tobimune"),
        ("../world/techniques.html", "Techniques"),
        ("index.html", "All blades"),
    ],
    "blades/tobimune.html": [
        ("../characters/samura.html", "Samura"),
        ("../characters/iori.html", "Iori"),
        ("../analysis/owl.html", "Owl over Japan"),
        ("kumeyuri.html", "Kumeyuri"),
        ("enten.html", "Enten"),
        ("../world/techniques.html", "Techniques"),
        ("index.html", "All blades"),
    ],
    "arcs/vs-sojo.html": [
        ("rakuzaichi.html", "Next: Rakuzaichi"),
        ("../characters/sojo.html", "Sojo"),
        ("../characters/char.html", "Char"),
        ("../blades/cloud-gouger.html", "Cloud Gouger"),
        ("../world/acg.html", "Anti-Cloud Gouger"),
        ("../analysis/sojo-fan.html", "Worst fan"),
        ("../manga/synopses.html#volume-1", "Vol. 1–2 synopses"),
        ("index.html", "All arcs"),
    ],
    "arcs/rakuzaichi.html": [
        ("vs-sojo.html", "Previous: Vs. Sojo"),
        ("sword-bearer.html", "Next: Sword Bearer"),
        ("../characters/hakuri.html", "Hakuri"),
        ("../characters/hiyuki.html", "Hiyuki"),
        ("../characters/kyora.html", "Kyora"),
        ("../world/storehouse.html", "Storehouse"),
        ("../factions/sazanami.html", "Sazanami"),
        ("../manga/synopses.html#volume-3", "Vol. 3–5 synopses"),
    ],
    "arcs/sword-bearer.html": [
        ("rakuzaichi.html", "Previous: Rakuzaichi"),
        ("seitei-war.html", "Next: Seitei War"),
        ("../characters/samura.html", "Samura"),
        ("../characters/uruha.html", "Uruha"),
        ("../characters/iori.html", "Iori"),
        ("../world/hotel.html", "Kyoto hotel"),
        ("../analysis/leak.html", "The leak"),
        ("../guide/part-1.html", "Part 1 long cut"),
    ],
    "arcs/seitei-war.html": [
        ("sword-bearer.html", "Previous: Sword Bearer"),
        ("../manga/part-2.html", "Part 2 page"),
        ("../characters/chiaki.html", "Chiaki"),
        ("../characters/kunishige.html", "Kunishige"),
        ("../world/irishima.html", "Irishima"),
        ("../analysis/irishima.html", "Vein essay"),
        ("../factions/soga.html", "Soga"),
        ("index.html", "All arcs"),
    ],
    "analysis/flame-bone.html": [
        ("../characters/hiyuki.html", "Hiyuki"),
        ("../characters/tafuku.html", "Tafuku"),
        ("revenge.html", "Revenge"),
        ("enten-purpose.html", "Enten’s purpose"),
        ("../arcs/rakuzaichi.html", "Rakuzaichi"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("index.html", "All essays"),
    ],
    "world/sorcery.html": [
        ("techniques.html", "Technique catalog"),
        ("contracts.html", "Contracts"),
        ("datenseki.html", "Datenseki"),
        ("iai.html", "Iai White Purity"),
        ("../analysis/true-realm.html", "True Realm"),
        ("../blades/index.html", "Enchanted Blades"),
        ("glossary.html", "Glossary"),
    ],
    "manga/volumes.html": [
        ("synopses.html", "Volume synopses"),
        ("covers.html", "Cover studies"),
        ("chapters.html", "Chapter index"),
        ("index.html", "Manga guide"),
        ("publication.html", "Publication record"),
        ("../collectibles/shop.html", "Where to buy"),
    ],
    "manga/chapters.html": [
        ("../arcs/vs-sojo.html", "Ch. 1–18 Vs. Sojo"),
        ("../arcs/rakuzaichi.html", "Ch. 19–46 Rakuzaichi"),
        ("../arcs/sword-bearer.html", "Ch. 47–115 Sword Bearer"),
        ("../arcs/seitei-war.html", "Ch. 116– Seitei War"),
        ("synopses.html", "Volume synopses"),
        ("part-2.html", "Part 2"),
        ("volumes.html", "Volume guide"),
    ],
    "manga/covers.html": [
        ("volumes.html", "Volume guide"),
        ("synopses.html", "Synopses"),
        ("color-pages.html", "Color pages"),
        ("../analysis/titles.html", "What the titles are doing"),
        ("index.html", "Manga guide"),
    ],
    "manga/color-pages.html": [
        ("covers.html", "Cover studies"),
        ("chapters.html", "Chapter index"),
        ("index.html", "Manga guide"),
        ("../fun/toc.html", "ToC ritual"),
    ],
    "manga/synopses.html": [
        ("volumes.html", "Volume guide"),
        ("covers.html", "Cover studies"),
        ("chapters.html", "Chapter index"),
        ("part-2.html", "Part 2"),
        ("../guide/part-1.html", "Part 1 long cut"),
        ("../arcs/index.html", "Story arcs"),
    ],
    "manga/index.html": [
        ("volumes.html", "Volumes"),
        ("synopses.html", "Synopses"),
        ("chapters.html", "Chapters"),
        ("covers.html", "Covers"),
        ("part-2.html", "Part 2"),
        ("../arcs/index.html", "Story arcs"),
        ("../guide/part-1.html", "Part 1 long cut"),
    ],
    "characters/index.html": [
        ("../blades/index.html", "Enchanted Blades"),
        ("../factions/hishaku.html", "Hishaku"),
        ("../factions/kamunabi.html", "Kamunabi"),
        ("../world/register.html", "Name register"),
        ("../guide/cast.html", "Who is who"),
        ("chihiro.html", "Chihiro"),
    ],
    "blades/index.html": [
        ("enten.html", "Enten"),
        ("cloud-gouger.html", "Cloud Gouger"),
        ("magatsumi.html", "Magatsumi"),
        ("kumeyuri.html", "Kumeyuri"),
        ("tobimune.html", "Tobimune"),
        ("../world/techniques.html", "Techniques"),
        ("../world/contracts.html", "Contracts"),
        ("../guide/blades.html", "Guide: the blades"),
    ],
    "arcs/index.html": [
        ("vs-sojo.html", "Vs. Sojo"),
        ("rakuzaichi.html", "Rakuzaichi"),
        ("sword-bearer.html", "Sword Bearer"),
        ("seitei-war.html", "Seitei War"),
        ("../manga/synopses.html", "Volume synopses"),
        ("../guide/story.html", "The story"),
        ("../guide/part-1.html", "Part 1 long cut"),
    ],
    "analysis/index.html": [
        ("enten-purpose.html", "Enten’s purpose"),
        ("malediction.html", "Malediction"),
        ("revenge.html", "Revenge"),
        ("irishima.html", "Irishima’s vein"),
        ("../arcs/index.html", "Story arcs"),
        ("../media/index.html", "Theories"),
    ],
    "guide/index.html": [
        ("series.html", "The series"),
        ("premise.html", "The premise"),
        ("blades.html", "The blades"),
        ("story.html", "The story"),
        ("part-1.html", "Part 1 long cut"),
        ("watch.html", "How to watch"),
        ("../characters/index.html", "Characters"),
    ],
    "fun/index.html": [
        ("community.html", "Sunday board"),
        ("goldfish.html", "Goldfish, not koi"),
        ("bowl.html", "The bowl"),
        ("hokazono.html", "Hokazono"),
        ("first-read.html", "First-read notes"),
        ("../media/anime.html", "Anime"),
    ],
    "fun/goldfish.html": [
        ("bowl.html", "The bowl"),
        ("../blades/enten.html", "Enten"),
        ("../analysis/enten-purpose.html", "Purpose essay"),
        ("hokazono.html", "Hokazono"),
        ("../characters/chihiro.html", "Chihiro"),
        ("index.html", "Fun"),
    ],
    "fun/hokazono.html": [
        ("goldfish.html", "Goldfish, not koi"),
        ("../guide/series.html", "The series"),
        ("../manga/publication.html", "Publication record"),
        ("meme.html", "Meme to flagship"),
        ("index.html", "Fun"),
    ],
    "fun/first-read.html": [
        ("../guide/premise.html", "The premise"),
        ("../characters/chihiro.html", "Chihiro"),
        ("goldfish.html", "Goldfish"),
        ("sunday.html", "Sunday ritual"),
        ("../manga/chapters.html", "Chapter index"),
        ("index.html", "Fun"),
    ],
    "fun/sunday.html": [
        ("community.html", "Sunday board"),
        ("toc.html", "ToC ritual"),
        ("fandom.html", "English fandom"),
        ("../manga/index.html", "Manga guide"),
        ("index.html", "Fun"),
    ],
    "fun/oneshots.html": [
        ("../manga/volumes.html", "Volume guide"),
        ("../characters/sojo.html", "Sojo"),
        ("../characters/soya.html", "Soya"),
        ("../manga/chapters.html", "Chapter index"),
        ("index.html", "Fun"),
    ],
    "world/index.html": [
        ("glossary.html", "Glossary"),
        ("locations.html", "Locations"),
        ("techniques.html", "Techniques"),
        ("battles.html", "Battles"),
        ("lineage.html", "Lineage"),
        ("register.html", "Name register"),
        ("irishima.html", "Irishima"),
        ("../factions/index.html", "Factions"),
    ],
    "world/battles.html": [
        ("../arcs/vs-sojo.html", "Vs. Sojo"),
        ("../arcs/rakuzaichi.html", "Rakuzaichi"),
        ("../arcs/sword-bearer.html", "Sword Bearer"),
        ("techniques.html", "Techniques"),
        ("hotel.html", "Kyoto hotel"),
        ("index.html", "World"),
    ],
    "world/objects.html": [
        ("../fun/bowl.html", "The bowl"),
        ("datenseki.html", "Datenseki"),
        ("storehouse.html", "Storehouse"),
        ("contracts.html", "Contracts"),
        ("fire-gate.html", "Fire-gate"),
        ("../blades/index.html", "Enchanted Blades"),
        ("index.html", "World"),
    ],
    "world/birthdays.html": [
        ("../characters/chihiro.html", "Chihiro"),
        ("../characters/kunishige.html", "Kunishige"),
        ("../characters/shiba.html", "Shiba"),
        ("../characters/sojo.html", "Sojo"),
        ("../characters/char.html", "Char"),
        ("register.html", "Name register"),
        ("lineage.html", "Lineage"),
    ],
    "world/lineage.html": [
        ("../factions/soga.html", "Soga"),
        ("../factions/sazanami.html", "Sazanami"),
        ("../characters/chihiro.html", "Chihiro"),
        ("../characters/chiaki.html", "Chiaki"),
        ("birthdays.html", "Birthdays"),
        ("register.html", "Name register"),
        ("index.html", "World"),
    ],
    "world/symbols.html": [
        ("../fun/goldfish.html", "Goldfish, not koi"),
        ("../factions/hishaku.html", "Hishaku"),
        ("../blades/enten.html", "Enten"),
        ("../analysis/malediction.html", "Malediction"),
        ("../analysis/owl.html", "Owl over Japan"),
        ("index.html", "World"),
    ],
    "collectibles/union-arena.html": [
        ("index.html", "Collectibles"),
        ("shop.html", "Shop"),
        ("../media/adaptations.html", "Adaptations"),
        ("../characters/chihiro.html", "Chihiro"),
        ("../characters/hakuri.html", "Hakuri"),
        ("../privacy.html", "Privacy"),
    ],
    "media/staff.html": [
        ("anime.html", "Anime"),
        ("adaptations.html", "Adaptations"),
        ("../fun/hokazono.html", "Hokazono"),
        ("../fun/voices.html", "Voices"),
        ("index.html", "Theories"),
    ],
    "media/adaptations.html": [
        ("anime.html", "Anime"),
        ("staff.html", "Staff"),
        ("../manga/index.html", "Manga guide"),
        ("../collectibles/union-arena.html", "UNION ARENA"),
        ("../fun/voices.html", "Voices"),
        ("index.html", "Theories"),
    ],
    "factions/index.html": [
        ("kamunabi.html", "Kamunabi"),
        ("hishaku.html", "Hishaku"),
        ("sazanami.html", "Sazanami"),
        ("masumi.html", "Masumi"),
        ("soga.html", "Soga"),
        ("../world/register.html", "Name register"),
        ("../characters/index.html", "Characters"),
    ],
    "media/index.html": [
        ("anime.html", "Anime countdown"),
        ("../guide/watch.html", "How to watch"),
        ("../analysis/index.html", "Essays"),
        ("../fun/fandom.html", "English fandom"),
    ],
    "about.html": [
        ("index.html", "Home"),
        ("guide/index.html", "Guide"),
        ("characters/index.html", "Characters"),
        ("faq.html", "FAQ"),
        ("search.html", "Search"),
        ("sitemap.html", "Site map"),
        ("privacy.html", "Privacy"),
    ],
    "index.html": [
        ("guide/index.html", "Guide"),
        ("characters/index.html", "Characters"),
        ("blades/index.html", "Enchanted Blades"),
        ("manga/synopses.html", "Volume synopses"),
        ("arcs/index.html", "Story arcs"),
        ("media/anime.html", "Anime"),
        ("search.html", "Search"),
        ("faq.html", "FAQ"),
    ],
    "faq.html": [
        ("search.html", "Search"),
        ("guide/index.html", "Guide"),
        ("media/anime.html", "Anime"),
        ("characters/chihiro.html", "Chihiro"),
        ("blades/index.html", "Enchanted Blades"),
        ("collectibles/union-arena.html", "UNION ARENA"),
        ("sitemap.html", "Site map"),
        ("about.html", "About"),
    ],
    "search.html": [
        ("faq.html", "FAQ"),
        ("sitemap.html", "Site map"),
        ("characters/index.html", "Characters"),
        ("blades/index.html", "Enchanted Blades"),
        ("guide/index.html", "Guide"),
        ("index.html", "Home"),
    ],
    "sitemap.html": [
        ("index.html", "Home"),
        ("search.html", "Search"),
        ("faq.html", "FAQ"),
        ("guide/index.html", "Guide"),
        ("characters/index.html", "Characters"),
        ("manga/synopses.html", "Volume synopses"),
        ("about.html", "About"),
    ],
    "privacy.html": [
        ("index.html", "Home"),
        ("about.html", "About"),
        ("collectibles/shop.html", "Shop"),
        ("collectibles/union-arena.html", "UNION ARENA"),
    ],
    "guide/series.html": [
        ("premise.html", "The premise"),
        ("paper.html", "On paper"),
        ("../fun/hokazono.html", "Hokazono"),
        ("../manga/publication.html", "Publication record"),
        ("index.html", "Guide"),
    ],
    "guide/premise.html": [
        ("blades.html", "The blades"),
        ("story.html", "The story"),
        ("../characters/chihiro.html", "Chihiro"),
        ("../fun/first-read.html", "First-read notes"),
        ("index.html", "Guide"),
    ],
    "guide/blades.html": [
        ("../blades/index.html", "Blade encyclopedia"),
        ("../world/techniques.html", "Techniques"),
        ("premise.html", "The premise"),
        ("../characters/kunishige.html", "Kunishige"),
        ("index.html", "Guide"),
    ],
    "guide/story.html": [
        ("part-1.html", "Part 1 long cut"),
        ("../manga/part-2.html", "Part 2"),
        ("../arcs/index.html", "Story arcs"),
        ("../manga/synopses.html", "Synopses"),
        ("index.html", "Guide"),
    ],
}

FOLDER_RELATED = {
    "characters": [
        ("index.html", "All characters"),
        ("../blades/index.html", "Enchanted Blades"),
        ("../world/register.html", "Name register"),
    ],
    "blades": [
        ("index.html", "All blades"),
        ("../world/techniques.html", "Techniques"),
        ("../characters/kunishige.html", "Kunishige"),
    ],
    "arcs": [
        ("index.html", "All arcs"),
        ("../manga/chapters.html", "Chapter index"),
        ("../manga/synopses.html", "Synopses"),
    ],
    "analysis": [
        ("index.html", "All essays"),
        ("../arcs/index.html", "Story arcs"),
        ("../blades/index.html", "Blades"),
    ],
    "manga": [
        ("index.html", "Manga guide"),
        ("synopses.html", "Synopses"),
        ("chapters.html", "Chapters"),
        ("volumes.html", "Volumes"),
    ],
    "fun": [
        ("index.html", "Fun"),
        ("community.html", "Sunday board"),
        ("goldfish.html", "Goldfish"),
    ],
    "world": [
        ("index.html", "World"),
        ("glossary.html", "Glossary"),
        ("techniques.html", "Techniques"),
        ("battles.html", "Battles"),
    ],
    "guide": [
        ("index.html", "Guide"),
        ("story.html", "The story"),
        ("cast.html", "Who is who"),
    ],
    "factions": [
        ("index.html", "Factions"),
        ("hishaku.html", "Hishaku"),
        ("kamunabi.html", "Kamunabi"),
    ],
    "collectibles": [
        ("index.html", "Collectibles"),
        ("shop.html", "Shop"),
        ("union-arena.html", "UNION ARENA"),
        ("../manga/volumes.html", "Volume ISBNs"),
    ],
    "media": [
        ("index.html", "Theories"),
        ("anime.html", "Anime"),
        ("staff.html", "Staff"),
        ("adaptations.html", "Adaptations"),
    ],
}

SRC_ALT = {
    "hokazono-commemorative.jpg": "Takeru Hokazono commemorative Kagurabachi illustration",
    "chihiro.webp": "Chihiro Rokuhira manga portrait",
    "chihiro-anime.png": "Official Cypic anime visual of Chihiro Rokuhira",
    "enten.webp": "Enten, Chihiro’s Enchanted Blade with three goldfish",
    "Enten.png": "Enten drawn in the manga",
    "ch009.png": "Kagurabachi chapter 9: Enten versus Cloud Gouger",
    "ch001.png": "Kagurabachi chapter 1: the Rokuhira workshop",
    "ch014.png": "Kagurabachi chapter 14: True Realm",
    "ch113.png": "Kagurabachi chapter 113: Irishima and Shokoku",
    "jp-vol1.webp": "Kagurabachi Japanese volume 1 jacket",
    "jp-vol2.webp": "Kagurabachi Japanese volume 2 jacket",
    "jp-vol10.webp": "Kagurabachi Japanese volume 10 jacket",
    "teaser-og.jpg": "Official Kagurabachi anime teaser visual",
    "hakuri.webp": "Hakuri Sazanami manga portrait",
    "yura.webp": "Yura of the Hishaku, manga portrait",
    "azami.webp": "Azami of the Kamunabi, manga portrait",
    "07.png": "Kagurabachi fan drawing from r/Kagurabachi",
    "jp-ogp.jpg": "Official Japanese Kagurabachi promotional still",
    "en-ogp.jpg": "Official English Kagurabachi promotional still",
    "enten.png": "Enten goldfish illustration",
    "sojo.webp": "Genichi Sojo manga portrait",
    "viz-social.jpg": "VIZ Media Kagurabachi social still",
    "x-en-avatar.jpg": "Official Kagurabachi anime English X account avatar",
    "x-jp-avatar.jpg": "Official Kagurabachi anime Japanese X account avatar",
    "chihiro-060.jpg": "UNION ARENA Chihiro Rokuhira Super Rare card 060 from the Kagurabachi set",
    "chihiro-059.jpg": "UNION ARENA Chihiro Rokuhira card 059 from the Kagurabachi set",
    "shiba-049.jpg": "UNION ARENA Togo Shiba card 049 from the Kagurabachi set",
    "hakuri-047.jpg": "UNION ARENA Hakuri Sazanami Super Rare card 047 from the Kagurabachi set",
    "char.jpg": "UNION ARENA Char Kyonagi card from the Kagurabachi set",
    "kyora.jpg": "UNION ARENA Kyora Sazanami card from the Kagurabachi set",
    "hiyuki-066.jpg": "UNION ARENA Hiyuki Kagari card 066 from the Kagurabachi set",
    "iori-005.jpg": "UNION ARENA Iori Samura card 005 from the Kagurabachi set",
    "iori-003.jpg": "UNION ARENA Iori Samura card 003 from the Kagurabachi set",
    "yura.jpg": "UNION ARENA Yura of the Hishaku card from the Kagurabachi set",
    "iai.jpg": "UNION ARENA Iai White Purity Style card from the Kagurabachi set",
    "booster-pack.jpg": "UNION ARENA Kagurabachi English booster pack UE16BT",
    "booster-box.jpg": "UNION ARENA Kagurabachi English booster box, 16 packs",
}

SKIP_RELATED = {"404.html"}

SERIES_SAME_AS = [
    "https://en.wikipedia.org/wiki/Kagurabachi",
    "https://www.viz.com/kagurabachi",
    "https://mangaplus.shueisha.co.jp/titles/100274",
    "https://anime.kagurabachi.jp/",
    "https://myanimelist.net/manga/158925/Kagurabachi",
]

_LASTMOD: dict[str, str] = {}

SECTIONS = [
    ("Guide", "guide"),
    ("Characters", "characters"),
    ("Enchanted Blades", "blades"),
    ("Manga", "manga"),
    ("Story arcs", "arcs"),
    ("World", "world"),
    ("Factions", "factions"),
    ("Essays", "analysis"),
    ("Fun", "fun"),
    ("Media", "media"),
    ("Collectibles", "collectibles"),
]


def html_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)


def rel_of(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def canonical_url(rel: str) -> str:
    if rel in ("index.html", "404.html"):
        return f"{SITE}/" if rel == "index.html" else f"{SITE}/404.html"
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[:-10]}"
    return f"{SITE}/{rel}"


def folder_of(rel: str) -> str | None:
    if "/" not in rel:
        return None
    return rel.split("/", 1)[0]


def attr(html: str, name: str) -> str | None:
    m = re.search(rf'<{name}[^>]*>(.*?)</{name}>', html, re.I | re.S)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return None


def meta_desc(html: str) -> str | None:
    m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.I)
    if m:
        return m.group(1)
    m = re.search(r'<meta\s+content="([^"]*)"\s+name="description"', html, re.I)
    return m.group(1) if m else None


def first_img_abs(html: str, rel: str) -> str:
    m = re.search(r'<img[^>]+src="([^"]+)"', html)
    if not m:
        return DEFAULT_OG
    src = m.group(1)
    if src.startswith("http"):
        return src
    if src.startswith("../"):
        # page is in a subfolder
        resolved = str(Path(rel).parent / src)
        resolved = str(Path(resolved).as_posix())
        while "/../" in resolved:
            resolved = re.sub(r"[^/]+/\.\./", "", resolved, count=1)
        resolved = resolved.lstrip("./")
        return f"{SITE}/{resolved}"
    if src.startswith("assets/") or src.startswith("/assets/"):
        return f"{SITE}/{src.lstrip('/')}"
    return f"{SITE}/{src.lstrip('/')}"


def og_image_for(html: str, rel: str) -> str:
    overrides = {
        "index.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "about.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "sitemap.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "faq.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "search.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "media/anime.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "guide/watch.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "404.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "fun/community.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "fun/index.html": f"{SITE}/assets/covers/teaser-og.jpg",
        "collectibles/union-arena.html": f"{SITE}/assets/cards/chihiro-060.jpg",
        "media/staff.html": f"{SITE}/assets/covers/hokazono-commemorative.jpg",
        "media/adaptations.html": f"{SITE}/assets/covers/teaser-og.jpg",
    }
    if rel in overrides:
        return overrides[rel]
    # Prefer a portrait or cover over a tiny tile if present.
    prefs = re.findall(r'<img[^>]+src="([^"]+(?:portraits|covers|official)[^"]+)"', html)
    if prefs:
        fake = f'<img src="{prefs[0]}">'
        return first_img_abs(fake, rel)
    return first_img_abs(html, rel)


def page_kind(rel: str) -> str:
    if rel == "about.html":
        return "AboutPage"
    if rel == "faq.html":
        return "FAQPage"
    if rel == "search.html":
        return "SearchResultsPage"
    if rel.endswith("/index.html") or rel in ("index.html", "sitemap.html"):
        return "CollectionPage"
    if rel.startswith("analysis/") or rel.startswith("manga/synopses"):
        return "Article"
    return "WebPage"


def breadcrumbs(html: str, rel: str, title: str) -> list[dict]:
    items = [{"name": "Home", "url": f"{SITE}/"}]
    crumb = re.search(r'<p class="crumb">(.*?)</p>', html, re.S)
    if crumb:
        for href, label in re.findall(r'<a href="([^"]+)">([^<]+)</a>', crumb.group(1)):
            # resolve relative href against rel
            resolved = str((Path(rel).parent / href).as_posix())
            while "/../" in f"/{resolved}":
                resolved = re.sub(r"[^/]+/\.\./", "", resolved)
            resolved = resolved.lstrip("./")
            if canonical_url(resolved) == f"{SITE}/":
                continue
            items.append({"name": htmlmod.unescape(label), "url": canonical_url(resolved)})
    # current page
    short = htmlmod.unescape(re.sub(r"\s*[·|].*$", "", re.sub(r"<[^>]+>", "", title))).strip()
    items.append({"name": short or "Page", "url": canonical_url(rel)})
    # dedupe consecutive
    out = []
    for it in items:
        if out and out[-1]["url"] == it["url"]:
            continue
        out.append(it)
    return out[:6]


def json_ld(rel: str, title: str, desc: str, html: str) -> str:
    clean_title = htmlmod.unescape(re.sub(r"<[^>]+>", "", title))
    url = canonical_url(rel)
    crumbs = breadcrumbs(html, rel, clean_title)
    modified = git_lastmod(rel)
    website = {
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "name": "Kagurabachi Archive",
        "alternateName": [
            "Kagurabachi Encyclopedia",
            "Kagurabachi.org",
            "Kagurabachi wiki",
            "KB",
            "カグラバチ 資料庫",
        ],
        "url": f"{SITE}/",
        "inLanguage": "en",
        "description": "Independent encyclopedia for Takeru Hokazono’s Kagurabachi: characters, Enchanted Blades, manga guide, and analysis.",
        "publisher": {"@id": f"{SITE}/#org"},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": f"{SITE}/search.html?q={{search_term_string}}",
            },
            "query-input": "required name=search_term_string",
        },
    }
    org = {
        "@type": "Organization",
        "@id": f"{SITE}/#org",
        "name": "Kagurabachi Archive",
        "url": f"{SITE}/",
        "logo": {
            "@type": "ImageObject",
            "url": f"{SITE}/assets/logo.png",
            "width": 512,
            "height": 512,
        },
    }
    page = {
        "@type": page_kind(rel),
        "@id": url,
        "url": url,
        "name": clean_title,
        "description": htmlmod.unescape(desc or ""),
        "isPartOf": {"@id": f"{SITE}/#website"},
        "inLanguage": "en",
        "image": og_image_for(html, rel),
        "dateModified": modified,
        "publisher": {"@id": f"{SITE}/#org"},
    }
    if page_kind(rel) == "Article":
        page["headline"] = clean_title
        page["datePublished"] = modified
        page["author"] = {"@id": f"{SITE}/#org"}
    graph: list[dict] = [website, org, page]
    if rel in ("index.html", "manga/index.html", "guide/series.html"):
        graph.append(comic_series())
        page["about"] = {"@id": f"{SITE}/#series"}
    if rel in ("media/anime.html", "guide/watch.html"):
        graph.append(tv_series())
        page["about"] = {"@id": f"{SITE}/#anime"}
    if rel == "faq.html":
        faqs = extract_faq(html)
        if faqs:
            page["mainEntity"] = faqs
    if len(crumbs) >= 2:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["name"], "item": c["url"]}
                for i, c in enumerate(crumbs)
            ],
        })
    if rel.startswith("characters/") and not rel.endswith("index.html"):
        jp = re.search(r'<h1>[^<]*<span class="jp">([^<]+)</span>', html)
        person = {
            "@type": ["Person", "FictionalCharacter"],
            "name": re.sub(r"\s*[·|].*$", "", clean_title).strip(),
            "url": url,
            "description": htmlmod.unescape(desc or ""),
            "mainEntityOfPage": url,
            "isPartOf": {"@id": f"{SITE}/#series"},
        }
        if jp:
            person["alternateName"] = htmlmod.unescape(jp.group(1)).strip()
        graph.append(person)
    if rel.startswith("blades/") and not rel.endswith("index.html"):
        graph.append({
            "@type": "CreativeWork",
            "name": re.sub(r"\s*[·|].*$", "", clean_title).strip(),
            "url": url,
            "description": htmlmod.unescape(desc or ""),
            "mainEntityOfPage": url,
            "isPartOf": {"@id": f"{SITE}/#series"},
        })
    dumped = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return dumped.replace("</", "<\\/")


def strip_old_seo(html: str) -> str:
    html = re.sub(r'\n?\s*<link rel="canonical"[^>]*>', "", html)
    html = re.sub(r'\n?\s*<meta property="og:[^"]+" content="[^"]*"\s*/?>', "", html)
    html = re.sub(r'\n?\s*<meta name="twitter:[^"]+" content="[^"]*"\s*/?>', "", html)
    html = re.sub(r'\n?\s*<meta name="robots" content="[^"]*"\s*/?>', "", html)
    html = re.sub(r'\n?\s*<meta name="googlebot" content="[^"]*"\s*/?>', "", html)
    html = re.sub(r'\n?\s*<meta name="theme-color" content="[^"]*"\s*/?>', "", html)
    html = re.sub(r'\n?\s*<link rel="sitemap"[^>]*>', "", html)
    html = re.sub(r'\n?\s*<link rel="search"[^>]*>', "", html)
    html = re.sub(r'\n?\s*<link rel="manifest"[^>]*>', "", html)
    html = re.sub(r'\n?\s*<link rel="apple-touch-icon"[^>]*>', "", html)
    html = re.sub(r'\n?\s*<link rel="alternate"[^>]*hreflang[^>]*>', "", html)
    html = re.sub(r'\n?\s*<link rel="preload"[^>]*>', "", html)
    html = re.sub(
        r'\n?\s*<script type="application/ld\+json">.*?</script>',
        "",
        html,
        flags=re.S,
    )
    return html


def inject_head(html: str, rel: str) -> str:
    html = strip_old_seo(html)
    title = TITLE_OVERRIDES.get(rel) or attr(html, "title") or "Kagurabachi Archive"
    # Apply title override in the document
    if rel in TITLE_OVERRIDES:
        html = re.sub(r"<title>.*?</title>", f"<title>{TITLE_OVERRIDES[rel]}</title>", html, count=1, flags=re.S)
        title = TITLE_OVERRIDES[rel]
    desc = DESC_OVERRIDES.get(rel) or meta_desc(html) or ""
    if rel in DESC_OVERRIDES:
        if meta_desc(html):
            html = re.sub(
                r'<meta name="description" content="[^"]*">',
                f'<meta name="description" content="{DESC_OVERRIDES[rel]}">',
                html,
                count=1,
            )
        else:
            html = html.replace(
                "</title>",
                f'</title>\n  <meta name="description" content="{DESC_OVERRIDES[rel]}">',
                1,
            )
        desc = DESC_OVERRIDES[rel]
    elif not meta_desc(html) and desc == "":
        lede = re.search(r'<p class="lede">(.*?)</p>', html, re.S)
        if lede:
            plain = re.sub(r"<[^>]+>", "", lede.group(1))
            plain = re.sub(r"\s+", " ", plain).strip()
            if len(plain) > 160:
                plain = plain[:157].rsplit(" ", 1)[0] + "…"
            desc = htmlmod.escape(plain, quote=True)
            html = html.replace(
                "</title>",
                f'</title>\n  <meta name="description" content="{desc}">',
                1,
            )

    clean_title = htmlmod.unescape(re.sub(r"<[^>]+>", "", title))
    url = canonical_url(rel)
    image = og_image_for(html, rel)
    robots = (
        "noindex, follow"
        if rel == "404.html"
        else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    )
    og_type = "article" if page_kind(rel) == "Article" else "website"
    ld = json_ld(rel, title, htmlmod.unescape(desc), html)
    og_alt = htmlmod.escape(clean_title, quote=True)

    extra = [
        f'  <link rel="canonical" href="{url}">',
        f'  <link rel="alternate" hreflang="en" href="{url}">',
        f'  <link rel="alternate" hreflang="x-default" href="{url}">',
        f'  <link rel="search" type="application/opensearchdescription+xml" title="Kagurabachi Archive" href="{SITE}/opensearch.xml">',
        f'  <link rel="manifest" href="{SITE}/manifest.webmanifest">',
        f'  <link rel="apple-touch-icon" href="{SITE}/assets/logo.png">',
        f'  <meta name="robots" content="{robots}">',
        f'  <meta name="googlebot" content="{robots}">',
        f'  <meta name="theme-color" content="#9b1419">',
        f'  <meta property="og:type" content="{og_type}">',
        f'  <meta property="og:site_name" content="Kagurabachi Archive">',
        f'  <meta property="og:locale" content="en_US">',
        f'  <meta property="og:url" content="{url}">',
        f'  <meta property="og:title" content="{htmlmod.escape(clean_title, quote=True)}">',
        f'  <meta property="og:description" content="{desc}">',
        f'  <meta property="og:image" content="{image}">',
        f'  <meta property="og:image:alt" content="{og_alt}">',
        f'  <meta name="twitter:card" content="summary_large_image">',
        f'  <meta name="twitter:title" content="{htmlmod.escape(clean_title, quote=True)}">',
        f'  <meta name="twitter:description" content="{desc}">',
        f'  <meta name="twitter:image" content="{image}">',
        '  <script type="application/ld+json">',
        ld,
        "  </script>",
    ]
    if rel == "index.html":
        extra.insert(1, f'  <link rel="sitemap" type="application/xml" href="{SITE}/sitemap.xml">')
        extra.insert(2, '  <link rel="preload" as="image" href="assets/covers/teaser-og.jpg" fetchpriority="high">')

    block = "\n".join(extra)
    if "</head>" not in html:
        raise SystemExit(f"no </head> in {rel}")
    html = html.replace("</head>", block + "\n</head>", 1)
    return html


def parse_related_links(inner: str) -> list[tuple[str, str]]:
    return [(h, htmlmod.unescape(t)) for h, t in re.findall(r'<a href="([^"]+)">([^<]*)</a>', inner)]


def fix_related_href(href: str, label: str) -> str:
    lab = label.strip().lower()
    faction = {
        "hishaku": "hishaku.html",
        "kamunabi": "kamunabi.html",
        "sazanami": "sazanami.html",
        "masumi": "masumi.html",
        "soga": "soga.html",
    }
    if "factions/index.html" in href and lab in faction:
        return href.replace("index.html", faction[lab])
    return href


def render_related(links: list[tuple[str, str]]) -> str:
    seen_href = set()
    seen_label = set()
    out = []
    for href, label in links:
        key = href.split("#")[0] or href
        lab = label.strip().lower()
        if key in seen_href and "#" not in href:
            continue
        if lab in seen_label:
            continue
        seen_href.add(key)
        seen_label.add(lab)
        out.append(f'<a href="{href}">{htmlmod.escape(label)}</a>')
        if len(out) >= 8:
            break
    return '<nav class="related" aria-label="Related pages">' + "".join(out) + "</nav>"


def merge_related(html: str, rel: str) -> str:
    if rel in SKIP_RELATED:
        return html
    extras = list(PAGE_RELATED.get(rel, []))
    folder = folder_of(rel)
    if folder and folder in FOLDER_RELATED and rel not in PAGE_RELATED:
        extras.extend(FOLDER_RELATED[folder])
    elif folder and folder in FOLDER_RELATED:
        # still allow a couple of folder hubs
        extras.extend(FOLDER_RELATED[folder][:2])

    existing_m = re.search(r'<(?:p|nav) class="related"[^>]*>(.*?)</(?:p|nav)>', html, re.S)
    existing: list[tuple[str, str]] = []
    if existing_m:
        existing = [(fix_related_href(h, t), t) for h, t in parse_related_links(existing_m.group(1))]

    merged = existing + extras
    if not merged:
        return html

    nav = render_related(merged)
    if existing_m:
        html = html[: existing_m.start()] + nav + html[existing_m.end() :]
        return html

    # Homepage: keep the chips inside .wrap so they inherit the column.
    if rel == "index.html" and "</div>\n  </main>" in html:
        html = html.replace("</div>\n  </main>", nav + "\n    </div>\n  </main>", 1)
        return html

    # Insert before last </article> if the related belongs with the prose,
    # else before </main>.
    article_close = html.rfind("</article>")
    if article_close != -1:
        html = html[:article_close] + nav + "\n    " + html[article_close:]
        return html
    main_close = html.rfind("</main>")
    if main_close != -1:
        html = html[:main_close] + "    " + nav + "\n  " + html[main_close:]
    return html


def alt_for_src(src: str) -> str:
    name = Path(src).name
    if name in SRC_ALT:
        return SRC_ALT[name]
    stem = Path(src).stem.replace("-", " ").replace("_", " ")
    return stem[:1].upper() + stem[1:] if stem else "Kagurabachi illustration"


def fill_empty_alts(html: str) -> str:
    def repl_block(m: re.Match) -> str:
        block = m.group(0)
        if 'alt=""' not in block:
            return block
        title = re.search(r"<b>([^<]+)</b>", block) or re.search(r"<h3>([^<]+)</h3>", block)
        if not title:
            return block
        label = re.sub(r"\s+", " ", title.group(1)).strip()
        return block.replace('alt=""', f'alt="{htmlmod.escape(label, quote=True)}"', 1)

    html = re.sub(
        r'<a class="(?:home-row|tile|card|path|board-card)"[^>]*>.*?</a>',
        repl_block,
        html,
        flags=re.S,
    )

    def repl_src_first(m: re.Match) -> str:
        alt = htmlmod.escape(alt_for_src(m.group(2)), quote=True)
        return f'<img{m.group(1)}src="{m.group(2)}"{m.group(3)}alt="{alt}">'

    def repl_alt_first(m: re.Match) -> str:
        alt = htmlmod.escape(alt_for_src(m.group(3)), quote=True)
        return f'<img{m.group(1)}alt="{alt}"{m.group(2)}src="{m.group(3)}"{m.group(4)}>'

    html = re.sub(r'<img([^>]*?)src="([^"]+)"([^>]*?)alt="">', repl_src_first, html)
    html = re.sub(r'<img([^>]*?)alt=""([^>]*?)src="([^"]+)"([^>]*?)>', repl_alt_first, html)
    return html


def upgrade_card_alts(html: str) -> str:
    html = html.replace("<h3><h3>", "<h3>")

    def repl(m: re.Match) -> str:
        pre, alt, mid, h3 = m.group(1), m.group(2), m.group(3), m.group(4)
        plain_h3 = re.sub(r"<[^>]+>", "", h3).strip()
        if alt.strip() and alt.strip().lower() in plain_h3.lower() and len(plain_h3) > len(alt.strip()) + 1:
            return f'<img{pre}alt="{htmlmod.escape(plain_h3, quote=True)}"{mid}{h3}</h3>'
        return m.group(0)

    return re.sub(
        r'<img([^>]*?)alt="([^"]*)"([^>]*>.{0,400}?<h3>)([^<]+)</h3>',
        repl,
        html,
        flags=re.S,
    )


def enhance_synopses(html: str, rel: str) -> str:
    if rel != "manga/synopses.html":
        return html
    html = re.sub(r"<h2>Volume (\d+):", r'<h2 id="volume-\1">Volume \1:', html)
    html = html.replace(
        "<h2>Volume 12 (solicited)",
        '<h2 id="volume-12">Volume 12 (solicited)',
        1,
    )
    if 'aria-label="Volumes on this page"' in html:
        return html
    items = []
    for n, rest in re.findall(r'<h2 id="volume-(\d+)">Volume \d+:?\s*([^<]*)', html):
        label = re.sub(r"<[^>]+>", "", rest).strip() or f"Volume {n}"
        label = re.sub(r"\s+", " ", label)
        items.append(f'<li><a href="#volume-{n}">Volume {n}: {label}</a></li>')
    if not items:
        return html
    toc = (
        '<nav class="toc" aria-label="Volumes on this page"><strong>On this page</strong>\n'
        f'      <ol>{"".join(items)}</ol>\n'
        "    </nav>\n"
    )
    html = html.replace("<article class=\"article\">", "<article class=\"article\">\n      " + toc, 1)
    # prev/next under each volume heading
    def add_turn(m: re.Match) -> str:
        n = int(m.group(1))
        heading = m.group(0)
        bits = []
        if n > 1:
            bits.append(f'<a href="#volume-{n-1}">Previous volume</a>')
        if n < 12:
            bits.append(f'<a href="#volume-{n+1}">Next volume</a>')
        bits.append(f'<a href="volumes.html">ISBNs</a>')
        bits.append(f'<a href="covers.html">Jacket</a>')
        return heading + '\n      <p class="vol-turn">' + " · ".join(bits) + "</p>"

    html = re.sub(r'<h2 id="volume-(\d+)">.*?</h2>', add_turn, html)
    return html


def enhance_volumes(html: str, rel: str) -> str:
    if rel != "manga/volumes.html":
        return html
    html = re.sub(
        r"<h3>Vol\. (\d+):",
        lambda m: f'<h3 id="vol-{int(m.group(1))}">Vol. {m.group(1)}:',
        html,
    )
    if "synopses.html#volume-1" in html:
        return html
    jumps = " · ".join(f'<a href="synopses.html#volume-{n}">{n}</a>' for n in range(1, 12))
    line = f"<p>Longer tellings of each spine sit on the <a href=\"synopses.html\">synopses</a> page: {jumps} · <a href=\"synopses.html#volume-12\">12</a>.</p>\n     "
    html = html.replace("<article class=\"article\">", "<article class=\"article\">\n     " + line, 1)
    return html


def enhance_chapters(html: str, rel: str) -> str:
    if rel != "manga/chapters.html":
        return html
    jump = (
        '<p class="arc-jump">Jump by movement: '
        '<a href="../arcs/vs-sojo.html">Ch. 1–18 Vs. Sojo</a> · '
        '<a href="../arcs/rakuzaichi.html">Ch. 19–46 Rakuzaichi</a> · '
        '<a href="../arcs/sword-bearer.html">Ch. 47–115 Sword Bearer Assassination</a> · '
        '<a href="../arcs/seitei-war.html">Ch. 116– Seitei War / Part 2</a>. '
        'The same commute by spine: <a href="synopses.html">volume synopses</a>.</p>'
    )
    html = re.sub(r'(?:\s*<p class="arc-jump">.*?</p>)+', "\n     " + jump, html, count=1, flags=re.S)
    if 'class="arc-jump"' in html:
        return html
    html = html.replace('<div class="table-wrap">', jump + '\n     <div class="table-wrap">', 1)
    return html


def lazy_images(html: str) -> str:
    """First <img> stays eager for LCP; later images lazy-load."""
    parts = html.split("<img")
    if len(parts) <= 2:
        return html
    out = [parts[0], "<img", parts[1]]
    for chunk in parts[2:]:
        out.append("<img")
        if "loading=" not in chunk[:100]:
            out.append(" loading=\"lazy\" decoding=\"async\"")
        out.append(chunk)
    return "".join(out)


def git_lastmod(rel: str) -> str:
    if rel in _LASTMOD:
        return _LASTMOD[rel]
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
        date = out.decode().strip()
        _LASTMOD[rel] = date or "2026-08-28"
    except Exception:
        _LASTMOD[rel] = "2026-08-28"
    return _LASTMOD[rel]


def comic_series() -> dict:
    return {
        "@type": "ComicSeries",
        "@id": f"{SITE}/#series",
        "name": "Kagurabachi",
        "alternateName": ["カグラバチ", "KB"],
        "url": f"{SITE}/manga/",
        "inLanguage": ["ja", "en"],
        "genre": ["Action", "Adventure", "Fantasy"],
        "author": {"@type": "Person", "name": "Takeru Hokazono"},
        "publisher": {"@type": "Organization", "name": "Shueisha"},
        "sameAs": SERIES_SAME_AS,
        "description": "Weekly Shōnen Jump manga by Takeru Hokazono. Chihiro Rokuhira, Enchanted Blades, and the Seitei War.",
    }


def tv_series() -> dict:
    return {
        "@type": "TVSeries",
        "@id": f"{SITE}/#anime",
        "name": "Kagurabachi",
        "alternateName": ["カグラバチ", "KB"],
        "url": f"{SITE}/media/anime.html",
        "inLanguage": "ja",
        "startDate": "2027-04",
        "director": {"@type": "Person", "name": "Tetsuya Takeuchi"},
        "productionCompany": {"@type": "Organization", "name": "Cypic"},
        "sameAs": [
            "https://anime.kagurabachi.jp/",
            "https://x.com/kb_anime_jp",
            "https://x.com/kb_anime_en",
        ],
        "description": "Cypic television adaptation of Takeru Hokazono’s Kagurabachi, scheduled for April 2027.",
        "isBasedOn": {"@id": f"{SITE}/#series"},
    }


def extract_faq(html: str) -> list[dict]:
    article = re.search(r'<article class="article[^"]*">(.*?)</article>', html, re.S)
    if not article:
        return []
    body = article.group(1)
    chunks = re.split(r'<h2 id="([^"]+)">', body)
    out = []
    for i in range(1, len(chunks) - 1, 2):
        inner = chunks[i + 1]
        q = re.search(r"([^<]+)</h2>", inner)
        a = re.search(r"<p>(.*?)</p>", inner, re.S)
        if not q or not a:
            continue
        question = htmlmod.unescape(re.sub(r"\s+", " ", q.group(1))).strip()
        answer = htmlmod.unescape(re.sub(r"<[^>]+>", " ", a.group(1)))
        answer = re.sub(r"\s+", " ", answer).strip()
        if question and answer:
            out.append({
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            })
    return out


def write_robots():
    (ROOT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /404.html\n"
        "Disallow: /tools/\n"
        "\n"
        "User-agent: Googlebot\n"
        "Allow: /\n"
        "Disallow: /404.html\n"
        "Disallow: /tools/\n"
        "\n"
        "User-agent: Googlebot-Image\n"
        "Allow: /\n"
        "Allow: /assets/\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
        f"Sitemap: {SITE}/sitemap-images.xml\n",
        encoding="utf-8",
    )


def abs_img(src: str, rel: str) -> str | None:
    if not src or src.startswith("data:"):
        return None
    if src.startswith("http://") or src.startswith("https://"):
        return src
    if src.startswith("//"):
        return "https:" + src
    fake = f'<img src="{src}">'
    return first_img_abs(fake, rel)


def write_image_sitemap(pages: list[str]):
    blocks = []
    seen_pair: set[tuple[str, str]] = set()
    for rel in pages:
        if rel in ("404.html",):
            continue
        html = (ROOT / rel).read_text(encoding="utf-8")
        page_url = canonical_url(rel)
        images = []
        for src, alt in re.findall(r'<img[^>]+src="([^"]+)"[^>]*(?:alt="([^"]*)")?', html):
            loc = abs_img(src, rel)
            if not loc or not loc.startswith(SITE):
                continue
            key = (page_url, loc)
            if key in seen_pair:
                continue
            seen_pair.add(key)
            cap = htmlmod.escape(alt or Path(src).stem.replace("-", " "), quote=True)
            images.append(
                "    <image:image>\n"
                f"      <image:loc>{htmlmod.escape(loc)}</image:loc>\n"
                f"      <image:title>{cap}</image:title>\n"
                f"      <image:caption>{cap}</image:caption>\n"
                "    </image:image>"
            )
        if not images:
            continue
        blocks.append(
            "  <url>\n"
            f"    <loc>{page_url}</loc>\n"
            + "\n".join(images[:20])
            + "\n  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        + "\n".join(blocks)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap-images.xml").write_text(xml, encoding="utf-8")


def write_opensearch():
    (ROOT / "opensearch.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">\n'
        "  <ShortName>Kagurabachi</ShortName>\n"
        "  <LongName>Kagurabachi Archive</LongName>\n"
        "  <Description>Search the Kagurabachi encyclopedia: characters, Enchanted Blades, arcs, essays.</Description>\n"
        "  <InputEncoding>UTF-8</InputEncoding>\n"
        f'  <Image width="16" height="16" type="image/svg+xml">{SITE}/assets/favicon.svg</Image>\n'
        f'  <Image width="512" height="512" type="image/png">{SITE}/assets/logo.png</Image>\n'
        f'  <Url type="text/html" method="get" template="{SITE}/search.html?q={{searchTerms}}"/>\n'
        "</OpenSearchDescription>\n",
        encoding="utf-8",
    )


def write_manifest():
    data = {
        "name": "Kagurabachi Archive",
        "short_name": "KB Archive",
        "description": "Independent encyclopedia for Takeru Hokazono’s Kagurabachi.",
        "start_url": "/",
        "scope": "/",
        "display": "browser",
        "lang": "en",
        "background_color": "#f6efe6",
        "theme_color": "#9b1419",
        "icons": [
            {
                "src": "/assets/logo.png",
                "sizes": "512x512",
                "type": "image/png",
            }
        ],
    }
    (ROOT / "manifest.webmanifest").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def inject_noscript(html: str, rel: str) -> str:
    html = re.sub(
        r'\n?<noscript>\s*<nav class="crawl-nav".*?</noscript>\n?',
        "",
        html,
        flags=re.S,
    )
    prefix = "../" if "/" in rel else ""
    links = [
        (f"{prefix}index.html", "Home"),
        (f"{prefix}search.html", "Search"),
        (f"{prefix}faq.html", "FAQ"),
        (f"{prefix}characters/index.html", "Characters"),
        (f"{prefix}blades/index.html", "Blades"),
        (f"{prefix}manga/index.html", "Manga"),
        (f"{prefix}arcs/index.html", "Story"),
        (f"{prefix}sitemap.html", "Site map"),
    ]
    inner = " · ".join(f'<a href="{h}">{t}</a>' for h, t in links)
    block = f'<noscript>\n<nav class="crawl-nav" aria-label="Site">{inner}</nav>\n</noscript>\n'
    html = re.sub(r"(<body[^>]*>)", r"\1\n" + block, html, count=1)
    return html


def search_entry(rel: str, html: str, title: str) -> dict | None:
    if rel in ("404.html",):
        return None
    clean_title = htmlmod.unescape(re.sub(r"<[^>]+>", "", title))
    short = re.sub(r"\s*[·|].*$", "", clean_title).strip()
    desc = htmlmod.unescape(meta_desc(html) or "")
    jp_m = re.search(r'<h1>[^<]*<span class="jp">([^<]+)</span>', html)
    jp = htmlmod.unescape(jp_m.group(1)).strip() if jp_m else ""
    article = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    body = article.group(1) if article else html
    body = re.sub(r'<span class="spoiler">.*?</span>', " ", body, flags=re.S)
    body = re.sub(r"<script[^>]*>.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = htmlmod.unescape(re.sub(r"\s+", " ", body)).strip()
    aliases = [short, Path(rel).stem.replace("-", " ")]
    if jp:
        aliases.append(jp)
        aliases.append(jp.replace(" ", ""))
    if rel == "index.html":
        aliases.extend(["KB", "Kagurabachi wiki", "カグラバチ", "Kagura bachi"])
    if rel == "faq.html":
        aliases.extend(["wiki", "FAQ", "KB", "how to read Kagurabachi"])
    if rel == "media/anime.html":
        aliases.extend(["Kagurabachi anime", "Cypic", "Crunchyroll", "2027", "BachiAnime"])
    section = folder_of(rel) or "site"
    return {
        "url": canonical_url(rel).replace(SITE, "") or "/",
        "title": short or clean_title,
        "jp": jp,
        "desc": desc,
        "section": section,
        "aliases": [a for a in dict.fromkeys(aliases) if a],
        "text": body[:800],
    }


def write_search_index(pages: list[str], titles: dict[str, str]) -> list[dict]:
    entries = []
    for rel in pages:
        html = (ROOT / rel).read_text(encoding="utf-8")
        entry = search_entry(rel, html, titles.get(rel) or rel)
        if entry:
            entries.append(entry)
    (ROOT / "assets" / "search-index.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return entries


def write_search_page(pages: list[str], titles: dict[str, str]):
    def title_of(rel: str) -> str:
        t = titles.get(rel) or rel
        t = htmlmod.unescape(re.sub(r"<[^>]+>", "", t))
        t = re.sub(r"\s*[·|].*$", "", t).strip()
        return t

    groups: dict[str, list[str]] = defaultdict(list)
    root_pages = []
    for rel in pages:
        if rel in ("404.html", "search.html"):
            continue
        if "/" not in rel:
            root_pages.append(rel)
            continue
        groups[rel.split("/", 1)[0]].append(rel)

    def lis(rels: list[str]) -> str:
        bits = []
        for rel in rels:
            href = rel if not rel.endswith("/index.html") else rel[:-10] + "index.html"
            bits.append(f'<li><a href="{href}">{htmlmod.escape(title_of(rel))}</a></li>')
        return "\n        ".join(bits)

    sections_html = []
    if root_pages:
        sections_html.append(
            "<h2>Front door</h2>\n    <ul class=\"map-list\">\n        "
            + lis(root_pages)
            + "\n    </ul>"
        )
    for label, folder in SECTIONS:
        rels = groups.get(folder, [])
        if not rels:
            continue
        rels = sorted(rels, key=lambda r: (0 if r.endswith("/index.html") else 1, r))
        sections_html.append(
            f"<h2>{label}</h2>\n    <ul class=\"map-list\">\n        "
            + lis(rels)
            + "\n    </ul>"
        )
    body = "\n    ".join(sections_html)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Search the Kagurabachi Encyclopedia | Characters, Blades, Arcs</title>
  <meta name="description" content="Search Kagurabachi.org: characters, Enchanted Blades, story arcs, volume synopses, and essays. Wiki-depth index for Takeru Hokazono’s manga.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="css/site.css">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / Search</p>
    <header class="page-hero">
      <div>
        <p class="kicker">Index</p>
        <h1>Search<span class="jp">検索</span></h1>
        <p class="lede">Names, blades, arcs, KB. The box Google can hand off to, and the directory a crawler can still walk if the script stays in the truck.</p>
      </div>
    </header>
    <form class="home-search" action="search.html" method="get" role="search">
      <label for="archive-q">Search this encyclopedia</label>
      <input id="archive-q" type="search" name="q" placeholder="Chihiro, Enten, Rakuzaichi, KB…" autocomplete="off" enterkeyhint="search">
      <button type="submit">Search</button>
    </form>
    <p class="search-status" id="search-status">Type a name, blade, arc, or KB. The index is this encyclopedia.</p>
    <div id="search-results"></div>
    <div id="search-fallback">
      <article class="article map-page">
        <p>Every page, grouped the way the workshop is. Same doors as the <a href="sitemap.html">site map</a>. Official chapters stay on <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>.</p>
      {body}
      </article>
    </div>
  </main>
  <div id="site-footer"></div>
  <script src="js/site.js"></script>
  <script src="js/search.js"></script>
</body>
</html>
"""
    (ROOT / "search.html").write_text(page, encoding="utf-8")


def write_xml_sitemap(pages: list[str]):
    skip = {"404.html"}
    urls = []
    for rel in pages:
        if rel in skip:
            continue
        url = canonical_url(rel)
        last = git_lastmod(rel)
        if rel == "index.html":
            pri, freq = "1.0", "weekly"
        elif rel.endswith("/index.html") or rel in (
            "sitemap.html",
            "faq.html",
            "search.html",
            "manga/synopses.html",
            "characters/chihiro.html",
            "media/anime.html",
        ):
            pri, freq = "0.8", "weekly"
        else:
            pri, freq = "0.6", "monthly"
        urls.append(
            "  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{last}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{pri}</priority>\n"
            "  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_html_sitemap(pages: list[str], titles: dict[str, str]):
    def title_of(rel: str) -> str:
        t = titles.get(rel) or rel
        t = htmlmod.unescape(re.sub(r"<[^>]+>", "", t))
        t = re.sub(r"\s*[·|].*$", "", t).strip()
        return t

    groups: dict[str, list[str]] = defaultdict(list)
    root_pages = []
    for rel in pages:
        if rel in ("404.html", "sitemap.html"):
            continue
        if "/" not in rel:
            root_pages.append(rel)
            continue
        groups[rel.split("/", 1)[0]].append(rel)

    def lis(rels: list[str]) -> str:
        bits = []
        for rel in rels:
            href = rel if not rel.endswith("/index.html") else rel[:-10] + "index.html"
            bits.append(f'<li><a href="{href}">{htmlmod.escape(title_of(rel))}</a></li>')
        return "\n        ".join(bits)

    sections_html = []
    if root_pages:
        sections_html.append(
            "<h2>Front door</h2>\n    <ul class=\"map-list\">\n        "
            + lis(root_pages)
            + "\n    </ul>"
        )
    for label, folder in SECTIONS:
        rels = groups.get(folder, [])
        if not rels:
            continue
        # index first
        rels = sorted(rels, key=lambda r: (0 if r.endswith("/index.html") else 1, r))
        sections_html.append(
            f"<h2>{label}</h2>\n    <ul class=\"map-list\">\n        "
            + lis(rels)
            + "\n    </ul>"
        )

    body = "\n    ".join(sections_html)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Site map · Kagurabachi Archive</title>
  <meta name="description" content="Every Kagurabachi.org page in one directory: characters, Enchanted Blades, volumes, arcs, world, essays, and fun.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="css/site.css">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
</head>
<body>
  <div id="site-header"></div>
  <main id="main" class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / Site map</p>
    <header class="page-hero">
      <div>
        <p class="kicker">Directory</p>
        <h1>Site map<span class="jp">サイトマップ</span></h1>
        <p class="lede">Every page on this encyclopedia, grouped the way the workshop is. A door for readers and for crawlers that have only seen the homepage.</p>
      </div>
    </header>
    <article class="article map-page">
      <p>Start with the <a href="guide/index.html">guide</a> if you are new, <a href="characters/chihiro.html">Chihiro</a> if you want a person, or <a href="manga/synopses.html">volume synopses</a> if you want the commute by spine. Official chapters live on <a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a>. We do not host them.</p>
    {body}
    </article>
  </main>
  <div id="site-footer"></div>
  <script src="js/site.js"></script>
</body>
</html>
"""
    (ROOT / "sitemap.html").write_text(page, encoding="utf-8")


def main() -> None:
    pages = [
        rel_of(p)
        for p in html_files()
        if rel_of(p) not in ("sitemap.html", "search.html")
    ]
    titles: dict[str, str] = {}
    for rel in pages:
        path = ROOT / rel
        html = path.read_text(encoding="utf-8")
        html = enhance_synopses(html, rel)
        html = enhance_volumes(html, rel)
        html = enhance_chapters(html, rel)
        html = fill_empty_alts(html)
        html = upgrade_card_alts(html)
        html = merge_related(html, rel)
        html = inject_head(html, rel)
        html = lazy_images(html)
        html = inject_noscript(html, rel)
        path.write_text(html, encoding="utf-8")
        titles[rel] = attr(html, "title") or rel
        print("seo", rel)

    write_html_sitemap(pages + ["sitemap.html"], titles)
    sm = ROOT / "sitemap.html"
    html = sm.read_text(encoding="utf-8")
    html = merge_related(html, "sitemap.html")
    html = inject_head(html, "sitemap.html")
    html = inject_noscript(html, "sitemap.html")
    sm.write_text(html, encoding="utf-8")
    titles["sitemap.html"] = attr(html, "title") or "Site map"

    write_search_page(pages + ["sitemap.html", "search.html"], titles)
    se = ROOT / "search.html"
    html = se.read_text(encoding="utf-8")
    html = merge_related(html, "search.html")
    html = inject_head(html, "search.html")
    html = inject_noscript(html, "search.html")
    se.write_text(html, encoding="utf-8")
    titles["search.html"] = attr(html, "title") or "Search"

    all_pages = pages + ["sitemap.html", "search.html"]
    write_search_index(all_pages, titles)
    write_xml_sitemap(all_pages)
    write_image_sitemap(all_pages)
    write_robots()
    write_opensearch()
    write_manifest()
    print(
        "wrote robots.txt sitemap.xml sitemap-images.xml sitemap.html search.html",
        "pages",
        len(all_pages),
    )


if __name__ == "__main__":
    main()
