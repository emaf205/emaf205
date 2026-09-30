# La chat è molto 2024: in aula ho trasformato due idee in due tool per architetti

*Un render che diventa video. Una planimetria che genera viste degli ambienti. La parte interessante, però, non è la demo: è capire quando una procedura smette di essere un prompt e diventa uno strumento.*

**Autore:** Emanuele BDC  
**Video originale:** [Google Flow per architetti — guarda la dimostrazione](https://youtu.be/LobK1usyn-g)

---

Stavo tenendo la seconda lezione di un corso sull’intelligenza artificiale a una ventina abbondante di architetti quando mi è venuta voglia di spostare il discorso.

Fino a quel momento stavamo lavorando come lavorano ormai in tanti: apri ChatGPT o Gemini, carichi un file, scrivi un prompt, correggi, riprovi.

Funziona.

A volte funziona anche molto bene.

Ma se quella stessa procedura la fai una volta, poi una seconda, poi una quinta, prima o poi arriva una domanda abbastanza semplice:

> **Se continuate a chiedere alla chat di fare sempre la stessa cosa, perché continuate a ricostruire la procedura ogni volta?**

È lì che ho detto una cosa che probabilmente riassume tutta la lezione:

> **Usare la chat così è molto 2024.**

Non perché la chat sia vecchia o inutile. Al contrario: resta uno dei posti migliori in cui ragionare, esplorare, correggere, provare.

Il problema nasce quando una conversazione smette di essere esplorazione e diventa **procedura**.

Se nel vostro studio esiste una sequenza che ripetete continuamente — carica questo, analizza quello, estrai queste informazioni, genera quell’output, usa sempre questo formato — forse non avete più bisogno di ricordarvi il prompt giusto.

Forse avete bisogno di **impacchettare quella procedura dentro uno strumento**.

Ed è esattamente quello che abbiamo provato a fare con Google Flow.

---

## Non volevo insegnare a programmare in venti minuti

Mettiamola subito in chiaro.

Non mi aspettavo che, dopo venti minuti, una classe di architetti diventasse improvvisamente una squadra di software engineer.

Sarebbe ridicolo.

Quello che volevo mostrare era molto più concreto: oggi la distanza tra **“ho un’idea”** e **“ho un primo prototipo che posso provare”** si è accorciata parecchio.

Google Flow permette di creare Tools personalizzati descrivendoli in linguaggio naturale. Secondo la [documentazione ufficiale](https://support.google.com/flow/answer/17104535?hl=it), Flow scrive il codice e costruisce l’interfaccia dello strumento; poi puoi continuare a modificarlo conversando con l’agente.

Per me la parte interessante non è “wow, l’AI scrive codice”.

È un’altra:

> **Posso prendere una procedura del mio lavoro e trasformarla in qualcosa che non devo reinventare ogni volta.**

Durante la lezione ne abbiamo costruiti due.

Il primo era quasi una sciocchezza.

Il secondo ha iniziato a diventare davvero interessante.

---

## Primo esperimento: Studio Panoramico

La prima mini-app l’ho chiamata **Studio Panoramico**.

L’idea era volutamente semplice:

> *Sono un architetto. Voglio poter caricare un’immagine e ottenere un breve video panoramico della scena.*

Fine.

Una ventina di parole, più o meno.

Niente master prompt da sei pagine. Niente formula magica. Niente “agisci come il miglior regista architettonico del pianeta”.

Una richiesta chiara.

Il tool doveva fare **una cosa sola**: prendere un render o una fotografia e trasformarlo in una breve animazione panoramica.

> **IMMAGINE 01 — INSERIRE QUI**  
> File: `images/01-studio-panoramico-intro.png`  
> Didascalia: *Studio Panoramico, il primo prototipo creato durante la dimostrazione.*

L’interfaccia che Flow ha costruito era elementare: scegli un’immagine, caricala, genera.

E va benissimo così.

> **IMMAGINE 02 — INSERIRE QUI**  
> File: `images/02-studio-panoramico-scegli-immagine.png`  
> Didascalia: *Il tool chiede un solo input: l’immagine da animare.*

Ho preso una scena architettonica notturna e invernale che avevo già generato e l’ho caricata.

> **IMMAGINE 03 — INSERIRE QUI**  
> File: `images/03-studio-panoramico-render-pronto.png`  
> Didascalia: *Il render caricato in Studio Panoramico prima della generazione.*

Poi ho premuto **Crea panorama**.

Dopo qualche minuto avevo un video animato della scena, con movimento e audio.

> **IMMAGINE 04 — INSERIRE QUI**  
> File: `images/04-studio-panoramico-video-generato.png`  
> Didascalia: *Il video prodotto dal tool durante la lezione.*

È la migliore applicazione mai costruita?

**No.**

È un’idea sofisticata?

**No.**

Per i social, una presentazione o una prova veloce può avere senso?

**Sì.**

Ed è proprio qui il punto.

Un tool non deve per forza fare cento cose. Non deve diventare Photoshop, AutoCAD, un gestionale e una piattaforma collaborativa nello stesso pomeriggio.

Può fare **una sola azione**.

Se quella singola azione vi evita di ripetere ogni volta lo stesso lavoro, ha già un motivo per esistere.

---

## Le 18 parole non sono il punto

La parte più facile da vendere sarebbe questa:

> *Ho scritto diciotto parole e l’AI mi ha costruito un’app.*

Fa scena.

Ma rischia anche di far capire la cosa sbagliata.

Il punto non è che diciotto parole bastino per costruire un software professionale.

Il punto è che **diciotto parole possono bastare per iniziare**.

Con pochissimo attrito arrivi a un primo oggetto funzionante. Lo guardi. Lo provi. E finalmente hai qualcosa di concreto da criticare.

Da lì comincia il lavoro vero.

Ed è esattamente quello che è successo con il secondo esperimento.

---

## Visione Planimetrica: qui abbiamo alzato l’asticella

La seconda idea era molto più vicina al lavoro quotidiano di uno studio di architettura.

Volevo caricare una planimetria e ottenere, per ogni ambiente riconosciuto, una o più immagini fotografiche del locale completamente vuoto.

In sostanza:

- carico la planimetria;
- il sistema riconosce gli ambienti;
- li elenca;
- decide quante viste possono servire;
- genera immagini fotografiche degli spazi senza arredi.

La metafora che ho usato durante la lezione era volutamente esagerata:

> **Gli do una planimetria e lui entra nella stanza a fare una fotografia.**

Naturalmente non entra da nessuna parte.

L’AI interpreta una rappresentazione bidimensionale e genera una possibile visualizzazione. Non è un rilievo. Non è una ricostruzione geometrica certificata. Non sostituisce un progetto tecnico.

Ma come strumento esplorativo, per immaginare rapidamente un ambiente vuoto prima di lavorarci, la cosa comincia a essere interessante.

> **IMMAGINE 05 — INSERIRE QUI**  
> File: `images/05-visione-planimetrica-editor.png`  
> Didascalia: *Visione Planimetrica aperto in modalità Modifica.*

---

## Prima di costruire, gli ho chiesto il piano

Con questo secondo tool non volevo fare il classico one-shot.

Prima di far partire tutto ho chiesto a Flow:

> **Prima di procedere, dimmi qual è il tuo piano.**

Questa piccola cosa ha fatto emergere subito un problema.

Flow mi ha proposto un workflow che, a prima vista, sembrava sensato: carica il PDF, clicca sulle stanze, nominale, indica le aree, genera le viste.

E lì l’ho fermato.

> **E no, caro. Le stanze non voglio identificarle io. Voglio che sia tu a identificarle.**

Se devo cliccare manualmente su ogni stanza, delimitarla e darle un nome, sto automatizzando la parte sbagliata.

La parte ripetitiva deve farla il sistema.

Io voglio rimanere nel punto in cui serve un giudizio: **hai riconosciuto correttamente gli ambienti oppure no?**

Quindi abbiamo cambiato il piano. Analisi automatica della planimetria, riconoscimento degli ambienti, scelta del numero di viste.

> **IMMAGINE 06 — INSERIRE QUI**  
> File: `images/06-visione-planimetrica-piano.png`  
> Didascalia: *Prima dell’implementazione ho chiesto a Flow di esplicitare il piano, così da poter correggere il workflow.*

Questa per me è una delle parti più importanti di tutto l’esperimento.

> **L’intelligenza artificiale non elimina la progettazione. Ti propone decisioni. Tu devi capire se sono buone.**

---

## Poi abbiamo iniziato a rompere il prototipo

A quel punto avevamo qualcosa.

E abbiamo fatto la cosa più utile possibile: **abbiamo cercato di farlo funzionare nel mondo reale**.

Mi sono accorto che la planimetria che avevo a disposizione in quel momento era in PNG.

Quindi: *fammi caricare anche PNG*.

Fatto.

Poi per caricare il file dovevo cliccare, aprire il Finder, cercarlo.

No.

*Voglio poter trascinare il file.*

Nuova modifica.

Poi le prime immagini generate erano arredate.

Io le volevo completamente vuote.

*Le stanze devono essere vuote. Niente arredamento.*

Nuova modifica.

Poi l’interfaccia non mi piaceva.

La volevo più secca, **brutalist, editoriale**.

Nuova modifica.

Poi ci siamo accorti che il supporto ai PDF non era come mi serviva.

*Mi serve caricare anche PDF.*

Nuova modifica.

> **IMMAGINE 07 — INSERIRE QUI**  
> File: `images/07-visione-planimetrica-supporto-pdf.png`  
> Didascalia: *Il supporto PDF viene aggiunto dopo aver individuato il limite durante il test.*

Poi è comparso un bug.

Abbiamo sistemato il bug.

Questa è la parte che spesso scompare dalle demo sull’AI.

Si mostra il prompt iniziale.

Si mostra il risultato finale.

In mezzo sembra esserci una fata madrina.

In realtà in mezzo c’è questo:

> **Test. Verifica. Modifica. Correzione. Debug. Nuovo test.**

Che è molto meno sexy.

Ed è anche molto più utile.

---

## L’app in venti minuti è il prototipo, non il prodotto finito

Dire “ho creato un’app in venti minuti” è tecnicamente affascinante e concettualmente pericoloso.

Perché dipende da cosa intendiamo per *creato*.

In venti minuti posso arrivare a un primo prototipo sorprendentemente funzionante.

Poi devo usarlo.

Ed è quando lo uso che scopro tutte le cose che nel prompt iniziale non avevo pensato di specificare:

il formato del file che utilizzo davvero, un click inutile, un passaggio che dovrebbe essere automatico, una bella immagine che però è sbagliata per il mio scopo, un output che non si scarica come voglio, una funzione che funziona con il mio test ma non con un file reale.

Per questo durante la lezione ho suggerito di provarlo per un po’.

Ho detto anche **quindici giorni**.

Non perché esista una legge dei quindici giorni.

È semplicemente un ordine di grandezza sensato: se lo usate davvero per due settimane, iniziate a scoprire se avete costruito uno strumento o soltanto una bella demo.

Ogni difetto diventa una nuova istruzione:

> *Fammelo così.*
>
> *Questo formato non va bene.*
>
> *Questa operazione deve essere automatica.*
>
> *Qui voglio due viste.*
>
> *Questa stanza deve restare vuota.*
>
> *Questo output deve essere scaricabile.*

A un certo punto non state più migliorando un prompt.

State costruendo **un protocollo**.

---

## Quando la planimetria entra davvero nel tool

Una volta sistemato il flusso, ho caricato una planimetria di prova.

Il sistema l’ha analizzata e ha restituito gli ambienti riconosciuti: soggiorno e cucina, bagno, disimpegno e gli altri locali individuati nella pianta.

Per ciascuno poteva poi stabilire quante viste generare.

> **IMMAGINE 08 — INSERIRE QUI**  
> File: `images/08-visione-planimetrica-ambienti.png`  
> Didascalia: *Il tool mostra gli ambienti riconosciuti e il numero di viste previste prima della generazione.*

Questo passaggio, per me, non va eliminato.

**Automazione non significa rinunciare al controllo.**

Significa spostare il controllo nel punto giusto.

Non voglio disegnare manualmente un rettangolo intorno a ogni stanza.

Voglio che la macchina faccia quel lavoro e che mi lasci la decisione importante: *ha capito bene oppure no?*

Dopo il controllo, il tool genera le viste.

> **IMMAGINE 09 — INSERIRE QUI**  
> File: `images/09-visione-planimetrica-vista-generata.png`  
> Didascalia: *Una delle viste generate da Visione Planimetrica, pronta per il download.*

A quel punto il flusso diventa quasi noioso.

Carico.

Controllo.

Genero.

Scarico.

Ed è un complimento.

---

## La differenza tra una chat e un protocollo

A questo punto l’obiezione è inevitabile:

> **Ma questa cosa non posso farla anche con ChatGPT o Gemini?**

Certo che puoi.

Il punto non è se una chat sia capace di analizzare una planimetria, leggere un PDF o generare immagini.

Il punto è che, la volta successiva, rischi di dover ricostruire almeno una parte della procedura.

Nel tool, invece, la logica è stata impacchettata.

Quando arriva una planimetria, il sistema sa già che deve analizzarla, riconoscere gli ambienti, proporre le viste, aspettare il controllo e generare gli output secondo le regole che abbiamo definito.

La volta dopo non ricomincio da zero.

E soprattutto non devo essere necessariamente io a usarlo.

Posso passarlo a un collega.

Questo, per me, è il salto:

> **Non chiedere all’AI di fare una cosa. Costruire il modo in cui quella cosa deve essere fatta ogni volta.**

---

## Il tool migliore, alla fine, dovrebbe essere quasi noioso

C’è un momento in cui uno strumento interno smette di essere affascinante.

Ed è un ottimo segno.

Non voglio che ogni volta mi sorprenda.

Non voglio pensare: *vediamo cosa decide oggi*.

Se una procedura è stata standardizzata bene, deve diventare prevedibile.

La sorpresa è bellissima durante una demo.

In ufficio, molto spesso, preferisco che una cosa faccia esattamente quello che deve fare.

Questo è anche il motivo per cui trovo interessanti i **piccoli tool monofunzione**.

Quando diciamo “applicazione” immaginiamo subito login, database, utenti, dashboard, pagamenti, quaranta funzioni e una startup da finanziare.

Ma per uno studio potrebbe essere molto più utile avere una serie di piccoli utensili: uno trasforma un render in una breve animazione, uno analizza planimetrie, uno prepara una moodboard secondo certe regole, uno estrae sempre le stesse informazioni da un documento, uno normalizza immagini in un formato preciso.

Non serve sempre il coltellino svizzero definitivo dell’architetto.

A volte serve un cacciavite.

---

## I crediti esistono. La magia ha un contatore

C’è naturalmente una parte meno romantica: **le generazioni costano crediti**.

Google specifica che i contenuti multimediali generati attraverso i Flow Tools consumano crediti e che il consumo dipende dal modello utilizzato. Il sistema mostra un avviso quando l’esecuzione di uno strumento può consumarli. La situazione dei piani cambia nel tempo, quindi prima di costruire workflow pesanti conviene controllare la [pagina ufficiale dei crediti](https://support.google.com/flow/answer/16526234?hl=it) e quella dei [piani di Flow](https://labs.google/fx/tools/flow).

Questo introduce una domanda molto sana:

> **Vale la pena automatizzare questa procedura?**

Se uno strumento mi fa risparmiare anche solo un’ora ogni settimana, il conto può avere perfettamente senso.

Se genera cinquanta varianti inutili perché ho progettato male il flusso, ho semplicemente automatizzato lo spreco.

---

## Anche la condivisione va capita

Uno dei vantaggi di questi tool è poterli condividere.

Ma *condividere* non significa automaticamente *privato, sicuro e aziendale*.

La documentazione Google specifica che chiunque abbia il link può accedere al **codice, al nome e alla miniatura** dello strumento. Inoltre il link fotografa la versione esistente quando viene generato: le modifiche successive non aggiornano automaticamente quella copia condivisa.

> **IMMAGINE 10 — INSERIRE QUI**  
> File: `images/10-flow-condivisione-tool.png`  
> Didascalia: *La schermata di condivisione del tool: prima di distribuire un link, conviene capire che cosa rende accessibile.*

Se dentro lo strumento avete logiche che considerate riservate, questa non è una nota a piè di pagina.

È parte del progetto.

---

## Siamo praticamente nel 2027. Questa, per me, è l’ABC

La cosa che ha stupito di più gli architetti non era soltanto la qualità del video o l’immagine generata dalla planimetria.

Era la distanza tra l’idea e il primo oggetto funzionante.

Quella distanza si è accorciata in maniera abbastanza assurda.

Posso avere un’idea, descriverla, farmi proporre un piano, contestarlo, costruire un prototipo, provarlo, trovare un bug, correggerlo, cambiare l’interfaccia, aggiungere un formato e poi condividerlo.

Non significa che lo sviluppo software sia diventato inutile.

Non significa che un architetto sia improvvisamente diventato uno sviluppatore.

E non significa che un software robusto, sicuro e complesso nasca magicamente da una frase.

Significa una cosa diversa:

> **Una quantità enorme di piccoli strumenti che fino a ieri non avremmo mai costruito, perché non sarebbe economicamente valso la pena svilupparli, oggi può essere prototipata.**

Ed è questo che mi interessa.

Non l’ennesima frase “l’AI rivoluzionerà tutto”.

Quella ormai la possiamo anche lasciare riposare.

Mi interessa il piccolo tool che venerdì non esisteva e lunedì mattina elimina una procedura stupida che il vostro studio ripete da anni.

---

## Se non sai quale tool costruire, chiedilo all’AI

Alla fine della lezione ho lasciato il consiglio più semplice.

Se non sapete che cosa costruire, **non sforzatevi per forza di avere l’idea geniale**.

Spiegate all’AI che cosa fate davvero.

Con quali file lavorate. Quali software utilizzate. Che cosa ripetete. Dove perdete tempo. Quale operazione vi irrita. Quale sequenza fate sempre nello stesso ordine.

Poi chiedetele qualcosa del genere:

> **Sono un architetto. Lavoro con planimetrie, PDF, render e immagini e uso strumenti come Archicad e piattaforme AI. Individua le procedure ripetitive o visive del mio lavoro che potrebbero diventare piccoli tool. Per ciascuna indicami input, output e vantaggio concreto. Evita idee generiche: proponi strumenti che potrei realmente testare nello studio.**

Questa è una cosa che continuo a vedere troppo poco nelle aziende.

Si chiede all’AI di scrivere una mail.

Di riassumere.

Di cercare.

Di sistemare una presentazione.

Molto meno spesso le si chiede:

> **Guardando il mio lavoro, dove vedi una procedura che non dovrei più fare a mano?**

Ed è una domanda molto più interessante.

---

## Il punto non sono questi due tool

Domani Studio Panoramico e Visione Planimetrica potrebbero essere rifatti meglio.

Potrei scoprire che una parte del workflow non regge con planimetrie più complesse.

Potrei cambiarli, buttarli via o sostituirli con altro.

Non è quello il punto.

Il punto è il cambio di mentalità.

> **Idea → prototipo → test → verifica → modifica → correzione → debug → implementazione → condivisione.**

La chat resta il luogo in cui posso ragionare.

Il tool diventa il luogo in cui una procedura smette di dover essere reinventata.

Se la stessa richiesta torna ancora e ancora nel vostro studio, cominciate da lì.

Perché forse non vi serve un prompt migliore.

**Forse vi serve uno strumento.**

---

## Fonti e approfondimenti

- [Video originale della lezione e della dimostrazione](https://youtu.be/LobK1usyn-g)
- [Google Flow — pagina ufficiale](https://labs.google/fx/tools/flow)
- [Google Flow Help — Crea e gestisci strumenti](https://support.google.com/flow/answer/17104535?hl=it)
- [Google Flow Help — Gestisci i crediti](https://support.google.com/flow/answer/16526234?hl=it)

*Le informazioni su Tools, condivisione e crediti sono state verificate sulla documentazione ufficiale Google il 30 settembre 2026. Funzioni, limiti e piani possono cambiare.*
