'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

x = "hello"
y = "world"

import unittest


class Testing(unittest.TestCase):

    def test_myname(self):
        try:
            x // y
        except TypeError:
            print("Ooops typerror again")

        try:
            z = x + " " + y
        except Exception:
            print("not sure why we can't add these two beauties")
        else:
            print(z)