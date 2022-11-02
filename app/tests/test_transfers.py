import unittest

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
        self.assertEqual(konto.saldo, self.doPzelewu, "saldo się nie zwiększyło")

    def test_zrobienie_przelewu(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 1000
        konto.przelew(self.doPzelewu)
        self.assertEqual(konto.saldo, 1000-self.doPzelewu, "saldo się nie zmiejszyło")

    def test_przelew_zbyt_duzy(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 100
        konto.przelew(self.doPzelewu)
        self.assertLess(konto.saldo, 0, "Zbyt duży przelew został wykonany")

    def test_dostanie_przelewu_firma(self):
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.dostaniePrzelew(self.doPzelewu)
        self.assertEqual(konto.saldo, self.doPzelewu, "saldo się nie zwiększyło")

    def test_zrobienie_przelewu_firma(self):
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 1000
        konto.przelew(self.doPzelewu)
        self.assertEqual(konto.saldo, 1000-self.doPzelewu, "saldo się nie zmiejszyło")

    def test_przelew_zbyt_duzy_firma(self):
        konto = KontoFirmowe(self.nip, self.nazwa)
        konto.saldo = 100
        konto.przelew(self.doPzelewu)
        self.assertLess(konto.saldo, 0, "Zbyt duży przelew został wykonany")
