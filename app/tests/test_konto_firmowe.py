import unittest
from unittest.mock import patch, Mock

from ..KontoFirmowe import KontoFirmowe

class TestKontoFirmowe(unittest.TestCase):
    nip = "1234567890"
    name = "nazwa"

    def _mock_response(self, status):
        return Mock(status_code=status)
    
    @patch('app.KontoFirmowe.KontoFirmowe.nip_czy_istnieje')
    def test_tworzenie_konta_firmy(self, mock_nip_czy_istnieje):
        mock_nip_czy_istnieje.return_value = True
        konto = KontoFirmowe(self.nip, self.name)
        self.assertEqual(konto.nip, self.nip, "Nip nie został zapisany")
        self.assertEqual(konto.name, self.name, "Nazwa nie została zapisana")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    @patch('requests.get')
    def test_nip_dlugosc(self, mock_g):
        mock_res = self._mock_response(status=400)
        mock_g.return_value = mock_res
        nip_krotki = "23"
        konto = KontoFirmowe(nip_krotki, self.name)
        self.assertEqual(konto.nip, "Pranie!")
        
    @patch('requests.get')
    def test_nip_litery(self, mock_g):
        mock_res = self._mock_response(status=400)
        mock_g.return_value = mock_res
        nip_litery = "2937asdsd"
        konto = KontoFirmowe(nip_litery, self.name)
        self.assertEqual(konto.nip, "Pranie!")
