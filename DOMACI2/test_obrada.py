from obrada import ObradaRezervacija


class TestIzvor:
    def ucitaj(self):
        return [
            {"gost": "Ana", "noci": "2", "cijena_noci": "100"},
            {"gost": "Marko", "noci": "3", "cijena_noci": "50"},
        ]


class TestIzvjestaj:
    def __init__(self):
        self.iznosi = []

    def sacuvaj(self, iznosi):
        self.iznosi = iznosi


def test_iznosi():
    program = ObradaRezervacija(TestIzvor(), TestIzvjestaj())
    assert program.obradi() == [200.0, 150.0]


def test_izvjestaj():
    izvjestaj = TestIzvjestaj()
    program = ObradaRezervacija(TestIzvor(), izvjestaj)

    program.obradi()
    assert izvjestaj.iznosi == [200.0, 150.0]


def test_prazne_rezervacije():
    class PrazanIzvor:
        def ucitaj(self):
            return []

    program = ObradaRezervacija(PrazanIzvor(), TestIzvjestaj())
    assert program.obradi() == []
