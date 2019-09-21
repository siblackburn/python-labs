'''
9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

'''

import re

characters = re.compile(r'a.*?b$')
user_input = input("enter a string:")


def ending_fun(x):
    string_search = characters.findall(user_input)

    return string_search

output = ending_fun(user_input)
print(output)
