# Zadanie 6.6: Opłata parkingowa

hours = int(input("Enter parking time in hours: "))

if hours < 1:
    print("Incorrect parking time")
elif hours <= 2:
    fee = 5
    print("Parking fee:", fee, "PLN")
elif hours <= 6:
    fee = 15
    print("Parking fee:", fee, "PLN")
else:
    fee = 20
    print("Parking fee:", fee, "PLN")
