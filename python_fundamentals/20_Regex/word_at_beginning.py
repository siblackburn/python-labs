'''
10. Write a Python program that matches a word at the beginning of a string.
'''

import re

characters = re.compile(r'^\w+')

sentence = ["Hello", "this", "is", "a", "TEST", "d0", "not", "print", " output"]


def beginning_with_func(x):
    sanitised = []
    for words in sentence:
        test = re.search(characters, words)
        if test:
            sanitised.append(words)

    return sanitised


output = beginning_with_func(sentence)
print(output)