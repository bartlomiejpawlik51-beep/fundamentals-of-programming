# 4, Zadanie 3
# Polecenie: Sprawdź, czy podana liczba znajduje się w przedziale od 2 do 15.
# Funkcja sprawdzająca zakres znajduje się w module number_range.py.

import number_range

number = int(input("A number: "))

if number_range.is_in_range(number, 2, 15):
    print("Number", number, "in the range <2,15>: yes")
else:
    print("Number", number, "in the range <2,15>: no")
