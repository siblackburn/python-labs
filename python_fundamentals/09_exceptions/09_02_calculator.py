'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


while True:

    try:

        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number:"))
        break
        # if type(number1) == int and type(number2) == int:
        #     break
    except ValueError:
        print("You should have entered 2 numbers. PLease try again")
        print(ValueError)




calc = number2 // number1

print(calc)
