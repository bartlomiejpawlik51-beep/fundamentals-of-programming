# 4, Zadanie 23
# Polecenie: Oblicz sumę liczb z zakresu, które są podzielne przez 2 i 3, ale nie przez 4.

def f(x, y):
    """Sumuje liczby z zakresu x-y podzielne przez 2 i 3, ale niepodzielne przez 4."""
    total = 0

    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total = total + number

    return total

print(f(1, 20))
print(f(10, 30))
