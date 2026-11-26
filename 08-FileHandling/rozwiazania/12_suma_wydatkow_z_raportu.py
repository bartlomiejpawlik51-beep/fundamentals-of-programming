# ZADANIE 12: Obliczenie całkowitej kwoty wydanej na zakupy.

import re

email_file = "report.txt"

# Odczytujemy wiadomość w kodowaniu UTF-8.
with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

# Wzorzec znajduje kwoty, np. €102, €30, €15 i €20.
pattern = r"€\s*(\d+(?:[.,]\d{1,2})?)"

# findall() zwraca listę znalezionych kwot.
amounts = re.findall(pattern, email)

total = 0

# Dodajemy każdą znalezioną kwotę do sumy.
for amount in amounts:
    # Zamieniamy tekst na liczbę.
    total += float(amount.replace(",", "."))

print("Łączna wartość zakupów:", total, "€")
