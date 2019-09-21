'''
20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs. Go to the editor

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
'''

import re

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = "lazy"

test = re.search(searched_words, sample_text)

print(f"the text '{searched_words.upper()}' is located between the following characters in '{sample_text}': {test.span()}")
