a = input('a=')
b = input('b=')
c = input('c=')
a = int(a)
b = int(b)
c = int(c)

volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of the cuboid is {volume}')
print(f'The surface area of the cuboid is {surface_area}')