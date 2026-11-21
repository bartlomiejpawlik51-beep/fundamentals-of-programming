# 4, Zadanie 12
# Polecenie: Napisz funkcję wykonującą działanie wskazane operatorem +, -, *, %, **.

def f(number1, number2, operator):
    """Wykonuje działanie arytmetyczne wskazane przez operator."""
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Nieznany operator"

print(f(2, 3, "+"))
print(f(2, 3, "%"))
print(f(2, 3, "**"))
print(f(2, 3, "*"))
print(f(2, 3, "-"))
