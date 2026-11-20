import pytest
from projekat import *

def test_kreiranje_modela():
    model = kreiraj_model("stablo")
    assert isinstance(model, DecisionTreeClassifier)


def test_nepoznat_model():
    with pytest.raises(ValueError):
        kreiraj_model("nepoznat")


def test_tacnost():
    y_tacno = [0, 1, 2, 0]
    y_pred = [0, 1, 1, 0]

    rezultat = izracunaj_metriku("accuracy", y_tacno, y_pred)
    assert rezultat == 0.75


def test_observer():
    trening = Treniranje()
    pratilac = PracenjeTreninga()

    trening.dodaj_pratioca(pratilac)

    assert len(trening.pratioci) == 1


def test_eksperiment():
    eksperiment = Eksperiment()
    rezultat = eksperiment.pokreni()

    assert 0 <= rezultat <= 1


def test_dekorator():
    @mjeri_vrijeme
    def saberi(a, b):
        return a + b

    rezultat = saberi(2, 3)
    assert rezultat == 5


