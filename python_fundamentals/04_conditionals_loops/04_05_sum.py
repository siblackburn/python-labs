'''
Take two numbers from the user, an upper and lower bound.
Using a loop, calculate the sum of all numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:

The sum is: 5050
'''

lower = int(input("Enter a lower number:"))
upper = int(input("Enter an upper number:"))

output = int()

for number in range(lower, upper+1):
    output += number

print(output)