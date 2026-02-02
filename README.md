# OOP Kalkulaator

Lihtne käsurea kalkulaator, mis on loodud **objektorienteeritud programmeerimise (OOP)** põhimõtteid järgides.  
Rakendusel on **põhifunktsioonid** (liitmine, lahutamine, korrutamine, jagamine, astendamine, ruutjuur) ning lisasin ka **kolm lisafunktsiooni** (protsent, absoluutväärtus, keskmine), et vastata hindele **5**.

---

## Eesmärk

Eesmärk oli koostada töökorras, hästi kommenteeritud ja heade tavade järgi vormistatud OOP-kalkulaator, mis vastab eksami kriteeriumitele ning on koodihoidlas (GitHubis).

---

##  Funktsionaalsus

### Põhifunktsioonid
- **Liitmine** – kahe arvu summa.
- **Lahutamine** – kahe arvu vahe.
- **Korrutamine** – kahe arvu korrutis.
- **Jagamine** – kahe arvu jagatis (sisaldab kontrolli nulliga jagamise vastu).
- **Astendamine** – esimene arv teise astmes.
- **Ruutjuur** – ruutjuur ühest arvust (sisaldab kontrolli negatiivse arvu korral).

### Lisafunktsioonid (hinne 5 jaoks)
- **Protsent (%)** – arvutan, mitu protsenti `b` on `a`-st: `(a * b) / 100`.
- **Absoluutväärtus** – tagastan arvu `a` absoluutväärtuse.
- **Keskmine** – kahe arvu aritmeetiline keskmine.

---

##  Mida ma lisasin ja parendasin

- Kirjutasin kalkulaatori **OOP stiilis** klassiga `Calculator`.
- **Parandasin ruutjuure**: algses koodis oli ruutjuur tegelikult astendamine `a ** b`. Minu versioonis on ruutjuur `sqrt(a)` ja kontrollin negatiivseid sisendeid.
- **Lisäsin veakontrolli** nulliga jagamise korral.
- **Lisasin 3 lisafunktsiooni**: protsent, absoluutväärtus, keskmine (sobib hindele 5).
- **Parandasin menüü loogika**: ühe sisendiga operatsioonid (ruutjuur, absoluut) küsivad ühe arvu, teised kaks.
- **Kommenteerisin koodi** ja hoidsin **stiili ühtlasena** (nimetamistava, tühikud, loetavus).
- **Tegin sisendi tüübid ujukomaarvudeks** (`float`), et kalkulaator toetaks ka kümnendmurde.

---

## 🏗️ Projekti struktuur
