"""Generate baba_sample.typ from the manuscript excerpt.

All wording is read from the manuscript runs (never retyped); only layout
and typographic glitches are corrected. Usage:
    python3 gen.py manuscript.docx baba_sample.typ
"""
import math
import re
import sys

import docx

SRC, OUT = sys.argv[1], sys.argv[2]
P = docx.Document(SRC).paragraphs


def runs(k):
    """Merged (text, bold, italic) runs of manuscript paragraph k."""
    out = []
    for item in P[k].iter_inner_content():
        for r in (item.runs if hasattr(item, 'runs') else [item]):  # hyperlinks hold runs
            t = r.text
            if not t:
                continue
            b, i = bool(r.bold), bool(r.italic)
            if not t.strip() and out:      # whitespace run: inherit neighbour's style
                b, i = out[-1][1], out[-1][2]
            if out and out[-1][1:] == (b, i):
                out[-1] = (out[-1][0] + t, b, i)
            else:
                out.append((t, b, i))
    return out


def join(*ks, bold_tail=None):
    """Join manuscript paragraphs that copy-paste split in two."""
    out = []
    for n, k in enumerate(ks):
        rs = runs(k)
        if bold_tail is not None and n > 0:
            rs = [(t, bold_tail, i) for t, _, i in rs]
        if out:
            out[-1] = (out[-1][0].rstrip() + ' ', *out[-1][1:])
            rs[0] = (rs[0][0].lstrip(), *rs[0][1:])
        out += rs
    return out


FIX = [
    (r'---', '\u2014'),
    (r'(\d) 1/2\b', '\\1 \u00bd'),
    (r'(?<![\d/])3/4\b', '\u00be'),
    (r'(\d)\u201d ?X (\d+)\u201d ?pan', '\\1\u201d \u00d7 \\2\u201d pan'),
    (r'8\u201d-9\u201d', '8\u201d\u20139\u201d'),
    (r'(\d)-(\d+) more', '\\1\u2013\\2 more'),
    (r'minutes\.Remove', 'minutes. Remove'),
    (r' {2,}', ' '),
]

ESC = re.compile(r'([\\/*_#\[\]$@<>~`])')


def esc(t):
    return ESC.sub(r'\\\1', t)


def typ(rs):
    """Runs -> Typst markup, keeping spaces outside the bold/italic spans."""
    fixed = []
    for t, b, i in rs:
        for pat, rep in FIX:
            t = re.sub(pat, rep, t)
        fixed.append((t, b, i))
    # merge neighbours that now share a style
    merged = []
    for r in fixed:
        if merged and merged[-1][1:] == r[1:]:
            merged[-1] = (merged[-1][0] + r[0], *r[1:])
        else:
            merged.append(r)
    out = ''
    for t, b, i in merged:
        lead = t[:len(t) - len(t.lstrip())]
        trail = t[len(t.rstrip()):]
        core = esc(t.strip())
        if not core:
            out += ' ' if t else ''
            continue
        if b and i:
            core = f'#strong[#emph[{core}]]'
        elif b:
            core = f'#strong[{core}]'
        elif i:
            core = f'#emph[{core}]'
        out += (' ' if lead else '') + core + (' ' if trail else '')
    out = re.sub(r' {2,}', ' ', out).strip()
    if re.match(r'^(\d+\.|[=+\-/])', out):
        out = '\\' + out
    return out


def plain(rs):
    return ''.join(t for t, _, _ in rs)


def lines(rs, chars=44):
    return math.ceil(len(plain(rs)) / chars) + 0.4


def two_col(items):
    """Split a list in two balanced columns (left never shorter)."""
    h = [lines(r) for r in items]
    best, cut = None, 1
    for c in range(1, len(items)):
        l, r = sum(h[:c]), sum(h[c:])
        if l + 0.01 < r:
            continue
        score = l - r
        if best is None or score < best:
            best, cut = score, c
    col = lambda rs: '(' + ''.join(f'\n    [{typ(r)}],' for r in rs) + '\n  )'
    return f'#two-col(\n  {col(items[:cut])},\n  {col(items[cut:])},\n)\n'


def paras(items):
    return '\n\n'.join(typ(r) for r in items)


out = ['''// Baba Returns — interior sample. Text from the author's manuscript, pp. 31–40.
#import "style.typ": *
#show: book.with(first-page: 31, book-title: "Baba Returns")
''']

# ================================================================ Holubtsi Zupa
out.append('''
// ------------------------------------------------------------ Holubtsi Zupa
#opener(
  photo: "img/holubtsi.jpg", photo-h: 5.55in,
  title: [Holubtsi Zupa], subtitle: [Cabbage Roll Soup (GF)],
  name: "Holubtsi Zupa",
)
''')
out.append('#intro[\n' + paras([runs(26), join(27, 30), runs(31), runs(32)]) + '\n]\n')
out.append('\n#section[Ingredients:]\n')
out.append(two_col([runs(36), runs(37), join(38, 39), runs(40), runs(41), join(42, 43)]
                   + [runs(k) for k in range(44, 50)]))
out.append('\n#section[Your Option:]\n')
out.append(two_col([runs(k) for k in (53, 54, 55, 56, 57, 58, 59, 62, 63)]))
out.append('\n#alert[\n' + typ(runs(65)) + '\n]\n')
out.append('\n#section[Recipe:]\n')
out.append('#method[\n' + paras([runs(70), runs(71), runs(72), join(73, 74, bold_tail=True),
                                  runs(75), runs(76), runs(77)]) + '\n]\n')
out.append('\n#proverbs([' + esc(P[80].text.strip()) + '], (\n'
           + ''.join(f'  [{typ(runs(k))}],\n' for k in (82, 83, 84)) + '))\n')

# ================================================================ Paska
out.append('''
// ------------------------------------------------------------ Gluten Free Paska
#opener(
  photo: "img/paska.jpg", photo-h: 6.1in,
  title: [Bez Hluteny Paska], subtitle: [Gluten Free Paska],
  name: "Gluten Free Paska",
)
''')
out.append('#intro[\n' + paras([runs(91)]) + '\n]\n')
out.append('\n#section[Ingredients:]\n')
# para 97 (red editor's note about the illustration) is not book text.
out.append(two_col([runs(k) for k in range(99, 105)] + [join(105, 106), runs(107), runs(108)]
                   + [runs(k) for k in range(110, 120)]))
out.append('\n#section[Your Option:]\n')
out.append(paras([runs(124)]) + '\n')
out.append('\n#section[Paska Recipe:]\n')
out.append('#method[\n' + paras([runs(k) for k in range(128, 139)]) + '\n]\n')
# caption is italic in the manuscript; the style sets it italic, so pass plain text
out.append('\n#illustration("img/saffron.jpg", 2.85in, [' + esc(plain(runs(146)).strip()) + '])\n')

# ================================================================ Varenyky
out.append('''
// ------------------------------------------------------------ Gluten Free Varenyky
#opener(
  photo: "img/varenyky.jpg", photo-h: 5.65in,
  title: [Bez Hluteny Varenyky],
  subtitle: [Gluten Free Varenyky #linebreak() (Perohy-Perogies)],
  name: "Gluten Free Varenyky",
)
''')
out.append('#intro[\n' + paras([runs(187), runs(188)]) + '\n]\n')
out.append('\n#section[Ingredients:]\n')
out.append('#subsection[Dough]\n')
out.append(two_col([runs(k) for k in range(194, 203)] + [join(203, 204), runs(205)]))
out.append('#subsection[Potato Cheddar Filling]\n')
out.append(two_col([runs(k) for k in range(211, 219)]))
out.append('\n#section[Filling Recipe. Make this first:]\n')
out.append('#method[\n' + paras([runs(222)]) + '\n]\n')
out.append('\n#section[Recipe:]\n')
out.append('#method[\n' + paras([runs(k) for k in (226, 227, 228, 229, 230, 231, 234)]) + '\n]\n')

open(OUT, 'w').write(''.join(out))
print('wrote', OUT)
