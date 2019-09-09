'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class car():

    def __init__(self, model, year, speed = 0):
        self.model = model
        self.year = year
        self.speed = speed
        self.newspeed = speed +5

    def new_attributes(self):
        self.accelerate = self.speed + 5
        self.brake = self.speed
        if self.brake >= 5:
            self.brake = self.speed - 5
        else:
            self.brake = self.speed
        return self.speed, self.brake

    def __str__(self):
        return f"{self.model} goes 'beep beep'"



honda_civic = car("civic", 2008)
print(f"The {honda_civic.model} was built in {honda_civic.year} and has a top speed of {honda_civic.speed}")

honda_nsx = car("nsx", 1999, 150)
print(f"The {honda_nsx.model} was built in {honda_nsx.year} and has a top speed of {honda_nsx.speed}")


#printing updated stats on the car based on the new_attibutes function

honda_civic.new_attributes()
print(f"Actually, the {honda_civic.model} was built in {honda_civic.year} and has a top speed of {honda_civic.accelerate}")

honda_nsx.new_attributes()
print(f"Actually, the {honda_nsx.model} was built in {honda_nsx.year} and has a top speed of {honda_nsx.accelerate}")

print(honda_civic)