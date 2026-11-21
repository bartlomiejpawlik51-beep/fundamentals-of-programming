# 4, Zadanie 6 - Tablice dwuwymiarowe
# Polecenie: Napisz program, który wpisuje jedynki na głównej przekątnej macierzy 3 na 3 i wyświetla wynik.
# Wstawianie jedynek na głównej przekątnej macierzy

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
