# 4, Zadanie 35 - Praktyka czyni mistrza
# Polecenie: Napisz program, który zamienia pierwszą i ostatnią kolumnę macierzy.
# Zamiana pierwszej i ostatniej kolumny macierzy

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Przed zmianą:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    temp = matrix[i][0]
    matrix[i][0] = matrix[i][len(matrix[i]) - 1]
    matrix[i][len(matrix[i]) - 1] = temp

print("Po zmianie:")
for row in matrix:
    print(row)
