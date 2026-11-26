# ZADANIE 14: Wyświetlanie pliku it_company.csv po pięć wierszy.

file_name = "it_company.csv"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        while True:
            lines = []

            # Pobieramy maksymalnie pięć kolejnych wierszy.
            for i in range(5):
                line = file.readline()

                # Pusty tekst oznacza koniec pliku.
                if line == "":
                    break

                lines.append(line)

            # Jeżeli nie ma już wierszy, kończymy.
            if len(lines) == 0:
                break

            # Wyświetlamy pobrane wiersze.
            for line in lines:
                print(line, end="")

            # Czekamy na Enter, jeżeli mogą być kolejne wiersze.
            if len(lines) == 5:
                input("\nNaciśnij Enter, aby wyświetlić kolejne wiersze...")

except FileNotFoundError:
    print("Nie znaleziono pliku:", file_name)
