# 4, Zadanie 9 - Moduł converters
# Polecenie: Utwórz funkcje przeliczające centymetry na cale oraz stopy i cale na centymetry.

def centimeters_to_inches(centimeters):
    """Przelicza długość z centymetrów na cale."""
    return centimeters / 2.54

def feet_inches_to_centimeters(feet, inches):
    """Przelicza podaną liczbę stóp i cali na centymetry."""
    total_inches = feet * 12 + inches
    return total_inches * 2.54
