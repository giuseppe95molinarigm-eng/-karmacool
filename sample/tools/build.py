"""Build the Raisa Stone sample (8.5 x 11 in, B&W interior) as a styled DOCX.

Text is read directly from the manuscript runs (no retyping), so wording,
ingredients and instructions stay exactly as the author wrote them; only
layout, spacing and typographic glitches are corrected.
"""
import re
import sys

import docx
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

SRC, IMG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
FONT = 'TeX Gyre Pagella'  # free Palatino-family face, close to the client's Book Antiqua
FIRST_PAGE = 31            # same folio the excerpt has in the manuscript

src = docx.Document(SRC)
P = src.paragraphs


# ---------------------------------------------------------------- text access
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
    """Join manuscript paragraphs that were split by copy-paste."""
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
    (r'---', '\u2014'),                    # triple hyphen -> em dash
    (r'(\d) 1/2\b', '\\1 \u00bd'),          # 1 1/2 -> 1 ½ (as elsewhere in the book)
    (r'(?<![\d/])3/4\b', '\u00be'),
    (r'(\d)\u201d ?X (\d+)\u201d ?pan', '\\1\u201d \u00d7 \\2\u201d pan'),
    (r'8\u201d-9\u201d', '8\u201d\u20139\u201d'),
    (r'(\d)-(\d+) more', '\\1\u2013\\2 more'),
    (r'minutes\.Remove', 'minutes. Remove'),
    (r' {2,}', ' '),
]


def clean(rs):
    rs = [(t, b, i) for t, b, i in rs]
    text = ''.join(t for t, _, _ in rs)
    # apply fixes run by run; patterns never straddle formatting here
    out = []
    for t, b, i in rs:
        for pat, rep in FIX:
            t = re.sub(pat, rep, t)
        out.append((t, b, i))
    # trim, and move edge spaces outside bold/italic spans
    out[0] = (out[0][0].lstrip(), *out[0][1:])
    out[-1] = (out[-1][0].rstrip(), *out[-1][1:])
    return [r for r in out if r[0]]


# ---------------------------------------------------------------- document
d = docx.Document()
sec = d.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.top_margin, sec.bottom_margin = Inches(0.8), Inches(0.75)
sec.left_margin, sec.right_margin = Inches(0.875), Inches(0.625)   # inside / outside
sec.header_distance, sec.footer_distance = Inches(0.4), Inches(0.4)
sec.gutter = Inches(0)
settings = d.settings.element
d.settings.odd_and_even_pages_header_footer = True
zoom = settings.find(qn('w:zoom'))
zoom.addnext(OxmlElement('w:mirrorMargins'))
pg = OxmlElement('w:pgNumType')
pg.set(qn('w:start'), str(FIRST_PAGE))
sec._sectPr.find(qn('w:cols')).addprevious(pg)

TEXT_W = 8.5 - 0.875 - 0.625  # 7.0 in

st = d.styles


def para_style(name, base='Normal', size=11.5, bold=False, italic=False,
               before=0, after=0, line=15, align=None, left=0, hanging=0,
               first=0, keep_next=False, keep_together=False):
    s = st[name] if name in [x.name for x in st] else st.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    if name != base and name != 'Normal':
        s.base_style = st[base]
    f = s.font
    f.name, f.size, f.bold, f.italic = FONT, Pt(size), bold, italic
    f.color.rgb = RGBColor(0, 0, 0)
    rpr = s.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), FONT)
    pf = s.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = Pt(line) if line else 1.0
    pf.left_indent = Inches(left)
    pf.first_line_indent = Inches(-hanging if hanging else first)
    pf.keep_with_next, pf.keep_together = keep_next, keep_together
    pf.widow_control = True
    if align is not None:
        pf.alignment = align
    return s


C, J = WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.JUSTIFY
para_style('Normal', size=11.5, line=15)
para_style('Recipe Title', size=24, bold=True, line=29, align=C, keep_next=True)
para_style('Recipe Subtitle', size=17, bold=True, line=22, align=C, after=14, keep_next=True)
para_style('Intro', size=11.5, line=15.5, first=0.25, align=J)
para_style('Intro First', base='Intro', size=11.5, line=15.5, first=0, align=J)
para_style('Section Head', size=14, bold=True, italic=True, line=17, before=16, after=6,
           keep_next=True)
para_style('Sub Head', size=12, bold=True, line=15, before=8, after=3, keep_next=True)
para_style('Ingredient', size=11.5, line=14.5, after=3, left=0.3, hanging=0.2,
           keep_together=True)
para_style('Step', size=11.5, line=15.5, after=7, align=J)
para_style('Alert', size=11, line=14.5, align=J, before=12, after=4, keep_together=True)
para_style('Caption', size=10.5, italic=True, line=13.5)
para_style('Image', size=11.5, line=0, align=C, after=12, keep_next=True)
para_style('Proverbs Head', size=16, bold=True, italic=True, line=20, align=C,
           before=30, after=8, keep_next=True)
para_style('Proverb', size=12, italic=True, line=16, align=C, after=7, keep_next=True)
para_style('Folio', size=10, line=12)


def add(style, rs=None, text=None):
    p = d.add_paragraph(style=style)
    if text is not None:
        rs = [(text, None, None)]
    for t, b, i in (rs or []):
        r = p.add_run(t)
        if b is not None: r.bold = b
        if i is not None: r.italic = i
    return p


def page_break():
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def image(name, width_in):
    p = add('Image')
    p.add_run().add_picture(f'{IMG}/{name}_bw.jpg', width=Inches(width_in))
    return p


def border(p, sides=('top', 'left', 'bottom', 'right'), sz=6, space=6, shade=None):
    ppr = p._p.get_or_add_pPr()
    bdr = OxmlElement('w:pBdr')
    for s in sides:
        e = OxmlElement(f'w:{s}')
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), str(sz))
        e.set(qn('w:space'), str(space)); e.set(qn('w:color'), '000000')
        bdr.append(e)
    ppr.append(bdr)
    if shade:
        sh = OxmlElement('w:shd')
        sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), shade)
        ppr.append(sh)


def ingredients(items):
    for rs in items:
        rs = clean(rs)
        add('Ingredient', [('\u25e6\t', False, False)] + rs)


def title(line1, line2, line3=None, new_page=True):
    t = add('Recipe Title', text=line1)
    t.paragraph_format.page_break_before = new_page
    p = add('Recipe Subtitle', text=line2)
    if line3:
        p.paragraph_format.space_after = Pt(0)
        add('Recipe Subtitle', text=line3)


def steps(items):
    for rs in items:
        add('Step', clean(rs))


def intro(items):
    for n, rs in enumerate(items):
        add('Intro First' if n == 0 else 'Intro', clean(rs))


# ------------------------------------------------- headers: outer-corner folio
def folio(hdr, align):
    hdr.is_linked_to_previous = False
    p = hdr.paragraphs[0]
    p.style = st['Folio']
    p.alignment = align
    r = p.add_run()
    for kind, val in (('begin', None), (None, ' PAGE '), ('end', None)):
        if kind:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), kind)
        else:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = val
        r._r.append(e)


folio(sec.header, WD_ALIGN_PARAGRAPH.RIGHT)            # odd pages: right
folio(sec.even_page_header, WD_ALIGN_PARAGRAPH.LEFT)   # even pages: left

# start with a clean body (python-docx template has one empty paragraph)
for p in list(d.paragraphs):
    p._p.getparent().remove(p._p)

# ============================================================ 1. Holubtsi Zupa
title('Holubtsi Zupa', 'Cabbage Roll Soup (GF)', new_page=False)
image('image1', TEXT_W)
intro([runs(26), join(27, 30), runs(31), runs(32)])

add('Section Head', text='Ingredients:')
ingredients([runs(36), runs(37), join(38, 39), runs(40), runs(41), join(42, 43)]
            + [runs(k) for k in range(44, 50)])

add('Section Head', text='Your Option:')
ingredients([runs(k) for k in (53, 54, 55, 56, 57, 58, 59, 62, 63)])

alert = add('Alert', clean(runs(65)))
border(alert, sz=6, space=8, shade='EDEDED')
alert.paragraph_format.left_indent = Inches(0.15)
alert.paragraph_format.right_indent = Inches(0.15)

add('Section Head', text='Recipe:')
steps([runs(70), runs(71), runs(72), join(73, 74, bold_tail=True),
       runs(75), runs(76), runs(77)])

add('Proverbs Head', text=P[80].text.strip())
for k in (82, 83, 84):
    add('Proverb', clean(runs(k)))

# ============================================================ 2. Paska
title('Bez Hluteny Paska', 'Gluten Free Paska')
image('image2', 3.25)
intro([runs(91)])

add('Section Head', text='Ingredients:')
# para 97 is an editor's note in red ("If illustration obscures text in B&W,
# modify illustration.") - not book content, so it is left out.
ingredients([runs(k) for k in range(99, 105)] + [join(105, 106), runs(107), runs(108)]
            + [runs(k) for k in range(110, 120)])

add('Section Head', text='Your Option:')
add('Intro First', clean(runs(124)))

add('Section Head', text='Paska Recipe:')
steps([runs(k) for k in range(128, 139)])

# saffron illustration with its caption beside it
tbl = d.add_table(rows=1, cols=2)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.autofit = False
wl, wr = 2.2, 3.4
for col, cell, w in zip(tbl.columns, tbl.rows[0].cells, (wl, wr)):
    col.width = cell.width = Inches(w)
    tcpr = cell._tc.get_or_add_tcPr()
    va = OxmlElement('w:vAlign'); va.set(qn('w:val'), 'center'); tcpr.append(va)
left, right = tbl.rows[0].cells
lp = left.paragraphs[0]; lp.style = st['Image']
lp.paragraph_format.space_after = Pt(0)
lp.add_run().add_picture(f'{IMG}/image3_bw.jpg', width=Inches(1.85))
rp = right.paragraphs[0]; rp.style = st['Caption']
for t, b, i in clean(runs(146)):
    rp.add_run(t).italic = True
trpr = tbl.rows[0]._tr.get_or_add_trPr()
cs = OxmlElement('w:cantSplit'); trpr.append(cs)

# ============================================================ 3. Varenyky
title('Bez Hluteny Varenyky', 'Gluten Free Varenyky', '(Perohy-Perogies)')
d.paragraphs[-1].paragraph_format.space_after = Pt(14)
image('image4', TEXT_W)
intro([runs(187), runs(188)])

add('Section Head', text='Ingredients:')
add('Sub Head', text='Dough')
ingredients([runs(k) for k in range(194, 203)] + [join(203, 204), runs(205)])
add('Sub Head', text='Potato Cheddar Filling')
ingredients([runs(k) for k in range(211, 219)])

add('Section Head', text='Filling Recipe. Make this first:')
steps([runs(222)])

add('Section Head', text='Recipe:')
steps([runs(k) for k in (226, 227, 228, 229, 230, 231, 234)])

# explicit zero wrap distance on every inline picture (LibreOffice otherwise
# offsets full-width photos toward the outer margin)
for inl in d.element.body.iter(qn('wp:inline')):
    for a in ('distT', 'distB', 'distL', 'distR'):
        inl.set(a, '0')

d.core_properties.title = 'Baba Returns \u2014 interior sample'
d.core_properties.author = 'Raisa Stone'
d.save(OUT)
print('saved', OUT)
