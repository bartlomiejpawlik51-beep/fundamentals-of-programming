# Zadanie 4.6: Suma liczb od 5 do 10

total = 0

for i in range(5, 11):  # górna granica range() nie jest wliczana
    total += i  # += dodaje wartość do aktualnej zmiennej

print(f"Sum is {total}")
