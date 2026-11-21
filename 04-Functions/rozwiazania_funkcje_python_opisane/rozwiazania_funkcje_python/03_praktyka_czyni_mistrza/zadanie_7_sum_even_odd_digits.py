# 4, Zadanie 7
# Polecenie: Napisz funkcję, która sumuje cyfry parzyste albo nieparzyste zależnie od parametru even.

def f(number, even):
    """Zwraca sumę cyfr parzystych lub nieparzystych zależnie od wartości even."""
    number = abs(number)
    total = 0

    for digit in str(number):
        digit = int(digit)

        if even == True and digit % 2 == 0:
            total = total + digit
        elif even == False and digit % 2 != 0:
            total = total + digit

    return total

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))
