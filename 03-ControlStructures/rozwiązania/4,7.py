# Zadanie 4.7: Suma liczb parzystych od 1 do 10

total = 0

for i in range(1, 11):
    if i % 2 == 0:
        total += i

print("Sum of even numbers in the range <1,10> is", total)
