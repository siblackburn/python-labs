'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.
'''



import math
math.pi
r = 3.14
h = 5

area = 2 * math.pi * r * h + (2 * math.pi * r**2)

print(area)

volume = math.pi * r**2 * h

print(volume)