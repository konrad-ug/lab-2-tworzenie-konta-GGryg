# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    czy_dostępny = RejestrKont.sprawdz_pesel(dane["PESEL"])
    if czy_dostępny == False:
        print("NIE")
        return jsonify("Konto o takim peselu już istanieje"), 400
    konto = Konto(dane["imie"], dane["nazwisko"], dane["PESEL"])
    RejestrKont.dodaj(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ilosc", methods=['GET'])
def ilosc():
    return f"Ilość kont: {RejestrKont.ilosc()}", 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto(pesel):
    print("Request o wyszukanie konta o peselu " + pesel)
    konto = RejestrKont.szukaj(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.PESEL, saldo=konto.saldo), 200

@app.route("/konta/konto/zmien/<pesel>", methods=['PUT'])
def zmien_dane(pesel):
    dane = request.get_json()
    print(f"Request o zmieniuniu danych z {dane}")
    konto = RejestrKont.szukaj(pesel)
    print("znaleziono")
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.PESEL = dane["PESEL"] if "PESEL" in dane else konto.PESEL
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.saldo
    return jsonify("Update zakończony z powodzeniem"), 200

@app.route("/konta/konto/usun/<pesel>", methods=['DELETE'])
def usuc_konto(pesel):
    print(f"Request o usunięciu konto o peselu: {pesel}")
    konto = RejestrKont.szukaj(pesel)
    RejestrKont.usun(konto)
    return "Konto zostało usunięte", 200
