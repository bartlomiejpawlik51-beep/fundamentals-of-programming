# 4, Zadanie 1 - Moduł months
# Polecenie: Zdefiniuj funkcję month(n), która zwraca nazwę miesiąca dla numeru od 1 do 12.

def month(n):
    """Zwraca nazwę miesiąca na podstawie numeru od 1 do 12."""
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if n >= 1 and n <= 12:
        return months[n - 1]
    return "Nieprawidłowy numer miesiąca"
