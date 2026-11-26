
from fastapi.testclient import TestClient

from main import app

klijent = TestClient(app)


def test_cjenovnik():
    r = klijent.get("/cjenovnik")
    assert r.status_code == 200
    assert r.json() == {"standardna_cijena": 25, "cijena_3_plus": 20}


def test_jedan_dan():
    r = klijent.post("/cijena", json={"dani": 1, "godine": 18})
    assert r.json()["ukupna_cijena"] == 25


def test_dva_dana():
    r = klijent.post("/cijena", json={"dani": 2, "godine": 20})
    assert r.json()["ukupna_cijena"] == 50


def test_tri_dana():
    r = klijent.post("/cijena", json={"dani": 3, "godine": 20})
    assert r.json()["ukupna_cijena"] == 60


def test_bez_depozita():
    r = klijent.post("/cijena", json={"dani": 5, "godine": 20})
    assert r.json()["depozit"] == 0


def test_sa_depozitom():
    r = klijent.post("/cijena", json={"dani": 6, "godine": 20})
    assert r.json()["ukupna_cijena"] == 120
    assert r.json()["depozit"] == 60
    assert r.json()["placanje_pri_preuzimanju"] == 60


def test_maloljetna_osoba():
    r = klijent.post("/cijena", json={"dani": 2, "godine": 17})
    assert r.status_code == 422


def test_nula_dana():
    r = klijent.post("/cijena", json={"dani": 0, "godine": 20})
    assert r.status_code == 422


def test_preko_maksimuma():
    r = klijent.post("/cijena", json={"dani": 31, "godine": 20})
    assert r.status_code == 422


def test_preuzimanje():
    r = klijent.post("/preuzimanje", json={"ugovor": True, "placeno": True})
    assert r.status_code == 200


def test_bez_ugovora():
    r = klijent.post("/preuzimanje", json={"ugovor": False, "placeno": True})
    assert r.status_code == 400


def test_bez_placanja():
    r = klijent.post("/preuzimanje", json={"ugovor": True, "placeno": False})
    assert r.status_code == 400


def test_nekompletna_oprema():
    r = klijent.post("/vracanje", json={
        "kompletna_oprema": False,
        "procijenjena_steta": 0
    })
    assert r.status_code == 400


def test_naknada_stete():
    r = klijent.post("/vracanje", json={
        "kompletna_oprema": True,
        "procijenjena_steta": 50
    })
    assert r.status_code == 200
    assert r.json()["naknada_stete"] == 50


def test_negativna_steta():
    r = klijent.post("/vracanje", json={
        "kompletna_oprema": True,
        "procijenjena_steta": -10
    })
    assert r.status_code == 422
