# 4, Zadanie 16
# Polecenie: Napisz funkcję, która usuwa wszystkie spacje ze zdania.

def f(sentence):
    """Zwraca tekst bez spacji."""
    return sentence.replace(" ", "")

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))
