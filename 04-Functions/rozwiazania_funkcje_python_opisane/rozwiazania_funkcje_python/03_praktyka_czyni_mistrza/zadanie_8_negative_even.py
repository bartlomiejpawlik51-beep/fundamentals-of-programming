# 4, Zadanie 8
# Polecenie: Policz ujemne liczby parzyste w zakresie od x do y włącznie.

def f(x, y):
    """Zwraca liczbę ujemnych liczb parzystych w podanym zakresie."""
    counter = 0

    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            counter = counter + 1

    return counter

print(f(-7, 8))
print(f(-1, 11))
