from izvjestaj import CuvanjeIzvjestaja
from obrada import ObradaRezervacija
from podaci import UcitavanjeRezervacija

izvor = UcitavanjeRezervacija("rezervacije.csv")
izvjestaj = CuvanjeIzvjestaja("izvjestaj.txt")

program = ObradaRezervacija(izvor, izvjestaj)

print(program.obradi())
