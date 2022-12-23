import unittest
from unittest.mock import patch

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class HistoriaOperacji(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"

    nip = "1234567890"
    nazwa = "nazwa"

    def test_dodawanie_operacji_dostanie_przelew_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        self.assertEqual(konto.historia, [100], "Operacja dostanie przelewu nie została poprawnie dodawana do historii - osobiste")

    def test_dodawanie_operacji_przelew_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.przelew(30)
        self.assertEqual(konto.historia, [-30], "Operacja przelewu nie została poprawnie dodawana do historii - osobiste")

    def test_dodawanie_operacji_przelew_ekspress_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.przelew_ekspress(10)
        self.assertEqual(konto.historia, [-10, -1], "Operacja przelewu ekspress nie została poprawnie dodawana do historii - osobiste")

    def test_dodanie_operacji_ciag_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.dostaniePrzelew(20)
        konto.przelew(100)
        konto.przelew_ekspress(20)
        self.assertEqual(konto.historia, [20, -100, -20, -1], "Operacje nie zostały poprawnie dodane - osobiste")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_dodawanie_operacji_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        self.assertEqual(konto.historia, [100], "Operacja dostanie przelewu nie została poprawnie dodawana do historii - firma")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_dodawanie_operacji_przelew_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 200
        konto.przelew(34)
        self.assertEqual(konto.historia, [-34], "Operacja przelewu nie została poprawnie dodawana do historii - firma")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_dodawanie_operacji_przelew_ekspress_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 200
        konto.przelew_ekspress(10)
        self.assertEqual(konto.historia, [-10, -5], "Operacja przelewu ekspress nie została poprawnie dodawana do historii - firma")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_dodanie_operacji_ciag_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 200
        konto.dostaniePrzelew(20)
        konto.przelew(102)
        konto.przelew_ekspress(25)
        self.assertEqual(konto.historia, [20, -102, -25, -5], "Operacje nie zostały poprawnie dodane - firma")