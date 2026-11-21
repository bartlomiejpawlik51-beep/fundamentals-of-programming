# 4, Zadanie 3 - Praktyka czyni mistrza
# Polecenie: Napisz program, który za pomocą pętli while zlicza parzyste liczby na liście.
# Liczenie liczb parzystych za pomocą while

arr = [34, 7, 19, 4, 21, 8]
even_count = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        even_count = even_count + 1
    i = i + 1

print("Liczba parzystych elementów:", even_count)
