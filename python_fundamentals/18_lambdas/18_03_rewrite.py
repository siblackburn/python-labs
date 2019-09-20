'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])


output = lambda x: [(x.startswith("D")) for x in names] # x is so lambda can accept an argument. the for loop has to be contained in square brackets to work
print(output(names))
