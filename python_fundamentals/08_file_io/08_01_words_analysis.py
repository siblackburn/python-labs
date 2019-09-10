'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open("words.txt", "r") as example:
    output = list()
    for words in example:
        words = words.strip()
        output = words.split()


    print("checking output type: ", type(output))
    print("checking the output: ", output)

shortest = []
longest = []
min_length = len(min(output, key=len))
max_length = len(max(output, key=len))

print("min length is: ", min_length)
print("max length is: ", max_length)

for entries in output:
    if len(entries) == min_length:
        shortest.append(entries)
    if len(entries) == max_length:
        longest.append(entries)


print("The shortest entry is: ", shortest)
print("The longest entry is: ", longest)
print(f'There are {len(output)} words in the file')