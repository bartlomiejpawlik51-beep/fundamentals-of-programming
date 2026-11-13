# Zadanie 4.4: Nazwa uczelni ze spacjami

university = "Krakow University of Economics"
university_expanded = ""

for char in university:
    university_expanded = university_expanded + char + " "

print(university)
print(university_expanded.strip())  # strip() usuwa spację z początku i końca tekstu
