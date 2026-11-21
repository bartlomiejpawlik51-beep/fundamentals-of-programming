# 4, Zadanie 21 - Praktyka czyni mistrza
# Polecenie: Napisz program, który zlicza elementy listy większe od wartości podanej przez użytkownika.
# Liczenie elementów większych od podanej liczby

numbers = [2.5, 7.1, 4.8, 9.2, 1.5, 6.0]
limit = float(input("Podaj wartość: "))
counter = 0

for number in numbers:
    if number > limit:
        counter = counter + 1

print("Liczba elementów większych od", limit, ":", counter)
