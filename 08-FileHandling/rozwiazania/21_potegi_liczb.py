# ZADANIE 21: Obliczenie i zapis liczb od 1 do 100 oraz ich potęg.

file_name = "powers.txt"

# Otwieramy plik w trybie zapisu.
with open(file_name, "w", encoding="utf-8") as file:
    # range(1, 101) generuje liczby od 1 do 100.
    for number in range(1, 101):
        square = number ** 2
        cube = number ** 3

        # Przygotowujemy wiersz: liczba, druga potęga, trzecia potęga.
        line = str(number) + "," + str(square) + "," + str(cube)

        # Wyświetlamy i zapisujemy wiersz.
        print(line)
        file.write(line + "\n")

print("Wyniki zapisano w pliku", file_name)
