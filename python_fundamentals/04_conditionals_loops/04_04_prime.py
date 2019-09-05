'''
Print out every prime number between 1 and 100.

'''

output = []

for number in range(1,100):
    for lower_number in range(2,number - 1):
        if number % lower_number == 0:
            break

    else:
        if output.count(number) < 1:
            output.append(number)
        else:
            break

print(output)