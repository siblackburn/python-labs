'''
16. Write a Python program to remove leading zeros from an IP address.
'''

import re

ip_address = "192.021.901.01"

print(re.sub("0", "", ip_address))

