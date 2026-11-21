# 4, Zadanie 10 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję star(n), która zwraca n gwiazdek, a następnie wyświetl wykres tekstowy dla podanych liczb.
# Wyświetlanie liczby gwiazdek

def star(n):
    """Tworzy i zwraca tekst składający się z podanej liczby gwiazdek."""
    result = ""
    for i in range(n):
        result = result + "*"
    return result

numbers = [2, 6, 4, 9, 7]

for number in numbers:
    print(str(number) + ": " + star(number))
