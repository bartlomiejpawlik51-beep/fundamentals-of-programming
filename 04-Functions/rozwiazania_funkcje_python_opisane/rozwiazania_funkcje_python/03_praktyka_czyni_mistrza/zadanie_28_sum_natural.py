# 4, Zadanie 28
# Polecenie: Zdefiniuj rekurencyjną funkcję obliczającą sumę liczb od 1 do n.

def sum_natural(n):
    """Zwraca sumę liczb naturalnych od 1 do n za pomocą rekurencji."""
    if n <= 0:
        return 0
    return n + sum_natural(n - 1)

print("Suma liczb od 1 do 10:", sum_natural(10))
