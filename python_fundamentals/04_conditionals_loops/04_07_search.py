'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

number = int(input("Enter a number between 0 and 1000000000:"))

if number <0 or number >1000000000:
    print("invalid number, please choose a number between 0 and 1,000,000,000")

guess = 0

while guess <= number:
    if guess == number:
        print(guess)
        break
    else:
        guess += 1
