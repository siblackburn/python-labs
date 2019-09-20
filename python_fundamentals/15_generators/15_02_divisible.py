'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

gen = (i for i in range(1,20000))

for i in gen:
    if i % 1111 == 0:
        print(i)
