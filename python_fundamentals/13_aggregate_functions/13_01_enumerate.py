'''
Demonstrate the use of the .enumerate() function.
'''
'''
courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

for i, c in enumerate(courses):
    print(f"{i}: {c} python")

for i in range(len(courses)):
    print(f"{i}: {courses[i]} python")
'''

my_list = ["apple", "banana", "orange"]

obj1 = list(enumerate(my_list, 1))

print(obj1)


