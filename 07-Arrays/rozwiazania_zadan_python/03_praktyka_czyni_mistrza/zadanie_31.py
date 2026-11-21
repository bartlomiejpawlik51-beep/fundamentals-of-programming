# 4, Zadanie 31 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję create_2d_arr(x, y), która tworzy macierz o podanych wymiarach wypełnioną zerami.
# Tworzenie tablicy 2D wypełnionej zerami

def create_2d_arr(x, y):
    """Tworzy i zwraca macierz o podanej liczbie wierszy i kolumn, wypełnioną zerami."""
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

matrix = create_2d_arr(3, 5)

for row in matrix:
    print(row)
