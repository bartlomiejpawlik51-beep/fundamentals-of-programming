# 4, Zadanie 5
# Polecenie: Zdefiniuj funkcję f(), która sprawdza, czy tekst zawiera wyłącznie cyfry 0 i 1.

def f(binary_number):
    """Zwraca True, jeśli tekst jest niepustą liczbą binarną."""
    if binary_number == "":
        return False

    for digit in binary_number:
        if digit != "0" and digit != "1":
            return False

    return True

print(f("101101"))
print(f("1311a10100"))
