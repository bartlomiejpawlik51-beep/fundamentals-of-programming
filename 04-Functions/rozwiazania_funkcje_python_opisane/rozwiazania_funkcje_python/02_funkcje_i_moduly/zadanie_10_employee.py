# 4, Zadanie 10
# Polecenie: Użyj modułu keyboard.py do pobrania danych pracownika.
# Zapytaj, czy wynagrodzenie ma być ukryte, i wyświetl dane pracownika.

import keyboard

first_name = keyboard.input_string("Podaj imię: ")
last_name = keyboard.input_string("Podaj nazwisko: ")
age = keyboard.input_integer("Podaj wiek: ")
salary = keyboard.input_real("Podaj wynagrodzenie: ")
is_salary_hidden = keyboard.input_boolean("Ukryć wynagrodzenie? (y/n): ")

print("DATA RECORD")
print("===========")
print("Imię:", first_name)
print("Nazwisko:", last_name)
print("Wiek:", age)

if is_salary_hidden == False:
    print("Wynagrodzenie:", salary)
else:
    print("Wynagrodzenie: ukryte")
