# 4, Zadanie 14 - Praktyka czyni mistrza
# Polecenie: Napisz program, który wyświetla tylko te elementy listy, które występują w niej dokładnie jeden raz.
# Wyświetlanie unikalnych elementów listy

arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

for value in arr:
    if arr.count(value) == 1:
        unique_elements.append(value)

print("Array:", *arr)
print("Unique elements:", *unique_elements)
