import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    PESELS = "50123456789"
    kod = "PROM_XYZ"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.PESEL)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.PESEL, self.PESEL, "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.PESEL), 11, "Nie prawidłowa długość PESELa")
        self.assertRegex(pierwsze_konto.PESEL, r"\b[0-9]{11}\b")

    #tutaj proszę dodawać nowe testy
    def test_tworzenie_konta_z_kodem(self):
        konto_z_kodem = Konto(self.imie, self.nazwisko, self.PESEL, self.kod)
        self.assertEqual(konto_z_kodem.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(konto_z_kodem.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto_z_kodem.PESEL, self.PESEL, "PESEL nie został zapisany")
        self.assertEqual(len(konto_z_kodem.PESEL), 11, "Nie prawidłowa długość PESELa")
        self.assertRegex(konto_z_kodem.kod, r"\bPROM_[A-Z]{3}\b", "Zły kupon")
        self.assertEqual(konto_z_kodem.saldo, 0, "Saldo konta z kuponem nie równa się 0")
        self.assertRegex(konto_z_kodem.PESEL, r"\b[0-9]{11}\b")


    def test_konta_prawidlowe_z_kodem(self):
        konto_seniora = Konto(self.imie, self.nazwisko, self.PESELS, self.kod)
        self.assertEqual(konto_seniora.imie, self.imie, "Imie nie zostałozapisane!")
        self.assertEqual(konto_seniora.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto_seniora.PESEL, self.PESELS, "PESEL nie został zapisany")
        self.assertEqual(len(konto_seniora.PESEL), 11, "Nie prawidłowa długość PESELa")
        self.assertRegex(konto_seniora.PESEL, r"\b[6-9|0][0-9]{10}\b", "PESEL wskazuje na urodzenie przed 1960 rokiem")
        self.assertRegex(konto_seniora.kod, r"\bPROM_[A-Z]{3}\b", "Zły kupon")
        self.assertEqual(konto_seniora.saldo, 50, "Saldo konta seniora z kuponem nie równa się 50")

