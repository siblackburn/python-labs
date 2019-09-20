'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

my_list = ["apple", "banana", "orange"]


def my_enumerate(fruits):
    for i in range(len(fruits)):
        print("{}, {}".format(i + 1, fruits[i]))

print(my_enumerate(my_list))