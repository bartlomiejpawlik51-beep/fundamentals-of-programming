# 4, Zadanie 27 - Praktyka czyni mistrza
# Polecenie: Napisz program, który rysuje wykres funkcji f(x) = x^2 - 3.
# Rysowanie wykresu funkcji f(x) = x^2 - 3

import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100, 101):
    x.append(n)

for n in x:
    y.append(n * n - 3)

plt.plot(x, y)
plt.title("Wykres funkcji f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
