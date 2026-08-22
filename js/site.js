(function () {
  const PAGES = [
    { t: "Home", u: "index.html", k: "archive portal kagurabachi" },
    { t: "Characters", u: "characters/index.html", k: "directory roster" },
    { t: "Chihiro Rokuhira", u: "characters/chihiro.html", k: "enten protagonist son" },
    { t: "Kunishige Rokuhira", u: "characters/kunishige.html", k: "swordsmith father datenseki" },
    { t: "Togo Shiba", u: "characters/shiba.html", k: "teleport cafe" },
    { t: "Hakuri Sazanami", u: "characters/hakuri.html", k: "storehouse isou rakuzaichi" },
    { t: "Hiyuki Kagari", u: "characters/hiyuki.html", k: "flame bone kamunabi" },
    { t: "Genichi Sojo", u: "characters/sojo.html", k: "cloud gouger kuregumo" },
    { t: "Yura", u: "characters/yura.html", k: "hishaku leader" },
    { t: "Seiichi Samura", u: "characters/samura.html", k: "tobimune iai white purity" },
    { t: "Yoji Uruha", u: "characters/uruha.html", k: "kumeyuri bearer" },
    { t: "Char Kyonagi", u: "characters/char.html", k: "healing regeneration" },
    { t: "Iori Samura", u: "characters/iori.html", k: "daughter iai" },
    { t: "Akemura Soga", u: "characters/akemura.html", k: "sword master magatsumi shinuchi" },
    { t: "Kyora Sazanami", u: "characters/kyora.html", k: "rakuzaichi auction" },
    { t: "Enchanted Blades", u: "blades/index.html", k: "yoto datenseki" },
    { t: "Enten", u: "blades/enten.html", k: "kuro aka nishiki goldfish" },
    { t: "Cloud Gouger", u: "blades/cloud-gouger.html", k: "kuregumo mei yui kou" },
    { t: "Magatsumi", u: "blades/magatsumi.html", k: "shinuchi malediction" },
    { t: "Kumeyuri", u: "blades/kumeyuri.html", k: "banquet play" },
    { t: "Tobimune", u: "blades/tobimune.html", k: "crow owl suzaku" },
    { t: "Manga Guide", u: "manga/index.html", k: "volumes chapters jump" },
    { t: "Volume Guide", u: "manga/volumes.html", k: "tankobon isbn" },
    { t: "Chapter Index", u: "manga/chapters.html", k: "weekly serialization" },
    { t: "Cover Studies", u: "manga/covers.html", k: "color palette volume art" },
    { t: "Color Pages & Pulls", u: "manga/color-pages.html", k: "jump color illustration" },
    { t: "Story Arcs", u: "arcs/index.html", k: "sojo rakuzaichi" },
    { t: "Vs. Sojo Arc", u: "arcs/vs-sojo.html", k: "char cloud gouger" },
    { t: "Rakuzaichi Arc", u: "arcs/rakuzaichi.html", k: "auction hakuri" },
    { t: "Sword Bearer Assassination Arc", u: "arcs/sword-bearer.html", k: "part 1 climax" },
    { t: "Seitei War Arc", u: "arcs/seitei-war.html", k: "part 2 irishima" },
    { t: "Story Analysis", u: "analysis/index.html", k: "essays themes" },
    { t: "What Enten Was Forged For", u: "analysis/enten-purpose.html", k: "destroy blades" },
    { t: "The Malediction", u: "analysis/malediction.html", k: "soga 200000" },
    { t: "Revenge and Inheritance", u: "analysis/revenge.html", k: "chihiro kunishige" },
    { t: "Factions", u: "factions/index.html", k: "kamunabi hishaku sazanami" },
    { t: "Collectibles", u: "collectibles/index.html", k: "volumes merch figures" },
    { t: "World & Timeline", u: "world/index.html", k: "history datenseki" },
    { t: "Datenseki", u: "world/datenseki.html", k: "ore ore" },
    { t: "Sorcery", u: "world/sorcery.html", k: "spirit energy yojutsu" },
    { t: "About the Archive", u: "about.html", k: "kanzenshuu fandom protocol" }
  ];

  function rootPrefix() {
    const depth = location.pathname.replace(/\\/g, "/").split("/").filter(Boolean).length;
    const inSub = /\/(characters|blades|manga|arcs|analysis|factions|collectibles|world)\//.test(location.pathname);
    return inSub || depth > 1 ? "../" : "";
  }

  const R = rootPrefix();
  const here = location.pathname.split("/").pop() || "index.html";

  function navLink(href, label) {
    const file = href.split("/").pop();
    const current = file === here ? ' aria-current="page"' : "";
    return `<li><a href="${R}${href}"${current}>${label}</a></li>`;
  }

  const header = `
    <a class="skip" href="#main">Skip to content</a>
    <header class="masthead">
      <div class="masthead-inner" id="mast">
        <a class="brand" href="${R}index.html">
          <svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true">
            <circle cx="32" cy="32" r="30" fill="#9b1419"/>
            <path d="M14 34c8-10 16-8 20-2 4-8 14-10 18 0-8 10-16 8-20 2-4 8-12 12-18 0z" fill="#e8c547"/>
            <path d="M18 30c6 2 10 8 8 14" stroke="#0c0b0a" stroke-width="2" fill="none"/>
          </svg>
          <span class="brand-name">Kagura<em>bachi</em><span class="brand-kana">カグラバチ 資料庫</span></span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">Menu</button>
        <ul class="primary-nav" id="primary-nav">
          ${navLink("index.html", "Archive")}
          ${navLink("characters/index.html", "Characters")}
          ${navLink("blades/index.html", "Blades")}
          ${navLink("manga/index.html", "Manga Guide")}
          ${navLink("arcs/index.html", "Arcs")}
          ${navLink("analysis/index.html", "Analysis")}
          ${navLink("collectibles/index.html", "Collectibles")}
        </ul>
        <div class="search">
          <label class="visually-hidden" for="q" style="position:absolute;left:-999px">Search the archive</label>
          <input id="q" type="search" placeholder="Search characters, blades, arcs…" autocomplete="off">
          <div class="search-results" id="results" role="listbox"></div>
        </div>
      </div>
    </header>
    <nav class="subnav" aria-label="Encyclopedia">
      <div class="subnav-inner">
        <a href="${R}world/index.html">World &amp; Timeline</a>
        <a href="${R}factions/index.html">Factions</a>
        <a href="${R}manga/volumes.html">Volumes</a>
        <a href="${R}manga/chapters.html">Chapters</a>
        <a href="${R}manga/covers.html">Cover Studies</a>
        <a href="${R}manga/color-pages.html">Color Pages</a>
        <a href="${R}world/datenseki.html">Datenseki</a>
        <a href="${R}world/sorcery.html">Sorcery</a>
        <a href="${R}about.html">About / Protocol</a>
      </div>
    </nav>
  `;

  const footer = `
    <footer class="site">
      <div class="footer-inner">
        <div>
          <h3>Kagurabachi Archive</h3>
          <p>An independent English-language database for Takeru Hokazono’s <em>Kagurabachi</em>. Built in the spirit of a Fandom encyclopedia and a Kanzenshuu-style publication guide — characters, blades, chapters, covers, and analysis, nothing else.</p>
          <p class="legal">Kagurabachi © Takeru Hokazono / Shueisha. This is a fan-made reference. Official chapters: <a href="https://www.viz.com/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/">MANGA Plus</a>. Volume cover reconstructions on this site are original color studies, not official art.</p>
        </div>
        <div>
          <h3>Read officially</h3>
          <p><a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ Shonen Jump</a><br>
          <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a><br>
          <a href="https://www.shonenjump.com/j/rensai/kagurabachi.html">Weekly Shōnen Jump (JP)</a></p>
        </div>
        <div>
          <h3>On this site</h3>
          <p><a href="${R}characters/index.html">Character encyclopedia</a><br>
          <a href="${R}manga/index.html">Manga guide</a><br>
          <a href="${R}analysis/index.html">Story analysis</a><br>
          <a href="${R}collectibles/index.html">Collectibles</a></p>
        </div>
      </div>
    </footer>
  `;

  const mountHead = document.getElementById("site-header");
  const mountFoot = document.getElementById("site-footer");
  if (mountHead) mountHead.innerHTML = header;
  if (mountFoot) mountFoot.innerHTML = footer;
  if (!document.querySelector('link[rel="icon"]')) {
    const icon = document.createElement("link");
    icon.rel = "icon";
    icon.type = "image/svg+xml";
    icon.href = R + "assets/favicon.svg";
    document.head.appendChild(icon);
  }

  const mast = document.getElementById("mast");
  const toggle = document.querySelector(".nav-toggle");
  if (toggle && mast) {
    toggle.addEventListener("click", () => {
      const open = mast.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const q = document.getElementById("q");
  const box = document.getElementById("results");
  if (q && box) {
    const render = (items) => {
      box.innerHTML = items.length
        ? items.map((p) => `<a href="${R}${p.u}"><strong>${p.t}</strong><small>${p.u}</small></a>`).join("")
        : `<a href="${R}characters/index.html"><strong>No match</strong><small>Browse the encyclopedia</small></a>`;
      box.classList.toggle("open", q.value.trim().length > 0);
    };
    q.addEventListener("input", () => {
      const s = q.value.trim().toLowerCase();
      if (!s) { box.classList.remove("open"); return; }
      render(PAGES.filter((p) => (p.t + " " + p.k).toLowerCase().includes(s)).slice(0, 8));
    });
    document.addEventListener("click", (e) => {
      if (!e.target.closest(".search")) box.classList.remove("open");
    });
  }

  document.querySelectorAll(".spoiler").forEach((el) => {
    el.tabIndex = 0;
    el.title = "Click to reveal spoiler";
    const reveal = () => el.classList.add("revealed");
    el.addEventListener("click", reveal);
    el.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); reveal(); }
    });
  });
})();
