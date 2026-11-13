# Zadanie 2.3: Zużycie paliwa

driving_mode = input("Enter driving mode (A/M/E): ").upper()
distance = int(input("Enter distance in km: "))

if driving_mode == "A":
    fuel_consumption = 7
elif driving_mode == "M":
    fuel_consumption = 9
elif driving_mode == "E":
    fuel_consumption = 6
else:
    fuel_consumption = 0
    print("Incorrect driving mode")

if fuel_consumption > 0:
    total_consumption = distance * fuel_consumption / 100
    print(f"Total fuel consumption: {total_consumption} liters")
