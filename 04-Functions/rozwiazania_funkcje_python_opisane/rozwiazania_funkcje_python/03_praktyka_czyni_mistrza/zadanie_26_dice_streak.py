# 4, Zadanie 26
# Polecenie: Znajdź największą liczbę takich samych wyników kostki występujących kolejno.

def f(dice):
    """Zwraca długość najdłuższej serii takich samych kolejnych cyfr."""
    if dice == "":
        return 0

    longest = 1
    current = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current = current + 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest

print(f("5233165554211"))
print(f("2133"))
