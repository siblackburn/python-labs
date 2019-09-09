'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''



def cube(x):
    return sq(x) * x

def sq(x):
    return x * x

def four(x):
    return cube(x) * x

number = 5

print(sq(number))
print(cube(number))
print(four(number))
