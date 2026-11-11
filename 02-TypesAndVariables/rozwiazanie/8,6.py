distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))

# Calculate total fuel consumption
total_fuel_consumption = distance * fuel_consumption / 100

# Calculate total cost
total_cost = total_fuel_consumption * fuel_price

# Display results
print(f'Fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Transport cost: {total_cost:.2f} PLN')