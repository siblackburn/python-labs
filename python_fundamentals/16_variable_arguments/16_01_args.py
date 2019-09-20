'''
Write a script with a function that demonstrates the use of *args.

'''


def my_function(*listings):
    for i in listings:
        print(i)


my_function("Hello", "this", "is", "args")
