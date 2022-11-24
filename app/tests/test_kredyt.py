import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


class TestKredyt(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"

    name = "nazwa"
    nip = "1234567890"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.PESEL)
        self.kontoFirma = KontoFirmowe(self.nip, self.name)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([500, 10, -100, -200, 20], 300, False, 0),
        ([100, 10, 100, 200, 20], 500, False, 0),
        ([500, 10, 100, 200, 20], 830, False, 0),
        ([], 500, False, 0),
        ([100, 200, 300], 500, False, 0),
        ([100, 200, 300], 1000, False, 0),
        ([100, 200, 300], 600, False, 0)
    ])
    def test_kredyt_poprawnie_przyznany(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kedyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik, "Kredyt został nie poprawnie przyznany")
        self.assertEqual(self.konto.saldo, oczekiwane_saldo,
                         "Saldo po zaciągnięciu kredytu zostało zmianione nie poprawnie")

    @parameterized.expand([
        (1000, [-1775, 100, -100, 200], 500, True, 1500),
        (1000, [-1775, 100, 2000, -1000], 501, False, 1000),
        (1000, [1775, 400, -500, 100], 500, False, 1000),
        (1000, [1775, -400, 400], 501, False, 1000),
        (0, [], 500, False, 0),
        (2000, [400, -100, 40, -1775], 1000, True, 3000)
    ])
    def test_kredyt_firma(self, saldo, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.kontoFirma.saldo = saldo
        self.kontoFirma.historia = historia
        czy_przyznany = self.kontoFirma.zaciagnij_kedyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik, "Kredyt został nie poprawnie przyznany")
        self.assertEqual(self.kontoFirma.saldo, oczekiwane_saldo, "Saldo po zaciągnięciu kredytu zostało zmienione nie poprawnie")