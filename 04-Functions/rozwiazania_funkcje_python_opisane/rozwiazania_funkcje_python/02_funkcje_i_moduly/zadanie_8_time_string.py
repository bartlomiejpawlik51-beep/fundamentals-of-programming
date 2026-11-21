# 4, Zadanie 8
# Polecenie: Zdefiniuj funkcję time_string(), która zamienia godzinę i minuty
# na zapis 24-godzinny lub 12-godzinny.

def time_string(hours, minutes, time_format):
    """Zwraca godzinę w formacie 24-godzinnym albo 12-godzinnym."""
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return "Nieprawidłowy czas"

    if time_format == "24":
        return f"{hours:02d}:{minutes:02d}"

    if time_format == "12":
        if hours == 0:
            return f"12:{minutes:02d}am"
        elif hours < 12:
            return f"{hours}:{minutes:02d}am"
        elif hours == 12:
            return f"12:{minutes:02d}"
        else:
            return f"{hours - 12}:{minutes:02d}pm"

    return "Nieprawidłowy format"

print(time_string(15, 38, "24"))
print(time_string(8, 3, "24"))
print(time_string(0, 5, "24"))
print(time_string(11, 15, "12"))
print(time_string(0, 7, "12"))
print(time_string(7, 30, "12"))
print(time_string(12, 46, "12"))
print(time_string(13, 10, "12"))
print(time_string(19, 2, "12"))
