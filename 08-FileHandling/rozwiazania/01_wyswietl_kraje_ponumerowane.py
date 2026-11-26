# ZADANIE 1: Wyświetlenie krajów z pliku i ponumerowanie ich.

file_name = "countries.txt"

# Otwieramy plik w trybie odczytu.
with open(file_name, "r", encoding="utf-8") as file:
    number = 1

    # Odczytujemy plik po jednym wierszu.
    for line in file:
        # strip() usuwa znak końca wiersza i zbędne spacje.
        line = line.strip()

        # Wyświetlamy numer i zawartość wiersza.
        print(str(number) + ". " + line)

        # Zwiększamy numer o jeden.
        number += 1
