<!-- v0.1.0_20261104_2304_README.md -->
# PROJECTON

Program do projektowania mebli online (biblioteka szafek, reguły otworów, MPR/XML, konfigurator, planer, kosztorys) — współpraca z FCH / Formatec.

## Zasady

Obowiązująca konstytucja projektu: plik `.cursorrules` w katalogu głównym repozytorium.
Kod technologiczny (reguły otworów, generator MPR, cenniki) działa **tylko na serwerze** — przeglądarka dostaje gotowy wynik (§III, §XVI).

## Testy

```bash
.venv/bin/python -m pytest -q
```

(środowisko `.venv` zakłada właściciel). Skrypt `uruchom_testy.sh` zostaje dla ludzi.
Wymagany Python 3.12. Zależności: wyłącznie `pytest` (na razie).

## Układ

- `backend/geometria/` — jedyne miejsce przeliczeń współrzędnych
- `backend/reguly/` — silnik reguł otworów (etap 2)
- `biblioteka/` — dane szafek, materiałów, okuć
- `config/` — przykłady parametrów (bez tajnych wartości w gicie)
- `docs/` — dokumentacja, m.in. układ współrzędnych
- `tests/` — pytest; `tests/zlote/` — złote pliki zamkniętych etapów
