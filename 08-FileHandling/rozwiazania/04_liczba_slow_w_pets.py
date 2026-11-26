# ZADANIE 4: Wyświetlenie tekstu pets.txt i policzenie słów.

file_name = "pets.txt"
number_of_words = 0

# Otwieramy plik i odczytujemy go wiersz po wierszu.
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        # Wyświetlamy aktualny wiersz.
        print(line, end="")

        # split() dzieli wiersz na słowa.
        words = line.split()

        # len() zwraca liczbę słów w danym wierszu.
        number_of_words += len(words)

# Wyświetlamy sumę słów.
print("\nLiczba słów:", number_of_words)
