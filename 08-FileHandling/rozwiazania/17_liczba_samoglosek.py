# ZADANIE 17: Obliczenie liczby samogłosek w tekście.

import re

text = input("Wpisz tekst: ")

# Wzorzec zawiera samogłoski polskie i angielskie.
vowels_pattern = r"[aeiouyąęóAEIOUYĄĘÓ]"

# findall() zwraca listę wszystkich samogłosek.
vowels = re.findall(vowels_pattern, text)

print("Liczba samogłosek:", len(vowels))
