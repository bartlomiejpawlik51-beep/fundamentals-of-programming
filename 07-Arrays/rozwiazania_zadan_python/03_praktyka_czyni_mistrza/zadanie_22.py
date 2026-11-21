# 4, Zadanie 22 - Praktyka czyni mistrza
# Polecenie: Napisz program, który umieszcza liczby parzyste przed nieparzystymi na nowej liście.
# Oddzielanie liczb parzystych od nieparzystych

arr = [7, 9, 2, 4, 5, 6]
even_numbers = []
odd_numbers = []

for number in arr:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

result = even_numbers + odd_numbers

print("arr =", arr)
print("arr =", result)
