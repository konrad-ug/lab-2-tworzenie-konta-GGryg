import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    kod = "PROM_XYZ"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.PESEL)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.PESEL, self.PESEL, "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.PESEL), 11, "Nie prawidłowa długość PESELa")

    #tutaj proszę dodawać nowe testy
    def test_tworzenie_konta_z_kodem(self):
        konto_z_kodem = Konto(self.ime, self.nazwisko, self.PESEL, self.kod)
        self.assertEqual(konto_z_kodem.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(konto_z_kodem.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto_z_kodem.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(konto_z_kodem.PESEL, self.PESEL, "PESEL nie został zapisany")
        self.assertEqual(len(konto_z_kodem.PESEL), 11, "Nie prawidłowa długość PESELa")
        self.assertEqual(konto_z_kodem.kod[0:4], "PROM_", "Nie ma początku PROM_")