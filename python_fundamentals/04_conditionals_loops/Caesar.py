secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


text = ""

for characters in secret:
    pos = ord(characters)
    new_pos = pos + cipher
    text += chr(new_pos)

print(text)
