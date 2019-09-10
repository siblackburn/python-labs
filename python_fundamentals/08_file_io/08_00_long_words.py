'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

# make a file and write a sentence to it
with open("words.txt", "w") as example:
    example.write("This is a random sentence containing abcdefghijln;kjnkjn;kjn;kjn;jknklmnopqrstuvwxyz")

#open file back up and split individual words into a list, not including whitespace
with open("words.txt", "r") as example:
    output = list()
    for words in example:
        words = words.strip()
        output = words.split()

#checking output
    print(type(output))
    print("What does the list look like once the words have been split out", output)

# Find which words in the list have more than 20 characters
    long_words = []
    print("test for long words blank list", long_words)
    for i in output:
        if len(i) > 20:
            long_words.append(i)


    print(type(i))

    print(len(i))
    print(long_words)


'''
example of just reading all the content in the words.txt file
with open("words.txt", "r") as example:
    contents = example.read()
    print(contents)
'''

