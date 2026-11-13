# Zadanie 1.6: Liczba parzysta czy nieparzysta

number = int(input("Enter number: "))

if number % 2 == 0:  # % zwraca resztę z dzielenia
    print(f"{number} is even")
else:
    print(f"{number} is odd")
