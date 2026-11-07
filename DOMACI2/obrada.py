from interfejsi import Izvjestavanje, IzvorRezervacija
from rezervacije import Rezervacija


class ObradaRezervacija:
    def __init__(self, izvor: IzvorRezervacija, izvjestaj: Izvjestavanje):
        self.izvor = izvor
        self.izvjestaj = izvjestaj

    def obradi(self) -> list[float]:
        iznosi = []

        for red in self.izvor.ucitaj():
            r = Rezervacija(
                red["gost"],
                int(red["noci"]),
                float(red["cijena_noci"])
            )
            iznosi.append(r.izracunaj_iznos())

        self.izvjestaj.sacuvaj(iznosi)
        return iznosi
