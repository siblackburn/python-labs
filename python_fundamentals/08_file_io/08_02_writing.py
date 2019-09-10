'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open("words.txt", "r") as reverse:
    output = list()
    for words in reverse:
        words = words.strip()
        output = words.split()

print(output)

output.reverse()

print(output)

string_output = str(output)

with open("words_reverse.txt", "w") as reverse:
    reverse.write(string_output)


