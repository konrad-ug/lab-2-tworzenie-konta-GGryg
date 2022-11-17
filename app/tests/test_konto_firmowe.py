import unittest

from ..KontoFirmowe import KontoFirmowe

class TestKontoFirmowe(unittest.TestCase):
    nip = "1234567890"
    name = "nazwa"
    
    def test_tworzenie_konta_firmy(self):
        konto = KontoFirmowe(self.nip, self.name)
        self.assertEqual(konto.nip, self.nip, "Nip nie został zapisany")
        self.assertEqual(konto.name, self.name, "Nazwa nie została zapisana")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_nip_dlugosc(self):
        nip_krotki = "23"
        konto = KontoFirmowe(nip_krotki, self.name)
        self.assertEqual(konto.nip, "Niepoprawny NIP!")
        

    def test_nip_litery(self):
        nip_litery = "2937asdsd"
        konto = KontoFirmowe(nip_litery, self.name)
        self.assertEqual(konto.nip, "Niepoprawny NIP!")
