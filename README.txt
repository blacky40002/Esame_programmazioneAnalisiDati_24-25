=========================================================================
ISTRUZIONI per il PROGETTO DI RECUPERO aa 2024/25
========================================================================
Il progetto prevede la realizzazione di un progetto Scratch e di un progetto Python
che realizzano la gestione di un bancomat, come specificato nel file ProgettoRecupero_aa24_25.pdf.

Come procedere:
(1) realizzare il progetto Scratch seguendo le istruzioni ed esportare il hotel.sb3.
(2) realizzare (nei file classi.py stanze.py e hotel.py) i metodi richiesti seguendo le indicazioni
    dei commenti in corrispondenza di ciascun metodo e testarli opportunamente.
(3) eseguire i test nel file main.py fornito dai docenti (senza modificarlo)
    per effettuare questo test i file main.py, testMy.py, e i file .py implementati
    si devono trovare nella stessa cartella.
(4) realizzare (nel file gui.py) la GUI come specificato nel file di istruzioni (oltre a questo README)
    e testarla opportunamente.
(5) assicurarsi che tutti i test vengono superati e venga stampato il messaggio finale 
    che invita alla consegna.
(6) scrivere una breve relazione che contiene la spiegazione della parte Scratch (spirite,logica,interazione);
    le motivazioni delle scelte implementative; e una guida utente che spiega come utilizzare il software.
(7) preparare un archivio zip con i file (hotel.sb3, classi.py stanze.py, hotel.py gui.py e relazione in pdf)
    per la consegna inserendo nome cognome e contatti dei componenti del gruppo nell'intestazione.
(8) consegnare su Moodle l'archivio (ed eventuali file aggiuntivi -- vedi istruzioni sotto)
    entro la data e ora dell'appello di cui si vuole svolgere l'orale.

------------------------------------------------
Cosa contiene questa il compito
------------------------------------------------

ProgettoRecupero_aa24_25.pdf	: file contenente la descrizione del progetto

classi.py 	            	    : file che contiene la definizione per le classi di supporto Data e Prenotazioni

stanze.py 	            	    : file che contiene la definizione della gerarchia di classi per le stanze

hotel.py 	               	    : file che contiene la definizione dei metodi da realizzare per l'hotel

gui.py                          : file in cui inserire il codice della GUI, con gli import necessari per usare l'hotel

main.py, testMy.py              : file per i test finali (NON MODIFICARE)

README.txt		                : questo file


========================================================================
ALCUNI SUGGERIMENTI per la realizzazione dell'assegnamento
========================================================================
Per la parte Python, è suggeribile partire da class.py, poi stanze.py e infine hotel.py.
Dopo aver implementato ciascuna classe in questo ordine è possibile usare main.py per testare
parzialmente il funzionamento delle classi implementate.

Conviene realizzare le funzioni richieste seguendo le specifiche nei commenti e
analizzando la struttura dei test del file main.py che usano un aversione aggiornata 
della testEqual() usata durante il corso e disponibile in testMy.py.
Durante lo sviluppo e' consigliato non usare immediatamente i test in main.py
per non avere risultati complessi e di difficile interpretazione. Consigliamo invece
di ispiraresi a main.py per creare dei test propri che permettano di
verificare il funzionamento delle funzioni passo passo durante la realizzazione
secondo il principio del debug incrementale spesso citato a lezione.

Quando si è ragionevolmente sicuri della correttezza di quanto realizzato, passare a test finali
in main.py.
Questi ultimi test verificano le funzionalità basilari delle funzioni richieste stampando
il risultato a video. Se tutti i test sono superati lo studente viene invitato
a effettuare la consegna altrimenti si stampa il numero di test falliti.

E' possibile aggiungere test, che vanno realizzati in un file di nome "moreTest.py"
da consegnare insieme ai file .py.

Se lo si desidera è possibile definire funzioni ausiliarie per la realizzazione delle 
funzioni richieste o aggiungere nuove funzioni, tuttavia
le nuove funzioni devono essere fornite specifiche chiare
del funzionamento (nei commenti) e test di funzionamento adeguati
 (nel file "moreTest.py")

 ========================================================================
 GUI - Interfaccia grafica utente
 ========================================================================

 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che carichi automaticamente il file 
 hotel_base.txt, permetta di mostrare sin da subito le stanze dell'hotel indicando tipo e numero della stanza 
 (con extra in caso di suite) e le seguenti funzionalità:
 - mostrare la lista di prenotazioni dell'hotel;
 - prenotazione di una stanza;
 - disdire la prenotazione di una stanza;
 - ottenere il prezzo di una prenotazione dato l'indice:
 - mostrare l'hotel ad una certa data inserendo i nomi dei clienti nelle stanze a quella data;
 - ottenere le stanze libere ad una certa data;
 - ottenere le prenotazioni di uno specifico cliente inserendo il nome;
 - ottenere il numero di persone nell'albergo ad una certa data;
 - salvare o caricare da file lo stato dell'hotel permettendo di inserire il nome del file.
 - uscire dall'applicazione 
 Per uscire dall'applicazione deve essere possibile usare sia mouse che tastiera.
 L'aspetto dell'interfaccia viene deciso dallo studente.

 NOTE IMPORTANTI: LEGGERE ATTENTAMENTE
---------------------------------------

1) tutti gli elaborati verranno confrontati fra di loro con tool automatici
   per stabilire eventuali situazioni di PLAGIO. Gli elaborato sono
   ragionevolmente simili verranno scartati.

2) Chi in sede di orale risulta palesemente non essere l'autore del software
   consegnato in uno degli assegnamenti dovra' ripetere l'esame con
   un nuovo progetto

3) Tutti i comportamenti scorretti ai punti 1 e 2 verranno segnalati
   ufficialmente al presidente del corso di laurea

----------------------------
 VALUTAZIONE DELL'ASSEGNAMENTO:
----------------------------

La modalità di valutazione degli assegnamenti è descritta nel file pdf.
