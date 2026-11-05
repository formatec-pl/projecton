# v0.1.1_20261106_0040_backend_geometria_jednostki.py
"""Jednostki i porównania wymiarów: mm (0,1) oraz rowne (tolerancja 0,05)."""

from __future__ import annotations

import math
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Union

LiczbaLubTekst = Union[int, float, str]


def mm(wartosc: LiczbaLubTekst | None) -> float:
    """Zaokrągla wartość do 0,1 mm (ROUND_HALF_UP). Przyjmuje int/float/tekst."""
    if wartosc is None:
        raise ValueError("Wartość mm nie może być None.")
    if isinstance(wartosc, bool):
        raise ValueError("Wartość mm ma nieprawidłowy typ.")
    if isinstance(wartosc, float) and math.isnan(wartosc):
        raise ValueError("Wartość mm nie może być nan.")
    if isinstance(wartosc, str):
        tekst = wartosc.strip().replace(",", ".")
        if not tekst:
            raise ValueError("Wartość mm ma nieprawidłowy tekst.")
        try:
            d = Decimal(tekst)
        except InvalidOperation as exc:
            raise ValueError("Wartość mm ma nieprawidłowy tekst.") from exc
    elif isinstance(wartosc, int):
        d = Decimal(wartosc)
    elif isinstance(wartosc, float):
        d = Decimal(str(wartosc))
    else:
        raise ValueError("Wartość mm ma nieprawidłowy typ.")
    if not d.is_finite():
        raise ValueError("Wartość mm musi być skończoną liczbą.")
    zaokr = d.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return float(zaokr)


def rowne(a: float, b: float, tolerancja: float = 0.05) -> bool:
    """True, gdy abs(a - b) <= tolerancja (zapas zmiennoprzecinkowy 1e-9)."""
    if tolerancja < 0:
        raise ValueError("Tolerancja nie może być ujemna.")
    return abs(float(a) - float(b)) <= float(tolerancja) + 1e-9


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
