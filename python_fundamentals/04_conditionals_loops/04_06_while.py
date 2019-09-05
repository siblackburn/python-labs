'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

number = 1

while number in range(1,1000):
    if number % 5 == 0:
        print(number)
    number += 1
