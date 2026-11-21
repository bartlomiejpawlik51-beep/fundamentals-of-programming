# 4, Zadanie 12
# Polecenie: Napisz funkcję sortującą listę liczb algorytmem bąbelkowym i użyj jej do posortowania dwóch list.
# Sortowanie bąbelkowe dwóch list

def bubble_sort(arr):
    """Sortuje listę rosnąco metodą bąbelkową i zwraca posortowaną listę."""
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print("Zużycie paliwa przed sortowaniem:", car_fuel_consumption)
print("Zużycie paliwa po sortowaniu:", bubble_sort(car_fuel_consumption))

print("Transakcje przed sortowaniem:", bank_transactions)
print("Transakcje po sortowaniu:", bubble_sort(bank_transactions))
