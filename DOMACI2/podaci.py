
import csv


class UcitavanjeRezervacija:
    def __init__(self, fajl: str):
        self.fajl = fajl

    def ucitaj(self) -> list:
        with open(self.fajl, encoding="utf-8") as f:
            return list(csv.DictReader(f))
