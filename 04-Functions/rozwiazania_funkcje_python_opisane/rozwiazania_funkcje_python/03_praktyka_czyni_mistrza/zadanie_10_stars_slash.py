# 4, Zadanie 10
# Polecenie: Zwróć ciąg n gwiazdek oddzielonych ukośnikami.

def f(n):
    """Zwraca n gwiazdek oddzielonych znakiem ukośnika."""
    result = ""

    for i in range(n):
        if i > 0:
            result = result + "/"
        result = result + "*"

    return result

print(f(4))
print(f(1))
