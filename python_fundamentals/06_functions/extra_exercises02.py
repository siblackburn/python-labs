'''
14. Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Click me to see the sample solution
https://www.w3resource.com/python-exercises/python-functions-exercises.php

'''

from string import ascii_lowercase

user = input("Enter a Pangram: ")

def pangram(sentence):
    user_lower = user.lower()
    missing_letters = []
    for letters in ascii_lowercase:
        letter_count = user_lower.count(letters)
        if letter_count <= 0:
            missing_letters.append(letters)

    return missing_letters

output = pangram(user)

if len(output) > 0:
    print(f"you were missing the following letters {output}")

else:
    print("well done, that was a pangram")


