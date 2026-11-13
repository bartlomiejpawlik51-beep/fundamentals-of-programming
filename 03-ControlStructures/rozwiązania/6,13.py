# Zadanie 6.13: Sprawdzenie prędkości samochodu

prędkość_samochodu = int(input("Wprowadź prędkość samochodu: "))
limit_prędkości_min = 40
limit_prędkości_max = 140

if prędkość_samochodu < limit_prędkości_min or prędkość_samochodu > limit_prędkości_max:
    print("Ostrzeżenie: nieprawidłowa prędkość samochodu!!")
else:
    print("Prędkość jest prawidłowa")
