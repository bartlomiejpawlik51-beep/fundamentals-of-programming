# 4, Zadanie 27
# Polecenie: Zastosuj rekurencję do obliczenia silni liczby 5.

def factorial(n):
    """Zwraca silnię liczby n, wywołując funkcję ponownie dla n-1."""
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n - 1)
    return None

print("5! =", factorial(5))
