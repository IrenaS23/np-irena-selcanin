class CuvanjeIzvjestaja:
    def __init__(self, fajl: str):
        self.fajl = fajl

    def sacuvaj(self, iznosi: list[float]) -> None:
        with open(self.fajl, "w", encoding="utf-8") as f:
            f.writelines(f"{iznos}\n" for iznos in iznosi)
