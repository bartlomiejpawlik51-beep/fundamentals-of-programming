# 4, Zadanie 6
# Polecenie: Zdefiniuj funkcję, która zwraca pełną nazwę dnia tygodnia na podstawie numeru.

def day_name(day_number):
    """Zwraca nazwę dnia tygodnia dla numeru od 1 do 7."""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

    if day_number >= 1 and day_number <= 7:
        return weekdays[day_number - 1]
    return "Nieprawidłowy numer dnia"

print("Dzień 5:", day_name(5))
print("Dzień 3:", day_name(3))
print("Dzień 7:", day_name(7))
