# 4, Zadanie 11
# Polecenie: Zwróć liczby od 1 do n połączone w jeden ciąg znaków.

def f(n):
    """Łączy kolejne liczby od 1 do n w jeden tekst."""
    result = ""

    for number in range(1, n + 1):
        result = result + str(number)

    return result

print(f(11))
print(f(4))
