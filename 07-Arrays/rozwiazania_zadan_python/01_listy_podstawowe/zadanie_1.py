# 4, Zadanie 1
# Polecenie: Napisz program, który wyświetla listę, jej długość oraz wskazane elementy i sumę.
# Wyświetlanie wybranych elementów listy

arr = [2, 3, 7, 5, 4]

print("Tablica:", arr)
print("Liczba elementów:", len(arr))
print("Pierwsza wartość:", arr[0])
print("Druga wartość:", arr[1])
print("Ostatnia wartość:", arr[len(arr) - 1])
print("Przedostatnia wartość:", arr[len(arr) - 2])
print("Suma pierwszej i ostatniej wartości:", arr[0] + arr[len(arr) - 1])
print("Wartość środkowa:", arr[len(arr) // 2])

print("Wszystkie wartości:", end=" ")
for element in arr:
    print(element, end=" ")
print()
