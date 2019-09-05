'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

string_input = input("Tell me something about Python")
symbol = input("enter a symbol")

print(string_input.replace(string_input[0],symbol,10))