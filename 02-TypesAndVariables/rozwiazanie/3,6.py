import math #importuje moduł matematyczny.
h = float(input("Podaj wysokość obserwatora w metrach: ")) 
d = 3.57 * math.sqrt(h)
print("Odległość do horyzontu wynosi:", round(d, 2), "km")