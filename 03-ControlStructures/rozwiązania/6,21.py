# Zadanie 6.21: Wydanie kwoty najmniejszą liczbą monet

amount = int(input("Enter amount in PLN: "))

coins5 = amount // 5
amount = amount % 5

coins2 = amount // 2
amount = amount % 2

coins1 = amount

print("5 PLN coins:", coins5)
print("2 PLN coins:", coins2)
print("1 PLN coins:", coins1)
