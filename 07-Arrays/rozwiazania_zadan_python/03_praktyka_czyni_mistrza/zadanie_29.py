# 4, Zadanie 29 - Praktyka czyni mistrza
# Polecenie: Napisz program, który wyświetla elementy tablicy dwuwymiarowej o dwóch wierszach i czterech kolumnach.
# Wyświetlanie tablicy dwuwymiarowej 2 na 4

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for row in arr:
    for value in row:
        print(value, end=" ")
    print()
