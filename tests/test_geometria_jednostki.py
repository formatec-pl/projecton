# v0.1.1_20261106_0040_tests_test_geometria_jednostki.py
"""Testy mm() i rowne() — MA001 (§XIII: 0,1 mm, tolerancja 0,05 mm)."""

from __future__ import annotations

import pytest

from backend.geometria import mm, rowne


def test_mm_zaokragla_do_jednej_dziesiatej() -> None:
    assert mm(362.07) == 362.1
    assert mm(361.93) == 361.9
    assert mm("362,05") == 362.1
    assert mm(-0.05) == -0.1
    assert mm(600) == 600.0
    assert mm(0.04) == 0.0


def test_mm_bledne_wartosci() -> None:
    with pytest.raises(ValueError):
        mm("abc")
    with pytest.raises(ValueError):
        mm(None)


def test_rowne_tolerancja() -> None:
    assert rowne(362.07, 362.1) is True
    assert rowne(362.0, 362.06) is False
    with pytest.raises(ValueError):
        rowne(1, 1, -1)


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
