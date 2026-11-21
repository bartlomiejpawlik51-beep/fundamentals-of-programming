# 4, Zadanie 11 - Moduł figures
# Polecenie: Umieść w module funkcję rysującą kwadrat o podanej długości boku.

import turtle

def draw_square(length):
    """Rysuje kwadrat o podanej długości boku."""
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
