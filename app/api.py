# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print("Request o stworzenie konta z danymi: " + dane)
    konto = Konto(dane["imie"], dane["nazwisko"], dane["PESEL"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ilosc", methods=['GET'])
def ilosc():
    return "Ilość kont: "+ RejestrKont.ilosc(), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto(pesel):
    print("Request o wyszukanie konta o peselu " + pesel)
    konto = RejestrKont.szukaj(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.PESEL), 200