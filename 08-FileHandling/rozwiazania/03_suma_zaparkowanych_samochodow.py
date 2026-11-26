# ZADANIE 3: Obliczenie całkowitej liczby zaparkowanych samochodów.

def read_from_file(name):
    """Odczytuje cały plik i zwraca jego zawartość jako tekst."""
    with open(name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


# Odczytujemy plik i dzielimy jego zawartość na wiersze.
file_content = read_from_file("car_park.txt")
file_lines = file_content.splitlines()

# Zmienna total przechowuje sumę samochodów.
total = 0

# Przechodzimy po każdym wierszu.
for line in file_lines:
    # Zamieniamy tekst na liczbę i dodajemy do sumy.
    total += int(line)

# Wyświetlamy wynik.
print("Total cars parked:", total)
