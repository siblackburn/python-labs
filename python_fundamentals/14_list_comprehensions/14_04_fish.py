'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

just_fish = [fish for fish in fish_tuple if fish.count("fish")>0]

print(just_fish)