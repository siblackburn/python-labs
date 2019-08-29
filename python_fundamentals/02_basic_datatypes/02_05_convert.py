'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 10

print(type(x))
floaty_x = float(x)
print(type(floaty_x))

back_to_integer = int(floaty_x)
print(type(back_to_integer))

print(5//2)

likelihood = int(input("what is the likelihood of Kanye West becoming President?"))
while not likelihood in range(0,101):
    print("you've broken the game, fool!")
    break

impact = float(input("what will the cost to the world be?"))

cost = (likelihood/100) * impact

print("The expected value of Kanye West becoming President is $", cost)


