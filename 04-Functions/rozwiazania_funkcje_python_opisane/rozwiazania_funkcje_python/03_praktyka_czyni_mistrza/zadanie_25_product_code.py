# 4, Zadanie 25
# Polecenie: Sprawdź poprawność czterocyfrowego kodu produktu.
# Ostatnia cyfra powinna być resztą z dzielenia sumy pierwszych trzech cyfr przez 7.

def f(product_code):
    """Sprawdza, czy ostatnia cyfra kodu jest resztą sumy trzech pierwszych cyfr z dzielenia przez 7."""
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    first_digit = int(product_code[0])
    second_digit = int(product_code[1])
    third_digit = int(product_code[2])
    control_digit = int(product_code[3])

    expected_digit = (first_digit + second_digit + third_digit) % 7
    return control_digit == expected_digit

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
