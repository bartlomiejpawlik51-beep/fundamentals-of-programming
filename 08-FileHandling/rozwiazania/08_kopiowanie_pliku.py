# ZADANIE 8: Skopiowanie zawartości pliku tekstowego.

original_file = "healthy_lifestyle.txt"
target_file = "copy_healthy_lifestyle.txt"

# Otwieramy plik źródłowy i odczytujemy całą zawartość.
with open(original_file, "r", encoding="utf-8") as file:
    content = file.read()

# Otwieramy plik docelowy i zapisujemy w nim odczytany tekst.
with open(target_file, "w", encoding="utf-8") as file:
    file.write(content)

print("Skopiowano zawartość pliku.")
