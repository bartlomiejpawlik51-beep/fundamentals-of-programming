# ZADANIE 18: Wyświetlenie nazw plików z rozszerzeniem mającym 4 znaki.

import re

file_name = "files.txt"

# Kropka oznacza początek rozszerzenia.
# [A-Za-z0-9]{4} oznacza dokładnie cztery znaki.
# $ oznacza koniec wiersza.
extension_pattern = r"\.[A-Za-z0-9]{4}$"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()

            if re.search(extension_pattern, name):
                print(name)

except FileNotFoundError:
    print("Nie znaleziono pliku:", file_name)
