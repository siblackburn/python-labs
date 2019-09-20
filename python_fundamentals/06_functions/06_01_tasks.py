'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

user = int(input("input a number"))
mod1 = 4
mod2 = 7

while user < 0 or user > 1000000000:
    print("number must be between 0 and 1000000000")
    user = int(input("input a number"))
else:

    def test(n):
        if user % mod1 == 0 or user % mod2 == 0:
            print("TRUE")
        else:
            print("FALSE")
        return

output = test(user)
print(output)

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results


