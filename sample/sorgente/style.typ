// Baba Returns — interior style (8.5 × 11 in, black & white)
//
// Compile for screen/client review:   typst compile baba_sample.typ
// Compile for KDP print with bleed:   typst compile --input bleed=1 baba_sample.typ
//
// Every vertical distance is a multiple of `unit` (half the body line pitch),
// so spacing stays identical on every page.

// ------------------------------------------------------------------ geometry
#let bleed = if sys.inputs.at("bleed", default: "0") == "1" { 0.125in } else { 0in }
#let trim-w = 8.5in
#let trim-h = 11in
#let m-inside = 1in
#let m-outside = 0.8in
#let m-top = 0.85in
#let m-bottom = 0.85in

#let body-size = 11.25pt
#let unit = 7.5pt            // half line: the vertical rhythm
#let rule-w = 0.5pt

// ------------------------------------------------------------------ fonts
#let serif = "TeX Gyre Pagella"   // Palatino family, like the author's Book Antiqua

// ------------------------------------------------------------------ helpers
#let is-opener-page() = {
  let pg = here().page()
  query(<opener>).any(m => m.location().page() == pg)
}

#let current-recipe() = {
  let pg = here().page()
  let found = query(<recipe-name>).filter(m => m.location().page() <= pg)
  if found.len() > 0 { found.last().value } else { "" }
}

#let folio-text(body) = text(size: 8.5pt, tracking: 0.12em, smallcaps(body))

// ------------------------------------------------------------------ document
#let book(first-page: 1, book-title: "", doc) = {
  set document(title: book-title + " — Interior Sample", author: "Raisa Stone")
  set page(
    width: trim-w + bleed,
    height: trim-h + 2 * bleed,
    binding: left,
    margin: (
      inside: m-inside,
      outside: m-outside + bleed,
      top: m-top + bleed,
      bottom: m-bottom + bleed,
    ),
    footer-descent: 0.36in,
    footer: context {
      if is-opener-page() { return }
      let n = counter(page).get().first()
      let num = text(size: 9.5pt, number-type: "old-style", str(n))
      let sep = h(0.9em) + box(height: 7pt, line(angle: 90deg, length: 7pt, stroke: 0.4pt)) + h(0.9em)
      if calc.odd(n) {
        align(right, folio-text(current-recipe()) + sep + num)
      } else {
        align(left, num + sep + folio-text(book-title))
      }
    },
  )
  set text(
    font: serif,
    size: body-size,
    lang: "en",
    region: "us",
    hyphenate: true,
    costs: (hyphenation: 45%, runt: 150%, widow: 200%, orphan: 200%),
  )
  set par(
    justify: true,
    leading: 0.7em,
    spacing: unit,
    first-line-indent: 0pt,
    linebreaks: "optimized",
  )
  set strong(delta: 300)
  counter(page).update(first-page)
  doc
}

// ------------------------------------------------------------------ recipe opener
// Full-bleed photograph across the top of the page, then the title block.
#let opener(photo: none, photo-h: 5.5in, title: [], subtitle: [], name: "") = {
  pagebreak(weak: true)
  [#metadata("opener") <opener>]
  [#metadata(name) <recipe-name>]
  context {
    let n = counter(page).get().first()
    let left-m = if calc.odd(n) { m-inside } else { m-outside + bleed }
    place(
      top + left,
      dx: -left-m,
      dy: -(m-top + bleed),
      box(
        width: trim-w + bleed,
        height: photo-h + bleed,
        clip: true,
        image(photo, width: 100%, height: 100%, fit: "cover"),
      ),
    )
  }
  v(photo-h - m-top + 4 * unit)
  align(center, {
    block(spacing: 0pt, text(size: 27pt, weight: "bold", tracking: 0.01em, title))
    v(1.2 * unit)
    block(spacing: 0pt, text(size: 15pt, style: "italic", subtitle))
    v(2 * unit)
    line(length: 0.9in, stroke: rule-w)
  })
  v(2.5 * unit)
}

// ------------------------------------------------------------------ headnote
#let intro(body) = {
  set par(first-line-indent: 1.4em, spacing: 0.7em)
  body
}

// ------------------------------------------------------------------ section head
// Author's style: bold italic with colon; a hairline carries the eye across.
#let section(body) = {
  v(3 * unit, weak: true)
  block(sticky: true, below: 1.5 * unit, {
    box(text(size: 13pt, weight: "bold", style: "italic", body))
    h(0.6em)
    box(width: 1fr, baseline: -0.3em, line(length: 100%, stroke: 0.35pt + luma(110)))
  })
}

#let subsection(body) = block(
  sticky: true,
  above: 2 * unit,
  below: 1 * unit,
  text(size: 10.5pt, weight: "bold", tracking: 0.08em, smallcaps(body)),
)

// ------------------------------------------------------------------ lists
#let bullet = text(size: 0.95em, baseline: -0.05em, "◦")

#let item-list(items) = {
  set par(justify: false, first-line-indent: 0pt, leading: 0.55em)
  set text(hyphenate: false)
  for it in items {
    block(spacing: 1.45 * unit, breakable: false,
      grid(columns: (1.05em, 1fr), bullet, it))
  }
}

// Two balanced columns (split decided by the generator).
#let two-col(left, right) = grid(
  columns: (1fr, 1fr),
  column-gutter: 0.42in,
  item-list(left),
  item-list(right),
)

// ------------------------------------------------------------------ method
#let method(body) = {
  set par(first-line-indent: 0pt, spacing: 1.6 * unit)
  body
}

// ------------------------------------------------------------------ Baba Alert
#let alert(body) = {
  v(3 * unit, weak: true)
  block(
    width: 100%,
    breakable: false,
    fill: luma(243),
    stroke: (left: 2.5pt + black),
    inset: (left: 16pt, right: 16pt, top: 11pt, bottom: 12pt),
    {
      set text(size: 10.5pt)
      set par(spacing: 0.7em)
      body
    },
  )
}

// ------------------------------------------------------------------ ornament
#let ornament = align(center, box({
  box(baseline: -0.32em, line(length: 0.8in, stroke: 0.4pt))
  h(0.5em)
  box(baseline: -0.05em, rotate(45deg, square(size: 4.5pt, fill: black)))
  h(0.5em)
  box(baseline: -0.32em, line(length: 0.8in, stroke: 0.4pt))
}))

#let proverbs(title, items) = {
  v(5 * unit, weak: true)
  v(1fr)
  block(breakable: false, width: 100%, {
    ornament
    v(2 * unit)
    align(center, text(size: 15pt, weight: "bold", style: "italic", title))
    v(1.5 * unit)
    set par(justify: false)
    for it in items {
      align(center, block(width: 80%, spacing: 1.3 * unit, text(style: "italic", size: 11.5pt, it)))
    }
    v(2 * unit)
    ornament
  })
}

// ------------------------------------------------------------------ figure
#let illustration(path, width, caption) = {
  v(4 * unit, weak: true)
  v(1fr)
  block(breakable: false, width: 100%, align(center, {
    image(path, width: width)
    v(1.2 * unit)
    block(width: 4.4in, {
      set par(justify: false)
      set text(hyphenate: false)
      text(size: 10pt, style: "italic", caption)
    })
  }))
  v(1.4fr)
}
