# 4, Zadanie 12 - Moduł figures_all
# Polecenie: Zdefiniuj funkcje rysujące kwadrat, trójkąt równoramienny i prostokąt.
# Każda funkcja korzysta z przekazanego obiektu żółwia.

def draw_square(pen, length):
    """Rysuje kwadrat o podanej długości boku."""
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    """Rysuje trójkąt równoboczny o podanej długości boku."""
    for i in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b):
    """Rysuje prostokąt o podanych długościach boków."""
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
