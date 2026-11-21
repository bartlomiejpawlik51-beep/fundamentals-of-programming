# 4, Zadanie 13
# Polecenie: Sprawdź, czy w pokoju przebywały jednocześnie co najmniej trzy osoby.
# Znak + oznacza wejście, a znak - oznacza wyjście.

def f(detector):
    """Zwraca True, jeśli w którymś momencie w pokoju były co najmniej trzy osoby."""
    people = 0

    for sign in detector:
        if sign == "+":
            people = people + 1
        elif sign == "-":
            people = people - 1

        if people >= 3:
            return True

    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
