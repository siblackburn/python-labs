'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''


name = input("Type your name:")

first = name[0]
print(first)

new_name = name.replace(first,"")

print(new_name,first,"ay")