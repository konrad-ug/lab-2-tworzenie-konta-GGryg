from app.Konto import Konto
import re
import requests
import os
import datetime

class KontoFirmowe(Konto):
    def __init__(self, nip, name):
        self.name = name
        self.nip = nip if self.nip_czy_istnieje(nip) and self.nip_poprawnosc(nip) else "Pranie!"
        self.saldo = 0
        self.oplata_ekspres = 5
        self.historia = []

    def nip_poprawnosc(self, nip):
        help = re.search(r"^[0-9]{10}$", nip)
        if help == None:
            return False
        else:
            return True

    @classmethod
    def nip_czy_istnieje(cls, nip):
        date_today = datetime.date.today()
        today = date_today.strftime("%Y-%m-%d")
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl')
        resp = requests.get(gov_url + "/api/search/nip/" + nip + "?date=" + today)
        if resp.status_code == 200:
            return True
        return False

    def zaciagnij_kedyt(self, kwota):
        if -1775 not in self.historia or self.saldo < 2 * kwota:
            return False
        self.saldo += kwota
        return True


