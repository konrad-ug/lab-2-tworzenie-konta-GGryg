from app.Konto import Konto

class RejestrKont():
    lista = []

    @classmethod
    def dodaj(cls, konto):
        cls.lista.append(konto)

    @classmethod
    def ilosc(cls):
        return len(cls.lista)

    @classmethod
    def szukaj(cls, pesel):
        for konto in cls.lista:
            if konto.PESEL == pesel:
                return konto
        return None