# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright 2026 range-et and contributors. Le Boat — https://github.com/range-et/le-boat.
"""Build GitHub Pages references from canonical project Markdown."""
from pathlib import Path
from html import escape
import re
import shutil
from urllib.parse import urlsplit, unquote
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
SOURCES = [ROOT / p for p in ('README.md', 'design-brief.md', 'LICENSE.md', 'DISCLAIMER.md', 'CONTRIBUTING.md')]
SOURCES += sorted((ROOT / 'project').glob('*.md'))
SOURCES += sorted((ROOT / 'journal').glob('*.md'))
SOURCES += sorted((ROOT / 'templates').glob('*.md'))
DEST = {p.resolve(): f'{p.stem}.html' for p in SOURCES}
NOTICE = 'Required Notice: Copyright 2026 range-et and contributors. Le Boat — https://github.com/range-et/le-boat. Software licensed under PolyForm Noncommercial 1.0.0.'


def rewrite_link(match, source):
    attr, quote, url = match.groups()
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return match.group(0)
    target = (source.parent / unquote(parts.path)).resolve()
    if target in DEST:
        result = DEST[target]
    elif target.is_file() and target.is_relative_to(ROOT):
        rel = target.relative_to(ROOT)
        copy = OUT / 'files' / rel
        copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target, copy)
        result = '../files/' + rel.as_posix()
    else:
        raise ValueError(f'Unresolved local reference in {source}: {url}')
    if parts.fragment:
        result += '#' + parts.fragment
    return f'{attr}={quote}{result}{quote}'


def main():
    (OUT / 'reference').mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        body = markdown.markdown(source.read_text(), extensions=['tables', 'fenced_code', 'sane_lists'])
        body = re.sub(r'(href|src)=([\"\'])(.*?)[\"\']', lambda m: rewrite_link(m, source), body)
        title = source.read_text().splitlines()[0].lstrip('# ')
        page = f'''<!doctype html>
<!-- {NOTICE} -->
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Le Boat</title><meta name="description" content="{escape(title)} — the experimental Le Boat design and build record.">
<link rel="stylesheet" href="../assets/style.css"></head><body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header"><a class="wordmark" href="../index.html">le boat<span>Toronto · a work in progress</span></a><nav aria-label="Main"><a href="../index.html#journal">Build journal</a><a href="design-brief.html">The brief</a><a href="https://github.com/range-et/le-boat">GitHub ↗</a></nav></header>
<main id="content" class="document"><a class="eyebrow back" href="../index.html">← Project home</a>{body}</main>
<footer><span>An experiment in CAD, AI co-creation and making.</span><a href="LICENSE.html">Licenses & attribution</a><a href="DISCLAIMER.html">Experimental-use notice</a></footer>
</body></html>'''
        (OUT / 'reference' / DEST[source.resolve()]).write_text(page)
    print(f'Built {len(SOURCES)} reference pages in {OUT}')


if __name__ == '__main__':
    main()
