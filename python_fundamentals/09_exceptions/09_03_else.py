'''
Write a script that demonstrates a try/except/else.

'''

while True:

    try:

        word = input("Type out a long word: ")
        letter = input("which letter in the word do you like best?")

        letter_count = word.count(letter)
        print(letter_count)
        if letter_count <= 0:
            print("you're supposed to choose a letter within the word you typed you spanner! try again")
        else:
            break

    except Exception:
        print("not sure how you messed this up.....")

    else:
        print(f" There are {letter_count} {letter}'s in the word {word}")
        break




'''
class MyCustomException(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise (MyCustomException(10))
except MyCustomException as error:
    print('A New Exception occurred:', error.value)
'''
