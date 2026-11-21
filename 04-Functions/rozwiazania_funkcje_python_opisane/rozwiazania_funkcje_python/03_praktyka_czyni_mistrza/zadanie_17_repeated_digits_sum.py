# 4, Zadanie 17
# Polecenie: Oblicz sumę cyfr, które powtarzają się w liczbie.
# Każdą powtarzającą się cyfrę dodajemy tylko raz.

def f(number):
    """Zwraca sumę różnych cyfr, które występują w liczbie co najmniej dwa razy."""
    digits = str(abs(number))
    total = 0

    for digit in digits:
        if digits.count(digit) > 1 and digits.index(digit) == digits.find(digit):
            total = total + int(digit)

    return total

print(f(1027))
print(f(230335))
print(f(513553007))
