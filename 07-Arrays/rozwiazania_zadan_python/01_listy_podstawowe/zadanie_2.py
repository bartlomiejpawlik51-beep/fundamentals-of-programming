# 4, Zadanie 2
# Polecenie: Napisz program, który kolejno modyfikuje trzy elementy listy i pokazuje wynik po każdej zmianie.
# Modyfikowanie elementów listy

arr = [1, 2, 3, 4, 5]
print("Array:", arr)

arr[0] = arr[0] - 1
print("Array:", arr)

arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print("Array:", arr)

arr[2] = arr[2] * 2
print("Array:", arr)
