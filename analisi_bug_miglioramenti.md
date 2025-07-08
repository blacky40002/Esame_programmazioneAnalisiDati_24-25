# Analisi Bug e Miglioramenti - Sistema Gestione Hotel

## 🐛 BUG IDENTIFICATI

### 1. **Bug critico in `classi.py` - Controllo date nel setter**
```python
# LINEA 34-41 in classi.py
@giorno.setter
def giorno(self, valore):
    if self._mese is None:
        raise ValueError("Impossibile impostare il giorno: il mese non è ancora stato definito.")
    giorni_max = self.mappa_mesi.get(self._mese)
    gestione_errori(valore,int,0,giorni_max+1)  # BUG: dovrebbe essere giorni_max, non giorni_max+1
    self._giorno = valore
```
**Problema**: Il controllo massimo permette giorni impossibili (es. 32 gennaio)
**Fix**: Cambiare `giorni_max+1` in `giorni_max`

### 2. **Bug di inconsistenza nell'interfaccia `Prenotazione`**
```python
# LINEA 104-107 in classi.py
def __init__(self, id_prenotazione=None, numero_stanza=0, data_arrivo=None, data_partenza=None, nome_cliente="", numero_persone=0):
```
**Problema**: Il costruttore accetta valori di default, ma nei test viene chiamato con tutti i parametri. Questo crea inconsistenza.

### 3. **Bug di logica in `hotel.py` - Controllo data partenza**
```python
# LINEA 59 in hotel.py  
if data_arrivo >= data_partenza:
    raise ValueError("La data di arrivo deve essere precedente alla data di partenza")
```
**Problema**: Non dovrebbe permettere arrivo uguale a partenza (soggiorno di 0 notti)

### 4. **Bug nella funzione `carica` in `hotel.py`**
```python
# LINEA 294-296 in hotel.py
elif tipo == "Suite":
    nuovo_stanze[numero] = Suite(numero, posti, ["TV", "Frigo"], prezzo)
```
**Problema**: Hardcoded degli extra per Suite, non preserva gli extra originali del file

### 5. **Bug nell'aggiornamento ID prenotazioni**
```python
# LINEA 318 in hotel.py
self.id_prenotazioni = max([0] + list(nuovo_prenotazioni.keys())) + 1
```
**Problema**: Non considera prenotazioni cancellate, potrebbe creare ID duplicati

## ⚠️ PROBLEMI DI PROGETTAZIONE

### 1. **Inconsistenza nell'uso di getter/setter**
- `classi.py` usa `@property` 
- `stanze.py` usa metodi `get_/set_`
- Manca standardizzazione

### 2. **Gestione errori non uniforme**
- Funzione `gestione_errori` ha parametri opzionali confusi
- Non tutti i controlli usano la stessa funzione

### 3. **Mancanza di validazione input**
- Nomi cliente troppo corti/lunghi non gestiti bene
- Date future non validate
- Prezzi negativi non bloccati adeguatamente

## 📈 MIGLIORAMENTI PROPOSTI

### 1. **Performance e Strutture Dati**
```python
# Aggiungere indici per ricerche frequenti
def __init__(self):
    self.stanze = {}
    self.prenotazioni = {}
    self.prenotazioni_per_stanza = {}  # Indice per stanza
    self.prenotazioni_per_cliente = {}  # Indice per cliente
```

### 2. **Miglioramento validazione Date**
```python
@classmethod
def is_valid_date(cls, giorno, mese):
    """Valida una data senza creare l'oggetto"""
    if mese < 1 or mese > 12:
        return False
    if giorno < 1 or giorno > cls.mappa_mesi.get(mese, 0):
        return False
    return True
```

### 3. **Aggiungere enum per tipi stanza**
```python
from enum import Enum

class TipoStanza(Enum):
    SINGOLA = "Singola"
    DOPPIA = "Doppia" 
    SUITE = "Suite"
```

### 4. **Logging e debugging**
```python
import logging

class Hotel:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # ... resto del codice
    
    def prenota(self, ...):
        self.logger.info(f"Tentativo prenotazione stanza {numero_stanza}")
        # ... logica prenotazione
```

### 5. **Gestione configurazione**
```python
# config.py
DEFAULT_SUITE_EXTRAS = ["TV", "Frigo"]
MAX_NOME_LUNGHEZZA = 50
MIN_NOME_LUNGHEZZA = 2
ANNO_RIFERIMENTO = 2025
```

### 6. **Miglioramento metodo `__str__` per debug**
```python
def __str__(self):
    stanze_dettaglio = [f"{s.get_tipo_stanza()}-{s.get_numero_stanza()}" 
                       for s in sorted(self.stanze.values(), 
                                     key=lambda x: x.get_numero_stanza())]
    return f"Hotel: {len(self.stanze)} stanze ({', '.join(stanze_dettaglio)}), {len(self.prenotazioni)} prenotazioni."
```

### 7. **Aggiungere metodi di utilità**
```python
def get_fatturato_periodo(self, data_inizio, data_fine):
    """Calcola il fatturato per un periodo"""
    fatturato = 0
    for pren in self.prenotazioni.values():
        if self._prenotazione_nel_periodo(pren, data_inizio, data_fine):
            fatturato += self.prezzo_prenotazione(pren.id_prenotazione)
    return fatturato

def get_tasso_occupazione(self, data):
    """Calcola percentuale di occupazione per una data"""
    stanze_occupate = len([p for p in self.prenotazioni.values() 
                          if p.data_arrivo <= data <= p.data_partenza])
    return (stanze_occupate / len(self.stanze)) * 100 if self.stanze else 0
```

## 🎯 MIGLIORAMENTI GUI (da implementare)

### 1. **Struttura MVC**
```python
# Separare logica di business da presentazione
class HotelController:
    def __init__(self, hotel_model, gui_view):
        self.model = hotel_model
        self.view = gui_view
```

### 2. **Validazione input real-time**
- Controllo date mentre utente digita
- Suggerimenti autocomplete per nomi clienti
- Validazione numero persone vs capacità stanza

### 3. **Feedback visivo**
- Calendario con disponibilità stanze
- Codici colore per tipi stanza
- Progress bar per operazioni lunghe

## 🔧 REFACTORING RACCOMANDATO

### 1. **Uniformare gestione errori**
```python
class HotelError(Exception):
    """Classe base per errori hotel"""
    pass

class StanzaNonTrovataError(HotelError):
    pass

class PrenotazioneNonValidaError(HotelError):
    pass
```

### 2. **Aggiungere type hints**
```python
from typing import List, Dict, Optional

def prenota(self, numero_stanza: int, data_arrivo: Data, 
           data_partenza: Data, nome_cliente: str, 
           numero_persone: int) -> int:
```

### 3. **Separare responsabilità**
- Classe `HotelManager` per operazioni complesse
- Classe `ReportGenerator` per statistiche
- Classe `FileManager` per I/O

## 📊 PRIORITÀ IMPLEMENTAZIONE

### 🔴 ALTA PRIORITÀ
1. Fix bug controllo giorni massimi
2. Fix bug caricamento Suite extras
3. Standardizzare gestione errori

### 🟡 MEDIA PRIORITÀ  
1. Implementare GUI completa
2. Aggiungere logging
3. Migliorare performance con indici

### 🟢 BASSA PRIORITÀ
1. Aggiungere type hints
2. Implementare pattern MVC
3. Aggiungere statistiche avanzate

## 📝 NOTE FINALI

Il codice è funzionalmente corretto (tutti i test passano) ma presenta diversi problemi di qualità del codice e potenziali bug in casi edge. La priorità dovrebbe essere:

1. **Correggere i bug critici** identificati
2. **Implementare la GUI** mancante  
3. **Migliorare la robustezza** del sistema
4. **Aggiungere funzionalità avanzate** per un uso reale

L'architettura generale è buona per un progetto didattico, ma necessiterebbe di significativi miglioramenti per un uso in produzione.