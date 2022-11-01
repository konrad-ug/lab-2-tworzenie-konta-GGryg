import unittest

from ..Konto import Konto

class TestBankTransfers(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    doPzelewu = 500
    
    def test_dostanie_przelewu(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.dostaniePrzelew(500)
        self.assertEqual(konto.saldo, 500, "saldo się nie zwiększyło")

    def test_zrobienie_przelewu(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 1000
        konto.przelew(self.doPzelewu)
        self.assertEqual(konto.saldo, 500, "saldo się nie zmiejszyło")
        self.assertGreaterEqual(konto.saldo, 0, "Zbyt duży przelew został wykonany")
