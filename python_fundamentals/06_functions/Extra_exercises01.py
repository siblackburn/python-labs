'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
https://www.w3resource.com/python-exercises/python-functions-exercises.php

1) take a list of numbers from the user
2) Turn the input into a list of integers. If it cannot be turned into a list of integers, ask the user to input numbers
3) Try to create a new list. If the new list fails for whatever reason, return an exception error
4) output the new list, with only unique numbers
'''

user_input = input("Please enter numbers, separated with a comma:")


def unique(numbers):
    output = []
    for n in numbers:
        if output.count(n) <= 0:
            output.append(n)

    return output

def new_function(numbers):
    if numbers[0] > 5:
        return f"Your number is > 5"
    else:
        return f"something else!!"




try:
    list_input = list(map(int, user_input.split(",")))
    # print(list_input)

except TypeError:
    print("You didn't enter whole numbers!")
    user_input = input("Please enter more than 5 numbers:")

except ValueError:
    print("did you enter letters instead?")
    user_input = input("Please enter more than 5 numbers:")

except Exception:
    print("something went wrong")
    user_input = input("Please enter more than 5 numbers:")

else:
    unique_list = unique(user_input)
    print(f"here's all the numbers you entered {unique_list}")











