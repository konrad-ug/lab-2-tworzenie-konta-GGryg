import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PESEL = pesel
        self.kod = kod

        self.coupon(kod, pesel)
    
    def coupon(self, kod, pesel):
        if kod != None and re.match(r"\b[6-9|0][0-9]{10}\b", pesel):
            self.saldo = 50

    def przelew(self, kwota):
        self.saldo -= kwota

    def dostaniePrzelew(self, kwota):
        self.saldo += kwota