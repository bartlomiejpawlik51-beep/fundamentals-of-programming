# ZADANIE 22: Podział książek na pliki według gatunku.

import csv


def save_books_by_genre(input_file, genre, output_file):
    """Zapisuje do pliku książki należące do wybranego gatunku.

    input_file - nazwa pliku CSV z książkami,
    genre - gatunek książki, którego szukamy,
    output_file - nazwa pliku, do którego zapisujemy wyniki.
    """
    # Otwieramy plik z książkami.
    with open(input_file, "r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)

        # Otwieramy plik wynikowy.
        with open(output_file, "w", encoding="utf-8", newline="") as target:
            writer = csv.DictWriter(target, fieldnames=reader.fieldnames)

            # Zapisujemy nagłówki kolumn.
            writer.writeheader()

            # Sprawdzamy każdy rekord książki.
            for row in reader:
                if row["Genre"] == genre:
                    writer.writerow(row)


# Słownik łączy nazwę gatunku z nazwą pliku wynikowego.
genres = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}

# Dla każdego gatunku wywołujemy funkcję.
for genre, output_file in genres.items():
    save_books_by_genre("books.csv", genre, output_file)

print("Książki zostały podzielone według gatunków.")
