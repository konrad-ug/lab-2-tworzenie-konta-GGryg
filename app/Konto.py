class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PESEL = pesel
        self.kod = kod

        self.coupon(kod)
    
    def coupon(self, kod):
        if kod != None:
            self.saldo = 50