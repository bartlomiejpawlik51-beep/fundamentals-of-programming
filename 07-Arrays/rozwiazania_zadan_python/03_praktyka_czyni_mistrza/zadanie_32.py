# 4, Zadanie 32 - Praktyka czyni mistrza
# Polecenie: Napisz program, który tworzy i wyświetla tablicę mnożenia o wymiarach 5 na 5.
# Tworzenie tablicy mnożenia 5x5

matrix = []

for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    matrix.append(row)

for row in matrix:
    for value in row:
        print(value, end="\t")
    print()
