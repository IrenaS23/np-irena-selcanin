# Mini projekat 3 – Rent Canon API

## Opis projekta

Kao temu projekta odabrala sam iznajmljivanje fotoaparata,
inspirisana sopstvenim malim biznisom Rent Canon.
Kreirala sam API za automatizaciju obračuna cijena,
depozita, preuzimanja i vraćanja opreme.

## Funkcionalnosti

- GET /cjenovnik – prikaz cijena iznajmljivanja.
- POST /cijena – obračun cijene i depozita.
- POST /preuzimanje – provjera ugovora i plaćanja.
- POST /vracanje – provjera opreme i naknade štete.

## Poslovna pravila

- Iznajmljivanje je dozvoljeno osobama starijim od 18 godina,
  uključujući osobe koje imaju 18 godina.
- Za 1 ili 2 dana cijena je 25 EUR dnevno.
- Za 3 ili više dana cijena je 20 EUR dnevno.
- Za više od 5 dana depozit iznosi 50% ukupne cijene.
- Depozit služi za osiguranje rezervacije.
- Ostatak cijene plaća se prilikom preuzimanja.
- Potpisivanje ugovora je obavezno.
- Oprema se mora vratiti u kompletnom stanju.
- Oštećenja se naplaćuju prema procijenjenoj šteti.

## Testiranje i kvalitet koda

Napisano je 15 pytest testova koji obuhvataju ispravne
i neispravne unose, granične slučajeve i poslovna pravila.

Rezultati:

- Pytest: 15 uspješnih testova.
- Ruff: nema grešaka.
- Mypy: nema problema sa tipovima.
- Bandit: nijesu pronađeni bezbjednosni propusti.
- Pip-audit: nakon ažuriranja nijesu pronađene poznate
  ranjivosti u direktnim zavisnostima.

## Bezbjednosni rizici i mjere smanjenja

1. Neispravni korisnički unosi

   Korišćena je Pydantic validacija za provjeru broja dana,
   godina korisnika i iznosa procijenjene štete.

2. Ranjive biblioteke

   Pomoću pip-audita pronađena je ranjivost PYSEC-2026-1845
   u biblioteci pytest 8.4.2. Biblioteka je ažurirana na
   verziju 9.0.3. Ponovna provjera direktnih zavisnosti
   nije pokazala poznate ranjivosti.

3. Neovlašćeni pristup

   API trenutno nema autentikaciju korisnika.
   U stvarnoj primjeni potrebno je uvesti autentikaciju
   i ograničiti pristup zaposlenima.

4. Izlaganje osjetljivih podataka

   API ne čuva lične podatke, lozinke ni podatke
   platnih kartica.

## Kontinuirana integracija

Kreiran je GitHub Actions workflow koji automatski
pokreće ruff, mypy i pytest pri izmjenama koda.

## Pokretanje projekta

pip install -r requirements.txt

uvicorn main:app --reload

## Pokretanje testova

pytest -v

## Zaključak

Kroz ovaj projekat primijenila sam znanje sa predavanja
na primjeru sopstvenog poslovanja. Poseban fokus bio je
na testiranju, kvalitetu i bezbjednosti koda.

API predstavlja jednostavan prototip i ne vrši stvarne
novčane transakcije niti provjerava identitet korisnika.
