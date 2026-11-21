# 4, Zadanie 21
# Polecenie: Sprawdź, czy hasło ma co najmniej sześć znaków i nie zawiera powtarzających się znaków.

def f(password):
    """Zwraca True, jeśli hasło ma co najmniej sześć różnych znaków."""
    if len(password) < 6:
        return False

    for character in password:
        if password.count(character) > 1:
            return False

    return True

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
