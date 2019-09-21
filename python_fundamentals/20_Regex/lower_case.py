'''
7. Write a Python program to find sequences of lowercase letters joined with a underscore.
'''

import re

characters = re.compile(r'^[a-z]+_[a-z]+')
user_input = input("enter a string:")


def search_func(x):
    string_search = characters.findall(user_input)

    return string_search


output = search_func(user_input)
print(output)



