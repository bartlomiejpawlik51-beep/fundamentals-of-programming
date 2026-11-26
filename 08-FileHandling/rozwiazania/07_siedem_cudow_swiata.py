# ZADANIE 7: Sortowanie i zapis Siedmiu Cudów Świata.

seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

file_name = "seven_wonders.txt"

# Sortujemy nazwy alfabetycznie.
sorted_wonders = sorted(seven_wonders)

# Zapisujemy każdy cud w osobnym wierszu.
with open(file_name, "w", encoding="utf-8") as file:
    for item in sorted_wonders:
        file.write(item + "\n")

print("Lista siedmiu cudów świata została zapisana.")
