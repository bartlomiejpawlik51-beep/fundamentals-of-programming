# 4, Zadanie 1
# Polecenie: Użyj funkcji wbudowanych Pythona, aby obliczyć maksimum, minimum, długość tekstu,
# odczytać tekst i liczbę z klawiatury, zamienić liczbę na zapis binarny i szesnastkowy,
# odczytać kod Unicode znaku euro oraz obliczyć wartość bezwzględną.

max_number = max(7, 5, 6, 3, 8, 2)
print("Największa liczba:", max_number)

min_number = min(4, 7, 2, 3, 9, 8)
print("Najmniejsza liczba:", min_number)

text = "informatyka"
print("Długość tekstu:", len(text))

word = input("Wpisz tekst: ")
print("Wpisany tekst:", word)

number_text = "20303"
number = int(number_text)
print("Liczba z tekstu:", number)

decimal_number = 304
print("Zapis binarny:", bin(decimal_number))
print("Zapis szesnastkowy:", hex(decimal_number))

print("Kod Unicode znaku €:", ord("€"))
print("Wartość bezwzględna -17:", abs(-17))
