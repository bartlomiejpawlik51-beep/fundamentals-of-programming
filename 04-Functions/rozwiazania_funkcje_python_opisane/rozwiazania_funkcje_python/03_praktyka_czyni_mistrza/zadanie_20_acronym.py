# 4, Zadanie 20
# Polecenie: Utwórz akronim z pierwszych liter wszystkich słów w tekście.

def f(name):
    """Zwraca akronim złożony z pierwszych liter słów podanego tekstu."""
    words = name.split()
    result = ""

    for word in words:
        result = result + word[0].upper()

    return result

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))
