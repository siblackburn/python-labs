'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():

    def __init__(self, name, colour, system):
        self.name = name
        self.colour = colour
        self.system = system

mars = Planet("mars", "red", "solar")

print(f"{mars.name} is a {mars.colour} planet in {mars.system} system")





'''
Init initialises a new object. In this line we're defining a new method - which is a function that sits inside a class
Self is the default object that Python creates
Then can separate with comma and add more objects to pass to the '''