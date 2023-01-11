import unittest
from unittest.mock import patch, Mock, MagicMock
import datetime

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from ..SMTP import SMTPConnection

class SendingMails(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"

    nip = "1234567890"
    name = "nazwa"

    date_today = datetime.date.today()
    subject = "Wyciąg z dnia " + str(date_today)
    textp = "Twoja historia konta to: "
    textb = "Historia konta Twojej firmy to: "
    email = "test@test.com"

    def _mock_response(self, status):
        return Mock(status_code=status)

    def test_send_mail_personal(self):
        text = self.textp + "[100]"
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        connector = SMTPConnection()
        connector.send = MagicMock(return_value = True)
        status = konto.send_mail(self.email, connector)
        self.assertEqual(status, True, "Nie udało się wysłać maila")
        connector.send.assert_called_once_with(self.subject, text, self.email)

    def test_send_mail_personal_bad(self):
        text = self.textp + "[100]"
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        connector = SMTPConnection()
        connector.send = MagicMock(return_value = False)
        status = konto.send_mail(self.email, connector)
        self.assertEqual(status, False, "Nie udało się wysłać maila")
        connector.send.assert_called_once_with(self.subject, text, self.email)

    @patch('requests.get')
    def test_send_mail_business(self, mock_nip_exists):
        text = self.textb + "[100]"
        mock_res = self._mock_response(status=200)
        mock_nip_exists.return_value = mock_res
        konto = KontoFirmowe(self.nip, self.name)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        connector = SMTPConnection()
        connector.send = MagicMock(return_value = True)
        status = konto.send_mail(self.email, connector)
        self.assertEqual(status, True, "Nie udało się wysłać maila")
        connector.send.assert_called_once_with(self.subject, text, self.email)


    @patch('requests.get')
    def test_send_mail_business_bad(self, mock_nip_exists):
        text = self.textb + "[100]"
        mock_res = self._mock_response(status=200)
        mock_nip_exists.return_value = mock_res
        konto = KontoFirmowe(self.nip, self.name)
        konto.saldo = 200
        konto.dostaniePrzelew(100)
        connector = SMTPConnection()
        connector.send = MagicMock(return_value = False)
        status = konto.send_mail(self.email, connector)
        self.assertEqual(status, False, "Wysłanie się powidoło mimo tego że nie miało")
        connector.send.assert_called_once_with(self.subject, text, self.email)

