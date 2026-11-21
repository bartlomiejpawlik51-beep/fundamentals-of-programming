# 4, Zadanie 18
# Polecenie: Napisz funkcję, która zwraca n-tą liczbę pierwszą.

def is_prime(number):
    """Sprawdza, czy liczba jest pierwsza."""
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

def f(n):
    """Zwraca n-tą liczbę pierwszą, licząc od 2."""
    counter = 0
    number = 1

    while counter < n:
        number = number + 1
        if is_prime(number):
            counter = counter + 1

    return number

print(f(1))
print(f(5))
