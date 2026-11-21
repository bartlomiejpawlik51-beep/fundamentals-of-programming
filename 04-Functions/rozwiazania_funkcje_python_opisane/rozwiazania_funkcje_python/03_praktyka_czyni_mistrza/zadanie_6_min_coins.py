# 4, Zadanie 6
# Polecenie: Oblicz minimalną liczbę monet 1 zł, 2 zł i 5 zł potrzebnych do zapłacenia podanej kwoty.

def f(amount_to_pay):
    """Zwraca minimalną liczbę monet o nominałach 5, 2 i 1 potrzebnych do zapłaty."""
    if amount_to_pay < 0:
        return 0

    coins = 0
    coins = coins + amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5

    coins = coins + amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2

    coins = coins + amount_to_pay
    return coins

print(f(23))
print(f(8))
print(f(2))
print(f(0))
