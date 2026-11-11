celsius = float(input('Enter temperature in Celsius: '))

# Convert to Kelvin
kelvin = celsius + 273.15

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

print(f'Temperature in Kelvin: {kelvin:.2f}')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')