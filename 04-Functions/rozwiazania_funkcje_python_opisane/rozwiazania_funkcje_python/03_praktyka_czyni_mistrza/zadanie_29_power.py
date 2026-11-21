# 4, Zadanie 29
# Polecenie: Zdefiniuj rekurencyjną funkcję power(x, n), która oblicza x do potęgi n.

def power(x, n):
    """Oblicza x do potęgi n za pomocą rekurencji dla nieujemnego n."""
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("5 do potęgi 3:", power(5, 3))
