# ZADANIE 19: Wyświetlenie imienia, nazwiska i e-maila grafików.

import csv

file_name = "it_company.csv"
job_title = "Graphic Designer"

print("GRAPHIC DESIGNERS")
print("=================")

with open(file_name, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Job Title"] == job_title:
            # Wypisujemy imię, nazwisko i e-mail w podanej kolejności.
            print(row["First Name"] + " " + row["Last Name"] + "," + row["Email"])
