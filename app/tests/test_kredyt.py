import unittest
import parameterized

from ..Konto import Konto


class TestKredyt(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.PESEL)

    @parameterized.expand({
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([500, 10, -100, -200, 20], 300, False, 0),
        ([100, 10, 100, 200, 20], 500, False, 0),
        ([500, 10, 100, 200, 20], 830, False, 0),
        ([], 500, False, 0),
        ([100, 200, 300], 500, False, 0),
        ([100, 200, 300], 1000, False, 0),
        ([100, 200, 300], 600, False, 0)
    })
    def test_kredyt_poprawnie_przyznany(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kedyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik, "Kredyt został nie poprawnie przyznany")
        self.assertEqual(self.konto.saldo, oczekiwane_saldo,
                         "Saldo po zaciągnięciu kredytu zostało zmianione nie poprawnie")
