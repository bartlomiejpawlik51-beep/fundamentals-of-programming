# ZADANIE 11: Przykłady wyrażeń regularnych.
# Wzorce można również wkleić do strony Regex101.

import re

text = """Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988.
They have a mutual friend named Mike, whose phone number is 555-123-4567.
In their hometown, which has a population of 1,234 or 1,235 people,
a holiday festival is held every year on December 25.
Alice works in an office with 30 employees. Her phone number is 555-765-4321."""

# Daty, np. March 12, 1992.
date_pattern = r"\b[A-Z][a-z]+ \d{1,2}, \d{4}\b"
print("Daty:", re.findall(date_pattern, text))

# Numery telefonów w formacie 555-123-4567.
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"
print("Numery telefonów:", re.findall(phone_pattern, text))

# Liczby z przecinkiem jako separatorem tysięcy.
thousands_pattern = r"\b\d{1,3}(?:,\d{3})+\b"
print("Liczby z przecinkami:", re.findall(thousands_pattern, text))

# Wyrazy zaczynające się wielką literą.
capital_words_pattern = r"\b[A-Z][a-z]+\b"
print("Wyrazy z wielkiej litery:", re.findall(capital_words_pattern, text))

# Liczby całkowite.
integer_pattern = r"\b\d+\b"
print("Liczby całkowite:", re.findall(integer_pattern, text))
