# 4, Zadanie 36 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję identity_matrix(n), która tworzy macierz jednostkową, oraz funkcję wyświetlającą macierz.
# Tworzenie macierzy jednostkowej i wyświetlanie jej

def identity_matrix(n):
    """Tworzy i zwraca macierz jednostkową o podanym rozmiarze."""
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    """Wyświetla macierz wierszami i kolumnami."""
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


print("Macierz 3:")
print_matrix(identity_matrix(3))

print("Macierz 5:")
print_matrix(identity_matrix(5))

print("Macierz 8:")
print_matrix(identity_matrix(8))
