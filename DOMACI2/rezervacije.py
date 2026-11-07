class Rezervacija:
    def __init__(self, gost: str, noci: int, cijena_noci: float):
        self.gost = gost
        self.noci = noci
        self.cijena_noci = cijena_noci

    def izracunaj_iznos(self) -> float:
        return self.noci * self.cijena_noci
