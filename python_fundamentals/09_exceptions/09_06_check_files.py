'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
numbers = []

with open("integers.txt", "r") as file:
    for contents in file.readlines():
        contents = contents.rstrip()
        numbers.append(contents)

    first_number = numbers[1]
    fourth_number = numbers[3]
    # print(type(first_number))

    try:

        calculation = fourth_number % first_number

    except TypeError:

        fourth_value = int(fourth_number)
        first_value = int(first_number)
        revised_calc = fourth_value % first_value
        print("The file doesn't seem to contain numbers...")
        print(f"but it's ok, we fixed it! The modulus of the fourth and first numbers is: {revised_calc}")

    except ValueError:
        print("value error!! uh oh...")

    except IOError:
        print("oops, couldn't read that file, please try a different filepath")

    else:
        print(f"the modulus of the fourth and first numbers is: {calculation}")


