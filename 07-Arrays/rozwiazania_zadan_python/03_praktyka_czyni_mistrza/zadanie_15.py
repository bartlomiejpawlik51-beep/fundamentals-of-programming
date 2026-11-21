# 4, Zadanie 15 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję occur(), która sprawdza, czy podana liczba znajduje się na liście. Liczbę pobierz od użytkownika.
# Sprawdzanie, czy liczba znajduje się na liście

def occur(liczba, tablica):
    """Sprawdza, czy podana liczba występuje w liście."""
    for value in tablica:
        if value == liczba:
            return True
    return False

arr = [15, 38, 7, 23, 14]
number = int(input("Number: "))

print("Array:", *arr)

if occur(number, arr):
    print("Result: number", number, "appears in the array")
else:
    print("Result: number", number, "does not appear in the array")
