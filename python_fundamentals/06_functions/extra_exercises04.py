'''
Let's use functions to calculate your trip's costs:

Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.
Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.
https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/functions/exercises_functions.html
'''


# Get integer inputs from user
nights = int(input("How many nights is your trip"))
hotel_cost = int(input("how much does your hotel cost per night?"))
plane_cost = int(input("how much were your plane tickets?"))
transport_cost = int(input("how much is your rental car per day?"))

# Define a function that takes 4 parameters. Calculate total cost and average cost
def trip(n, h, p, t):
    total_accommodation_cost = hotel_cost * nights
    total_transport_cost = transport_cost * (nights + 1)
    total_cost = total_accommodation_cost + total_transport_cost + plane_cost
    average_cost = total_cost / nights

    return total_cost, average_cost

# The two returns from the function take input arguments from the four user inputs
total, average = trip(nights, hotel_cost, plane_cost, transport_cost)

print(f"Your total trip cost was: {total} and average cost per night is: {average}")





