'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi

class rectangle():
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * length + 2 * width

    def __str__(self):
        return f"The area of the rectangle is, {self.area}, whereas the perimeter is {self.perimeter}"

class circle():
    def __init__(self, radius = 0):
        self.radius = radius
        self.area = round(pi * radius**2,2)
        self.circumference = round(2 * pi * radius,2)

    def __str__(self):
        return f"The area of the circle is, {self.area}, whereas the circumference is {self.circumference1}"


disc = circle(3)
print(disc)

box = rectangle(3,4)
print(box)


