# ZADANIE 20: Wyświetlenie produktów tańszych niż 60 i ze stanem poniżej 40.

import csv

file_name = "clothing.csv"

with open(file_name, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Odczytujemy cenę i stan magazynowy.
        price = float(row["Price"])
        stock = int(row["Stock_Quantity"])

        # Produkt musi spełniać oba warunki.
        if price < 60 and stock < 40:
            print(
                row["Product_Name"],
                "Rozmiar:", row["Size"],
                "Cena:", price,
                "Stan:", stock
            )
