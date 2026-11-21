# 4, Zadanie 22
# Polecenie: Oblicz wyrażenie zawierające jednocyfrowe liczby oraz operatory + i -.
# Program wykonuje działania od lewej do prawej.

def f(expression):
    """Oblicza proste wyrażenie z jednocyfrowymi liczbami i znakami plus oraz minus."""
    total = 0
    current_number = 0
    operation = "+"

    for character in expression:
        if character.isdigit():
            current_number = int(character)
            if operation == "+":
                total = total + current_number
            elif operation == "-":
                total = total - current_number
        elif character == "+" or character == "-":
            operation = character

    return total

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
