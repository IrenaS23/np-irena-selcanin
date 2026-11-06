import csv


def prosjecna_cijena(fajl: str) -> float:
    ukupno = 0.0
    noci = 0

    with open(fajl, encoding="utf-8") as f:
        for red in csv.DictReader(f):
            n = int(red["noci"])
            cijena = float(red["cijena_noci"])

            ukupno = ukupno + n * cijena
            noci = noci + n

    if noci == 0:
        raise ValueError("Nema ostvarenih nocenja")

    return ukupno / noci


if __name__ == "__main__":
    print(prosjecna_cijena("rezervacije.csv"))
