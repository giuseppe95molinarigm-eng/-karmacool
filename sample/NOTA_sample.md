# Nota interna sul sample di *Baba Returns* (Raisa Stone), versione 2

La prima versione è stata respinta per quattro motivi: spaziature affollate e incoerenti, rientri trascurati, foto rimpicciolite e giustificazione scadente. Questa versione è rifatta da zero con un sistema di composizione tipografica vero, **Typst**, al posto di Word/LibreOffice. Ogni critica ha una risposta precisa.

| Critica | Cosa è cambiato |
|---|---|
| Spaziatura affollata e incoerente | Tutte le distanze verticali sono multipli di un'unica unità (7,5 pt, mezza riga). Sono uguali tra titolo e testo, tra le sezioni, tra le voci d'elenco e tra i passaggi, in ogni pagina. Interlinea più ariosa (circa 15,7 pt su corpo 11,25). |
| Rientri | C'è un solo filo sinistro per tutto: titoli, elenchi, procedimenti, box. I rientri di prima riga compaiono solo nei paragrafi narrativi consecutivi, secondo la regola editoriale, mai dopo un titolo. I pallini degli elenchi hanno sempre la stessa sporgenza. |
| Foto rimpicciolite | Le foto di apertura sono **al vivo**, a tutta larghezza fino al bordo del foglio, come nel manoscritto. La zuppa e i varenyky sono a piena pagina in larghezza, la Paska è ancora più grande (6,1"). L'illustrazione dello zafferano ha la misura originale (2,85"). |
| Giustificazione | La giustificazione ora è calcolata sull'intero paragrafo (algoritmo Knuth-Plass, lo stesso di TeX), con sillabazione inglese. Le spaziature tra le parole sono uniformi e non ci sono "fiumi" bianchi. Gli elenchi sono allineati a sinistra senza sillabazione. |

Il controllo automatico conferma che il testo è identico parola per parola al manoscritto (unica modifica: "X" → "×"). Ho controllato a vista tutte le 9 pagine: nessuna riga vedova o orfana, nessun titolo isolato a fondo pagina, nessun testo tagliato o sovrapposto.

## File

| File | Uso |
|---|---|
| `Baba_Returns_sample_8.5x11_BN.pdf` | **Da mostrare alla cliente**: formato rifilato 8,5 × 11", come apparirà il libro |
| `Baba_Returns_sample_KDP_stampa_bleed.pdf` | Lo stesso, nel formato di stampa KDP con bleed (8,625 × 11,25"): dimostra che il file è pronto per la produzione |
| `sorgente/` | Versione modificabile. È un testo semplice: `style.typ` contiene tutto lo stile (margini, caratteri, spaziature), `baba_sample.typ` il contenuto. `gen.py` rigenera il contenuto dal .docx; `img/` contiene le immagini in B/N |
| `font/` | TeX Gyre Pagella (licenza GUST, uso commerciale libero) |

Per rigenerare i PDF: `pip install typst`, poi dalla cartella `sorgente/` compilare `baba_sample.typ` aggiungendo `font/` come percorso dei caratteri. Per il PDF con bleed si aggiunge l'input `bleed=1`; il comando completo è in testa a `style.typ`.

Una versione Word non riprodurrebbe questa qualità: Word non ha la giustificazione per paragrafo, il bleed e i margini a specchio con questa precisione. Se Raisa vuole intervenire lei stessa sui testi, conviene farlo sul manoscritto e rigenerare.

## Scelte di design (sobrie, nello stile della cliente)

- **Carattere:** TeX Gyre Pagella, famiglia Palatino come il Book Antiqua usato da Raisa. Un solo carattere in tutto il libro.
- **Apertura ricetta:**
  - foto al vivo in alto;
  - nome ucraino in grassetto 27 pt, nome inglese in corsivo;
  - un filetto corto centrato;
  - introduzione.

  I titoli sono centrati come nel manoscritto.
- **Intestazioni *Ingredients: / Your Option: / Recipe:***: in grassetto corsivo con i due punti, come le scrive la cliente. Un filetto sottile le prolunga fino al margine.
- **Ingredienti** su due colonne bilanciate: le liste sono lunghe, e così ogni lista è leggibile in un colpo d'occhio e lo spazio è usato meglio. *Dough* e *Potato Cheddar Filling* sono in maiuscoletto.
- **Procedimento:** paragrafi giustificati, separati da mezza riga, con i grassetti della cliente come guida.
- ***Baba Alert*:** riquadro grigio chiaro con barra nera a sinistra.
- **Ukrainian Proverbs:** centrati in corsivo, tra due fregi, ancorati al piede della pagina.
- **Piede di pagina:** numero nell'angolo esterno, accompagnato dal titolo del libro sulle pagine pari e dal nome della ricetta sulle dispari, in maiuscoletto spaziato. Le pagine d'apertura con foto non hanno piede, secondo la convenzione editoriale.

## Pagina e margini

- **Formato:** 8,5 × 11"; il PDF di stampa misura 8,625 × 11,25" con bleed di 0,125" su testa, piede e lato esterno.
- **Margini:** interno 1", esterno 0,8", superiore 0,85", inferiore 0,85".
- **Minimi KDP:** il margine interno di 1" supera il minimo KDP per qualsiasi numero di pagine (0,875" oltre 700 pagine). L'esterno supera ampiamente il minimo di 0,375" previsto con bleed.
- **Da verificare** sul conteggio finale e sulle specifiche KDP del momento. Per recuperare pagine, l'interno può scendere (per esempio a 0,75" sotto le 500 pagine).
- **Bleed su tutto il libro:** in KDP il bleed vale per l'intero volume, quindi il libro completo va impaginato tutto in questo formato.
- **Foto e piega:** le foto al vivo attraversano anche il margine interno. Una piccola parte, vicino alla piega, sarà meno visibile nel volume rilegato. Nella zuppa e nei varenyky quella zona è solo sfondo. Nella Paska, che apre su una pagina pari, il bordo verso la piega mostra una pagnotta già tagliata dall'inquadratura originale.

## Immagini: risoluzione effettiva alla misura di stampa

| Immagine | Pixel | Misura stampata | Risoluzione | Valutazione |
|---|---|---|---|---|
| Holubtsi Zupa | 1883 × 1236 | 8,625" al vivo | 218 ppi | Buona per un interno B/N; 300 ppi sarebbe l'ideale |
| Varenyky | 1870 × 1247 | 8,625" al vivo | 216 ppi | Come sopra |
| Paska | 625 × 658 | 8,625" al vivo | **72 ppi** | ⚠️ **In stampa risulterà morbida e sgranata.** L'ho tenuta grande perché così la vuole la cliente, ma **serve il file originale**: almeno 2600 px di larghezza per questa misura. Non l'ho ingrandita artificialmente, perché non aggiungerebbe dettaglio. |
| Zafferano | 416 × 277 | 2,85" (misura originale) | **146 ppi** | ⚠️ Accettabile per un acquerello morbido, ma meglio un file più grande |

Tutte le immagini sono convertite in scala di grigi:

- livelli automatici;
- correzione dei mezzitoni (la zuppa era molto scura);
- nero massimo intorno al 96%, per l'allargamento del punto sulla carta KDP;
- leggera maschera di contrasto.

## Punti da verificare con la cliente (testo non modificato)

- "Jury is **outraged**" (forse "Jury is *out*").
- "Soniashnyk (**safflower** oil)" nella Paska, ma "**sunflower** oil" nell'Holubtsi.
- "…while you cook, **Short** and squat": maiuscola dopo la virgola, residuo di una riga spezzata.
- "Noone".
- *In Baba's Kitchen: Ukrainian Soul Food* è il titolo del primo libro e andrebbe in corsivo.
- "Your Option" al singolare.
- La nota in rosso "If illustration obscures text in B&W, modify illustration" era un'istruzione per l'impaginatore. Non compare nel layout e il problema non si pone: l'illustrazione non copre il testo.

## Kindle e PDF per il sito

- **Kindle:** l'impaginazione a pagina fissa non si trasferisce. Dal contenuto già ripulito (`gen.py` produce testo strutturato) si genera un EPUB reflowable con gli stessi stili e le foto a colori.
- **Link affiliati:** il manoscritto contiene link Amazon Associates (`amzn.to`). Il regolamento Associates in generale non li consente negli e-book: va verificato.
- **PDF per il sito:** stessa impaginazione, senza bleed, con le foto **a colori** e i link attivi, compresi i numerosi rimandi "in my first book".
