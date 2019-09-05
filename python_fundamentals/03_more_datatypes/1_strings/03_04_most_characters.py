'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

try1 = input("Write a word")
try2 = input("Write another")
try3 = input("Write a final word")

length1 = len(try1)
length2 = len(try2)
length3 = len(try3)


if length1 == max(length1, length2, length3):
    print("The longest word is: ", try1)

if length2 == max(length1, length2, length3):
    print("The longest word is: ", try2)

if length3 == max(length1, length2, length3):
    print("The longest word is: ", try3)