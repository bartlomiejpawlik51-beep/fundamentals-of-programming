# Zadanie 6.12: Rabat 25% na każdy produkt powyżej dwóch

quantity = int(input("Number of products: "))
price = float(input("Product price: "))

total = 0

for i in range(1, quantity + 1):
    if i > 2:
        total += price * 0.75
    else:
        total += price

print(f"Amount to pay: {total:.2f}")
