# 4, Zadanie 26 - Praktyka czyni mistrza
# Polecenie: Napisz program, który za pomocą matplotlib rysuje odcinek od punktu (1, 3) do punktu (8, 10).
# Rysowanie odcinka za pomocą matplotlib
# Jeśli biblioteka nie jest zainstalowana, wpisz w terminalu: pip install matplotlib

import matplotlib.pyplot as plt

xpoints = [1, 8]
ypoints = [3, 10]

plt.plot(xpoints, ypoints)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Odcinek od (1, 3) do (8, 10)")
plt.grid()
plt.show()
