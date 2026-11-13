# Zadanie 2.4: Prosty kalkulator

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Cannot divide by zero"
else:
    result = "Unknown operation"

print(f"{number1} {operator} {number2} = {result}")
