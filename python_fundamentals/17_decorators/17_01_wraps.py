'''
Write a decorator function that wraps text passed to it in a html <p> tag.
https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

I followed this tutorial: https://www.python-course.eu/python3_decorators.php

'''
#func could be anything. We're passing something into the decorator function and THEN using it

def decorator(func):        # So this is saying our decorator function takes another function as a parameter? yes!!
    def wrapper(x):         # Works only when decortor functin gets called. Wrapper gets passed func as a local variable. Need to be able to pass arguments into the wrapper function. Because html has 1 argyment, wrapper function also need 1 argument
        res = func(x)       # Why does this work? func is htmltag that is being passed in through decorator function.
        print(f"<p> {res} </p>")
    return wrapper          # This is returning for decorator. Which is the function wrapper
# wrapper function would be a good place to use *args so we can pass in as many arguments as we want

@decorator
def htmltag(text):          # This is the initial function
    return text.upper()     # Whatever the initial function does


# greeting = htmltag("hi")
# print(greeting)
# print(type(greeting))

greeting2 = decorator(htmltag)    #long hand version of syntactic sugar
# print(greeting2)
greeting2("This is greeting2")

# htmltag("this is html")





