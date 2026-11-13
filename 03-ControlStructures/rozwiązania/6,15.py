# Zadanie 6.15: Sprawdzenie numeru EAN-13

ean = input("Enter EAN-13 number: ")

if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    if ean.startswith("590"):  # startswith() sprawdza początek tekstu
        print("Article manufactured in Poland")
else:
    print("Article number is incorrect")
