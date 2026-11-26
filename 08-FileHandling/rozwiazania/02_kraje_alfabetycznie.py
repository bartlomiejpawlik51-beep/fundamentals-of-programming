# ZADANIE 2: Wyświetlenie krajów w kolejności alfabetycznej.

def read_from_file(name):
    """Odczytuje cały plik tekstowy i zwraca jego zawartość."""
    with open(name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


# Wywołujemy funkcję i pobieramy tekst z pliku.
file_content = read_from_file("countries.txt")

# Dzielimy tekst na osobne wiersze.
file_lines = file_content.splitlines()

# Sortujemy wiersze alfabetycznie.
sorted_lines = sorted(file_lines)

# Wyświetlamy posortowaną listę.
for line in sorted_lines:
    print(line)
