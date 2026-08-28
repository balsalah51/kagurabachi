(function () {
  /* Paste your Amazon Associates tag (example: "kagurabachi-20") to earn commission on volume buys. Empty tag still opens Amazon; no commission until you join and paste it. */
  const KAGURA = Object.assign({
    amazonTag: "",
    bookshopId: "",
    animeStart: "2027-04-01T00:00:00+09:00",
  }, window.KAGURA || {});
  window.KAGURA = KAGURA;

  function rootPrefix() {
    const depth = location.pathname.replace(/\\/g, "/").split("/").filter(Boolean).length;
    const inSub = /\/(characters|blades|manga|arcs|analysis|factions|collectibles|world|media|fun|guide)\//.test(location.pathname);
    return inSub || depth > 1 ? "../" : "";
  }

  const R = rootPrefix();
  const here = location.pathname.split("/").pop() || "index.html";
  const isHome = here === "index.html" && !/\/(characters|blades|manga|arcs|analysis|factions|collectibles|world|media|fun|guide)\//.test(location.pathname);
  const hideShop = isHome || /\/(characters|blades|factions)\//.test(location.pathname);

  function navLink(href, label, folder) {
    const file = href.split("/").pop();
    const on = file === here || (folder && location.pathname.includes("/" + folder + "/"));
    const current = on ? ' aria-current="page"' : "";
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
        <form class="site-search" action="${R}search.html" method="get" role="search">
          <label class="sr-only" for="nav-q">Search the Kagurabachi encyclopedia</label>
          <input id="nav-q" type="search" name="q" placeholder="Search Kagurabachi…" autocomplete="off" enterkeyhint="search">
          <button type="submit">Search</button>
        </form>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">Menu</button>
        <ul class="primary-nav" id="primary-nav">
          ${navLink("index.html", "Home")}
          ${navLink("characters/index.html", "Characters", "characters")}
          ${navLink("manga/index.html", "Manga", "manga")}
          ${navLink("arcs/index.html", "Story", "arcs")}
          ${navLink("analysis/index.html", "Essays", "analysis")}
          ${navLink("fun/index.html", "Fun", "fun")}
        </ul>
      </div>
    </header>
    <nav class="subnav" aria-label="Encyclopedia">
      <div class="subnav-inner">
        <a href="${R}guide/index.html">Guide</a>
        <a href="${R}blades/index.html">Blades</a>
        <a href="${R}world/techniques.html">Techniques</a>
        <a href="${R}manga/volumes.html">Volumes</a>
        <a href="${R}manga/part-2.html">Part 2</a>
        <a href="${R}world/index.html">World</a>
        <a href="${R}factions/hishaku.html">Hishaku</a>
        <a href="${R}factions/kamunabi.html">Kamunabi</a>
        <a href="${R}media/anime.html">Anime</a>
        <a href="${R}fun/community.html">Board</a>
        <a href="${R}search.html">Search</a>
        <a href="${R}faq.html">FAQ</a>
        <a href="${R}sitemap.html">Map</a>
        <a href="${R}about.html">About</a>
      </div>
    </nav>
  `;

  const footer = `
    <footer class="site">
      <div class="footer-inner">
        <div>
          <h3>Kagurabachi</h3>
          <p>A fan site for Takeru Hokazono’s <em>Kagurabachi</em>. Characters, blades, volumes, and the goldfish.</p>
          <p class="legal">Kagurabachi © Takeru Hokazono / Shueisha. Anime images © Takeru Hokazono / Project Kagurabachi. Fan-made reference. Official chapters: <a href="https://www.viz.com/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/">MANGA Plus</a>. <a href="${R}sitemap.html">Site map</a> · <a href="${R}privacy.html">Privacy</a>.</p>
        </div>
        <div>
          <h3>Read officially</h3>
          <p><a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ Shonen Jump</a><br>
          <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a><br>
          <a href="https://www.shonenjump.com/j/rensai/kagurabachi.html">Weekly Shōnen Jump (JP)</a></p>
        </div>
        <div>
          <h3>On this site</h3>
          <p><a href="${R}guide/index.html">Guide</a> · <a href="${R}guide/part-1.html">Part 1</a><br>
          <a href="${R}characters/index.html">Characters</a><br>
          <a href="${R}factions/hishaku.html">Hishaku</a> · <a href="${R}factions/kamunabi.html">Kamunabi</a><br>
          <a href="${R}world/techniques.html">Techniques</a> · <a href="${R}world/storehouse.html">Storehouse</a> · <a href="${R}world/workshop.html">Workshop</a><br>
          <a href="${R}manga/part-2.html">Part 2</a> · <a href="${R}manga/synopses.html">Synopses</a><br>
          <a href="${R}media/anime.html">Anime countdown</a>${hideShop ? "" : ` · <a href="${R}collectibles/shop.html">Shop</a>`}<br>
          <a href="${R}fun/index.html">Fun of the manga</a> · <a href="${R}fun/community.html">Sunday board</a><br>
          <a href="${R}blades/index.html">Enchanted Blades</a> · <a href="${R}arcs/index.html">Story arcs</a><br>
          <a href="${R}analysis/index.html">Essays</a> · <a href="${R}world/glossary.html">Glossary</a><br>
          <a href="${R}search.html">Search</a> · <a href="${R}faq.html">FAQ</a><br>
          <a href="${R}about.html">About</a> · <a href="${R}sitemap.html">Site map</a> · <a href="${R}privacy.html">Privacy</a></p>
        </div>
      </div>
    </footer>
  `;

  document.querySelectorAll(".layout").forEach((el) => {
    const box = el.querySelector(":scope > .infobox");
    if (box && el.firstElementChild !== box) el.prepend(box);
  });

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

  document.querySelectorAll(".spoiler").forEach((el) => {
    el.tabIndex = 0;
    el.title = "Click to reveal spoiler";
    const reveal = () => el.classList.add("revealed");
    el.addEventListener("click", reveal);
    el.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); reveal(); }
    });
  });

  function amazonUrl(query) {
    const url = new URL("https://www.amazon.com/s");
    url.searchParams.set("k", query);
    if (KAGURA.amazonTag) url.searchParams.set("tag", KAGURA.amazonTag);
    return url.toString();
  }

  document.querySelectorAll("[data-amazon]").forEach((el) => {
    el.href = amazonUrl(el.getAttribute("data-amazon"));
    el.rel = "sponsored noopener noreferrer";
    el.target = "_blank";
  });

  document.querySelectorAll("[data-bookshop]").forEach((el) => {
    const q = encodeURIComponent(el.getAttribute("data-bookshop") || "Kagurabachi");
    const id = KAGURA.bookshopId;
    el.href = id
      ? `https://bookshop.org/a/${encodeURIComponent(id)}/search?keywords=${q}`
      : `https://bookshop.org/search?keywords=${q}`;
    el.rel = "noopener noreferrer";
    el.target = "_blank";
  });

  const start = new Date(KAGURA.animeStart).getTime();
  document.querySelectorAll("[data-clock]").forEach((root) => {
    const dEl = root.querySelector("[data-d]");
    const hEl = root.querySelector("[data-h]");
    const mEl = root.querySelector("[data-m]");
    const sEl = root.querySelector("[data-s]");
    const live = root.querySelector("[data-clock-live]");
    function pad(n, w) {
      return String(Math.max(0, n)).padStart(w, "0");
    }
    function tick() {
      const diff = start - Date.now();
      if (diff <= 0) {
        if (dEl) dEl.textContent = "000";
        if (hEl) hEl.textContent = "00";
        if (mEl) mEl.textContent = "00";
        if (sEl) sEl.textContent = "00";
        if (live) live.textContent = "The April 2027 season is here. A first-episode date lands when they print one.";
        return;
      }
      const s = Math.floor(diff / 1000);
      const days = Math.floor(s / 86400);
      const hours = Math.floor((s % 86400) / 3600);
      const mins = Math.floor((s % 3600) / 60);
      const secs = s % 60;
      if (dEl) dEl.textContent = pad(days, 3);
      if (hEl) hEl.textContent = pad(hours, 2);
      if (mEl) mEl.textContent = pad(mins, 2);
      if (sEl) sEl.textContent = pad(secs, 2);
    }
    tick();
    setInterval(tick, 1000);
  });
})();
