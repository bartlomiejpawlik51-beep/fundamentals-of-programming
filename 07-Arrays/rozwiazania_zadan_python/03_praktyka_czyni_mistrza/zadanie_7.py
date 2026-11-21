# 4, Zadanie 7 - Praktyka czyni mistrza
# Polecenie: Napisz program, który oblicza średnią arytmetyczną elementów listy za pomocą pętli for.
# Obliczanie średniej za pomocą pętli for

arr = [15, 8, 31, 47, 2, 19]
total = 0

for value in arr:
    total = total + value

average = total / len(arr)

print("Array:", arr)
print("Average:", average)
