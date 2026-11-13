# Zadanie 6.31: Dwadzieścia losowych liczb od 5 do 10

import random

for i in range(20):
    number = random.randint(5, 10)  # randint() losuje liczbę całkowitą, razem z końcami zakresu
    print(number, end=" ")
print()
