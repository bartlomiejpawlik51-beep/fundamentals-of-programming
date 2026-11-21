# 4, Zadanie 33 - Praktyka czyni mistrza
# Polecenie: Napisz program, który znajduje minimum i maksimum w macierzy oraz podaje ich położenie.
# Znajdowanie minimum, maksimum oraz ich pozycji w macierzy

matrix = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

minimum = matrix[0][0]
maximum = matrix[0][0]
min_row = 0
min_col = 0
max_row = 0
max_col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
            min_row = i
            min_col = j
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            max_row = i
            max_col = j

print("Minimum:", minimum, "wiersz:", min_row + 1, "kolumna:", min_col + 1)
print("Maximum:", maximum, "wiersz:", max_row + 1, "kolumna:", max_col + 1)
