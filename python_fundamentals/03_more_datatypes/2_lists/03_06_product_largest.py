'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
#method 1:

numbers = input("enter ten whole numbers: ").split()

numbers_list = list(numbers)

print(type(numbers_list))
print(numbers_list)

largest_number = max(numbers_list)
print("The largest number is: ", largest_number)


count = 1

while count < len(numbers_list):
    count * numbers_list[count]
    count += 1

else:
    0
