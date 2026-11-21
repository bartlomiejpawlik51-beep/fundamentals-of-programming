# 4, Zadanie 4 - Tablice dwuwymiarowe
# Polecenie: Napisz program, który wyświetla tygodniowy plan posiłków wraz z nazwami dni tygodnia.
# Wyświetlanie tygodniowego planu posiłków

meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
    """Zwraca nazwę dnia tygodnia dla numeru od 1 do 7."""
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

def day_meal_plan(meal_plan, day_number):
    """Zwraca posiłki zaplanowane na wybrany dzień jako jeden tekst."""
    meals = meal_plan[day_number - 1]
    return meals[0] + ", " + meals[1] + ", " + meals[2]

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for day in range(1, 8):
    print(weekday(day) + ": " + day_meal_plan(meal_plan, day))
