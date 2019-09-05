'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

number = int(input("enter a number:"))

mod = number % 3

if mod == 0:
    print("number is divisble by 3")

else:
    print("number is not divisble by 3")