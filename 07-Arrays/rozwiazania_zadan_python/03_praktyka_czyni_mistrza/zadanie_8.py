# 4, Zadanie 8 - Praktyka czyni mistrza
# Polecenie: Napisz program, który oblicza średnią arytmetyczną elementów listy za pomocą pętli while.
# Obliczanie średniej za pomocą pętli while

arr = [15, 8, 31, 47, 2, 19]
total = 0
i = 0

while i < len(arr):
    total = total + arr[i]
    i = i + 1

average = total / len(arr)

print("Array:", arr)
print("Average:", average)
