'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]


new_sizes = [s +" " + c for c in colors for s in sizes]
print(f"our new store stocks: {new_sizes}")
