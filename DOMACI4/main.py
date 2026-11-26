
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Rent Canon API")


class Rezervacija(BaseModel):
    dani: int = Field(ge=1, le=30, strict=True)
    godine: int = Field(ge=18, strict=True)


class Preuzimanje(BaseModel):
    ugovor: bool
    placeno: bool


class Vracanje(BaseModel):
    kompletna_oprema: bool
    procijenjena_steta: float = Field(ge=0)


@app.get("/cjenovnik")
def cjenovnik() -> dict[str, int]:
    return {"standardna_cijena": 25, "cijena_3_plus": 20}


@app.post("/cijena")
def izracunaj(r: Rezervacija) -> dict[str, float]:
    if r.dani >= 3:
        cijena = r.dani * 20
    else:
        cijena = r.dani * 25

    if r.dani > 5:
        depozit = cijena * 0.5
    else:
        depozit = 0.0

    return {
        "ukupna_cijena": cijena,
        "depozit": depozit,
        "placanje_pri_preuzimanju": cijena - depozit
    }


@app.post("/preuzimanje")
def preuzimanje(p: Preuzimanje) -> dict[str, str]:
    if not p.ugovor:
        raise HTTPException(400, "Ugovor nije potpisan")

    if not p.placeno:
        raise HTTPException(400, "Placanje nije izvrseno")

    return {"status": "Preuzimanje odobreno"}


@app.post("/vracanje")
def vracanje(v: Vracanje) -> dict[str, str | float]:
    if not v.kompletna_oprema:
        raise HTTPException(400, "Oprema nije kompletna")

    return {
        "status": "Oprema vracena",
        "naknada_stete": v.procijenjena_steta
    }
