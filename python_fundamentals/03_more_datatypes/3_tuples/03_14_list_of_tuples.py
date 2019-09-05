'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

user_input = input("enter some text: ").split()
new_list = []

for letters in user_input:
    new_list.append(letters)

print(new_list)

print(type(new_list))

