# 4, Zadanie 3
# Polecenie: Zdefiniuj funkcję obliczającą pole trójkąta ze wzoru Herona.
# Pobierz trzy boki od użytkownika i sprawdź również trzy podane przykłady.

import math

def triangle_area(a, b, c):
    """Oblicza pole trójkąta ze wzoru Herona na podstawie długości trzech boków."""
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))
print("Pole trójkąta:", triangle_area(a, b, c))

print("Pole trójkąta 3, 4, 5:", triangle_area(3, 4, 5))
print("Pole trójkąta 5, 12, 13:", triangle_area(5, 12, 13))
print("Pole trójkąta 7, 24, 25:", triangle_area(7, 24, 25))
