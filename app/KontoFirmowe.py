from app.Konto import Konto
import re

class KontoFirmowe(Konto):
    def __init__(self, nip, name):
        self.name = name
        self.nip = self.nip_poprawnosc(nip)
        self.saldo = 0
        self.oplata_ekspres = 5
        self.historia = []

    def nip_poprawnosc(self, nip):
        help = re.search(r"^[0-9]{10}$", nip)
        if help == None:
            return "Niepoprawny NIP!"
        else:
            return nip

    def zaciagnij_kedyt(self, kwota):
        if -1775 not in self.historia or self.saldo < 2 * kwota:
            return False
        self.saldo += kwota
        return True

