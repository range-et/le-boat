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
SOURCES = [ROOT / p for p in ('README.md', 'design-brief.md', 'LICENSE.md', 'DISCLAIMER.md', 'CONTRIBUTING.md', 'THIRD_PARTY_NOTICES.md')]
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
<link rel="stylesheet" href="../assets/monad/monad.css"><link rel="stylesheet" href="../assets/style.css"></head><body>
<a class="skip" href="#content">Skip to content</a>
<header class="monad-header site-header"><a class="monad-header__name" href="../index.html">Le Boat</a><nav aria-label="Main"><a href="../index.html#tools">Tools</a><a href="../index.html#journal">Build journal</a><a href="design-brief.html">Design brief</a><a href="https://github.com/range-et/le-boat">GitHub</a></nav><button class="atomos-btn atomos-btn--ghost atomos-btn--sm" type="button" data-mn-theme-toggle aria-label="Light theme" aria-pressed="false">Light theme</button></header>
<main id="content" class="document"><a class="back" href="../index.html">← Project home</a>{body}</main>
<footer><span>Le Boat · Toronto</span><a href="LICENSE.html">Licenses & attribution</a><a href="THIRD_PARTY_NOTICES.html">Third-party notices</a><a href="DISCLAIMER.html">Experimental-use notice</a></footer>
<script src="../assets/monad/monad.js"></script>
</body></html>'''
        (OUT / 'reference' / DEST[source.resolve()]).write_text(page)
    print(f'Built {len(SOURCES)} reference pages in {OUT}')


if __name__ == '__main__':
    main()
