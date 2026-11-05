# Krepšelis

7 dienų mitybos planas pagal žmogaus poreikius (kalorijos, baltymai, mitybos tipas, alergijos), su receptais, gaminimu 2 kartus per savaitę ir pirkinių sąrašu Maximos (Barbora) ir Rimi e. parduotuvių kainomis.

**Programėlė:** https://gedissxd.github.io/krepselis/

## Failai

- `src/app.html`: programėlės šaltinis (HTML, CSS ir JavaScript viename faile).
- `build.py`: iš `src/app.html` sukuria `index.html`, kurį rodo GitHub Pages. Paleiskite `python3 build.py` po kiekvieno pakeitimo.
- `scraper/`: kainų surinkimas iš Barbora ir Rimi e. parduotuvių (`fetch.py` atsisiunčia paieškos puslapius, `pick.py` parenka produktus pagal `rules.py`).

Kainos surinktos 2026-11-05, fizinėse parduotuvėse jos gali skirtis. Tai nėra medicininė konsultacija.
