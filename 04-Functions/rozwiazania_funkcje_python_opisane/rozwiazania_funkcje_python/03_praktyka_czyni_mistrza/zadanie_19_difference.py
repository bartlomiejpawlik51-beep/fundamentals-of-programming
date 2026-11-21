# 4, Zadanie 19
# Polecenie: Zwróć różnicę między największą i najmniejszą z trzech liczb.

def f(number1, number2, number3):
    """Oblicza różnicę między największą i najmniejszą z trzech liczb."""
    biggest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return biggest - smallest

print(f(7, 4, 9))
print(f(2, 12, 8))
