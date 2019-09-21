'''
6. Write a Python program that matches a string that has an a followed by two to three 'b'
'''


import re

user_input = input("Enter a string:")

def search_func(x):
    s = re.search("ab{2,3}", user_input)
    if s:
        return "match"
    else:
        return "no match"


output = search_func(user_input)
print(output)
