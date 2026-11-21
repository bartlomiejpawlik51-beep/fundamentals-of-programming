# 4, Zadanie 6 - Praktyka czyni mistrza
# Polecenie: Napisz program, który znajduje najmniejszą i największą liczbę bez używania funkcji min() i max().
# Znajdowanie minimum i maksimum bez funkcji min() i max()

arr = [-15, 8, -31, 47, -2, 19]

minimum = arr[0]
maximum = arr[0]

for value in arr:
    if value < minimum:
        minimum = value
    if value > maximum:
        maximum = value

print("Minimum:", minimum)
print("Maximum:", maximum)
