import pytest

from cijene import prosjecna_cijena


def test_prosjecna_cijena():
    rezultat = prosjecna_cijena("rezervacije.csv")
    assert rezultat == pytest.approx(540 / 7)


def test_prazan_fajl(tmp_path):
    fajl = tmp_path / "prazan.csv"
    fajl.write_text("gost,noci,cijena_noci\n")

    with pytest.raises(ValueError):
        prosjecna_cijena(str(fajl))
