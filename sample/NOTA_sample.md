# Nota interna sul sample di *Baba Returns* (Raisa Stone)

## File consegnati

| File | Contenuto |
|---|---|
| `Baba_Returns_sample_8.5x11_BN.pdf` | Il sample da mostrare alla cliente: 9 pagine, 8,5 × 11", B/N, font incorporati |
| `Baba_Returns_sample_8.5x11_BN.docx` | Versione modificabile, costruita interamente con stili di paragrafo con nome |
| `immagini_bn/` | Le 4 immagini convertite in scala di grigi, alla risoluzione originale (nessun ricampionamento) |
| `font/` | TeX Gyre Pagella con licenza GUST (libera, anche per uso commerciale) |
| `tools/` | Script che rigenerano docx e PDF dal manoscritto |

## Pagine scelte

Ho impaginato tutto l'estratto ricevuto (pp. 31–40 del manoscritto). Con l'impaginazione pulita occupa 9 pagine, numerate 31–39 come nell'originale:

| Pagine | Contenuto |
|---|---|
| 31–33 | **Holubtsi Zupa / Cabbage Roll Soup (GF)**: titolo, foto, introduzione, ingredienti, *Your Option*, box *Baba Alert*, procedimento, seguiti dai **Ukrainian Proverbs** |
| 34–36 | **Bez Hluteny Paska / Gluten Free Paska**: con l'illustrazione dello zafferano e la sua didascalia |
| 37–39 | **Bez Hluteny Varenyky / Gluten Free Varenyky (Perohy-Perogies)**: con i sottogruppi *Dough* e *Potato Cheddar Filling* |

Se volete mostrare solo 3–5 pagine, le pp. **31–33** sono già un estratto autonomo con una ricetta completa, la foto e i proverbi. In alternativa, le pp. **31–35**.

## Impostazione della pagina

- **Formato:** 8,5 × 11", senza bleed.
- **Margini a specchio:** interno 0,875", esterno 0,625", superiore 0,8", inferiore 0,75".
- **Margine interno (gutter):** i minimi KDP dipendono dal numero di pagine:
  - 151–300 pagine: 0,5";
  - 301–500 pagine: 0,625";
  - 501–700 pagine: 0,75".

  Con ~300 pagine il libro è a cavallo di due fasce, quindi ho lasciato un margine abbondante. **Va ricontrollato sul conteggio finale e sulle specifiche KDP in vigore al momento della pubblicazione.** Se serve recuperare pagine, si può scendere a 0,75".
- **Numeri di pagina:** in alto, nell'angolo esterno (a destra sulle dispari, a sinistra sulle pari). Ho mantenuto la posizione in alto scelta dalla cliente. Ho verificato sul PDF che margini e numeri si alternano correttamente.
- **Carattere:** la cliente usa Book Antiqua, che fa parte della famiglia Palatino. Ho usato **TeX Gyre Pagella**, un Palatino libero da incorporare nel PDF di stampa senza problemi di licenza. L'aspetto è quasi identico.
  - Testo a 11,5 pt.
  - Titoli delle ricette a 24/17 pt in grassetto centrato, come nel manoscritto.
  - Intestazioni *Ingredients / Your Option / Recipe* in grassetto corsivo, come nel manoscritto.

## Cosa ho migliorato (solo impaginazione, nessuna modifica a testi o dosi)

Il manoscritto mostra i segni tipici di una conversione da PDF a Word, o di copia e incolla:

1. **Frasi spezzate a metà, ricucite:**
   - "…picking me up from cheese / making factory";
   - "**Add bay leaf,** / tomatoes, rice, salt and pepper." (la seconda metà era diventata un "Titolo 4");
   - "1 ¼ cups goes in dough, / ¼ cup is for egg wash";
   - "…while you cook, / Short and squat, like many Babas.".
2. **Righe di continuazione che erano diventate voci d'elenco separate, riunite alla voce giusta:**
   - "Do not use crushed crap from jar! Must be fresh" (con l'aglio);
   - "and DO NOT use canned crap…" (con il brodo).
3. **Spaziatura:** ho eliminato decine di paragrafi vuoti usati come spaziatori, compresi i titoli vuoti dopo ogni intestazione. La spaziatura ora è definita dagli stili ed è uguale in tutte le ricette.
4. **Rientri:** c'erano 6–7 valori diversi, impostati a mano. Gli elenchi della Paska e delle varianti dell'Holubtsi avevano due livelli senza motivo. Ora tutti gli elenchi usano lo stesso rientro e lo stesso pallino vuoto della cliente.
5. **Gerarchia:**
   - Nei Varenyky "Ingredients:" era testo semplice e "Dough" / "Potato Cheddar Filling" erano titoli più grandi. L'ordine ora è corretto: sezione, poi sottogruppo.
   - I titoli delle ricette sono su due o tre righe regolari (nome ucraino, nome inglese).
6. **Procedimenti:** paragrafi distinti con spazio tra un passaggio e l'altro. I grassetti della cliente sono conservati e fanno da guida alla lettura. Ogni parola era un "run" separato: li ho uniformati, quindi spazi e grassetti non saltano più.
7. ***Baba Alert*:** in un riquadro con filetto e fondo grigio chiaro (8%), adatto alla stampa B/N.
8. **Ukrainian Proverbs:** centrati in corsivo, con il titolo centrato davvero. Nel file era spostato con una fila di spazi.
9. **Microtipografia:**
   - "---" → "—";
   - "9” X 13”pan" → "9” × 13” pan";
   - "1 1/2" → "1 ½" e "3/4" → "¾", come nel resto del testo;
   - trattino breve negli intervalli (10–15, 8”–9”);
   - spazi doppi eliminati;
   - "minutes.Remove" → "minutes. Remove".

   Ho lasciato "1/3", "1/2" e "1/5" nel passaggio della Paska perché il font non ha i glifi ⅓ e ⅕.
10. **Continuità tra le pagine:** titoli sempre agganciati al paragrafo successivo, voci d'elenco mai spezzate, controllo di vedove e orfane, ogni ricetta che inizia su pagina nuova.
11. **Nota redazionale:** ho tolto dal layout la nota in rosso "*If illustration obscures text in B&W, modify illustration.*". È un'istruzione per l'impaginatore, non testo del libro.

Ho controllato in automatico che il testo del sample coincida parola per parola con quello del manoscritto. Ho poi controllato ogni pagina a vista: niente testo tagliato, immagini deformate, sovrapposizioni o pagine vuote accidentali.

## Immagini

Ogni immagine è stata convertita in scala di grigi con:

- livelli automatici;
- correzione dei mezzitoni (la foto della zuppa era molto scura e l'ho schiarita);
- nero massimo intorno al 96%, per contenere l'allargamento del punto sulla carta KDP;
- leggera maschera di contrasto.

Nessuna immagine è stata ingrandita artificialmente.

| Immagine | Pixel | Dimensione di stampa | Risoluzione effettiva | Valutazione |
|---|---|---|---|---|
| Holubtsi Zupa (p. 31) | 1883 × 1236 | 7,0" (larghezza colonna) | **269 ppi** | Buona |
| Paska (p. 34) | 625 × 658 | 3,25" | **192 ppi** | ⚠️ **Insufficiente.** Ho dovuto ridurla. A tutta pagina, come nel manoscritto, scenderebbe a ~74 ppi e stamperebbe sgranata. In basso a sinistra ha anche una sottile striscia chiara che è nel file originale. **Serve l'originale ad alta risoluzione** (almeno 1000–2000 px di lato) |
| Zafferano (p. 36) | 416 × 277 | 1,85" | **225 ppi** | Accettabile a questa misura piccola; non si può ingrandire. In B/N l'acquerello viola diventa grigio chiaro: ho aumentato il contrasto. Meglio avere un file più grande |
| Varenyky (p. 37) | 1870 × 1247 | 7,0" | **267 ppi** | Buona |

KDP consiglia 300 ppi. Le due foto a ~268 ppi sono più che adeguate per un interno B/N. Paska e zafferano vanno sostituite, se possibile, prima del libro completo.

**Foto a tutta pagina:** nel manoscritto le foto arrivano al bordo del foglio. In stampa questo richiede il bleed. In KDP il bleed vale per tutto il libro: pagina 8,625 × 11,25", margine esterno minimo 0,375". Per il sample ho tenuto le foto entro i margini, che è più semplice e non fa rischiare tagli. Se Raisa preferisce le foto al vivo, si può fare sul libro completo.

## Punti da verificare con la cliente (non li ho toccati)

Il tono e la sintassi "alla Baba" sono voluti, quindi non ho corretto nulla. Questi punti però sembrano refusi e vanno confermati dall'autrice:

- "**Jury is outraged** whether is wheat…": forse "Jury is *out*"?
- "**Soniashnyk (safflower oil)**" nella Paska. Nell'Holubtsi lo stesso termine è tradotto "sunflower oil" (*soniashnyk* = girasole).
- "**Short and squat**" con la maiuscola dopo la virgola, conseguenza della riga spezzata.
- "Noone" (no one), "monosadisticglucosaphetamine" (presumo gioco di parole voluto).
- "*In Baba's Kitchen: Ukrainian Soul Food*" è il titolo del primo libro: andrebbe in corsivo come gli altri titoli.
- "Your Option:" al singolare, mentre sotto ci sono più opzioni.
- Nella Paska e nei Varenyky ingredienti e attrezzatura sono nella stessa lista. Si potrebbero separare in "Ingredients" ed "Equipment", ma è una scelta di contenuto da proporre, non da imporre.

## Note per Kindle e PDF per il sito

- **Kindle (reflowable):** il docx ora usa solo stili con nome, senza paragrafi vuoti né rientri manuali, quindi è una buona base per la conversione. Per l'e-book conviene:
  - trasformare gli elenchi in elenchi veri (ora il pallino è un carattere seguito da tabulazione, scelta comoda per la stampa);
  - togliere i numeri di pagina;
  - usare immagini a colori.
- **Link affiliati:** il manoscritto contiene link Amazon Associates (`amzn.to`) su "Bob's Red Mill". Nel cartaceo non servono e li ho resi come testo. Per l'e-book va verificato il regolamento Amazon Associates, che in generale **non consente link affiliati negli e-book**. Nel PDF per il sito si possono mantenere attivi.
- **PDF per il sito:** si può ricavare dallo stesso file con le foto **a colori** e i link attivi. I rimandi "in my first book", molto frequenti, potrebbero diventare link al primo libro.
- **Copertina:** la foto di copertina non era nei file arrivati in questa sessione. Non serve per il sample, ma andrà controllata la sua risoluzione per una copertina 8,5 × 11" con bleed.

## Rigenerare i file

```
python3 tools/bw.py <cartella media del docx> <cartella output>      # crea imageN_bw.jpg
python3 tools/build.py manoscritto.docx <cartella output> sample.docx
soffice --headless --convert-to pdf sample.docx
```

Il carattere in `font/` va installato prima di esportare il PDF. Se su un PC con Word il font non è installato, Word lo sostituisce. In quel caso si installa (è gratuito) oppure si cambia il carattere negli stili, una sola modifica per stile.
