# 4, Zadanie 38 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję, która zamienia tablicę dwuwymiarową na jednowymiarową, i przetestuj ją na podanych przykładach.
# Zamiana tablicy 2D na tablicę 1D

def flatten_array(matrix):
    """Łączy elementy macierzy 2D w jedną listę."""
    result = []

    for row in matrix:
        for value in row:
            result.append(value)

    return result


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for matrix in arrays:
    print("Tablica 1D:", flatten_array(matrix))
