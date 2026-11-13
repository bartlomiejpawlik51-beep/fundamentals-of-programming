# Zadanie 6.20: Konwersja liczby dziesiętnej na binarną

number = int(input("Enter decimal number: "))
original_number = number
binary = ""

if number == 0:
    binary = "0"
else:
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2  # // wykonuje dzielenie całkowite

print(f"{original_number}(10) = {binary}(2)")
