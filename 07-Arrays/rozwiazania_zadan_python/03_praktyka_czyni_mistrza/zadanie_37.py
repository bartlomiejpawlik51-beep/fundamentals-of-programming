# 4, Zadanie 37 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję transpose_matrix(), która zwraca macierz transponowaną, i przetestuj ją na podanych macierzach.
# Transponowanie macierzy

def transpose_matrix(m):
    """Zwraca macierz, w której wiersze i kolumny zostały zamienione miejscami."""
    result = []

    for col in range(len(m[0])):
        new_row = []
        for row in range(len(m)):
            new_row.append(m[row][col])
        result.append(new_row)

    return result


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for matrix in matrices:
    print("Macierz transponowana:")
    result = transpose_matrix(matrix)
    for row in result:
        print(row)
    print()
