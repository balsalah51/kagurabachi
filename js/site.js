(function () {
  function rootPrefix() {
    const depth = location.pathname.replace(/\\/g, "/").split("/").filter(Boolean).length;
    const inSub = /\/(characters|blades|manga|arcs|analysis|factions|collectibles|world|media|fun|guide)\//.test(location.pathname);
    return inSub || depth > 1 ? "../" : "";
  }

  const R = rootPrefix();
  const here = location.pathname.split("/").pop() || "index.html";

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
        <a href="${R}manga/volumes.html">Volumes</a>
        <a href="${R}world/index.html">World</a>
        <a href="${R}world/glossary.html">Glossary</a>
        <a href="${R}factions/index.html">Factions</a>
        <a href="${R}media/anime.html">Anime</a>
        <a href="${R}fun/goldfish.html">Goldfish</a>
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
          <p class="legal">Kagurabachi © Takeru Hokazono / Shueisha. Anime images © Takeru Hokazono / Project Kagurabachi. Fan-made reference. Official chapters: <a href="https://www.viz.com/kagurabachi">VIZ</a> and <a href="https://mangaplus.shueisha.co.jp/">MANGA Plus</a>.</p>
        </div>
        <div>
          <h3>Read officially</h3>
          <p><a href="https://www.viz.com/shonenjump/chapters/kagurabachi">VIZ Shonen Jump</a><br>
          <a href="https://mangaplus.shueisha.co.jp/titles/100274">MANGA Plus</a><br>
          <a href="https://www.shonenjump.com/j/rensai/kagurabachi.html">Weekly Shōnen Jump (JP)</a></p>
        </div>
        <div>
          <h3>On this site</h3>
          <p><a href="${R}guide/index.html">Guide</a><br>
          <a href="${R}characters/index.html">Characters</a><br>
          <a href="${R}fun/index.html">Fun of the manga</a><br>
          <a href="${R}media/index.html">Theories &amp; video</a><br>
          <a href="${R}analysis/index.html">Essays</a><br>
          <a href="${R}manga/index.html">Manga guide</a></p>
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
