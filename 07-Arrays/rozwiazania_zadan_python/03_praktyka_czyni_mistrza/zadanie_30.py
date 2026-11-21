# 4, Zadanie 30 - Praktyka czyni mistrza
# Polecenie: Napisz program, który oblicza sumę elementów znajdujących się w ostatniej kolumnie macierzy.
# Suma elementów w ostatniej kolumnie

arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0

for row in arr:
    total = total + row[len(row) - 1]

print("Suma ostatniej kolumny:", total)
