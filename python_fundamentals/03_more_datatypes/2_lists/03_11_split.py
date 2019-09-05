'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

text = input("Name some fruit: ").split()

text_list = list(text)
max_fruit = []

for fruits in text_list:
    if text_list.count(fruits) == #the fruit with the highest count
        max_fruit.append(fruits)

print(max_fruit)
