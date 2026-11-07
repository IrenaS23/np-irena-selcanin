# Napredno programiranje – Domaći 2

## Opis zadatka
U ovom zadatku radila sam refaktoring programa za obradu rezervacija, koristeći objektno orijentisano programiranje i SOLID principe.
Kao osnovu koristila sam primjer obrade rezervacija iz prezentacije, kao i prethodni zadatak u kojem smo radili sa CSV fajlovima.
Cilj mi je bio da kod podijelim na više jednostavnijih djelova, umjesto da se učitavanje podataka, računanje iznosa i čuvanje rezultata obavljaju na jednom mjestu.
Program učitava rezervacije iz CSV fajla, računa iznos za svakog gosta i čuva rezultate u fajlu izvjestaj.txt.

## Organizacija koda
Program sam podijelila u nekoliko fajlova, tako da svaki ima svoju ulogu:

rezervacije.py – sadrži klasu koja računa iznos jedne rezervacije.
podaci.py – učitava podatke iz CSV fajla.
interfejsi.py – sadrži dva Protocol interfejsa, za učitavanje podataka i izvještavanje.
izvjestaj.py – čuva izračunate iznose u tekstualnom fajlu.
obrada.py – povezuje učitavanje, računanje i čuvanje rezultata.
main.py – služi za pokretanje programa.
test_obrada.py – sadrži testove programa.

## SOLID principi
U zadatku sam primijenila dva SOLID principa: S i D.

S – Single Responsibility
Podijelila sam program tako da svaka klasa ima svoj zadatak. Jedna učitava podatke, druga računa iznos rezervacije, a treća čuva izvještaj. Tako je kod pregledniji i lakši za izmjene.

D – Dependency Inversion
Koristila sam Protocol za izvor podataka i izvještavanje. Na taj način klasa za obradu ne mora da zna da li podaci dolaze iz CSV fajla ili nekog drugog izvora.

Ovo sam provjerila i kroz testove, gdje sam umjesto pravog CSV fajla koristila zamjenski izvor podataka.

## Korišćenje AI alata
Tokom izrade zadatka koristila sam ChatGPT kao pomoć pri pisanju, organizaciji i razumijevanju koda.
Neki od upita koje sam koristila bili su:

„Objasni prince S i D?“
„Može li jednostavnije?“

AI mi je pomogao da kod pojednostavim i da napravim testove. Nakon toga sam program pokrenula i provjerila rezultate.

## Šta sam primijetila i ispravila
Prilikom provjere koda pomoću Ruff-a pojavilo se nekoliko problema. Većinu sam ispravila automatski, a dio za učitavanje CSV fajla sam pojednostavila.
Umjesto pravljenja prazne liste i dodavanja svakog reda posebno, koristila sam list(csv.DictReader(f)), jer na taj način dobijam isti rezultat sa manje koda.
Nakon izmjena ponovo sam provjerila program i Ruff više nije prijavljivao greške.

## Testiranje
Napravila sam tri testa pomoću pytest-a sa zamjenskim izvorom podataka.
Testirala sam:

Da li program pravilno računa iznose rezervacija.

Da li se izračunati iznosi prosljeđuju izvještaju.

Kako se program ponaša kada nema rezervacija.

Sva tri testa su uspješno prošla, uz jedno upozorenje koje nije uticalo na rezultate testiranja.

## Pokretanje programa

Program se pokreće iz foldera DOMACI2 komandom:

python main.py

Za pokretanje testova koristila sam:

python -m pytest -q

Za provjeru koda:

python -m ruff check .

## Zakljucak
Kroz ovaj zadatak sam bolje razumjela kako se program može podijeliti na više klasa i zašto je takva organizacija korisna.
 U početku mi neki djelovi, posebno Protocol, nisu bili baš najjasniji, ali sam kroz praktičan rad i testiranje bolje
shvatila njihovu ulogu.