# Zadanie 6.2: Liczenie samogłosek pętlą while

text = input("Enter text: ")
vowels = "aąeęioóuy"
counter = 0
i = 0

while i < len(text):  # len() zwraca liczbę znaków w tekście
    if text[i].lower() in vowels:  # lower() zamienia literę na małą
        counter += 1
    i += 1

print("Number of vowels:", counter)
