# ZADANIE 16: Obliczenie liczby wierszy, znaków i słów w pliku.

file_name = input("Podaj nazwę pliku: ")

try:
    # Otwieramy wskazany plik i odczytujemy całą zawartość.
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    # Dzielimy tekst na wiersze i słowa.
    lines = content.splitlines()
    words = content.split()

    # Obliczamy liczbę wierszy, znaków i słów.
    number_of_lines = len(lines)
    number_of_characters = len(content)
    number_of_words = len(words)

    print("Number of lines:", number_of_lines)
    print("Number of characters:", number_of_characters)
    print("Number of words:", number_of_words)

except FileNotFoundError:
    # Obsługujemy sytuację, gdy plik nie istnieje.
    print("Nie znaleziono pliku. Sprawdź nazwę i spróbuj ponownie.")
