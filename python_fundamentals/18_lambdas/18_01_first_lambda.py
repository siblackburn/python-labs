'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''

u1 = int(input("enter a number"))
u2 = int(input("enter another number"))
u3 = int(input("enter a final number"))

numbers_list = [u1, u2, u3]
# print(type(numbers_list))
# print(numbers_list)

output = (lambda x: x[0] + x[1] + x[2])

print(output(numbers_list))

