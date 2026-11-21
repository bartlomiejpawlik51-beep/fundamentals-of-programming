# 4, Zadanie 28 - Praktyka czyni mistrza
# Polecenie: Napisz program, który rysuje wykres funkcji sin(x) dla kątów od 0 do 360 stopni.
# Rysowanie funkcji y = sin(x) dla kątów od 0 do 360 stopni

import math
import matplotlib.pyplot as plt

x = []
y = []

for degree in range(361):
    x.append(degree)
    radians = math.radians(degree)
    y.append(math.sin(radians))

plt.plot(x, y)
plt.title("Wykres funkcji y = sin(x)")
plt.xlabel("Kąt w stopniach")
plt.ylabel("sin(x)")
plt.grid()
plt.show()
