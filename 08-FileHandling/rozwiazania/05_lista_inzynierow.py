# ZADANIE 5: Wyświetlenie pracowników na stanowisku Software Engineer.

import csv

file_name = "it_company.csv"
job_title = "Software Engineer"
number = 1

# Otwieramy plik CSV.
with open(file_name, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    # Odczytujemy dane każdego pracownika.
    for row in reader:
        # Sprawdzamy nazwę stanowiska.
        if row["Job Title"] == job_title:
            print(
                str(number) + ". " +
                row["First Name"] + " " +
                row["Last Name"] + ", " +
                row["Email"]
            )
            number += 1
