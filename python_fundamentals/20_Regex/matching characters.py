'''
https://www.w3resource.com/python-exercises/re/
2. Write a Python program that matches a string that has an a followed by zero or more b's.
'''


import re

user_input = input("Enter something")

def searching_func(x):
    s = re.search("ab*?", user_input)
    if s:
        return "match"
    else:
        return "no match"



output = searching_func(user_input)
print(output)



