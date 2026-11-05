<!-- v0.1.1_20261106_0040_backend_geometria_README.md -->
# backend/geometria

Jedno źródło matematyki PROJECTON (§I.3): współrzędne, przeliczenia, konwencje z `docs/UKLAD_WSPOLRZEDNYCH.md`.

**Tu będzie:** API geometrii formatki (mm, tolerancja 0,1 / 0,05).

`mm(wartosc)` — zaokrągla wymiar do 0,1 mm (ROUND_HALF_UP; int/float/tekst z `.` lub `,`).
`rowne(a, b, tolerancja=0.05)` — porównanie z tolerancją (domyślnie 0,05 mm; zapas 1e-9).

**Nie wolno:** reguł otworów, generatora MPR, sekretów, logiki w przeglądarce.
