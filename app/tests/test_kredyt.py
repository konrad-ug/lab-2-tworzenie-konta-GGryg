import unittest

from ..Konto import Konto

class TestKredyt(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    PESEL = "12345678901"

    def test_kredyt_poprawnie_przyznany(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [-100, 100, 100, 100, 600]
        czy_przyznany = konto.zaciagnij_kedyt(500)
        self.assertEqual(czy_przyznany, True, "Kredyt został nie poprawnie przyznany")
        self.assertEqual(konto.saldo, 500, "Saldo po zaciągnięciu kredytu zostało zmianione nie poprawnie")

    def test_kredyt_nie_przyzany_warunek_a_nie_spelniony(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [500, 10, -100, -200, 20]
        czy_przyznany = konto.zaciagnij_kedyt(300)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo że 3 ostatnie transackjie nie są przelewem na konto")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")

    def test_kredyt_nie_przyzany_warunek_b_nie_spelniony(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [100, 10, 100, 200, 20]
        czy_przyznany = konto.zaciagnij_kedyt(500)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo suma 5 ostatnich transakcji nie jest większa od kredytu ")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")


    def test_kredyt_nie_przyzany_warunek_b_nie_spelniony_rowny(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [500, 10, 100, 200, 20]
        czy_przyznany = konto.zaciagnij_kedyt(830)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo suma 5 ostatnich transakcji jest równa kredytowi")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")

    def test_kredyt_nie_przyzany_brak_historii(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = []
        czy_przyznany = konto.zaciagnij_kedyt(500)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo że nie ma historii")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")
    
    def test_kredyt_nie_przyzany_za_malo_transakcji(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [100, 200, 300]
        czy_przyznany = konto.zaciagnij_kedyt(500)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo że konto nie ma wystarczjąco transakcji")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")

    def test_kredyt_nie_przyzany_za_malo_transakcji_i_suma_jest_za_mala(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [100, 200, 300]
        czy_przyznany = konto.zaciagnij_kedyt(1000)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo że konto nie ma wystarczjąco transakcji oraz ich suma nie jest więksa od kredytu")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")

    def test_kredyt_nie_przyzany_za_malo_transakcji_i_suma_rowna(self):
        konto = Konto(self.imie, self.nazwisko, self.PESEL)
        konto.historia = [100, 200, 300]
        czy_przyznany = konto.zaciagnij_kedyt(600)
        self.assertEqual(czy_przyznany, False, "Kredyt został przyznany pomimo że konto nie ma wystarczjąco transakcji oraz ich suma jest równa kredytu")
        self.assertEqual(konto.saldo, 0, "Saldo się zmieniło pomino że konto nie jest wstanie zaciągnośc kredyt")
