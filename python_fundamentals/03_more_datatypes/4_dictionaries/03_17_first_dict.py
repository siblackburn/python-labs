'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

dictionary = dict()

for values in range(1,10):
    print(dictionary)
    dictionary[values] = values ** 2

print(dictionary)

print(type(dictionary))

'''dictionary key and value being added at the same time
dict[key] = value
'''