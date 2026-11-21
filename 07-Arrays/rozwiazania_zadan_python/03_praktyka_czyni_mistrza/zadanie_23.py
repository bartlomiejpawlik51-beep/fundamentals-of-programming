# 4, Zadanie 23 - Praktyka czyni mistrza
# Polecenie: Napisz program, który sprawdza, czy wszystkie elementy pierwszej listy znajdują się w drugiej.
# Sprawdzanie, czy pierwsza lista jest podzbiorem drugiej

arr1 = [2, 4, 6]
arr2 = [1, 2, 3, 4, 5, 6, 7]

is_subset = True

for value in arr1:
    if value not in arr2:
        is_subset = False

print("First list:", arr1)
print("Second list:", arr2)
print("Czy pierwsza lista jest podzbiorem drugiej?", is_subset)
