# 4, Zadanie 9
# Polecenie: Zwróć True, jeśli przynajmniej jedna z trzech podanych liczb jest ujemna.

def f(n1, n2, n3):
    """Sprawdza, czy przynajmniej jedna z trzech liczb jest ujemna."""
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    return False

print(f(11, 6, -4))
print(f(5, 4, 14))
