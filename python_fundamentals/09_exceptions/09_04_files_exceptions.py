'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

with open("C:/Users/sibla/Documents/CodingNomads/labs/python_fundamentals/09_exceptions/books/war_and_peace.txt", encoding="utf8") as wap:
    # contents = wap.read()
    # print(contents)
    pass


with open("C:/Users/sibla/Documents/CodingNomads/labs/python_fundamentals/09_exceptions/books/crime_and_punishment.txt", "w") as cap:
    cap.write("hi")
    cap.close()

first_letters = []
with open("C:/Users/sibla/Documents/CodingNomads/labs/python_fundamentals/09_exceptions/books/crime_and_punishment copy.txt", encoding="utf8") as cap2:
    print(cap2.read(2))

    # for words in cap2:
    #     first_letters.append(cap2[0])
    # print(first_letters)

'''
import fileinput
import sys

files = fileinput.input("C:/Users/sibla/Documents/CodingNomads/labs/python_fundamentals/09_exceptions/books")
output = ()

for words in files:
    if 1 > 0:
        pass
'''

