from typing import Protocol


class IzvorRezervacija(Protocol):
    def ucitaj(self) -> list:
        ...


class Izvjestavanje(Protocol):
    def sacuvaj(self, iznosi: list[float]) -> None:
        ...
