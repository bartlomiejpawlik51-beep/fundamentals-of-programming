# 4, Zadanie 1
# Polecenie: Pobierz numer miesiąca od użytkownika i wyświetl jego nazwę.
# Funkcja month() znajduje się w osobnym module months.py.

import months

month_number = int(input("Enter month number: "))
print("The name of month", month_number, "is", months.month(month_number))
