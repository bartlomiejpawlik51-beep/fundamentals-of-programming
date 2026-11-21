# 4, Zadanie 3
# Polecenie: Napisz funkcję, która dla numeru od 1 do 7 zwraca nazwę dnia tygodnia.
# Funkcja zwracająca nazwę dnia tygodnia

def weekday(n):
    """Zwraca nazwę dnia tygodnia dla numeru od 1 do 7."""
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    if n >= 1 and n <= 7:
        return weekdays[n - 1]
    return "Nieprawidłowy numer dnia"

print(weekday(1))
print(weekday(4))
print(weekday(7))
