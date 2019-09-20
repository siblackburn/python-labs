'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
# How can I import this from 17_01 without copying and pasting?
# eg. import "webpage_generator_task.py" works but import 17_01 doesn't as it starts with a number


def decorator(func):
    def wrapper(x):
        res = func(x)
        print(f"<{user_tag}> {res} /<{user_tag}>") # don't use global variables!
    return wrapper

@decorator
def htmltag(text):
    return text.upper()

user_text = input("enter a word")
user_tag = input("Enter a tag")

output = htmltag(user_text)