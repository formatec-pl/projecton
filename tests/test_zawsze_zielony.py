# v0.1.0_20261104_2000_tests_test_zawsze_zielony.py
"""Testy szkieletu PJ001 — zawsze zielone (brak logiki technologicznej)."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

# Wzorce: password|token|api_key|secret z przypisaną wartością (nie sama nazwa pola).
_WZORZEC_SEKRETU = re.compile(
    r"(?i)\b(password|token|api_key|secret)\b\s*[=:]\s*(['\"]?)([^\s'\"]+)\2"
)


def test_zawsze_prawda() -> None:
    """(a) Minimalny test środowiskowy."""
    assert True


def test_import_backend_geometria_i_reguly() -> None:
    """(b) Pakiety backend.geometria i backend.reguly są importowalne."""
    import backend.geometria  # noqa: F401
    import backend.reguly  # noqa: F401


def test_brak_sekretow_w_sledzonych_plikach() -> None:
    """(c) Prosty skan git ls-files — brak przypisanych wartości sekretów."""
    wynik = subprocess.run(
        ["git", "ls-files"],
        capture_output=True,
        text=True,
        check=True,
        cwd=Path(__file__).resolve().parents[1],
    )
    pliki = [p for p in wynik.stdout.splitlines() if p.strip()]
    naruszenia: list[str] = []
    for rel in pliki:
        sciezka = Path(__file__).resolve().parents[1] / rel
        if not sciezka.is_file():
            continue
        try:
            tekst = sciezka.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for nr, linia in enumerate(tekst.splitlines(), start=1):
            m = _WZORZEC_SEKRETU.search(linia)
            if m:
                naruszenia.append(f"{rel}:{nr}")
    assert not naruszenia, f"Podejrzenie sekretów: {naruszenia}"


# =============================================================================
# AUTOR: Mariusz Adamczyk
# WSZELKIE PRAWA ZASTRZEŻONE (C) 2026
# Niniejszy program i kod źródłowy stanowią wyłączną własność autora.
# Wprowadza się całkowity i bezwzględny zakaz udostępniania, rozpowszechniania
# lub kopiowania programu osobom trzecim bez wyraźnej, pisemnej zgody autora.
# Zastrzeżenie odpowiedzialności: Autor nie ponosi żadnej odpowiedzialności
# za skutki wykorzystywania programu przez podmioty trzecie, w tym za ewentualne
# szkody materialne, uszkodzenia sprzętu lub błędy produkcyjne maszyn CNC.
# =============================================================================
