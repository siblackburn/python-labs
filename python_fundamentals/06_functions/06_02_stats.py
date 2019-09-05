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
