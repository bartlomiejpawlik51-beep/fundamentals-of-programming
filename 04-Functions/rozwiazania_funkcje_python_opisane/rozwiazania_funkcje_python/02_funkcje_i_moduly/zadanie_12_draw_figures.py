# 4, Zadanie 12
# Polecenie: Narysuj kwadrat, trójkąt i prostokąt, każdy dwa razy w różnych miejscach ekranu.
# Funkcje rysujące znajdują się w module figures_all.py.

import turtle
import figures_all

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

# Pierwszy kwadrat
pen.penup()
pen.goto(-250, 100)
pen.pendown()
figures_all.draw_square(pen, 60)

# Drugi kwadrat
pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures_all.draw_square(pen, 80)

# Pierwszy trójkąt
pen.penup()
pen.goto(0, 100)
pen.pendown()
figures_all.draw_triangle(pen, 70)

# Drugi trójkąt
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures_all.draw_triangle(pen, 90)

# Pierwszy prostokąt
pen.penup()
pen.goto(-200, -100)
pen.pendown()
figures_all.draw_rectangle(pen, 100, 50)

# Drugi prostokąt
pen.penup()
pen.goto(0, -100)
pen.pendown()
figures_all.draw_rectangle(pen, 120, 70)

pen.hideturtle()
window.mainloop()
