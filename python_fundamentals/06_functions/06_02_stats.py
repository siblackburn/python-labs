'''
Write a script that takes in a list and finds the max, min, average and sum.

script = input("enter 5 numbers: ")
numbers = list(map(int,script.split(" ")))


print("you entered: ", numbers)

while len(numbers) != 5:
    print("You need to enter 5 numbers: ")
    script = input("enter 5 numbers: ")

else:
    def stats(bob):
        maximum = max(numbers)
        minimum = min(numbers)
        avg = sum(numbers) / len(numbers)
        return minimum, maximum, avg

x, y, z = stats(script)
print("The minimum value is:", x)
print("The maximum value is:", y)
print("the average value is:", z)


'''

script = input("enter 5 numbers: ")

def stats(numbers):
    numbers = list(map(int, script.split(" ")))
    maximum = max(numbers)
    minimum = min(numbers)
    avg = sum(numbers) / len(numbers)
    return minimum, maximum, avg

x, y, z = stats(script)
print("The minimum value is:", x)
print("The maximum value is:", y)
print("the average value is:", z)


'''
How can I then use the same function to work on a different input (e.g. user_input2)?
Could put the function in a for loop, looking up inputs thar are in a list

def a function that does something(and what you want to do it on):
    some calculation involving the inputs you want to do it on
    return the outputs x, y, z

The output I want to take outside the function = the function(my inputs)
print(the output)
    

'''