# ZADANIE 9: Zapisanie pracowników Software Engineer do osobnego pliku.

import csv

employees_file = "it_company.csv"
position_file = "software_engineer.txt"
job_title = "Software Engineer"

# Otwieramy plik CSV z pracownikami.
with open(employees_file, "r", encoding="utf-8", newline="") as input_file:
    reader = csv.DictReader(input_file)

    # Otwieramy plik wynikowy.
    with open(position_file, "w", encoding="utf-8") as output_file:
        for row in reader:
            # Sprawdzamy stanowisko pracownika.
            if row["Job Title"] == job_title:
                # Zapisujemy cały wiersz pracownika.
                output_file.write(
                    row["Last Name"] + "," +
                    row["First Name"] + "," +
                    row["Job Title"] + "," +
                    row["Email"] + "\n"
                )

print("Dane inżynierów zapisano w pliku", position_file)
