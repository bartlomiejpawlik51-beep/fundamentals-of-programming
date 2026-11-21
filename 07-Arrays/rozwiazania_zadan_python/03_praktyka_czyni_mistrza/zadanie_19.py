# 4, Zadanie 19 - Praktyka czyni mistrza
# Polecenie: Napisz program, który zlicza wystąpienia wybranej wartości w krotce.
# Zliczanie wystąpień wartości w krotce

numbers = (50, 20, 40, 50, 30, 50)
value = 50
counter = 0

for number in numbers:
    if number == value:
        counter = counter + 1

print("Tuple:", numbers)
print("Value:", value)
print("Number of occurrences:", counter)
