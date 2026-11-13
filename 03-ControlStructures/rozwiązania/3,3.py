# Zadanie 3.3: Sprawdzenie prawa do zniżki

age = int(input("Enter your age: "))

if age < 18 or age >= 65:
    print("Discount available")
else:
    print("Discount not available")
