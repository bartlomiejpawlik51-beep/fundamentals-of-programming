# Zadanie 6.18: Położenie punktu na płaszczyźnie

x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x > 0 and y > 0:
    print("Point is in the first quadrant")
elif x < 0 and y > 0:
    print("Point is in the second quadrant")
elif x < 0 and y < 0:
    print("Point is in the third quadrant")
elif x > 0 and y < 0:
    print("Point is in the fourth quadrant")
elif x == 0 and y == 0:
    print("Point is at the origin (0,0)")
elif x == 0:
    print("Point is on the Y axis")
else:
    print("Point is on the X axis")
