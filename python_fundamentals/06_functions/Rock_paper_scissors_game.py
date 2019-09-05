'''
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner

Some Tips
Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass
'''
#Define user input and computer input. Also creating a dictionary at a global level so I can recall the dictionary during when outputting the answer

user_input = input("Please choose rock paper or scissors:")

from random import randrange
computer_input = randrange(2)

interpreter = {"scissors": 0, "rock": 1, "paper": 2}

# defining the function. Using if statements to make sure all conitions are met
def get_hand(hand):
    winner = []
    draw = "draw"
    user_win = "Congratulations you win!"
    computer_win = "unlucky you've lost"
    hand = interpreter[user_input]
    if hand == computer_input:
        winner.append(draw)
    elif hand == 0 and computer_input == 2:
        winner.append(user_win)
    elif computer_input == 0 and hand == 2:
        winner.append(computer_win)
    elif hand > computer_input:
        winner.append(user_win)
    elif computer_input > hand:
        winner.append(computer_win)
    else:
        print("Please choose rock paper or scissors")
    return winner



output = get_hand(user_input)
print("You played ", user_input)
for key, value in interpreter.items():
    if value == computer_input:
        print("The computer played ", key)
print(output)

