import unittest
from unittest.mock import patch
from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestBankTransfers(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    doPzelewu = 500

    nazwa = "nazwa"
    nip = "1234567890"
    
    def test_dostanie_przelewu(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.dostaniePrzelew(self.doPzelewu)
        self.assertEqual(konto.saldo, self.doPzelewu, "saldo się nie zwiększyło, konto osobiste")

    def test_zrobienie_przelewu(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 1000
        konto.przelew(self.doPzelewu)
        self.assertEqual(konto.saldo, 1000-self.doPzelewu, "saldo się nie zmiejszyło, konto osobiste")

    def test_przelew_zbyt_duzy(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 100
        konto.przelew(self.doPzelewu)
        self.assertLess(konto.saldo, 0, "Zbyt duży przelew został wykonany, konto osobiste")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_dostanie_przelewu_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.dostaniePrzelew(self.doPzelewu)
        self.assertEqual(konto.saldo, self.doPzelewu, "saldo się nie zwiększyło, konto firmowe")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_zrobienie_przelewu_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 1000
        konto.przelew(self.doPzelewu)
        self.assertEqual(konto.saldo, 1000-self.doPzelewu, "saldo się nie zmiejszyło, konto firmowe")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_przelew_zbyt_duzy_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 100
        konto.przelew(self.doPzelewu)
        self.assertLess(konto.saldo, 0, "Zbyt duży przelew został wykonany, konto firmowe")

    def test_przelew_ekspress_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 1000
        konto.przelew_ekspress(400)
        self.assertEqual(konto.saldo, 599, "Przelew ekspresowy nie pobiera oplaty poprawnie, konto osobiste")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_przelew_ekspress_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 1000
        konto.przelew_ekspress(400)
        self.assertEqual(konto.saldo, 595, "Przelew ekspresowy nie pobiera oplaty poprawnie, konto firmowe")

    def test_przelew_ekspress_za_duzy_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 400
        konto.przelew_ekspress(500)
        self.assertLess(konto.saldo, -1, "Zbyt duży przelew ekspresowy został wykonany, konto osobiste")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_przelew_ekspress_za_duzy_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 400
        konto.przelew_ekspress(500)
        self.assertLess(konto.saldo, -5, "Zbyt duży przelew ekspresowy został wykonany, konto firmowe")

    def test_przelew_ekspress_oplata_nieprawidlowa_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 400
        konto.przelew_ekspress(400)
        self.assertEqual(konto.saldo, -1, "Nie wystarczjąco środków by pobrać opłate, konto osobiste")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_przelew_ekspress_oplata_nieprawidlowa_firma(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 400
        konto.przelew_ekspress(400)
        self.assertEqual(konto.saldo, -5, "Nie wystarczająco środków by pobrać opłate, konto firmowe")