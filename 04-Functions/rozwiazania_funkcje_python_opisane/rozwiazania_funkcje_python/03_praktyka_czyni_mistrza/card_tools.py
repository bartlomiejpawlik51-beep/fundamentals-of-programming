# 4, Zadanie 4 - Moduł card_tools
# Polecenie: Zdefiniuj funkcję hide(), która ukrywa środkowe cyfry 16-cyfrowego numeru karty.

def hide(card_number):
    """Zwraca numer karty z widocznymi dwiema pierwszymi i czterema ostatnimi cyframi."""
    if len(card_number) != 16 or not card_number.isdigit():
        return "Nieprawidłowy numer karty"

    return card_number[:2] + "*" * 10 + card_number[-4:]
