from app.Konto import Konto
import re

class KontoFirmowe(Konto):
    def __init__(self, nip, name):
        self.name = name
        self.nip = self.nip_poprawnosc(nip)
        self.saldo = 0

    def nip_poprawnosc(self, nip):
        help = re.search(r"^[0-9]*$", nip)
        if len(nip) != 10:
            return "Niepoprawny NIP!"
        else:
            if help == None:
                return "Niepoprawny NIP!"
            else:
                return nip

