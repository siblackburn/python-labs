'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

output = []

for numbers in range(1,100):
    if numbers % 2 != 0:
        print(numbers)