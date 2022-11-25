import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"
    pesel2 = "54321678900"

    @classmethod
    def setUpClass(cls):
        konto = Konto(cls.imie, cls.nazwisko, cls.PESEL)
        RejestrKont.dodaj(konto)

    def test_1_dodaj_konto(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.ilosc(), 2, "Konto nie zostało dodane do listy")

    def test_2_dodaj_konto_2(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel2)
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.ilosc(), 3, "Konto nie zostało dodane do listy")

    def test_3_szukaj(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel2)
        szukaj = RejestrKont.szukaj(self.pesel2)
        self.assertNotEqual(szukaj, None, "Konto zostało źle wyszukane")

    def test_4_szukaj_konto_nie_istnieje(self):
        pesel = "09876543211"
        szukaj = RejestrKont.szukaj(pesel)
        self.assertEqual(szukaj, None, "Nie istniejące konto zostało znalezione")

    def test_5_ilosc_kont(self):
        RejestrKont.dodaj(Konto(self.imie, self.nazwisko, self.PESEL))
        RejestrKont.dodaj(Konto("A", "A", "09876543211"))
        ilosc = RejestrKont.ilosc()
        self.assertEqual(ilosc, 5, "Zła ilość kont")



    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []