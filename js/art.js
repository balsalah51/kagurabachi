/* Inline SVG portraits, original decorative marks, not official art */
window.KBArt = {
  fish(color) {
    const fill = color || "#e8c547";
    return `<svg viewBox="0 0 160 90" fill="none" aria-hidden="true"><path d="M22 48c18-22 40-24 58-10 6-16 28-24 48-8-22 20-40 18-54 6-10 18-32 28-52 12z" fill="${fill}"/><circle cx="118" cy="36" r="3.2" fill="#0c0b0a"/><path d="M20 48c-10 8-16 4-18-6 8 2 12-2 18 6z" fill="${fill}" opacity=".85"/></svg>`;
  },
  blade() {
    return `<svg viewBox="0 0 80 160" fill="none" aria-hidden="true"><path d="M40 8l6 110H34L40 8z" fill="#f6efe6"/><rect x="28" y="118" width="24" height="6" fill="#c9a227"/><rect x="36" y="124" width="8" height="26" fill="#2a2420"/><rect x="32" y="148" width="16" height="6" fill="#c9a227"/></svg>`;
  }
};
