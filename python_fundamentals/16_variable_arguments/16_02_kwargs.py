'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_function(**things):
    for k, v in things.items():
        print(k, v)

my_function(item1='hi', item2='hello')