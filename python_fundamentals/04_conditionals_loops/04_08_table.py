'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
#There must be an easier way to do this!!

output = 0
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

while output < 10:
    L1.append(output)
    output += 1

while output <20:
    L2.append(output)
    output += 1

while output <30:
    L3.append(output)
    output += 1

while output <40:
    L4.append(output)
    output += 1

while output <50:
    L5.append(output)
    output += 1

print(L1)
print(L2)
print(L3)
print(L4)
print(L5)

