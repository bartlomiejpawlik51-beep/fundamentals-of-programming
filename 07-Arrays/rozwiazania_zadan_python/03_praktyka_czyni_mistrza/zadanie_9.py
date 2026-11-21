# 4, Zadanie 9 - Praktyka czyni mistrza
# Polecenie: Napisz program, który znajduje i wyświetla najdłuższe imię z listy.
# Znajdowanie najdłuższego imienia

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]

for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", " ".join(names))
print("Longest name:", longest_name)
