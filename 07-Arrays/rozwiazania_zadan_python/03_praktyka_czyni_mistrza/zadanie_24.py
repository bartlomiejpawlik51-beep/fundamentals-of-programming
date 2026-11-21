# 4, Zadanie 24 - Praktyka czyni mistrza
# Polecenie: Zdefiniuj funkcję rand_elem(), która losuje i zwraca element listy. Wywołaj ją kilka razy.
# Losowanie elementów listy

import random

def rand_elem(array):
    """Losuje i zwraca jeden element z podanej listy."""
    position = random.randint(0, len(array) - 1)
    return array[position]

arr = ["jabłko", "gruszka", "banan", "śliwka", "kiwi"]

for i in range(5):
    print(rand_elem(arr))
