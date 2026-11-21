# 4, Zadanie 4
# Polecenie: Zdefiniuj funkcję, która oblicza sumę cyfr liczby.
# Wczytaj liczbę od użytkownika i wyświetl sumę jej cyfr.

def sum_digits(number):
    """Zwraca sumę cyfr podanej liczby całkowitej, także ujemnej."""
    number = abs(number)
    text = str(number)
    total = 0

    for digit in text:
        total = total + int(digit)

    return total

any_number = int(input("Podaj liczbę całkowitą: "))
result = sum_digits(any_number)
print("Suma cyfr liczby", any_number, "wynosi", result)
