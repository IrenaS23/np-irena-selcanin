import time
from functools import wraps

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score


iris = load_iris()


# Factory
def kreiraj_model(naziv):
    modeli = {
        "linearni": LogisticRegression(max_iter=200),
        "stablo": DecisionTreeClassifier(random_state=42),
        "knn": KNeighborsClassifier()
    }

    if naziv not in modeli:
        raise ValueError("Nepoznat model")

    return modeli[naziv]


# Strategy
def tacnost(y_tacno, y_pred):
    return accuracy_score(y_tacno, y_pred)


def f1_metrika(y_tacno, y_pred):
    return f1_score(y_tacno, y_pred, average="macro")


metrike = {
    "accuracy": tacnost,
    "f1": f1_metrika
}


def izracunaj_metriku(naziv, y_tacno, y_pred):
    return metrike[naziv](y_tacno, y_pred)


# Observer
class PracenjeTreninga:
    def kraj_treninga(self, naziv_modela):
        print("Zavrseno treniranje modela:", naziv_modela)


class Treniranje:
    def __init__(self):
        self.pratioci = []

    def dodaj_pratioca(self, pratilac):
        self.pratioci.append(pratilac)

    def treniraj(self, model, x, y):
        model.fit(x, y)

        for pratilac in self.pratioci:
            pratilac.kraj_treninga(type(model).__name__)

        return model


# Template Method
class Eksperiment:
    def pokreni(self):
        x_trening, x_test, y_trening, y_test = train_test_split(
            iris.data, iris.target,
            test_size=0.2,
            random_state=42,
            stratify=iris.target
        )

        model = self.napravi_model()

        trening = Treniranje()
        trening.dodaj_pratioca(PracenjeTreninga())
        trening.treniraj(model, x_trening, y_trening)

        predvidjanja = model.predict(x_test)
        rezultat = izracunaj_metriku("accuracy", y_test, predvidjanja)

        return rezultat

    def napravi_model(self):
        return kreiraj_model("stablo")


class KNNEksperiment(Eksperiment):
    def napravi_model(self):
        return kreiraj_model("knn")


# Decorator
def mjeri_vrijeme(funkcija):
    @wraps(funkcija)
    def nova_funkcija(*args, **kwargs):
        pocetak = time.time()
        rezultat = funkcija(*args, **kwargs)
        kraj = time.time()

        print("Vrijeme izvrsavanja:", round(kraj - pocetak, 4), "sekundi")
        return rezultat

    return nova_funkcija


class EksperimentSaVremenom(Eksperiment):
    @mjeri_vrijeme
    def pokreni(self):
        return super().pokreni()
