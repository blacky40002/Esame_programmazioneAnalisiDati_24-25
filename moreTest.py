import unittest
from hotel import Hotel
from stanze import Singola, Doppia
from classi import Data

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

if __name__ == '__main__':
    unittest.main()
