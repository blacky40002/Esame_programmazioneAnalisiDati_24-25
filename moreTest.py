import unittest
import tempfile
from hotel import Hotel
from stanze import Singola, Doppia
from classi import Data, Prenotazione

class TestHotelExtra(unittest.TestCase):
    def test_data_from_string(self):
        self.assertEqual(Data.from_string("5/2"), Data(5, 2))

    def test_doppia_get_tipo_stanza(self):
        stanza = Doppia(101, 50.0)
        self.assertEqual(stanza.get_tipo_stanza(), "Doppia")

    def test_rimuovi_stanza_elimina_prenotazioni(self):
        h = Hotel()
        h.aggiungi_stanza(Singola(100, 50.0))
        pren_id = h.prenota(100, Data(1,1), Data(2,1), "Test", 1)
        self.assertIn(pren_id, h.prenotazioni)
        h.rimuovi_stanza(100)
        self.assertNotIn(100, h.stanze)
        self.assertEqual(len(h.prenotazioni), 0)

class TestHotelVulnerabilities(unittest.TestCase):
    """Test che verificano la corrispondenza fra i commenti e l'implementazione."""

    def test_stanza_prezzo_base_validation(self):
        """Il commento indica che il prezzo deve essere > 1."""
        with self.assertRaises(ValueError):
            Singola(200, 0.5)

    def test_prenotazione_cross_year_not_allowed(self):
        """Le specifiche vietano prenotazioni a cavallo di due anni."""
        h = Hotel()
        h.aggiungi_stanza(Singola(101, 50.0))
        with self.assertRaises(ValueError):
            h.prenota(101, Data(31,12), Data(1,1), "Test", 1)

    def test_nome_cliente_troppo_corto(self):
        """Verifica che venga sollevata eccezione per nomi troppo brevi."""
        with self.assertRaises(ValueError):
            Prenotazione(1,101, Data(1,1), Data(2,1), "Al", 1)

    def test_numero_persone_deve_essere_positivo(self):
        """Lo stato richiede numero_persone positivo (>0)."""
        with self.assertRaises(ValueError):
            Prenotazione(2,101, Data(1,1), Data(2,1), "Mario", 0)

    def test_data_bool_non_valida(self):
        """I parametri giorno e mese dovrebbero essere interi e non booleani."""
        with self.assertRaises(TypeError):
            Data(True, 1)

    def test_carica_formato_non_valido(self):
        """Il metodo carica dovrebbe sollevare ValueError su formato errato."""
        h = Hotel()
        with tempfile.NamedTemporaryFile("w", delete=False) as tf:
            tf.write("Qualcosa\n")
            nome = tf.name
        with self.assertRaises(ValueError):
            h.carica(nome)

if __name__ == '__main__':
    unittest.main()
