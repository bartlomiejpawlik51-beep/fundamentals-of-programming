# 4, Zadanie 3 - Moduł number_range
# Polecenie: Zdefiniuj funkcję sprawdzającą, czy liczba mieści się w podanym zakresie.

def is_in_range(number, x, y):
    """Zwraca True, jeśli liczba mieści się w przedziale od x do y włącznie."""
    return number >= x and number <= y
