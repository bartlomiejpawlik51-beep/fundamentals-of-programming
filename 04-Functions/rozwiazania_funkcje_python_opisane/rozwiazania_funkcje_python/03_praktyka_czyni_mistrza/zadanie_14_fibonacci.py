# 4, Zadanie 14
# Polecenie: Zdefiniuj funkcję zwracającą n-tą wartość ciągu Fibonacciego.
# Pierwszy element ma indeks 1 i wartość 0, drugi ma wartość 1.

def f(n):
    """Zwraca n-tą wartość ciągu Fibonacciego, licząc od f(1) = 0."""
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    first = 0
    second = 1

    for i in range(3, n + 1):
        next_number = first + second
        first = second
        second = next_number

    return second

print(f(5))
print(f(9))
