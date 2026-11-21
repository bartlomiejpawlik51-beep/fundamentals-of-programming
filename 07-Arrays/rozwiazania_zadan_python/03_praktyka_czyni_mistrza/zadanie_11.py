# 4, Zadanie 11 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję compare(), która sprawdza, czy dwie listy mają taką samą długość i takie same elementy.
# Porównywanie dwóch list

def compare(tablica1, tablica2):
    """Porównuje dwie listy i zwraca True, jeśli są identyczne."""
    if len(tablica1) != len(tablica2):
        return False

    for i in range(len(tablica1)):
        if tablica1[i] != tablica2[i]:
            return False

    return True

pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for first, second in pairs:
    print("Array1:", first)
    print("Array2:", second)

    if compare(first, second):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")
    print()
