# 4, Zadanie 3 - Tablice dwuwymiarowe
# Polecenie: Napisz program, który oblicza wydatki według kategorii, tygodni oraz łącznie za cały miesiąc.
# Obliczanie wydatków w tygodniach i kategoriach

monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

food_total = 0
transport_total = 0
utilities_total = 0
week_totals = []
month_total = 0

for week in monthly_expenses:
    food_total = food_total + week[0]
    transport_total = transport_total + week[1]
    utilities_total = utilities_total + week[2]

    week_sum = 0
    for expense in week:
        week_sum = week_sum + expense
    week_totals.append(week_sum)
    month_total = month_total + week_sum

print("MONTHLY EXPENSES")
print("----------------")
print("Food:", food_total)
print("Transport:", transport_total)
print("Utilities:", utilities_total)

for i in range(len(week_totals)):
    print("Week", i + 1, ":", week_totals[i])

print("---------------")
print("TOTAL:", month_total)
