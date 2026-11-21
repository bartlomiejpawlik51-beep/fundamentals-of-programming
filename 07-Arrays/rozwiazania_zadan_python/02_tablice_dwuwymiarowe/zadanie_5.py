# 4, Zadanie 5 - Tablice dwuwymiarowe
# Polecenie: Napisz program, który oblicza liczbę miejsc dostępnych i zarezerwowanych w kinie oraz sprawdza status wybranych miejsc.
# Informacje o miejscach w kinie

cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    """Oblicza łączną liczbę wszystkich miejsc w kinie."""
    total = 0
    for row in seats:
        total = total + len(row)
    return total

def seats_available(seats):
    """Zlicza miejsca oznaczone literą A, czyli dostępne."""
    total = 0
    for row in seats:
        for seat in row:
            if seat == "A":
                total = total + 1
    return total

def seats_booked(seats):
    """Zlicza miejsca oznaczone literą B, czyli zarezerwowane."""
    total = 0
    for row in seats:
        for seat in row:
            if seat == "B":
                total = total + 1
    return total

def seat_status(seats, row, place):
    """Zwraca informację, czy wskazane miejsce jest dostępne, czy zarezerwowane."""
    if seats[row - 1][place - 1] == "A":
        return "dostępne"
    return "zarezerwowane"

print("CINEMA INFORMATION TABLE")
print("Total seats:", seats_total(cinema_seats))
print("Seats available:", seats_available(cinema_seats))
print("Seats booked:", seats_booked(cinema_seats))
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))
