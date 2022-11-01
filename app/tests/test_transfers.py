import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestBankTransfers(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    doPzelewu = 500
    zbytDuze = 1200

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
        self.assertGreaterEqual(konto.saldo, 0, "Zbyt duży przelew został wykonany")

