# Zadanie 6.30: Kupon loterii 1--49

for row in range(7):
    for column in range(7):
        number = row + 1 + column * 7
        print(number, end=" ")
    print()
