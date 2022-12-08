from app.Konto import Konto

class RejestrKont():
    lista = []

    @classmethod
    def dodaj(cls, konto):
        if cls.sprawdz_pesel(konto.PESEL):
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

    @classmethod
    def usun(cls, konto):
        cls.lista.remove(konto)

    @classmethod
    def sprawdz_pesel(cls, pesel):
        for konto in cls.lista:
            if konto.PESEL == pesel:
                return False
        return True