(function () {
  const input = document.getElementById("archive-q");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const fallback = document.getElementById("search-fallback");
  if (!input || !results) return;

  const params = new URLSearchParams(location.search);
  const initial = (params.get("q") || "").trim();
  if (initial && !input.value) input.value = initial;
  const navQ = document.getElementById("nav-q");
  if (navQ && initial && !navQ.value) navQ.value = initial;

  function normalize(s) {
    return String(s || "")
      .toLowerCase()
      .normalize("NFKC")
      .replace(/[_.,/·|]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function tokens(s) {
    return normalize(s).split(" ").filter((t) => t.length >= 1);
  }

  function score(entry, q) {
    const nq = normalize(q);
    if (!nq) return 0;
    const title = normalize(entry.title);
    const jp = normalize(entry.jp);
    const desc = normalize(entry.desc);
    const aliases = (entry.aliases || []).map(normalize);
    const hay = normalize(entry.text);
    const section = normalize(entry.section);
    const stem = normalize((entry.url.split("/").pop() || "").replace(/\.html$/, "").replace(/index$/, ""));
    let s = 0;
    if (title === nq || jp === nq) s += 120;
    if (stem && stem === nq) s += 85;
    if (title.startsWith(nq)) s += 70;
    if (title.includes(nq)) s += 40;
    if (jp.includes(nq) && nq.length >= 1) s += 50;
    if (section === nq) s += 15;
    for (const a of aliases) {
      if (a === nq) s += 90;
      else if (a.startsWith(nq)) s += 35;
      else if (a.includes(nq)) s += 18;
    }
    if (desc.includes(nq)) s += 12;
    if (hay.includes(nq)) s += 6;
    const toks = tokens(q);
    if (toks.length > 1) {
      const blob = `${title} ${jp} ${aliases.join(" ")} ${desc} ${hay}`;
      let hit = 0;
      for (const t of toks) {
        if (blob.includes(t)) hit += 1;
      }
      if (hit === toks.length) s += 25;
      else if (hit === 0) s = 0;
      else s += hit * 3;
    }
    return s;
  }

  function snippet(entry, q) {
    const nq = normalize(q);
    const text = entry.desc || entry.text || "";
    if (!nq || !text) return text.slice(0, 180);
    const lower = text.toLowerCase();
    const at = lower.indexOf(nq);
    if (at < 0) return text.slice(0, 180);
    const start = Math.max(0, at - 40);
    const chunk = (start ? "…" : "") + text.slice(start, start + 180).trim();
    return chunk;
  }

  function render(entries, q) {
    results.innerHTML = "";
    if (!q) {
      if (status) status.textContent = "Type a name, blade, arc, or KB. The index is this encyclopedia.";
      if (fallback) fallback.hidden = false;
      return;
    }
    if (fallback) fallback.hidden = true;
    if (!entries.length) {
      if (status) {
        status.innerHTML = `No page titled “${escapeHtml(q)}”. Try the <a href="sitemap.html">site map</a> or the <a href="faq.html">FAQ</a>.`;
      }
      return;
    }
    if (status) {
      status.textContent = entries.length === 1
        ? "1 page."
        : `${entries.length} pages.`;
    }
    const ul = document.createElement("ul");
    ul.className = "search-hits";
    for (const entry of entries.slice(0, 40)) {
      const li = document.createElement("li");
      const href = entry.url.replace(/^https:\/\/kagurabachi\.org/, "") || "/";
      const title = escapeHtml(entry.title);
      const jp = entry.jp ? `<span class="jp">${escapeHtml(entry.jp)}</span>` : "";
      const section = entry.section ? `<small>${escapeHtml(labelSection(entry.section))}</small>` : "";
      const snip = escapeHtml(snippet(entry, q));
      li.innerHTML = `<a href="${href}"><b>${title}</b>${jp}${section}</a><p>${snip}</p>`;
      ul.appendChild(li);
    }
    results.appendChild(ul);
  }

  function labelSection(section) {
    const map = {
      characters: "Character",
      blades: "Enchanted Blade",
      manga: "Manga",
      arcs: "Story arc",
      analysis: "Essay",
      world: "World",
      factions: "Faction",
      fun: "Fun",
      guide: "Guide",
      media: "Media",
      collectibles: "Collectibles",
    };
    return map[section] || "Page";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  let index = [];
  function run(q) {
    const query = (q || "").trim();
    if (!query) {
      render([], "");
      return;
    }
    const ranked = index
      .map((entry) => ({ entry, s: score(entry, query) }))
      .filter((row) => row.s > 0)
      .sort((a, b) => b.s - a.s)
      .map((row) => row.entry);
    render(ranked, query);
  }

  const form = input.form;
  if (form) {
    form.addEventListener("submit", (e) => {
      const q = input.value.trim();
      const next = q ? `search.html?q=${encodeURIComponent(q)}` : "search.html";
      if (location.pathname.split("/").pop() === "search.html") {
        e.preventDefault();
        history.replaceState(null, "", next);
        run(q);
      }
    });
  }

  input.addEventListener("input", () => {
    const q = input.value.trim();
    if (location.pathname.split("/").pop() === "search.html") {
      const next = q ? `search.html?q=${encodeURIComponent(q)}` : "search.html";
      history.replaceState(null, "", next);
      run(q);
    }
  });

  fetch("assets/search-index.json", { credentials: "same-origin" })
    .then((r) => {
      if (!r.ok) throw new Error("index");
      return r.json();
    })
    .then((data) => {
      index = Array.isArray(data) ? data : data.pages || [];
      run(input.value);
    })
    .catch(() => {
      if (status) {
        status.textContent = "The live index did not load. The directory below is every page, still.";
      }
      if (fallback) fallback.hidden = false;
    });
})();
