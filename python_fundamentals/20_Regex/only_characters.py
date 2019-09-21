'''
https://www.w3resource.com/python-exercises/re/

Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
'''

# import re, which is used when working with regular expressions
import re
characters = re.compile(r'[\w]')

#gather user input to check
user_input = input("Enter something:")

# function to take a parameter and search to see if each part of the string is in characters. Characters is any english character
def checker(x):
    not_in_list = []
    for chars in x:
        string = characters.search(chars)  #searches all the characters in the variable defined above and checks against individual characters in user input
        if not string:                     #if user has entered something that isn't in characters
            not_in_list.append(chars)      # add it to the empty list

    return not_in_list                      # return out of the function anything that has been identified as not in characters


output = checker(user_input)
print(output)
# print(type(user_input))