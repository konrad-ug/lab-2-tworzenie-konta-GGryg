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
        konto = Konto(self.imie, self.nazwisko, self.pesel2)
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.ilosc(), 2, "Konto nie zostało dodane do listy")

    def test_2_sprawdznie_peselu_1(self):
        czy_dostepny = RejestrKont.sprawdz_pesel("09876543216")
        self.assertEqual(czy_dostepny, True)

    def test_3_sprawdzenie_peselu_2(self):
        czy_dostepny = RejestrKont.sprawdz_pesel(self.PESEL)
        self.assertEqual(czy_dostepny, False)

    def test_3_dodaj_konto_2(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel2)
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.ilosc(), 2, "Konto zostało dodane do listy pomiomo że pesel już jest zajęty")

    def test_4_dodaj_konto_3(self):
        konto = Konto(self.imie, self.nazwisko, "09876543219")
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.ilosc(), 3, "Konto nie zostało dodane")

    def test_5_szukaj(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel2)
        szukaj = RejestrKont.szukaj(self.pesel2)
        self.assertNotEqual(szukaj, None, "Konto zostało źle wyszukane")

    def test_6_szukaj_konto_nie_istnieje(self):
        pesel = "09876543211"
        szukaj = RejestrKont.szukaj(pesel)
        self.assertEqual(szukaj, None, "Nie istniejące konto zostało znalezione")

    def test_7_ilosc_kont(self):
        RejestrKont.dodaj(Konto(self.imie, self.nazwisko, "80987654321"))
        RejestrKont.dodaj(Konto("A", "A", "09876543211"))
        ilosc = RejestrKont.ilosc()
        self.assertEqual(ilosc, 5, "Zła ilość kont")

    def test_8_usun_konto(self):
        ilosc_przed = RejestrKont.ilosc()
        konto = RejestrKont.szukaj(self.PESEL)
        RejestrKont.usun(konto)
        ilosc_po = RejestrKont.ilosc()
        self.assertEqual(ilosc_po, ilosc_przed - 1, "Ilość kont się nie zmieniła po usunięciu")




    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []