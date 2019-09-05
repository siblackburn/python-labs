'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

#method 1:

numbers = input("enter ten whole numbers: ").split()

numbers_list = list(numbers)

print(numbers_list)

print(numbers_list[3], numbers_list[5], numbers_list[7], numbers_list[9])
print(numbers_list[8], numbers_list[6], numbers_list[4], numbers_list[2], numbers_list[0])
