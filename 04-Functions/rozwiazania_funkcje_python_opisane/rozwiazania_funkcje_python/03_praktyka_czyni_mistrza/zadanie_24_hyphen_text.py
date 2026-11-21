# 4, Zadanie 24
# Polecenie: Zwróć tekst, w którym każdy znak jest oddzielony myślnikiem.

def f(text):
    """Łączy znaki tekstu, wstawiając między nimi myślniki."""
    return "-".join(text)

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))
