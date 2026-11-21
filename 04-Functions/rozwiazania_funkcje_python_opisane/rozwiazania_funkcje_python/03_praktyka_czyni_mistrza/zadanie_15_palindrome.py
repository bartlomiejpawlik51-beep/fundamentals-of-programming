# 4, Zadanie 15
# Polecenie: Sprawdź, czy podany tekst jest palindromem.

def f(palindrome):
    """Zwraca True, jeśli tekst czytany od tyłu jest taki sam jak od przodu."""
    return palindrome == palindrome[::-1]

print(f("radar"))
print(f("12-11-21"))
print(f("book"))
