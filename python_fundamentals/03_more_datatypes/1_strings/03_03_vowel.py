'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''


string_input = input("Tell me something you did today:")

vowels = "AEIOUaeiou"
count = 0

for number in string_input:
    if number == "a":
        count += 1
    if number == "i":
        count += 1
    if number == "o":
        count += 1
    if number == "u":
        count += 1

print(count)


