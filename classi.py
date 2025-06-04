"""
Definire una classe Data per rappresentare una specifica data all'interno di un anno non bisestile.
#STATO:
- mappa_mesi: dizionario con chiave il numero del mese e valore il numero di giorni. Esempio: {1: 31, 2: 28, ...}. Sfruttare questa mappa per controllare la validità di una data e per calcolare la differenza tra due date.
- giorno: intero con valore compreso tra 1 e il numero di giorni del mese. 
- mese: intero con valore compreso tra 1 e 12.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- Costruttore che prende in input giorno, mese e anno e inizializza le variabili di istanza. Esempio di utilizzo: d = Data(1, 1) FATTO
- Metodi getter e setter per giorno e mese. FATTO
- Metodo per la rappresentazione in forma di stringa della data, rispettando il formato di esempio: "1/1"
- Metodo per il calcolo della differenza in giorni tra due date. Esempio di utilizzo: d2 - d1 dove d1 = Data(1, 1), d2 = Data(1, 2), risultato -> 31. Nota, d2 - d1 deve essere uguale a d1 - d2.
- Metodo per il confronto di uguaglianza tra due date.
- Metodo per il confronto di maggiore tra due date. Esempio di utilizzo: d1 < d2
- Metodo per il confronto di minore tra due date. Esempio di utilizzo: d1 > d2
- Metodo per il confronto di minore o uguale tra due date. Esempio di utilizzo: d1 <= d2
"""
#chiedere perchè se il costruttore prende in input giorno, mese e anno, ma poi si inizializzano solo giorno e mese e non l'anno
#dire se va bene il controllo del giorno e mese nel costruttore o se va fatto in un metodo setter
class Data:
    mappa_mesi = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #2025 anno di riferimento non bisestile

    def __init__(self, giorno:int, mese:int,anno=2025 ):
        self._mese = None 
        self._giorno = None   
        self.mese = mese
        self.giorno = giorno
    #metodi getter e setter per giorno e mese
    #todo perchè qui facciamo in questo modo e poi piu avanti con i param? non è meglio fare in un modo solo per consistenza?
    @property
    def giorno(self):
        return self._giorno

    @giorno.setter
    def giorno(self, valore):
        #controllo che il mese sia stato impostato
        if self._mese is None:
            raise ValueError("Impossibile impostare il giorno: il mese non è ancora stato definito.")
        # Recupero il numero massimo di giorni nel mese
        giorni_max = self.mappa_mesi.get(self._mese)
        gestione_errori(valore,int,0,giorni_max+1)  
        self._giorno = valore

    @property
    def mese(self):
        return self._mese

    @mese.setter
    def mese(self, valore):
        gestione_errori(valore,int,0,13)
        self._mese = valore  
    #metodo per la rappresentazione in forma di stringa della data
    def data_in_stringa(self):
        return f"{self._giorno}/{self._mese}"
    
    #metodo per il calcolo della differenza in giorni tra due date
    def __sub__(self, other):
        gestione_errori(other,Data)
        # Calcola i giorni dall'inizio dell'anno per self e other usando la mappa_mesi
        giorni_self = sum(Data.mappa_mesi[m] for m in range(1, self._mese)) + self._giorno
        giorni_other = sum(Data.mappa_mesi[m] for m in range(1, other._mese)) + other._giorno
        return abs(giorni_self - giorni_other)

    #metodo per il confronto di uguaglianza tra due date
    def __eq__(self, other):
        gestione_errori(other,Data)
        return self._giorno == other._giorno and self._mese == other._mese # ritorna un valore booleano
    
    #metodo per il confronto di maggiore tra due date
    def __lt__(self, other):
        gestione_errori(other,Data)
        return (self._mese, self._giorno) < (other._mese, other._giorno) # ritorna un valore booleano 
    
    #metodo per il confronto di min
    def __gt__(self, other):
        gestione_errori(other,Data)
        return (self._mese, self._giorno) > (other._mese, other._giorno) # ritorna un valore booleano
    #metodo per il confronto di minore o uguale tra due date
    def __le__(self, other):
         gestione_errori(other,Data)
         return (self._mese, self._giorno) <= (other._mese, other._giorno) # ritorna un valore booleano
    def __str__(self):
    # Ritorna la stringa "giorno/mese"
            return f"{self._giorno}/{self._mese}"
    @classmethod
    def from_string(cls, s: str):
        """
        Crea e restituisce un oggetto Data a partire da una stringa "giorno/mese".
        Esempio: "1/2" => Data(1,2)
        """
        parti = s.split("/")
        giorno = int(parti[0])
        mese = int(parti[1])
        # se esiste anche l'anno, dovresti gestirlo; per i test, sembra basti ignorarlo
        return cls(giorno, mese)
    
"""
Definire una classe Prenotazione per rappresentare una prenotazione di una stanza di un hotel.
Le prenotazioni saranno solo all'interno dello stesso anno solare. Ad esempio, non è possibile avere come data di arrivo il 27/12 e come data di partenza il 5/1.
#STATO:
- id_prenotazione: intero non negativo.
- numero_stanza: intero positivo.
- data_arrivo: oggetto di tipo Data.
- data_partenza: oggetto di tipo Data, non deve essere precedente alla data di arrivo.
- nome_cliente: stringa non vuota.
- numero_persone: intero positivo.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- Costruttore che prende in input il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone. Esempio di utilizzo: p = Prenotazione(101, Data(1, 1), Data(5, 1), "Mario Rossi", 2)
- Metodi getter e setter per il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone.
- Metodo per la rappresentazione in forma di stringa della prenotazione. Rispettando il formato di esempio: "Prenotazione 1 per stanza 101 da 1/1 a 5/1 a nome Mario Rossi per 1 persone"
- Metodo per il confronto di uguaglianza profonda tra due prenotazioni.
"""
#cercare i metodi per il confronto di uguaglianza profonda o no
class Prenotazione:         #TODO non è stata considerato questo punto presente nellle linee guida: "Non si considerano date a cavallo della fine dell’anno, ad esempio: arrivo 31/12 partenza 1/1"
    id_counter = 1

    def __init__(self, id_prenotazione=None, numero_stanza=0, data_arrivo=None, data_partenza=None, nome_cliente="", numero_persone=0):
        if id_prenotazione is None:
              self.id_prenotazione = Prenotazione.id_counter
              Prenotazione.id_counter += 1
        else:
            gestione_errori(id_prenotazione,int,0)
            self.id_prenotazione = id_prenotazione

        self.numero_stanza = numero_stanza
        self.data_arrivo = data_arrivo
        self.data_partenza = data_partenza
        self.nome_cliente = nome_cliente
        self.numero_persone = numero_persone
#- Metodi getter e setter per il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone.

    @property
    def id_prenotazione(self):
        return self._id_prenotazione

    @id_prenotazione.setter
    def id_prenotazione(self, value):
        gestione_errori(value,int,0)
        self._id_prenotazione = value

    @property
    def numero_stanza(self):
        return self._numero_stanza

    @numero_stanza.setter
    def numero_stanza(self, value):
        gestione_errori(value,int,0)
        self._numero_stanza = value

    @property
    def data_arrivo(self):
        return self._data_arrivo

    @data_arrivo.setter
    def data_arrivo(self, value):
        gestione_errori(value,Data)
        self._data_arrivo = value

    @property
    def data_partenza(self):
        return self._data_partenza

    @data_partenza.setter   
    def data_partenza(self, value):
        gestione_errori(value,Data) 
        if self.data_arrivo is None:
            raise ValueError("Impostare la data di arrivo prima della data di partenza")
        if value < self.data_arrivo:
            raise ValueError("La data di partenza non può essere precedente alla data di arrivo.")
        self._data_partenza = value

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, value):
        value = value.strip()
        gestione_errori(value,str)
        lunghezza_nome = len(value)
        if lunghezza_nome > 20 or lunghezza_nome < 3: #controllo lunghezza nome
            raise ValueError("Il nome deve essere lungo almeno 3 caratteri ed un massimo di 20")
        self._nome_cliente = value
 
    @property
    def numero_persone(self):
        return self._numero_persone

    @numero_persone.setter
    def numero_persone(self, value):
        gestione_errori(value,int,0)
        self._numero_persone = value

    #- Metodo per la rappresentazione in forma di stringa della prenotazione. Rispettando il formato di esempio: "Prenotazione 1 per stanza 101 da 1/1 a 5/1 a nome Mario Rossi per 1 persone"

    def __str__(self):
        persone_str = "persona" if self.numero_persone == 1 else "persone"
        return f"Prenotazione {self.id_prenotazione} per stanza {self.numero_stanza} dal {self.data_arrivo.giorno}/{self.data_arrivo.mese} al {self.data_partenza.giorno}/{self.data_partenza.mese} a nome {self.nome_cliente} per {self.numero_persone} {persone_str}"

    #- Metodo per il confronto di uguaglianza profonda tra due prenotazioni.
    def __eq__(self, other):
        if not isinstance(other, Prenotazione):
            return False
        return (
            self.numero_stanza == other.numero_stanza and
            self.data_arrivo == other.data_arrivo and
            self.data_partenza == other.data_partenza and
            self.nome_cliente == other.nome_cliente and
            self.numero_persone == other.numero_persone
        )

def gestione_errori(data, tipo_dato, min=None, max=None):
    if not isinstance(data, tipo_dato):
        raise TypeError(f"Il valore deve essere di tipo {tipo_dato.__name__}.")

    if min is not None:
        if data < min:
            raise ValueError(f"Il valore deve essere maggiore di {min}.")

    if max is not None:
          if data > max:
            raise ValueError(f"Il valore deve essere minore a {max}.")

