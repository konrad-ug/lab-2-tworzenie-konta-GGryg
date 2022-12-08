import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "nick",
        "nazwisko": "cave",
        "PESEL": "12345679903"
    }

    url = "http://127.0.0.1:5000"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_tworzenie_konta_popwtorka_pesela(self):
        create_resp = requests.post(self.url + "/konta/stowrz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 404)

    def test_3_get_po_peselu(self):
        get_resp = requests.get(self.url + "/konta/konto/" + self.body["PESEL"])
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_4_put(self):
        update = {
            "imie": "osd"
        }
        put_resp = requests.put(self.url + "/konta/konto/zmien/" + self.body["PESEL"], json=update)
        self.assertEqual(put_resp.status_code, 200)
        get_resp = requests.get(self.url + "/konta/konto/" + self.body["PESEL"])
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], update["imie"])

    def test_5_delete(self):
        delete_response = requests.delete(self.url + "/konta/konto/usun/" + self.body['PESEL'])
        self.assertEqual(delete_response.status_code, 200)
