'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class accommodation():

    def __init__(self, name, usp, average_cost = 50):
        self.name = name
        self.average_cost = average_cost
        self.usp = usp

    def __add__(self, other):
        total_cost = self.average_cost + other.average_cost
        total_usp = self.usp + other.usp
        return accommodation(total_cost, total_usp)

    def __str__(self):
        return f"{self.name} have an average cost of {self.average_cost} but they provide {self.usp}."



Hotel = accommodation("hotel", "comfort", 100)
Tent = accommodation("tent", "nature", 10)

total = Hotel + Tent

print(f'{Hotel.name} costs an average of {Hotel.average_cost} and provides {Hotel.usp}')



class Transport():

    number_of_transport = 0
    sum_of_costs = 0

    def __init__(self, name, environmental_impact, cost = 0, number_seats = 1):
        self.name = name
        self.environmental_impact = environmental_impact
        self.cost = cost
        self.number_seats = number_seats
        Transport.number_of_transport += 1
        Transport.sum_of_costs += cost


    @staticmethod
    def average_costs():
        avg = Transport.sum_of_costs / Transport.number_of_transport
        return avg

    def __str__(self):
        return f"{self.name} costs {self.cost} to transport {self.number_seats} people and has a {self.environmental_impact} environmental impact"


car = Transport("car", "high", 40, 5)
bike = Transport("bike", "low", 15, 1)
minivan = Transport("minivan", "high", 60, 9)
cost = Transport.average_costs()
print("The average cost for our modes of transport is:", cost)

print("The number of different types of transport are: ", Transport.number_of_transport)
print(car)
print(bike)
print(minivan)




'''


        total_cost = 0
        Transport.number_of_transport += 1
        for i in Transport:
            total_cost.append(Transport)

    def __str__(self):
        return f'{self.complete}'

'''

