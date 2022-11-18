import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PESEL = self.pesel_poprawnosc(pesel)
        self.kod = kod
        self.oplata_ekspres = 1
        self.historia = []

        self.coupon(kod, pesel)

    def pesel_poprawnosc(self, pesel):
        help = re.search(r"^[0-9]*$", pesel)
        if len(pesel) != 11:
            return "Nie poprawny pesel"
        else:
            if help == None:
                return "Nie poprawny pesel"
            else:
                return pesel
    
    def coupon(self, kod, pesel):
        if kod != None and re.match(r"\b[6-9|0][0-9]{10}\b", pesel):
            self.saldo = 50

    def przelew(self, kwota):
        self.saldo -= kwota
        self.historia.append(-kwota)

    def dostaniePrzelew(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelew_ekspress(self, kwota):
        self.saldo -= kwota + self.oplata_ekspres
        self.historia.append(-kwota)
        self.historia.append(-self.oplata_ekspres)

    def zaciagnij_kedyt(self, kwota):
        if len(self.historia) < 5:
            return False
        suma = 0
        for i in self.historia[-5:]:
            suma += i

        czy_dodatnie = True
        for i in self.historia[-3:]:
            if i < 0:
                czy_dodatnie = False
        
        if suma > kwota and czy_dodatnie:
            self.saldo += kwota
            return True
        return False