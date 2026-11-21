# 4, Zadanie 34 - Praktyka czyni mistrza
# Polecenie: Napisz program, który zamienia pierwszy i ostatni wiersz macierzy.
# Zamiana pierwszego i ostatniego wiersza macierzy

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Przed zmianą:")
for row in matrix:
    print(row)

temp = matrix[0]
matrix[0] = matrix[len(matrix) - 1]
matrix[len(matrix) - 1] = temp

print("Po zmianie:")
for row in matrix:
    print(row)
