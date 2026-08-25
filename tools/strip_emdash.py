#!/usr/bin/env python3
"""Strip em-dashes (U+2014) from the site. Titles use a middot; prose uses commas or colons."""
from pathlib import Path
import re

ROOT = Path("/workspace")
SKIP = {".git", "tools"}  # tools generators may still mention the character in comments; we still clean html/css/js


def transform(text: str) -> str:
    # Title / brand separators
    text = text.replace(" — Kagurabachi Archive", " · Kagurabachi Archive")
    text = text.replace(" — Kagurabachi", " · Kagurabachi")
    # Common caption / label pattern: "Chapter 9 — the first"
    text = re.sub(r"(Chapter \d+) — ", r"\1: ", text)
    text = re.sub(r"(Ch\. \d+) — ", r"\1: ", text)
    text = re.sub(r"(Vol\. 0?\d+) — ", r"\1: ", text)
    # Remaining spaced em-dashes: treat as a colon after a short noun phrase, else a comma.
    def spaced(m):
        return ": "
    # Generic spaced em-dash -> comma (reads as an aside)
    text = text.replace(" — ", ", ")
    # Unspaced leftovers (compound labels like Talks—END)
    text = text.replace("—", ": ")
    return text


changed = []
for path in ROOT.rglob("*"):
    if any(part in SKIP for part in path.parts):
        continue
    if path.suffix.lower() not in {".html", ".css", ".js", ".md", ".svg"}:
        continue
    if not path.is_file():
        continue
    raw = path.read_text(encoding="utf-8")
    if "—" not in raw:
        continue
    new = transform(raw)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        changed.append((str(path.relative_to(ROOT)), raw.count("—"), new.count("—")))

for rel, before, after in changed:
    print(f"{rel}: {before} -> {after}")
print("files", len(changed))
# leftover scan
left = []
for path in ROOT.rglob("*"):
    if any(part in SKIP for part in path.parts):
        continue
    if path.suffix.lower() not in {".html", ".css", ".js", ".md", ".svg"}:
        continue
    if path.is_file() and "—" in path.read_text(encoding="utf-8"):
        left.append(str(path.relative_to(ROOT)))
print("leftover", left)
