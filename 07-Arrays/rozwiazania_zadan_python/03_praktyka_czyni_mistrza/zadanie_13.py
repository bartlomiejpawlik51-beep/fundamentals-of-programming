# 4, Zadanie 13 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję bubblesort(), która sortuje listę algorytmem bąbelkowym. Przetestuj ją na trzech listach.
# Sortowanie bąbelkowe trzech list

def bubblesort(array):
    """Sortuje elementy listy rosnąco za pomocą sortowania bąbelkowego."""
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

arr1 = [8, 3, 1, 9, 2]
arr2 = [15, 4, 12, 7, 1]
arr3 = [20, -5, 0, 13, 6]

print("Lista 1:", bubblesort(arr1))
print("Lista 2:", bubblesort(arr2))
print("Lista 3:", bubblesort(arr3))
